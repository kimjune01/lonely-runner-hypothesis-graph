# Connected relations in the first spectral band

Date: 2026-08-16

## Hypothesis

For `n` positive integer speeds with

```text
ML(v_1,...,v_n) <= 2/(2n+1),
```

form a hypergraph on the `n` runner indices. For every integer relation

```text
sum_i a_i v_i = 0,       |a_i| <= 2,
```

add its nonzero support as a hyperedge. The hypothesis is that this
hypergraph is connected.

This is stronger than the bounded-relation theorem: one short relation may
involve only a proper subset, whereas connectivity couples every speed. A
connected coefficient-two graph bounds all speed ratios through a chain and
would reduce first-band analysis to finitely many normalized patterns.

## Why the cutoff is necessary

The corresponding claim on the whole interval `ML(v)<1/n` is false. For
three speeds,

```text
ML(1,2,3s) = s/(3s+1) < 1/3.
```

The third speed requires coefficients growing with `s` to join the component
containing `1,2`. For example, `(1,2,18)` has maximum loneliness `6/19` and
is still disconnected when coefficients up to `5` are allowed. This family
converges to the lower-dimensional accumulation value `1/3`.

The first-band cutoff keeps only `s<=2` from this family. It is also the first
non-tight value predicted by the original spectrum pattern, while allowing
the amended-spectrum exceptions found in later work.

## Exact evidence

The following primitive tuples were found below the midpoint between the LRC
threshold and the lower-dimensional threshold:

```text
n=3, height <= 30:
(1,2,3) (1,2,6) (1,3,4) (1,5,6) (2,3,5)

n=4, height <= 22:
(1,2,3,4) (1,2,3,8) (1,3,4,5)
(1,3,4,7) (1,4,5,6) (3,4,7,11)

n=5, height <= 13:
(1,2,3,4,5) (1,2,3,4,10) (1,2,3,5,8)
(1,3,4,5,7) (1,3,4,5,9) (1,3,4,7,10)
(1,4,5,6,7)
```

Every tuple has a connected coefficient-two relation hypergraph. Only
`(1,2,6)` and `(1,2,3,8)` require coefficient `2`; the other listed tuples
are connected by coefficient-one relations.

The published seven-speed exception

```text
(1,3,4,5,7,13,18),       ML=3/23 < 2/15,
```

is also connected by coefficient-one relations.

`bounded_relation_components` performs the exact relation enumeration. The
test suite preserves representative fixtures and the `(1,2,18)` cutoff
failure.

## Proposed proof mechanism

Use a cluster version of the triangular-bump Fourier expansion. If bounded
relations split into multiple components, the low-frequency expansion
factorizes across those components. Because each component contains fewer
than `n` runners and the first-band cutoff is separated from its LRC
threshold, its good-time factor should have uniformly positive mean. The
zero mean of the full product would then require a bounded cross-component
frequency, contradicting the definition of the components.

The missing lemma is the uniform positive component-mean bound with constants
strong enough to keep the cross-component coefficient at `2`. A weaker bound
depending only on `n` would still prove connectedness for some explicit
coefficient `C(n)` and would already strengthen H28 materially.

## Sources

- Ho Tin Fan and Alec Sun, [*Amending the Lonely Runner Spectrum
  Conjecture*](https://arxiv.org/abs/2306.10417).
- Vikram Giri and Noah Kravitz, [*The structure of Lonely Runner
  spectra*](https://arxiv.org/abs/2304.01462).
