# Final multiples-of-four regulator audit v1

Mode: CERTIFICATION — evidence audit, not proof production or repair.

**Wave verdict: PASS for the exact positive-multiples-of-four lemma. All documented proof-acceptance conditions for this lemma are met. No mathematical, formal, integration, or source-provenance blocker remains. The original all-even `ArithmeticStatement.Target` remains unresolved.**

The accepted endpoint is exactly:

```lean
ArithmeticStatement.representation_multiple_four (m : ℕ) (hm : 0 < m) :
  ArithmeticStatement.HasRepresentation (4 * m)
```

Its actual master location is `P/lean/Statement/FourWork/Assembly.lean:21–24`, exposed by `import Statement`. Here `P=.clawcodex/math-team/problems/liouville-goldbach-jul2026`, `W=P/waves/multiples-four`, `I=W/formal/integration-full`, and `R=P/../../review-inputs/r20260924-four-v1`. Audit date: 2026-09-27 UTC.

## 1. Scope and independently reconciled identities

I read the protocol and Lean workflow, both requests, actual master and all five FourWork dependencies, Definitions/Partial/FourPartial, root-only Scaffold/Smoke, protected snapshots, isolated literal readbacks, fidelity/candidate reviews, final prose, both final mathematical reviews, source/reproduction/map records, integration diff and raw diagnostic evidence. No proof, statement, source ledger, reproduction document, shared status, or earlier review was edited. No agent, task/team call, network lookup, installation, dependency update, or Lean rebuild was performed.

The companion **`final-four-regulator-v1.json`** records independent mechanical reconciliation, not a copied integrator verdict: 258 delivery-file identities rehashed; 56 protected pre-integration files reconciled with the sole root-import exception; 38 theorem headers and six definition bodies/types compared to snapshots; 56 saved command records and their stream hashes/lengths checked; all 4326 inventoried imported source files rehashed. Current package HEADs and clean worktrees were checked independently. No mismatch was found, including the final end-of-audit rehash.

| Artifact | Actual SHA-256 |
|---|---|
| `W/PROOF.md` | `205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b` |
| `Statement/FourWork/Assembly.lean` | `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066` |
| `Statement.lean` | `cd6a1dd9bff63ef400559805123c5e6cb7d2d4c9af28cf7f7c24f2cc640abc3c` |
| `Statement/FourWork/Descent/Ternary.lean` | `d6f231fc9aa372f562b19170268b31ae16bdca178185256131232011fd255753` |
| `Statement/FourWork/Descent/Cyclic.lean` | `09fbee47a60bf7db94d65e871fc49f5d07d60838c8b01cfbfdecb53033471290` |
| `Statement/FourWork/Character/ResidueValue.lean` | `3df5a3f0a6de6a60c2b8b8ba89dd6e44fa4d47cb28e98c33f1e31d1dfb7d84dd` |
| `Statement/FourWork/Character/Rigidity.lean` | `843e4ee562071ef4729a61c715b77510b378add7f19b8c02d1e3d36fa9165f88` |
| `Statement/FourWork/Character/ResiduePrime.lean` | `518f28a33ab98d1a44ea7b544ca7f695e28c48893982caaf72eb4879956763dd` |
| `Statement/FourPartial.lean` | `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325` |
| `Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |

Lean paths in this table are relative to `P/lean`. Complete evidence identities are in the companion JSON and `I/artifact-hashes-v1.json`.

## 2. Statement correspondence and all 38 interfaces — PASS

A compiler pass alone would establish only the encoded proposition under its axioms. Separate source-correspondence evidence is present and current:

- Exact lemma: `W/formal/approved-v1/Declaration.lean`, SHA-256 `bdfb30bcfade7b9df33e48f280125d10a40dd76f365cf5b87047183475fee7ed`; isolated `R/readback.md`; independent `formal/reviews/statement-fidelity-v1.md`.
- Earlier 19 helpers: `formal/generator/four-interfaces-v1.lean`, SHA-256 `be55b4df2e640ec4645a2544b0013de5d6f366439162820af4233162766a0cee`; isolated `R/interfaces-readback.md`; `helper-fidelity-v1.md` and `four-candidate-review-v1.md`.
- Full 19-theorem packet and definitions: `formal/descent-blueprint/Readback.lean.txt`, SHA-256 `372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763`; isolated `R/descent-readback.md`, SHA-256 `460c911b32d72948da676c52e3f0edba52ad724aa505bd4d650b94375165e6ab`; `descent-fidelity-v1.md` and `full-candidate-review-v1.md`.

The neutral packets contain code-only signatures and defining dependencies, not the source proof. Their current bytes match the protected copies. Literal readback is used for its quantifiers and caveats, not as source-fidelity or proof certification. The independent fidelity reports supply the source comparison. The final candidate review also covers the exact final prose and the unchanged proof implementation.

All **19 FourPartial theorem headers plus 19 full-packet headers** match their protected snapshots internally, excluding proof assignments/bodies and outer whitespace. All **six relevant definitions** match. The initially approved endpoint differs only in whitespace. `I/06-root-import.stdout:1–148` independently displays the elaborated types and definitions; no extra implicit or typeclass premise appears. The original all-even snapshot `P/formal/approved-v1/Definitions.lean` is byte-identical to the actual Definitions file, including `Target`.

The expanded endpoint is precisely

```text
∀ m : ℕ, 0 < m → ∃ a b : ℕ,
  0 < a ∧ 0 < b ∧ 4*m = a+b ∧
  (-1 : ℤ)^a.primeFactorsList.length = -1 ∧
  (-1 : ℤ)^b.primeFactorsList.length = -1.
```

Multiplicity is genuine: the pinned factor-list recursion removes one minimum prime factor at a time, prime powers give repeated lists, and positive multiplication concatenates lists up to permutation without coprimality. `lambda 1=1`; the totalization at zero does not supply a witness. Both witness positivities and both individual negative signs are explicit. Equal witnesses are allowed. There is no sign, parity, congruence, primality, coprimality, uniform-witness, or additional size premise on `m`.

## 3. Vacuity, premises, cases, and dependency direction — PASS

The source/code/review comparison checks the following load-bearing risks, rather than treating header equality as enough:

- **Complete multiplier coverage:** positive-sign multipliers use `2m,2m`, including `m=1`; even multipliers use the two-sign seed at eight; odd negative-sign multipliers have a prime divisor with a positive sign-+1 cofactor. Scaling requires no coprimality and permits repeated prime factors or cofactor one.
- **Complete prime coverage:** prime two is handled by the even branch; prime three by the twelve seed; primes 1 modulo four by the reviewed two-squares branch; the remaining primes are exactly those at least seven and 3 modulo four. The lower endpoint seven is included. The reverse implication of the proved prime-core equivalence is the direction used in Assembly.
- **Degenerate squares:** the earlier square-sum helper permits zero or equal coordinates. Unequal coordinates yield strictly positive sum/difference roots; equal coordinates use the eight seed. No unjustified positive/distinct root is extracted from the library theorem.
- **Descent:** positivity guards make reflection subtraction legitimate. Divisibility by three is proved before using the two quotients. Ordered gaps strictly decrease; oddness excludes the equal-entry case. The approved gap interface asserts strict decrease, not an additional exact contraction theorem.
- **Cyclic and residue steps:** the wrapping case and both signs of integer `k` are covered. The essential bound is strictly `n*d<p`, justifying ordinary multiplicativity before modular reduction. `GoodMultiplier` separately requires its multiplier to be nonzero and tests every nonzero residue; it does not encode a representation premise. Cancellation is by a proved nonzero sign. Modular-square uses exclude a zero residue/root through `0<n<p`.
- **Small prime:** `p≥7` and `p%4=3` make the quarter exact and at least two. A prime divisor satisfies `2≤r≤(p+1)/4<p`. The reciprocity branches supply all prime instances, oddness/distinctness conditions, and correct implication directions.
- **No circular endpoint premise:** Ternary derives antireflection from hypothetical nonrepresentation without importing Assembly. Rigidity is explicitly conditional on antireflection; the independent small-prime module assumes neither antireflection nor nonrepresentation. Assembly introduces `hno` only within contradiction, supplies antireflection from Ternary, and contradicts the small prime's sign. Neither premise survives either endpoint. The earlier scaling helper's core premise is ultimately discharged, not silently assumed.

The deliberately impossible premise bundles of the contradiction helpers after the endpoint is proved are not endpoint vacuity. The antireflection condition at prime two is also impossible, but the final application has `p≥7`. Empty small-multiplier induction range at one is handled by the identity multiplier.

The actual local root graph has **12 acyclic modules**, and Assembly's proof import closure has **nine**. No helper imports Assembly or root `Statement`; no duplicate declaration or alternate defining body occurs in this integrated closure. Signature-only neutral copies and historical scratch candidates are not imported competing definitions. Root-only `UnfinishedScaffold` has an unprovided `result : Target` field; its constructor requires that proof. It supplies no inhabitant or axiom. Smoke's `#eval` checks are not proof evidence.

## 4. Integrated compiler evidence, axioms, and recorder correction — PASS

Actual pinned environment: Lean **v4.32.2**, compiler commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`; Lake `5.0.0-src+f3b06c7`; arm64 Apple Darwin. Saved argv, cwd, exits, stdin, stdout/stderr bytes and hashes were independently checked. Working directory is `P/lean`.

| Preserved execution | Observed exit |
|---|---:|
| `01`: `lake build` | 0 |
| `02`: `lake build Statement.FourWork.Assembly` | 0 |
| `03`: `lake env lean Statement/FourWork/Assembly.lean` | 0 |
| `04`: `lake env lean -t0 Statement/FourWork/Assembly.lean` | 0 |
| `05`: `lake env lean -t0 <source>` for the other eleven local modules | 0 each |
| `06`: root-only type/definition/axiom stdin check | 0 |
| `08`: root-only explicitly expanded endpoint type | 0 |
| `07`: two deliberately absent original endpoint names | 1, expected |

Default-build output explicitly replays Assembly, builds `Statement`, and finishes successfully with 2850 jobs. It is not represented as a cold rebuild. Direct/trust-zero source checks cover every local module; their stored built-module identities still match. Root-only stdin ascribes the expanded intended proposition to the **actual theorem**, not an unrelated successful example. `08` displays that expanded type. No passing build needed repetition.

All **1003 axiom-print occurrences**, including Lake-prefixed replay messages, were independently parsed and reconciled across **156 distinct declaration names**. Every set is a subset of `{propext, Classical.choice, Quot.sound}`. Both endpoints and **each of the 38 new wave theorems have exactly those three transitive axioms**. All 156 root queries are answered. Thus required transitive proof dependencies introduce no `sorryAx`, unsupported custom axiom, or native-reduction assumption. Source inspection and searches corroborate this: no `sorry`, `admit`, custom axiom, `native_decide`, unsafe/custom elaborator/macro/extern/implemented-by proof bypass occurs in the local closure. The only warnings are four inherited unused-variable warnings in Partial at lines 51, 171, 187, and 291; they are not unfinished goals.

The interruption is correctly classified. `I/recorder-attempt-1.raw.txt` records sixteen exit-zero Lean commands, followed by a **Python assertion** whose missing-name set is precisely `Finset.sum_nbij'`. The initial parser closed identifiers at any apostrophe. The corrected parser closes at the diagnostic phrase following the quoted name. My independent delimiter-based parser retains the internal apostrophe and reproduces its actual axiom set `{propext, Quot.sound}`. Original raw streams and their hashes are preserved. `all-commands-audit-v1.json` also correctly handles the Lake prefixes; the primary `audit-v1.json` diagnostic counts of zero for the two build logs reflect its narrower direct-output matcher, not absent checks. Use the complete all-commands reconciliation for those counts.

The expected unknown-name test proves only absence of two declaration names, not mathematical impossibility of the original conjecture. Earlier failed proof attempts, unavailable transport, the recorder interruption, and one corrected display-only Python syntax typo during this audit carry no negative mathematical inference. No Lean proof was changed or rerun because of these mechanical issues.

## 5. Eligible sources and disclosed trust — PASS

The fixed manifest SHA-256 is `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03`. All nine installed package revisions match it and have clean worktrees; nested manifests agree. Mathlib is exactly **`905b95818eb32af7874a58b427f50c1711a5e96c`**. Inherited `inputRev` branch labels do not replace these resolved immutable revisions; no update was performed.

I compared retained raw public-CI responses, exact `head_sha`, public repository flags, and creation times with `P/formal/environment/public-availability-witnesses.json`, not just commit dates. Mathlib and Lean have exact-SHA public witnesses on **2026-07-28**; the other packages have witnesses on **2026-07-13**, except LeanSearchClient on **2026-02-12**. All precede **2026-08-01**, satisfying the inclusive **2026-07-31** cutoff. The companion JSON records the ten concrete witness URLs/IDs. A CI failure label does not negate public availability and is not proof evidence.

`W/sources.md`, `REPRODUCE.md`, and `LEMMA_MAP.md` now exist in completed integrated form. They link the original preserved ledger and precise load-bearing source statements/guards. The complete source-import inventory has 4326 matching hashes, including 1983 library modules newly imported by the wave, 929 after FourPartial. Every external inventory record selects an eligible pinned revision with a matching retained witness. The inspected factorization, two-squares, Legendre-symbol and reciprocity declarations match these pinned sources. No current documentation, later revision, or new external mathematical source was used in this audit.

**Proof-route disclosure is correct:** the prose directly proves floor-parity and inverse-pairing arguments; Lean uses eligible quadratic reciprocity/supplements and Fermat two-squares instead, and implements the cyclic statement through bins/pigeonhole. Both final reviews explicitly check these alternatives. They are not statement drift, but one must not describe Lean as avoiding those library theorems or as formalizing every generic-function prose assertion line by line. Local deductions made after the cutoff are documented new work, not later external literature. The quarantined post-cutoff snippet and contextual Mangerel paper are not proof dependencies here.

The admitted foundational base is the three standard axioms above. The disclosed implementation trust includes the installed Lean kernel/compiler, Lake, elaborator/tactic implementations, and pinned imported `.olean`/cache artifacts. Same-pin cache acquisition is recorded; no cold bootstrap or full from-source rebuild of upstream libraries is claimed. Local trust-zero recompilation does not erase that imported-artifact boundary. Ordinary proof-producing tactics are distinguished from unsupported native proof oracles.

## 6. Two fresh final mathematical reviews — PASS

| Independent final review | Current/delivery SHA-256 | Coverage |
|---|---|---|
| `nl/reviews/final-four-review-a-v1.md` | `f8a73c44d01e7f8e09657c004341e73a86f7cff61707bdfc5e077aa5513542bd` | Complete standalone argument, exact Assembly and five dependencies, baseline reductions, pinned alternative routes; beginning/end mathematical hashes agree. Explicitly records the sole authorized root-import change and final root hash. |
| `nl/reviews/final-four-review-b-v1.md` | `7bf8a90a16d1b20a14142095892d11d23abb4deb8f82daf25aa7d46dfa6971c4` | Separately completed final-root review of the same mathematics, exact integrated root, source prerequisites and preserved raw formal evidence. Beginning/end hashes agree. |

Both reports are complete, scoped PASS reports, not placeholders or author-confidence statements. Both cover the exact integrated mathematical files, positivity, multiplicity, smallest cases, descent, cyclic strictness, residue reasoning, and final assembly. They explicitly distinguish mathematical review from kernel verification and exclude the all-even conjecture. A's durable complete report is valid evidence notwithstanding the later usage-limit tool-return error; no missing report was reconstructed. Its permitted import-only change does not invalidate review of unchanged mathematical content, and B independently reviews the final root.

Current report hashes match the recorded independent deliveries; there is no indicated author rewrite. Fresh anonymous synchronous dispatch and non-editing are supported by the supplied assignment and RUN/interruption record, not inferred from mathematical hashes alone. The earlier `descent-review-v1.md` is additional novel-proof evidence, **not** a replacement for either final review.

## 7. Evidence gaps, ledger corrections, and next assignments

**Evidence gaps blocking this lemma: none. Integration needs: none. Smallest remaining action: leader-owned publication/status reconciliation, not proof repair.**

Recommended record updates, without rewriting immutable historical evidence:

1. **Team-lead:** replace the pending final-audit/integrator-documentation checkpoint in `W/STATUS.md` and `W/HANDOFF.md` with this scoped PASS and the already completed `I/integration-report-v1.txt`. Append the completed integration checkpoint to RUN; its earlier scratch-promotion warning is historical. Update the parent summary only to add this accepted partial result, retaining the original conjecture's unresolved status.
2. **Team-lead:** distinguish historical pending fields in `I/audit-v1.json` from the later final-review deliveries and this regulator. The integration report already reconciles the two NL reviews. Preserve old raw reports, parser failures, and earlier partial-scope labels; do not rewrite them to pretend the complete lemma existed then. `FourWork`, `FourPartial`, and the unrelated original `UnfinishedScaffold` names are harmless historical labels, not current proof omissions.
3. **Proof specialists/integrator:** no repair or reintegration assignment is needed for these hashes. Any later semantic edit requires renewed affected readback/fidelity/mathematical and Lean checks; no cleanup is necessary for acceptance.
4. **Optional next mathematical wave, only if the leader continues the original problem:** route the residual all-even obligation to the NL sketcher and FL blueprinter. The accepted original prime-product reduction, together with this lemma, leaves the odd-prime-pair family `HasRepresentation (2*p*q)` as a precise next interface, with equal primes allowed. This is an unresolved research obligation, not a disproved proposition and not a condition on the now-accepted `4*m` theorem.

The leader may now report **success for every positive multiple of four**, under the stated standard Lean foundations and disclosed implementation trust. It must not report a proof of every even integer greater than two.
