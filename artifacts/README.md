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

## `k8-p47-three-unit-fiber`

This certificate eliminates the branch with exactly three speeds coprime to
`9`. Unit symmetry fixes one of them to speed `1`; the CNF selects two other
unit speeds and five nonunit speeds and enforces exact coverage.

It also includes a proved necessary fiber clause: on each nonzero fiber,
either a selected `g=9` speed covers the whole fiber or an active `g=3` speed
occupies phase class `1`. Speed `1` covers phases `{0,8}`; if class `1` were
absent, the other two unit edges could cover at most two of its three points.

```bash
gzip -dc artifacts/k8-p47-three-unit-fiber.cnf.gz > /tmp/k8-p47-three-unit-fiber.cnf
gzip -dc artifacts/k8-p47-three-unit-fiber.drup.gz > /tmp/k8-p47-three-unit-fiber.drup
drat-trim /tmp/k8-p47-three-unit-fiber.cnf /tmp/k8-p47-three-unit-fiber.drup
```

Expected result: `s VERIFIED`.

```text
f400cf4904c496441f2e846625b12523935a1ef5e6dcc85bf91cea2c95cbafeb  k8-p47-three-unit-fiber.cnf.gz
4c4bf3d192b85ef1bdbd732b34056eda0f802e27fb3ae4d13d0b6658f6f978be  k8-p47-three-unit-fiber.drup.gz
```

The uncompressed instance has 1,386 variables and 2,572 clauses. Glucose 4
emitted 410,310 proof steps. `drat-trim` independently verified the proof on
2026-08-16. This certificate still covers only one divisibility-profile
branch, not the full finite instance.

## High-unit exhaustive replay

[`../verify_high_unit_branches.cpp`](../verify_high_unit_branches.cpp) covers
the remaining profiles at `k=8,p=47`. It normalizes one selected unit speed to
`1`, enumerates all nonunit choices, and performs exact bitset set-cover search
for the remaining unit speeds. Reusing a speed cannot help because its entire
coverage mask is removed after selection; a completion using fewer than the
available slots can always be extended with unused unit speeds.

```bash
clang++ -O3 -std=c++20 -Wall -Wextra -pedantic \
  verify_high_unit_branches.cpp -o /tmp/verify_high_unit_branches
for branch in 4 5 6 7; do /tmp/verify_high_unit_branches 47 "$branch"; done
```

Expected final lines:

```text
VERIFIED branch=4 checked=208104
VERIFIED branch=5 checked=37214
VERIFIED branch=6 checked=1311
VERIFIED branch=7 checked=23
```

Source SHA-256 at the recorded run:

```text
1d98b58f91f00e58a92a83cb2096e45f3d3b056555dd0e7e513973c7309fd534  verify_high_unit_branches.cpp
```

The recorded environment used Apple clang 21.0.0 on arm64 macOS. These four
branches are exhaustive replay, not DRUP certificates. Together with the two
DRUP-certified low-unit branches, they close the `p=47` finite obstruction.

The verifier is parameterized for `p <= 233`. Recorded H21 runs are in
[`h21-prime-replay.tsv`](h21-prime-replay.tsv). An early parameterized build
used only three words for the candidate-coverer packing mask; that was enough
through `p=61` but not beyond. All rows from `p=67` onward in the table were
withdrawn and rerun after changing that mask to the full compile-time width.

## Published nine-runner sieve replay

[`nine-runner-sieve-audit.md`](nine-runner-sieve-audit.md) records a complete
2026-08-16 replay of Trakulthongchai's independently published `1 -> 3 -> 9`
lifting sieve for all 39 primes in the nine-runner proof. The durable receipt
[`nine-runner-sieve-replay.tsv`](nine-runner-sieve-replay.tsv) records the
three intermediate set sizes; every final `U` size is zero and every row
matches the authors' receipt.

This is an independent execution of pinned source, not an independently
generated formal certificate. Its semantic scope, provenance, exact integer
contradiction, and remaining trust assumptions are documented in the audit.
