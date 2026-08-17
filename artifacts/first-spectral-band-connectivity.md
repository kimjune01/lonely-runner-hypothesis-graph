# Bounded relation rank in the first spectral band

Date: 2026-08-16

## Current hypothesis

For `n` positive integer speeds with

```text
ML(v_1,...,v_n) <= 2/(2n+1),
```

let `R_2(v)` be the rational span of the integer relations

```text
a dot v = 0,       a_i in {-2,-1,0,1,2}.
```

The current hypothesis is

```text
rank R_2(v) >= n-2.
```

Equivalently, the speed vector lies in a rational subspace of dimension at
most two defined by coefficient-two normals. Since only finitely many such
normal matrices exist for fixed `n`, this reduces every first-band tuple to a
finite list of two-parameter coefficient patterns.

Every hypothetical LRC counterexample lies strictly below the first-band
ceiling. A proof would therefore place its cyclic orbit inside one of finitely
many 2-dimensional rational subtori. Jain and Kravitz prove that the Lonely
Runner spectrum relative to each fixed 2-dimensional subtorus can be
characterized by a finite calculation. The remaining task would be to exclude
values below `1/(n+1)` uniformly across the finite coefficient patterns.

## Certificate semantics correction

The first checker joined the support of every bounded relation. That was
wrong: summing two unrelated relations creates a relation whose support
crosses both blocks. For example,

```text
(1,2,100,200)
```

has internal relations `2*1-2=0` and `2*100-200=0`; their sum is not evidence
that the two blocks interact.

The corrected connectivity checker uses only **indecomposable supports**. A
support is discarded if it partitions into two disjoint nonempty supports
that each carry a bounded relation. The regression above now yields the two
components `{1,2}` and `{100,200}`. All reported scans were rerun after this
correction.

This correction also motivated the rank formulation. Linear rank is invariant
under adding decomposable certificates and directly measures the number of
parameters left after elimination.

## Exact scan evidence

Complete primitive scans used the first-band cutoff `2/(2n+1)`:

| speeds `n` | height | primitive first-band tuples | rank below `n-2` | missing positive tree |
|---:|---:|---:|---:|---:|
| 3 | 100 | 5 | 0 | 0 |
| 4 | 35 | 6 | 0 | 0 |
| 5 | 30 | 8 | 0 | 0 |
| 6 | 22 | 10 | 0 | 0 |
| 7 | 20 | 13 | 0 | 0 |

Thus all `42` survivors have coefficient-two relation rank at least `n-2`.
They also have a spanning tree of indecomposable relations that can each be
oriented as

```text
v_max = sum_i c_i v_i,       c_i in {1,2}, v_i < v_max.
```

Representative noncanonical fixtures include

```text
(1,3,4,5,18)                ML=2/11
(1,5,6,11,16,17)            ML=5/33
(1,3,4,5,7,13,18)           ML=3/23
(2,5,6,8,10,11)             ML=2/13
(2,6,7,8,10,13,14)          ML=2/15
```

The last two reveal why rank, rather than positive generation, is the stable
invariant.

The stronger claim `rank R_2(v)=n-1` is already false. The four-speed survivor

```text
(3,4,7,11),       ML=2/9,
```

has rank exactly `2=n-2`. A primitive integer basis for the common nullspace
of its coefficient-two relations is

```text
(2,-1,1,0),       (1,-1,0,-1).
```

Thus the two-dimensional conclusion is sharp in the completed scans;
relative-subtorus descent cannot be replaced by a finite list of rays.

Run a replay with:

```text
uv run scan_first_band.py --runners 6 --height 22
```

The CLI emits exact TSV rows containing maximum loneliness, relation rank,
corrected components, positive-seed count, and positive-tree status.

## Killed strengthenings

### Whole near-tight interval

Uniform bounded connectivity fails if the cutoff is weakened to `ML(v)<1/n`:

```text
ML(1,2,3s) = s/(3s+1) < 1/3.
```

The coefficient needed to connect `3s` grows with `s`; these values accumulate
at the lower-dimensional threshold `1/3`. The first-band cutoff retains only
`s<=2` from this family.

### Two positive seeds

It is also false that every first-band tuple can be generated from at most two
earlier positive seeds using coefficients `0,1,2`. The first exact obstruction
is

```text
(2,5,6,8,10,11),       ML=2/13.
```

The speeds `2,5,6` are all positive seeds. Nevertheless signed elimination
leaves only two parameters:

```text
6 = 2*5 - 2*2,
8 = 2 + 6,
10 = 2*5,
11 = 5 + 6.
```

The seven-speed tuple `(2,6,7,8,10,13,14)` gives the same positive-seed
failure at `ML=2/15` while retaining relation rank `n-2`.

## Coarse theorem under induction

Assume LRC for `n-1` speeds and put

```text
beta = 2/(2n+1),
g = 1/n-beta = 1/[n(2n+1)],
epsilon = g/2.
```

If a primitive first-band vector has Euclidean norm `V`, the quantitative
Kronecker argument of Giri--Kravitz shows that whenever

```text
V * omega_(n-1) * epsilon^(n-1) > 1,
```

its cyclic subtorus is `epsilon`-dense in a higher-dimensional subtorus.
Induction bounds that subtorus's maximum loneliness below by `1/n`, so the
original tuple would have loneliness at least

```text
1/n-epsilon > beta,
```

a contradiction. Using the cube lower bound
`omega_d >= (2/d)^d` gives the explicit coarse result

```text
||v||_2 <= [n(n-1)(2n+1)]^(n-1).
```

This already proves that some coefficient bound depending on `n` gives full
relation rank. It does not explain why the exact first band appears to need
only coefficient `2` or why codimension `n-2` is the natural sharp threshold.

## Proposed proof mechanism

Use a cluster version of the triangular-bump Fourier expansion. If the
coefficient-two relation span has rank at most `n-3`, its low-frequency terms
retain at least three independent parameters. Proper clusters contain fewer
than `n` runners, while the first-band ceiling is separated from their
lower-dimensional LRC threshold. A uniform positive lower bound for the
cluster means should force another independent bounded frequency relation,
raising the rank.

The immediate lemma to prove is therefore:

> At first-band width, a vanishing full tent-product whose coefficient-two
> relation span has rank `r<n-2` forces a new coefficient-two relation outside
> that span.

A weaker coefficient bound `C(n)` follows from the coarse height theorem. The
hard and potentially decisive claim is the sharp cutoff `C=2`.

## Exact two-torus bridge

For a two-column integer pattern, write its coordinate rows as `(a_i,b_i)` and
define

```text
F(x,y) = min_i ||a_i x+b_i y||.
```

The exact checker partitions `[0,1]^2` by the integer parts of all coordinate
forms. On each cell, maximizing `F` is a rational linear program in
`(x,y,r)`. Enumerating triples of active inequalities returns an exact maximum
and witness.

Only three tuples in the completed scans have bounded-relation rank exactly
`n-2`:

| tuple | ambient maximum | margin above `1/(n+1)` |
|---|---:|---:|
| `(1,5,6)` | `1/3` | `1/12` |
| `(2,3,5)` | `1/3` | `1/12` |
| `(3,4,7,11)` | `1/4` | `1/20` |

This strict margin gives an elementary finite descent. A primitive parameter
pair `(A,B)` traces a closed geodesic whose flat-torus covering radius is
`1/(2 sqrt(A^2+B^2))`. If `L^2=max_i(a_i^2+b_i^2)` and the ambient margin is
`rho`, the coordinate forms remain safe in a Euclidean ball of radius
`rho/L`. Hence the geodesic is automatically safe whenever

```text
A^2+B^2 > L^2/(4 rho^2).
```

For the sharp four-speed pattern the squared cutoff is `500`. Every larger
parameter pair is safe, and only finitely many primitive pairs at or below
that cutoff need exact checking. This is more explicit for positive-margin
patterns than invoking the finite-symmetric-difference statement of the
relative-spectrum theorem.

The new frontier is the zero-margin case: prove that every H33 pattern has
ambient maximum strictly above `1/(n+1)`, or show that equality forces an
additional bounded relation or a lower-dimensional reduction.

## Sources

- Vanshika Jain and Noah Kravitz, [*Relative Lonely Runner
  spectra*](https://arxiv.org/abs/2411.12684).
- Vikram Giri and Noah Kravitz, [*The structure of Lonely Runner
  spectra*](https://arxiv.org/abs/2304.01462).
- Noah Kravitz, [*Barely lonely runners and very lonely
  runners*](https://arxiv.org/abs/1912.06034).
- Ho Tin Fan and Alec Sun, [*Amending the Lonely Runner Spectrum
  Conjecture*](https://arxiv.org/abs/2306.10417).
