# Multiples-of-four lemma — PROVED AND ACCEPTED

All requested mathematical, statement-fidelity, Lean, integration, source-cutoff, and final-review gates for this lemma have passed. No mathematical or formal obligation remains for the positive-multiples-of-four result. The original all-even conjecture remains unresolved.

## Exact accepted theorem

```lean
theorem ArithmeticStatement.representation_multiple_four
    (m : ℕ) (hm : 0 < m) :
    ArithmeticStatement.HasRepresentation (4 * m)
```

This gives, for every positive integer m, positive a,b with 4m=a+b and lambda(a)=lambda(b)=-1. Equal summands and m=1 are included; there is no extra condition on m or the witnesses. Master: `../../lean/Statement/FourWork/Assembly.lean:21–24`, available through `import Statement`.

## Frozen identities

- `PROOF.md`: `205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b`.
- `Statement/FourWork/Assembly.lean`: `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066`.
- Root `Statement.lean`: `cd6a1dd9bff63ef400559805123c5e6cb7d2d4c9af28cf7f7c24f2cc640abc3c`, imports Assembly.
- Original Definitions/Partial and FourPartial remain unchanged; all dependency hashes are recorded in the integrated evidence and final reviews.

## Acceptance evidence

- Isolated statement readbacks and independent fidelity reviews cover the exact endpoint, all 38 new wave theorem signatures, and relevant definitions. See `formal/reviews/` and `formal/descent-blueprint/Readback.lean.txt`.
- Independent exact full-candidate check: `formal/reviews/full-candidate-review-v1.md` and raw companion files.
- Integrator-only promotion: `formal/integration-full/integration-report-v1.txt`. Its only proof-graph edit was the root import; all mathematical source bytes were preserved.
- Actual default build, explicit Assembly build, direct source check, trust-zero checks of all 12 local modules, and root-only expanded-type/axiom checks passed. Raw commands, exit statuses, diagnostics and hashes are in `formal/integration-full/`.
- All 38 new theorem transitive axiom sets are exactly `propext`, `Classical.choice`, `Quot.sound`. All 156 queried axiom sets are subsets of that base. No sorry/admit/sorryAx, unsupported custom axiom, native proof assumption, or circular endpoint premise remains in the accepted closure.
- Two fresh final mathematics reviews PASS: `nl/reviews/final-four-review-a-v1.md` and `final-four-review-b-v1.md`. Both cover the same exact mathematical files and their Lean alternatives. Review A's complete durable report survived an interrupted tool return and was recovered without edits.
- **Final regulator PASS:** `formal/reviews/final-four-regulator-v1.md`, with independent mechanical evidence in its companion JSON. It finds no mathematical, formal, integration or source-provenance blocker.

Lean v4.32.2 and Mathlib `905b95818eb32af7874a58b427f50c1711a5e96c`, together with all original dependency pins, meet the inclusive 2026-07-31 source cutoff. New imports use the same eligible revision. Compiler/kernel and pinned compiled-library artifact trust is disclosed; no full from-source Mathlib rebuild is claimed. See `sources.md` and `REPRODUCE.md`.

## Records, history and scope

`PROOF.md` contains the standalone argument. `LEMMA_MAP.md` links informal steps to exact declarations, dependencies, provenance and reviews. `HANDOFF.md` preserves the accepted restart baseline. Historical pending fields in integration audit JSON and earlier partial-scope records are superseded by the completed integration report, the two final NL reviews and the final regulator; immutable evidence is not rewritten. The recorded apostrophe-name parser failure was mechanical and was fixed without changing any proof or rerunning passed builds.

Earlier seed/partner/square-shift and norm-form explorations are preserved but are not premises of the final uniform proof. No finite computation establishes the theorem; the universal proof is Lean-checked. The names FourWork/FourPartial and the original uninhabited UnfinishedScaffold are historical labels, not gaps in this lemma.

## Team and next work

Team-lead `tcp9ou0cy` has accepted the result. fl-generator `tw05jhslm` and fl-integrator-final `tdkudsui0` are idle and available; no further work is assigned. Final integration task047e2ef62825 and lead acceptance task79921be483cb are complete. The team remains available with at most two persistent workers.

The original theorem for every even N>2 has not been proved. Any further mathematical wave or any semantic alteration to this accepted baseline needs a new assignment and the corresponding fresh review/checking gates. No commit or publication was requested or made.

Publication checkpoint (2026-09-27, before PR creation): the no-commit/no-publication statements above describe the earlier acceptance checkpoint. The scoped private archive and release metadata have since been committed and pushed on `proof/liouville-multiples-four` through `58eb98d95714b79e8abcdcdda33fe2f4abcda9f1` (VERSION `0.1.0.0`). No PR existed at this checkpoint; no merge or deployment was performed.
