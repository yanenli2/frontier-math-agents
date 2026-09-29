# Independent statement-fidelity review v1

Mode: CERTIFICATION — exact new statement only.

**VERDICT: APPROVE.** No source-fidelity mismatch found. **The exact statement and defining dependencies identified below may be protected for proof work.** This does not certify a proof, compilation, or the original all-even conjecture.

## Paths and scope

- `P` = `.clawcodex/math-team/problems/liouville-goldbach-jul2026`
- `W` = `P/waves/multiples-four`
- `R` = `.clawcodex/math-team/review-inputs/r20260924-four-v1`
- `M` = `P/lean/.lake/packages/mathlib`
- `T` = `~/.elan/toolchains/leanprover--lean4---v4.32.2`

Reviewed the supplied neutral declaration, dependencies, literal readback, actual defining code, and proposition interface. Read the required workflow/protocol. No earlier fidelity reports or author-confidence material were consulted; no agents, task tools, proof search, or candidate edits were used.

## Source and declaration locators

- Exact continuation: `W/request.md:3,7–16`, especially the signature at lines 10–11 and explicit interpretation at line 14.
- Original definitions and conventions: `P/request.md:7–14,51–57`; source cutoff: lines 16–26.
- Candidate: `R/Declaration.lean:17–18`, in namespace `ArithmeticStatement`.
- Actual omega/lambda: `P/lean/Statement/Definitions.lean:6–8`.
- Actual representation predicates: `P/lean/Statement/Partial.lean:14–20`.
- Proposition interface: `W/formal/formalizer/Interface.lean:7–8`.
- Literal readback: `R/readback.md:7–49`. Its literal account agrees with this independent comparison; its label is not used as evidence of source fidelity.

The candidate unfolds to:

```lean
∀ (m : ℕ) (hm : 0 < m), ∃ a b : ℕ,
  0 < a ∧ 0 < b ∧ 4 * m = a + b ∧
    ArithmeticStatement.lambda a = (-1 : ℤ) ∧
    ArithmeticStatement.lambda b = (-1 : ℤ)
```

## Fidelity audit

- **Quantifiers/dependencies:** Universal `m`, then its positivity premise, then existential `a,b`. Witnesses may vary with `m`; no uniform witnesses or auxiliary assumptions are demanded. `hm` is a proof, not an additional numerical parameter. Lambda and omega are fixed definitions, not quantified functions. The helper sign parameter is fixed to integer `-1` before selecting witnesses.
- **Domains and coverage:** `m,a,b : ℕ`, with explicit strict positivity. This faithfully represents positive integers. Every positive multiple of four is covered by `4*m` with `m>0`; conversely such an input is a positive multiple of four and exceeds two. The new target is only this subclass, not a replacement for the original all-even target.
- **Hypotheses and restrictions:** The only theorem premise is `0<m`. There is no extra lambda-sign, parity, primality, coprimality, threshold, upper-bound, or seed-representation hypothesis on `m`. Neither witness has any additional restriction beyond positivity, the sum, and its required sign. Equality `a=b` is permitted.
- **Conclusion and direction:** This is unconditional existence for every admissible `m`, not a converse, implication from a representation assumption, almost-all assertion, or asymptotic assertion. The sum is exact; both sign equalities hold separately. No aggregate bound has been replaced by a pointwise bound, and no product-of-signs condition substitutes for the two signs. Constants `4`, `0`, and `-1` are fixed by the source, not unjustified choices.
- **Multiplicity:** `R/Declaration.lean:5–7` is byte-identical to `Definitions.lean:6–8`; `R/Declaration.lean:9–15` is byte-identical to `Partial.lean:14–20`. Actual `M/Mathlib/Data/Nat/Factors.lean:38–44` removes one minimum prime factor per recursion, without deduplication. Lines 55 and 70 specify prime entries and their product; lines 181–182 give `(p^n).primeFactorsList = List.replicate n p`. Actual minimum-factor definitions and properties agree with the neutral excerpts: `M/Mathlib/Data/Nat/Prime/Defs.lean:107,207–219,287–300`. Actual list length and replication agree with `R/ListOperations.lean`: `T/src/lean/Init/Prelude.lean:3027–3029` and `T/src/lean/Init/Data/List/Basic.lean:84–90,705–707`. Thus omega counts factors with multiplicity, not distinct primes.
- **Signs and boundary cases:** Lambda takes values in `ℤ`, with integer base `-1` and natural exponent; negative one is not natural-number negation. The empty factor list at 1 gives omega(1)=0 and lambda(1)=1. The analogous totalization at 0 is harmless because witnesses are positive. `m=0` is excluded exactly as requested; `m=1` is included. The premise is inhabited at 1, and the boundary case admits the allowed equal pair `(2,2)` under the supplied factor-list definition. These are semantic boundary checks, not a general existence proof.
- **Hidden assumptions:** No section variables, universe-generalized algebraic parameters, or typeclass premises occur in the target. Arithmetic, ordering, negation, exponentiation, and list-length addition resolve on concrete `ℕ`/`ℤ`, not adjustable instances supplied as hypotheses. The actual interface also disables auto-implicit parameters.

**Mismatch details:** None affecting the statement. The neutral files omit theorem proofs and some recursion-termination material; they are readback excerpts, not standalone verified theorem modules. Their defining equations agree with the inspected pinned implementation.

## Proof-status boundary and environment

`Interface.lean:7–8` defines a proposition. It does not supply an inhabitant/proof of that proposition. Its `#check` expressions at lines 13–17 assume `h : statement`; they do not establish it. Likewise, the neutral theorem signature contains no proof. No new-theorem compilation or axiom certification is claimed by this review.

The configured project pins Mathlib `905b95818eb32af7874a58b427f50c1711a5e96c` in both `lakefile.toml` and `lake-manifest.json`; local `git rev-parse HEAD` matched. `git status --porcelain --untracked-files=no` returned no changes. Local commit metadata dates that revision to `2026-07-28T18:36:13+02:00`. Both toolchain files specify `leanprover/lean4:v4.32.2`; the directly invoked installed binary reported Lean 4.32.2, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`. These checks succeeded. Only the supplied sources and explicitly authorized existing pin were used, with no external lookup, fetch, installation, or update. This is not a new public-availability audit of the preselected environment.

Next owner: leader may route proof work against this exact protected type. Proving it, checking its proof in the pinned environment, and reviewing its axioms remain separate obligations. A statement or defining-dependency change invalidates this approval and requires fresh readback/fidelity review.

## Exact SHA-256 identities

Hashes are over complete raw file bytes unless stated otherwise.

| Input | SHA-256 |
|---|---|
| `P/request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `R/Declaration.lean` | `bdfb30bcfade7b9df33e48f280125d10a40dd76f365cf5b87047183475fee7ed` |
| `R/Dependencies.lean` | `fd4ec312622db449d27d6ac0b18b1decd62a9f76e18f8251bb40ffbabdef7981` |
| `R/ListOperations.lean` | `925cbf08a1aac0870075ad56ff2d95c7b0eb94c87853ace32d0043a9c094e2bc` |
| `R/readback.md` | `5005673911eff1d1c13d16ad9bd7dd7dac5c33af88cb42e4f51115c41f24ebbe` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `W/formal/formalizer/Interface.lean` | `d8d4a87650d077b5b28f289055a0f11e58f9579c73b5343c5fa6a0748a27ea7d` |
| `P/lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `P/lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `P/lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |
| `M/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `M/Mathlib/Data/Nat/Prime/Defs.lean` | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `T/src/lean/Init/Prelude.lean` | `44f86ebbb9ab743a05c6ebe2c674aadbf2c822bee874f1b16d7e6c8d56318dc9` |
| `T/src/lean/Init/Data/List/Basic.lean` | `c6b61f1b5fcac4ea4339625f2e66916d1f2c1ae2531c10ee45b401846ffb6061` |

Declaration-signature hash (`R/Declaration.lean:17–18`, including each line's final LF):
`8553b2804a2be4c99b92e7e8127e588b00351a5d650386160c3056ee997d1728`.

Neutral code-snapshot hash:
`c5abd7fb64adc299338371578c825fe97af1427aff939fb71f9e928a7385da72`.
This is SHA-256 of the UTF-8 manifest formed by `file_sha256 + "  " + basename + "\n"`, in order `Declaration.lean`, `Dependencies.lean`, `ListOperations.lean`.
