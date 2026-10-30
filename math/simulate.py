"""Monte Carlo simulation of Candy Riot.

Usage: python simulate.py [--spins N] [--mode base|bonus] [--seed S]
"""

import argparse
import statistics
import time

from engine import Game


def run(mode, spins, seed):
    game = Game(seed=seed)
    cost = game.cfg["bonus_buy_cost"] if mode == "bonus" else 1
    fs_wins = []
    free_spins = game.free_spins

    def counted_free_spins(*args, **kwargs):
        win = free_spins(*args, **kwargs)
        fs_wins.append(win)
        return win

    game.free_spins = counted_free_spins
    wins = [game.play(mode) for _ in range(spins)]
    return game, cost, wins, fs_wins


def report(mode, spins, seed):
    start = time.time()
    game, cost, wins, fs_wins = run(mode, spins, seed)
    elapsed = time.time() - start
    total = sum(wins)
    rtp = total / (spins * cost)
    hits = sum(1 for w in wins if w > 0)
    sd = statistics.pstdev(wins) / cost
    print(f"mode           {mode}")
    print(f"rounds         {spins:,}  ({elapsed:.1f}s)")
    print(f"RTP            {rtp * 100:.2f}%  (+/- {1.96 * sd / spins ** 0.5 * 100:.2f}% at 95%)")
    print(f"hit rate       1 in {spins / max(hits, 1):.2f}")
    print(f"std deviation  {sd:.2f}")
    print(f"max win        {max(wins):,.2f}x")
    if mode == "base" and fs_wins:
        fs_rtp = sum(min(w, game.cfg["max_win"]) for w in fs_wins) / spins
        print(f"free spins     1 in {spins / len(fs_wins):,.0f}  "
              f"(avg {statistics.mean(fs_wins):.1f}x, {fs_rtp * 100:.2f}% of RTP)")
    for t in (100, 1000, 5000, game.cfg["max_win"]):
        n = sum(1 for w in wins if w >= t)
        print(f"  >= {t:>6,}x    {'1 in ' + format(spins / n, ',.0f') if n else 'never'}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--spins", type=int, default=200_000)
    p.add_argument("--mode", choices=("base", "bonus"), default="base")
    p.add_argument("--seed", type=int, default=1)
    a = p.parse_args()
    report(a.mode, a.spins, a.seed)
