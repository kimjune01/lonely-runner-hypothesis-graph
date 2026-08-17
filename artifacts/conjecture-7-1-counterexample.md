# Counterexample to the universal grid-witness conjecture

Date: 2026-08-16

## Statement under test

Conjecture 7.1 of Sungkawichai and Trakulthongchai (arXiv:2604.23906v1)
states that for each fixed `k+1` there is a constant `D` such that, for every
integer `d >= D`, every coprime non-tight positive `k`-speed tuple has a
witness time in `(1/d) Z`.

The conjecture is false as written, already for `k=2` (three runners).

## Infinite counterexample family

For any integer `r >= 1`, put

```text
d = 6r + 1,        v = (1, 3r).
```

The tuple is coprime not only internally but also to the denominator:

```text
gcd(1, 3r) = 1,
gcd(d, 1 * 3r) = gcd(6r+1, 3r) = 1.
```

Thus the family also defeats the natural repair that every speed be a unit
modulo `d`.

### The tuple is non-tight

If `3r` is odd, time `t=1/2` gives distance `1/2` for both speeds. If
`3r=2a` is even, use

```text
t = a / (2a+1).
```

Then the distance for speed `1` is `t`, while

```text
2a * t = a - a/(2a+1)
```

has the same distance `t`. In the even case `r >= 2`, so `a >= 3` and
`t > 1/3`. Hence every tuple in the family has a strict real witness and is
non-tight.

### No point of `(1/d) Z` is a witness

Consider `t=j/d`, with `j` reduced to `0 <= j < d`. If

```text
j not in {2r+1, ..., 4r},
```

then the speed `1` has distance strictly less than `1/3`.

It remains to consider the middle interval. If `j=2s`, then

```text
3r*j = 6rs = -s (mod d),
```

where `r+1 <= s <= 2r`. Its distance is therefore at most
`2r/(6r+1) < 1/3`.

If `j=2s+1`, then

```text
3r*j = 6rs+3r = 3r-s (mod d),
```

where `r <= s <= 2r-1`. Again the residue lies between `r+1` and `2r`,
so its distance is less than `1/3`.

At every grid time at least one speed is therefore too close to an integer.
Since the denominators `6r+1` are unbounded, no universal `D` exists.

## Consequence for lift-tree hypotheses

There are also compatible modular survivor families that do not arise from a
single fixed positive integer tuple. For any fixed odd `q` not divisible by
`3`, the residues

```text
v_a = (q^a - 1)/2  (mod q^a)
```

are compatible under projection. For large enough `a`, `(1,v_a)` is
non-tight and has no witness on the `q^a` grid. Thus a theorem that kills
*all* compatible profinite lift branches is too strong. A viable multiscale
statement must retain an Archimedean height or fixed-integer realizability
condition.

## Verification

`test_counterexample_family_to_universal_grid_witness_conjecture` checks the
first 100 members with exact rational arithmetic, including coprimality,
strict real witnesses, and failure at every grid point. The proof above covers
the entire infinite family.

Primary source:

- Touch Sungkawichai and Tanupat Trakulthongchai, [*Eleven, twelve, and thirteen lonely runners*](https://arxiv.org/abs/2604.23906), Conjecture 7.1.
