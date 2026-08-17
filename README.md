# Lonely Runner proof audit

A hypothesis-graph inquiry into the modular set-cover obstruction used in recent work on the Lonely Runner Conjecture. The initially selected nine-runner case was already solved in two independent 2025 preprints. A 2026 preprint now reports the conjecture through twelve relative speeds (thirteen physical runners). This repository records an independent replay only of Trakulthongchai's published nine-runner sieve; it makes no novelty claim.

## Replay

```bash
uv run --with pytest --with z3-solver --with python-sat --with ortools pytest -q
```

The project contains exploratory code, finite certificates, killed hypotheses, and a full replay receipt for the known nine-runner theorem. The newer `k<=12` result is recorded at primary-source audit grade in [`artifacts/2026-lrc12-literature-audit.md`](artifacts/2026-lrc12-literature-audit.md), not independently replayed. The project does not claim a proof of the general conjecture or a new bounded-runner case.

The `k=8,p=47` finite obstruction is closed across every gcd profile. Under
Rosenfeld's finite reduction, this proves that `47` divides the product of the
relative speeds in any hypothetical nine-runner counterexample. One prime
divisor is not enough to prove the nine-runner case; the current product-bound
target needs 37 suitable primes through `233`.

UNSAT certificate export uses Glucose through `python-sat`. The resulting DIMACS and DRUP files should be checked independently with [`drat-trim`](https://github.com/marijnheule/drat-trim); solver output alone is not treated as a certificate.

See [`artifacts/README.md`](artifacts/README.md) for each certificate's exact
semantic scope and replay command. In particular, the `k8-p47-two-unit-fiber`
artifact certifies one divisibility-profile branch, not the full `k=8` case.

The high-unit branches replay with:

```bash
clang++ -O3 -std=c++20 -Wall -Wextra -pedantic \
  verify_high_unit_branches.cpp -o /tmp/verify_high_unit_branches
for branch in 4 5 6 7; do /tmp/verify_high_unit_branches 47 "$branch"; done
```

The complete published nine-runner sieve audit is summarized in
[`artifacts/nine-runner-sieve-audit.md`](artifacts/nine-runner-sieve-audit.md).
Its 39 exact intermediate counts are in
[`artifacts/nine-runner-sieve-replay.tsv`](artifacts/nine-runner-sieve-replay.tsv)
and are checked, together with the final product inequality, by the test suite.

The continuing general-case inquiry found an infinite counterexample family
to Conjecture 7.1 of Sungkawichai--Trakulthongchai as written. The exact proof,
its stronger coprimality property, and the resulting restriction on profinite
lift-tree hypotheses are recorded in
[`artifacts/conjecture-7-1-counterexample.md`](artifacts/conjecture-7-1-counterexample.md).

The current general-case branch proves height-sensitive grid recovery, a
multi-fast-runner gap lemma, and an explicit bounded Fourier relation theorem.
The surviving first-spectral-band bounded-rank hypothesis is summarized in
[`artifacts/first-spectral-band-connectivity.md`](artifacts/first-spectral-band-connectivity.md).
Its counterexample-relevant version is completely checked for three and four
speeds under the published finite bounds. The four-coordinate two-torus audit
replays with

```bash
uv run classify_four_patterns.py
uv run classify_four_patterns.py --exact  # several minutes
```

The complete four-speed counterexample-domain rank audit replays with:

```bash
clang++ -O3 -std=c++20 verify_h33_n4.cpp -o /tmp/verify_h33_n4
/tmp/verify_h33_n4 1000 0 1
```

The bounded first-band scanner now reports positive-generation,
signed-dissociated seed, and two-seed appendability certificates. The
eight-speed scan separates the last two: direct H42-style generation fails,
while the weaker H44 appendability ordering still proves the desired rank.
An exact periodic-window sweep additionally tests cyclic rotations of the
singleton-owner sequence as geometrically selected bounded elimination orders.
The completed scan now reaches nine speeds; its sharper local certificate uses
the preceding new owner and at most two earlier owners per relation. It also
reports the residual handoff-core size at the normalized band edge and the
rank of the full coefficient-two circuit space modulo those independent local
rows.
