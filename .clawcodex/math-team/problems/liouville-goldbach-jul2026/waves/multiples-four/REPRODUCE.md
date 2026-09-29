# Reproduce the integrated positive-multiples-of-four theorem

Mode: CERTIFICATION — mechanically integrated, compiler-checked exact candidate.
Fresh final NL reviews [A](nl/reviews/final-four-review-a-v1.md) and [B](nl/reviews/final-four-review-b-v1.md) report PASS for these exact mathematical files (A also records the root-only promotion; B records the integrated root). Final regulator/publication acceptance remains leader-owned.

## Exact result and scope

Import `Statement` (the default root) or `Statement.FourWork.Assembly`:

```lean
ArithmeticStatement.representation_multiple_four (m : ℕ) (hm : 0 < m) :
  ArithmeticStatement.HasRepresentation (4 * m)
```

Here the conclusion is exactly

```lean
∃ a b : ℕ, 0 < a ∧ 0 < b ∧ 4 * m = a + b ∧
  (-1 : ℤ) ^ a.primeFactorsList.length = -1 ∧
  (-1 : ℤ) ^ b.primeFactorsList.length = -1
```

There is no extra prime, sign, parity, congruence, coprimality, or threshold premise; `m=1` is included and equal witnesses are allowed. The prime-core endpoint is `ArithmeticStatement.representation_four_prime_three_mod_four`, for prime `p≥7` with `p%4=3`.

**This does not prove the original all-even `ArithmeticStatement.Target`.** The old `UnfinishedScaffold` has an unprovided `result : Target` field, not a constructed proof. The original `../../REPRODUCE.md` remains frozen. The superseded nineteen-helper draft is preserved verbatim at [`formal/integration-full/REPRODUCE.before.md.txt`](formal/integration-full/REPRODUCE.before.md.txt); its absence claim for the new `representation_multiple_four` is historical, not current.

## Fixed environment

- Lean `leanprover/lean4:v4.32.2`, compiler commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`.
- Lake `5.0.0-src+f3b06c7`; actual platform arm64 Apple Darwin.
- Mathlib `905b95818eb32af7874a58b427f50c1711a5e96c`.
- Manifest SHA-256 `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03`.

| Package | Exact revision |
|---|---|
| mathlib | `905b95818eb32af7874a58b427f50c1711a5e96c` |
| plausible | `e12c1910fe855cbfc38803cd4e55543906d5fa62` |
| LeanSearchClient | `c5d5b8fe6e5158def25cd28eb94e4141ad97c843` |
| importGraph | `7e9612bf0b9ee66db3cb5b9988a35afc706f5a12` |
| proofwidgets | `6e311e2a844da9b2cc3971187df2fe0066947b93` |
| aesop | `a7dbf0c63b694e47f425f3dcddbc0e178bb432d3` |
| Qq | `38d591e778f100aec9762bb582f9c7f55f50e9dc` |
| batteries | `023ce7d62a0531e22a5331e20b587817a80d49ff` |
| Cli | `88679d088c9720c27ebdf2ba4dafe17341747f94` |

All nine HEADs and clean package worktrees were checked before and after integration; nested manifests agree. Retained exact-SHA public CI metadata places every external version before **2026-08-01** (cutoff **2026-07-31 inclusive**). See [sources.md](sources.md), the frozen [original source ledger](../../sources.md), and `formal/integration-full/{pre,post}-provenance.json`. No network lookup, fetch, cache acquisition, installation, toolchain change, `lake update`, or manifest regeneration occurred during integration.

## Commands actually checked

Working directory for every Lean/Lake command is the problem's `lean/` directory, `../../lean` relative to this wave. In the original checkout its absolute path is:

```text
.clawcodex/math-team/problems/liouville-goldbach-jul2026/lean
```

Using that existing pinned environment:

```bash
lake env lean --version
lake --version
lake build
lake build Statement.FourWork.Assembly
lake env lean Statement/FourWork/Assembly.lean
lake env lean -t0 Statement/FourWork/Assembly.lean
lake env lean -t0 Statement/Definitions.lean
lake env lean -t0 Statement/Scaffold.lean
lake env lean -t0 Statement/Smoke.lean
lake env lean -t0 Statement/Partial.lean
lake env lean -t0 Statement/FourPartial.lean
lake env lean -t0 Statement/FourWork/Descent/Ternary.lean
lake env lean -t0 Statement/FourWork/Character/ResidueValue.lean
lake env lean -t0 Statement/FourWork/Descent/Cyclic.lean
lake env lean -t0 Statement/FourWork/Character/Rigidity.lean
lake env lean -t0 Statement/FourWork/Character/ResiduePrime.lean
lake env lean -t0 Statement.lean
lake env lean -t0 --stdin < ../waves/multiples-four/formal/integration-full/06-root-import.stdin.lean
lake env lean -t0 --stdin < ../waves/multiples-four/formal/integration-full/08-root-expanded-type.stdin.lean
```

**Every command above exited 0.** Default `lake build` completed 2850 jobs, explicitly replayed `Statement.FourWork.Assembly`, and rebuilt the root. All twelve local modules were additionally re-elaborated at trust level zero; default-build replay was not the sole evidence. Only four pre-existing unused-variable warnings in unchanged `Partial.lean:51,171,187,291` occurred. Assembly and both root diagnostic inputs have no warnings.

The `06` diagnostic imports **only `Statement`**. It checks all 38 wave theorem types (19 earlier helpers and 19 full-packet theorems including the two endpoints), six definition types/bodies, the final fully expanded type by definitional ascription, and 156 distinct transitive axiom sets. The `08` diagnostic checks the same theorem through `id` with the expanded type explicitly fixed; its output displays the positive natural witnesses and factor-list powers without the local representation/lambda abbreviations. Neither diagnostic adds a theorem to the master.

Scope-only negative test:

```bash
lake env lean -t0 --stdin < ../waves/multiples-four/formal/integration-full/07-original-endpoints-absent.stdin.lean
```

Expected and observed exit **1**, with exactly two unknown identifiers: `ArithmeticStatement.pointwise_keystone` and `ArithmeticStatement.liouville_goldbach`. This is not a failed proof or an assertion that those mathematical propositions are false.

## Exact promotion and identities

The **only master edit** was appending `import Statement.FourWork.Assembly` to `Statement.lean`. No proof declaration, namespace, filename, definition, or statement was copied, renamed, or rewritten. All six full-packet files remain byte-identical to the approved candidate, as do the previous masters and pins.

| File relative to `../../lean` | SHA-256 |
|---|---|
| `Statement.lean` before | `dc72b845dbb045593ef3a6212b03a54cc0797a29baac132e870aff324cdc5853` |
| `Statement.lean` integrated | `cd6a1dd9bff63ef400559805123c5e6cb7d2d4c9af28cf7f7c24f2cc640abc3c` |
| `Statement/FourWork/Assembly.lean` | `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066` |
| `Statement/FourWork/Descent/Cyclic.lean` | `09fbee47a60bf7db94d65e871fc49f5d07d60838c8b01cfbfdecb53033471290` |
| `Statement/FourWork/Descent/Ternary.lean` | `d6f231fc9aa372f562b19170268b31ae16bdca178185256131232011fd255753` |
| `Statement/FourWork/Character/ResidueValue.lean` | `3df5a3f0a6de6a60c2b8b8ba89dd6e44fa4d47cb28e98c33f1e31d1dfb7d84dd` |
| `Statement/FourWork/Character/ResiduePrime.lean` | `518f28a33ab98d1a44ea7b544ca7f695e28c48893982caaf72eb4879956763dd` |
| `Statement/FourWork/Character/Rigidity.lean` | `843e4ee562071ef4729a61c715b77510b378add7f19b8c02d1e3d36fa9165f88` |
| `Statement/FourPartial.lean` | `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325` |
| `Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |

Frozen prose `PROOF.md`: `205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b`.
Full approved signature/definition snapshot `formal/descent-blueprint/Readback.lean.txt`: `372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763`.
The exact source file still contains the final theorem at `Assembly.lean:21–24`.

## Axioms and actual trust boundary

Both endpoints and all 38 wave theorems use exactly **`propext`, `Classical.choice`, `Quot.sound`**. Every other printed set is a subset of those three standard axioms. No `sorryAx`, custom axiom, native-reduction axiom, or admitted obligation occurs in the target's proof closure. The twelve-file local import graph is acyclic, and source scans found no admission/custom/native-proof shortcut; actual compilation and transitive axiom checks corroborate those scans.

Trust includes the installed Lean/Lake compiler and kernel, elaborator/tactic implementations, and existing pinned imported `.olean`/build artifacts. A cold compiler bootstrap and a complete from-source upstream-library rebuild were **not** performed. Local `-t0` recompilation does not remove the imported-artifact/build trust boundary. `Smoke`'s `#eval` tests are not proof evidence. Ordinary `decide`, `omega`, `ring`, and `nlinarith` produce checked proof terms; library tactic implementation internals are not claimed to contain no unsafe code.

Historical same-pin cache acquisitions are preserved in `formal/generator/four-cache-sum-two-squares-v1.json` and `formal/character-generator/reciprocity-cache.json`; neither was repeated here.

## Proof-method and review boundaries

The Lean proof uses eligible Mathlib **Fermat two-squares and quadratic reciprocity** results. The frozen prose proves its floor-parity and inverse-pairing alternatives directly. Likewise Lean's cyclic helper uses bins/pigeonhole rather than sorting circular gaps. These are reviewed proof-method differences, not altered target statements. Do not describe the Lean proof as avoiding those imported theorems or as a line-by-line formalization of every generic-function prose assertion.

Exact candidate approval: [`formal/reviews/full-candidate-review-v1.md`](formal/reviews/full-candidate-review-v1.md). Statement protection and neutral readback references: [LEMMA_MAP.md](LEMMA_MAP.md). This integration does not self-certify a changed statement; all protected interfaces are unchanged.

## Durable evidence

All final integration evidence is in [`formal/integration-full/`](formal/integration-full/):

- `integration-report-v1.txt`: final checklist, boundaries, exact handoff.
- `audit-v1.json`: passing merged gate and all 156 axiom sets.
- `snapshot-before.json`, `snapshot-after.json`, `artifact-hashes-v1.json`: exact identities and preserved inputs.
- `signatures-integrated.json`: all 38 exact theorem headers and six definitions, with source/snapshot lines and hashes.
- `integration.diff`, `Statement.before.lean.txt`: the single import change and retained old root.
- `01`–`08` records: exact argv, working directories, exit codes, diagnostic inputs, raw stdout/stderr and stream hashes.
- `local-closure.json`, `olean-identities.json`: acyclic local imports and built-artifact identities.
- `library-inventory-v1.json`, `new-library-modules-v1.txt`: complete wave-added library provenance inventory.

The initial recorder had two non-Lean failures: a nonexistent original-document inventory path, then an axiom parser that missed an apostrophe in `Finset.sum_nbij'`. All Lean commands had passed. `resume-integration-v1.py` validated preserved logs/hashes, repaired only interpretation of diagnostic names, and finished missing checks without repeating passed builds. A separate source-inventory parser was restricted to Lean import headers after it encountered a JavaScript import inside a string. Raw failures are retained in `recorder-attempt-*` and `library-inventory-attempt-0.txt`; no mathematical source changed. The record-producing scripts use exclusive output creation to prevent overwriting history; reproduce Lean results with the direct commands above.
