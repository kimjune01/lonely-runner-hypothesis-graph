#!/usr/bin/env python3
"""Emit an exact TSV receipt for first-spectral-band relation hypotheses."""

from __future__ import annotations

import argparse
from fractions import Fraction

import lonely_runner_h7 as lrc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runners", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    parser.add_argument("--coefficient", type=int, default=2)
    args = parser.parse_args()

    print(
        "runners\theight\tspeeds\tmaximum_loneliness\trelation_rank"
        "\tcomponents\tpositive_seeds\tsigned_dissociated_seeds"
        "\ttwo_seed_appendable\thandoff_seeds\thandoff_seed_appendable"
        "\tpositive_tree\tambient_maximum"
        "\tambient_margin\tparameter_norm_squared_cutoff"
    )
    for speeds, loneliness in lrc.first_band_survivors(
        runner_count=args.runners,
        height=args.height,
    ):
        rank = lrc.bounded_relation_rank(
            speeds, max_coefficient=args.coefficient
        )
        components = lrc.bounded_relation_components(
            speeds, max_coefficient=args.coefficient
        )
        seeds, _ = lrc.positive_generation_certificate(
            speeds, max_coefficient=args.coefficient
        )
        signed_seeds, _ = lrc.bounded_dissociated_generation_certificate(
            speeds, max_coefficient=args.coefficient
        )
        appendable = lrc.bounded_appendability_certificate(
            speeds, max_coefficient=args.coefficient, seed_count=min(2, len(speeds))
        )
        handoff_seeds = lrc.handoff_seed_pair(
            speeds, delta=Fraction(1, args.runners + 1)
        )
        handoff_steps = (
            lrc.bounded_appendability_from_seeds(
                speeds,
                seeds=handoff_seeds,
                max_coefficient=args.coefficient,
            )
            if handoff_seeds is not None
            else None
        )
        tree = lrc.positive_triangular_relation_tree(
            speeds, max_coefficient=args.coefficient
        )
        pattern = lrc.bounded_relation_pattern(
            speeds, max_coefficient=args.coefficient
        )
        ambient = margin = cutoff = ""
        if len(pattern) == 2:
            ambient_value, _ = lrc.pattern_maximum_loneliness(pattern)
            margin_value = ambient_value - Fraction(1, args.runners + 1)
            ambient = str(ambient_value)
            margin = str(margin_value)
            if margin_value > 0:
                cutoff = str(
                    lrc.pattern_parameter_norm_squared_cutoff(
                        pattern, threshold=Fraction(1, args.runners + 1)
                    )
                )
        component_text = "|".join(
            ",".join(map(str, component)) for component in components
        )
        print(
            f"{args.runners}\t{args.height}\t{','.join(map(str, speeds))}"
            f"\t{loneliness}\t{rank}\t{component_text}\t{len(seeds)}"
            f"\t{len(signed_seeds)}\t{'yes' if appendable is not None else 'no'}"
            f"\t{','.join(map(str, handoff_seeds or ()))}"
            f"\t{'yes' if handoff_steps is not None else 'no'}"
            f"\t{'yes' if tree is not None else 'no'}"
            f"\t{ambient}\t{margin}"
            f"\t{cutoff}"
        )


if __name__ == "__main__":
    main()
