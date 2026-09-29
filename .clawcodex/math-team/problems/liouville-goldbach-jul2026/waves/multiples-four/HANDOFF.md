# Accepted multiples-of-four theorem: handoff

## Outcome

The user's lemma is **PROVED AND ACCEPTED**, including faithful Lean checking and final independent reviews:

```lean
theorem ArithmeticStatement.representation_multiple_four
    (m : ℕ) (hm : 0 < m) :
    ArithmeticStatement.HasRepresentation (4 * m)
```

This means positive a,b exist with 4m=a+b and both Liouville signs -1 for every m>0. Multiplicity, lambda(1)=1, m=1 and equal witnesses are preserved. No extra premise remains. The original all-even Target is not proved by this result.

## Protected accepted baseline

- Actual theorem: `../../lean/Statement/FourWork/Assembly.lean:21–24`; SHA-256 `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066`.
- Standalone exposition: `PROOF.md`; SHA-256 `205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b`.
- Default root: `../../lean/Statement.lean`; SHA-256 `cd6a1dd9bff63ef400559805123c5e6cb7d2d4c9af28cf7f7c24f2cc640abc3c`; imports Assembly.
- Definitions: `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d`.
- Original Partial: `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0`.
- FourPartial: `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325`.
- Five Descent/Character dependency modules and all source identities: `formal/integration-full/artifact-hashes-v1.json` and final regulator JSON.

Do not change mathematical source, defining dependencies, or accepted statements without renewed affected fidelity/readback, mathematical review, compilation and axiom checks. No golf or cleanup is required for acceptance.

## Evidence to retain

1. Exact statement/helper snapshots and isolated readbacks; `formal/reviews/*fidelity*` and `full-candidate-review-v1.md`.
2. `formal/integration-full/integration-report-v1.txt`, `audit-v1.json`, `all-commands-audit-v1.json`, and all raw command streams. Default/explicit/direct/trust-zero/root-import checks passed; actual final type was unfolded and checked.
3. Fresh final NL reviews `nl/reviews/final-four-review-a-v1.md` and `final-four-review-b-v1.md`. Both exact mathematical snapshots passed. A's complete report survived a later transport/usage-limit return; the final regulator explicitly accepts its preserved evidence and scope.
4. **Final acceptance audit:** `formal/reviews/final-four-regulator-v1.md` and companion JSON. Verdict PASS, no remaining blocker. Every one of the 38 new theorem signatures is preserved and every new theorem uses only standard propext, Classical.choice and Quot.sound. All 156 queried declarations have no prohibited transitive assumption.
5. `REPRODUCE.md`, `sources.md`, `LEMMA_MAP.md`, and `PROOF.md` provide reproduction, exact provenance, informal/formal dependency mapping and full exposition.

The failed parser for `Finset.sum_nbij'` was an evidence-recorder error, not a Lean failure. It was corrected against preserved passing output; no mathematical file changed and no passing build was rerun. Earlier pending fields and partial-result records are historical; this handoff and final regulator supersede their progress labels without rewriting their bytes.

## Environment and provenance

Lean v4.32.2, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`; Mathlib `905b95818eb32af7874a58b427f50c1711a5e96c`. All nine packages remain locked to the original manifest. The inclusive 2026-07-31 cutoff applies to every external mathematical version. Preserved exact-SHA public records and source inventories support eligibility. No later literature is a premise; the originally encountered post-cutoff snippet remains excluded.

Trusted mechanisms are the standard Lean foundations, installed compiler/kernel, Lake and pinned imported compiled artifacts. Local trust-zero checks were run, but no independent kernel implementation or full cold-source rebuild of upstream libraries is claimed. Reproduce using the recorded commands; there is no need to repeat passing checks merely to restate this result.

## Runtime and possible next wave

Team math-team, leader tcp9ou0cy. fl-generator tw05jhslm and fl-integrator-final tdkudsui0 are idle and available. Integration task047e2ef62825 and acceptance task79921be483cb are completed. At most two persistent workers; fresh anonymous synchronous reviewers were used. No further work or team shutdown is assigned. On process restart, inspect actual runtime rather than treating team.json as live ownership.

If the user later resumes the original all-even problem, this lemma handles all multiples of four. The existing prime-product reduction suggests the remaining odd-prime-pair cases `HasRepresentation (2*p*q)` as a research direction, with equality p=q permitted; no new proof of that remaining universal family is supplied here. Do not restart it automatically or recast it as a premise of the now-proved lemma.

All files remain local and uncommitted; no push or publication was requested. Do not delete dependency/evidence directories as cleanup without authorization.

Publication checkpoint (2026-09-27, before PR creation): the no-commit/no-publication statements above describe the earlier acceptance checkpoint. The scoped private archive and release metadata have since been committed and pushed on `proof/liouville-multiples-four` through `58eb98d95714b79e8abcdcdda33fe2f4abcda9f1` (VERSION `0.1.0.0`). No PR existed at this checkpoint; no merge or deployment was performed.
