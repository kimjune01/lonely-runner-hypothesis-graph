"""Certificate search for Rosenfeld's modular Lonely Runner obstruction.

This is an exploratory implementation, not a proof of the general conjecture.
It returns an explicit admissible cover when one exists and ``None`` when an
exhaustive search finds none for the given finite instance.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, gcd, lcm


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


def periodic_bad_window_cells(
    speeds: tuple[int, ...], *, delta: Fraction
) -> tuple[tuple[Fraction, Fraction, tuple[int, ...]], ...]:
    """Partition one reset cycle into exact constant-load open cells."""
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    delta = Fraction(delta)
    if not 0 < delta < Fraction(1, 2):
        raise ValueError("delta must lie strictly between zero and one half")

    endpoints = {Fraction(0), Fraction(1)}
    for speed in speeds:
        for center in range(speed):
            endpoints.add(((Fraction(center) - delta) / speed) % 1)
            endpoints.add(((Fraction(center) + delta) / speed) % 1)
    ordered = sorted(endpoints)
    return tuple(
        (
            left,
            right,
            tuple(
                index
                for index, speed in enumerate(speeds)
                if fractional_distance(speed * ((left + right) / 2)) < delta
            ),
        )
        for left, right in zip(ordered, ordered[1:])
    )


def handoff_seed_pair(
    speeds: tuple[int, ...], *, delta: Fraction
) -> tuple[int, int] | None:
    """First two distinct singleton-load owners encountered after reset."""
    distinct: list[int] = []
    for owner in singleton_handoff_owners(speeds, delta=delta):
        if owner in distinct:
            continue
        distinct.append(owner)
        if len(distinct) == 2:
            return distinct[0], distinct[1]
    return None


def singleton_handoff_owners(
    speeds: tuple[int, ...], *, delta: Fraction
) -> tuple[int, ...]:
    """Cyclic sequence of singleton-load cell owners after the common reset."""
    states: list[tuple[int, ...]] = []
    for _, _, active in periodic_bad_window_cells(speeds, delta=delta):
        if not states or states[-1] != active:
            states.append(active)
    if len(states) > 1 and states[0] == states[-1]:
        states.pop()
    return tuple(active[0] for active in states if len(active) == 1)


def handoff_transition_edges(
    speeds: tuple[int, ...], *, delta: Fraction
) -> tuple[tuple[int, int], ...]:
    """Undirected owner transitions in their first cyclic occurrence order."""
    owners = singleton_handoff_owners(speeds, delta=delta)
    if len(owners) < 2:
        return ()
    edges: list[tuple[int, int]] = []
    for first, second in zip(owners, owners[1:] + owners[:1]):
        if first == second:
            continue
        edge = tuple(sorted((first, second)))
        if edge not in edges:
            edges.append(edge)
    return tuple(edges)


def inductive_private_window_margin(runner_count: int) -> Fraction:
    """Slack at a private bad window supplied by the lower LRC case."""
    if runner_count < 2:
        raise ValueError("runner_count must be at least two")
    return Fraction(1, runner_count) - Fraction(1, runner_count + 1)


def _critical_times(speeds: tuple[int, ...]):
    """Yield every possible lower-envelope maximum time in [0,1].

    At a maximum, active affine pieces have opposing slopes; their equality
    has denominator ``v_i+v_j``. Taking ``i=j`` includes triangular-wave
    cusps with denominator ``2*v_i``.
    """
    yield Fraction(0)
    yield Fraction(1)
    for index, first in enumerate(speeds):
        for second in speeds[index:]:
            denominator = first + second
            for numerator in range(denominator + 1):
                yield Fraction(numerator, denominator)


def maximum_loneliness(speeds: tuple[int, ...]) -> Fraction:
    """Compute max_t min_i ||v_i t|| exactly from its critical times."""
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    return max(
        min(fractional_distance(speed * time) for speed in speeds)
        for time in set(_critical_times(speeds))
    )


def loneliness_at_most(speeds: tuple[int, ...], *, threshold: Fraction) -> bool:
    """Decide an upper bound exactly, returning early at a violating time."""
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    threshold = Fraction(threshold)
    return all(
        min(fractional_distance(speed * time) for speed in speeds) <= threshold
        for time in _critical_times(speeds)
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


def dissociated_riesz_forces_lrc(runner_count: int) -> bool:
    """Whether the elementary dissociated Riesz bound proves LRC.

    If the speeds have no nonzero relation with coefficients in ``{-1,0,1}``,
    the Riesz product ``prod_v (1-cos(2*pi*v*t))`` gives
    ``1 <= n(1-cos(2*pi*ML))``.  The inequalities
    ``1-cos(x) <= x^2/2`` and ``pi^2 < 10`` contradict
    ``ML < 1/(n+1)`` whenever ``(n+1)^2 >= 20n``.
    """
    if runner_count < 2:
        raise ValueError("runner_count must be at least two")
    return (runner_count + 1) ** 2 >= 20 * runner_count


def riesz_constant_term(speeds: tuple[int, ...]) -> Fraction:
    """Return the exact constant term of ``prod(1-cos(2*pi*v*t))``."""
    if any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be positive integers")
    total = Fraction()
    for signs in product((-1, 0, 1), repeat=len(speeds)):
        if sum(sign * speed for sign, speed in zip(signs, speeds)):
            continue
        support = sum(sign != 0 for sign in signs)
        total += Fraction((-1) ** support, 2**support)
    return total


def riesz_cover_ratio(speeds: tuple[int, ...]) -> Fraction:
    """Normalize a Riesz constant term by all one-factor deletions.

    A bad-arc cover at width ``delta`` requires this ratio to be at most
    ``1-cos(2*pi*delta)``.  Exact ratios expose how short relations weaken the
    dissociated-product argument before any transcendental comparison.
    """
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    denominator = sum(
        riesz_constant_term(speeds[:index] + speeds[index + 1 :])
        for index in range(len(speeds))
    )
    if not denominator:
        raise ZeroDivisionError("all one-factor deletion integrals vanish")
    return riesz_constant_term(speeds) / denominator


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


def _indecomposable_bounded_relations(
    speeds: tuple[int, ...], *, max_coefficient: int
) -> dict[int, tuple[int, ...]]:
    """Map each indecomposable support mask to one primitive relation."""
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    if max_coefficient < 1:
        raise ValueError("max_coefficient must be positive")

    relations_by_mask: dict[int, tuple[int, ...]] = {}
    coefficients = range(-max_coefficient, max_coefficient + 1)
    for relation in product(coefficients, repeat=len(speeds)):
        support = [index for index, coefficient in enumerate(relation) if coefficient]
        if len(support) < 2:
            continue
        if sum(coefficient * speed for coefficient, speed in zip(relation, speeds)):
            continue
        mask = sum(1 << index for index in support)
        if mask not in relations_by_mask:
            divisor = gcd(*(abs(coefficient) for coefficient in relation))
            primitive = tuple(coefficient // divisor for coefficient in relation)
            if next(coefficient for coefficient in primitive if coefficient) < 0:
                primitive = tuple(-coefficient for coefficient in primitive)
            relations_by_mask[mask] = primitive

    indecomposable: dict[int, tuple[int, ...]] = {}
    for mask, relation in relations_by_mask.items():
        decomposable = False
        submask = (mask - 1) & mask
        while submask:
            complement = mask ^ submask
            if submask in relations_by_mask and complement in relations_by_mask:
                decomposable = True
                break
            submask = (submask - 1) & mask
        if not decomposable:
            indecomposable[mask] = relation
    return indecomposable


def bounded_relation_components(
    speeds: tuple[int, ...], *, max_coefficient: int
) -> tuple[tuple[int, ...], ...]:
    """Components joined by indecomposable bounded relation supports.

    A support is decomposable when it splits into two disjoint nonempty
    supports that each carry a bounded relation. Such a relation may be only
    the sum of two unrelated certificates and must not connect their blocks.
    """
    relations = _indecomposable_bounded_relations(
        speeds, max_coefficient=max_coefficient
    )
    parent = list(range(len(speeds)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(first: int, second: int) -> None:
        first_root = find(first)
        second_root = find(second)
        if first_root != second_root:
            parent[second_root] = first_root

    for mask in relations:
        support = [index for index in range(len(speeds)) if mask & (1 << index)]
        for index in support[1:]:
            union(support[0], index)

    components: dict[int, list[int]] = {}
    for index in range(len(speeds)):
        components.setdefault(find(index), []).append(index)
    return tuple(sorted((tuple(component) for component in components.values())))


def bounded_relation_connectivity_certificate(
    speeds: tuple[int, ...], *, max_coefficient: int
) -> tuple[tuple[int, ...], ...] | None:
    """Return an exact spanning relation tree, or ``None`` if disconnected."""
    relations = _indecomposable_bounded_relations(
        speeds, max_coefficient=max_coefficient
    )
    parent = list(range(len(speeds)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    certificate: list[tuple[int, ...]] = []
    for mask, relation in sorted(
        relations.items(), key=lambda item: (item[0].bit_count(), item[0])
    ):
        support = [index for index in range(len(speeds)) if mask & (1 << index)]
        roots = {find(index) for index in support}
        if len(roots) < 2:
            continue
        root = support[0]
        for index in support[1:]:
            first_root = find(root)
            second_root = find(index)
            if first_root != second_root:
                parent[second_root] = first_root
        certificate.append(relation)
        if len({find(index) for index in range(len(speeds))}) == 1:
            return tuple(certificate)
    return None


def positive_triangular_relation_tree(
    speeds: tuple[int, ...], *, max_coefficient: int
) -> tuple[tuple[int, ...], ...] | None:
    """Span all runners by indecomposable relations solving for their maximum.

    Each returned relation is oriented with coefficient ``-1`` on the largest
    speed in its support and positive bounded coefficients on smaller speeds.
    """
    indecomposable_masks = set(
        _indecomposable_bounded_relations(
            speeds, max_coefficient=max_coefficient
        )
    )
    positive_by_mask: dict[int, tuple[int, ...]] = {}
    coefficients = range(-max_coefficient, max_coefficient + 1)
    for relation in product(coefficients, repeat=len(speeds)):
        support = [index for index, coefficient in enumerate(relation) if coefficient]
        if len(support) < 2:
            continue
        mask = sum(1 << index for index in support)
        if mask not in indecomposable_masks or mask in positive_by_mask:
            continue
        if sum(coefficient * speed for coefficient, speed in zip(relation, speeds)):
            continue
        largest = max(support, key=lambda index: speeds[index])
        oriented = relation
        if oriented[largest] == 1:
            oriented = tuple(-coefficient for coefficient in oriented)
        if oriented[largest] != -1:
            continue
        if any(
            coefficient < 0
            for index, coefficient in enumerate(oriented)
            if index != largest
        ):
            continue
        positive_by_mask[mask] = oriented

    parent = list(range(len(speeds)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    certificate: list[tuple[int, ...]] = []
    for mask, relation in sorted(
        positive_by_mask.items(), key=lambda item: (item[0].bit_count(), item[0])
    ):
        support = [index for index in range(len(speeds)) if mask & (1 << index)]
        roots = {find(index) for index in support}
        if len(roots) < 2:
            continue
        root = support[0]
        for index in support[1:]:
            first_root = find(root)
            second_root = find(index)
            if first_root != second_root:
                parent[second_root] = first_root
        certificate.append(relation)
        if len({find(index) for index in range(len(speeds))}) == 1:
            return tuple(certificate)
    return None


def positive_generation_certificate(
    speeds: tuple[int, ...], *, max_coefficient: int
) -> tuple[tuple[int, ...], tuple[tuple[int, tuple[int, ...]], ...]]:
    """Generate each possible speed from earlier ones, leaving minimal seeds.

    Since the speeds are strictly increasing, whether a target has a positive
    bounded representation depends only on earlier speeds. Every target that
    lacks one is necessarily a seed; choosing a representation whenever one
    exists therefore minimizes the seed count.
    """
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    if tuple(sorted(set(speeds))) != speeds:
        raise ValueError("speeds must be strictly increasing")
    if max_coefficient < 1:
        raise ValueError("max_coefficient must be positive")

    seeds: list[int] = []
    relations: list[tuple[int, tuple[int, ...]]] = []
    for target, speed in enumerate(speeds):
        representation = None
        for prefix in product(range(max_coefficient + 1), repeat=target):
            if sum(
                coefficient * speeds[index]
                for index, coefficient in enumerate(prefix)
            ) == speed:
                representation = prefix + (0,) * (len(speeds) - target)
                break
        if representation is None:
            seeds.append(target)
        else:
            relations.append((target, representation))
    return tuple(seeds), tuple(relations)


def bounded_relations(
    speeds: tuple[int, ...], *, max_coefficient: int
) -> tuple[tuple[int, ...], ...]:
    """All nonzero speed relations within a symmetric coefficient box."""
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    if max_coefficient < 1:
        raise ValueError("max_coefficient must be positive")

    coefficients = range(-max_coefficient, max_coefficient + 1)
    return tuple(
        relation
        for relation in product(coefficients, repeat=len(speeds))
        if any(relation)
        and not sum(
            coefficient * speed for coefficient, speed in zip(relation, speeds)
        )
    )


def _rational_row_basis(
    rows: tuple[tuple[int, ...], ...], *, width: int
) -> dict[int, list[Fraction]]:
    basis: dict[int, list[Fraction]] = {}
    for relation in rows:
        row = [Fraction(coefficient) for coefficient in relation]
        for pivot in sorted(basis):
            if row[pivot]:
                factor = row[pivot]
                row = [
                    entry - factor * basis_entry
                    for entry, basis_entry in zip(row, basis[pivot])
                ]
        pivot = next((index for index, entry in enumerate(row) if entry), None)
        if pivot is None:
            continue
        scale = row[pivot]
        basis[pivot] = [entry / scale for entry in row]
        if len(basis) == width:
            break
    return basis


def _reduced_row_echelon(
    rows: tuple[tuple[int, ...], ...], *, width: int
) -> tuple[tuple[Fraction, ...], ...]:
    matrix = [[Fraction(entry) for entry in row] for row in rows]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / scale for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                entry - scale * pivot_entry
                for entry, pivot_entry in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return tuple(tuple(row) for row in matrix[:pivot_row])


def _nullspace_pattern(
    row_basis: tuple[tuple[Fraction, ...], ...], *, width: int
) -> tuple[tuple[int, ...], ...]:
    pivots = [next(index for index, entry in enumerate(row) if entry) for row in row_basis]
    free = [index for index in range(width) if index not in pivots]
    columns: list[tuple[int, ...]] = []
    for free_index in free:
        column = [Fraction(0) for _ in range(width)]
        column[free_index] = 1
        for pivot, row in reversed(tuple(zip(pivots, row_basis))):
            column[pivot] = -sum(
                coefficient * entry
                for coefficient, entry in zip(row[pivot + 1 :], column[pivot + 1 :])
            )
        denominator = lcm(*(entry.denominator for entry in column))
        integer_column = [int(entry * denominator) for entry in column]
        divisor = gcd(*integer_column)
        integer_column = [entry // divisor for entry in integer_column]
        first = next(entry for entry in integer_column if entry)
        if first < 0:
            integer_column = [-entry for entry in integer_column]
        columns.append(tuple(integer_column))
    return tuple(columns)


def bounded_relation_rank(speeds: tuple[int, ...], *, max_coefficient: int) -> int:
    """Rank over Q of all speed relations within a coefficient box."""
    relations = bounded_relations(speeds, max_coefficient=max_coefficient)
    basis = _rational_row_basis(relations, width=len(speeds))
    return len(basis)


def _bounded_dissociated(
    speeds: tuple[int, ...], indices: tuple[int, ...], *, max_coefficient: int
) -> bool:
    coefficients = range(-max_coefficient, max_coefficient + 1)
    return not any(
        any(relation)
        and not sum(
            coefficient * speeds[index]
            for coefficient, index in zip(relation, indices)
        )
        for relation in product(coefficients, repeat=len(indices))
    )


def bounded_dissociated_generation_certificate(
    speeds: tuple[int, ...], *, max_coefficient: int
) -> tuple[tuple[int, ...], tuple[tuple[int, tuple[int, ...]], ...]]:
    """Find a smallest maximal bounded-dissociated seed set.

    For every nonseed target, maximality supplies a relation supported only on
    the seeds and that target. These star relations are automatically linearly
    independent because each has its own nonzero target coordinate.
    """
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    if max_coefficient < 1:
        raise ValueError("max_coefficient must be positive")
    coefficients = range(-max_coefficient, max_coefficient + 1)
    for size in range(1, len(speeds) + 1):
        for seeds in combinations(range(len(speeds)), size):
            if not _bounded_dissociated(
                speeds, seeds, max_coefficient=max_coefficient
            ):
                continue
            relations = []
            maximal = True
            for target in range(len(speeds)):
                if target in seeds:
                    continue
                support = seeds + (target,)
                supported_relation = None
                for local in product(coefficients, repeat=len(support)):
                    if not any(local) or not local[-1]:
                        continue
                    if sum(
                        coefficient * speeds[index]
                        for coefficient, index in zip(local, support)
                    ):
                        continue
                    full = [0] * len(speeds)
                    for coefficient, index in zip(local, support):
                        full[index] = coefficient
                    supported_relation = tuple(full)
                    break
                if supported_relation is None:
                    maximal = False
                    break
                relations.append((target, supported_relation))
            if maximal:
                return seeds, tuple(relations)
    raise RuntimeError("the full speed tuple should always be maximal dissociated")


def bounded_appendability_certificate(
    speeds: tuple[int, ...], *, max_coefficient: int, seed_count: int = 2
) -> tuple[tuple[int, ...], tuple[tuple[int, tuple[int, ...]], ...]] | None:
    """Find a bounded-relation elimination ordering from fixed-size seeds.

    A target is appendable when an exact bounded relation uses that target and
    only already available coordinates. Appendability is monotone as the
    available set grows, so greedily adding any available target cannot spoil
    a certificate for a chosen seed set.
    """
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    if max_coefficient < 1:
        raise ValueError("max_coefficient must be positive")
    if not 1 <= seed_count <= len(speeds):
        raise ValueError("seed_count must be between one and the number of speeds")

    relations = tuple(
        sorted(
            bounded_relations(speeds, max_coefficient=max_coefficient),
            key=lambda row: (
                sum(coefficient != 0 for coefficient in row),
                sum(abs(coefficient) for coefficient in row),
                row,
            ),
        )
    )
    for seeds in combinations(range(len(speeds)), seed_count):
        steps = _bounded_appendability_steps(
            speeds, seeds=seeds, relations=relations
        )
        if steps is not None:
            return seeds, steps
    return None


def _bounded_appendability_steps(
    speeds: tuple[int, ...],
    *,
    seeds: tuple[int, ...],
    relations: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, tuple[int, ...]], ...] | None:
    available = set(seeds)
    steps: list[tuple[int, tuple[int, ...]]] = []
    while len(available) < len(speeds):
        addition = None
        for target in range(len(speeds)):
            if target in available:
                continue
            relation = next(
                (
                    row
                    for row in relations
                    if row[target]
                    and all(
                        not coefficient
                        or index in available
                        or index == target
                        for index, coefficient in enumerate(row)
                    )
                ),
                None,
            )
            if relation is not None:
                addition = target, relation
                break
        if addition is None:
            return None
        target, relation = addition
        available.add(target)
        steps.append((target, relation))
    return tuple(steps)


def bounded_appendability_from_seeds(
    speeds: tuple[int, ...],
    *,
    seeds: tuple[int, ...],
    max_coefficient: int,
) -> tuple[tuple[int, tuple[int, ...]], ...] | None:
    """Try the bounded appendability closure from a specified seed set."""
    if not speeds or any(speed <= 0 for speed in speeds):
        raise ValueError("speeds must be a nonempty tuple of positive integers")
    if max_coefficient < 1:
        raise ValueError("max_coefficient must be positive")
    if not seeds or len(set(seeds)) != len(seeds):
        raise ValueError("seeds must be distinct indices")
    if any(index < 0 or index >= len(speeds) for index in seeds):
        raise ValueError("seed index out of range")
    relations = tuple(
        sorted(
            bounded_relations(speeds, max_coefficient=max_coefficient),
            key=lambda row: (
                sum(coefficient != 0 for coefficient in row),
                sum(abs(coefficient) for coefficient in row),
                row,
            ),
        )
    )
    return _bounded_appendability_steps(
        speeds, seeds=seeds, relations=relations
    )


def handoff_appendability_certificate(
    speeds: tuple[int, ...], *, delta: Fraction, max_coefficient: int
) -> tuple[tuple[int, int], tuple[tuple[int, tuple[int, ...]], ...]] | None:
    """Try successive singleton-owner handoffs as appendability seed pairs."""
    owners = singleton_handoff_owners(speeds, delta=delta)
    if len(owners) < 2:
        return None
    tried: set[tuple[int, int]] = set()
    for first, second in zip(owners, owners[1:] + owners[:1]):
        if first == second or (first, second) in tried:
            continue
        tried.add((first, second))
        steps = bounded_appendability_from_seeds(
            speeds,
            seeds=(first, second),
            max_coefficient=max_coefficient,
        )
        if steps is not None:
            return (first, second), steps
    return None


def handoff_elimination_certificate(
    speeds: tuple[int, ...], *, delta: Fraction, max_coefficient: int
) -> tuple[
    tuple[int, ...], tuple[tuple[int, tuple[int, ...]], ...]
] | None:
    """Use a cyclic handoff first-occurrence order as bounded elimination."""
    owners = singleton_handoff_owners(speeds, delta=delta)
    if len(owners) < len(speeds):
        return None
    relations = tuple(
        sorted(
            bounded_relations(speeds, max_coefficient=max_coefficient),
            key=lambda row: (
                sum(coefficient != 0 for coefficient in row),
                sum(abs(coefficient) for coefficient in row),
                row,
            ),
        )
    )
    for rotation in range(len(owners)):
        order: list[int] = []
        for owner in owners[rotation:] + owners[:rotation]:
            if owner not in order:
                order.append(owner)
        if len(order) != len(speeds):
            continue
        available = set(order[:2])
        steps: list[tuple[int, tuple[int, ...]]] = []
        for target in order[2:]:
            relation = next(
                (
                    row
                    for row in relations
                    if row[target]
                    and all(
                        not coefficient
                        or index in available
                        or index == target
                        for index, coefficient in enumerate(row)
                    )
                ),
                None,
            )
            if relation is None:
                break
            available.add(target)
            steps.append((target, relation))
        else:
            return tuple(order), tuple(steps)
    return None


def local_handoff_elimination_certificate(
    speeds: tuple[int, ...],
    *,
    delta: Fraction,
    max_coefficient: int,
    max_support: int,
) -> tuple[
    tuple[int, ...], tuple[tuple[int, tuple[int, ...]], ...]
] | None:
    """Require each handoff row to contain its predecessor and small support."""
    if max_support < 2:
        raise ValueError("max_support must be at least two")
    owners = singleton_handoff_owners(speeds, delta=delta)
    if len(owners) < len(speeds):
        return None
    relations = tuple(
        sorted(
            bounded_relations(speeds, max_coefficient=max_coefficient),
            key=lambda row: (
                sum(coefficient != 0 for coefficient in row),
                sum(abs(coefficient) for coefficient in row),
                row,
            ),
        )
    )
    for rotation in range(len(owners)):
        order: list[int] = []
        for owner in owners[rotation:] + owners[:rotation]:
            if owner not in order:
                order.append(owner)
        if len(order) != len(speeds):
            continue
        available = set(order[:2])
        steps: list[tuple[int, tuple[int, ...]]] = []
        for position, target in enumerate(order[2:], 2):
            predecessor = order[position - 1]
            relation = next(
                (
                    row
                    for row in relations
                    if row[target]
                    and row[predecessor]
                    and sum(coefficient != 0 for coefficient in row)
                    <= max_support
                    and all(
                        not coefficient
                        or index in available
                        or index == target
                        for index, coefficient in enumerate(row)
                    )
                ),
                None,
            )
            if relation is None:
                break
            available.add(target)
            steps.append((target, relation))
        else:
            return tuple(order), tuple(steps)
    return None


def bounded_relation_pattern(
    speeds: tuple[int, ...], *, max_coefficient: int
) -> tuple[tuple[int, ...], ...]:
    """Primitive integer basis for the subspace cut out by bounded relations.

    Each returned column is a coordinate pattern.  Their rational span is the
    common nullspace of every bounded relation and therefore contains the
    supplied speed vector.  Under H33 there are at most two columns.
    """
    relations = bounded_relations(speeds, max_coefficient=max_coefficient)
    row_basis = _reduced_row_echelon(relations, width=len(speeds))
    return _nullspace_pattern(row_basis, width=len(speeds))


@lru_cache(maxsize=None)
def coefficient_relation_patterns(
    *, coordinate_count: int, max_coefficient: int, nullity: int
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """Enumerate canonical nullspaces generated by bounded integer normals."""
    if coordinate_count < 2:
        raise ValueError("coordinate_count must be at least two")
    if max_coefficient < 1:
        raise ValueError("max_coefficient must be positive")
    rank = coordinate_count - nullity
    if rank < 1 or nullity < 1:
        raise ValueError("nullity must lie strictly between zero and coordinate_count")

    primitive_rows = set()
    coefficients = range(-max_coefficient, max_coefficient + 1)
    for row in product(coefficients, repeat=coordinate_count):
        if not any(row):
            continue
        divisor = gcd(*row)
        normalized = tuple(entry // divisor for entry in row)
        first = next(entry for entry in normalized if entry)
        if first < 0:
            normalized = tuple(-entry for entry in normalized)
        primitive_rows.add(normalized)

    spaces: dict[
        tuple[tuple[Fraction, ...], ...], tuple[tuple[int, ...], ...]
    ] = {}
    for generators in combinations(sorted(primitive_rows), rank):
        row_basis = _reduced_row_echelon(generators, width=coordinate_count)
        if len(row_basis) != rank or row_basis in spaces:
            continue
        spaces[row_basis] = _nullspace_pattern(row_basis, width=coordinate_count)
    return tuple(sorted(spaces.values()))


def pattern_positive_distinct_witness(
    pattern: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[Fraction, Fraction] | None:
    """Find a rational parameter direction giving positive distinct coordinates."""
    if len(pattern) != 2 or not pattern[0] or len(pattern[0]) != len(pattern[1]):
        raise ValueError("pattern must contain two equal nonempty columns")
    forms = tuple(zip(*pattern))
    if len(set(forms)) != len(forms):
        return None

    boundaries = set()
    linear_forms = list(forms)
    linear_forms.extend(
        (first[0] - second[0], first[1] - second[1])
        for first, second in combinations(forms, 2)
    )
    for first, second in linear_forms:
        if second:
            boundaries.add(Fraction(-first, second))
    ordered = sorted(boundaries)
    candidates = [Fraction(0)] if not ordered else [ordered[0] - 1, ordered[-1] + 1]
    candidates.extend(
        (left + right) / 2 for left, right in zip(ordered, ordered[1:])
    )
    parameter_pairs = [(Fraction(sign), sign * slope) for slope in candidates for sign in (1, -1)]
    parameter_pairs.extend(((Fraction(0), Fraction(1)), (Fraction(0), Fraction(-1))))
    for parameters in parameter_pairs:
        values = [
            first * parameters[0] + second * parameters[1]
            for first, second in forms
        ]
        if all(value > 0 for value in values) and len(set(values)) == len(values):
            return parameters
    return None


def _pattern_subspace_key(
    pattern: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[tuple[Fraction, ...], ...]:
    return _reduced_row_echelon(tuple(pattern), width=len(pattern[0]))


@lru_cache(maxsize=None)
def admissible_pattern_symmetry_representatives(
    *, coordinate_count: int, max_coefficient: int, nullity: int
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """Quotient positive-distinct patterns by signed coordinate permutations.

    Permuting coordinates or changing their signs preserves every distance to
    the nearest integer, so it preserves the ambient maximum loneliness.
    """
    if nullity != 2:
        raise ValueError("ambient pattern symmetry reduction currently requires nullity two")
    patterns = coefficient_relation_patterns(
        coordinate_count=coordinate_count,
        max_coefficient=max_coefficient,
        nullity=nullity,
    )
    admissible = tuple(
        pattern
        for pattern in patterns
        if pattern_positive_distinct_witness(pattern) is not None
    )
    seen: set[tuple[tuple[Fraction, ...], ...]] = set()
    representatives = []
    for pattern in admissible:
        key = _pattern_subspace_key(pattern)
        if key in seen:
            continue
        for permutation in permutations(range(coordinate_count)):
            for signs in product((1, -1), repeat=coordinate_count):
                transformed = tuple(
                    tuple(
                        signs[index] * column[permutation[index]]
                        for index in range(coordinate_count)
                    )
                    for column in pattern
                )
                seen.add(_pattern_subspace_key(transformed))
        representatives.append(pattern)
    return tuple(representatives)


def _solve_three_equations(
    equations: tuple[tuple[tuple[Fraction, Fraction, Fraction], Fraction], ...]
) -> tuple[Fraction, Fraction, Fraction] | None:
    matrix = [[*coefficients, bound] for coefficients, bound in equations]
    for column in range(3):
        pivot = next(
            (row for row in range(column, 3) if matrix[row][column]), None
        )
        if pivot is None:
            return None
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = matrix[column][column]
        matrix[column] = [entry / scale for entry in matrix[column]]
        for row in range(3):
            if row == column or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                entry - scale * pivot_entry
                for entry, pivot_entry in zip(matrix[row], matrix[column])
            ]
    return tuple(matrix[row][3] for row in range(3))


def pattern_maximum_loneliness(
    pattern: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[Fraction, tuple[Fraction, Fraction]]:
    """Exactly maximize loneliness on a two-dimensional rational subtorus.

    ``pattern`` consists of two integer coordinate columns.  The routine
    partitions the unit square by the integer parts of every coordinate form
    and solves the resulting three-variable rational linear programs by
    enumerating their vertices.
    """
    if len(pattern) != 2 or not pattern[0] or len(pattern[0]) != len(pattern[1]):
        raise ValueError("pattern must contain two equal nonempty columns")
    forms = tuple(zip(*pattern))
    floor_ranges = []
    for first, second in forms:
        lower = min(0, first) + min(0, second)
        upper = max(0, first) + max(0, second)
        floor_ranges.append(range(lower - 1, upper + 1))

    best = Fraction(-1)
    witness = (Fraction(0), Fraction(0))
    base_constraints = (
        ((Fraction(-1), Fraction(0), Fraction(0)), Fraction(0)),
        ((Fraction(1), Fraction(0), Fraction(0)), Fraction(1)),
        ((Fraction(0), Fraction(-1), Fraction(0)), Fraction(0)),
        ((Fraction(0), Fraction(1), Fraction(0)), Fraction(1)),
        ((Fraction(0), Fraction(0), Fraction(-1)), Fraction(0)),
        ((Fraction(0), Fraction(0), Fraction(1)), Fraction(1, 2)),
    )
    for floors in product(*floor_ranges):
        constraints = list(base_constraints)
        for (first, second), floor in zip(forms, floors):
            constraints.extend(
                (
                    ((Fraction(-first), Fraction(-second), Fraction(1)), Fraction(-floor)),
                    ((Fraction(first), Fraction(second), Fraction(1)), Fraction(floor + 1)),
                )
            )
        for active in combinations(constraints, 3):
            point = _solve_three_equations(active)
            if point is None:
                continue
            if any(
                sum(coefficient * value for coefficient, value in zip(coefficients, point))
                > bound
                for coefficients, bound in constraints
            ):
                continue
            if point[2] > best:
                best = point[2]
                witness = point[:2]
    if best < 0:
        raise RuntimeError("two-torus linear programs had no feasible cell")
    return best, witness


def pattern_parameter_norm_squared_cutoff(
    pattern: tuple[tuple[int, ...], tuple[int, ...]], *, threshold: Fraction
) -> Fraction:
    """Sufficient squared parameter norm above which the pattern is safe.

    A primitive geodesic with parameter vector ``(A,B)`` has covering radius
    ``1/(2*sqrt(A^2+B^2))`` in the flat two-torus.  Each coordinate form is
    Lipschitz with constant at most the largest Euclidean row norm.  Therefore
    an ambient margin ``rho`` is inherited whenever
    ``A^2+B^2 > L^2/(4*rho^2)``.
    """
    value, _ = pattern_maximum_loneliness(pattern)
    threshold = Fraction(threshold)
    margin = value - threshold
    if margin <= 0:
        raise ValueError("ambient pattern maximum must strictly exceed threshold")
    row_norm_squared = max(
        first * first + second * second for first, second in zip(*pattern)
    )
    return Fraction(row_norm_squared, 4) / (margin * margin)


def first_band_survivors(*, runner_count: int, height: int):
    """Yield primitive tuples at or below the first spectral-band ceiling."""
    if runner_count < 1:
        raise ValueError("runner_count must be positive")
    if height < runner_count:
        raise ValueError("height must accommodate distinct positive speeds")
    threshold = Fraction(2, 2 * runner_count + 1)
    for speeds in combinations(range(1, height + 1), runner_count):
        if gcd(*speeds) != 1:
            continue
        if loneliness_at_most(speeds, threshold=threshold):
            yield speeds, maximum_loneliness(speeds)


def first_band_survivors_by_sum(*, runner_count: int, sum_bound: int):
    """Yield primitive first-band tuples with a bounded sum of speeds."""
    if runner_count < 1:
        raise ValueError("runner_count must be positive")
    if sum_bound < runner_count * (runner_count + 1) // 2:
        raise ValueError("sum_bound cannot accommodate distinct positive speeds")
    threshold = Fraction(2, 2 * runner_count + 1)
    for speeds in combinations(range(1, sum_bound + 1), runner_count):
        if sum(speeds) > sum_bound:
            continue
        if gcd(*speeds) != 1:
            continue
        if loneliness_at_most(speeds, threshold=threshold):
            yield speeds, maximum_loneliness(speeds)


def inductive_counterexample_sum_bound(runner_count: int) -> int:
    """Malikiosis--Santos--Schymura finite-checking bound under induction.

    Their theorem bounds the sum of a primitive counterexample's speeds by
    ``binom(n+1,2)^(n-1)`` once LRC is known for fewer speeds.
    """
    if runner_count < 2:
        raise ValueError("runner_count must be at least two")
    return comb(runner_count + 1, 2) ** (runner_count - 1)


def inductive_first_band_height_bound(runner_count: int) -> int:
    """Coarse norm bound from quantitative Kronecker and `(n-1)`-LRC.

    This is a theorem only under the induction hypothesis that LRC holds for
    fewer runners. The integer expression uses a cube lower bound for the
    Euclidean unit-ball volume, avoiding floating-point constants.
    """
    if runner_count < 2:
        raise ValueError("runner_count must be at least two")
    return (
        runner_count * (runner_count - 1) * (2 * runner_count + 1)
    ) ** (runner_count - 1)


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
