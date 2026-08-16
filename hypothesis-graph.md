# Lonely Runner Conjecture — hypothesis graph

Date: 2026-08-16  
Status: open inquiry; no proof or new mathematical result claimed  
Method: [The Proof Manual](/the-proof-manual) recorded using the replay contract from [The Hypothesis Graph](/the-hypothesis-graph-semantic-memory-methodeutics)

## Target

For distinct nonzero integer speeds `v_1, ..., v_n`, prove that there is a real `t` such that

```text
||t v_i|| >= 1/(n+1)  for every i,
```

where `||x||` is the distance from `x` to the nearest integer.

The general conjecture remains open. Integer speeds suffice after normalization. The strongest recent work also reduces every fixed `n` to a finite check, but the bound remains too large for a naive search.

Sources:

- Malikiosis, Santos, and Schymura, “Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants”: https://doi.org/10.1017/fms.2025.10107
- Perarnau and Serra, “The Lonely Runner Conjecture turns 60”: https://arxiv.org/abs/2409.20160
- Rosenfeld, “The lonely runner conjecture holds for eight runners”: https://arxiv.org/abs/2509.14111
- Blanco, Criado, and Santos, “Coloopless zonotopes and counterexamples to the Shifted Lonely Runner Conjecture”: https://arxiv.org/abs/2603.24784

## Graph

```text
H0  original LRC is open and correctly normalized
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
                                     WITNESSED for p=47,53,59,61,67 only
```

## Nodes

### H0 — The selected target is genuinely open

- Mode: induction from current literature
- Hypothesis: the general Lonely Runner Conjecture remains unresolved as of 2026-08-16, while fixed small cases and finite-checking reductions are known.
- Kill condition: a dated primary source proves or disproves the general formulation.
- Trial: inspect the current survey and the 2025–2026 papers listed under Sources; compare their theorem statements with the target above.
- Observed outcome: the survey calls the general problem open; subsequent papers prove bounded-runner cases, finite reduction, or disprove shifted variants, not the original general conjecture.
- Verdict: witnessed at artifact-replay grade.
- Credence: high, capped below certainty because literature status can change.

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

- Observed outcome: not run. This is the surviving frontier, not a result.
- Verdict: open.
- Credence: low.

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
  - The low-unit CNFs and parameterized high-unit verifier now close the first twelve target primes `47,53,59,61,67,71,73,79,83,89,97,101`. Exact branch counts are recorded in `artifacts/h21-prime-replay.tsv`.
  - Parameterization exposed and repaired a verifier-width bug: the first version used three 64-bit words for candidate coverer sets, sufficient through `p=61` but not beyond. All `p>=67` high-unit results were withdrawn and recomputed with the full 17-word width. Address/undefined-behavior sanitizers replay the corrected `p=67,u=4` branch without error.
  - A Claude/Sonnet review proposed a finite carry automaton on the nine-phase masks. The coarse relaxation is killed: locally covered edge configurations admit self-loops when carry choices are independent. A refinement would have to retain mechanical-word carry feasibility. It remains finite, but is deferred unless it avoids an open prime-distribution problem.
  - The same review recommended proof-producing SAT plus an independent formula regenerator. This matches the surviving certificate route; rerunning the same generator and solver is not counted as independent verification.

- Verdict: open frontier. Seven of 37 sufficient prime obstructions are closed at replay level; only the `p=47` low-unit branches currently have archived independent DRUP proofs.
- Credence: medium that the finite computations extend, low that brute force alone is the right final proof.

## What the graph established

1. The elementary measure branch recovers `1/(2n)` and dies by an exact factor-two deficit.
2. The failure generates a concrete need: control overlap, not individual bad-set size.
3. The tempting shifted generalization is false; common-phase arithmetic is therefore load-bearing.
4. A generic covering proof cannot work alone if it forgets that arithmetic.
5. The strongest surviving branch is a modular set-cover certificate that converts coverage into divisibility.
6. The printed set-cover threshold fails differential replay; `1/(k+1)` matches the lemma and published fixtures.
7. At `k=8`, the corrected finite predicate is SAT through `p=43` and UNSAT for the completed tests `p=47,53,59,61,67`.
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
21. Thirty-seven primes from `47` through `233` would cross the known product bound. H21 is the next falsifiable node. No general theorem or new Lonely Runner case was proved.

## Frontier

- Primary: parameterize H20 by `p` and prove or kill H21 across the 37-prime target, looking first for a symbolic large-`p` argument.
- Secondary: export independently checked certificates for the replay-grade `u=4,...,7` branches at `p=47`.
- Secondary: retain H19's one-gap exchange fixtures as boundary tests for any proposed H20 lemma.
- Secondary: extract a rational dual certificate for the H18 minimax value `40/23`; until then it remains a solver verdict.
- Secondary: extend the prime scan beyond `67`, with explicit timeouts recorded as `unknown`, never as `UNSAT`.
- Secondary: return to H2 only with an overlap inequality that explicitly depends on gcd/ratio data and therefore respects H4.
- Pruned: first-moment-only proofs, independently shifted formulations, and embeddings that retain only interval lengths.
