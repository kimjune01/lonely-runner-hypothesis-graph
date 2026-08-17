# Four-speed counterexample-domain bounded-rank audit

Date: 2026-08-16

## Semantic scope

This audit proves a **counterexample-relevant** version of H33 for four
speeds. It does not prove the broader statement for every tuple at or below
the first spectral-band ceiling.

Assuming the known lower-runner cases, Malikiosis--Santos--Schymura imply that
any primitive four-speed LRC counterexample has

```text
v1+v2+v3+v4 <= binom(5,2)^3 = 1000.
```

Fan--Sun imply that any tuple with maximum loneliness at most `2/9` has every
pairwise gcd at most `2`: pairwise gcd above `3` forces loneliness at least
`1/4`, while their only gcd-`3` exception `(1,2,3,12k)` has value
`3k/(12k+1)>2/9`.

The verifier enumerates every strictly increasing positive quadruple with sum
at most `1000`. A fixed rational-time mask rejects a tuple only when it gives
an explicit time at which all four distances are strictly greater than `2/9`.
For every unresolved primitive tuple satisfying the gcd restriction, the
verifier checks all exact critical times with denominators `v_i+v_j`. It then
computes whether the relations in `{-2,-1,0,1,2}^4` have rank at least two.

## Result

```text
SURVIVOR 1,2,3,4 rank=2
SURVIVOR 1,2,3,8 rank=2
SURVIVOR 1,3,4,5 rank=2
SURVIVOR 1,3,4,7 rank=2
SURVIVOR 1,4,5,6 rank=2
SURVIVOR 3,4,7,11 rank=2
VERIFIED bound=1000 shard=0/1 enumerated=1705044764 grid_rejected=1705042194 nonprimitive=1473 gcd_excluded=0 exact_rejected=1091 first_band=6 rank_failures=0
```

Thus every possible four-speed LRC counterexample would have coefficient-two
relation rank at least `2=n-2`. The six wider first-band survivors also pass.
The known four-speed LRC theorem separately says that none is a counterexample.

## Replay

```bash
clang++ -O3 -std=c++20 verify_h33_n4.cpp -o /tmp/verify_h33_n4
/tmp/verify_h33_n4 1000 0 1
```

Recorded source hash:

```text
d6b88a9e875e9cd54bdc4198fe4811abf903efa09af64da9fd0cec9b85a8a9cd  verify_h33_n4.cpp
```

The pytest suite compiles the verifier, differentially checks sum bound `60`
against the Python oracle, and replays the complete `1000` receipt.

## Sources

- Romanos Diogenes Malikiosis, Francisco Santos, and Matthias Schymura,
  [*Linearly-exponential checking is enough for the Lonely Runner Conjecture
  and some of its variants*](https://arxiv.org/abs/2411.06903).
- Ho Tin Fan and Alec Sun, [*Amending the Lonely Runner Spectrum
  Conjecture*](https://arxiv.org/abs/2306.10417).
