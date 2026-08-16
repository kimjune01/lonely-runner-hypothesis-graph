"""Certificate search for Rosenfeld's modular Lonely Runner obstruction.

This is an exploratory implementation, not a proof of the general conjecture.
It returns an explicit admissible cover when one exists and ``None`` when an
exhaustive search finds none for the given finite instance.
"""

from __future__ import annotations

from functools import lru_cache
from math import gcd


def covers(*, v: int, j: int, k: int, p: int, denominator: int) -> bool:
    """Whether v covers j under the strict threshold 1 / denominator."""
    modulus = (k + 1) * p
    residue = (j * v) % modulus
    distance_numerator = min(residue, modulus - residue)
    return distance_numerator * denominator < modulus


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
