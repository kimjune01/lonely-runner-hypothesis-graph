# Lonely Runner experiment

A hypothesis-graph inquiry into the modular set-cover obstruction used in recent work on the Lonely Runner Conjecture.

## Replay

```bash
uv run --with pytest --with z3-solver --with python-sat pytest -q
```

The project contains exploratory code, finite certificates, and killed hypotheses. It does not claim a proof of the general conjecture or a new bounded-runner case.

UNSAT certificate export uses Glucose through `python-sat`. The resulting DIMACS and DRUP files should be checked independently with [`drat-trim`](https://github.com/marijnheule/drat-trim); solver output alone is not treated as a certificate.
