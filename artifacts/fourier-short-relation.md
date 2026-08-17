# A bounded Fourier relation for bad or tight tuples

Date: 2026-08-16

## Theorem

Fix `n>=1` and `0<=delta<1/2`. Define

```text
a = 1/2-delta,
S = a + 1/(3a),
K = floor(2n S^(n-1) / (9 a^(n+1))) + 1.
```

If positive integer speeds `v=(v_1,...,v_n)` satisfy

```text
ML(v) <= delta,
```

then there is a nonzero integer vector `m=(m_1,...,m_n)` with

```text
sum_i m_i v_i = 0,       max_i |m_i| <= K.
```

Thus, at the Lonely Runner threshold `delta=1/(n+1)`, every hypothetical
counterexample—and every tight tuple—lies in one of finitely many rational
hyperplanes with a normal vector bounded solely in terms of `n`.

## Proof

Let `f` be the periodic triangular bump of height one centered at `1/2` and
half-width `a`. It is positive on `(delta,1-delta)`, zero outside that interval,
and zero at the two endpoints.

If `ML(v)<=delta`, then

```text
product_i f(v_i t) = 0
```

for every `t`. When the minimum distance is below `delta`, a factor is outside
the support; at a tight witness, a factor lies on its boundary.

The Fourier coefficients of the tent are

```text
f_hat(0) = a,
|f_hat(q)| = a * sinc(pi*a*q)^2 <= 1/(a*pi^2*q^2)  for q != 0.
```

They are absolutely summable. Using the Basel sum gives

```text
sum_q |f_hat(q)| <= a + 1/(3a) = S.
```

Using `pi^2>9` and `sum_{q>K} 1/q^2 < 1/K` gives

```text
sum_{|q|>K} |f_hat(q)| < 2/(9aK).
```

Expand the product and integrate over one period. Only frequency vectors
`m in Z^n` satisfying `sum_i m_i v_i=0` remain. The zero vector contributes
the positive constant term `a^n`.

Suppose no nonzero surviving frequency has all coordinates at most `K` in
absolute value. Every nonconstant term then has at least one tail coordinate.
A union bound over that coordinate makes the absolute sum of all nonconstant
terms smaller than

```text
n * 2/(9aK) * S^(n-1) < a^n
```

by the definition of `K`. The integral is therefore positive, contradicting
the identically zero product. A bounded nonzero relation must exist. QED.

## Explicit LRC bounds

For `delta=1/(n+1)`, the first bounds are:

| `n` speeds | `K(n)` |
|---:|---:|
| 2 | 209 |
| 3 | 428 |
| 4 | 1,028 |
| 5 | 2,561 |
| 6 | 6,439 |
| 7 | 16,214 |
| 8 | 40,753 |
| 9 | 102,112 |
| 10 | 254,978 |
| 11 | 634,500 |
| 12 | 1,573,723 |
| 13 | 3,891,190 |

These are deliberately coarse analytic bounds, not optimized constants.

## What this does and does not prove

The theorem supplies the previously missing bounded-relation statement
without primes, finite checking, or a hypothetical counterexample fixture.
It does not turn the relation into a smaller counterexample. That requires a
new relative-subtorus theorem: for each bounded normal `m`, control all cyclic
subtori contained in `m dot x=0`, or define a transformation that preserves a
bad cover while reducing runner count or speed height.

`fourier_relation_bound` evaluates `K` exactly with rational arithmetic.
`find_bounded_relation` is a small diagnostic search used on fixtures; it is
not intended to enumerate the full analytic bound.
