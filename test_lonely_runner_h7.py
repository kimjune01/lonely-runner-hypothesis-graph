import importlib.util
import csv
import itertools
import math
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).with_name("lonely_runner_h7.py")
SPEC = importlib.util.spec_from_file_location("lonely_runner_h7", MODULE_PATH)
lrc = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(lrc)


def test_cover_uses_exact_integer_arithmetic():
    # D = (k + 1)p = 28. At j = 1, v = 7 is exactly 1/4 away,
    # so the strict bad-time predicate must not count it as covered.
    assert not lrc.covers(v=7, j=1, k=3, p=7, denominator=4)
    assert lrc.covers(v=6, j=1, k=3, p=7, denominator=4)


def test_gcd_constraint_checks_every_omitted_speed():
    assert lrc.gcd_constraint((1, 2, 3), k=3, p=7)
    assert not lrc.gcd_constraint((2, 4, 5), k=3, p=7)


def test_reproduces_published_working_modulus():
    result = lrc.find_bad_cover(k=3, p=7, denominator=4)
    assert result is None


def test_reproduces_published_exception():
    result = lrc.find_bad_cover(k=6, p=17, denominator=7)
    assert result is not None
    assert len(result) <= 6
    assert lrc.gcd_constraint(result, k=6, p=17)
    assert lrc.covers_universe(result, k=6, p=17, denominator=7)


def test_smt_search_matches_backtracking_on_known_cases():
    assert lrc.find_bad_cover_smt(k=3, p=7, denominator=4) is None
    result = lrc.find_bad_cover_smt(k=6, p=17, denominator=7)
    assert result is not None
    assert lrc.gcd_constraint(result, k=6, p=17)
    assert lrc.covers_universe(result, k=6, p=17, denominator=7)


def test_k8_p43_certificate_replays():
    witness = (1, 7, 9, 45, 54, 63, 72, 117)
    assert lrc.gcd_constraint(witness, k=8, p=43)
    assert lrc.covers_universe(witness, k=8, p=43, denominator=9)


def test_unsat_core_is_named_and_replayable():
    core = lrc.unsat_core(k=3, p=7, denominator=4)
    assert "count_exactly_3" in core
    assert any(name.startswith("cover_j_") for name in core)
    assert lrc.replay_unsat_core(k=3, p=7, denominator=4, core=core)


def test_cadical_search_matches_calibration_cases():
    assert lrc.find_bad_cover_sat(k=3, p=7, denominator=4) is None
    result = lrc.find_bad_cover_sat(k=6, p=17, denominator=7)
    assert result is not None
    assert lrc.gcd_constraint(result, k=6, p=17)
    assert lrc.covers_universe(result, k=6, p=17, denominator=7)


def test_exports_dimacs_and_drup_certificate(tmp_path):
    cnf_path = tmp_path / "k3-p7.cnf"
    proof_path = tmp_path / "k3-p7.drup"
    metadata = lrc.export_unsat_certificate(
        k=3,
        p=7,
        denominator=4,
        cnf_path=cnf_path,
        proof_path=proof_path,
    )
    assert cnf_path.read_text().startswith("p cnf ")
    assert proof_path.read_text().rstrip().endswith("0")
    assert metadata["status"] == "UNSAT"
    assert metadata["proof_steps"] > 0


def test_only_three_is_a_nonredundant_gcd_prime_at_k8_p53():
    assert lrc.active_gcd_primes(k=8, p=53) == (3,)


def test_cadical_coverage_core_replays_on_calibration_case():
    core = lrc.unsat_coverage_core_sat(k=3, p=7, denominator=4)
    assert core
    assert all(1 <= j <= 14 for j in core)
    assert lrc.replay_coverage_core_sat(k=3, p=7, denominator=4, core=core)


def test_relaxed_cover_can_require_two_nonmultiples_before_boundary():
    result = lrc.find_cover_with_min_nonmultiples(
        k=8, p=11, denominator=9, prime=3, minimum=2
    )
    assert result is not None
    assert sum(v % 3 != 0 for v in result) >= 2
    assert lrc.covers_universe(result, k=8, p=11, denominator=9)


def test_canonical_dirichlet_cover_replays_across_boundary():
    canonical = tuple(9 * multiplier for multiplier in range(1, 9))
    for p in (43, 47, 53, 59, 67):
        assert lrc.covers_universe(canonical, k=8, p=p, denominator=9)


def test_cpsat_coverage_core_replays_on_calibration_case():
    core = lrc.unsat_coverage_core_cpsat(k=3, p=7, denominator=4)
    assert core
    assert all(1 <= j <= 14 for j in core)
    assert lrc.replay_coverage_core_cpsat(k=3, p=7, denominator=4, core=core)


def test_max_coverage_finds_a_complete_preboundary_cover():
    result, uncovered = lrc.max_coverage_candidate(
        k=8, p=11, denominator=9, prime=3, minimum_nonmultiples=2
    )
    assert len(result) == 8
    assert sum(v % 3 != 0 for v in result) >= 2
    assert uncovered == ()


def test_exact_coverage_size_formula_at_boundary():
    k, p = 8, 47
    limit = ((k + 1) * p) // 2
    for v in range(1, limit + 1):
        if v % p == 0:
            continue
        actual = sum(
            lrc.covers(v=v, j=j, k=k, p=p, denominator=9)
            for j in range(1, limit + 1)
        )
        assert actual == lrc.coverage_size(k=k, p=p, v=v)


def test_first_two_incidence_moments_do_not_determine_union():
    first = (23, 78, 86, 126, 138, 159, 183, 192)
    second = (12, 49, 57, 93, 102, 116, 144, 150)
    first_moments = lrc.selection_moments(first, k=8, p=47, denominator=9)
    second_moments = lrc.selection_moments(second, k=8, p=47, denominator=9)
    assert first_moments[:2] == second_moments[:2] == (371, 271)
    assert first_moments[2] == 184
    assert second_moments[2] == 190


def test_order_three_fourier_counts_at_first_boundary():
    assert lrc.coverage_residue_counts(v=1, k=8, p=47, modulus=3) == (31, 31, 31)
    assert lrc.coverage_residue_counts(v=3, k=8, p=47, modulus=3) == (33, 30, 30)
    assert lrc.coverage_residue_counts(v=9, k=8, p=47, modulus=3) == (33, 33, 33)


def test_single_character_fourier_bound_has_large_slack():
    selection = (27, 42, 96, 157, 162, 176, 189, 207)
    ratio, character = lrc.max_fourier_positivity_ratio(
        selection, k=8, p=47, denominator=9
    )
    assert character != 0
    assert ratio < 0.251


def test_boundary_has_an_admissible_one_gap_cover():
    selection = (33, 46, 57, 149, 150, 160, 206, 207)
    assert lrc.gcd_constraint(selection, k=8, p=47)
    assert lrc.uncovered_times(selection, k=8, p=47, denominator=9) == (181,)


def test_unit_action_normalizes_the_one_gap_cover():
    selection = (33, 46, 57, 149, 150, 160, 206, 207)
    normalized = lrc.scale_speeds(selection, multiplier=181, k=8, p=47)
    assert normalized == (51, 62, 78, 103, 134, 165, 180, 196)
    assert lrc.uncovered_times(normalized, k=8, p=47, denominator=9) == (1,)


def test_special_time_p_forces_a_multiple_of_nine():
    for speed in range(1, 212):
        if speed % 47 == 0:
            continue
        assert lrc.covers(v=speed, j=47, k=8, p=47, denominator=9) == (
            speed % 9 == 0
        )


def test_normalized_one_gap_covers_are_isolated_by_one_exchange():
    fixtures = (
        ((51, 62, 78, 103, 134, 165, 180, 196), 3),
        ((54, 58, 110, 112, 139, 166, 168, 197), 4),
    )
    for selection, expected_minimum in fixtures:
        assert lrc.uncovered_times(selection, k=8, p=47, denominator=9) == (1,)
        exchanges = lrc.best_gap_closing_exchanges(
            selection, gap=1, k=8, p=47, denominator=9
        )
        assert len(exchanges[0][2]) == expected_minimum
        assert all(len(new_gaps) == expected_minimum for _, _, new_gaps in exchanges)


def test_mod_p_fibers_reduce_to_small_phase_patterns():
    for residue in range(1, 47):
        assert len(lrc.coverage_fiber(v=1, residue=residue, k=8, p=47)) == 2
    for speed in range(1, 212):
        if speed % 47 == 0:
            continue
        for residue in range(47):
            fiber = lrc.coverage_fiber(v=speed, residue=residue, k=8, p=47)
            common = __import__("math").gcd(speed, 423)
            if common == 1:
                assert len(fiber) == (1 if residue == 0 else 2)
            elif common == 3:
                assert len(fiber) in (0, 3)
                assert len({phase % 3 for phase in fiber}) <= 1
            elif common == 9:
                assert len(fiber) in (0, 9)


def test_local_phase_cover_requires_three_classes_with_two_unit_speeds():
    assert lrc.minimum_g3_phase_classes(unit_speeds=2) == 3
    assert lrc.minimum_g3_phase_classes(unit_speeds=3) == 1
    assert lrc.minimum_g3_phase_classes(unit_speeds=4) == 1
    assert lrc.minimum_g3_phase_classes(unit_speeds=5) == 0


def test_two_unit_fiber_obstruction_is_unsat():
    assert lrc.two_unit_fiber_obstruction_is_unsat(p=47)


def test_three_unit_fiber_obstruction_is_unsat():
    assert lrc.three_unit_fiber_obstruction_is_unsat(p=47)


def test_high_unit_exhaustive_verifier(tmp_path):
    compiler = shutil.which("clang++") or shutil.which("g++")
    if compiler is None:
        pytest.skip("a C++20 compiler is required for the exhaustive verifier")
    source = Path(__file__).with_name("verify_high_unit_branches.cpp")
    executable = tmp_path / "verify_high_unit_branches"
    subprocess.run(
        [compiler, "-O3", "-std=c++20", str(source), "-o", str(executable)],
        check=True,
    )
    expected = {4: 208104, 5: 37214, 6: 1311, 7: 23}
    for branch, count in expected.items():
        result = subprocess.run(
            [str(executable), "47", str(branch)],
            check=True,
            capture_output=True,
            text=True,
        )
        assert f"VERIFIED branch={branch} checked={count}" in result.stdout


def test_published_nine_runner_sieve_receipt_crosses_product_bound():
    receipt = Path(__file__).with_name("artifacts") / "nine-runner-sieve-replay.tsv"
    with receipt.open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))

    primes = tuple(int(row["p"]) for row in rows)
    assert len(primes) == 39
    assert primes[:3] == (47, 53, 59)
    assert primes[-3:] == (233, 239, 241)
    assert all(int(row["u_size"]) == 0 for row in rows)
    assert all(row["matches_published"] == "yes" for row in rows)
    assert all(
        p > 1 and all(p % divisor for divisor in range(2, math.isqrt(p) + 1))
        for p in primes
    )

    product = math.prod(primes)
    bound_numerator = 36**56
    bound_denominator = 8**8
    assert product * bound_denominator > bound_numerator


def test_counterexample_family_to_universal_grid_witness_conjecture():
    for r in range(1, 101):
        denominator, speeds, strict_witness = lrc.universal_grid_counterexample(r=r)
        assert denominator == 6 * r + 1
        assert speeds == (1, 3 * r)
        assert math.gcd(denominator, math.prod(speeds)) == 1
        assert min(lrc.fractional_distance(speed * strict_witness) for speed in speeds) > Fraction(1, 3)
        assert all(
            min(
                lrc.fractional_distance(Fraction(j * speed, denominator))
                for speed in speeds
            )
            < Fraction(1, 3)
            for j in range(denominator)
        )


@pytest.mark.parametrize(
    ("speeds", "expected"),
    [
        ((1, 2), Fraction(1, 3)),
        ((1, 3), Fraction(1, 2)),
        ((1, 4), Fraction(2, 5)),
        ((1, 2, 3), Fraction(1, 4)),
    ],
)
def test_exact_maximum_loneliness_at_critical_times(speeds, expected):
    assert lrc.maximum_loneliness(speeds) == expected


def test_height_sensitive_grid_bound_for_small_non_tight_tuples():
    for speeds in [(1, second) for second in range(2, 9)]:
        threshold = Fraction(1, len(speeds) + 1)
        if lrc.maximum_loneliness(speeds) <= threshold:
            continue
        first_denominator = lrc.height_sensitive_grid_bound(speeds)
        for denominator in range(first_denominator, first_denominator + 4):
            assert max(
                min(
                    lrc.fractional_distance(Fraction(j * speed, denominator))
                    for speed in speeds
                )
                for j in range(denominator)
            ) > threshold


def test_multi_fast_union_condition_certifies_small_tuples():
    for runner_count, height in [(4, 14), (5, 10)]:
        certified = 0
        for speeds in itertools.combinations(range(1, height + 1), runner_count):
            for fast_count in range(1, (runner_count + 1) // 2):
                if lrc.multi_fast_union_condition(speeds, fast_count=fast_count):
                    certified += 1
                    assert lrc.maximum_loneliness(speeds) >= Fraction(1, runner_count + 1)
        assert certified > 0

    for speeds in [(1, 2, 100, 101), (1, 2, 3, 120, 121)]:
        assert lrc.multi_fast_union_condition(speeds, fast_count=2)
        assert lrc.maximum_loneliness(speeds) >= Fraction(1, len(speeds) + 1)


@pytest.mark.parametrize(
    ("speeds", "delta", "expected"),
    [
        ((1,), Fraction(1, 3), Fraction(1, 3)),
        ((1, 2), Fraction(1, 5), Fraction(2, 5)),
        ((1, 3, 4), Fraction(1, 5), Fraction(1, 10)),
    ],
)
def test_exact_valid_time_measure(speeds, delta, expected):
    assert lrc.valid_time_measure(speeds, delta=delta) == expected


@pytest.mark.parametrize(
    ("speeds", "delta"),
    [
        ((1, 2), Fraction(2, 5)),
        ((1, 2, 3), Fraction(3, 10)),
    ],
)
def test_failed_threshold_has_relation_within_fourier_bound(speeds, delta):
    assert lrc.maximum_loneliness(speeds) < delta
    bound = lrc.fourier_relation_bound(len(speeds), delta=delta)
    relation = lrc.find_bounded_relation(speeds, max_coefficient=3)
    assert relation is not None
    assert max(map(abs, relation)) <= bound
    assert sum(coefficient * speed for coefficient, speed in zip(relation, speeds)) == 0


def test_dissociated_riesz_argument_crosses_lrc_threshold_at_eighteen():
    assert not lrc.dissociated_riesz_forces_lrc(17)
    assert lrc.dissociated_riesz_forces_lrc(18)
    assert all(lrc.dissociated_riesz_forces_lrc(n) for n in range(18, 200))


def test_riesz_constant_term_is_one_for_coefficient_one_dissociated_tuple():
    assert lrc.riesz_constant_term((5, 7, 11)) == 1
    assert lrc.riesz_cover_ratio((5, 7, 11)) == Fraction(1, 3)


def test_single_three_term_circuit_has_exact_riesz_obstruction():
    assert lrc.riesz_constant_term((1, 2, 3)) == Fraction(3, 4)
    assert lrc.riesz_cover_ratio((1, 2, 3)) == Fraction(1, 4)


@pytest.mark.parametrize("speeds", [(1, 2), (1, 2, 3), (1, 2, 3, 4)])
def test_tight_tuple_relation_is_within_fourier_bound(speeds):
    delta = Fraction(1, len(speeds) + 1)
    assert lrc.maximum_loneliness(speeds) == delta
    relation = lrc.find_bounded_relation(speeds, max_coefficient=3)
    assert relation is not None
    assert max(map(abs, relation)) <= lrc.fourier_relation_bound(
        len(speeds), delta=delta
    )


@pytest.mark.parametrize(
    "speeds",
    [
        (1, 2, 3),
        (1, 2, 6),
        (1, 3, 4),
        (1, 5, 6),
        (2, 3, 5),
        (1, 2, 3, 4),
        (1, 2, 3, 8),
        (1, 3, 4, 7),
        (3, 4, 7, 11),
        (1, 3, 4, 5, 7, 13, 18),
    ],
)
def test_first_spectral_band_fixtures_have_connected_two_relations(speeds):
    runner_count = len(speeds)
    assert lrc.maximum_loneliness(speeds) <= Fraction(2, 2 * runner_count + 1)
    assert lrc.bounded_relation_components(speeds, max_coefficient=2) == (tuple(range(runner_count)),)


def test_connected_relation_hypothesis_needs_first_band_cutoff():
    speeds = (1, 2, 18)
    assert lrc.maximum_loneliness(speeds) == Fraction(6, 19) < Fraction(1, 3)
    assert len(lrc.bounded_relation_components(speeds, max_coefficient=5)) > 1


def test_decomposable_sum_does_not_connect_independent_relation_blocks():
    speeds = (1, 2, 100, 200)
    assert lrc.bounded_relation_components(speeds, max_coefficient=2) == (
        (0, 1),
        (2, 3),
    )


@pytest.mark.parametrize("speeds", [(1, 2, 6), (1, 2, 3, 8), (1, 3, 4, 5, 18)])
def test_first_band_connectivity_certificate_is_an_exact_relation_tree(speeds):
    certificate = lrc.bounded_relation_connectivity_certificate(
        speeds, max_coefficient=2
    )
    assert certificate is not None
    assert len(certificate) <= len(speeds) - 1
    assert all(
        sum(coefficient * speed for coefficient, speed in zip(relation, speeds)) == 0
        for relation in certificate
    )
    assert all(max(map(abs, relation)) <= 2 for relation in certificate)


@pytest.mark.parametrize("speeds", [(1, 2, 18), (1, 2, 100, 200)])
def test_disconnected_tuple_has_no_bounded_relation_tree(speeds):
    assert (
        lrc.bounded_relation_connectivity_certificate(speeds, max_coefficient=2)
        is None
    )


@pytest.mark.parametrize(
    "speeds",
    [
        (1, 2, 6),
        (1, 2, 3, 8),
        (1, 3, 4, 5, 18),
        (1, 5, 6, 11, 16, 17),
        (1, 3, 4, 5, 7, 13, 18),
    ],
)
def test_first_band_fixtures_have_positive_triangular_relation_tree(speeds):
    certificate = lrc.positive_triangular_relation_tree(
        speeds, max_coefficient=2
    )
    assert certificate is not None
    for relation in certificate:
        support = [index for index, coefficient in enumerate(relation) if coefficient]
        largest = max(support, key=lambda index: speeds[index])
        assert relation[largest] == -1
        assert all(
            coefficient > 0
            for index, coefficient in enumerate(relation)
            if index != largest and coefficient
        )
        assert sum(
            coefficient * speed for coefficient, speed in zip(relation, speeds)
        ) == 0


@pytest.mark.parametrize(
    "speeds",
    [
        (1, 2, 6),
        (1, 3, 4, 5, 18),
        (1, 5, 6, 11, 16, 17),
        (1, 3, 4, 5, 7, 13, 18),
    ],
)
def test_first_band_fixtures_are_generated_by_at_most_two_seeds(speeds):
    seeds, relations = lrc.positive_generation_certificate(
        speeds, max_coefficient=2
    )
    assert len(seeds) <= 2
    assert len(seeds) + len(relations) == len(speeds)
    for target, coefficients in relations:
        assert speeds[target] == sum(
            coefficient * speeds[index]
            for index, coefficient in enumerate(coefficients)
        )


def test_generic_three_speed_tuple_needs_three_positive_seeds():
    seeds, _ = lrc.positive_generation_certificate(
        (5, 7, 11), max_coefficient=2
    )
    assert seeds == (0, 1, 2)


@pytest.mark.parametrize(
    "speeds",
    [
        (1, 2, 6),
        (1, 3, 4, 5, 18),
        (2, 5, 6, 8, 10, 11),
        (2, 6, 7, 8, 10, 13, 14),
        (1, 3, 4, 5, 7, 13, 18),
    ],
)
def test_first_band_relations_leave_at_most_two_parameters(speeds):
    assert lrc.bounded_relation_rank(speeds, max_coefficient=2) >= len(speeds) - 2


@pytest.mark.parametrize(
    "speeds",
    [
        (1, 2, 6),
        (1, 3, 4, 5, 18),
        (2, 5, 6, 8, 10, 11),
        (2, 6, 7, 8, 10, 13, 14),
        (1, 3, 4, 5, 7, 13, 18),
    ],
)
def test_scanned_first_band_fixtures_have_full_short_relation_rank(speeds):
    assert lrc.bounded_relation_rank(speeds, max_coefficient=2) == len(speeds) - 1


def test_generic_tuple_can_have_more_than_two_relation_parameters():
    speeds = (5, 7, 11)
    assert lrc.bounded_relation_rank(speeds, max_coefficient=2) < len(speeds) - 2


@pytest.mark.parametrize(
    "speeds",
    [
        (1, 2, 6),
        (1, 3, 4, 5, 18),
        (2, 5, 6, 8, 10, 11),
        (2, 6, 7, 8, 10, 13, 14),
        (1, 3, 4, 5, 7, 13, 18),
        (3, 4, 7, 11),
    ],
)
def test_first_band_fixtures_have_two_signed_dissociated_seeds(speeds):
    seeds, relations = lrc.bounded_dissociated_generation_certificate(
        speeds, max_coefficient=2
    )

    assert len(seeds) <= 2
    assert len(relations) == len(speeds) - len(seeds)
    for target, relation in relations:
        assert relation[target] != 0
        assert all(
            coefficient == 0
            for index, coefficient in enumerate(relation)
            if index not in seeds and index != target
        )
        assert sum(
            coefficient * speed for coefficient, speed in zip(relation, speeds)
        ) == 0


def test_generic_tuple_can_require_three_dissociated_seeds():
    seeds, relations = lrc.bounded_dissociated_generation_certificate(
        (5, 7, 11), max_coefficient=2
    )
    assert seeds == (0, 1, 2)
    assert relations == ()


def test_two_parameter_pattern_reconstructs_common_nullspace():
    speeds = (1, 2, 7)
    pattern = lrc.bounded_relation_pattern(speeds, max_coefficient=2)

    assert pattern == ((1, 2, 0), (0, 0, 1))
    assert all(
        sum(coordinate * entry for coordinate, entry in zip(relation, column)) == 0
        for relation in lrc.bounded_relations(speeds, max_coefficient=2)
        for column in pattern
    )


def test_first_band_rank_bound_is_sharp_and_gives_two_torus_pattern():
    speeds = (3, 4, 7, 11)
    pattern = lrc.bounded_relation_pattern(speeds, max_coefficient=2)

    assert lrc.maximum_loneliness(speeds) == Fraction(2, 9)
    assert lrc.bounded_relation_rank(speeds, max_coefficient=2) == 2
    assert pattern == ((2, -1, 1, 0), (1, -1, 0, -1))


def test_two_torus_pattern_has_exact_safe_margin():
    pattern = ((2, -1, 1, 0), (1, -1, 0, -1))
    value, witness = lrc.pattern_maximum_loneliness(pattern)

    assert value == Fraction(1, 4)
    assert all(
        lrc.fractional_distance(
            sum(column[index] * coordinate for column, coordinate in zip(pattern, witness))
        )
        >= value
        for index in range(4)
    )


def test_safe_margin_gives_finite_parameter_norm_cutoff():
    pattern = ((2, -1, 1, 0), (1, -1, 0, -1))

    assert lrc.pattern_parameter_norm_squared_cutoff(
        pattern, threshold=Fraction(1, 5)
    ) == 500


def test_parameter_cutoff_requires_strict_ambient_margin():
    pattern = ((2, -1, 1, 0), (1, -1, 0, -1))

    with pytest.raises(ValueError, match="strictly exceed"):
        lrc.pattern_parameter_norm_squared_cutoff(
            pattern, threshold=Fraction(1, 4)
        )


def test_coefficient_relation_patterns_include_sharp_four_speed_subspace():
    sharp = lrc.bounded_relation_pattern((3, 4, 7, 11), max_coefficient=2)
    patterns = lrc.coefficient_relation_patterns(
        coordinate_count=4, max_coefficient=2, nullity=2
    )

    assert sharp in patterns
    assert len(patterns) == len(set(patterns))
    assert all(len(pattern) == 2 for pattern in patterns)


def test_positive_distinct_pattern_witness_filters_degenerate_coordinates():
    sharp = ((2, -1, 1, 0), (1, -1, 0, -1))
    witness = lrc.pattern_positive_distinct_witness(sharp)

    assert witness is not None
    values = [
        sum(column[index] * parameter for column, parameter in zip(sharp, witness))
        for index in range(4)
    ]
    assert all(value > 0 for value in values)
    assert len(set(values)) == 4
    assert lrc.pattern_positive_distinct_witness(((1, 1), (0, 0))) is None


def test_four_coordinate_pattern_symmetry_reduction_is_replayable():
    representatives = lrc.admissible_pattern_symmetry_representatives(
        coordinate_count=4, max_coefficient=2, nullity=2
    )

    assert len(representatives) == 123
    assert all(
        lrc.pattern_positive_distinct_witness(pattern) is not None
        for pattern in representatives
    )


def test_four_pattern_classifier_emits_symmetry_receipt():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("classify_four_patterns.py"))],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "relation_subspaces\t18074" in result.stdout
    assert "positive_distinct\t7332" in result.stdout
    assert "symmetry_classes\t123" in result.stdout


def test_full_bounded_relation_rank_recovers_the_primitive_speed_ray():
    speeds = (2, 5, 6, 8, 10, 11)
    pattern = lrc.bounded_relation_pattern(speeds, max_coefficient=2)

    assert pattern == (speeds,)
    assert math.gcd(*pattern[0]) == 1


def test_first_band_enumerator_replays_three_speed_survivors():
    survivors = list(lrc.first_band_survivors(runner_count=3, height=30))
    assert [speeds for speeds, _ in survivors] == [
        (1, 2, 3),
        (1, 2, 6),
        (1, 3, 4),
        (1, 5, 6),
        (2, 3, 5),
    ]
    assert all(value <= Fraction(2, 7) for _, value in survivors)


def test_first_band_scan_cli_emits_replayable_receipt():
    result = subprocess.run(
        [
            sys.executable,
            str(Path(__file__).with_name("scan_first_band.py")),
            "--runners",
            "3",
            "--height",
            "6",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    lines = result.stdout.splitlines()
    assert lines[0].startswith("runners\theight\tspeeds\tmaximum_loneliness")
    assert "ambient_maximum" in lines[0]
    assert "signed_dissociated_seeds" in lines[0]
    assert "parameter_norm_squared_cutoff" in lines[0]
    assert any("1,2,6\t2/7" in line for line in lines[1:])


def test_coarse_inductive_first_band_height_bound():
    assert lrc.inductive_first_band_height_bound(3) == 1764
    assert lrc.inductive_first_band_height_bound(4) == 1_259_712


def test_published_finite_checking_sum_bound():
    assert lrc.inductive_counterexample_sum_bound(3) == 36
    assert lrc.inductive_counterexample_sum_bound(4) == 1000


def test_complete_three_speed_first_band_check_under_published_sum_bound():
    bound = lrc.inductive_counterexample_sum_bound(3)
    survivors = list(
        lrc.first_band_survivors_by_sum(runner_count=3, sum_bound=bound)
    )

    assert [speeds for speeds, _ in survivors] == [
        (1, 2, 3),
        (1, 2, 6),
        (1, 3, 4),
        (1, 5, 6),
        (2, 3, 5),
    ]
    assert all(
        lrc.bounded_relation_rank(speeds, max_coefficient=2) >= 1
        for speeds, _ in survivors
    )


def test_four_speed_h33_cpp_verifier_matches_small_exact_domain(tmp_path):
    compiler = shutil.which("clang++") or shutil.which("g++")
    if compiler is None:
        pytest.skip("a C++20 compiler is required for the exhaustive verifier")
    source = Path(__file__).with_name("verify_h33_n4.cpp")
    executable = tmp_path / "verify_h33_n4"
    subprocess.run(
        [compiler, "-O3", "-std=c++20", str(source), "-o", str(executable)],
        check=True,
    )
    result = subprocess.run(
        [str(executable), "60", "0", "1"],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "VERIFIED bound=60 shard=0/1" in result.stdout
    assert "first_band=6 rank_failures=0" in result.stdout
    for speeds in [
        "1,2,3,4",
        "1,2,3,8",
        "1,3,4,5",
        "1,3,4,7",
        "1,4,5,6",
        "3,4,7,11",
    ]:
        assert f"SURVIVOR {speeds}" in result.stdout

    complete = subprocess.run(
        [str(executable), "1000", "0", "1"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert (
        "VERIFIED bound=1000 shard=0/1 enumerated=1705044764 "
        "grid_rejected=1705042194 nonprimitive=1473 gcd_excluded=0 "
        "exact_rejected=1091 first_band=6 rank_failures=0"
    ) in complete.stdout


def test_early_first_band_predicate_matches_exact_maximum():
    for runner_count, height in [(3, 14), (4, 10)]:
        threshold = Fraction(2, 2 * runner_count + 1)
        for speeds in itertools.combinations(range(1, height + 1), runner_count):
            assert lrc.loneliness_at_most(speeds, threshold=threshold) == (
                lrc.maximum_loneliness(speeds) <= threshold
            )
