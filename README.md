# Lonely Runner experiment

A hypothesis-graph inquiry into the modular set-cover obstruction used in recent work on the Lonely Runner Conjecture.

## Replay

```bash
uv run --with pytest --with z3-solver --with python-sat --with ortools pytest -q
```

The project contains exploratory code, finite certificates, and killed hypotheses. It does not claim a proof of the general conjecture or a new bounded-runner case.

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
