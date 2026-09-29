# STATUS — infinitely-many-primes  (COMPLETE)

Team: `math-team` (lead agent id `tcknimqkn`). Mode: natural-language.
Final update by team-lead after proof acceptance and publication.

## Result

**Independent-review PASS.** The existence of infinitely many primes is proved
by an accepted natural-language proof, verified by a fresh independent
`math-nl-verifier` in CERTIFICATION mode.

Acceptance basis: **LLM mathematical review**, not Lean kernel/compiler
verification. No formal machine-checked proof of this statement has been done.

## Original target

Prove that there are infinitely many primes. (Verbatim request in `request.md`.)

Primary reading: `P := { p ∈ ℕ : p prime }` is infinite. Working form:
`∀ n ∈ ℕ, ∃ p ∈ P, p > n`. The `∀∃` quantifier order is load-bearing; the
swapped form `∃p ∀n` is false and was never used.

## Deliverables

| Artifact | Path | SHA-256 |
|---|---|---|
| **Accepted proof** | `nl/generator/proof-v1.md` | `8a9cfda30bb3667442155db72547857cf6eac98f19687bf03bc236feb1260053` |
| **Published PDF** | `proof.pdf` | `b3e61e1dec1b1eab700a79aa566005e3962609a89ff421c558282ef634d26e77` |
| Published LaTeX wrapper | `proof.tex` | `bbe45156016b5059f05318c885575d279a91507dee51c27a1f2116b9c2c8ece0` |
| Proof review (PASS) | `nl/reviews/proof-review-v1.md` | `430b98d4365a885506c45e29f0e01eff584e58982342e9a73ce59bf5d54f7958` |
| Plan review (PASS) | `nl/reviews/plan-review-v1.md` | `26fa887b69a7243c2d6ee06a6414b52ea04239e3b90c21d76a8de2dff75a5783` |
| Target contract | `nl/sketcher/target-contract.md` | `1cc7975d9ef0888a58d85efc3ed75f1f48a1e69aa1fea2bdf114897b0ac53a83` |
| Lemma plan | `nl/sketcher/lemma-plan.md` | `e9d61a7cf1bccf4b1efa6fc5506d01dce400c59a86f9a44fb797dd984cce16d9` |
| Sketch obligations | `nl/sketcher/obligations.md` | `501c581d5d112b59fb335bf6ac71596ddf1e20c227a43fc9ab0f12e8856c0914` |
| Generator ledger | `nl/generator/obligations.md` | `81cc4c1d0063bae7ec882563666d142e33973ab4077a48142fd4df35b1062fb8` |
| Generator report | `nl/generator/report.md` | `735b8c3e5ca5fe24b07fb45e71efa74abf467e55c7f97a3a6973d96af7391e31` |

`proof.tex` is a mechanical publication: its body is a **byte-identical** copy of
`proof-v1.md` (verified: extracted body SHA-256 equals the source SHA-256), wrapped
in a provenance header. No TeX toolchain (pandoc/pdflatex/xelatex/tectonic) is
installed, so it was **not compiled** and no PDF exists. Compilation would be
typesetting only, not verification. `proof-v1.md` at the hash above remains
authoritative.

## Acceptance evidence

### 1. Plan-level review — PASS
Reviewer: fresh one-shot `math-nl-verifier`, CERTIFICATION. Hashes recomputed,
matched. Scope: (a) target fidelity and quantifier order, (b) decomposition
adequacy, (c) assembly implication and non-circularity. **Not** covered: the truth
of any lemma. Verdict: PASS.

### 2. Proof-level review — PASS
Reviewer: fresh one-shot `math-nl-verifier`, CERTIFICATION, no name/team, no prior
verdicts or author confidence supplied. Recomputed all seven hashes; all matched.
Independently re-derived E1–E11, AR1–AR5, L1–L6 and the assembly.

Key findings of the accepted review:
- The candidate establishes the exact original claim, in both the working `∀n∃p`
  form and the cardinality form, with no weakening or strengthening.
- The keystone (every `m ≥ 2` has a prime divisor) is proved by a well-ordering
  minimal-element argument and independently confirmed **non-circular**: no
  infinitude of primes, no FTA (existence or uniqueness), no Euclid's lemma, no
  iterative factor-extraction.
- The cardinality bridge is **proved, not assumed**: `L5` (finite ⟹ bounded) plus
  contrapositive `L5*` and converse `L5c`, giving `infinite ⟺ unbounded` for
  subsets of ℕ. This discharges ambiguity `A1` rather than assuming a reading.
- Case splits exhaustive; inductions correctly founded; subtraction formed only
  when `a > b`; the empty set is never given a maximum.
- The candidate explicitly corrects the baseline's imprecise `O-AR4` wording and
  does not inherit it.
- No obligation is claimed discharged that is in fact open.

## Remaining open obligations

- `O-DEF2` (`D2` divisor form ⟺ `D3` irreducible form) — left **OPEN** by the
  generator. The review confirmed this is genuinely **off the critical path**: the
  proof uses only `D2`, so the target is fully established without it. Optional
  completeness item, non-blocking.
- Non-blocking review notes carried forward: (i) calling `ℕ = {1,2,…}` a
  "commutative semiring" is terminologically loose (no additive identity in this
  truncation); none of the used clauses depends on the label. (ii) An `A1`
  non-escalation judgment call in the contract, explicitly flagged and defensible.
  (iii) A finite-set/cardinality precision note, immaterial since `P ≠ ∅`.

## Failed attempts

None. Both reviews returned PASS on first submission; no repair cycle was needed.

## Members and final state

| Name | Agent id | Role | Final state |
|---|---|---|---|
| `team-lead` | `tcknimqkn` | routing, records, publication | done; reported |
| `nl-sketcher` | `tbe8p1w6i` | target contract + lemma plan | idle, deliverable accepted |
| `nl-generator` | `to4k6hjem` | proof attempt | idle, deliverable accepted |

Team left **standing** (user did not request shutdown). Fresh reviewers were
one-shot calls and are not roster members.

## Scope statement for reuse

This result is an **independently reviewed natural-language proof**. It must not
be described as a Lean-certified theorem. If a machine-checked result is wanted,
the appropriate next step is the `formal` Lean workflow (see `HANDOFF.md`).
