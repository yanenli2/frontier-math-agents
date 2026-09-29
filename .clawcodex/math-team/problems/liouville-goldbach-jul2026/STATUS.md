# Status: PARTIAL; original target UNRESOLVED

No faithful full theorem proof has been obtained. `ArithmeticStatement.Target` remains a proposition definition without an inhabitant supplied by this project. Neither `ArithmeticStatement.liouville_goldbach` nor `ArithmeticStatement.pointwise_keystone` is declared in the build. There is no claimed counterexample.

## Accepted continuation: every positive multiple of four

The user-requested lemma `∀ m>0, HasRepresentation (4*m)` is now **proved, Lean-checked, integrated, and accepted after two fresh final mathematics reviews and a final regulator audit**. The actual theorem is `ArithmeticStatement.representation_multiple_four` at `lean/Statement/FourWork/Assembly.lean:21–24`, available through the default root import. There is no extra premise on m or its positive summands; equal summands are allowed.

The [wave status](waves/multiples-four/STATUS.md), [full proof](waves/multiples-four/PROOF.md), [reproduction instructions](waves/multiples-four/REPRODUCE.md), and [final regulator](waves/multiples-four/formal/reviews/final-four-regulator-v1.md) bind the exact accepted result. This remains a partial result for the original all-even Target, which is not proved. Earlier final-review/build hashes below identify the preserved first-wave baseline; the current root additionally imports the accepted continuation modules.

## Checked and integrated results

Pinned Lean v4.32.2 and Mathlib `905b95818eb32af7874a58b427f50c1711a5e96c`, with all dependencies cutoff-audited. Master `lean/Statement/Partial.lean` contains 42 theorems and eight helper definitions. It is imported by the default root build and has SHA-256 `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0`.

Principal results:
- Required representation for every N=8m with m>0.
- Diagonal representation for every even N>2 with lambda(N)=1.
- Exact integer identity `4*(R N : ℤ) = ((N : ℤ)-1)-2*L(N-1)+C N`, for every N≥2. R counts actual ordered positive pairs, including the diagonal once.
- Count/existence and strict-inequality equivalences.
- Exact equivalence of Target with required representations of all `2*p*q`, for arbitrary primes p,q including equality.

These partial families and reductions do not prove either universal missing premise. Complete per-lemma definitions, dependencies, provenance and evidence: [LEMMA_MAP.md](LEMMA_MAP.md).

## Actual evidence

- Independent blind readbacks and statement reviews preserve the exact positive-natural normalization, multiplicity and signed codomain; see `formal/reviews/` and neutral `../../review-inputs/r20260924-v1/`.
- Exact candidate review: `formal/reviews/candidate-audit-v1.md` with independent compile/axiom logs.
- Integration: default build, explicit module build, direct Lean, trust-zero Lean, and root-import checks all exit 0; `formal/integration/audit-v1.json` and `v1-*` records.
- All 42 theorem axiom sets contain only `propext`, `Classical.choice`, `Quot.sound`; no admitted obligations, custom mathematical axioms, or native-evaluation assumptions in accepted closure.
- Self-contained exposition `FINAL_ARGUMENT.md`, hash `1b93364b818b0eae95875d391ca6f944614f00b963a1e384ba1a0fe2533957a9`, has two fresh final reviews: `nl/reviews/final-review-a-v2.md` (PASS for exact partial argument) and `final-review-b-v1.md` (no partial defect; original request UNRESOLVED).
- Earlier final-review-a-v1 is not counted: its metadata drift/exposure qualifications were resolved through metadata-only reconciliation and new clean reviewer packets. Lean/mathematics did not change.
- Final formal-regulator audit `formal/reviews/final-regulator-v1.md` ACCEPTS the documented partial wave, with no remaining mechanical blocker. Its JSON preserves the mechanical evidence. It explicitly leaves the original Target UNRESOLVED.
- Historical metadata annotation: frozen `sources.md` retains its earlier extraction-review “pending” wording, but extraction is now complete and the source distinction is covered by both final reviews. The candidate audit's older source-ledger hash describes its historical snapshot, not the final ledger. The final reviews and regulator bind the current frozen ledger hash `9df552348f03fd84ffe0e203f1340f26e6a902f8424f924068fe6fb86c1a7dbb`. These annotations supersede stale progress wording without changing reviewed snapshots.

## Exact unresolved goals

```lean
N : ℕ
hEven : Even N
hN : 2 < N
⊢ 2 * ArithmeticStatement.L (N - 1) - ((N : ℤ) - 1) < ArithmeticStatement.C N
```

Equivalently:

```lean
⊢ ∀ p q : ℕ, Nat.Prime p → Nat.Prime q →
    ArithmeticStatement.HasRepresentation (2 * p * q)
```

Neither is a missing tactic/library lemma: both are genuine remaining mathematical claims. There is no effective sufficiently-large threshold with a complete checked finite remainder.

## Rejected/limited approaches and next branches

1. Optional O-M5, `L(q-1)<0` for every prime q≥5, is refuted at q=5, L(4)=0. Do not use it.
2. Fixed finite seed/common-scaling methods and small partner/square-shift menus have scoped obstructions; these do not refute Target. Expanded bounded searches do not create a uniform construction.
3. Prime-indexed bridge PB (positive-positive pair at 2q for every prime q≥5) and the LS/LS-square shift routes remain unproved sufficient routes. A new uniform argument is needed, not another finite table.
4. Mangerel arXiv:2404.12117v2, 2024-05-02, proves a different eventual correlation result with an ineffective threshold. Remark 2 poses this exact target. No analytic result is a Lean proof dependency. Bounded follow-up searches do not establish a literature-wide open-status claim.

Finite Python audit: 255 identity cases N=2..256 and explicit template examples, 1260 assertions, no failures; not Lean-certified and not a universal proof. Its historical PB-label mapping remains unverified and irrelevant to accepted theorems.

## Persistence and live owners

`REPRODUCE.md` records exact pins, theorem names and actual commands. `sources.md` records dates, versions, source locators and the excluded accidentally returned post-cutoff snippet. `HANDOFF.md` records the restart point. At most two persistent workers were live; currently fl-generator (`tw05jhslm`) and fl-integrator-final (`tdkudsui0`) are idle after completing the multiples-of-four wave. The team remains available; no shutdown of the whole team was requested.
