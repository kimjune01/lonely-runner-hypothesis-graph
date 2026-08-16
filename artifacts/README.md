# Certificate artifacts

## `k8-p47-two-unit-fiber`

This certificate eliminates one branch of the `k=8`, `p=47` modular
obstruction: a hypothetical cover with exactly two speeds coprime to `9`.
It is **not** a certificate for the full finite instance or the general Lonely
Runner Conjecture.

The CNF encodes a necessary condition. On every nonzero fiber modulo `47`,
unless a selected speed divisible by `9` covers the whole fiber, the selected
speeds with gcd `3` against `9` must be active in all three phase classes.
Exactly six nonunit speeds are selected, and at least one is divisible by `9`.

Replay the proof with `drat-trim`:

```bash
gzip -dc artifacts/k8-p47-two-unit-fiber.cnf.gz > /tmp/k8-p47-two-unit-fiber.cnf
gzip -dc artifacts/k8-p47-two-unit-fiber.drup.gz > /tmp/k8-p47-two-unit-fiber.drup
drat-trim /tmp/k8-p47-two-unit-fiber.cnf /tmp/k8-p47-two-unit-fiber.drup
```

Expected result: `s VERIFIED`.

SHA-256 checksums:

```text
7dc24d048f4347b177242dedb22f7d99e19926b57560f42afc87b3870101e653  k8-p47-two-unit-fiber.cnf.gz
32f4fb5e166cc795dd8b74c81a4052415c84e1b3406f9236e1d55184353b7f46  k8-p47-two-unit-fiber.drup.gz
```

The uncompressed instance has 825 variables and 1,651 clauses. Glucose 4
emitted 330,722 proof steps. `drat-trim` independently verified the proof on
2026-08-16.
