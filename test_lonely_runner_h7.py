import importlib.util
from pathlib import Path


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
