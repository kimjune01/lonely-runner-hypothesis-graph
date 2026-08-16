# Nine-runner published-proof audit

Audit date: 2026-08-16

## Outcome

The Lonely Runner Conjecture holds for nine runners. This is a known result,
not a new theorem from this repository. Rosenfeld and Trakulthongchai announced
independent computer-assisted proofs in late 2025. This audit reconstructs the
logic of Trakulthongchai's proof and replays its complete finite computation.

## Deductive chain

For `k=8`, let `I(8,l,p)` denote the improper eight-speed tuples modulo `lp`:
after deleting any speed no common divisor with `lp` is allowed, and the tuple
has no sampled time at which every speed is at least `1/9` from an integer.

1. If `I(8,9,p)` is empty, the prime-divisor lemma implies that `p` divides
   the product of the eight relative speeds of every hypothetical nine-runner
   counterexample.
2. The lifting lemma gives
   `I(8,m,p) subset delta_m I(8,l,p)` whenever `l` divides `m`. The verifier
   therefore computes improper sets successively at levels `1`, `3`, and `9`.
3. For each of the 39 primes in `nine-runner-sieve-replay.tsv`, the final
   level-9 set has size zero.
4. Those primes are distinct and their exact product is

   ```text
   19570880530831227159611114469289180443865177656785618176063821114999202895619850591.
   ```

5. The Malikiosis--Santos--Schymura finite-checking corollary bounds the speed
   product of a minimal counterexample by

   ```text
   (36^7 / 8)^8
   = 84765698874878218361067180729674171436543015292348049288994557831877912686493696.
   ```

   The forced prime product is about `230.882` times larger. Hence a minimal
   counterexample cannot exist.

## Computational replay

Source repository:
<https://github.com/t-tanupat/nine-and-ten-lonely-runners>

Pinned commit and source digest:

```text
e17c415b807258806cd9192a17e9a51e20455a75
25a417a3bff84a48b458fe1a35d23460be0010b0bf79d36abd6a7369d200d0a5  lrc_for_nine_runners.cpp
```

The unmodified published command was run across all 39 target primes. The
local log had SHA-256 digest
`a5a2af76789f62076bf5d97c3a530ec53bcf8ee2e39520264e0291aac53cbabb`.
For every prime, all three intermediate cardinalities matched the published
receipt (whose digest is
`200b5a182defe027754875bc2191f2830cb1161f537ddb8c7574b1c885d30a08`),
and the final set `U=I(8,9,p)` was empty.

Replay from a checkout of that commit:

```bash
bash meta_lrc_nine.sh lrc_for_nine_runners.cpp 8 \
  47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 \
  137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 \
  223 227 229 233 239 241 results-local.txt
```

The local test `test_published_nine_runner_sieve_receipt_crosses_product_bound`
checks the durable 39-row receipt, primality, final emptiness, and the exact
integer product inequality.

## Verification grade and trust boundary

- The two lifting and prime-divisor lemmas were checked semantically against
  the paper's statements and proofs.
- The complete finite calculation was independently replayed from pinned
  source, and all intermediate counts were compared with the authors' receipt.
- The final arithmetic contradiction is checked with exact integers.
- The computation is still replay grade, not a proof-producing certificate:
  source/compiler defects shared with the published run remain possible.
- The theorem is independently supported by Rosenfeld's different 2025 proof,
  which uses prime powers and stronger divisibility conditions.

## Primary sources

- Tanupat Trakulthongchai, [*Nine and ten lonely runners*](https://arxiv.org/abs/2511.22427), v2, 2026.
- Matthieu Rosenfeld, [*The lonely runner conjecture holds for nine runners*](https://arxiv.org/abs/2512.01912), v2, 2026.
- Malikiosis, Santos, and Schymura, [*Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants*](https://doi.org/10.1017/fms.2025.10107), 2025.
