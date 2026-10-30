"""Candy Riot game logic.

Grid layout: grid[reel] is a list of symbols, index 0 is the top row.
All wins are expressed as multiples of the total bet.

Mechanics:
  * Burst Ways - ways pays, left to right, 3+ adjacent reels. Winning
    symbols burst, every reel that lost symbols grows by one row (up to
    max_rows) and new symbols drop in. Repeats until there is no win.
  * Shove Wilds - a wild landing on reels 2-5 shoves out to fill the whole
    reel and gets a multiplier. Multipliers of wild reels in a win add up.
    A wild reel bursts together with the win it takes part in.
  * Free spins - reel heights are kept between spins instead of resetting.
"""

import json
import random
from pathlib import Path

CONFIG_PATH = Path(__file__).with_name("config.json")


def load_config(path=CONFIG_PATH):
    with open(path) as f:
        return json.load(f)


class Game:
    def __init__(self, config=None, seed=None):
        self.cfg = config or load_config()
        self.rng = random.Random(seed)
        self.reels = self.cfg["reels"]
        self.min_rows = self.cfg["min_rows"]
        self.max_rows = self.cfg["max_rows"]
        self.wild_reels = set(self.cfg["wild_reels"])
        self.paying = [s for s, d in self.cfg["symbols"].items() if d["kind"] in ("low", "high")]
        self.pay = {s: {int(k): v for k, v in p.items()} for s, p in self.cfg["paytable"].items()}
        self.mult_values = [int(k) for k in self.cfg["wild_multipliers"]]
        self.mult_weights = list(self.cfg["wild_multipliers"].values())
        self.fs_award = {int(k): v for k, v in self.cfg["free_spins_award"].items()}
        self.fs_retrigger = {int(k): v for k, v in self.cfg["free_spins_retrigger"].items()}
        # Per mode, per reel symbol tables; wilds only exist on wild reels.
        self.tables = {}
        for mode, weights in self.cfg["weights"].items():
            per_reel = []
            for r in range(self.reels):
                syms = [s for s in weights if s != "wild" or r in self.wild_reels]
                per_reel.append((syms, [weights[s] for s in syms]))
            self.tables[mode] = per_reel

    # -- drawing -----------------------------------------------------------

    def draw(self, mode, reel, n):
        syms, weights = self.tables[mode][reel]
        return self.rng.choices(syms, weights, k=n)

    def draw_grid(self, mode, heights):
        return [self.draw(mode, r, h) for r, h in enumerate(heights)]

    # -- evaluation ----------------------------------------------------------

    def evaluate(self, grid, wild_mult):
        """Return a list of wins: (symbol, length, ways, multiplier, amount)."""
        wins = []
        for s in self.paying:
            ways, mult, length = 1, 0, 0
            for r in range(self.reels):
                if r in wild_mult:
                    count = len(grid[r])
                    mult += wild_mult[r]
                else:
                    count = grid[r].count(s)
                if count == 0:
                    break
                ways *= count
                length += 1
            if length >= 3:
                mult = max(mult, 1)
                wins.append((s, length, ways, mult, self.pay[s][length] * ways * mult))
        return wins

    def shove_wilds(self, grid, wild_mult, events):
        for r in self.wild_reels:
            if r not in wild_mult and "wild" in grid[r]:
                wild_mult[r] = self.rng.choices(self.mult_values, self.mult_weights)[0]
                grid[r] = ["wild"] * len(grid[r])
                if events is not None:
                    events.append({"type": "shove", "reel": r, "mult": wild_mult[r]})

    def tumble(self, mode, grid, heights, events=None):
        """Run the burst/grow/refill loop. Mutates grid and heights."""
        wild_mult = {}
        total = 0.0
        while True:
            self.shove_wilds(grid, wild_mult, events)
            wins = self.evaluate(grid, wild_mult)
            if not wins:
                break
            amount = sum(w[4] for w in wins)
            total += amount
            burst = [set() for _ in range(self.reels)]
            for s, length, *_ in wins:
                for r in range(length):
                    if r in wild_mult:
                        burst[r].update(range(len(grid[r])))
                    else:
                        burst[r].update(i for i, x in enumerate(grid[r]) if x == s)
            for r in [r for r in wild_mult if burst[r]]:
                del wild_mult[r]
            if events is not None:
                events.append({
                    "type": "win",
                    "wins": [dict(zip(("symbol", "length", "ways", "mult", "amount"), w)) for w in wins],
                    "burst": [sorted(b) for b in burst],
                })
            added = [0] * self.reels
            for r in range(self.reels):
                if not burst[r]:
                    continue
                kept = [x for i, x in enumerate(grid[r]) if i not in burst[r]]
                heights[r] = min(heights[r] + 1, self.max_rows)
                added[r] = heights[r] - len(kept)
                grid[r] = self.draw(mode, r, added[r]) + kept
            if events is not None:
                events.append({"type": "refill", "grid": [list(c) for c in grid],
                               "heights": list(heights), "added": added})
        scatters = sum(c.count("ticket") for c in grid)
        return total, scatters

    # -- rounds --------------------------------------------------------------

    def free_spins(self, spins, events=None):
        heights = [self.min_rows] * self.reels
        total, played = 0.0, 0
        while played < spins:
            played += 1
            grid = self.draw_grid("free", heights)
            if events is not None:
                events.append({"type": "spin", "free": played, "of": spins,
                               "grid": [list(c) for c in grid], "heights": list(heights)})
            win, scatters = self.tumble("free", grid, heights, events)
            total += win
            if scatters >= 3:
                extra = self.fs_retrigger[min(scatters, 6)]
                spins += extra
                if events is not None:
                    events.append({"type": "retrigger", "extra": extra})
            if total >= self.cfg["max_win"]:
                break
        return total

    def play(self, mode="base", events=None):
        """Play one round. mode is 'base' or 'bonus' (bought free spins).

        Returns the win as a multiple of the base bet (not of the buy cost).
        """
        total = 0.0
        if mode == "base":
            heights = [self.min_rows] * self.reels
            grid = self.draw_grid("base", heights)
            if events is not None:
                events.append({"type": "spin", "grid": [list(c) for c in grid], "heights": list(heights)})
            total, scatters = self.tumble("base", grid, heights, events)
            if scatters >= 3:
                spins = self.fs_award[min(scatters, 6)]
                if events is not None:
                    events.append({"type": "trigger", "spins": spins})
                total += self.free_spins(spins, events)
        else:
            spins = self.fs_award[3]
            if events is not None:
                events.append({"type": "trigger", "spins": spins})
            total = self.free_spins(spins, events)
        return min(total, self.cfg["max_win"])
