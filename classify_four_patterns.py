#!/usr/bin/env python3
"""Replay the coefficient-two, four-coordinate ambient-pattern audit."""

from __future__ import annotations

import argparse
from collections import Counter

import lonely_runner_h7 as lrc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--exact",
        action="store_true",
        help="compute all 123 exact ambient maxima (several minutes)",
    )
    args = parser.parse_args()

    patterns = lrc.coefficient_relation_patterns(
        coordinate_count=4, max_coefficient=2, nullity=2
    )
    admissible = tuple(
        pattern
        for pattern in patterns
        if lrc.pattern_positive_distinct_witness(pattern) is not None
    )
    representatives = lrc.admissible_pattern_symmetry_representatives(
        coordinate_count=4, max_coefficient=2, nullity=2
    )
    print(f"relation_subspaces\t{len(patterns)}")
    print(f"positive_distinct\t{len(admissible)}")
    print(f"symmetry_classes\t{len(representatives)}")
    if not args.exact:
        return

    results = []
    print("class\tpattern\tambient_maximum\twitness")
    for index, pattern in enumerate(representatives, 1):
        value, witness = lrc.pattern_maximum_loneliness(pattern)
        results.append(value)
        print(f"{index}\t{pattern}\t{value}\t{witness}", flush=True)
    print("distribution")
    for value, count in sorted(Counter(results).items()):
        print(f"{value}\t{count}")


if __name__ == "__main__":
    main()
