# A union-bound lemma for several fast runners

Date: 2026-08-16

## Theorem

Let `v_1<...<v_N` be positive integer speeds. Split them after `m=N-r`, so
the last `r` runners are called fast, and assume `2r<N+1`. Put

```text
L = ML(v_1,...,v_m),
M = v_m,
delta = 1/(N+1),
eta = (L-delta)/M.
```

If

```text
eta * (1-2r*delta) > delta * sum_{j=m+1}^N 1/v_j,
```

then `ML(v_1,...,v_N)>=delta`.

## Proof

Choose `t_0` where the slow tuple attains `L`, and take the interval
`I=[t_0-eta,t_0+eta]`, of length `ell=2eta`. Distance to the nearest integer
is 1-Lipschitz. For every slow speed `v_i<=M` and every `t` in `I`,

```text
||v_i t|| >= ||v_i t_0|| - v_i |t-t_0|
            >= L-M*eta
            = delta.
```

It remains to find a point of `I` where all fast runners are valid.

For one speed `v`, the bad set `{t: ||vt||<delta}` is periodic with period
`1/v` and occupies length `2delta/v` per period. Decompose an arbitrary
interval of length `ell` into complete periods and one remainder. Its bad
measure is at most

```text
2delta*ell + 2delta/v.
```

The union of the `r` fast bad sets inside `I` consequently has measure at
most

```text
2r*delta*ell + 2delta*sum_fast(1/v).
```

The stated inequality, after multiplying by two, says this is strictly less
than `ell`. Some point of `I` avoids every fast bad set, while all slow
runners remain valid there. That point is a Lonely Runner witness. QED.

## Inductive gap corollary

Assume LRC for the `m` slow runners, so `L>=1/(m+1)`. If every fast speed is
at least `V`, the theorem's condition follows from

```text
V > M * (m+1) * (N+1) / (N+1-2r).
```

Indeed,

```text
eta >= r / ((m+1)(N+1)M),
sum_fast(1/v) <= r/V.
```

Thus any hypothetical `N`-speed counterexample, under induction for fewer
runners, must satisfy the reverse gap bound at every cut with
`r<(N+1)/2` speeds above it.

This is a general, non-prime structural restriction. It does not control a
cut whose upper side contains at least half the runners, because then the
main measure coefficient `1-2r*delta` is nonpositive.

## Verification

`multi_fast_union_condition` implements the exact rational inequality. The
test suite checks its conclusion wherever it triggers among all four-speed
tuples of height at most `14` and five-speed tuples of height at most `10`.
It also checks genuine two-fast cases `(1,2,100,101)` and
`(1,2,3,120,121)`.

## Sources and relation to prior work

Fan and Sun's one- and two-very-fast-runner lemmas use local time
perturbations. The theorem above supplies a single measure argument for any
number `r` below the half-runner barrier. It is presented here as a derived
lemma, not as a claim of literature novelty.

- Ho Tin Fan and Alec Sun, [*Amending the Lonely Runner Spectrum
  Conjecture*](https://arxiv.org/abs/2306.10417), Section 3.1.
- Vikram Giri and Noah Kravitz, [*The structure of Lonely Runner
  spectra*](https://arxiv.org/abs/2304.01462), Section 7.
