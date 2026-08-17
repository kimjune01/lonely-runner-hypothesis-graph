#!/usr/bin/env python3
"""Replay the three-block first-band falsification scan for H71."""

from __future__ import annotations

import argparse
from fractions import Fraction

import lonely_runner_h7 as lrc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-block-size", type=int, required=True)
    parser.add_argument("--scale-multiple", type=int, default=5)
    args = parser.parse_args()
    if args.max_block_size < 3:
        parser.error("max-block-size must be at least three")
    if args.scale_multiple < 1:
        parser.error("scale-multiple must be positive")

    print(
        "block_size\tscale_start\tscale_end"
        "\tgrid_survivors\texact_survivors"
    )
    for block_size in range(3, args.max_block_size + 1):
        block_sum = block_size * (block_size + 1) // 2
        scale_start = block_sum + 1
        scale_end = args.scale_multiple * block_sum + 1
        runner_count = 3 * block_size
        threshold = Fraction(2, 2 * runner_count + 1)
        grid_survivors = 0
        exact_survivors = 0
        for scale in range(scale_start, scale_end + 1):
            speeds = tuple(
                multiplier * scale**power
                for power in range(3)
                for multiplier in range(1, block_size + 1)
            )
            if lrc.strict_band_edge_grid_cover_certificate(speeds) is None:
                continue
            grid_survivors += 1
            if lrc.loneliness_at_most(speeds, threshold=threshold):
                exact_survivors += 1
        print(
            f"{block_size}\t{scale_start}\t{scale_end}"
            f"\t{grid_survivors}\t{exact_survivors}"
        )


if __name__ == "__main__":
    main()
