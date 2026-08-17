# General-case hypotheses after the universal-grid failure

Date: 2026-08-16

## Result: a height-sensitive grid theorem

For a positive integer tuple `v=(v_1,...,v_k)`, write

```text
L(v) = max_t min_i ||v_i t||,      M = max_i v_i.
```

If `L(v)>1/(k+1)`, then every integer denominator

```text
d > (k+1) M^2
```

has a strict witness in `(1/d)Z`.

The function `min_i ||v_i t||` is the lower envelope of finitely many affine
pieces. Its maximum occurs at a cusp or where two pieces agree. The critical
time therefore has denominator dividing one of

```text
2v_i,       v_i+v_j,       |v_i-v_j|,
```

and hence at most `2M`. The rational value `L(v)` also has denominator at
most `2M`. A positive gap over `1/(k+1)` is consequently at least
`1/(2M(k+1))`.

Round a maximizing time to the nearest `d`-grid point. Since distance to the
nearest integer is 1-Lipschitz, every runner loses at most `M/(2d)`. This is
strictly smaller than the gap when `d>(k+1)M^2`.

This proves the quantifier-swapped, height-sensitive repair of Conjecture 7.1:
each fixed non-tight tuple eventually appears on every sufficiently fine grid.
It does not prove that a tuple is non-tight.

## Downgraded hypothesis: bounded dual relation

The next target is:

> For each `k`, if `L(v)<1/(k+1)`, then the actual integer vector `v` has a
> nonzero relation `a dot v=0` with `||a||_1<=C(k)` and a sign pattern that
> permits runner contraction, polynomial degeneracy, or descent.

The audit found that this is not operational as stated. Its antecedent is an
actual counterexample to LRC, so a negative finite fixture would already
disprove the main conjecture. Its weak conclusion is also cheap: every integer
vector has two-coordinate relations, and known finite-checking bounds already
bound their coefficients under induction. The phrase “permits descent” hides
the entire missing transformation and preservation proof.

The suggested single-critical-time mechanism also fails. Active edge
equations are differences of vertex potentials, so summing any cycle gives
`0=0`. Known tight tuples have only active pairs at individual maximizing
times. A useful relation would need to couple several distinct critical times
or carry additional inequality data.

## Other live hypotheses

1. **Multi-fast-runner exclusion.** This is now proved: if fewer than half the
   runners lie above a sufficiently large multiplicative gap, interval measure
   produces a witness. See `artifacts/multi-fast-runner-lemma.md`.
2. **Height-stabilized lifting.** Once a modulus exceeds twice the tuple
   height, centered residues must be literal zero-extensions of fixed
   integers. A bounded number of stabilized levels should yield a witness or
   an exact polynomial degeneracy.
3. **Short-relation descent.** Each sign-compatible bounded relation from a
   finite list should transform a counterexample into one with fewer runners
   or smaller height.

The next missing component is a complementary restriction on speed cuts whose
upper side contains at least half the runners. The lifting version remains a
secondary encoding because raw profinite compactness has already failed.

## Prime boundary

Prime facts are needed by the current prime-modular sieve route, not known to
be necessary for the general conjecture. The Archimedean dual, critical-graph,
and height-descent hypotheses do not assume prime distribution. Any branch
that becomes a standalone open problem about primes is left open on purpose.
