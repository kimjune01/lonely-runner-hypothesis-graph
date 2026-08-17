# Lonely Runner Conjecture — hypothesis graph

Date: 2026-08-17
Status: LRC known through twelve relative speeds; nine-runner case independently replayed; general conjecture remains open; no novelty claimed
Method: [The Proof Manual](/the-proof-manual) recorded using the replay contract from [The Hypothesis Graph](/the-hypothesis-graph-semantic-memory-methodeutics)

## Target

For distinct nonzero integer speeds `v_1, ..., v_n`, prove that there is a real `t` such that

```text
||t v_i|| >= 1/(n+1)  for every i,
```

where `||x||` is the distance from `x` to the nearest integer.

The general conjecture remains open. Integer speeds suffice after normalization. Sungkawichai--Trakulthongchai report a computer-assisted proof through `n=12` relative speeds. The strongest general work also reduces every fixed `n` to a finite check, but the bound remains too large for a naive search.

Sources:

- Malikiosis, Santos, and Schymura, “Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants”: https://doi.org/10.1017/fms.2025.10107
- Perarnau and Serra, “The Lonely Runner Conjecture turns 60”: https://arxiv.org/abs/2409.20160
- Rosenfeld, “The lonely runner conjecture holds for eight runners”: https://arxiv.org/abs/2509.14111
- Trakulthongchai, “Nine and ten lonely runners”: https://arxiv.org/abs/2511.22427
- Rosenfeld, “The lonely runner conjecture holds for nine runners”: https://arxiv.org/abs/2512.01912
- Sungkawichai and Trakulthongchai, “Eleven, twelve, and thirteen lonely runners”: https://arxiv.org/abs/2604.23906
- Blanco, Criado, and Santos, “Coloopless zonotopes and counterexamples to the Shifted Lonely Runner Conjecture”: https://arxiv.org/abs/2603.24784

## Graph

```text
H0  selected nine-runner target is open
 |   KILLED: two independent 2025 proofs were found on dated recheck
 |
 +--H1  first-moment / union-bound proof reaches 1/(n+1)
 |    KILLED: it stops at 1/(2n)
 |       |
 |       +--H2  forced pairwise overlap closes the gap
 |              OPEN: overlap depends on arithmetic relations among speeds
 |
 +--H3  prove a phase-shifted version, then specialize
 |    KILLED: the shifted conjecture has counterexamples
 |       |
 |       +--H4  common phase is load-bearing arithmetic structure
 |              WITNESSED
 |
 +--H5  generic continuous covering methods suffice
      KILLED: they discard the common-phase/divisibility structure
         |
         +--H6  embed into a modular set-cover obstruction
                WITNESSED for the eight-runner strategy
                   |
                   +--H7  every complete bad-residue cover forces enough
                          prime divisibility to contradict the size bound
                          PARTIALLY TESTED
                             |
                             +--H8  paper's 1/(k-1) cover threshold is usable
                             |       KILLED: contradicts a published fixture
                             |
                             +--H9  corrected finite predicate becomes UNSAT
                                     for large enough p at k=8
                                     WITNESSED through p=107 on the H21 target list
                                        |
                                        +--H22  published 1→3→9 sieve closes
                                                the complete nine-runner proof
                                                REPLAYED for all 39 primes
                                                   |
                                                   +--H23  universal denominator
                                                           for non-tight tuples
                                                           KILLED by (1,3r), d=6r+1
                                                          |
                                                          +--H24  height-sensitive
                                                          |       denominator bound
                                                          |       PROVED: d>(k+1)M^2
                                                          |
                                                          +--H25  missing central cube
                                                                  forces a bounded
                                                                  integer relation
                                                                  SPLIT: relation proved,
                                                                  descent unspecified
                                                                     |
                                                                     +--H26  one critical-time
                                                                     |       graph yields a
                                                                     |       bounded cycle
                                                                     |       KILLED: telescopes
                                                                     |
                                                                     +--H27  fewer than half
                                                                     |       are very fast
                                                                     |       PROVED by union bound
                                                                     |
                                                                     +--H28  triangular Fourier
                                                                             bump forces a bounded
                                                                             speed relation
                                                                             PROVED explicitly
                                                                                |
                                                                                +--H29  first spectral
                                                                                        band has connected
                                                                                        coefficient-2 relations
                                                                                        SURVIVES CORRECTED SCANS
                                                                                           |
                                                                                           +--H30  first-band height
                                                                                           |       is bounded under
                                                                                           |       induction
                                                                                           |       PROVED (coarse)
                                                                                           |
                                                                                           +--H31  positive triangular
                                                                                           |       relation tree
                                                                                           |       SURVIVES SCANS
                                                                                           |
                                                                                           +--H32  two positive seeds
                                                                                           |       generate the tuple
                                                                                           |       KILLED at n=6
                                                                                           |
                                                                                           +--H33  coefficient-2
                                                                                           |       relation rank >=n-2
                                                                                           |       SURVIVES SCANS
                                                                                           |
                                                                                           +--H34  full short-relation
                                                                                           |       rank n-1
                                                                                           |       KILLED at n=4
                                                                                           |
                                                                                           +--H35  strict ambient
                                                                                           |       two-torus margin
                                                                                           |       PROVED UNDER INDUCTION
                                                                                           |
                                                                                           +--H36  four-coordinate
                                                                                           |       coefficient-2 patterns
                                                                                           |       VERIFIED EXACTLY
                                                                                           |
                                                                                           +--H37  counterexample-rank
                                                                                           |       base case n=3
                                                                                           |       COMPLETE
                                                                                           |
                                                                                           +--H38  four-speed first-band
                                                                                           |       candidates have all
                                                                                           |       pairwise gcd <=2
                                                                                           |       PROVED FROM FAN--SUN
                                                                                           |
                                                                                           +--H39  counterexample-only
                                                                                           |       coefficient-2 rank
                                                                                           |       SELECTED
                                                                                           |
                                                                                           +--H40  H39 at n=4
                                                                                           |       COMPLETE finite audit
                                                                                           |
                                                                                           +--H41  every counterexample
                                                                                           |       at n>=18 has a
                                                                                           |       coefficient-1 relation
                                                                                           |       PROVED BY RIESZ PRODUCT
                                                                                           |
                                                                                           +--H42  two-element maximal
                                                                                           |       coefficient-2
                                                                                           |       dissociated seed
                                                                                           |       TESTING
                                                                                           |
                                                                                           +--H43  iterate unmodified
                                                                                           |       Riesz product
                                                                                           |       KILLED EXACTLY
                                                                                           |
                                                                                           +--H44  two-seed bounded
                                                                                           |       appendability ordering
                                                                                           |       SELECTED FOR TESTING
                                                                                           |
                                                                                           +--H45  sliding-window handoff
                                                                                           |       order eliminates
                                                                                           |       SELECTED FOR TESTING
                                                                                           |
                                                                                           +--H46  every runner owns a
                                                                                           |       singleton-load window
                                                                                           |       PROVED BY INDUCTION
                                                                                           |
                                                                                           +--H47  segment-local four-owner
                                                                                                   handoff elimination
                                                                                                   SELECTED FOR TESTING
                                                                                                   |
                                                                                                   +--H48  strict first-band
                                                                                                            full relation rank
                                                                                                            SELECTED FOR TESTING
                                                                                                            |
                                                                                                            +--H49  divisible-speed
                                                                                                                     first-band barrier
                                                                                                                     SELECTED; SUFFICIENT
                                                                                                                     |
                                                                                                                     +--H50  largest divisible
                                                                                                                              reset counting
                                                                                                                              PROVED
                                                                                                                              |
                                                                                                                              +--H51  exact reset-kernel
                                                                                                                                       certificate
                                                                                                                                       PROVED
                                                                                                                                       |
                                                                                                                                       +--H52  largest-runner
                                                                                                                                                phase boundaries
                                                                                                                                                KILLED
                                                                                                                                                |
                                                                                                                                                +--H53  residue-class
                                                                                                                                                         blocking minimum
                                                                                                                                                         PROVED
                                                                                                                                                         |
                                                                                                                                                         +--H54  central-cell
                                                                                                                                                                  escape
                                                                                                                                                                  KILLED
                                                                                                                                                                  |
                                                                                                                                                                  +--H55  unit-grid
                                                                                                                                                                           handoff skeleton
                                                                                                                                                                           PROVED
                                                                                                                                                                           |
                                                                                                                                                                           +--H56  opposite-unit
                                                                                                                                                                                    quotient collision
                                                                                                                                                                                    PROVED
                                                                                                                                                                                    |
                                                                                                                                                                                    +--H57  complete all-runner
                                                                                                                                                                                             event sweep
                                                                                                                                                                                             PROVED
                                                                                                                                                                                             |
                                                                                                                                                                                             +--H58  boundary-event
                                                                                                                                                                                                      capacity sieve
                                                                                                                                                                                                      PROVED
                                                                                                                                                                                                      |
                                                                                                                                                                                                      +--H59  boundary-event
                                                                                                                                                                                                               moment hierarchy
                                                                                                                                                                                                               PROVED
                                                                                                                                                                                                               |
                                                                                                                                                                                                               +--H60  repeated cluster
                                                                                                                                                                                                                        bounded relation
                                                                                                                                                                                                                        KILLED
                                                                                                                                                                                                                        |
                                                                                                                                                                                                                        +--H61  signed-error
                                                                                                                                                                                                                                 sumset compression
                                                                                                                                                                                                                                 PROVED
                                                                                                                                                                                                                                 |
                                                                                                                                                                                                                                 +--H62  2026 lift/project
                                                                                                                                                                                                                                          theorem through k=12
                                                                                                                                                                                                                                          RETRIEVED
                                                                                                                                                                                                                                          |
                                                                                                                                                                                                                                          +--H63  temporal-spanner
                                                                                                                                                                                                                                                   dismount-or-core
                                                                                                                                                                                                                                                   REFINED
                                                                                                                                                                                                                                                   |
                                                                                                                                                                                                                                                   +--H64  residual-core rank
                                                                                                                                                                                                                                                            accounting and
                                                                                                                                                                                                                                                            singleton persistence
                                                                                                                                                                                                                                                            PROVED
                                                                                                                                                                                                                                                            |
                                                                                                                                                                                                                                                            +--H65  promote a core
                                                                                                                                                                                                                                                                     owner to a handoff
                                                                                                                                                                                                                                                                     seed pair
                                                                                                                                                                                                                                                                     KILLED
                                                                                                                                                                                                                                                                     |
                                                                                                                                                                                                                                                                     +--H66  quotient all
                                                                                                                                                                                                                                                                              circuits by local
                                                                                                                                                                                                                                                                              handoff rows
                                                                                                                                                                                                                                                                              PROVED
                                                                                                                                                                                                                                                                              |
                                                                                                                                                                                                                                                                              +--H67  residual core
                                                                                                                                                                                                                                                                                       has size at
                                                                                                                                                                                                                                                                                       most one
                                                                                                                                                                                                                                                                                       SELECTED
                                                                                                                                                                                                                                                                                       |
                                                                                                                                                                                                                                                                                       +--H68  canonical factor
                                                                                                                                                                                                                                                                                                extension family
                                                                                                                                                                                                                                                                                                is harmless
                                                                                                                                                                                                                                                                                                PROVED
                                                                                                                                                                                                                                                                                                |
                                                                                                                                                                                                                                                                                                +--H69  strict first-band
                                                                                                                                                                                                                                                                                                         coefficient-one
                                                                                                                                                                                                                                                                                                         rank n-2
                                                                                                                                                                                                                                                                                                         SELECTED
                                                                                                                                                                                                                                                                                                         |
                                                                                                                                                                                                                                                                                                         +--H70  low rank forces
                                                                                                                                                                                                                                                                                                                  a reciprocal Riesz
                                                                                                                                                                                                                                                                                                                  load floor
                                                                                                                                                                                                                                                                                                                  KILLED
                                                                                                                                                                                                                                                                                                                  |
                                                                                                                                                                                                                                                                                                                  +--H71  geometric canonical
                                                                                                                                                                                                                                                                                                                           blocks share a
                                                                                                                                                                                                                                                                                                                           fixed phase
                                                                                                                                                                                                                                                                                                                           PROVED
                                                                                                                                                                                                                                                                                                                           |
                                                                                                                                                                                                                                                                                                                           +--H72  arbitrary geometric
                                                                                                                                                                                                                                                                                                                                    multiplier blocks
                                                                                                                                                                                                                                                                                                                                    synchronize eventually
                                                                                                                                                                                                                                                                                                                                    PROVED
```

## Nodes

### H0 — The selected nine-runner target is genuinely open

- Mode: induction from current literature
- Hypothesis: the selected next bounded case—nine runners—remains unresolved as of 2026-08-16.
- Kill condition: a dated primary source proves the nine-runner case.
- Trial: re-run the literature-status search against 2025–2026 primary sources rather than relying on the older survey or the initial problem-selection pass.
- Observed outcome: killed. Trakulthongchai announced a computer-assisted proof for nine and ten runners in November 2025; Rosenfeld independently announced a different nine-runner proof in December 2025. Revised 2026 versions state the results explicitly. The general conjecture remains open, but the selected bounded target does not.
- Verdict: killed at primary-source grade.
- Credence: high.
- Edge generated: H22—replace attempted novelty with reconstruction and independent replay of the known theorem.

### H1 — A first-moment argument proves the conjectured threshold

- Mode: deduction
- Hypothesis: viewing time `t` as uniform on `[0,1)` and bounding bad times by measure proves the threshold `1/(n+1)`.
- Kill condition: the total bad-set measure bound is at least `1` at that threshold.
- Trial:

  ```text
  Let B_i(delta) = {t in [0,1): ||v_i t|| < delta}.
  Multiplication by nonzero integer v_i preserves uniform measure mod 1,
  so mu(B_i(delta)) = 2 delta.
  Therefore mu(union_i B_i(delta)) <= 2 n delta.
  Substitute delta = 1/(n+1): 2n/(n+1) > 1 for n > 1.
  ```

- Observed outcome: the bound proves only `delta < 1/(2n)`; it cannot reach `1/(n+1)`.
- Verdict: killed at strong-replay grade.
- Credence: deductive.
- Edge generated: H2. The exact deficit says the next proof must exploit overlap among the bad sets rather than their individual measures.

### H2 — Arithmetic overlap among bad sets closes the factor-two gap

- Mode: abduction
- Hypothesis: inclusion–exclusion, Fourier coefficients, or another correlation argument can show that the periodic bad sets overlap enough to leave an uncovered time at `delta = 1/(n+1)`.
- Kill condition: construct normalized speed families whose overlap statistics obey no uniform inequality stronger than the first-moment bound, or show that the required inequality implies a known false shifted statement.
- Trial: derive or retrieve a lower bound on intersections `mu(B_i intersect B_j)` that survives all distinct normalized integer speed vectors and is strong enough, after inclusion–exclusion, to force `mu(union_i B_i) < 1`.
- Observed outcome: not run to completion. Pairwise overlap depends on gcd and ratio structure; no uniform bound was established in this inquiry.
- Verdict: open.
- Credence: low; proposed, not tested.
- Edge if killed by uncontrolled higher-order dependence: move from global inclusion–exclusion to residue-class decomposition and H6.

### H3 — Prove the independently phase-shifted statement

- Mode: abduction
- Hypothesis: the proof should survive replacing each constraint by `||v_i t + s_i|| >= 1/(n+1)` for arbitrary phases `s_i`; the original follows by setting every `s_i = 0`.
- Kill condition: one counterexample to the shifted formulation.
- Trial: inspect the theorem statements and explicit constructions in Blanco, Criado, and Santos (2026), arXiv:2603.24784.
- Observed outcome: explicit counterexamples exist to the shifted Lonely Runner Conjecture starting at `n = 5`.
- Verdict: killed at artifact-replay grade.
- Credence: high.
- Edge generated: H4. The common phase in the original problem is load-bearing and must remain visible in any embedding.

### H4 — Common phase is load-bearing structure

- Mode: induction
- Hypothesis: a viable proof must use the fact that all bad intervals are centered on the common arithmetic condition `v_i t in Z`, rather than treating them as arbitrary periodic arcs.
- Kill condition: prove the original statement using only properties invariant under independent translations of the bad sets.
- Trial: compare the original and shifted formulations. Any argument invariant under independent translations would prove both; H3 records counterexamples to the shifted form.
- Observed outcome: translation-invariant information cannot suffice.
- Verdict: witnessed at strong-replay grade, conditional on the cited shifted counterexamples.
- Credence: deductive from H3.
- Edge generated: preserve congruence, gcd, and divisibility data in the next representation.

### H5 — Generic continuous covering machinery is sufficient

- Mode: abduction
- Hypothesis: compactness, convexity, or generic circle-covering bounds prove the target without arithmetic information about the speeds.
- Kill condition: the proposed machinery is invariant under independent phase shifts or sees only interval lengths.
- Trial: erase the centers of the sets `B_i` and retain only their measures and periodicity. Check whether the resulting data distinguishes the original formulation from H3's false shifted formulation.
- Observed outcome: it does not distinguish them.
- Verdict: killed as a standalone route; continuous tools may still participate after an arithmetic embedding.
- Credence: moderate.
- Edge generated: H6, embed the obstruction into modular residues while preserving common phase.

### H6 — Modular set cover exposes a finite obstruction

- Mode: induction from a published construction
- Hypothesis: for suitable rational test times, failure of loneliness becomes a finite set-cover problem whose complete covers force divisibility constraints on a minimal counterexample.
- Kill condition: the discretization loses a possible real-time witness, or the cover certificate has no implication for the integer speeds.
- Trial: replay the reformulation in Rosenfeld (2025), especially the bad-residue cover and prime-divisibility lemmas used for eight runners; compare it with the finite-checking theorem of Malikiosis, Schymura, and Santos.
- Observed outcome: this route yields a computer-assisted proof for eight runners by forcing enough primes to divide the product of the speeds to contradict an independent upper bound.
- Verdict: witnessed for the bounded case at artifact-replay grade; not established uniformly in `n`.
- Credence: high for the cited case, low for generalization.
- Edge generated: H7.

### H7 — Complete residue covers force enough divisibility uniformly

- Mode: abduction
- Hypothesis: for every `n`, sufficiently many moduli `p` have the property that a complete bad-residue cover forces `p | product_i v_i`, or a stronger condition such as multiple divisible speeds or a forced prime power. The accumulated divisibility then exceeds the finite-checking upper bound for a minimal counterexample.
- Kill condition: exhibit arbitrarily large `n` and admissible complete covers avoiding enough independent prime divisors, or prove that the forced-prime product grows too slowly relative to the minimal-counterexample bound.
- Trial:

  1. Formalize Rosenfeld’s constrained set-cover predicate for symbolic `n` and modulus `p`.
  2. Enumerate small `(n,p)` instances with a certificate-producing SAT or exact-cover solver.
  3. Classify failures by their residue and gcd structure.
  4. Test candidate strengthenings: prime powers, at least two speeds divisible by `p`, or interacting moduli.
  5. Compare the certified divisor-product lower bound against the published upper bound on a minimal counterexample.

- Observed outcome: witnessed for fixed bounded cases, not uniformly. Trakulthongchai's lifting sieve closes `n=8,9`, Rosenfeld independently closes `n=8`, and Sungkawichai–Trakulthongchai extend the computational framework through `n=12`. No uniform-in-`n` theorem follows.
- Verdict: open as a general mechanism; proved for the cited bounded cases.
- Credence: high for the bounded results, low for uniform extrapolation.

### H8 — The printed `1/(k-1)` coverage threshold is the intended predicate

- Mode: deduction plus differential replay
- Hypothesis: Section 6 of Rosenfeld’s source can be implemented literally: `v` covers `j` when `||jv/((k+1)p)|| < 1/(k-1)`.
- Kill condition: the literal predicate produces an admissible cover for a `(k,p)` pair the same paper reports as having no cover.
- Trial:

  ```text
  uv run --with pytest --with z3-solver --with python-sat pytest -q

  For k=3, p=7, D=28, test the candidate {1,2,3} at threshold 1/(k-1)=1/2.
  It covers every j in {1,...,14}; for each omitted candidate,
  gcd(28, the other two candidates)=1.
  ```

- Observed outcome: `{1,2,3}` is an admissible complete cover under `1/(k-1)`, but the paper reports that the required no-cover property holds for `k=3` and every prime `p >= 7`. The main lemma itself uses the lonely threshold `1/(k+1)`.
- Verdict: killed at strong-replay grade. The experiment therefore uses `1/(k+1)`. This appears to be a typographical error in the paper’s cover definition; it is not a defect in the main lemma.
- Credence: high.
- Edge generated: H9. Validate the corrected formalization against both a published working case and a published exception before exploring new instances.

### H9 — The corrected finite predicate becomes UNSAT for larger moduli at `k=8`

- Mode: induction from finite exact experiments
- Hypothesis: with nine runners (`k=8` nonzero relative speeds), admissible complete covers disappear once `p` is sufficiently large.
- Kill condition: find admissible complete covers for arbitrarily larger tested primes, or fail to reproduce the published lower-`k` fixtures.
- Trial implementation: `lonely_runner_h7.py`, tested by `test_lonely_runner_h7.py` under Python 3.13 and Z3 5.1.0.
- Encoding:

  - one Boolean variable per candidate residue in `1,...,floor((k+1)p/2)`, excluding multiples of `p`;
  - exactly `k` selected residues;
  - one coverage clause per rational test time;
  - for every prime `q | (k+1)p`, at least two selected residues are nonzero modulo `q`. This is equivalent to `gcd(D, all selected residues except any one)=1`.

- Calibration outcome:

  - `k=3,p=7`: UNSAT, matching a published working modulus;
  - `k=6,p=17`: SAT, matching a published exception;
  - `k=6,p=17` witness is replayed by the test suite.

- New finite outcomes for `k=8`:

  | p | Verdict | Replay artifact |
  |---:|:---|:---|
  | 11 | SAT | `(1,3,4,5,6,7,9,43)` |
  | 13 | SAT | `(1,3,4,5,6,9,15,21)` |
  | 17 | SAT | `(1,9,22,38,40,49,58,71)` |
  | 19 | SAT | `(1,5,6,7,9,45,54,72)` |
  | 23 | SAT | `(1,7,9,27,36,45,54,63)` |
  | 29 | SAT | `(1,8,9,18,27,45,72,99)` |
  | 31 | SAT | `(1,7,9,45,54,72,81,126)` |
  | 37 | SAT | `(1,8,9,27,36,45,63,117)` |
  | 41 | SAT | `(1,7,9,45,54,63,72,99)` |
  | 43 | SAT | `(1,7,9,45,54,63,72,117)` |
  | 47 | UNSAT | deterministic Z3 replay, 25.885 s in the recorded run |
  | 53 | UNSAT | deterministic Z3 replay |
  | 59 | UNSAT | deterministic Z3 replay |
  | 61 | UNSAT | deterministic Z3 replay |
  | 67 | UNSAT | deterministic Z3 replay, 25.154 s in the recorded run |

- Observed outcome: a sharp tested transition occurs between `p=43` and `p=47`. Every tested prime through `43` admits a cover; every completed test from `47` through `67` is UNSAT.
- Verdict: witnessed only for the listed finite instances. SAT rows have compact independently replayable witnesses. UNSAT rows currently have deterministic solver replay but no exported proof certificate, so their replay grade is weaker.
- Credence: high for SAT witnesses; moderate-high for UNSAT runs; low for extrapolation to all `p >= 47`.
- Edge generated: H10 — export checkable UNSAT certificates and search for the structural reason the transition occurs at `47`.

### H10 — A structural obstruction explains the `k=8` transition

- Mode: abduction
- Hypothesis: for `k=8`, every admissible complete cover at sufficiently large `p` violates either a coverage clause or the “two nonmultiples per prime divisor” gcd condition for a small, classifiable family of residues.
- Kill condition: UNSAT cores vary without a stable residue/gcd pattern across larger primes, or SAT witnesses reappear.
- Trial:

  1. Label every coverage and gcd clause and extract UNSAT cores for `p=47,53,59,61,67`.
  2. Minimize the cores and normalize them under `v -> D-v` and multiplication by units modulo `D`.
  3. Intersect the normalized cores across moduli.
  4. Attempt to state the shared core as a symbolic counting or divisibility lemma.
  5. Export an independently checkable proof certificate for each finite UNSAT result.

- Observed outcome:

  - Named Z3 core extraction was calibrated on `k=3,p=7`; its returned core replays as UNSAT.
  - At `k=8,p=47`, tracked Z3 did not finish in approximately one minute and returned `unknown` when interrupted.
  - At `k=8,p=53`, tracked Z3 likewise did not finish within the trial budget.
  - The lower-level CNF encoding was independently calibrated: Glucose emitted a 63-step DRUP proof for `k=3,p=7`, and `drat-trim` verified it against the exported 94-variable, 168-clause DIMACS instance using 716 resolution steps.
  - Proof-producing Glucose and external CaDiCaL runs for `k=8,p=53` were each interrupted after roughly one minute. Both are recorded as `unknown`, not `UNSAT`; no partial proof is treated as evidence.

- Verdict: open. Core extraction and independent certification work, but proof production at the `k=8` boundary exceeds the present interactive budget.
- Credence: low.
- Edge generated: H11 — reduce the CNF before requesting a proof, rather than asking a proof logger to rediscover every symmetry and dominated candidate.

### H11 — Preprocessing exposes a small certificate-bearing obstruction

- Mode: abduction from search-budget failure
- Hypothesis: symmetry breaking, candidate domination, and clause subsumption reduce the `k=8` boundary instance enough for proof logging and core extraction to terminate cheaply.
- Kill condition: independently checked preprocessing leaves proof generation at the same scale, or removes a known SAT witness from a calibration instance.
- Trial:

  1. Differentially validate every reduction against SAT witnesses for `p <= 43` and UNSAT verdicts for `p >= 47`.
  2. Remove coverage clauses implied by stricter coverage clauses.
  3. Identify candidates whose coverage mask and divisibility signature are dominated by another candidate.
  4. Add one sound orbit-breaking constraint under multiplication by units modulo `D`, with a written lifting argument.
  5. Export reduced DIMACS, obtain DRAT/LRAT, and verify it with an independent checker.

- Observed outcome:

  - Coverage-clause subsumption is sound but weak. At `p=53`, 238 time clauses reduce to 236 unique clauses and 235 inclusion-minimal clauses; the other tested moduli remove the same order of only three clauses.
  - Candidate-independent gcd preprocessing is stronger. For `k=8,p=53`, the modulus is `D=9p`, whose prime divisors are `3` and `p`. Multiples of `p` are excluded from the candidate set, so selecting eight candidates automatically satisfies the `p` constraint. Only the prime `3` remains active.
  - Removing that active `3` constraint makes the coverage problem SAT at `p=47,53,59`. Thus coverage itself does not cause the transition.
  - Restoring the constraint makes the calibrated full instances UNSAT. Equivalently, every eight-element cover in these finite instances contains at least seven multiples of `3`; the main lemma forbids it because every omitted-speed gcd must remain `1`.
  - Omitting the redundant `p` constraint did not make boundary proof production cheap; a `p=53` CaDiCaL run was interrupted after approximately 30 seconds and recorded as `unknown`.

- Verdict: the broad preprocessing hypothesis is killed—generic subsumption barely reduces the instance—but it exposes the load-bearing arithmetic obstruction.
- Credence: low.
- Edge generated: H12 — prove directly that an eight-residue cover at sufficiently large `p` requires at least seven multiples of `3`.

### H12 — Eight-residue coverage forces seven multiples of `3`

- Mode: abduction from constraint ablation
- Hypothesis: for sufficiently large primes `p`, if eight residues cover every `j in {1,...,floor(9p/2)}` at threshold `1/9`, then at most one selected residue is nonzero modulo `3`.
- Kill condition: find a prime beyond the tested boundary and an eight-cover containing two residues nonzero modulo `3`, or derive a covering construction with two such residues for infinitely many `p`.
- Trial:

  1. Partition test times and candidate residues by their classes modulo `3`.
  2. Write each coverage mask as three scaled interval systems.
  3. Bound the union contributed by two nonmultiples of `3` plus six arbitrary candidates.
  4. Identify the finite exceptional range where endpoint rounding can defeat the bound.
  5. Compare the resulting threshold with the observed last SAT modulus `43` and first UNSAT modulus `47`.

- Observed outcome:

  - Assumption-core extraction at `p=47` exceeded one minute and was interrupted; its verdict is `unknown`.
  - Relaxing the requirement from two nonmultiples of `3` to one produces the explicit `p=47` cover `(9,18,27,36,45,54,63,76)` in 0.406 seconds. The first seven entries form a rigid arithmetic progression.
  - The eight-element progression `(9,18,27,36,45,54,63,72)` covers the test grid for every checked prime across the boundary. This is not merely experimental: dividing speeds by `9` reduces it to the Dirichlet cover `{1,...,8}` at threshold `1/9`.
  - Therefore the full-cover SAT witnesses are explained by a universal degenerate construction. Their defect is exactly arithmetic: every speed is divisible by `3`, so they violate the omitted-speed gcd condition.

- Verdict: open, but reformulated. Raw coverage does not force seven multiples of `3`; a universal all-multiple cover exists. The actual claim is that an eight-cover cannot survive the two exchanges required by the gcd condition once `p` is sufficiently large.
- Credence: low, but more specific than H10: it names the exact arithmetic statement a general proof must establish.
- Edge generated: H13.

### H13 — Two-exchange obstruction for the Dirichlet cover

- Mode: abduction from a witnessed canonical construction
- Hypothesis: for sufficiently large prime `p`, replacing two or more members of the canonical cover `{9,18,...,72}` by residues nonzero modulo `3` necessarily exposes at least one test time. More generally, every eight-cover with two nonmultiples of `3` has a structural defect equivalent to such an exchange.
- Kill condition: construct an eight-cover with two nonmultiples of `3` for any prime beyond the tested boundary, or find a family not reducible to the canonical-cover exchange picture.
- Trial:

  1. For every pair of nonmultiples `(a,b)`, compute the test times they cover by residue class modulo `3`.
  2. Ask which six multiples of `3` maximize coverage of the complement.
  3. Quotient those six speeds by `3`, turning their constraints into a six-multiplier approximation problem modulo `3p`.
  4. Search for a small family of test times that no such pair-plus-six decomposition covers.
  5. Convert that family into a pigeonhole or interval-length inequality with explicit endpoint error in `p`.

- Observed outcome:

  - CP-SAT assumption cores calibrate and replay, but the `p=47` run exceeded one minute and returned `UNKNOWN` when interrupted. Changing the pseudo-Boolean solver did not expose a core.
  - Weighted MaxSAT was then used to seek the admissible eight-selection covering the most test times. It too exceeded the bounded budget at `p=47`; finding a relaxed witness is easy, but certifying the closest near-cover is equivalent in difficulty to the UNSAT question.
  - Direct modular inspection finds exactly four test times that no nonmultiple of `3` can cover: `p,2p,3p,4p`. At `p,2p,4p`, a covering speed must be divisible by `9`; at `3p`, it must be divisible by `3`. These force lattice participation but do not alone force seven lattice residues.

- Verdict: open. The solver-core and global-optimization routes are killed under the present budget; the direct modular route survives.
- Credence: low.
- Edge generated: H14.

### H14 — Coverage capacity plus forced overlap proves the exchange obstruction

- Mode: deduction followed by abduction
- Hypothesis: exact coverage sizes, combined with an unavoidable-overlap bound between congruence classes, show that six multiples of `3` and two nonmultiples cannot cover the half-grid.
- Exact lemma: let `D=9p`, let `p != 3` be prime, let `p` not divide `v`, and put `g=gcd(v,D)=gcd(v,9)`. On the half-grid `j=1,...,(D-1)/2`, the number of times covered by `v` at threshold `1/9` is

  ```text
  |C_v| = (g(2 floor((p-1)/g) + 1) - 1) / 2.
  ```

  Reason: multiplication by `v` maps the cyclic group onto the multiples of `g`, each with `g` preimages. The open interval of residues at distance less than `p` from zero contains `2 floor((p-1)/g)+1` such image points. Remove `j=0`, then quotient the remaining points by the symmetry `j <-> D-j`.

- Replay: the formula is exhaustively checked for every candidate at `k=8,p=47` by `test_exact_coverage_size_formula_at_boundary`.
- Kill condition for a capacity-only proof: the sum of the eight largest permitted coverage sizes already exceeds the universe.
- Observed outcome: capacity alone dies. At `p=47`, two nonmultiples contribute at most `46` times each and six `g=9` multiples contribute at most `49` each, totaling `386` incidences over a universe of `211` times. A proof must account for at least `175` repeated incidences; it cannot use only marginal set sizes.
- Verdict: the exact-size lemma is witnessed; the capacity-only hypothesis is killed.
- Credence: deductive for the lemma and kill, low for the proposed overlap completion.
- Edge generated: H15 — derive exact or lower-bounded pairwise intersections as a function of `gcd(v,w,9p)` and use the modulo-`3` split to force enough wasted incidence.

### H15 — Congruence classes force excessive pairwise overlap

- Mode: abduction from H14’s exact deficit
- Hypothesis: among six multiples of `3`, periodic bad-time sets overlap so heavily that two nonmultiples cannot supply the missing distinct coverage. A Bonferroni or Fourier bound sensitive to `gcd(v,w,9p)` closes the `175`-incidence gap at `p=47` and scales with `p`.
- Kill condition: construct admissible selections whose pairwise intersections meet the needed bound while higher-order intersections defeat every second-order union estimate.
- Trial:

  1. Derive an exact pair-intersection counter using the simultaneous congruences `|jv|_D < p` and `|jw|_D < p`.
  2. Aggregate it separately for `(0,0)`, `(0,nonzero)`, and `(nonzero,nonzero)` residue classes modulo `3`.
  3. Optimize the resulting second-order upper bound over six-plus-two selections.
  4. If second order dies, retain the counterexample as the kill edge to a Fourier or higher-order argument.

- Observed outcome:

  - Pair intersections are not determined by the natural gcd signature. At `p=47`, pairs with signature `(gcd(v,D),gcd(w,D),gcd(v,w,D)) = (1,1,1)` have intersections ranging from `5` to `23`; `(9,9,9)` ranges from `4` to `22`.
  - More strongly, two admissibility-shaped selections have identical first and second incidence moments but different union sizes:

    ```text
    A = (23,78,86,126,138,159,183,192): (S1,S2,|union|) = (371,271,184)
    B = (12,49,57,93,102,116,144,150):  (S1,S2,|union|) = (371,271,190)
    ```

    Both contain six multiples of `3` and two nonmultiples. The fixture is replayed by `test_first_two_incidence_moments_do_not_determine_union`.
  - The abstract occupancy equations with `S1=371` and `S2=271` permit a union of `300` points—for example multiplicities `{n1=288,n2=1,n3=1,n6=1,n8=9}`—far above the actual universe size `211`. Thus the first two moments cannot certify noncoverage even when known exactly.

- Verdict: killed. Gcd-class pairwise bounds and second-order incidence moments discard the higher-order alignment that controls the union.
- Credence: low.
- Edge generated: H16 — retain the whole multiplicity profile or move to Fourier characters that preserve simultaneous alignment.

### H16 — Fourier support exposes the two-exchange obstruction

- Mode: abduction from the second-moment collision
- Hypothesis: the indicator of each bad-time set has explicit Fourier support on multiples of `D/gcd(v,D)`. Six speeds divisible by `3` concentrate on a shared character subgroup; two nonmultiples cannot cancel the resulting uncovered coefficient once `p` is large.
- Kill condition: the Fourier inequalities reduce to the same first two incidence moments, or admissible near-covers satisfy every tractable low-frequency constraint.
- Trial:

  1. Write the discrete Fourier transform of `1[|jv|_D < p]` exactly.
  2. Separate characters divisible by `3` from the other characters.
  3. Express complete coverage as the pointwise inequality `sum_i 1[C_vi] >= 1` and test it against a character supported on the shared subgroup.
  4. Optimize the resulting inequality over six multiples and two nonmultiples.
  5. If one character is insufficient, retain the explicit near-cover as the kill edge to a small semidefinite or flag-algebra certificate.

- Exact transform: for `D=9p`, `g=gcd(v,D)`, and character `r`, the coefficient vanishes unless `g | r`. When `r=gs`, let `u` be the inverse of `v/g` modulo `D/g` and let `m=floor((p-1)/g)`. Then

  ```text
  Fourier(C_v)(r) = g * sum_{q=-m}^{m} exp(-2 pi i s q u / (D/g)).
  ```

  This is a rotated Dirichlet kernel. It retains the ratio information that gcd-only pair bounds discarded.
- Observed outcome for the most natural order-three character `r=D/3` at `p=47`:

  - nonmultiples of `3` have residue counts `(31,31,31)`, hence coefficient `0`;
  - speeds with `gcd(v,9)=3` have counts `(33,30,30)`, hence coefficient `3` up to phase;
  - multiples of `9` have counts `(33,33,33)`, hence coefficient `0`.

  The fixture is replayed by `test_order_three_fourier_counts_at_first_boundary`. Against complete coverage, positivity allows a nonzero Fourier coefficient as large as the zero-frequency excess, which here is hundreds of incidences. A coefficient of at most `18` from six multiples is far too small.
- Verdict: the single order-three character is killed. The full transform survives, but any useful character must adapt to the selected ratios rather than merely to their modulo-`3` classes.
- Credence: low.
- Edge generated: H17.

### H17 — An adaptive Dirichlet-kernel character separates every admissible selection

- Mode: abduction from the exact transform
- Hypothesis: for every six-plus-two selection, some character `r` simultaneously aligns the six rotated Dirichlet kernels from the multiples of `3` while the two nonmultiple kernels remain too small to satisfy positivity of `sum_i 1[C_vi]-1`.
- Kill condition: find an admissibility-shaped near-cover for which every character satisfies the positive-function Fourier bound with slack.
- Trial:

  1. Compute, for each finite selection, the maximum normalized violation
     `max_r |sum_i Fourier(C_vi)(r)| / (sum_i |C_vi| - D)`.
  2. Search for the selection minimizing that maximum at `p=47`.
  3. Inspect the maximizing characters and infer their relation to inverses of `v_i/3 mod 3p`.
  4. Attempt a simultaneous-approximation lemma selecting one character that aligns six phases.
  5. Verify the derived inequality symbolically, not by floating-point Fourier output.

- Observed outcome:

  - A deterministic sample of 20,000 six-plus-two selections at `p=47` produced zero single-character violations.
  - The strongest counterexample found was

    ```text
    (27,42,96,157,162,176,189,207).
    ```

    Its largest nonzero Fourier coefficient is less than `0.251` times the zero-frequency surplus. Thus every single-character positivity inequality holds with a factor-of-four margin even though the selection does not cover.
  - The ratio is independently recomputed by `test_single_character_fourier_bound_has_large_slack`; the maximizing character is nonzero.

- Verdict: killed. Adapting one character to the selection still compresses away the joint phase information needed to locate an uncovered point.
- Credence: low.
- Edge generated: H18 — use a positive trigonometric polynomial, equivalently a weighted combination of characters, as a separating certificate.

### H18 — A low-degree positive trigonometric polynomial separates every admissible selection

- Mode: abduction from the single-character kill
- Hypothesis: there is a bounded-degree nonnegative test polynomial `P(j)` whose weighted coverage satisfies `sum_j P(j)(sum_i 1[C_vi](j)-1) < 0` for every six-plus-two selection. In Fourier language, several characters combine to localize where any admissible selection must leave a gap.
- Kill condition: the minimum separating degree grows with `p`, or finite SDP certificates show no common polynomial even across the first few UNSAT moduli.
- Trial:

  1. For a fixed selection, solve the dual linear program for nonnegative weights on test times; inspect sparsity and modular pattern.
  2. Seek one weight pattern valid across all selections via a cutting-plane loop: propose weights, find the worst selection, add it, repeat.
  3. Constrain weights to a low-degree sum-of-squares trigonometric polynomial.
  4. Rationalize the coefficients and check the final inequalities exactly.
  5. Compare certificates across `p=47,53,59` to infer a symbolic family.

- Observed outcome:

  - The stronger unrestricted problem was solved numerically at `p=47`: allow an arbitrary nonnegative weight `w_j` on every test time, with `sum_j w_j=1`, and minimize the largest weighted incidence of an eight-speed selection having at least two nonmultiples of `3`.
  - A cutting-plane LP converged after 81 selection cuts to

    ```text
    min_w max_selection sum_j w_j multiplicity_selection(j)
      = 1.7391304347826... = 40/23.
    ```

    The displayed primal optimum is uniform weight `1/23` on

    ```text
    3,12,15,21,33,48,60,69,75,78,84,87,
    102,105,111,114,123,132,147,165,183,186,192.
    ```

  - Since the optimum is far above `1`, even unrestricted nonnegative test-time weights cannot separate every admissible selection by additive incidence. A low-degree positive polynomial is a restriction of this failed class.
  - Verification grade: solver verdict. The `40/23` value still needs a rational dual certificate before it should be cited as a proof-grade optimization result.

- Verdict: killed computationally. Additive weighting cannot recover the overlap information lost by the first moment.
- Credence: very low.
- Edge generated: H19 — use an overlap-sensitive functional or analyze the tight one-gap configurations directly.

### H19 — Tight one-gap configurations expose the missing local exchange lemma

- Mode: abduction from the failure of all additive weights
- Hypothesis: every admissible selection at the first boundary misses a test time; after unit normalization, the obstruction can be expressed as a local exchange law around a configuration that covers every time except `1`.
- Kill condition: admissible one-gap configurations have no stable arithmetic pattern under normalization, or the required exchange law is equivalent in complexity to the original set-cover instance.
- Trial:

  1. Search directly for high-coverage legal selections rather than a common linear separator.
  2. Normalize any unit gap to `1` using the action `v -> a v (mod D)`, taking representatives modulo sign.
  3. Classify normalized one-gap configurations by `gcd(v,9)`, their private points, and the changes caused by replacing a speed with one that covers the gap.
  4. Use the special times `p,2p,3p,4p` to force divisibility classes before analyzing the remaining exchanges.
  5. State and test the smallest local lemma that rules out closing the final gap without opening another.

- Observed outcome:

  - A deterministic swap search found the admissible selection

    ```text
    (33,46,57,149,150,160,206,207),
    ```

    which covers `210` of the `211` half-grid times and misses only `181`.
  - Since `gcd(181,423)=1`, scaling all speeds by `181` moves the sole gap to `1` and gives

    ```text
    (51,62,78,103,134,165,180,196).
    ```

    Both facts replay in the test suite. This shows the finite obstruction is exactly tight: a proof must distinguish full coverage from a one-point defect.
  - At the special time `j=p=47`, coverage is equivalent to `9 | v`; hence every hypothetical cover contains a multiple of `9`. More generally, `j=3p` forces a multiple of `3`.
  - A second normalized one-gap witness was found:

    ```text
    (54,58,110,112,139,166,168,197).
    ```

    It has gcd profile `(six g=1, one g=3, one g=9)`, unlike the first witness's `(four g=1, three g=3, one g=9)`. Counts by divisibility class therefore do not classify the tight configurations.
  - Both witnesses are isolated in the graph whose edges replace one speed while retaining coverage of all times except `1`. Moreover, replacing one speed by any speed that covers `1` opens at least three new gaps for the first witness and four for the second. This exact exchange calculation replays in `test_normalized_one_gap_covers_are_isolated_by_one_exchange`.
  - Adding the sound symmetry break `speed 1 is selected` and then also fixing the multiple `180` did not finish within the bounded solver run. These interrupted searches are `UNKNOWN`, not `UNSAT`.
  - A lean normalized CNF—speed `1` fixed, at most seven additional speeds, already-covered clauses deleted—reduced the encoding from `3663` variables and `6990` clauses to `1599` variables and `3144` clauses. Kissat still timed out, including after fixing second unit speed `2`; raw encoding size is not the dominant difficulty.

- Verdict: open frontier.
- Credence: medium as a structural reduction; low as a complete proof route.
- Edge generated: H20 — quotient the exact coverage problem into nine-point fibers over `Z/pZ`.

### H20 — Fiber phases force an impossible divisibility profile

- Mode: structural reduction from H19 and the special time `j=p`
- Hypothesis: partitioning `Z/(9p)Z` by reduction modulo `p` turns every speed into one of three rigid patterns on `Z/9Z`; the requirement that all 47 fibers be covered rules out every admissible `(g=1,g=3,g=9)` profile.
- Kill condition: the exact fiber formulation is merely a relabeling with no profile-level constraint stronger than the already-killed incidence bounds.
- Exact fiber lemma: fix `r in Z/pZ` and write the fiber as `r + a p`, `a in Z/9Z`.

  - If `gcd(v,9)=1`, the covered phases form a two-point edge when `r != 0`, and a singleton when `r=0`. The edge difference is `±v^(-1) mod 9`, so different speeds need not share one cyclic adjacency relation.
  - If `gcd(v,9)=3`, the covered phases are either empty or one full congruence class modulo `3` (three points).
  - If `gcd(v,9)=9`, the speed covers either all nine phases or none.

  The lemma follows because increasing `a` shifts `jv` by `pv`: respectively all nine `p`-spaced positions, three positions each repeated three times, or zero modulo `9p`. The strict interval `(-p,p)` then gives the stated patterns. It is exhaustively replayed by `test_mod_p_fibers_reduce_to_small_phase_patterns`.
- Consequence: outside the fibers wholly covered by a `g=9` speed, two unit speeds can hit at most two points of any missing modulo-`3` phase class. Therefore a profile with exactly two unit speeds must have active `g=3` speeds in all three phase classes on every such fiber. Similar finite phase-cover rules apply to the other profiles.
- Trial:

  1. Split the hypothetical cover by the counts `(u,t,h)` of speeds with gcd `1,3,9` against `9`.
  2. Derive the minimal `Z/9Z` phase-cover patterns for each `u`.
  3. Translate those patterns into interval-cover constraints on `r in Z/pZ`.
  4. Rule out each profile with a counting, cyclic-order, or polynomial argument.
- Observed outcome:

  - The first relaxation, retaining only total incidence at least `9` per fiber, is too weak. CP-SAT finds `(9,54,63,66,72,75,200,202)`, which satisfies every fiber-capacity inequality but misses 12 actual times. Phase positions, not just fiber totals, are essential.
  - With speed `1` normalized and exact phase coverage retained, three-second profile splits already return `INFEASIBLE` for `(u,t,h)=(2,5,1),(2,2,4),(2,1,5),(2,0,6),(3,0,5)`. All other completed bounded runs returned `UNKNOWN`; these are search directions, not proof claims.
  - The whole `u=2` branch can be consolidated without fixing `(t,h)`: select exactly six nonunit speeds, require at least one `g=9` speed, and on each nonzero fiber require either whole-fiber coverage or an active `g=3` speed in each of the three phase classes. The resulting necessary CNF has 825 variables and 1,651 clauses.
  - Glucose 4 proved that consolidated CNF `UNSAT` in 330,722 DRUP steps. `drat-trim` independently returned `s VERIFIED`; the compressed CNF, proof, checksums, semantic scope, and replay command are stored under `artifacts/k8-p47-two-unit-fiber.*`. This is a certificate for the exact-two-unit branch only, not for the full `k=8` instance.
  - After normalizing one of three unit speeds to `1`, its edge is `{0,8}` on every nonzero fiber. If no `g=9` speed covers that fiber wholesale, phase class `1` must be active among the `g=3` speeds: the two remaining unit edges otherwise hit at most two of the three class-`1` points.
  - Only 174 five-nonunit selections satisfy this necessary phase-`1` condition, and an exhaustive pair check shows that none can be completed by two more unit speeds. The exact augmented CNF has 1,386 variables and 2,572 clauses. Glucose 4 emitted a 410,310-step DRUP proof, independently accepted by `drat-trim`; it and its replay metadata are stored as `artifacts/k8-p47-three-unit-fiber.*`.
  - For `u=4`, the weaker local requirement is that at least one `g=3` phase class be active whenever no `g=9` speed covers the fiber wholesale. Exactly 208,104 four-nonunit selections satisfy this condition. An exhaustive indexed-pair check found that none can be completed by three further unit speeds after normalization to speed `1`; the smallest residual before those three speeds has 40 points. Verification grade: replay, not independent certificate.
  - For `u=5`, all 37,214 nonunit triples containing at least one `g=9` speed were exhaustively tested. None can be completed by four further unit speeds after speed `1`; the smallest residual before completion has 63 points. Verification grade: replay, not independent certificate.
  - Two initial checks of `u=6`—recursive Python completion and incremental SAT over 1,311 nonunit pairs—were interrupted after poor scaling. Fixing a selected `g=9` speed to `9` by unit symmetry also left the full and `u=7` CNFs unresolved in bounded runs. Every interrupted result remains `UNKNOWN`; none is used below.
  - A bounded-memory C++ verifier then replaced those searches. It normalizes one unit speed to `1`, enumerates every admissible nonunit choice, and uses exact bitset set-cover search for the remaining unit speeds. Its pruning rules are upper capacity and a packing lower bound from test points with pairwise-disjoint coverer sets.
  - The same verifier returns:

    ```text
    VERIFIED branch=4 checked=208104
    VERIFIED branch=5 checked=37214
    VERIFIED branch=6 checked=1311
    VERIFIED branch=7 checked=23
    ```

    The counts for `u=4,5` reproduce the earlier Python runs. The `u=6,7` results close the previously open high-unit tail. `test_high_unit_exhaustive_verifier` compiles the source and replays all four branches.
  - Profiles `u<2` violate the gcd condition. Profile `u=8` is impossible because covering `j=p` requires a `g=9` speed. Therefore `u=2,...,7` exhaust every hypothetical cover.

- Verdict: proved computationally for the finite instance `k=8,p=47`. The `u=2,3` branches have independent DRUP certificates; `u=4,...,7` have a small exhaustive verifier with cross-language replay for `u=4,5`.
- Credence: high for the finite obstruction; this is not yet a proof of the nine-runner case.
- Edge generated: H21 — accumulate enough certified primes to cross the global product bound.

### H21 — Enough modular obstructions prove the nine-runner case

- Mode: deduction from Rosenfeld's prime-divisor lemma and the `p=47` obstruction
- Hypothesis: the finite obstruction can be certified for enough distinct primes that their product, together with `lcm(2,...,9)`, exceeds the explicit upper bound on the product of a minimal counterexample.
- Exact target for `k=8`:

  ```text
  B = (36^7 / 8)^8
    = 84765698874878218361067180729674171436543015292348049288994557831877912686493696.
  ```

  Starting at `47`, the first 37 primes through `233` satisfy

  ```text
  lcm(2,...,9) * product(primes 47 through 233) > B.
  ```

- Trial:

  1. Parameterize the fiber lemmas and exhaustive verifier by `p`.
  2. Certify the obstruction for the target list
     `47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233`.
  3. Seek a symbolic monotonicity or large-`p` argument before accepting 37 unrelated computations.
  4. Independently verify every finite certificate and the final integer inequality.
- Observed outcome:

  - `p=47` is now closed at all unit profiles. By the corrected finite reformulation, this proves that `47` divides the product of the eight relative speeds in any hypothetical nine-runner counterexample.
  - The low-unit CNFs and parameterized high-unit verifier now close the first fourteen target primes `47,53,59,61,67,71,73,79,83,89,97,101,103,107`. Exact branch counts are recorded in `artifacts/h21-prime-replay.tsv`.
  - Parameterization exposed and repaired a verifier-width bug: the first version used three 64-bit words for candidate coverer sets, sufficient through `p=61` but not beyond. All `p>=67` high-unit results were withdrawn and recomputed with the full 17-word width. Address/undefined-behavior sanitizers replay the corrected `p=67,u=4` branch without error.
  - A Claude/Sonnet review proposed a finite carry automaton on the nine-phase masks. The coarse relaxation is killed: locally covered edge configurations admit self-loops when carry choices are independent. A refinement would have to retain mechanical-word carry feasibility. It remains finite, but is deferred unless it avoids an open prime-distribution problem.
  - The same review recommended proof-producing SAT plus an independent formula regenerator. This matches the surviving certificate route; rerunning the same generator and solver is not counted as independent verification.

- Verdict: superseded as the route to the selected target. Fourteen of 37 proposed obstructions were closed by the local profile split, but the published lifting sieve proves a stronger 39-prime statement and completes the nine-runner case.
- Credence: medium that the finite computations extend, low that brute force alone is the right final proof.

### H22 — The published lifting sieve proves the nine-runner case

- Mode: reconstruction, independent replay, and exact arithmetic
- Hypothesis: Trakulthongchai's `1 -> 3 -> 9` lifting sieve proves `I(8,9,p)=empty` for a prime set whose product exceeds the finite-checking bound, thereby excluding every nine-runner counterexample.
- Kill condition: any target prime has a nonempty final improper set; any local intermediate cardinality differs from the published receipt; the prime list is not pairwise coprime; the forced product does not exceed the bound; or a lifting/divisibility implication fails semantic inspection.
- Trial:

  1. Check Lemmas 5 and 7 and the proof of Theorem 2 in Trakulthongchai's 2026 revision.
  2. Pin public verifier commit `e17c415b807258806cd9192a17e9a51e20455a75` and source digest `25a417a...d200d0a5`.
  3. Run the unmodified verifier for all 39 primes `47,...,241`.
  4. Compare every level-1, level-3, and level-9 cardinality against the authors' receipt.
  5. Verify primality and the final product inequality with exact integers.
- Observed outcome:

  - All 39 runs completed successfully. Every intermediate cardinality matches the published receipt, and every final level-9 set has size zero. The exact rows are in `artifacts/nine-runner-sieve-replay.tsv`.
  - The forced prime product is

    ```text
    19570880530831227159611114469289180443865177656785618176063821114999202895619850591,
    ```

    while the minimal-counterexample bound is

    ```text
    (36^7 / 8)^8
    = 84765698874878218361067180729674171436543015292348049288994557831877912686493696.
    ```

    The former is about `230.882` times larger.
  - Rosenfeld's independent proof supplies a different corroborating route using prime powers and extra divisibility conditions.
- Verdict: the nine-runner theorem is proved in the cited literature and completely reproduced here at semantic-match plus independent-replay grade. This is not a new theorem and not a proof of the general conjecture.
- Credence: high. Remaining computational trust is common-mode source/compiler error because the sieve does not emit formal proof certificates.
- Artifact: `artifacts/nine-runner-sieve-audit.md`.

### H23 — Non-tight tuples have a universal grid denominator

- Mode: direct falsification of Conjecture 7.1 in Sungkawichai--Trakulthongchai (2026)
- Hypothesis: for fixed `k+1`, some `D` ensures that every coprime non-tight positive speed tuple has a witness in `(1/d)Z` for every `d >= D`.
- Kill condition: an unbounded family of denominators `d` and coprime non-tight tuples with no witness on the `d`-grid.
- Trial: for `k=2` and every `r >= 1`, set `d=6r+1` and take speeds `(1,3r)`.
- Observed outcome:

  - `gcd(d,3r)=1`, so even requiring every speed to be a unit modulo the denominator does not repair the statement.
  - The tuple is non-tight. If `3r` is odd, `t=1/2` is a strict witness. If `3r=2a`, then `t=a/(2a+1)>1/3` gives both speeds the same distance `t`.
  - No `j/d` is a witness. Outside the middle third, speed `1` is bad. Inside it, parity gives `3r(2s)=-s mod d` and `3r(2s+1)=3r-s mod d`; the resulting distance is at most `2r/(6r+1)<1/3`.
  - The first 100 instances replay with exact rational arithmetic in the test suite.
- Verdict: killed deductively as written.
- Credence: deductive, subject only to the source statement having the intended quantifier order.
- Edge generated: any repair must depend on tuple height or fixed-integer realizability. Uniform finite grids cannot control an object allowed to scale with the grid. Likewise, a prime-power lift theorem cannot quantify over all compatible profinite branches: compatible non-Archimedean survivor families exist.
- Artifact: `artifacts/conjecture-7-1-counterexample.md`.

### H24 — Height-sensitive grid recovery

- Mode: repair H23 by preserving the height of one fixed integer tuple
- Statement: let `v` be a positive `k`-speed tuple, let `M=max(v)`, and suppose its maximum loneliness is strictly greater than `1/(k+1)`. Then every denominator `d > (k+1)M^2` has a strict witness in `(1/d)Z`.
- Proof:

  - The lower envelope `min_i ||v_i t||` reaches its maximum at a cusp or at an intersection of two affine pieces.
  - Every such critical time has denominator at most `2M`: it divides some `2v_i`, `v_i+v_j`, or `|v_i-v_j|`.
  - The maximum value therefore has denominator at most `2M`. If it exceeds `1/(k+1)`, its gap above the threshold is at least `1/(2M(k+1))`.
  - Rounding a maximizing time to the nearest point of a `d`-grid changes every runner's distance by at most `M/(2d)`. This is smaller than the gap when `d>(k+1)M^2`.
- Verdict: proved.
- Verification: `maximum_loneliness` computes the exact critical-time maximum; the test suite checks canonical exact values and the grid conclusion on small non-tight tuples.
- Limitation: this converts a strict real witness into grid witnesses; it does not prove that every tuple has the initial real witness.
- Edge generated: a general proof must explain why a central-cube miss by one fixed integer direction creates bounded algebraic structure, rather than asking for height-free grid compactness.
- Artifact: `artifacts/general-case-hypotheses.md`.

### H25 — A central-cube miss forces a bounded integer relation

- Mode: Archimedean duality, proposed by the Claude clean-room audit
- Hypothesis: for each `k`, if `L(v)=max_t min_i ||v_i t|| < 1/(k+1)`, then the actual integer vector `v` has a nonzero relation `a dot v=0` with `||a||_1 <= C(k)` and a sign pattern supporting contraction, polynomial degeneracy, or descent.
- Why it survives H23: the relation is imposed on one fixed ordinary integer vector. The spurious compatible residues `(q^a-1)/2` change their centered integer representative at every level.
- Audit result: the original finite test was non-operational because the antecedent `L(v)<1/(k+1)` is itself an unknown counterexample. The weak conclusion is nevertheless provable directly, and even holds at equality; see H28.
- Missing content: “a sign pattern supporting descent” carries the entire burden but has no specified transformation or preservation lemma.
- Verdict: split. The bounded-relation half is proved with an explicit coefficient bound; the descent half remains open and must be stated as a concrete transformation before testing.
- Prime boundary: prime-modular lifting may help test this hypothesis, but no prime-distribution statement is built into it. Prime-only obstacles belong to that proof route and remain deliberately open.
- Artifact: `artifacts/general-case-hypotheses.md`.

### H26 — A critical-time graph supplies the relation

- Mode: exact active-set geometry
- Hypothesis: the runners active at one maximum form a connected graph with a bounded signed cycle whose summed edge equations give a useful relation among the speeds.
- Kill condition: the cycle equations telescope, or known extremal fixtures have no such graph.
- Trial: on an affine piece write the active runner equation as `epsilon_i(v_i t-m_i)=L`. Equality along an edge `i-j` is the difference of the two vertex equations.
- Observed outcome:

  - Every oriented cycle sums vertex-potential differences and therefore gives the identity `0=0`, not a new speed relation.
  - The tight tuple `(1,2,3)` has only runners `1` and `3` active at each maximizing time. The tight four-speed tuples `(1,2,3,4)` and `(1,3,4,7)` likewise have disjoint active pairs rather than a connected active graph at one time.
- Verdict: killed as stated. Relations would have to couple several distinct critical times or use additional inequalities; a single active graph contains no cycle information beyond telescoping.
- Artifact: `artifacts/multi-fast-runner-lemma.md`.

### H27 — A large upper gap with fewer than half fast runners is safe

- Mode: Archimedean interval measure, generalizing the one-very-fast-runner idea
- Statement: sort `N` speeds and split them into `m=N-r` slow and `r` fast speeds, with `2r<N+1`. Let `L` be the exact maximum loneliness of the slow tuple, `M` its largest speed, and `delta=1/(N+1)`. If

  ```text
  ((L-delta)/M) * (1-2r*delta) > delta * sum_fast(1/v),
  ```

  then the full tuple satisfies LRC.
- Proof idea: around a maximizing slow time, an interval of radius `(L-delta)/M` keeps every slow runner valid. On an interval of length `ell`, one fast runner is bad on measure at most `2*delta*ell+2*delta/v`. The displayed inequality says the union of all fast bad sets cannot fill the slow-valid interval.
- Inductive corollary: assuming LRC for `m` speeds, it is enough that the smallest fast speed `V` satisfy

  ```text
  V > M * (m+1) * (N+1) / (N+1-2r).
  ```

  Hence a hypothetical counterexample cannot have such an upper multiplicative gap at any cut with fewer than half its speeds above the cut.
- Verdict: proved.
- Verification: exact enumeration checks every triggered certificate among four-speed tuples of height `14` and five-speed tuples of height `10`, plus explicit two-fast fixtures `(1,2,100,101)` and `(1,2,3,120,121)`.
- Limitation: the union bound becomes silent at `2r>=N+1`; the lower half of the speed vector remains uncontrolled.
- Artifact: `artifacts/multi-fast-runner-lemma.md`.

### H28 — A bad or tight tuple has a uniformly bounded Fourier relation

- Mode: exact Fourier expansion of a supported triangular bump
- Statement: fix `n` and `0 <= delta < 1/2`. Put `a=1/2-delta`, `S=a+1/(3a)`, and

  ```text
  K = floor(2n S^(n-1) / (9 a^(n+1))) + 1.
  ```

  If `ML(v_1,...,v_n) <= delta`, then some nonzero integer vector `m` satisfies `sum_i m_i v_i=0` and `max_i |m_i| <= K`.
- Proof:

  - Let `f` be the height-one triangular bump centered at `1/2`, supported on `[delta,1-delta]`. If `ML(v)<=delta`, then `product_i f(v_i t)` vanishes identically, including at tight witnesses because some factor is on the support boundary.
  - Its mean is `a`; its Fourier coefficients are absolutely summable, with total `l1` norm at most `S` and tail past `K` less than `2/(9aK)`.
  - Integrating the product retains exactly frequency tuples satisfying `sum_i m_i v_i=0`. If every nonzero relation had some coefficient larger than `K`, the nonconstant terms would have absolute sum less than `n * 2/(9aK) * S^(n-1) < a^n`.
  - The positive constant term is `a^n`, so the integral could not be zero. Contradiction.
- LRC specialization: at `delta=1/(n+1)`, the bounds `K` for `n=2,...,13` are `209, 428, 1028, 2561, 6439, 16214, 40753, 102112, 254978, 634500, 1573723, 3891190`.
- Verdict: proved.
- Verification: exact code evaluates the rational bound and finds relations for failed-threshold fixtures and the tight tuples `(1,2)`, `(1,2,3)`, and `(1,2,3,4)`.
- Consequence: a hypothetical counterexample lies in one of finitely many rational hyperplanes whose normal vector depends only on `n`. The unresolved step is to prove LRC, or a descent, on each resulting relative subtorus.
- Artifact: `artifacts/fourier-short-relation.md`.

### H29 — First-band tuples have a connected coefficient-two relation graph

- Mode: exact near-tight spectrum structure
- Hypothesis: if `ML(v_1,...,v_n) <= 2/(2n+1)`, form a hypergraph from the indecomposable supports of integer relations `sum_i a_i v_i=0` with `|a_i|<=2`. This hypergraph is connected.
- Certificate correction: an arbitrary relation support is invalid as an edge when it splits into two disjoint supports that each carry their own bounded relation. Adding those unrelated relations creates a spurious cross-block support. The regression `(1,2,100,200)` must have components `{1,2}` and `{100,200}`, not one component.
- Why this is the needed strengthening: H28 can return a relation confined to a proper subset. Connectivity couples every speed, bounds all ratios through a finite chain, and gives a concrete target for relative-subtorus descent.
- Broad version killed: merely assuming `ML(v)<1/n` is insufficient. The family `(1,2,3s)` has `ML=s/(3s+1)<1/3`, while the coefficient needed to connect `3s` grows with `s`. These values accumulate at the lower-dimensional threshold `1/3`.
- First-band trials:

  - Complete primitive scans through `(n,height)=(3,100),(4,35),(5,30),(6,22),(7,20)` found respectively `5,6,8,10,13` first-band tuples.
  - Every survivor was revalidated after the decomposable-support bug was fixed; all have connected coefficient-two relation hypergraphs.
  - New coefficient-two fixtures beyond the earlier range include `(1,3,4,5,18)` with `ML=2/11`.
  - The published amended-spectrum exception `(1,3,4,5,7,13,18)`, with `ML=3/23<2/15`, is connected using coefficient-one relations.
  - The cutoff regression `(1,2,18)` has `ML=6/19<1/3` but remains disconnected even at coefficient bound `5`.
- Verdict: survives current exact fixtures; not proved.
- Kill condition: a tuple at or below `2/(2n+1)` whose coefficient-two relation hypergraph is disconnected.
- Next proof target: a connected-cluster Fourier expansion. Proper components have a uniform loneliness gap because the cutoff lies strictly below their lower-dimensional threshold; use that positive component mass to force a bounded cross-component frequency.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H30 — Induction gives a coarse first-band height bound

- Mode: quantitative Kronecker theorem plus lower-runner induction
- Statement: assume LRC for `n-1` speeds. If `ML(v)<=2/(2n+1)` and `v` is primitive, then

  ```text
  ||v||_2 <= [n(n-1)(2n+1)]^(n-1).
  ```

- Proof: the gap from the lower-dimensional guarantee `1/n` to the first-band ceiling is `g=1/[n(2n+1)]`. Use density radius `epsilon=g/2`. Giri--Kravitz's tube argument says a 1-dimensional subtorus of volume `V` is `epsilon`-dense in a higher-dimensional subtorus once `V*omega_(n-1)*epsilon^(n-1)>1`. Induction bounds the latter subtorus by `D<=1/2-1/n`, so density would give `ML(v)>=1/n-epsilon>2/(2n+1)`, a contradiction. Finally use the cube lower bound `omega_d >= (2/d)^d` with `d=n-1`.
- Consequence: a connected relation certificate exists with a very large coefficient depending only on `n`; pair relations already span the full kernel. This proves coarse finite structure but not the sharp coefficient `2`.
- Verdict: proved, conditional only on the standard induction hypothesis for fewer runners.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H31 — First-band tuples have a positive triangular relation tree

- Mode: operational refinement of H29
- Hypothesis: H29's components can be spanned by indecomposable coefficient-two relations, each oriented as

  ```text
  v_max = sum_{i in S} c_i v_i,     c_i in {1,2}, v_i < v_max.
  ```

- Trial: exact certificates were extracted for every survivor in the five complete scan ranges. The form survives, including `(1,5,6,11,16,17)` and the seven-speed amended-spectrum exception.
- Why it matters: this specifies the sign pattern and transformation shape that H25 left hidden; it is a candidate input to a relative-subtorus elimination lemma.
- Verdict: survives current exact scans; not proved.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H32 — Two positive seeds generate every first-band tuple

- Mode: strengthen H31 to an acyclic positive recurrence
- Hypothesis: after sorting, all but at most two speeds are positive `{0,1,2}`-combinations of earlier speeds.
- Kill condition: a first-band tuple with at least three speeds lacking such an earlier representation.
- Counterexamples:

  - `(2,5,6,8,10,11)` has `ML=2/13`; the speeds `2,5,6` are all positive seeds under coefficient two.
  - `(2,6,7,8,10,13,14)` has `ML=2/15` and likewise needs three positive seeds.

- Verdict: killed. Signed elimination still leaves only two parameters in both examples, generating H33.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H33 — First-band coefficient-two relations have rank at least `n-2`

- Mode: bounded Freiman dimension / relative-subtorus reduction
- Hypothesis: if `ML(v)<=2/(2n+1)`, the rational span of all relations `a dot v=0` with `a_i in {-2,-1,0,1,2}` has rank at least `n-2`.
- Equivalent consequence: `v` lies in a rational linear subspace of dimension at most two defined by coefficient-two normals. For fixed `n` there are only finitely many such subspaces.
- Trial: exact rational row reduction found rank at least `n-2` for all `55` first-band survivors across the seven complete scan ranges through nine speeds. It includes both H32 counterexamples; for `(2,5,6,8,10,11)`, signed elimination gives `6=2*5-2*2`.
- Why it matters: every hypothetical counterexample lies below the first-band ceiling. Proving H33 would reduce it to a 1-dimensional subtorus inside one of finitely many 2-dimensional rational subtori, precisely the objects whose relative spectra Jain--Kravitz show are explicitly computable by finite calculation.
- Verdict: survives complete bounded scans; not proved.
- Kill condition: a first-band tuple whose bounded relation rank is at most `n-3`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H34 — First-band coefficient-two relations have full rank `n-1`

- Mode: strengthen H33 from two parameters to a finite list of rays
- Hypothesis: every first-band tuple has coefficient-two relation rank `n-1`.
- Kill condition: a first-band tuple with rank at most `n-2`.
- Counterexample: `(3,4,7,11)` has `ML=2/9` and coefficient-two relation rank exactly `2=n-2`. Its bounded-relation nullspace has the primitive integer basis

  ```text
  (2,-1,1,0), (1,-1,0,-1).
  ```

- Verdict: killed. H33's two-dimensional conclusion is sharp even in the smallest completed four-speed scan.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H35 — H33 patterns have a strict ambient two-torus margin

- Mode: explicit relative-subtorus descent
- Hypothesis: every irreducible two-column coefficient pattern arising under H33 has ambient maximum loneliness strictly greater than `1/(n+1)`.
- Exact test: partition the parameter square by the integer parts of its coordinate forms and maximize the lower envelope by rational linear programming.
- Trial: the only genuine rank-`n-2` patterns in the completed scans occur for `(1,5,6)`, `(2,3,5)`, and `(3,4,7,11)`. Their ambient maxima are respectively `1/3`, `1/3`, and `1/4`, with margins `1/12`, `1/12`, and `1/20` above the LRC threshold.
- Consequence: if the largest squared row norm is `L^2` and the margin is `rho>0`, a primitive parameter pair `(A,B)` is automatically safe once

  ```text
  A^2+B^2 > L^2/(4 rho^2).
  ```

  This follows because its geodesic has flat-torus covering radius `1/(2 sqrt(A^2+B^2))`. Only finitely many smaller pairs remain.
- Theorem under induction: Giri--Kravitz Lemma 3.3 gives `max S_2(n)=max S_1(n-1)` in the distance-to-center convention. If LRC holds for `n-1` speeds, every proper two-dimensional subtorus therefore has ambient maximum loneliness at least `1/n`, strictly above `1/(n+1)` by `1/[n(n+1)]`.
- Verdict: proved under the lower-runner induction hypothesis. The feared zero-margin case cannot occur. Pattern-by-pattern optimization is needed only to make the remaining finite parameter cutoff explicit.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H36 — Four-coordinate coefficient-two patterns have ambient loneliness at least `1/4`

- Mode: exhaustive base-case classification and independent audit of H35
- Domain: every rank-two subspace in four coordinates generated by coefficient-two integer normals and admitting a vector with positive distinct coordinates.
- Reduction: `18,074` canonical relation subspaces; `7,332` admit positive distinct coordinates; signed coordinate permutations reduce these to `123` ambient-distance classes.
- Exact result:

  ```text
  1/4:2, 2/7:4, 1/3:31, 4/11:10, 3/8:13, 5/13:4,
  2/5:30, 7/17:1, 5/12:2, 3/7:6, 1/2:20.
  ```

- Verdict: verified exactly. The minimum is `1/4`, attained by two symmetry classes. This independently agrees with the abstract H35 induction bound.
- Replay: `uv run classify_four_patterns.py --exact` (several minutes).
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H37 — The counterexample-relevant rank statement holds for three speeds

- Mode: published finite-checking theorem plus exhaustive exact replay
- Published input: under the lower-runner induction hypothesis, Malikiosis--Santos--Schymura show that a primitive `n`-speed counterexample must have

  ```text
  sum_i v_i <= binom(n+1,2)^(n-1).
  ```

- For `n=3`, the bound is `36`. Exhaustive enumeration of every primitive positive distinct triple with sum at most `36` leaves exactly five tuples at or below the first-band ceiling `2/7`:

  ```text
  (1,2,3), (1,2,6), (1,3,4), (1,5,6), (2,3,5).
  ```

  Every one has coefficient-two relation rank at least `1=n-2`.
- Verdict: the counterexample-only version H39 is completely checked for `n=3`; this is not a proof of broad H33 for every first-band tuple, because the published sum bound applies to LRC counterexamples rather than all tuples with `ML<=2/7`.
- Verification: `test_complete_three_speed_first_band_check_under_published_sum_bound`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H38 — Four-speed first-band candidates have pairwise gcd at most two

- Mode: specialize the published four-speed spectrum theorem
- Fan--Sun theorem: if a primitive four-speed tuple has a pair with gcd greater than `3`, then `ML>=1/4`. The same holds for gcd `3`, except for `(1,2,3,12k)`, whose value is `3k/(12k+1)`.
- First-band consequence: `2/9<1/4`, and `3k/(12k+1)>2/9` for every positive integer `k`. Hence every tuple with `ML<=2/9` has all pairwise gcds at most `2`.
- Verdict: proved. Combined with the published sum bound `1000`, this sharply defines the finite domain relevant to a hypothetical four-speed LRC counterexample. The sum bound does not bound every tuple in the wider first spectral band.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H39 — Minimal counterexamples have coefficient-two relation rank at least `n-2`

- Mode: restrict H33 to exactly the quantifier needed by general-case induction
- Hypothesis: if `v` is a primitive minimal LRC counterexample with `n` speeds, then the rational span of relations `a dot v=0` with `a_i in {-2,-1,0,1,2}` has rank at least `n-2`.
- Difference from H33: H33 asserts the rank conclusion for every tuple with `ML<=2/(2n+1)`. H39 asserts it only for hypothetical LRC counterexamples, which satisfy the stronger inequality `ML<1/(n+1)`. The published finite-checking bound is valid for H39's domain but cannot by itself prove H33's wider quantifier.
- Why sufficient: under minimal-counterexample induction, H39 places the cyclic orbit inside a proper subtorus of dimension at most two. H35 supplies a strict ambient margin, and geodesic covering reduces the remaining parameter pairs to a finite residue.
- Verdict: selected as the load-bearing general-case hypothesis. It is proved for `n=3,4` by H37 and H40 and survives all larger bounded scans.
- Kill condition: a bounded-runner counterexample whose coefficient-two relation rank is at most `n-3`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H40 — H39 holds completely for four speeds

- Mode: exact exhaustive audit of the published counterexample domain
- Domain: every strictly increasing positive quadruple with sum at most `1000`; grid witnesses safely reject most tuples, nonprimitive tuples scale to smaller ones, and Fan--Sun removes unresolved tuples with pairwise gcd at least `3`.
- Exact receipt: `1,705,044,764` quadruples enumerated; `1,705,042,194` rejected by explicit grid witnesses; `1,473` unresolved tuples were nonprimitive; `1,091` were rejected at exact critical times; six first-band survivors remained, all with coefficient-two relation rank `2=n-2`; zero rank failures.
- Verdict: complete. This proves the counterexample-relevant rank implication for `n=4`; it does not assert that the six survivors are counterexamples (the known four-speed LRC theorem rules that out).
- Replay: compile `verify_h33_n4.cpp` and run `/tmp/verify_h33_n4 1000 0 1`.
- Artifact: `artifacts/h33-n4-counterexample-domain.md`.

### H41 — Every counterexample with `n>=18` has a coefficient-one relation

- Mode: dissociated Riesz product, following Bedert's Lemma 4.1 with constants retained
- Statement: if `n>=18` and `v` is an LRC counterexample, some nonzero `epsilon in {-1,0,1}^n` satisfies `epsilon dot v=0`.
- Proof: if no such relation exists, the Riesz product `R(t)=product_i(1-cos(2 pi v_i t))` and every one-factor deletion have integral `1`. The bad intervals at `delta=ML(v)` cover the circle, so integration gives

  ```text
  1 <= n(1-cos(2 pi delta)).
  ```

  But `delta<1/(n+1)`, `1-cos x<=x^2/2`, and `pi^2<10` make the right side strictly less than `20n/(n+1)^2<=1` for `n>=18`, a contradiction.
- Consequence: H39's first independent relation is proved with coefficient bound `1`, uniformly and without primes. The missing step is to iterate the argument until the relation rank reaches `n-2`.
- Verdict: proved.
- Artifact: `artifacts/riesz-unit-relation.md`.

### H42 — Minimal counterexamples have a two-element maximal coefficient-two dissociated seed

- Mode: stronger operational form of H39, proposed by the relation-lattice audit
- Hypothesis: every primitive minimal LRC counterexample has some inclusion-maximal subset `S` of at most two speeds with no nonzero relation having every coefficient in `{-2,-1,0,1,2}`.
- Star consequence: for every target `j` outside `S`, maximality supplies an exact coefficient-two relation supported on `S union {j}`. Its target coefficient is nonzero. One relation per target is independent because the matrix on the nonseed coordinates is diagonal with nonzero diagonal. Therefore the relation rank is at least `n-|S|>=n-2`, proving H39.
- Evidence: all 42 primitive first-band survivors in the completed scans for `3<=n<=7` have such a seed set. The complete four-speed counterexample-domain survivors all pass.
- Broad-form obstruction: `(1,4,5,6,7,11,13,16)` has `ML=2/17` but requires three direct seeds. Thus the analogous statement for every first-band tuple is false at eight speeds.
- Caution: H42 is strictly stronger than H39. Independent short relations arranged in a long chain need not all be generated from a single pair; counterexample minimality would have to exclude that geometry.
- Verdict: the broad first-band form is killed; the narrower minimal-counterexample hypothesis remains open but is superseded experimentally by H44.
- Kill condition: a possible minimal counterexample, or a compelling first-band family, for which every maximal coefficient-two dissociated subset has size at least three.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H43 — The unmodified Riesz product can be iterated after finding one relation

- Mode: exact constant-term audit
- Proposal: after H41 finds one short relation, reuse `product_i(1-cos(2*pi*v_i*t))` and its one-factor deletions to force another.
- Obstruction: the circuit `(1,2,3)` has Riesz integral `3/4` and normalized cover ratio `1/4`, rather than the dissociated value `1/3`. The two signed Fourier terms for `1+2-3=0` each contribute `-1/8`, already larger than H41's asymptotic gap.
- Scan: none of the 42 completed first-band survivors has normalized ratio large enough to contradict `ML<1/(n+1)` using the unmodified product.
- Verdict: killed. A viable successor must annihilate known circuit terms by reweighting, or contract short circuits using minimal-counterexample structure.
- Verification: `riesz_constant_term`, `riesz_cover_ratio`, and their exact regression tests.
- Artifact: `artifacts/riesz-unit-relation.md`.

### H44 — Minimal counterexamples admit a two-seed bounded appendability ordering

- Mode: temporal-spanner-inspired weakening of H42
- Definition: a target speed is coefficient-two appendable to an available set `S` when an exact relation `c_j v_j + sum_(i in S) c_i v_i=0` has every coefficient in `{-2,-1,0,1,2}` and `c_j` nonzero.
- Hypothesis: every primitive minimal LRC counterexample has two seed speeds from which all remaining speeds can be appended successively.
- Rank consequence: order one chosen relation per appended target. Restricted to target columns, the relation matrix is triangular with nonzero diagonal, so its `n-2` rows are independent. Hence H44 implies H39.
- Strict weakening: the eight-term Fibonacci chain needs three direct H42 seeds but is H44-appendable from `(1,2)`. The first-band tuple `(1,4,5,6,7,11,13,16)` likewise kills broad H42 while appending from `(1,4)` via `5=1+4`, `6=1+5`, `7=1+6`, `11=4+7`, `13=6+7`, and `16=5+11`.
- Evidence: all 55 primitive first-band survivors in the completed scans through `n=9` pass; a dissociated control `(5,7,11)` fails.
- Stalled-core consequence: if closure from every seed pair stops, every coefficient-two relation crossing from the available set contains at least two unresolved coordinates. This gives an exact nondismountable core for the complementary branch.
- Verdict: selected for testing, not proved.
- Kill condition: a possible minimal counterexample, or a structured first-band family, with no two-seed appendability ordering.
- Verification: `bounded_appendability_certificate`, scan column `two_seed_appendable`, and exact separator regressions.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H45 — Sliding-window handoff owners seed the appendability ordering

- Mode: canonical geometric seed selection for H44, motivated by windows scheduling and augmenting-path load balancing
- Load identity: at `delta=1/(n+1)`, the bad-window load `L(t)=#{i: ||v_i t||<delta}` has exact mean `2n/(n+1)<2`. Therefore some constant-load cell has load at most one.
- Rule: compress the singleton-load cells into their cyclic owner sequence. For each cyclic rotation, order runners by first appearance.
- Hypothesis: in every primitive minimal LRC counterexample, some rotation is a coefficient-two elimination order: its first two owners are seeds and every later first-time owner has a coefficient-two relation supported only on itself and earlier owners.
- Consequence: the selected relations are triangular on the first-occurrence targets, giving `n-2` independent rows and proving H39 directly.
- Evidence: the cyclic-order rule passes all 55 completed first-band survivors through nine speeds at the conjectured width. The original 49 through eight speeds also pass at three tested slack full-cover widths. Every one of the 385 distinct transition edges in those slack profiles lies in some coefficient-two relation.
- Reset-order control: `(2,3,5,6,8,11)` has `ML=3/19`, just outside the first band. Its reset order stalls from `(2,11)`, while rotating to `(11,8)` gives the full elimination order `(11,8,6,5,3,2)`. This kills the generic reset-anchored strengthening and makes cyclic rotation load-bearing.
- Caveat: H46 makes the transition graph connected, and the scan links every transition edge to a short relation, but neither fact guarantees that the relation avoids owners appearing later in the order.
- Verdict: selected for testing, not proved.
- Kill condition: a possible minimal counterexample for which every cyclic first-occurrence order stalls before visiting all runners.
- Verification: `periodic_bad_window_cells`, `singleton_handoff_owners`, `handoff_transition_edges`, `handoff_elimination_certificate`, and scan column `handoff_order_eliminates`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H46 — Every runner in a minimal counterexample owns a singleton-load window

- Mode: lower-runner induction plus continuity
- Statement: assume LRC for `n-1` speeds and let `v` be an `n`-speed counterexample at `delta=1/(n+1)`. For every runner `i`, there is a nonempty open interval on which `i` is the unique bad runner.
- Proof: apply the lower case to the tuple with `i` removed. At some `t_i`, every remaining runner has distance at least `1/n`, with uniform slack `1/n-1/(n+1)=1/(n(n+1))` above `delta`. Since the full tuple is a counterexample, runner `i` must be bad at `t_i`. Continuity preserves both strict conditions on a neighborhood of `t_i`.
- Consequence: every runner occurs in the cyclic singleton-owner sequence. The handoff transition edges form a closed walk visiting all runners, hence their graph is connected. H45 only needs a rotation whose new owners can be eliminated using earlier ones.
- Verdict: proved conditionally under the standard minimal-counterexample induction.
- Verification: `inductive_private_window_margin`, exact load-profile tests, and the proof above.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H47 — A segment-local four-owner handoff order eliminates a minimal counterexample

- Mode: segment-local strengthening of H45
- Hypothesis: H45 has a successful cyclic rotation in which every new owner `j` has a relation supported on at most four runners, contains both `j` and the preceding first-time owner, draws every additional owner from the intervening handoff segment or the two initial seeds, and has every coefficient in `{-2,-1,0,1,2}`.
- Consequence: the rows remain triangular on their new-owner targets, so H47 proves H39. Compared with H45, it localizes each step to a handoff segment plus two fixed anchors.
- Evidence: all 229 elimination steps in the 55 completed certificates through nine speeds satisfy the rule. Coefficient one fails on 36 tuples. Support three fails on `(1,3,4,5,7,11,18)`; its necessary four-term step is `-2*5+2*7-2*11+18=0`.
- Killed strengthening: consecutive first-time owners need not be consecutive singleton handoffs. This fails on 75 of 229 steps; the longest observed segment crosses 24 singleton regions. A proof cannot use only one overload block.
- Why promising: despite arbitrarily repeated old owners, the certificate selects at most two of them. An unbounded-support dependence on the whole segment is unnecessary throughout the scan.
- Caveat: endpoint overlap inequalities currently give approximate relations with potentially large integer labels, not coefficient-two exact equalities. Selecting two old owners and making that arithmetic upgrade are the missing steps.
- Verdict: selected for testing, not proved.
- Kill condition: a possible minimal counterexample for which every cyclic handoff order needs coefficient above two, support above four, a future owner, or omission of the immediate predecessor.
- Verification: `local_handoff_elimination_certificate`, its segment-support and sharp-support regressions, and scan column `local_handoff_eliminates`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H48 — Strictly below the first band, coefficient-two relation rank is full

- Mode: strict-band strengthening of H39, suggested by band-edge endpoint labels
- Hypothesis: if `ML(v)<2/(2n+1)`, then `rank R_2(v)=n-1`.
- Consequence: `n-1` independent coefficient-two rows determine a primitive speed vector up to sign. The maximal-minor formula and determinant expansion give `max(v_i)<=(n-1)! 2^(n-1)`. Thus a hypothetical counterexample has an explicit finite height bound derived from sharp relations, not the much larger quantitative-Kronecker bound.
- Exact normalization: with `q=2n+1` and `delta=2/q`, every handoff endpoint satisfies `q v_i t=q m+/-2`. A hypothetical counterexample is a strict cover at this width, and its grid samples satisfy: for every `k mod q`, some `i` has `k v_i` congruent to `0,+1,-1 mod q`.
- Proved cell reduction: on `t=(k+x)/q`, every bad window is `|v_i x-r|<2` with `r=-k v_i (mod q)`. Strict coverage is equivalent to an overlapping interval chain from a label `r in {-1,0,1}` to one with `v_i-r in {-1,0,1}`. Adjacent labels obey `s v_i-r v_j<2(v_i+v_j)`, and the left side is divisible by `q`.
- Evidence: exactly 14 of the 55 completed first-band survivors are strict, distributed by `n=3,...,9` as `1,2,2,2,5,1,1`; all 14 have rank `n-1`. The H47 band-edge sweep also succeeds on all 55.
- Boundary sharpness: the three rank-`n-2` scan tuples `(1,5,6)`, `(2,3,5)`, and `(3,4,7,11)` all have `ML=2/(2n+1)`. Strictness cannot simply be dropped.
- Caveat: the modular grid cover alone does not force short additive relations: `(1,3,9)` passes it for `q=7` but has `ML=1/2` and coefficient-two rank zero. Prime `q` remains intentionally open. The missing input is continuous coverage between adjacent grid samples.
- Verdict: selected for testing, not proved.
- Kill condition: a primitive tuple strictly below the first-band edge with coefficient-two relation rank at most `n-2`.
- Verification: `strict_band_edge_grid_cover_certificate`, `band_edge_grid_cell_intervals`, `strict_band_edge_cover_certificate`, exact endpoint-event tests, the scan's `band_edge_local_handoff_eliminates` column, and bounded-relation rank.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H49 — A primitive `n+1`-divisible speed forces the first-band bound

- Mode: direct non-prime barrier suggested by the strict/interior split
- Hypothesis: for a primitive tuple of `n` distinct positive integer speeds, if `(n+1)` divides some `v_i`, then `ML(v)>=2/(2n+1)`.
- Consequence: H49 proves the general Lonely Runner Conjecture immediately. Divide arbitrary speeds by their gcd `g`. If no primitive speed is divisible by `n+1`, then `t=1/[g(n+1)]` makes every reduced residue nonzero and gives distance at least `1/(n+1)`. If a primitive divisible speed exists, H49 gives the stronger first-band bound.
- Killed broad form: primitive normalization is load-bearing. `(4,8,12)` has all speeds divisible by `4` but `ML=1/4<2/7`; it is a dilation of `(1,2,3)`.
- Evidence: all 14 strict first-band scan survivors through nine speeds avoid `n+1` multiples and contain speeds `1` and `n`. A targeted scan of 2,875,130 primitive tuples containing a divisible speed found no strict first-band tuple: `n=3` height 300, `n=4` height 60, `n=5` height 40, and `n=6` height 28.
- Sharpness: `(1,3,4,5,18)` contains a multiple of `6` and has `ML=2/11` exactly, so the claimed constant cannot be increased uniformly.
- Partial proof: lower-runner induction plus the first-band slack proves the barrier when the divisible runner is at least `2n` times faster than every other speed. The moderate-ratio case remains.
- Literature boundary: Kravitz's Spectrum Conjecture would eliminate non-tight values in the strict first band, but H49 also requires primitive tight tuples to avoid `n+1` multiples. Since tight-instance classification is open, H49 is not presently a corollary of the spectrum or tight-instance literature.
- Adversarial construction audit: no Goddyn--Wong single-acceleration construction made the accelerated speed divisible by `n+1` for `n<=500` and multiplier at most `100`. Another 7,840 exact one-speed mutations of canonical and known tight tuples produced six band-boundary cases and no strict case.
- Proved reset-cell reduction: with `N=n+1` and `t=(k+x)/N`, target-width bad windows become radius-one intervals `|v_i x-r|<1`, where `r=-k v_i mod N`. Any counterexample needs an overlapping chain in all `N` cells; adjacent labels have a positive cross-determinant divisible by `N` and strictly below `v_i+v_j`.
- Why promising: it converts the adversarial mixed-speed problem into exactly the user's reset/backoff dichotomy and avoids prime-modulus analysis. At the band edge, the moderate-ratio case has the proved radius-two interval-chain representation.
- Verdict: selected for testing; sufficient for the general case; not proved.
- Kill condition: any primitive tuple containing an `n+1` multiple with `ML<2/(2n+1)`.
- Verification: targeted exact scans, the strict-divisibility regressions, `lrc_grid_cell_intervals`, `strict_lrc_cell_cover_certificate`, and `maximum_loneliness`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H50 — Reset counting handles a largest divisible speed with small gcd strata

- Mode: proved non-prime subcase of the reset/backoff program
- Statement: put `N=n+1`. If the largest speed `w` is divisible by `N` and every slower speed satisfies `gcd(v_i,N)<=2`, then `ML(v)>=1/N`.
- Proof: test `t_k=(k+1/w)/N` for `k mod N`. The largest runner is exactly `1/N` from an integer. Writing `y=v/w in (0,1)`, a slower runner is bad precisely when `distance(kv+y,NZ)<1`. If `gcd(v,N)=1`, its two bad indices solve `kv=0,-1 mod N`; if the gcd is two, its two bad indices solve `kv=0 mod N`. Every bad-index set has size two and contains zero. The `N-2` slower runners therefore block at most `1+(N-2)=N-1` candidates.
- Consequence: an unresolved primitive H49 tuple must have an `N`-divisible speed below the maximum or another speed in a gcd stratum at least three. This isolates the genuinely mixed-factor case.
- Sharp boundary fixture: `(1,3,4,5,18)` is outside the theorem because `gcd(3,6)=3`; all six reset candidates are blocked, and its maximum is the first-band edge `2/11`.
- Verdict: proved.
- Verification: `largest_divisible_reset_witness` and exact witness regressions at moderate speed ratios.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H51 — Exact reset-kernel certificate removes the gcd cutoff

- Mode: proved arithmetic characterization of the reset/backoff candidates
- Statement: put `N=n+1`, let the largest speed `w` be divisible by `N`, and test `t_k=(k+1/w)/N`. A slower speed `v` blocks exactly `{0,-v^{-1}}` when `gcd(v,N)=1`, and exactly the kernel `{k:kv=0 mod N}` otherwise. Hence an unblocked reset index is an explicit LRC witness.
- Proof: write `y=v/w in (0,1)`. Badness is `distance(kv+y,NZ)<1`. Unit residues zero and minus one are the only possibilities. If `d=gcd(v,N)>1`, the residues are multiples of `d`, and only zero can qualify because `d-y>1`.
- Consequence: H50 is the union-bound corollary. Higher gcd strata can help through kernel overlap: `(1,3,5,7,12)` leaves `k=3` unblocked and yields `t=37/72`. The sharp fixtures `(1,3,4,5,18)` and `(1,4,5,6,7,11,16)` instead block every reset candidate and saturate all unit residue classes.
- Verdict: proved exact certificate; not a proof when its union is all of `Z/NZ`.
- Verification: `largest_divisible_reset_blocked_indices`, direct-arithmetic exhaustive regressions through six speeds, and exact witness tests.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H52 — All phase boundaries of the largest divisible runner suffice

- Mode: attempted phase-shift extension of H51
- Hypothesis: if the largest speed `w` is divisible by `N=n+1` and the LRC bound holds, some witness occurs at `t=(j+/-1/N)/w`, where the largest runner is exactly at the target boundary.
- Positive fixture: the fixed H51 reset offset is fully blocked for `(1,3,4,5,18)`, but the larger boundary set finds `t=47/108`.
- Kill: `(1,3,4,5,12)` has `ML=2/9>1/6`, while every largest-runner boundary candidate fails.
- Lesson: a variable-backoff algorithm must include window events owned by the slower runners; the divisible runner's phase clock alone loses necessary handoffs.
- Verdict: killed.
- Verification: `largest_divisible_boundary_witness` and exact boundary regressions.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H53 — Exact residue-class minimum for a full reset block

- Mode: proved adversarial set-cover invariant refining H51
- Statement: suppose the largest speed is the unique `N`-divisible speed. The minimum number of slower residue classes that can block all H51 reset candidates is `phi(N)` for prime `N`, and `phi(N)+omega(N)` for composite `N`, where `omega` counts distinct prime divisors.
- Proof: every nonzero unit reset `k` forces its unique unit residue `v=-k^{-1}`, requiring all `phi(N)` unit classes. For composite `N`, blocking reset `p` requires `N/p|v` for each prime `p|N`; one proper residue cannot serve distinct primes because `lcm(N/p,N/q)=N`. Conversely, unit residues block the units and residues `N/p` block every nonunit reset divisible by `p`.
- Consequence: only `N-2` slower runners exist, so the largest, uniquely divisible subcase follows whenever this minimum exceeds `N-2`. This includes every prime `N` and `N=4`. The prime conclusion is elementary here; no unresolved prime branch is invoked.
- Sharpness: for `N=6` the minimum is four, exactly the number of slower runners, and `(1,3,4,5,18)` realizes the required residue pattern.
- Verdict: proved.
- Verification: `minimum_unique_divisible_reset_blockers` and exact values across prime, prime-power, and mixed composite moduli.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H54 — A full reset block must escape in a central cell

- Mode: attempted geometric localization after H53
- Hypothesis: if all reset candidates are blocked with a unique divisible largest speed, one of the central radius-one cells is not strictly covered.
- Kill: `(1,2,3,5,6)` blocks all six reset candidates and strictly covers cells `2` and `3`; its uncovered cells are `1` and `4`.
- Lesson: the symmetric gaps seen in the first sharp fixtures are real, but their location is not fixed by reset saturation alone.
- Verdict: killed.
- Verification: exact `strict_lrc_cell_cover_certificate` regression.

### H55 — Unit grid points force a two-sided handoff skeleton

- Mode: proved local event invariant for the full sliding-window sweep
- Statement: suppose `w` is the unique `N`-divisible speed. At every unit grid point `k/N`, `w` is centered in its bad window; slower runners with `kv=1 mod N` are the boundary owners immediately to the left, and those with `kv=-1 mod N` are the boundary owners immediately to the right. No other slower runner is locally bad.
- Consequence under H53 saturation: every unit residue occurs, so both sides exist at every unit grid point and the sweep pairs residues `r` and `-r` through `w`. Selected opposite runners satisfy `N|(v_r+v_{-r})`.
- Limitation: the quotient `(v_r+v_{-r})/N` is height-dependent, so the divisibility alone is not yet a bounded relation or an induction step.
- Verdict: proved.
- Verification: `unit_grid_handoff_skeleton`, saturated sharp fixtures, and a missing-residue fixture with empty handoff sides.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H56 — Opposite-unit quotient collisions force a bounded relation

- Mode: proved low-height bridge from reset saturation to relation rank
- Statement: under H55 saturation write the unique divisible largest speed as `w=Na` and choose one representative `v_r` per unit residue. Each opposite pair has `v_r+v_{-r}=Nq_r` with `1<=q_r<=2a-1`. If `q_r=a`, the pair sums to `w`; equal non-`a` quotients give pair-sum differences. For `P=phi(N)/2` pairs and `d` distinct non-`a` quotients, these rows are independent and have rank `P-d>=P-(2a-2)`.
- Pigeonhole corollary: if `phi(N)/2>2a-2`, at least one such coefficient-one relation is forced.
- Evidence fixture: for `N=9`, `w=18`, the saturated tuple `(1,2,3,4,5,7,8,18)` has three opposite pairs but only two relation-free quotient values.
- Limitation: H39 needs `n-2` independent rows; the lower bound can still be zero at large height and does not include the nonunit kernel classes.
- Verdict: proved.
- Verification: `opposite_unit_sum_relation_basis`, direct pair-sum and four-term fixtures, an exact rank regression, and the low-height pigeonhole regression.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H57 — All-runner boundary events form a complete witness set

- Mode: proved exact networking-style event reduction
- Statement: at width `1/N`, if a lonely time exists then one exists among `t=(j+/-1/N)/v_i` over every runner and every period index. The feasible set is closed and not the whole circle, so a component boundary is a runner event.
- Contrast with H52: `(1,3,4,5,12)` has no witness on the largest runner's boundaries, but the all-runner event set finds one.
- Limitation: the event set has size `2 sum_i v_i`; completeness for each fixed tuple is not a height-independent proof.
- Verdict: proved.
- Verification: `lrc_boundary_event_witness` and exact boundary regressions.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H58 — Exact pairwise boundary-event capacity sieve

- Mode: proved incidence obstruction on the H57 event set
- Statement: for one sign of runner `v`'s boundary events, runner `u` blocks exactly `g * #{z:-V<z<V, z=U mod N}`, where `g=gcd(u,v)`, `U=u/g`, and `V=v/g`. Hence a counterexample requires the sum of these capacities over `u!=v` to be at least `v` for every `v`.
- Proof mechanism: after clearing denominators, blocked events correspond bijectively to integers `z=N(Uj-mV)+U` in the displayed interval; each reduced event repeats `g` times. The opposite sign has the same count by negation.
- Consequence: any capacity deficit identifies a runner with an unblocked boundary event and therefore an LRC witness. A coarser closed bound replaces the exact count by `g ceil((2V-1)/N)`.
- Reach: the exact sieve certifies 13,279 of 16,648 primitive three-speed tuples through height 50, plus large fractions of sampled four- through six-speed domains. It does not eliminate the known sharp divisible fixtures.
- Verdict: proved necessary condition and sufficient witness test; not the general theorem.
- Verification: `boundary_event_block_count`, exhaustive direct-event equality tests, and `boundary_capacity_witness_runner`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H59 — Odd boundary-event moments give a certified hierarchy

- Mode: proved overlap-aware escalation of H58
- Statement: for blocker event sets `A_u` on one side of runner `v`, let `S_r` sum all `r`-fold intersection sizes. Every odd Bonferroni truncation `B_{2h+1}=S_1-S_2+...+S_{2h+1}` upper-bounds the covered events. If `B_{2h+1}<v`, an unblocked boundary event is an LRC witness.
- Second-order waste bound: since an event has load at most `N-2`, its excess incidence is at least `2 binom(load,2)/(N-2)`. Hence `|union A_u|<=S_1-ceil(2S_2/(N-2))`.
- Reach: order three certifies `(1,3,4,5,18)`, all 15,246 primitive five-speed tuples through height 20, and 7,974/7,980 six-speed tuples through height 16. It also closes sampled H58 survivors through ten speeds.
- Boundary: explicit eleven- and twelve-speed samples survive order three and require higher odd orders, so order three is not the general theorem.
- Consequence: the continuous adversarial problem is now an exact load-moment question on arithmetic event sets. A uniform order or structural high-load bound would prove the conjecture.
- Verdict: proved hierarchy; uniform closing order open.
- Verification: `boundary_event_blocked_centers`, `boundary_bonferroni_witness_runner`, sharp and high-dimensional survivor regressions.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H60 — A repeated four-blocker cluster forces a bounded relation

- Mode: attempted bridge from high event load to H39
- Hypothesis: if four runners jointly block at least three boundary events of another runner, those five speeds have a nonzero coefficient-two relation.
- Kill: blockers `(113,118,178,282)` jointly hit events `{221,224,276}` of boundary runner `281`, but `(113,118,178,281,282)` has coefficient-two relation rank zero.
- Lesson: repeated congestion support alone discards the signed error and event-phase data needed for algebraic structure. A valid bridge must compare several clusters or retain their exact indices.
- Verdict: killed.
- Verification: exact `boundary_event_blocked_centers` intersection and `bounded_relation_rank` regression.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H61 — Signed errors compress repeated events into sumset growth

- Mode: proved phase-preserving replacement for H60
- Compression: if a blocker `u` hits two events `j_1,j_2` of boundary runner `v`, their centered errors differ by `Nd_u`, where `d_u=u(j_2-j_1) mod v` has centered magnitude below `2v/N`. Thus every common blocker is bad at time `(j_2-j_1)/v` with doubled width, while `v` is reset.
- Multiscale form: for a common event set `J`, every element of `rJ-rJ` makes every blocker bad at width `2r/N`.
- Stabilizer lemma: if `r<=N/6`, the stabilizer order of `rJ-rJ` divides `gcd(v, all blockers)`. Otherwise its phase subgroup contains a point at distance at least `1/3`, contradicting the compressed strict width.
- Kneser corollary: for a gcd-one cluster the stabilizer is trivial, so `|rJ-rJ|>=2r|J|-(2r-1)`.
- Consequence: high event moments force either additive growth in a wider simultaneous bad set or a shared gcd cluster. This retains the phase information H60 discarded.
- Limitation: a uniform upper bound on the wider simultaneous bad set is still missing.
- Verdict: proved.
- Verification: `boundary_event_signed_error`, `compressed_boundary_event_error`, `common_boundary_event_sum_difference_set`, and exact multiscale regressions.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H62 — Small lifts, backward projection, and a polynomial step prove `k<=12`

- Mode: current-literature retrieval and semantic audit
- Source theorem: Sungkawichai--Trakulthongchai, arXiv:2604.23906, Theorem 1.3, states `LRC(k)` for every `k<=12` relative speeds, or at most thirteen physical runners.
- Computational mechanism: repeatedly lift improper residue tuples by small multipliers, delete proper lifts, and project survivors back modulo `p`. Projection preserves every residue class that is improper at all finite levels while collapsing many transient lifted branches.
- Fixed-case outcomes: `2`- and `3`-lifts empty the `k=11` survivors. For `k=10,12`, repeated `2`-lifts leave only equivalents of `(1,2,...,k)`.
- Analytic mechanism: when `k+1` and `p>k(k+1)` are odd primes, a degree-`k` polynomial identity over `Z/(k+1)` and a discontinuity-gap transfer prove eventual properness of that canonical class.
- Verification grade: primary-source semantic match. The accompanying repository and result logs were inspected, but the `k=10,11,12` computations were not independently rerun here; this is not certificate grade.
- Consequence: the current bounded frontier is `k=13` relative speeds (fourteen physical runners). The general non-prime question is whether small lift/project operators collapse arbitrary survivor sets uniformly to finitely many structured tight classes.
- Prime boundary: the paper's prime-field polynomial proposition is accepted as a proved input. Per the user's instruction, no unresolved prime-generalization branch is pursued.
- Verdict: retrieved known theorem; not a new result of this inquiry.
- Artifact: `artifacts/2026-lrc12-literature-audit.md`.

### H63 — Recursively dismount local handoffs or expose a rigid core

- Mode: algorithmic transfer from temporal-spanner dismountability
- Translation: regard each runner's periodic bad intervals as a temporal stream and the singleton-owner word as the ordered handoff trace of a work-conserving cyclic server. A runner is locally dismountable when a coefficient-two relation of support at most four absorbs its first handoff using its predecessor, the two initial seeds, and owners in the intervening segment.
- Hypothesis: recursive local dismounting either removes all but two runners, proving the rank target H39, or stalls on a core whose entry and exit extrema form two matchings and whose handoff labels have shifted-matching structure. The latter should feed the reset/factor branches H51--H56 rather than require arbitrary further casework.
- Source analogy: Baligacs's 2026 temporal-clique proof recursively dismounts locally reducible vertices; a nondismountable instance reduces to an extremally matched bi-clique, where short cut-crossing paths versus extended stars cover a constant fraction before recursion.
- Exact trial: all 55 completed first-band survivors through nine speeds are fully dismounted by the existing H47 certificates: 229 local rows, coefficient bound two, support at most four. The same certificates pass at the exact first-band edge. The wider tuple `(1,2,3,12)` at width `25/104` has every singleton owner but leaves speed `1` unresolved in the best rotation `(3,12,1,2)`, so the band restriction is load-bearing.
- Kill condition: a strict primitive first-band survivor whose local peeling stalls and whose residual event core has neither the two-matching extremal structure nor a reset/factor reduction.
- Caution: temporal reachability is not a theorem about circle-window coverage. Only the proof architecture transfers; every dismount or core claim still needs an exact arithmetic proof.
- Verdict: refined. The reducible branch is now an exact diagnostic, but “extremally matched” has not yet been defined arithmetically and therefore supplies no theorem beyond H47. Retain the dismount-or-core decomposition; withdraw any implication that temporal-spanner structure automatically classifies the core.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H64 — The residual core exactly measures the missing relation rank

- Mode: proved diagnostic invariant under lower-runner induction
- Definition: for each cyclic rotation of the singleton-owner word, retain every H47 segment-local row that exists and record the unresolved later first owners. Choose a rotation minimizing that residual core `C`.
- Rank theorem: the retained rows are triangular in first-occurrence order. Each has a distinct latest owner with nonzero coefficient and no later owner in its support. Hence they are independent and `rank R_2(v) >= n-2-|C|`.
- Singleton theorem: assuming LRC for `n-1` speeds, a full `n`-speed cover at any width `delta<1/n` gives every runner an open singleton window, with uniform margin `1/n-delta`. In particular, at the first-band edge `2/(2n+1)` the margin is `1/[n(2n+1)]`; a hypothetical counterexample cannot create a fake core merely by omitting an owner.
- Exact trials: the five primitive three-speed first-band survivors through height `100` and the six four-speed survivors through height `50` have empty core at the band edge. The full earlier 55-tuple corpus also has empty core. At the wider width `25/104`, `(1,2,3,12)` has `|C|=1`, confirming that core size becomes nontrivial outside the first band.
- Consequence: H47 is now equivalent to the operational statement `C=empty`; a bound `|C|<=c` would still reduce any counterexample to ambient dimension at most `c+2`.
- Verdict: proved; uniform core emptiness remains H47.
- Verification: `local_handoff_residual_core`, `inductive_private_window_margin_at_width`, and exact regressions.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H65 — Rerooting at a residual owner always repairs local peeling

- Mode: temporal-spanner pivot analogue, tested exactly
- Hypothesis: if H47 leaves a residual owner, promote that owner and one adjacent singleton owner to the two seeds; coefficient-two appendability then eliminates every remaining speed.
- Positive trials: the stalled four-speed tuple `(1,2,3,12)` is repaired by seeds `(1,12)`, followed by `2*1=2` and `1+2=3`. Four local-core examples in exact subcritical scans through five speeds all repair this way; structured families through seven speeds also pass.
- Kill: at width `97/784`, the tuple `(1,4,5,6,7,11,13,48)` has maximum loneliness `6/49`, residual core `{1}`, and no adjacent-core pivot certificate. A different handoff pair still gives full appendability and the coefficient-two relation rank is `7`.
- Stronger separation: `(1,4,5,6,7,11,13,96)` has maximum loneliness `12/97`, residual core `{7}`, no core pivot, and no handoff-selected two-seed appendability at all, while its coefficient-two rank remains exactly `6=n-2`.
- Sharp family audit: for `(1,4,5,6,7,11,13,8r)`, exact checks for `2<=r<=15` give maximum loneliness `r/(8r+1)`. At `r=2` this is the first-band edge `2/17`; the handoff hierarchy succeeds. Failures begin only above the edge, while the rank target survives throughout.
- Lesson: rerooting is a useful repair heuristic but not a uniform theorem. Outside the first band, the scheduling-selected order can lose relations that remain present in the full circuit lattice. The invariant to prove is rank, not success of one owner-selection algorithm.
- Verdict: killed in its broad form. Its strict first-band restriction adds nothing beyond H47 because every tested first-band core is empty.
- Verification: `handoff_core_pivot_certificate` and the `r=2,6,12` hierarchy regressions.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H66 — Back-substitution isolates the exact global circuit quotient

- Mode: proved linear-algebraic reduction
- Construction: order the H64 local rows by their distinct latest first owner and back-substitute them from every coefficient-two circuit. Each canonical residual is supported only on the two initial seeds and the unresolved core `C`.
- Exact identity: the local rows have rank `n-2-|C|`. If `Q` is the residual circuit space, then

  ```text
  dim Q = rank R_2(v) - (n-2-|C|).
  ```

  Therefore H39 is equivalent to `dim Q>=|C|`. This removes every scheduling-order choice from the repair step.
- Example: for `(1,4,5,6,7,11,13,96)` the local rank is `5`, `C={7}`, and `Q` is one-dimensional. Its normalized residual is `1-(1/7)7=0`, obtained by combining bounded original circuits even though the quotient coefficient denominator is `7`.
- Stronger example: `(1,2,3,12)` has local rank `1`, one residual owner, and a two-dimensional quotient, recovering full relation rank `3`.
- Limitation: this is an exact reformulation, not yet a lower bound on `dim Q`. Quotient coefficients may grow during elimination even though every original circuit has coefficients at most two.
- Verdict: proved.
- Verification: `handoff_circuit_quotient_basis`, support/rank identities, and scan receipt columns `band_edge_core_size` and `circuit_quotient_rank`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H67 — A subcritical handoff cover has at most one residual owner

- Mode: weakened, operational successor to H47
- Hypothesis: under lower-runner induction, every strict primitive first-band cover has `|C|<=1` for the H64 best cyclic rotation.
- Why useful: H64 then gives coefficient-two rank at least `n-3`, and H66 reduces every missing repair to a three-coordinate quotient. This does not itself prove H39, but replaces an unbounded adversarial core by one scalar circuit obligation.
- Exact evidence: all 55 completed first-band survivors have `C=empty`. At widths just below the lower-dimensional threshold, a complete five-speed height-`30` scan found 24 strict covers with core histogram `{0:16,1:8}`; a six-speed height-`22` scan found 22 covers, all with empty core. Three structured two-outlier scans found 17, 11, and 9 eligible covers through seven speeds, again with no core larger than one. Extended tail searches through height `300` found 61 eligible extensions of `(1,2,3)` and 64 of `(1,3,4)`; height-`250` searches found 41 extensions of `(1,2,3,4)` and 43 of `(1,3,4,5)`. Every core still had size at most one. The dilation family in H65 has core size at most one for `2<=r<=15`.
- Kill condition: a subcritical cover with two unresolved owners in every cyclic rotation. A strict first-band example kills the stated hypothesis; a wider example only kills the exploratory broad form.
- Verdict: selected for testing; no proof yet.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H68 — The canonical factor-extension family has an exact safe value

- Mode: direct near-packing argument, answering the factor-chain branch
- Statement: for `n>=3` and `r>=2`,

  ```text
  ML(1,2,...,n-1,nr) = r/(nr+1).
  ```

- Lower bound: at `t=r/(nr+1)`, every `k=1,...,n-1` has distance at least `r/(nr+1)`, while `nr` has exactly that distance because `nr=-1 mod nr+1`.
- Replacement-arc lemma: if `delta>1/(n+1)` and `||kt||>=delta` for `k=1,...,n-1`, the `n` half-open arcs of length `delta` beginning at `0,t,...,(n-1)t` are disjoint. Delete the first arc. Both it and its translate beginning at `nt` fit into the complement of the remaining `n-1` common arcs, whose total length is `delta+E` with `E=1-n delta<delta`. Only one complement component can hold an interval of length `delta`, so both replacement arcs lie there and `||nt||<=E`.
- Upper bound: set `delta=r/(nr+1)`, for which `E=1/(nr+1)`. The lemma gives `||nrt||<=r||nt||<=rE=delta`; hence either a canonical speed or the factor extension is bad at every time.
- Rank consequence: the relations `2*1-2=0` and `1+(k-1)-k=0` for `3<=k<=n-1` are `n-2` independent coefficient-two rows. Thus the family already satisfies H39 even as its values accumulate upward at `1/n`.
- Consequence: the principal adversarial “factor chain plus one reset runner” is completely safe and explains the one-owner cores dominating the subcritical scans. Any H67 counterexample needs at least two genuinely noncanonical escaping directions.
- Verdict: proved.
- Verification: exact critical-time and relation-rank regressions for `3<=n<=8` and several `r`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H69 — Strict first-band tuples have coefficient-one rank at least `n-2`

- Mode: stronger order-independent successor to H39, suggested by H41
- Hypothesis: if `ML(v)<2/(2n+1)`, then the relations in `{-1,0,1}^n` have rational rank at least `n-2`.
- Why sufficient: coefficient-one relations are coefficient-two relations, so H69 immediately implies H39. A hypothetical minimal LRC counterexample lies strictly below `1/(n+1)<2/(2n+1)` and satisfies the antecedent.
- Exact audit: all 14 strict tuples in the completed 55-tuple first-band corpus through nine speeds have coefficient-one rank at least `n-2`; there are zero strict failures.
- Boundary separation: the closed-band strengthening is false. `(1,2,6)`, `(1,2,3,8)`, and `(1,3,4,5,18)` have `ML=2/(2n+1)` and coefficient-one rank exactly `n-3`. No other completed survivor fails. Thus one unit-relation dimension appears precisely when moving into the strict interior in the observed spectrum.
- Analytic bridge: H41 already proves that every hypothetical counterexample with `n>=18` has at least one coefficient-one relation. H69 asks for the rank form of that Riesz phenomenon, not an iteration of a coefficient-two scheduling algorithm.
- Kill condition: a strict primitive first-band tuple with coefficient-one relation rank below `n-2`.
- Verdict: selected for testing; unproved.
- Verification: scan receipt columns `coefficient_one_rank` and `strict_first_band`, plus exact boundary regressions.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H70 — Low coefficient-one rank forces a reciprocal Riesz load floor

- Mode: quantitative load-balancing route to the large-`n` part of H69, killed by separated dense blocks
- Hypothesis: if `rank R_1(v)<=n-3`, then

  ```text
  riesz_cover_ratio(v)
    = CT prod_i(1-cos(v_i x))
      / sum_j CT prod_{i!=j}(1-cos(v_i x))
    >= 1/(3n).
  ```

- Why useful: a width-`delta` bad-arc cover forces this ratio to be at most `1-cos(2*pi*delta)`. At the first-band width `delta=2/(2n+1)`, `1-cos x<=x^2/2` and `pi^2<10` make the upper bound smaller than `1/(3n)` for every `n>=59`. Thus H70 would prove H69 for all `n>=59`, leaving only a finite range and the separate strict-margin issue.
- Networking interpretation: the deletion integrals are the loads assigned to the possible blocking runners. The normalized quotient measures how much simultaneous slack survives after adversarial correlations. Relation rank is the dependency budget; H70 says three unresolved directions prevent that load from collapsing below reciprocal scale.
- Exact exhaustive trials: among primitive tuples with `rank R_1<=n-3`, the minima of `n*riesz_cover_ratio` were `1`, `4/5`, `5/8`, and `9/16` for scans `(n,height)=(3,40),(4,28),(5,18),(6,13)`. The minimizing tuples were `(1,2,4)`, `(1,2,3,7)`, `(1,2,3,5,12)`, and `(1,6,10,11,12,13)`.
- Hostile structured trials: Fibonacci dependency chains through `n=10` reached a minimum `90/167>1/2`; tribonacci and cumulative-sum chains stayed above one. Random three-seed subset-sum constructions reached `20/49` at `n=8` and `27/62` at `n=9`, still above `1/3`.
- Exact kill: let `B=(1,2,...,17)`. Direct convolution gives `rho(B)=139/7285`, hence `17 rho(B)=2363/7285<1/3`. Choose `M=1009` and concatenate `B`, `MB`, and `M^2B`. Since `M^2>(M+1)sum(B)`, every coefficient-one zero sum splits blockwise. Each block's coefficient-one relations span its `16`-dimensional rational kernel, so the 51-speed union has rank `48=n-3`. Constant terms and deletion sums factor blockwise, giving `rho(union)=rho(B)/3` and therefore `n rho(union)=17 rho(B)<1/3`.
- Domain separation: this killer is not a first-band tuple. Because `M=1 mod 18`, time `t=1/18` gives all three blocks the same phases as `B`, so its maximum loneliness is at least `1/18>2/103`. The failed inequality discarded precisely the near-cover coupling that H69 needs.
- Verdict: killed. Rank alone is not a sufficient dependency budget. Any spectral successor must retain first-band geometry or an invariant excluding independent dense circuit blocks; merely improving the constant cannot work, since longer consecutive blocks drive the normalized load still lower.
- Verification: exact Riesz ratio regressions and scan receipt columns `riesz_cover_ratio` and `normalized_riesz_ratio`.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H71 — Geometrically scaled canonical blocks share an LRC fixed point

- Mode: proved non-prime mixed-factor family, extracted from the H70 killer audit
- Statement: let `m,r>=2` and `M>=m+2`, and concatenate the `r` disjoint blocks

  ```text
  B_m, M B_m, ..., M^(r-1) B_m,       B_m=(1,2,...,m).
  ```

  This `n=rm` speed tuple satisfies the full LRC bound.
- Explicit witness: put `q=M-1`, `a=floor(q/(m+1))`, and `t=a/q`. Since `(M^j-1)/(M-1)` is integral, `M^j t=t mod 1` for every block. Also `0<t<=1/(m+1)`, so among `k=1,...,m` the minimum of `||kt||` is exactly `t`.
- Bound: write `q=(m+1)a+s` with `0<=s<=m`. Because `a>=1` and `r>=2`,

  ```text
  a(rm+1)-q = a(r-1)m-s >= m-s >= 0.
  ```

  Hence `t=a/q>=1/(rm+1)=1/(n+1)`.
- Adversarial relevance: for `m>=5` and sufficiently separated scales, the coefficient-one relations split blockwise and have rank `r(m-1)=n-r`. In particular, three blocks realize the exact `n-3` rank deficiency targeted by H69/H70, yet phase synchronization proves them safe. This removes an infinite mixed factor/nonfactor family rather than weakening the rank conjecture.
- Exact falsification audit before the proof: for `3<=m<=28` and `sum(B_m)<M<=5 sum(B_m)+1`, the first-band grid admitted many false positives but exact critical-time replay admitted none. The fixed-point proof closes every remaining scale at once and explains those rejections.
- Verdict: proved.
- Verification: `geometric_canonical_block_witness`, exact phase/distinctness/LRC-distance regressions, and `scan_geometric_blocks.py` for the pre-proof falsification receipt.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

### H72 — Arbitrary geometric multiplier blocks eventually synchronize

- Mode: proved mixed factor/nonfactor extension of H71
- Setup: let `A_0,...,A_(r-1)` be nonempty finite sets of distinct positive multipliers, let `n=sum_j |A_j|`, and put `m=max union_j A_j`. For an integer scale `M>m`, take the distinct speeds

  ```text
  union_j M^j A_j.
  ```

- Exact fixed-phase certificate: if

  ```text
  ceil((M-1)/(n+1)) <= floor((M-1)/(m+1)),
  ```

  choose any integer `a` in that interval and set `t=a/(M-1)`. Then `M^j t=t mod 1`; moreover `1/(n+1)<=t<=1/(m+1)`, so every multiplier `1<=k<=m` satisfies `||kt||>=t`. Hence every runner is at least `1/(n+1)` lonely.
- Uniform large-scale consequence: when `n>m`, the interval has length at least one—and therefore contains an integer—as soon as

  ```text
  M >= 1 + ceil((m+1)(n+1)/(n-m)).
  ```

  Thus every fixed collection of arbitrary multiplier blocks is safe at all sufficiently separated geometric scales. Unequal canonical prefixes are the special case `A_j={1,...,m_j}`.
- Sharp method boundary: below the uniform scale the integer interval may still be nonempty; `(B_5,6B_2)` is the smallest recorded miss for this certificate, while `(B_5,7B_2)` succeeds at `t=1/6`. If `n<=m`, the low-phase safe interval itself is empty, though another phase may still prove the tuple safe.
- Consequence for the user's case split: factor groups need not have equal shapes. Once their total runner count exceeds the largest normalized within-group multiplier and the inter-group scale is large enough, a single reset fixed point synchronizes every group; no induction over group handoffs is needed.
- Verdict: proved certificate and eventual-family theorem.
- Verification: `geometric_multiplier_block_witness`, `geometric_multiplier_block_scale_bound`, unequal-prefix wrappers, and exact positive/miss/boundary regressions.
- Artifact: `artifacts/first-spectral-band-connectivity.md`.

## What the graph established

1. The elementary measure branch recovers `1/(2n)` and dies by an exact factor-two deficit.
2. The failure generates a concrete need: control overlap, not individual bad-set size.
3. The tempting shifted generalization is false; common-phase arithmetic is therefore load-bearing.
4. A generic covering proof cannot work alone if it forgets that arithmetic.
5. The strongest surviving branch is a modular set-cover certificate that converts coverage into divisibility.
6. The printed set-cover threshold fails differential replay; `1/(k+1)` matches the lemma and published fixtures.
7. At `k=8`, the corrected finite predicate is SAT through `p=43`; the local H21 profile split closed the first fourteen target primes from `47` through `107`.
8. Independent UNSAT certification works on the calibration case but exceeded the interactive budget at the `k=8` boundary.
9. Constraint ablation isolates the boundary mechanism: coverage remains possible, but only with too many multiples of `3` to satisfy the minimal-counterexample gcd condition.
10. The relaxed SAT branch is explained by the canonical Dirichlet cover `{9,18,...,72}`; admissibility demands at least two exchanges out of this divisible lattice.
11. Exact single-speed coverage counts are now proved, but their capacity bound dies with 175 excess incidences at the first boundary.
12. Pairwise gcd data and the first two incidence moments are provably insufficient; they admit abstract unions larger than the universe and collide on actual selections with different union sizes.
13. The exact Fourier transform is a rotated Dirichlet kernel; the obvious order-three character is rigorously too weak.
14. Even an adaptive single Fourier character is too compressed: a concrete selection satisfies every character bound with factor-of-four slack.
15. Even arbitrary nonnegative test-time weights fail numerically: the minimax additive-incidence value at `p=47` is `40/23`, pending an exact dual replay.
16. The first boundary is tight. A legal eight-speed selection covers `210/211` test times, and unit symmetry normalizes its sole gap to `1`.
17. Normalized one-gap witnesses are isolated under one-speed exchanges, but their divisibility profiles differ.
18. Modulo-`p` fibers give an exact new representation: unit speeds are oriented two-point edges on `Z/9`, `g=3` speeds are three-point phase classes, and `g=9` speeds are all-or-nothing.
19. Fiber phases plus exact completion eliminate every possible unit-count profile at `k=8,p=47`; the first two branches are independently certified and the remaining four replay in a bounded-memory verifier.
20. This finite result proves one prime divisor, `47`, for any hypothetical nine-runner counterexample. It does not alone prove the nine-runner case.
21. The local 37-prime H21 route was overtaken by current literature before completion.
22. Trakulthongchai's published 39-prime lifting sieve was replayed in full: every final improper set is empty and the forced divisor product exceeds the counterexample bound by a factor greater than 230. The known nine-runner theorem is thereby reconstructed, not newly discovered.
23. The proposed universal grid-witness Conjecture 7.1 is false as written. The unit family `(1,3r)` at denominator `6r+1` is non-tight but misses every grid witness. Multiscale hypotheses must retain height or integer-realizability information.
24. Height dependence repairs the quantifier failure: every fixed non-tight tuple of height `M` has witnesses on every grid with denominator greater than `(k+1)M^2`.
25. The bounded-relation proposal is not operational as stated: its weak conclusion is automatic after finite checking, while the undefined “descent-compatible” qualifier hides the missing theorem.
26. A single critical-time active graph cannot supply that theorem because its edge equations are vertex differences and every cycle telescopes; known tight tuples also lack the proposed connected graph.
27. A direct interval-measure argument proves a multi-fast-runner lemma: fewer than half the runners cannot lie above a sufficiently large multiplicative speed gap in a counterexample.
28. A triangular-bump Fourier argument proves the weak bounded-relation theorem explicitly: every bad or tight `n`-tuple lies on one of finitely many bounded-normal rational hyperplanes. The remaining burden is relative-subtorus descent, not relation existence.
29. Uniform connectedness fails across the whole near-tight interval by `(1,2,3s)`, but coefficient-two connectivity survives every tested tuple in the first spectral band `ML<=2/(2n+1)`. This is now the sharp non-prime hypothesis to attack.
30. Quantitative Kronecker plus induction proves a coarse height—and hence coarse connected-relation—bound throughout the first band.
31. Every scanned first-band tuple admits a positive triangular coefficient-two relation tree, making the desired sign pattern operational.
32. Positive generation from two earlier seeds is false at six speeds; `(2,5,6,8,10,11)` is the first exact obstruction.
33. The invariant surviving that kill is relation rank: coefficient-two relations span rank at least `n-2` on all 55 scanned survivors, reducing the speed family to at most two parameters.
34. Full bounded-relation rank is false: `(3,4,7,11)` sharply requires a two-dimensional ambient subtorus.
35. Exact rational cell optimization gives that sharp pattern ambient loneliness `1/4`, a strict `1/20` margin; flat-torus geodesic covering then reduces the pattern to finitely many parameter pairs.
36. Giri--Kravitz Lemma 3.3 makes the strict ambient margin automatic under induction: every proper two-dimensional ambient torus has loneliness at least `1/n`.
37. Independently, all 123 admissible four-coordinate coefficient-two symmetry classes were classified exactly; their minimum ambient loneliness is `1/4`.
38. The published linearly-exponential finite-checking bound reduces the three-speed counterexample domain to sum at most `36`; exhaustive exact replay proves the counterexample-relevant rank implication there.
39. Fan--Sun removes every four-speed first-band tuple having a pairwise gcd at least `3`; any hypothetical four-speed counterexample therefore has sum at most `1000` and all pairwise gcds at most `2`.
40. The broader H33 quantifier and the counterexample-only H39 quantifier are now separated. The published sum bound supports H39, not all of H33.
41. A complete exact audit of `1,705,044,764` four-speed tuples proves H39 for `n=4`: only six first-band survivors remain and all have coefficient-two rank `2`.
42. A dissociated Riesz product proves uniformly that every hypothetical counterexample with `n>=18` has a coefficient-one subset-sum relation. This sharply improves H28's first relation but does not yet provide rank `n-2`.
43. A two-element inclusion-maximal coefficient-two dissociated seed would imply H39 by independent star relations. The first 42 scanned survivors pass, but an eight-speed first-band tuple kills the broad H42 form by requiring three direct seeds.
44. Exact Riesz constant terms kill blind iteration: the circuit `(1,2,3)` lowers the normalized cover ratio from `1/3` to `1/4`, and the unmodified product excludes none of the 42 scanned survivors.
45. Two-seed bounded appendability repairs H42's chain defect while retaining the rank implication. All 55 scanned survivors through nine speeds pass, including three direct-H42 failures at eight and nine speeds.
46. Exact sliding-window sweeps form a cyclic first-occurrence order from singleton owners. Some rotation is a complete bounded elimination order for all 55 survivors; the original 49 also pass three slack full-cover widths.
47. Lower-runner induction proves that every runner in a minimal counterexample owns an open singleton-load window; consequently the handoff transition graph is connected.
48. Every one of 229 tested elimination steps localizes to the preceding new owner plus at most two earlier owners with coefficient bound two. Both coefficient two and support four are sharp in the scan.
49. Moving the sweep to the exact band edge labels every endpoint by `q m+/-2`. All 55 retain segment-local elimination there, while all 14 strict survivors have full relation rank `n-1`; the rank-`n-2` obstructions live exactly on the boundary.
50. Every strict primitive survivor avoids multiples of `n+1`. The resulting H49 barrier would prove the full conjecture after gcd normalization; its unnormalized form is killed by `(4,8,12)`, while the primitive form survives 2,875,130 targeted tuples and is sharp on the band boundary.
51. Exact reset counting proves LRC when the largest speed is an `n+1` multiple and every slower speed has gcd at most two with `n+1`. Any remaining divisible-speed obstruction is genuinely mixed: the divisible runner is not largest or a gcd-at-least-three stratum is present.
52. The reset bad sets are now characterized for every gcd stratum: units block two indices and nonunits block multiplication kernels. Kernel overlap proves new mixed cases, while sharp fixtures fully cover the reset indices and saturate the unit residue classes.
53. Allowing every phase boundary of the largest divisible runner still does not give a complete witness set: `(1,3,4,5,12)` kills that extension. The next sweep must include slower-runner window events and their ownership handoffs.
54. A full reset block with a unique divisible largest speed needs every unit residue plus one proper kernel per prime divisor: exactly `phi(N)` blockers for prime `N`, or `phi(N)+omega(N)` for composite `N`. The runner count proves the subcase for prime `N` and `N=4`; `N=6` is tight.
55. Reset saturation does not localize the escape to the central cells: `(1,2,3,5,6)` kills that shortcut. The gap location depends on the actual quotient data above the residues.
56. At each unit grid point, however, the full sweep has a deterministic local skeleton: residue `k^{-1}` approaches from the left, residue `-k^{-1}` from the right, and the unique divisible runner lies between them. Full reset saturation forces every such two-sided handoff.
57. Pairing the forced opposite unit residues turns height into a finite quotient palette. The quotient classes supply coefficient-one relation rank at least `phi(N)/2-[2(w/N)-2]`; a positive value forces a relation of support at most four.
58. The complete networking-style schedule consists of every runner's target-boundary events, not merely those of the reset runner. Any feasible component has such an event on its boundary, yielding an exact fixed-tuple algorithm of size `2 sum v_i`.
59. Pairwise blocking of those events has an exact gcd-residue count. If the capacities aimed at either side of runner `v` sum below `v`, an explicit boundary witness exists; this sieve certifies most small three-speed tuples but leaves the sharp adversarial fixtures.
60. Odd Bonferroni moments of the blocker event sets form a certified hierarchy. Order three closes the sharp divisible fixtures and nearly every completed small scan, but higher-dimensional examples require higher order; a uniform order or high-load structure theorem would prove the general case.
61. Repeated four-way congestion does not automatically yield a coefficient-two relation: an explicit five-speed cluster co-blocks three events while having bounded-relation rank zero. Event indices or signed errors are load-bearing.
62. Signed errors restore that lost information. Equal-cardinality event sums compress to wider simultaneous bad phases; below scale `N/6`, Kneser gives linear sumset growth unless the boundary runner and every blocker share a nontrivial gcd.
63. The April 2026 lifting/projection and polynomial sieve proves `LRC(k)` through `k=12` relative speeds. Its backward-projection operator is the closest published analogue of H61's phase compression; the next bounded case is `k=13`, not nine.
64. Temporal-spanner dismountability suggests a precise recursion for the handoff branch: peel a locally certified runner, or classify the nondismountable residue as an extremally matched, shifted core. All 55 completed first-band survivors peel completely; a wider explicit tuple stalls, confirming that the first-band cutoff cannot be dropped.
65. Residual-core accounting makes that recursion exact without importing temporal reachability. If `C` owners remain unresolved, the local rows already have independent rank `n-2-|C|`; induction guarantees that every runner appears throughout the subcritical first-band sweep. Thus only genuine arithmetic row failures, not missing owners, can populate a hypothetical core.
66. Promoting a residual owner to a new handoff pivot repairs small stalls but fails at eight speeds. The family `(1,4,5,6,7,11,13,8r)` separates three levels above the sharp first-band edge: local peeling, handoff-selected appendability, and full coefficient-two rank. The first two eventually fail; the rank target survives.
67. Back-substitution removes the algorithm from the remaining question. Modulo the independent local rows, every bounded circuit is supported on the two seeds plus the residual core, and H39 is exactly the inequality `dim Q>=|C|` for that quotient circuit space.
68. No exact subcritical scan has produced two residual owners. The weakened H67 target `|C|<=1` would reduce any remaining repair to a three-coordinate quotient, but it does not by itself supply the last circuit.
69. A replacement-arc argument exactly disposes of the canonical factor-extension family: `ML(1,2,...,n-1,nr)=r/(nr+1)`, and the canonical chain already supplies rank `n-2`. These one-scale accumulation examples cannot obstruct the general conjecture.
70. Coefficient-one rank exhibits an even sharper boundary jump. Every strict survivor through nine speeds has rank at least `n-2`; the only three deficiencies have rank `n-3` and lie exactly at `ML=2/(2n+1)`. This upgrades the preferred invariant from coefficient-two handoff rank to a strict-interior unit-circuit hypothesis.
71. The rank-only Riesz load floor H70 is false, but its separated-block killer is itself harmless for a stronger reason. H71 synchronizes every geometric canonical block at the fixed phase `t=floor((M-1)/(m+1))/(M-1)` and proves the full LRC bound for any number of blocks.
72. H72 removes both equal-size and consecutive-block assumptions. Arbitrary multiplier blocks `A_j` synchronize at `a/(M-1)` whenever the exact fixed-phase grid meets `[1/(n+1),1/(m+1)]`; if `n>m`, this is automatic beyond the explicit scale `1+ceil((m+1)(n+1)/(n-m))`.

## Frontier

- Primary: for the general conjecture, seek a uniform small-lift/backward-projection collapse theorem suggested by H62. The target is eventual survivor structure for arbitrary `k`, not another fixed-prime computation; keep the proved prime-field canonical-class lemma as an input rather than opening a prime-generalization branch.
- Primary: prove the H63 nondismountable-core classification. First show that failure of every H47 local row forces the entry and exit extrema to be matchings; then test whether the induced cyclic label matrix is shifted-matching or falls into the composite reset/kernel branch. Do not import temporal reachability as a black box.
- Primary: use H64 rather than the informal temporal vocabulary. Bound the residual core `C` directly from the band-edge endpoint labels `q m+/-2`; empty `C` proves H39, while `|C|=1` reduces the remaining orbit to a three-dimensional ambient pattern. Any claimed matching structure must be stated as an exact condition on these labels.
- Primary: H65 shows that more elaborate rerooting rules are not the invariant. For the strict first band, compare the span of all coefficient-two circuits with the triangular handoff rows and prove that any residual core contributes an independent global circuit, regardless of whether a handoff order discovers it.
- Primary: prove or kill H67. Two failed owners must lie in disjoint first-occurrence segments of every best rotation; retain their band-edge endpoint labels and test whether subtracting the two failures yields either one H47 row or a nonzero quotient circuit in H66.
- Primary: lower-bound `dim Q` directly. For `|C|=1`, back-substitution leaves three integer speeds; seek a band-edge inequality that bounds their primitive determinant strongly enough to force one original coefficient-two circuit outside the local span.
- Primary: use H68 as the equality model for H67. If a one-core tuple approaches `1/n`, compare its `n` near-packed arcs with the canonical translate and quantify how any second unresolved direction consumes more than the total packing slack.
- Primary: prove or kill H69. Revisit H41 with the coefficient-one relation space quotiented out: the target is a lower bound on its rank, and the three exact boundary deficiencies are mandatory calibration cases for any strict-margin inequality.
- Killed route: H70 shows that coefficient-one codimension three alone does not force a reciprocal Riesz load floor; three separated consecutive blocks violate it. A successor must use the strict first-band cover to forbid or couple such dense relation blocks.
- Proved family: use H71 as the equality model for mixed factor groups. Any counterexample built from several geometric copies of a canonical block must break the common-scale fixed point—for example through unequal block shapes or non-geometric transitions—rather than merely separating the blocks.
- Proved extension: H72 also removes unequal and internally nonfactor block shapes at sufficiently large common scale. The live grouped-speed obstruction is now a small-scale transition or a sparse normalized block system with total count `n<=m`; test short-period points there before returning to handoff casework.
- Primary: replace H23 by a height-sensitive gap theorem, or formulate a lift-tree invariant that distinguishes fixed ordinary integers from spurious profinite survivor branches.
- Primary: combine H27's upper-gap constraints with finite-checking/volume bounds; seek a complementary lemma controlling cuts with at least half the runners above them.
- Primary: for the finite H28 normal vectors, formulate and test a concrete relative-subtorus descent; do not use the phrase “compatible sign pattern” without the transformation and preserved invariant.
- Primary: prove or kill H33. Combine a connected-cluster Fourier argument with the strict first-band gap to force bounded-relation codimension at least `n-2`.
- Primary: prove or kill H39 uniformly. It is the weaker statement actually sufficient for the general induction; H33 remains a useful stronger spectrum hypothesis.
- Primary: iterate H41 on relation clusters or a quotient without treating sums of unrelated relations as bridges; the target is `n-2` independent coefficient-two rows.
- Primary: formulate a relation-annihilating dual polynomial whose constant term ignores the known circuit lattice, and test it first on `(1,2,3)` and the 42 scan survivors.
- Primary: prove or kill H44. Analyze the nondismountable core left when coefficient-two appendability stalls; every crossing relation then contains at least two unresolved speeds.
- Primary: prove or kill H45. In a hypothetical full cover, analyze the overload blocks separating singleton-owner cells and derive either a zero-load escape or a bounded relation involving the successive owners.
- Primary: prove or kill H47. Analyze the entire handoff segment between successive first-time owners; select at most two old owners whose endpoint events reduce the segment's large labels to one coefficient-two relation.
- Primary: prove or kill H48 in its exact cell-chain form. Convert the divisible overlap determinants of the radius-two chains into one more independent coefficient-two speed relation at each rank-deficient stage.
- Primary: prove or kill H49. The fast divisible-runner case follows from induction and slack; in the moderate case, show that the `N` radius-one reset chains cannot coexist with primitive gcd one. Do not weaken this back to the endpoint-only modular cover.
- Primary: extend H51 beyond fully blocked reset unions using the radius-one interval handoff chains between reset candidates. H52 shows that varying the backoff only across the divisible runner's own phase boundaries is insufficient; slower-runner entry and exit events are load-bearing.
- Primary: in the equality and near-equality cases of H53, exploit the forced unit permutation and maximal-kernel residues to constrain those handoff events. Start with the tight `N=6` pattern rather than a prime-modulus branch.
- Primary: turn H55's opposite-residue divisibilities into a height-independent quantity. Candidate: compare the quotients `(v_r+v_{-r})/N` around the unit-grid cycle and seek a telescoping difference, rather than bounding each quotient separately.
- Primary: combine H56's unit-pair rank with relations forced by the maximal nonunit kernel classes. The target is to cover the remaining `n-2-[P-d]` rank without assuming that relation contraction preserves the reset obstruction.
- Primary: strengthen H58 from summed pair capacities to overlap-aware event ownership. Two blockers that hit the same `v` events waste capacity; quantify this by exact pairwise intersections before returning to a raw union bound.
- Primary: prove a uniform H59 truncation bound from the arithmetic form of the event sets, or show that survival to order `2h+1` forces an `h`-way gcd/relation cluster usable by H39. Do not assume order three remains sufficient past the tested range.
- Primary: after H60, retain signed event errors `e_u=u(Nj+1)-mNv` when comparing repeated clusters. Test relations among error differences across two event indices, not among the blocker speeds from one cluster alone.
- Primary: close H61 by upper-bounding the wider simultaneous bad set. Combine its aperiodic growth lower bound with an exact lattice count; in the periodic branch, feed the exposed common gcd back into minimal-counterexample induction.
- Primary: turn H39 plus the ambient margin into a uniform contradiction, using determinant bounds for coefficient-two nullspaces rather than enumerating patterns separately for every `n`.
- Secondary: if stronger auditability is desired, make the published sieve proof-producing or independently reimplement its three levels.
- Historical: the local H21 37-prime scan and p=47 branch certificates remain useful cross-checks, but no longer block the nine-runner theorem.
- Secondary: retain H19's one-gap exchange fixtures as boundary tests for any proposed H20 lemma.
- Secondary: extract a rational dual certificate for the H18 minimax value `40/23`; until then it remains a solver verdict.
- Secondary: extend the prime scan beyond `107`, with explicit timeouts recorded as `unknown`, never as `UNSAT`.
- Secondary: return to H2 only with an overlap inequality that explicitly depends on gcd/ratio data and therefore respects H4.
- Pruned: first-moment-only proofs, independently shifted formulations, and embeddings that retain only interval lengths.
