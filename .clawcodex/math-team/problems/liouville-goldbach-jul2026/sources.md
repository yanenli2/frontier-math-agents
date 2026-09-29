# Source provenance ledger

Cutoff: public availability on or before 2026-07-31 inclusive. Version-specific eligibility is mandatory. Search snippets are not mathematical evidence. The pinned library is the only external proof dependency; literature below is dated context, not an imported proof.

## ENV-LEAN
- Title: Lean 4 v4.32.2 release.
- Authors: Lean developers / leanprover.
- URL: https://github.com/leanprover/lean4/releases/tag/v4.32.2
- Version: v4.32.2 (installed elan toolchain).
- Public availability: 2026-07-28T16:34:35Z, GitHub published_at queried 2026-09-24.
- Evidence command: `gh api repos/leanprover/lean4/releases/tags/v4.32.2 --jq '{tag_name,published_at,target_commitish,html_url}'` (exit 0).
- Role: compiler/kernel/standard library dependency. Exact commit, public-availability evidence and full dependency audit are recorded below and in formal/environment/.
- Theorem/page: not applicable to release metadata.

## ENV-MATHLIB and exact dependency versions

- Title: Mathlib 4, release v4.32.2. Authors: the Mathlib community.
- Immutable revision: `905b95818eb32af7874a58b427f50c1711a5e96c`.
- URL: https://github.com/leanprover-community/mathlib4/tree/905b95818eb32af7874a58b427f50c1711a5e96c
- Release public availability: 2026-07-28T16:47:51Z; exact-SHA public release workflow https://github.com/leanprover-community/mathlib4/actions/runs/30379912464 created 2026-07-28T16:47:39Z.
- Lean exact revision: `f3b06c705e6c85f5314019d5d3baab0fec5b580c`; source https://github.com/leanprover/lean4/tree/f3b06c705e6c85f5314019d5d3baab0fec5b580c ; exact-SHA public workflow https://github.com/leanprover/lean4/actions/runs/30368480005 created 2026-07-28T14:27:52Z.
- Release tags are mutable; the mathematical dependency is pinned by immutable commit. Raw metadata and exact commands are in formal/environment/.

All transitive packages are source-code dependencies, credited to their upstream contributors. Dates below are observed exact-SHA public CI creation dates, not claims of first publication. Each linked source is the actual pinned version; all are before cutoff.

| Title / contributor group | Version-specific source URL | Public witness date (UTC) |
|---|---|---|
| Plausible / plausible contributors | https://github.com/leanprover-community/plausible/tree/e12c1910fe855cbfc38803cd4e55543906d5fa62 | 2026-07-13T13:20:50Z |
| LeanSearchClient / LeanSearchClient contributors | https://github.com/leanprover-community/LeanSearchClient/tree/c5d5b8fe6e5158def25cd28eb94e4141ad97c843 | 2026-02-12T00:28:07Z |
| Import graph / import-graph contributors | https://github.com/leanprover-community/import-graph/tree/7e9612bf0b9ee66db3cb5b9988a35afc706f5a12 | 2026-07-13T13:50:43Z |
| ProofWidgets 4 / ProofWidgets contributors | https://github.com/leanprover-community/ProofWidgets4/tree/6e311e2a844da9b2cc3971187df2fe0066947b93 | 2026-07-13T13:20:54Z |
| Aesop / Aesop contributors | https://github.com/leanprover-community/aesop/tree/a7dbf0c63b694e47f425f3dcddbc0e178bb432d3 | 2026-07-13T14:03:38Z |
| Qq / quote4 contributors | https://github.com/leanprover-community/quote4/tree/38d591e778f100aec9762bb582f9c7f55f50e9dc | 2026-07-13T13:20:57Z |
| Batteries / Batteries contributors | https://github.com/leanprover-community/batteries/tree/023ce7d62a0531e22a5331e20b587817a80d49ff | 2026-07-13T20:29:43Z |
| Lean 4 CLI / lean4-cli contributors | https://github.com/leanprover/lean4-cli/tree/88679d088c9720c27ebdf2ba4dafe17341747f94 | 2026-07-13T13:20:47Z |

Exact public witness URLs, authorship convention, nested-manifest audit and raw responses: formal/formalizer/proposed-sources-additions.txt §§A–C; formal/environment/public-availability-witnesses.json; formal/environment/dependency-audit.stdout. No current main branch was fetched. Existing source-hash-addressed build cache is a disclosed trusted artifact mechanism, not a new source version; integration additionally ran Lean with trust level zero. Neither cache use nor metadata establishes the unproved Target.

### Mathematical source locators at the pinned Mathlib version

- *Prime numbers*, Leonardo de Moura, Jeremy Avigad, Mario Carneiro: `Mathlib/Data/Nat/Factors.lean`, primeFactorsList 38–44, empty case 49–50, prime entries 55–65, product 70–81, prime singleton 83–88, uniqueness 167–179, multiplicative concatenation 196–202. URL: https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Data/Nat/Factors.lean . Last-changing ancestor available 2026-03-25.
- *Prime numbers (definitions)*, same authors: `Mathlib/Data/Nat/Prime/Defs.lean`, Prime 42–43, minFac 207–219, minFac_dvd/minFac_prime 287–303. Last-changing ancestor available 2026-06-30.
- *Squares and even elements*, Damiano Testa: `Mathlib/Algebra/Group/Even.lean` 53–57, generated Even definition, checked with `#print`; last-changing ancestor 2025-11-19.
- Power sign dichotomy: `Mathlib/Algebra/Ring/Parity.lean` 387–391, `neg_one_pow_eq_ite`; finite intervals/cardinality: `Mathlib/Order/Interval/Finset/Nat.lean` 82–85; sum bijection: `Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean` 497–510; finite sums and distribution: `Mathlib/Algebra/BigOperators/Ring/Finset.lean` 56–60. File authors remain credited in the pinned headers. Full exact theorem statements/application guards are in formal/blueprinter/blueprint-v1.md §4 and formal/integration/source-proof-map-v1.txt; these source files share the dated immutable Mathlib release above.
- Core List.length/List.replicate/Int power: Lean source at its exact commit, `src/Init/Prelude.lean` 3027–3029, `src/Init/Data/List/Basic.lean` 84–90 and 705–707, `src/Init/Data/Int/Basic.lean` 400–405. Exact bytes/source hashes: formal/environment/source-file-identities.json.

No external analytic theorem (PNT, Siegel, Linnik, Chowla, Goldbach) is imported as an assumption. Lean trusts only its standard foundations and disclosed compiler/build mechanisms, documented in REPRODUCE.md.

## Local deductions
New work during this run is permitted but requires proof and independent review. It is not attributed to an external historical source. The integrated partial proofs are in lean/Statement/Partial.lean, hash `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0`. Lemma/declaration correspondence is maintained in LEMMA_MAP.md. The original target has no proof.

## LIT-1: versioned primary source
- Title: On a Goldbach-type problem for the Liouville function.
- Author: Alexander P. Mangerel.
- Version: arXiv:2404.12117v2.
- URLs: https://arxiv.org/abs/2404.12117v2 ; https://arxiv.org/pdf/2404.12117v2
- Public availability metadata: submitted v1 2024-04-18; v2 2024-05-02 14:48:54 UTC, verified on the version-selected arXiv record through gstack browse on 2026-09-24.
- Preserved source: knowledge/mangerel-v2/paper.pdf (229632 bytes), SHA-256 ae26a659220985c55576a18d05a84d5a56988024f8781ae4ccbe04847ac16505. Metadata: knowledge/mangerel-v2/arxiv-metadata.txt.
- Relevant locators: Theorem 1.2, printed/PDF p.1; Remark 1, p.2; Remark 2, p.3. Exact source extraction and independent mathematical applicability review pending. These items are not imported Lean proofs.

## Contamination
The source searcher encountered an automatically returned MathOverflow snippet whose footer read `rev 2026.9.15.45626`, despite the query filter `before:2026-08-01`. URL: https://mathoverflow.net/questions/427499/does-asymptotic-goldbach-imply-grh . The result was not opened or used; all its mathematical assertions are excluded. See nl/searcher/search-trace.md. No later mathematical source body has intentionally been read. Unversioned search results remain unadmitted.
