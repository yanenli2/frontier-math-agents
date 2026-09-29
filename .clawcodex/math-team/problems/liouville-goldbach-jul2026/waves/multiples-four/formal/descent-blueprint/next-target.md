# Next-target recommendation

Mode: CERTIFICATION — recommendation only; no new theorem proved.

## Immediate decision

Approve/freeze the code-only `Readback.lean.txt` interfaces through fresh blind readback and source-fidelity comparison. Then use two proof slots with exclusive project scratch paths. The exact final statement stays unchanged.

**Highest-priority new lemma:** `ArithmeticStatement.FourWork.cyclic_short_multiple`. It is the only cross-worker proof dependency and the main formalization risk. Its signature requires `k≠0`, `k.natAbs<n`, `d>0`, and **`n*d<p`**. Prove it with the integer-bin/wraparound pigeonhole construction in `blueprint.md §6`, using the successfully probed finite-cardinality API. Do not start by building AddCircle or sorting circular gaps.

**Independent second target:** `prime_dvd_quarter_isSquare`, followed by `exists_small_prime_isSquare`. The exact pinned reciprocity APIs and parameter directions are audited in `api-audit.md §2`. This is a small number-theory module once its missing `.olean` is built; it does not depend on antireflection or character rigidity.

## Two-slot schedule and nonoverlap

Let `P=.clawcodex/math-team/problems/liouville-goldbach-jul2026`.

1. Current proof worker `flgenerator` owns only:
   - `P/lean/Statement/FourWork/Descent/Cyclic.lean`: G first;
   - `P/lean/Statement/FourWork/Descent/Ternary.lean`: A1–A6 next.
2. Recycle/re-dispatch the idle integrator slot as a second proof-generator role during proof production, owning only:
   - `P/lean/Statement/FourWork/Character/ResiduePrime.lean`: C1–C2;
   - `P/lean/Statement/FourWork/Character/ResidueValue.lean`: both new definitions and B1–B5;
   - `P/lean/Statement/FourWork/Character/Rigidity.lean`: B6–B8, after G is compiled.
3. Once both proof packages pass their checks, restore the integration role serially for:
   - `P/lean/Statement/FourWork/Reduction.lean`: mechanical importable copy of the fixed 19-helper candidate;
   - `P/lean/Statement/FourWork/Assembly.lean`: D1–D2 and audits.

No third persistent worker is needed. A substantial new proof should not be assigned to a worker still restricted to mechanical integration. These are proposed future ownership grants; the blueprinter has not created or edited anything in these paths.

The second worker can finish C and residue-value preliminaries while G is developed. B has the legitimate explicit full-antireflection premise from NL §4, so it does not wait for or import the A implementation. Only final D1 discharges that premise with A6. Do not introduce a temporary cyclic-short-multiple axiom or ship B with an extra unproved short-multiple hypothesis.

## Setup needed, not yet done

- `Mathlib.NumberTheory.LegendreSymbol.QuadraticReciprocity` source is present at the pin but its `.olean` is absent. Authorize a targeted same-pin build/cache step before compiling C, then `#check` and `#print axioms` the three reciprocity/supplementary APIs in the audit. Do not change the toolchain or dependency revision.
- `Real.exists_int_int_abs_mul_sub_le` genuinely has the useful `1/(N+1)` bound, but its module is also uncached. The recommended finite route does not need it.
- Use targeted `lake build Statement.FourWork.<...>` from `P/lean`; new scratch imports need built `.olean`s. There is no need to edit root `Statement.lean` during proof production.
- The fixed candidate hash is `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325`. Its core equivalence is not yet in `Statement.Partial`; preserve the candidate and require its outstanding review/integration gates before final use.

## Final assembly and acceptance

D1 assumes absence of the required representation, derives A6 antireflection, chooses a prime r from C2, applies B8 to get lambda(r)=1, and contradicts baseline `lambda_prime` at r. D2 uses `.mpr` of the existing `multiple_four_iff_prime_three_mod_four_core` and specializes to m, hm.

No full quadratic-character classification, FSPD, least residue prime, floor-count calculation, Wilson proof, generic sign-function library, or second all-m scaling proof is on the critical path.

Each implemented module needs:

- fresh statement readback/fidelity coverage of its exact declaration and new definitions;
- pinned source compilation and rebuilt dependency modules;
- no admitted obligations;
- `#print axioms` for exported helpers and final endpoints, without `sorryAx` or unsupported new axioms;
- recorded hashes and the actual build/import commands.

Current deliverable status: all 19 proposed proposition types elaborate as types; cached API probe passes; no proposed theorem has a proof here. The NL acceptance is unchanged. Remaining proof risks are strict cyclic bounds, exact ternary quotients, and avoiding circular modular multiplicativity; the concrete setup blocker is the uncached reciprocity module.
