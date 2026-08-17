# A coefficient-one relation in every large counterexample

Date: 2026-08-16

## Theorem

Let `V` be `n>=18` distinct positive integer speeds. If `V` is an LRC
counterexample, then there is a nonzero vector

```text
epsilon in {-1,0,1}^n,       sum_v epsilon_v v = 0.
```

Thus every hypothetical counterexample with at least eighteen speeds has an
exact equality between two disjoint nonempty subset sums. This improves the
large coefficient supplied by the earlier triangular-bump Fourier theorem to
coefficient one, but currently forces only one independent relation.

## Proof

Suppose no such relation exists. Then `V` is dissociated. Define the
nonnegative Riesz product

```text
R(t) = product_(v in V) (1-cos(2 pi v t)).
```

Dissociativity says that the constant Fourier coefficient of `R`, and of the
product with any one factor removed, is `1`. Hence all those products have
integral `1`.

Put `delta=ML(V)`. The bad sets `{t: ||vt||<=delta}` cover the circle. Multiply
their summed indicators by `R` and integrate. On the bad set for `v`, its own
factor is at most `1-cos(2 pi delta)`. Removing that factor leaves a product of
integral `1`, so

```text
1 <= n(1-cos(2 pi delta)).
```

If `delta<1/(n+1)`, then, using `1-cos x <= x^2/2` and `pi^2<10`,

```text
n(1-cos(2 pi delta))
  < 2 pi^2 n/(n+1)^2
  < 20n/(n+1)^2
  <= 1
```

whenever `(n+1)^2>=20n`. This holds at `n=18`, and the left-to-right ratio
improves with `n`. The contradiction proves the theorem.

## Scope

The argument does not prove H39's desired rank `n-2`; it establishes rank at
least one. Its value is qualitative and uniform: the first relation has the
sharp coefficient alphabet `{-1,0,1}` and requires neither primes nor a finite
height reduction. The next problem is to quotient or cluster this Riesz
argument without losing control of the remaining runners.

## Source

The dissociated Riesz-product mechanism is Lemma 4.1 of Benjamin Bedert,
[*Riesz products and the Lonely Runner Conjecture: A wider gap of
loneliness*](https://arxiv.org/abs/2511.16636). The explicit `n>=18` threshold
above follows by retaining the elementary constants in that argument.
