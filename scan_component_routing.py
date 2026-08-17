#!/usr/bin/env python3
"""Audit the first-band component-routing hypothesis on a height box."""

from __future__ import annotations

import argparse
from itertools import combinations
from math import gcd

import lonely_runner_h7 as lrc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runners", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    args = parser.parse_args()

    modulus = args.runners + 1
    targeted = rank_deficient = failures = 0
    for speeds in combinations(range(1, args.height + 1), args.runners):
        if gcd(*speeds) != 1 or not any(speed % modulus == 0 for speed in speeds):
            continue
        targeted += 1
        if (
            lrc.bounded_relation_rank(speeds, max_coefficient=2)
            >= args.runners - 1
        ):
            continue
        rank_deficient += 1
        witness = lrc.first_band_component_routing_witness(speeds)
        if witness is None:
            failures += 1
            print("failure", ",".join(map(str, speeds)), sep="\t")

    print(
        "summary",
        args.runners,
        args.height,
        targeted,
        rank_deficient,
        failures,
        sep="\t",
    )


if __name__ == "__main__":
    main()
