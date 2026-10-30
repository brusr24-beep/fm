"""Measure the pieces that make up the RTP, to help tune config.json.

Prints base game RTP (without free spins), free spins trigger rate,
average free spins win and the total. Paytable values scale every win
linearly, so the suggested scale brings the total to the target RTP.

Usage: python tune.py [--spins N] [--fs N] [--target 0.96]
"""

import argparse
import statistics

from engine import Game


def measure(game, spins, fs_rounds):
    base_total, triggers, awards = 0.0, 0, []
    for _ in range(spins):
        heights = [game.min_rows] * game.reels
        grid = game.draw_grid("base", heights)
        win, scatters = game.tumble("base", grid, heights)
        base_total += win
        if scatters >= 3:
            triggers += 1
            awards.append(game.fs_award[min(scatters, 6)])
    fs = [game.free_spins(game.rng.choice(awards) if awards else 8) for _ in range(fs_rounds)]
    bought = [game.free_spins(game.fs_award[3]) for _ in range(fs_rounds)]
    return base_total / spins, triggers / spins, statistics.mean(fs), statistics.mean(bought)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--spins", type=int, default=100_000)
    p.add_argument("--fs", type=int, default=3_000)
    p.add_argument("--target", type=float, default=0.96)
    p.add_argument("--seed", type=int, default=7)
    a = p.parse_args()
    game = Game(seed=a.seed)
    base, rate, fs_avg, bought_avg = measure(game, a.spins, a.fs)
    total = base + rate * fs_avg
    print(f"base game RTP    {base * 100:.2f}%")
    print(f"trigger rate     1 in {1 / rate:,.0f}" if rate else "trigger rate     never")
    print(f"free spins avg   {fs_avg:.1f}x  ({rate * fs_avg * 100:.2f}% of RTP)")
    print(f"total RTP        {total * 100:.2f}%")
    print(f"pay scale        x{a.target / total:.4f} to reach {a.target * 100:.1f}%")
    # After scaling the bought round averages bought_avg * scale, so the
    # cost that returns the target RTP is bought_avg * scale / target.
    print(f"bought FS avg    {bought_avg:.1f}x -> buy cost {bought_avg / total:.1f}x "
          f"after scaling, for {a.target * 100:.1f}% RTP")
