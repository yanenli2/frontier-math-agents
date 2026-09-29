# Multiples-four wave source provenance

Mode: CERTIFICATION. External sources must have been publicly available on or before **2026-07-31 inclusive**. New local deductions are allowed but require proof/review; they are not retroactively attributed to historical literature. No post-cutoff source, new network lookup, or dependency update was used during this integration.

## 1. Inherited pins and public-availability evidence

The frozen [original source ledger](../../sources.md), especially ENV-LEAN, ENV-MATHLIB and its dependency table, remains authoritative for the original baseline. It is not edited by this wave. [REPRODUCE.md](REPRODUCE.md) lists every exact manifest revision.

- **Lean 4 v4.32.2**, Lean developers / leanprover. Immutable compiler/standard-library commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`: <https://github.com/leanprover/lean4/tree/f3b06c705e6c85f5314019d5d3baab0fec5b580c>. Exact-SHA public workflow <https://github.com/leanprover/lean4/actions/runs/30368480005>, created **2026-07-28T14:27:52Z**. Release published **2026-07-28T16:34:35Z**.
- **Mathlib 4 v4.32.2**, Mathlib community. Immutable revision `905b95818eb32af7874a58b427f50c1711a5e96c`: <https://github.com/leanprover-community/mathlib4/tree/905b95818eb32af7874a58b427f50c1711a5e96c>. Exact-SHA release workflow <https://github.com/leanprover-community/mathlib4/actions/runs/30379912464>, created **2026-07-28T16:47:39Z**. Release published **2026-07-28T16:47:51Z**.
- Plausible, Import graph, ProofWidgets 4, Aesop, Qq, Batteries, and Lean 4 CLI have retained exact-SHA public witnesses on **2026-07-13**; LeanSearchClient's is **2026-02-12**. Their authorship is credited to the respective upstream contributor groups, and exact version URLs/dates are in the original ledger and `formal/integration-full/{pre,post}-provenance.json`.

Public witnesses are retained raw metadata, not freshly queried webpages or commit timestamps alone. Source: [`../../formal/environment/public-availability-witnesses.json`](../../formal/environment/public-availability-witnesses.json), SHA-256 `051de67ee5bfd81242942075cf9dabacd8cfa96b74abf3733b025456694cc4c1`. A public CI record establishes availability of its exact `head_sha`; its success/failure is not itself mathematical evidence. All nine actual package HEADs match the manifest, package worktrees are clean, and nested manifests have no conflicting revisions. Dates below mean a verified public witness no later than the cutoff, not a claim of first publication.

## 2. Complete imported-source inventory

This ledger includes the following machine-readable and plain-text appendices:

- [`formal/integration-full/new-library-modules-v1.txt`](formal/integration-full/new-library-modules-v1.txt): **all 1983 wave-added library source modules**, each with title, credited authors, immutable URL/revision, exact-SHA public witness date and URL, whole-module line locator, SHA-256, and the stage that first imported it.
- [`formal/integration-full/library-inventory-v1.json`](formal/integration-full/library-inventory-v1.json): complete static source-import graph, source hashes, and the original/partial/full module sets, including inherited modules and Lean standard-library dependencies.

The original set is the closure of `Statement.{Definitions,Scaffold,Smoke,Partial}` before this wave: 2336 source modules. Adding `FourPartial` gives 3391; the full six-file packet gives 4326 (excluding the trivial root wrapper). Seven of the 1990 wave additions are local proof modules, leaving 1983 library modules; 929 library modules are added after the earlier FourPartial stage. This source graph includes ordinary and public/meta imports and implicit Init, so its counts differ from Lake's 2850 build-job count. It is an import inventory, not a claim that every imported theorem is used in the final proof. Where a module supplies no title/Authors header, the appendix explicitly uses the module identifier/upstream contributor group rather than inventing an individual author.

All Mathlib entries use the immutable revision and eligible release above. Other package/core entries carry their own already-pinned revision and exact witness. The readable entries below give the precise **load-bearing mathematical locators**, as distinct from each imported module's whole-file locator.

## 3. New load-bearing mathematical sources

All Mathlib URLs in this section select **`905b95818eb32af7874a58b427f50c1711a5e96c`**, publicly available by **2026-07-28**. Titles/authors are from those exact file headers, not current documentation.

### SQ — Sums of two squares

- Title: **Sums of two squares**. Authors: **Chris Hughes, Michael Stoll**.
- URL: <https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/NumberTheory/SumTwoSquares.lean#L33-L38>.
- Locator: `Nat.Prime.sq_add_sq`, lines 35–38. Source SHA-256 `ecc1647de087331c1876ca386b495ff2a83943a428bf140bf6ba8047f9fd80f9`.
- Exact usable type:

  ```lean
  {p : ℕ} → [Fact p.Prime] → p % 4 ≠ 3 → ∃ a b : ℕ, a ^ 2 + b ^ 2 = p
  ```

- Application: `Statement/FourPartial.lean:81–86` constructs `Fact p.Prime` from `hp`, derives `p%4≠3` from `p%4=1`, and reverses the returned equality. The receiving square-sum helper permits zero and equal roots and handles those cases explicitly.
- Proved source dependencies: **Gaussian integers**, Chris Hughes, [GaussianInt.lean:243–255](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/NumberTheory/Zsqrtd/GaussianInt.lean#L243-L255), `GaussianInt.sq_add_sq_of_nat_prime_of_not_irreducible`; and **Facts about the Gaussian integers relying on quadratic reciprocity**, Chris Hughes, [Zsqrtd/QuadraticReciprocity.lean:34–85](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/NumberTheory/Zsqrtd/QuadraticReciprocity.lean#L34-L85), `GaussianInt.prime_iff_mod_four_eq_three_of_nat_prime`.
- Source hashes, Git blob matches, source application review: `formal/integration-partial/provenance-addendum-v1.txt` and `formal/reviews/four-candidate-review-v1.md`.

### NEG — Legendre symbol: squareness of −1

- Title: **Legendre symbol**. Authors: **Chris Hughes, Michael Stoll**.
- URL: <https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/NumberTheory/LegendreSymbol/Basic.lean#L269-L286>.
- Locator: prime-instance scope at 269; `ZMod.exists_sq_eq_neg_one_iff`, lines 284–286.
- Source SHA-256 `9ac75516bf1585b7af0c71340344ecb3e4c135ac3c06f959d6a3f1e8c2ebd95c`.
- Usable type: for `[Fact p.Prime]`, `IsSquare (-1 : ZMod p) ↔ p % 4 ≠ 3`.
- Application: `Character/ResiduePrime.lean:43,48`, with the prime instance at `r` constructed from `hr`; use the appropriate implication for `r%4=1` or `r%4=3`.

### QR — Quadratic reciprocity and the supplement at 2

- Title: **Quadratic reciprocity**. Authors: **Chris Hughes, Michael Stoll**.
- URL: <https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean>.
- Source SHA-256 `24ffbf256f6f6f7a2617901323c2d532e2d7871c826a8b11f0580b283e994302`.
- Exact usable interfaces and instance scopes:
  - Lines 45,73–77: `[Fact p.Prime]`, `p≠2` imply `IsSquare (2 : ZMod p) ↔ p%8=1 ∨ p%8=7` (`ZMod.exists_sq_eq_two_iff`).
  - Lines 99,153–160: `[Fact p.Prime] [Fact q.Prime]`, `p%4=1`, `q≠2` imply `IsSquare (q : ZMod p) ↔ IsSquare (p : ZMod q)` (`ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_one`).
  - Lines 99,162–167: the same prime instances, `p%4=3`, `q%4=3`, `p≠q` imply `IsSquare (q : ZMod p) ↔ ¬ IsSquare (p : ZMod q)` (`ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_three`).
- Application: `Character/ResiduePrime.lean:13–48`. Both prime instances are derived from explicit hypotheses. Exact division gives `p+1=4rs` and `r≤(p+1)/4<p`. If `r=2`, then `p%8=7` and `p≥7` supplies `p≠2`. If `r%4=1`, apply the first reciprocity equivalence with its arguments swapped (`p=r,q=original p`) in the `.mp` direction. If `r%4=3`, use `.mpr` with the original `p,q=r`; `r<p` gives distinctness. The congruence `p=-1` modulo `r` and NEG provide the required square/nonsquare premise. No target or antireflection hypothesis enters these number-theoretic lemmas.
- These library results are proved in the eligible source tree via finite-field quadratic characters/Gauss sums; they are not custom axioms. See `formal/character-generator/provenance-v1.json` and exact formal review §6.

## 4. Algebra, representatives, counting, and tactics

These are pinned proof infrastructure, not additional analytic assumptions. Some were already transitively imported before the wave; the complete inventory distinguishes that fact.

| Key / title | Authors | Immutable source and locator | Use |
|---|---|---|---|
| FIELD — `ZMod p` is a field | Chris Hughes | [Algebra/Field/ZMod.lean:17–39](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Algebra/Field/ZMod.lean#L17-L39) | `ZMod.instField`; every `[Fact p.Prime]` is locally constructed from `hp`, permitting nonzero-product and cancellation laws. |
| REP — Integers mod `n` | Chris Hughes | [Data/ZMod/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Data/ZMod/Basic.lean), `.val` 51–64, bounds 89–93; exact named cast/negation interfaces in `06-root-import` axiom list | Least natural representatives for positive modulus; no periodicity of lambda is assumed. Modulus-zero totalization is not used as a finite field. |
| SQUARE — Squares and even elements | Damiano Testa | [Algebra/Group/Even.lean:50–57](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Algebra/Group/Even.lean#L50-L57) | `IsSquare t` is `∃ r, t=r*r` in the displayed multiplication type, here `ZMod p`. |
| PH — Cardinality of a finite set | Leonardo de Moura, Jeremy Avigad | [Data/Finset/Card.lean:446–458](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Data/Finset/Card.lean#L446-L458) | `Finset.exists_ne_map_eq_of_card_lt_of_maps_to`: if `card t<card s` and `f` maps `s` to `t`, two distinct elements of `s` have the same image. Cyclic:64–76 supplies `s=range n`, `t=range(n−1)`, and the bin-map premise. |
| LIN — Linarith tactic module | Robert Y. Lewis | [Tactic/Linarith.lean:1–18](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Tactic/Linarith.lean#L1-L18), importing Frontend and NormNum | Kernel-checked arithmetic inequalities, including `nlinarith`; not an external solver axiom. |
| RING — Ring tactic | Mario Carneiro, Aurélien Saue, Anne Baanen (Basic header); aggregator has no Authors header | [Tactic/Ring.lean:1–7](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Tactic/Ring.lean#L1-L7), [Ring/Basic.lean:1–25](https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Tactic/Ring/Basic.lean#L1-L25) | Ring normalization; already used by the original Partial module. |

The inherited positive-domain factorization APIs (`Nat.perm_primeFactorsList_mul`, `Nat.prod_primeFactorsList`, prime singleton/list membership) and `Nat.Prime` are documented in [the original ledger](../../sources.md#mathematical-source-locators-at-the-pinned-mathlib-version). They count multiplicity and require no coprimality for positive-argument multiplication. Core strong induction and integer/natural arithmetic are from the exact Lean standard library pin above. No PNT, Chowla, Goldbach, Siegel, or Linnik theorem is an imported assumption.

## 5. Local mathematical work and review identity

| Local source | Authorship/version | Exact role |
|---|---|---|
| [request.md](request.md) | User continuation request, hash `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` | Every positive `m`, including 1; positive natural witnesses; both signs −1. |
| [PROOF.md](PROOF.md) | Local math-team exposition, frozen hash `205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b` | Final informal theorem and §§1–8 argument; unchanged by integration. |
| [nl/generator/proof-attempt-v1.md](nl/generator/proof-attempt-v1.md) | Local NL generator, version 1 | Earlier nineteen-helper families and reductions, §§1–4. |
| [nl/descent/proof-attempt-v1.md](nl/descent/proof-attempt-v1.md) | Local NL descent work, version 1, hash `23fc6ad19d1c45dd432945aa84756b190700b8c15394b1554ebb3ecaff82235e` | Source lines 31–42,44–332 for the full helper graph. |
| [formal/descent-blueprint/Readback.lean.txt](formal/descent-blueprint/Readback.lean.txt) | Local protected interface snapshot, hash `372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763` | Nineteen full signatures, two new definitions, four fixed defining bodies. |
| [formal/reviews/full-candidate-review-v1.md](formal/reviews/full-candidate-review-v1.md) | Independent exact-candidate formal reviewer, version 1 | APPROVE for Assembly hash `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066` and frozen closure; does not itself publish the root. |

These local artifacts were produced during the 2026-09-24/25 work, after the external-source cutoff; they are disclosed **new deductions**, not disallowed later external literature. [LEMMA_MAP.md](LEMMA_MAP.md) records exact declaration/source/dependency/status links. Fresh final NL reviews [A](nl/reviews/final-four-review-a-v1.md) and [B](nl/reviews/final-four-review-b-v1.md) both report PASS on the frozen PROOF/Assembly/dependency hashes; these are independent mathematical reviews, not compiler verification. The final regulator gate remains leader-owned.

The prose uses a direct floor-parity proof for the small square prime and inverse pairing for primes 1 modulo 4. **Lean instead uses QR/NEG and SQ**, respectively, and a pigeonhole bin implementation for the cyclic lemma. The statement snapshots/reviews explicitly permit these same-conclusion proof routes; the individual prose substeps and its arbitrary-function generalization are not all separately formalized. Neither `PROOF.md`'s elementary-only description nor an author-confidence statement is substituted for compiler evidence.

## 6. Build-artifact trust and exclusions

The generator previously acquired exact-pin cached artifacts with `lake exe cache get Mathlib.NumberTheory.SumTwoSquares` and `lake exe cache get Mathlib.NumberTheory.LegendreSymbol.QuadraticReciprocity`. The preserved commands, environments and exit-0 records are `formal/generator/four-cache-sum-two-squares-v1.json` and `formal/character-generator/reciprocity-cache.json`. Cache use is an explicit imported-artifact trust boundary, not a newer source version. No cache acquisition was repeated during final integration.

All local proof modules were re-elaborated with Lean trust level zero, and the final theorem's transitive axioms are exactly `propext`, `Classical.choice`, `Quot.sound`. No admission/custom/native-reduction axiom is accepted. This is not a cold bootstrap or a full from-source rebuild of upstream libraries. Full commands, raw diagnostics and hashes are in [REPRODUCE.md](REPRODUCE.md) and `formal/integration-full/`.

The original ledger's Mangerel paper is contextual literature, not a proof dependency of this wave. Its quarantined post-cutoff MathOverflow snippet remains excluded. No newly encountered external mathematical source was used here. The original all-even target is not proved by this multiples-four result.
