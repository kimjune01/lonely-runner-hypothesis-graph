"""Certificate search for Rosenfeld's modular Lonely Runner obstruction.

This is an exploratory implementation, not a proof of the general conjecture.
It returns an explicit admissible cover when one exists and ``None`` when an
exhaustive search finds none for the given finite instance.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd


def covers(*, v: int, j: int, k: int, p: int, denominator: int) -> bool:
    """Whether v covers j under the strict threshold 1 / denominator."""
    modulus = (k + 1) * p
    residue = (j * v) % modulus
    distance_numerator = min(residue, modulus - residue)
    return distance_numerator * denominator < modulus


def fractional_distance(value: Fraction | int) -> Fraction:
    """Return the exact distance from a rational value to the nearest integer."""
    value = Fraction(value)
    residue = value % 1
    return min(residue, 1 - residue)


def maximum_loneliness(speeds: tuple[int, ...]) -> Fraction:
    """Compute max_t min_i ||v_i t|| exactly from its critical times.

    A maximum of the lower envelope occurs at a cusp of one triangular wave
    or where two affine pieces agree. Those times have denominators 2*v_i,
    v_i+v_j, or |v_i-v_j|.
    """
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")

    candidates = {Fraction(0), Fraction(1)}
    for speed in speeds:
        denominator = 2 * speed
        candidates.update(Fraction(numerator, denominator) for numerator in range(denominator + 1))
    for index, first in enumerate(speeds):
        for second in speeds[index + 1 :]:
            for denominator in {first + second, abs(first - second)} - {0}:
                candidates.update(
                    Fraction(numerator, denominator)
                    for numerator in range(denominator + 1)
                )

    return max(
        min(fractional_distance(speed * time) for speed in speeds)
        for time in candidates
    )


def height_sensitive_grid_bound(speeds: tuple[int, ...]) -> int:
    """First denominator guaranteed to preserve any strict LRC witness.

    If M=max(speeds), exact critical-time geometry makes a positive gap over
    1/(k+1) at least 1/(2*M*(k+1)). Rounding a witness to the nearest point of
    a d-grid loses at most M/(2*d), so every d >= (k+1)*M**2+1 works.
    """
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    return (len(speeds) + 1) * max(speeds) ** 2 + 1


def multi_fast_union_condition(speeds: tuple[int, ...], *, fast_count: int) -> bool:
    """Whether a union bound certifies adding several fast runners.

    Split the sorted tuple into a slow prefix and ``fast_count`` faster
    runners. Around an exact maximizing time for the slow prefix, the slow
    runners remain above the full-tuple threshold on an interval of radius
    ``eta``. On that interval each fast runner is bad on measure at most
    ``2*delta*length + 2*delta/speed``. If their union cannot fill the
    interval, a simultaneous witness exists.
    """
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    ordered = tuple(sorted(speeds))
    runner_count = len(ordered)
    if not 1 <= fast_count < runner_count:
        raise ValueError("fast_count must leave at least one slow runner")
    if 2 * fast_count >= runner_count + 1:
        return False

    slow = ordered[:-fast_count]
    fast = ordered[-fast_count:]
    delta = Fraction(1, runner_count + 1)
    slow_loneliness = maximum_loneliness(slow)
    if slow_loneliness <= delta:
        return False
    eta = (slow_loneliness - delta) / max(slow)
    return eta * (1 - 2 * fast_count * delta) > delta * sum(
        (Fraction(1, speed) for speed in fast),
        start=Fraction(0),
    )


def valid_time_measure(speeds: tuple[int, ...], *, delta: Fraction) -> Fraction:
    """Exact measure of times where every speed is at least ``delta`` lonely."""
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    delta = Fraction(delta)
    if not 0 <= delta <= Fraction(1, 2):
        raise ValueError("delta must lie between 0 and 1/2")

    endpoints = {Fraction(0), Fraction(1)}
    for speed in speeds:
        for integer in range(speed + 1):
            zero = Fraction(integer, speed)
            for boundary in (zero - delta / speed, zero + delta / speed):
                if 0 <= boundary <= 1:
                    endpoints.add(boundary)

    ordered = sorted(endpoints)
    measure = Fraction(0)
    for left, right in zip(ordered, ordered[1:]):
        midpoint = (left + right) / 2
        if all(fractional_distance(speed * midpoint) >= delta for speed in speeds):
            measure += right - left
    return measure


def fourier_relation_bound(runner_count: int, *, delta: Fraction) -> int:
    """Explicit coefficient bound forced by failure at threshold ``delta``.

    The proof uses a triangular bump of half-width ``a=1/2-delta``. Its
    Fourier l1 norm is at most ``S=a+1/(3a)``, while the coefficient tail past
    K is less than ``2/(9aK)``. Choosing K so that the product-expansion tail
    is smaller than the positive constant term forces a nonzero frequency
    relation among the speeds.
    """
    if runner_count < 1:
        raise ValueError("runner_count must be positive")
    delta = Fraction(delta)
    if not 0 <= delta < Fraction(1, 2):
        raise ValueError("delta must lie between 0 and 1/2")
    half_width = Fraction(1, 2) - delta
    fourier_l1_bound = half_width + Fraction(1, 3) / half_width
    cutoff = (
        Fraction(2 * runner_count, 9)
        * fourier_l1_bound ** (runner_count - 1)
        / half_width ** (runner_count + 1)
    )
    return int(cutoff) + 1


def find_bounded_relation(
    speeds: tuple[int, ...], *, max_coefficient: int
) -> tuple[int, ...] | None:
    """Find a small integer relation by exhaustive search for diagnostics."""
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    if max_coefficient < 1:
        raise ValueError("max_coefficient must be positive")
    coefficients = range(-max_coefficient, max_coefficient + 1)
    for relation in product(coefficients, repeat=len(speeds)):
        if not any(relation):
            continue
        if sum(coefficient * speed for coefficient, speed in zip(relation, speeds)):
            continue
        divisor = gcd(*(abs(coefficient) for coefficient in relation))
        primitive = tuple(coefficient // divisor for coefficient in relation)
        first = next(coefficient for coefficient in primitive if coefficient)
        if first < 0:
            primitive = tuple(-coefficient for coefficient in primitive)
        return primitive
    return None


def universal_grid_counterexample(*, r: int) -> tuple[int, tuple[int, int], Fraction]:
    """Give the r-th counterexample to the universal grid-witness conjecture.

    At denominator d=6r+1, the coprime speeds (1,3r) have no witness in
    (1/d)Z, although the returned rational time is a strict real witness.
    """
    if r < 1:
        raise ValueError("r must be positive")
    denominator = 6 * r + 1
    second_speed = 3 * r
    if second_speed % 2:
        strict_witness = Fraction(1, 2)
    else:
        strict_witness = Fraction(second_speed // 2, second_speed + 1)
    return denominator, (1, second_speed), strict_witness


def coverage_size(*, k: int, p: int, v: int) -> int:
    """Exact half-grid coverage count at threshold 1/(k+1), for odd D."""
    modulus = (k + 1) * p
    if modulus % 2 == 0:
        raise ValueError("formula currently requires an odd modulus")
    if v % p == 0:
        raise ValueError("candidate must not be divisible by p")
    common = gcd(v, modulus)
    radius_steps = (p - 1) // common
    return (common * (2 * radius_steps + 1) - 1) // 2


def selection_moments(
    speeds: tuple[int, ...], *, k: int, p: int, denominator: int
) -> tuple[int, int, int]:
    """Return total incidences, pair incidences, and union size."""
    limit = ((k + 1) * p) // 2
    masks = {}
    for speed in speeds:
        mask = 0
        for j in range(1, limit + 1):
            if covers(v=speed, j=j, k=k, p=p, denominator=denominator):
                mask |= 1 << (j - 1)
        masks[speed] = mask
    first = sum(mask.bit_count() for mask in masks.values())
    second = sum(
        (masks[left] & masks[right]).bit_count()
        for index, left in enumerate(speeds)
        for right in speeds[index + 1 :]
    )
    union = 0
    for mask in masks.values():
        union |= mask
    return first, second, union.bit_count()


def coverage_residue_counts(
    *, v: int, k: int, p: int, modulus: int
) -> tuple[int, ...]:
    """Count the full cyclic coverage set in each residue class."""
    period = (k + 1) * p
    counts = [0] * modulus
    for j in range(period):
        if covers(v=v, j=j, k=k, p=p, denominator=k + 1):
            counts[j % modulus] += 1
    return tuple(counts)


def coverage_fiber(*, v: int, residue: int, k: int, p: int) -> tuple[int, ...]:
    """Phases covered in the nine-point fiber over a residue modulo p."""
    if k != 8:
        raise ValueError("nine-point fiber representation requires k=8")
    if not 0 <= residue < p:
        raise ValueError("residue must be in range(p)")
    return tuple(
        phase
        for phase in range(9)
        if covers(
            v=v,
            j=residue + phase * p,
            k=k,
            p=p,
            denominator=k + 1,
        )
    )


def minimum_g3_phase_classes(*, unit_speeds: int) -> int:
    """Necessary distinct three-point classes for a nine-phase local cover."""
    if unit_speeds < 0:
        raise ValueError("unit_speeds must be nonnegative")
    if unit_speeds <= 2:
        return 3
    if unit_speeds <= 4:
        return 1
    return 0


def _build_two_unit_fiber_cnf(*, p: int):
    """Necessary fiber constraints for a k=8 cover with exactly two units."""
    from pysat.card import CardEnc, EncType
    from pysat.formula import CNF, IDPool

    k = 8
    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    gcd3 = tuple(v for v in candidates if gcd(v, 9) == 3)
    gcd9 = tuple(v for v in candidates if gcd(v, 9) == 9)
    pool = IDPool()
    variables = {v: pool.id(f"choose_{v}") for v in (*gcd3, *gcd9)}
    cnf = CNF()
    cnf.extend(
        CardEnc.equals(
            lits=list(variables.values()),
            bound=6,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    # The special fiber r=0 forces at least one speed divisible by 9.
    cnf.append([variables[v] for v in gcd9])
    for residue in range(1, p):
        whole_fiber = [
            variables[v]
            for v in gcd9
            if coverage_fiber(v=v, residue=residue, k=k, p=p)
        ]
        for phase_class in range(3):
            active_class = []
            for v in gcd3:
                fiber = coverage_fiber(v=v, residue=residue, k=k, p=p)
                if fiber and fiber[0] % 3 == phase_class:
                    active_class.append(variables[v])
            cnf.append(whole_fiber + active_class)
    return cnf


def two_unit_fiber_obstruction_is_unsat(*, p: int) -> bool:
    """Check the reduced necessary constraints with an independent SAT model."""
    from pysat.solvers import Solver

    cnf = _build_two_unit_fiber_cnf(p=p)
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        return not solver.solve()


def _build_three_unit_fiber_cnf(*, p: int):
    """Exact normalized k=8 branch with three units plus a phase lemma."""
    from pysat.card import CardEnc, EncType
    from pysat.formula import CNF, IDPool

    k = 8
    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(2, limit + 1) if v % p != 0)
    units = tuple(v for v in candidates if gcd(v, 9) == 1)
    gcd3 = tuple(v for v in candidates if gcd(v, 9) == 3)
    gcd9 = tuple(v for v in candidates if gcd(v, 9) == 9)
    nonunits = (*gcd3, *gcd9)
    pool = IDPool()
    variables = {v: pool.id(f"choose_{v}") for v in candidates}
    cnf = CNF()
    # Speed 1 is already selected by unit normalization.
    cnf.extend(
        CardEnc.equals(
            lits=[variables[v] for v in units],
            bound=2,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    cnf.extend(
        CardEnc.equals(
            lits=[variables[v] for v in nonunits],
            bound=5,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    cnf.append([variables[v] for v in gcd9])
    for j in range(p, limit + 1):
        cnf.append(
            [
                variables[v]
                for v in candidates
                if covers(v=v, j=j, k=k, p=p, denominator=k + 1)
            ]
        )
    # Speed 1 covers phases 0 and 8 on each nonzero fiber. With only two
    # other unit edges, every fiber not covered wholesale needs phase class 1.
    for residue in range(1, p):
        whole_fiber = [
            variables[v]
            for v in gcd9
            if coverage_fiber(v=v, residue=residue, k=k, p=p)
        ]
        phase_one = []
        for v in gcd3:
            fiber = coverage_fiber(v=v, residue=residue, k=k, p=p)
            if fiber and fiber[0] % 3 == 1:
                phase_one.append(variables[v])
        cnf.append(whole_fiber + phase_one)
    return cnf


def three_unit_fiber_obstruction_is_unsat(*, p: int) -> bool:
    """Check the exact normalized three-unit branch plus its phase lemma."""
    from pysat.solvers import Solver

    cnf = _build_three_unit_fiber_cnf(p=p)
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        return not solver.solve()


def _export_cnf_certificate(*, cnf, cnf_path, proof_path):
    from pathlib import Path

    from pysat.solvers import Solver

    with Solver(
        name="glucose4", bootstrap_with=cnf.clauses, with_proof=True
    ) as solver:
        if solver.solve():
            raise ValueError("cannot export a certificate for a SAT instance")
        proof = solver.get_proof() or []
    if not proof:
        raise RuntimeError("solver returned UNSAT without a proof trace")
    cnf_path = Path(cnf_path)
    proof_path = Path(proof_path)
    cnf.to_file(str(cnf_path))
    proof_path.write_text("\n".join(proof) + "\n")
    return {
        "status": "UNSAT",
        "variables": cnf.nv,
        "clauses": len(cnf.clauses),
        "proof_steps": len(proof),
    }


def export_two_unit_fiber_certificate(*, p: int, cnf_path, proof_path):
    """Export the reduced two-unit obstruction and a DRUP certificate."""
    cnf = _build_two_unit_fiber_cnf(p=p)
    return _export_cnf_certificate(
        cnf=cnf, cnf_path=cnf_path, proof_path=proof_path
    )


def export_three_unit_fiber_certificate(*, p: int, cnf_path, proof_path):
    """Export the exact normalized three-unit branch and a DRUP proof."""
    cnf = _build_three_unit_fiber_cnf(p=p)
    return _export_cnf_certificate(
        cnf=cnf, cnf_path=cnf_path, proof_path=proof_path
    )


def max_fourier_positivity_ratio(
    speeds: tuple[int, ...], *, k: int, p: int, denominator: int
) -> tuple[float, int]:
    """Largest single-character coefficient divided by zero-frequency surplus."""
    import cmath
    import math

    period = (k + 1) * p
    incidences = [
        sum(
            covers(v=speed, j=j, k=k, p=p, denominator=denominator)
            for speed in speeds
        )
        for j in range(period)
    ]
    surplus = sum(incidences) - period
    if surplus <= 0:
        raise ValueError("single-character positivity bound needs positive surplus")
    best_magnitude = -1.0
    best_character = 0
    for character in range(1, period):
        root = cmath.exp(-2j * math.pi * character / period)
        power = 1 + 0j
        coefficient = 0j
        for incidence in incidences:
            coefficient += incidence * power
            power *= root
        magnitude = abs(coefficient)
        if magnitude > best_magnitude:
            best_magnitude = magnitude
            best_character = character
    return best_magnitude / surplus, best_character


def gcd_constraint(speeds: tuple[int, ...], *, k: int, p: int) -> bool:
    """Check gcd(D, all speeds except each one) = 1."""
    if len(speeds) != k:
        return False
    modulus = (k + 1) * p
    for omitted in range(k):
        common = modulus
        for index, speed in enumerate(speeds):
            if index != omitted:
                common = gcd(common, speed)
        if common != 1:
            return False
    return True


def covers_universe(
    speeds: tuple[int, ...], *, k: int, p: int, denominator: int
) -> bool:
    limit = ((k + 1) * p) // 2
    return all(
        any(covers(v=v, j=j, k=k, p=p, denominator=denominator) for v in speeds)
        for j in range(1, limit + 1)
    )


def uncovered_times(
    speeds: tuple[int, ...], *, k: int, p: int, denominator: int
) -> tuple[int, ...]:
    """Return the half-grid test times missed by every selected speed."""
    limit = ((k + 1) * p) // 2
    return tuple(
        j
        for j in range(1, limit + 1)
        if not any(
            covers(v=v, j=j, k=k, p=p, denominator=denominator) for v in speeds
        )
    )


def scale_speeds(
    speeds: tuple[int, ...], *, multiplier: int, k: int, p: int
) -> tuple[int, ...]:
    """Apply a unit scaling and return canonical representatives modulo sign."""
    modulus = (k + 1) * p
    if gcd(multiplier, modulus) != 1:
        raise ValueError("multiplier must be a unit modulo (k + 1)p")
    representatives = []
    for speed in speeds:
        residue = (multiplier * speed) % modulus
        representatives.append(min(residue, modulus - residue))
    return tuple(sorted(representatives))


def best_gap_closing_exchanges(
    speeds: tuple[int, ...], *, gap: int, k: int, p: int, denominator: int
) -> tuple[tuple[int, int, tuple[int, ...]], ...]:
    """Return one-speed replacements that close a gap and open fewest gaps."""
    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    masks = {}
    for speed in candidates:
        mask = 0
        for j in range(1, limit + 1):
            if covers(v=speed, j=j, k=k, p=p, denominator=denominator):
                mask |= 1 << (j - 1)
        masks[speed] = mask

    best_count = limit + 1
    best = []
    for removed in speeds:
        remaining = tuple(v for v in speeds if v != removed)
        base_mask = 0
        for speed in remaining:
            base_mask |= masks[speed]
        for added in candidates:
            if added in remaining or not covers(
                v=added, j=gap, k=k, p=p, denominator=denominator
            ):
                continue
            replacement = tuple(sorted((*remaining, added)))
            if not gcd_constraint(replacement, k=k, p=p):
                continue
            union = base_mask | masks[added]
            new_gaps = tuple(
                j for j in range(1, limit + 1) if not union & (1 << (j - 1))
            )
            if len(new_gaps) < best_count:
                best_count = len(new_gaps)
                best = [(removed, added, new_gaps)]
            elif len(new_gaps) == best_count:
                best.append((removed, added, new_gaps))
    return tuple(best)


def find_bad_cover(*, k: int, p: int, denominator: int) -> tuple[int, ...] | None:
    """Find a k-element cover satisfying the gcd constraint, if one exists."""
    modulus = (k + 1) * p
    limit = modulus // 2
    universe_mask = (1 << limit) - 1
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)

    masks: dict[int, int] = {}
    coverers: list[list[int]] = [[] for _ in range(limit)]
    for v in candidates:
        mask = 0
        for j in range(1, limit + 1):
            if covers(v=v, j=j, k=k, p=p, denominator=denominator):
                mask |= 1 << (j - 1)
                coverers[j - 1].append(v)
        masks[v] = mask

    @lru_cache(maxsize=None)
    def search(selected: tuple[int, ...], covered: int) -> tuple[int, ...] | None:
        if len(selected) == k:
            if covered == universe_mask and gcd_constraint(selected, k=k, p=p):
                return selected
            return None

        selected_set = set(selected)
        slots = k - len(selected)
        uncovered = universe_mask & ~covered

        if not uncovered:
            options = [v for v in candidates if v not in selected_set]
        else:
            uncovered_indices = [
                index for index in range(limit) if uncovered & (1 << index)
            ]
            pivot = min(
                uncovered_indices,
                key=lambda index: sum(v not in selected_set for v in coverers[index]),
            )
            options = [v for v in coverers[pivot] if v not in selected_set]

        if not options:
            return None

        # Even granting each remaining slot its best independent contribution,
        # there must be enough total capacity to cover what remains.
        gains = sorted(
            ((masks[v] & uncovered).bit_count() for v in candidates if v not in selected_set),
            reverse=True,
        )
        if sum(gains[:slots]) < uncovered.bit_count():
            return None

        for v in options:
            next_selected = tuple(sorted((*selected, v)))
            if len(next_selected) == k - 1:
                common = modulus
                for speed in next_selected:
                    common = gcd(common, speed)
                if common != 1:
                    continue
            found = search(next_selected, covered | masks[v])
            if found is not None:
                return found
        return None

    return search((), 0)


def _prime_divisors(value: int) -> tuple[int, ...]:
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return tuple(factors)


def active_gcd_primes(*, k: int, p: int) -> tuple[int, ...]:
    """Prime gcd constraints not implied by selecting exactly k candidates."""
    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    return tuple(
        prime
        for prime in _prime_divisors(modulus)
        if sum(v % prime == 0 for v in candidates) >= k - 1
    )


def find_bad_cover_smt(*, k: int, p: int, denominator: int) -> tuple[int, ...] | None:
    """Solve the finite cover instance with Z3; return a SAT witness or None."""
    from z3 import Bool, If, Or, Solver, Sum, sat, unsat

    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    chosen = {v: Bool(f"choose_{v}") for v in candidates}
    solver = Solver()

    solver.add(Sum([If(chosen[v], 1, 0) for v in candidates]) == k)

    for j in range(1, limit + 1):
        covering = [
            chosen[v]
            for v in candidates
            if covers(v=v, j=j, k=k, p=p, denominator=denominator)
        ]
        solver.add(Or(covering))

    # gcd(D, all selected speeds except any one) = 1 iff, for each prime
    # q dividing D, at least two selected speeds are not divisible by q.
    for prime in active_gcd_primes(k=k, p=p):
        solver.add(
            Sum(
                [
                    If(chosen[v], 1, 0)
                    for v in candidates
                    if v % prime != 0
                ]
            )
            >= 2
        )

    status = solver.check()
    if status == unsat:
        return None
    if status != sat:
        raise RuntimeError(f"SMT search was inconclusive: {status}")
    model = solver.model()
    return tuple(v for v in candidates if model.evaluate(chosen[v], model_completion=True))


def _named_smt_constraints(*, k: int, p: int, denominator: int):
    from z3 import Bool, If, Or, Sum

    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    chosen = {v: Bool(f"choose_{v}") for v in candidates}
    constraints = {
        f"count_exactly_{k}": Sum([If(chosen[v], 1, 0) for v in candidates])
        == k
    }
    for j in range(1, limit + 1):
        constraints[f"cover_j_{j}"] = Or(
            [
                chosen[v]
                for v in candidates
                if covers(v=v, j=j, k=k, p=p, denominator=denominator)
            ]
        )
    for prime in active_gcd_primes(k=k, p=p):
        constraints[f"gcd_prime_{prime}"] = (
            Sum(
                [
                    If(chosen[v], 1, 0)
                    for v in candidates
                    if v % prime != 0
                ]
            )
            >= 2
        )
    return constraints


def unsat_core(*, k: int, p: int, denominator: int) -> tuple[str, ...]:
    """Return stable labels for a Z3 UNSAT core of the finite instance."""
    from z3 import Bool, Solver, unsat

    constraints = _named_smt_constraints(k=k, p=p, denominator=denominator)
    solver = Solver()
    solver.set(unsat_core=True)
    for name, constraint in constraints.items():
        solver.assert_and_track(constraint, Bool(name))
    status = solver.check()
    if status != unsat:
        raise ValueError(f"expected UNSAT instance, got {status}")
    return tuple(sorted(str(label) for label in solver.unsat_core()))


def replay_unsat_core(
    *, k: int, p: int, denominator: int, core: tuple[str, ...]
) -> bool:
    """Check that the named subset alone remains UNSAT."""
    from z3 import Solver, unsat

    constraints = _named_smt_constraints(k=k, p=p, denominator=denominator)
    if any(name not in constraints for name in core):
        return False
    solver = Solver()
    solver.add([constraints[name] for name in core])
    return solver.check() == unsat


def _build_sat_cnf(*, k: int, p: int, denominator: int):
    from pysat.card import CardEnc, EncType
    from pysat.formula import CNF, IDPool

    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    pool = IDPool()
    variables = {v: pool.id(f"choose_{v}") for v in candidates}
    cnf = CNF()
    cnf.extend(
        CardEnc.equals(
            lits=list(variables.values()),
            bound=k,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    for j in range(1, limit + 1):
        cnf.append(
            [
                variables[v]
                for v in candidates
                if covers(v=v, j=j, k=k, p=p, denominator=denominator)
            ]
        )
    for prime in active_gcd_primes(k=k, p=p):
        cnf.extend(
            CardEnc.atleast(
                lits=[variables[v] for v in candidates if v % prime != 0],
                bound=2,
                vpool=pool,
                encoding=EncType.seqcounter,
            ).clauses
        )

    return candidates, variables, cnf


def find_bad_cover_sat(*, k: int, p: int, denominator: int) -> tuple[int, ...] | None:
    """Solve the finite cover as CNF with CaDiCaL; return a SAT witness."""
    from pysat.solvers import Solver

    candidates, variables, cnf = _build_sat_cnf(
        k=k, p=p, denominator=denominator
    )

    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        if not solver.solve():
            return None
        positive = {literal for literal in solver.get_model() if literal > 0}
    return tuple(v for v in candidates if variables[v] in positive)


def export_unsat_certificate(
    *, k: int, p: int, denominator: int, cnf_path, proof_path
) -> dict[str, int | str]:
    """Write DIMACS CNF plus a DRUP proof emitted by Glucose 4."""
    from pathlib import Path

    from pysat.solvers import Solver

    _, _, cnf = _build_sat_cnf(k=k, p=p, denominator=denominator)
    with Solver(
        name="glucose4", bootstrap_with=cnf.clauses, with_proof=True
    ) as solver:
        if solver.solve():
            raise ValueError("cannot export an UNSAT certificate for a SAT instance")
        proof = solver.get_proof() or []
    if not proof:
        raise RuntimeError("solver returned UNSAT without a proof trace")

    cnf_path = Path(cnf_path)
    proof_path = Path(proof_path)
    cnf.to_file(str(cnf_path))
    proof_path.write_text("\n".join(proof) + "\n")
    return {
        "status": "UNSAT",
        "variables": cnf.nv,
        "clauses": len(cnf.clauses),
        "proof_steps": len(proof),
    }


def _coverage_assumption_instance(*, k: int, p: int, denominator: int):
    from pysat.card import CardEnc, EncType
    from pysat.formula import CNF, IDPool

    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    pool = IDPool()
    variables = {v: pool.id(f"choose_{v}") for v in candidates}
    cnf = CNF()
    cnf.extend(
        CardEnc.equals(
            lits=list(variables.values()),
            bound=k,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    for prime in active_gcd_primes(k=k, p=p):
        cnf.extend(
            CardEnc.atleast(
                lits=[variables[v] for v in candidates if v % prime != 0],
                bound=2,
                vpool=pool,
                encoding=EncType.seqcounter,
            ).clauses
        )

    assumptions = {}
    for j in range(1, limit + 1):
        selector = pool.id(f"require_cover_j_{j}")
        assumptions[j] = selector
        cnf.append(
            [-selector]
            + [
                variables[v]
                for v in candidates
                if covers(v=v, j=j, k=k, p=p, denominator=denominator)
            ]
        )
    return cnf, assumptions


def unsat_coverage_core_sat(*, k: int, p: int, denominator: int) -> tuple[int, ...]:
    """Return test-time indices in a CaDiCaL assumption core."""
    from pysat.solvers import Solver

    cnf, assumptions = _coverage_assumption_instance(
        k=k, p=p, denominator=denominator
    )
    all_assumptions = list(assumptions.values())
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        if solver.solve(assumptions=all_assumptions):
            raise ValueError("expected an UNSAT finite instance")
        core_literals = set(solver.get_core() or [])
    if not core_literals:
        raise RuntimeError("solver returned UNSAT without an assumption core")
    return tuple(sorted(j for j, literal in assumptions.items() if literal in core_literals))


def replay_coverage_core_sat(
    *, k: int, p: int, denominator: int, core: tuple[int, ...]
) -> bool:
    from pysat.solvers import Solver

    cnf, assumptions = _coverage_assumption_instance(
        k=k, p=p, denominator=denominator
    )
    if any(j not in assumptions for j in core):
        return False
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        return not solver.solve(assumptions=[assumptions[j] for j in core])


def find_cover_with_min_nonmultiples(
    *, k: int, p: int, denominator: int, prime: int, minimum: int
) -> tuple[int, ...] | None:
    """Find a cover while requiring a chosen number nonzero modulo prime."""
    from pysat.card import CardEnc, EncType
    from pysat.formula import CNF, IDPool
    from pysat.solvers import Solver

    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    pool = IDPool()
    variables = {v: pool.id(f"choose_{v}") for v in candidates}
    cnf = CNF()
    cnf.extend(
        CardEnc.equals(
            lits=list(variables.values()),
            bound=k,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    for j in range(1, limit + 1):
        cnf.append(
            [
                variables[v]
                for v in candidates
                if covers(v=v, j=j, k=k, p=p, denominator=denominator)
            ]
        )
    cnf.extend(
        CardEnc.atleast(
            lits=[variables[v] for v in candidates if v % prime != 0],
            bound=minimum,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        if not solver.solve():
            return None
        positive = {literal for literal in solver.get_model() if literal > 0}
    return tuple(v for v in candidates if variables[v] in positive)


def _coverage_cpsat_model(
    *, k: int, p: int, denominator: int, core: tuple[int, ...] | None = None
):
    from ortools.sat.python import cp_model

    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    model = cp_model.CpModel()
    chosen = {v: model.new_bool_var(f"choose_{v}") for v in candidates}
    model.add(sum(chosen.values()) == k)
    for prime in active_gcd_primes(k=k, p=p):
        model.add(sum(chosen[v] for v in candidates if v % prime != 0) >= 2)

    selectors = {}
    times = range(1, limit + 1) if core is None else core
    for j in times:
        covering = [
            chosen[v]
            for v in candidates
            if covers(v=v, j=j, k=k, p=p, denominator=denominator)
        ]
        if core is None:
            selector = model.new_bool_var(f"require_cover_j_{j}")
            selectors[selector.index] = j
            model.add(sum(covering) >= 1).only_enforce_if(selector)
            model.add_assumption(selector)
        else:
            model.add(sum(covering) >= 1)
    return model, selectors


def unsat_coverage_core_cpsat(
    *, k: int, p: int, denominator: int
) -> tuple[int, ...]:
    """Return test-time indices from a CP-SAT sufficient assumption core."""
    from ortools.sat.python import cp_model

    model, selectors = _coverage_cpsat_model(k=k, p=p, denominator=denominator)
    solver = cp_model.CpSolver()
    status = solver.solve(model)
    if status != cp_model.INFEASIBLE:
        raise ValueError(f"expected INFEASIBLE instance, got {solver.status_name(status)}")
    literal_indices = solver.sufficient_assumptions_for_infeasibility()
    core = tuple(sorted(selectors[index] for index in literal_indices if index in selectors))
    if not core:
        raise RuntimeError("CP-SAT returned INFEASIBLE without a coverage core")
    return core


def replay_coverage_core_cpsat(
    *, k: int, p: int, denominator: int, core: tuple[int, ...]
) -> bool:
    from ortools.sat.python import cp_model

    limit = ((k + 1) * p) // 2
    if any(j < 1 or j > limit for j in core):
        return False
    model, _ = _coverage_cpsat_model(
        k=k, p=p, denominator=denominator, core=core
    )
    solver = cp_model.CpSolver()
    return solver.solve(model) == cp_model.INFEASIBLE


def max_coverage_candidate(
    *,
    k: int,
    p: int,
    denominator: int,
    prime: int,
    minimum_nonmultiples: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Find an admissible-size selection minimizing uncovered test times."""
    from pysat.card import CardEnc, EncType
    from pysat.examples.rc2 import RC2
    from pysat.formula import IDPool, WCNF

    modulus = (k + 1) * p
    limit = modulus // 2
    candidates = tuple(v for v in range(1, limit + 1) if v % p != 0)
    pool = IDPool()
    variables = {v: pool.id(f"choose_{v}") for v in candidates}
    formula = WCNF()
    formula.extend(
        CardEnc.equals(
            lits=list(variables.values()),
            bound=k,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    formula.extend(
        CardEnc.atleast(
            lits=[variables[v] for v in candidates if v % prime != 0],
            bound=minimum_nonmultiples,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    for j in range(1, limit + 1):
        formula.append(
            [
                variables[v]
                for v in candidates
                if covers(v=v, j=j, k=k, p=p, denominator=denominator)
            ],
            weight=1,
        )

    with RC2(formula) as solver:
        model = solver.compute()
    positive = {literal for literal in model if literal > 0}
    selected = tuple(v for v in candidates if variables[v] in positive)
    uncovered = tuple(
        j
        for j in range(1, limit + 1)
        if not any(
            covers(v=v, j=j, k=k, p=p, denominator=denominator)
            for v in selected
        )
    )
    return selected, uncovered
