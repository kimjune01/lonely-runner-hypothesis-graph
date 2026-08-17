# 2026 bounded-case literature audit

Checked: 2026-08-17

## Current theorem boundary

Sungkawichai and Trakulthongchai state and prove, with computer assistance,
that `LRC(k)` holds for every `k<=12`, where `k` is the number of nonzero
relative speeds. In the physical-runner convention this covers at most
thirteen runners. The next bounded case is therefore `k=13`, or fourteen
physical runners. No dated primary source found in the August 17 search claims
that case or the general conjecture.

Primary source:

- Touch Sungkawichai and Tanupat Trakulthongchai, [*Eleven, twelve, and
  thirteen lonely runners*](https://arxiv.org/abs/2604.23906), v1, submitted
  2026-04-26.
- Accompanying code and result logs:
  <https://github.com/vzsky/13-lonely-runners> (last repository update observed
  2026-07-11).

This is a preprint-level, computer-assisted result. The present repository has
not independently replayed its `k=10,11,12` computations and therefore records
the theorem at primary-source semantic-match grade, not independent-replay or
certificate grade. The authors' repository says the polished `main` branch
was checked through `k=10`; the earlier `for-k-12` branch and supplied logs
were used for `k=11,12`.

## Proof architecture

For prime `p`, the paper defines `J(k,p)` as the residue tuples modulo `p` that
remain improper under every finite lift. If `J(k,p)` is empty, then `p` must
divide the product of the speeds in any minimal counterexample. Enough such
primes contradict the published finite-checking upper bound on that product.

The computational advance is a survivor-preserving pipeline:

1. compute the initial improper set modulo `p`;
2. lift by a small multiplier, especially `2`, and delete newly proper tuples;
3. project survivors back modulo `p`;
4. repeat with further small lifts;
5. exploit permutation, sign, and unit-scaling equivalences.

Backward projection cannot lose a genuinely never-proper residue tuple, but
it can collapse many lifted survivors before the next lift. For `k=11`, lifts
by `2` and `3` empty the survivor set. For `k=10,12`, repeated `2`-lifts reduce
the survivors to the equivalence class of `(1,2,...,k)`.

The canonical class is removed analytically when `k+1` and
`p>k(k+1)` are odd primes. The polynomial argument works over `Z/(k+1)`: a
degree-`k` product polynomial and a Fermat indicator polynomial agree at all
`k+1` field elements, forcing the required affine transform of every
nontrivial lift. A discontinuity-gap lemma then transfers the transform from
the `(k+1)` grid to the `p` grid.

## Implications for this inquiry

- The historical nine-runner target remains a valid replay artifact, but it is
  no longer the current bounded frontier.
- The general lifting question should be phrased in terms of eventual
  survivor sets `J(k,p)` and lift/project operators, not one universal grid
  denominator. The counterexample to the paper's Conjecture 7.1 does not kill
  eventual properness of each fixed residue class.
- The polynomial step is a proved prime-field lemma. Following the user's
  instruction, no unresolved prime-generalization branch is pursued here.
- The general non-prime target is to explain uniformly why repeated small
  lifts and projections collapse every non-tight survivor to finitely many
  structured tight classes, then dispose of those classes analytically.
- H57--H61 give a continuous analogue of the same pipeline: boundary events
  are the initial ansatz, odd moments prune survivors, and signed-error
  difference sets are a projection/compression operator. A useful synthesis
  must prove survivor preservation and uniform collapse rather than merely
  observe it in fixed dimensions.

