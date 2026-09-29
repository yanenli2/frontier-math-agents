# Statement audit: representation_multiple_four, v1

Mode: CERTIFICATION — statement formalization and elaboration only. **No proof of the new lemma is supplied or claimed.** Independent statement acceptance is pending.

## Paths and scope

- Project root: `.`.
- `P`: `.clawcodex/math-team/problems/liouville-goldbach-jul2026`.
- `W`: `P/waves/multiples-four`.
- Owned checks/report: `W/formal/formalizer/`.
- Neutral snapshot: `.clawcodex/math-team/review-inputs/r20260924-four-v1/`.

Read the assigned continuation request, original request, protocol, Lean workflow, actual master definitions, actual pinned standard definitions, and prior neutral code supplements. No proof search, proof construction for the requested lemma, baseline rebuild, dependency download, tool/config change, or master edit was performed.

## Exact declaration and source map

The body-erased scaffold is `Declaration.lean` in the neutral snapshot. Its new declaration, inside `namespace ArithmeticStatement`, is exactly:

```lean
theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :
  HasRepresentation (4 * m)
```

This is a theorem *signature*, not a registered proved theorem. The file intentionally has no proof body and is not a standalone compilable theorem module. No `sorry`, `admit`, or replacement axiom is inserted.

| Source locator | Encoding | Neutral locator |
|---|---|---|
| `W/request.md:3,7–14`, every positive multiple of 4 | Explicit `m : ℕ`, explicit `hm : 0 < m`, result at `4 * m` | `Declaration.lean:17–18` |
| `P/request.md:7`, prime-factor count with multiplicity | Existing `ArithmeticStatement.omega`; `P/lean/Statement/Definitions.lean:6` | `Declaration.lean:5` |
| `P/request.md:7`, signed power | Existing `ArithmeticStatement.lambda`; `Definitions.lean:8` | `Declaration.lean:7` |
| `P/request.md:10–14`; `W/request.md:14`, positive summands, exact sum, both signs | Existing `HasSignedRepresentation`; `P/lean/Statement/Partial.lean:14–17` | `Declaration.lean:9–12` |
| `W/request.md:10–14`, sign exactly −1 | Existing `HasRepresentation`; `Partial.lean:19–20` | `Declaration.lean:14–15` |

`run-check.py` verified byte-for-byte equality of all four copied custom definitions against these master source ranges. The only custom definitions in the neutral packet are the transitive closure

`HasRepresentation → HasSignedRepresentation → lambda → omega`.

The new declaration is not a redefinition of `Target` and does not replace the original all-even problem.

## Literal meaning and translation decisions

The proposition, with definitions expanded, is:

```lean
∀ (m : ℕ), 0 < m →
  ∃ a b : ℕ,
    0 < a ∧ 0 < b ∧ 4 * m = a + b ∧
      (-1 : ℤ) ^ a.primeFactorsList.length = (-1 : ℤ) ∧
      (-1 : ℤ) ^ b.primeFactorsList.length = (-1 : ℤ)
```

1. Quantifier order is universal `m`, positivity hypothesis, then existential `a,b`. The witnesses may depend on `m`; no uniform pair, threshold, or aggregate statement is substituted.
2. Positive integers use the already approved representation as naturals with strict positivity. Every positive integer has exactly one such natural value. `4 * m`, `a + b`, and inequalities are in `ℕ`; only the values of `lambda` and its base/sign are in `ℤ`.
3. The theorem has no other assumptions: no parity or sign of `m`, no primality, no coprimality, no distinctness, no inequality ordering the summands. The only guard is `0 < m`, not `1 < m`.
4. For positive `m`, `4 * m` is at least 4 and is an even integer greater than 2. Thus the requested domain is a subfamily of the original domain, not a revised all-even conjecture. An explicit `Even (4 * m)` premise would be unnecessary and is not added.
5. The equality orientation remains `4 * m = a + b`. Separate conjunctions express both equations `lambda a = -1` and `lambda b = -1`; this is not a product-sign condition.
6. `omega` is the existing identifier for the source's uppercase Ω, not a distinct-prime-factor counting function. Existing `def`s remain `def`s. The new assertion is a theorem signature; the compiled scratch interface is only a `def ... : Prop`, not a theorem inhabitant or an axiom.
7. No material ambiguity remains in the dispatched statement: `W/request.md:14` explicitly fixes `m=1`, positive witnesses, equal witnesses, and absence of extra restrictions. Independent fidelity approval is still required.

## Actual definition audit

The master files were inspected directly; the compiler's loaded versions are also printed in `Check.stdout:1–12`.

- **Representation expansion:** `HasRepresentation N` is definitionally `HasSignedRepresentation (-1 : ℤ) N`, hence exactly the two positive existential witnesses and five conjunction fields displayed above. Two `#check` conversions, using only a supplied hypothesis, elaborate in both directions (`Check.stdout:13–22`). No intermediate equivalence theorem or representation theorem is needed.
- **Multiplicity:** pinned Mathlib `Mathlib/Data/Nat/Factors.lean:38–44` recursively prepends `Nat.minFac n` and continues on `n / minFac n`. There is no deduplication. `prime_of_mem_primeFactorsList` at 55–65 says each entry is prime; `prod_primeFactorsList` at 70–81 recovers `n` under the explicit guard `n ≠ 0`; `Prime.primeFactorsList_pow` at 181–187 gives `List.replicate n p`. These are definition-audit facts, not a proof route for the new lemma.
- **Factor extraction:** `Mathlib/Data/Nat/Prime/Defs.lean:207–219` gives `minFacAux` and `minFac`; the standard specifications used by the prior neutral supplement are at 107, 287–300. The termination justifications are omitted only in the body-erased review excerpts, not changed in the imported library.
- **List cardinality:** pinned Lean `src/Init/Prelude.lean:3027–3029` defines list length by one increment per cons; `src/Init/Data/List/Basic.lean:84–90,705–707` gives the length equations and replication. Repeated factors therefore contribute repeatedly.
- **One:** `primeFactorsList 1 = []` (Factors:49–50); the actual scratch evaluations returned `[]`, `omega 1 = 0`, and `lambda 1 = 1`. This matches Ω(1)=0 exactly.
- **Signed codomain:** `lambda : ℕ → ℤ` uses `(-1 : ℤ) ^ omega n`, not natural subtraction. Pinned Lean `src/Init/Data/Int/Basic.lean:400–405` supplies the integer power operation. Negative one is represented as an integer, not truncated to zero.
- **Zero:** the inherited totalization also has `primeFactorsList 0 = []`; it is not used to admit zero summands. The two explicit inequalities exclude `a=0` and `b=0`, and `hm` excludes `m=0`. No new zero convention was introduced.

## Positivity, smallest case, and equal witnesses

These are fixed definition/interface checks, not a search or a general proof.

- The compiled interface still prints `∀ (m : ℕ), 0 < m → ...` (`Interface.stdout:6–7`). It does not silently discharge the hypothesis.
- Specialization of a *supplied* inhabitant of that proposition at `m=1` elaborates as `statement → 0 < 1 → HasRepresentation 4` (`Interface.stdout:12–14`). The fixed evaluation of `0 < 1` is `true`; `0 < 0` is `false`.
- `Check.lean` typechecks the literal constructor with the same natural `a` twice under supplied assumptions `0 < a` and `lambda a = -1`. Its displayed type is `∀ a, 0 < a → lambda a = -1 → HasRepresentation (a+a)` (`Check.stdout:23–25`). Thus the actual predicate permits equal witnesses; this is not just an informal convention.
- The single prescribed boundary witness `(a,b)=(2,2)` at `m=1` was evaluated directly: both witnesses are positive, `4*1=2+2`, and `lambda 2=-1`; the conjunction evaluates to `true`. This is a fixed diagnostic, not enumeration and not a kernel proof of the universal lemma.
- The fixed multiplicity check returned `primeFactorsList 4 = [2,2]`, `omega 4 = 2`, `lambda 4 = 1`. Only the specified small values 0, 1, 2, and 4 are involved in these checks.

## Neutral packet isolation

Only these three code-only files are in the new neutral directory:

1. `Declaration.lean`: exact body-erased theorem signature and the four transitive custom definitions, with a standard Mathlib import. No original `Target`, auxiliary project lemmas, proof bodies, source-intent comments, proof plans, or previous verdicts.
2. `Dependencies.lean`: exact copy of lines 5–53 of prior neutral `r20260924-v1/Dependencies.lean`, containing standard factor definitions and body-erased standard specifications.
3. `ListOperations.lean`: byte-for-byte copy of the prior neutral file of the same name.

The unused prior `Even` definition and its universe declaration were not copied: `Even` is not in the new theorem's transitive custom-definition closure. Its unused import is likewise not retained in the neutral excerpt. No approved definition is altered by this omission. The original masters keep all their original imports.

The neutral excerpts are for readback, not compilation units: standard theorem proof bodies and recursive termination proofs are intentionally absent. The live elaboration checks instead import the existing `Statement.Partial` module. Text scans found no comments, proof-body marker `:= by`, `sorry`, `admit`, or axiom declaration in the neutral packet. The new scratch Lean files have no admissions or axiom declarations either. Do not give this audit, the scratch checks, original requests, or earlier readback reports to the blind reader.

## Toolchain, commands, diagnostics, and immutability

Actual working directory for the Lean checks:

`.clawcodex/math-team/problems/liouville-goldbach-jul2026/lean`

Actual commands and outcomes:

```text
lake env lean --version
exit 0: Lean 4.32.2, commit f3b06c705e6c85f5314019d5d3baab0fec5b580c

lean --print-prefix
exit 0: ~/.elan/toolchains/leanprover--lean4---v4.32.2

lake env lean .clawcodex/math-team/problems/liouville-goldbach-jul2026/waves/multiples-four/formal/formalizer/Interface.lean
exit 0

lake env lean .clawcodex/math-team/problems/liouville-goldbach-jul2026/waves/multiples-four/formal/formalizer/Check.lean
exit 0
```

Reproducible runner, executed from the same cwd:

```text
python3 .clawcodex/math-team/problems/liouville-goldbach-jul2026/waves/multiples-four/formal/formalizer/run-check.py
exit 0
```

`check-record.json` records each command, actual absolute cwd, exit status, stdout/stderr, pin comparison, and before/after hashes. Raw Lean output is also in `Interface.stdout`, `Interface.stderr`, `Check.stdout`, `Check.stderr`.

The interface has one harmless linter warning that binder name `hm` is not referenced in its conclusion. Its hypothesis is retained in the printed proposition; no lint suppression or binder change was made. Both stderr files are empty. `Check.lean` has no warnings/errors.

`#print axioms` reports `[propext, Classical.choice, Quot.sound]` for each of the four imported custom definitions and the proposition-valued interface. There is no `sorryAx` in these reported dependency closures. This is **not** an axiom audit of a proof of `representation_multiple_four`: that proof does not exist in these artifacts, and no such theorem is added to Lean's environment.

The runner checked all nine package HEADs against `lake-manifest.json`; all match, with no tracked modifications. Mathlib HEAD is `905b95818eb32af7874a58b427f50c1711a5e96c`. All eight source identities from the existing `formal/environment/source-file-identities.json` match their recorded SHA-256 values. Master sources, pin files, cached `Definitions.olean`/`Partial.olean`, their Lake traces, and prior neutral inputs are unchanged before/after the checks. Importing the cached baseline is not a fresh certification of its already-checked proofs; no `lake build` or compilation of either master was run.

One preliminary nonessential tag-name diagnostic failed, and is disclosed rather than treated as a pin failure. From the same Lean cwd the actual chained command was:

```text
lake env lean --version && lean --print-prefix && git -C .lake/packages/mathlib show -s --format='%H%n%aI%n%cI%n%s' HEAD && git -C .lake/packages/mathlib describe --tags --exact-match HEAD
```

The chain exited 128 at the final `git describe`, with `fatal: No names found, cannot describe anything.` The preceding checks succeeded and printed the pinned SHA and commit date `2026-07-28T18:36:13+02:00`. The checkout has no locally available tag names; the independently checked immutable SHA, not a tag lookup, is the required pin. All commands in the subsequently saved `check-record.json` exited 0.

## Cutoff and provenance

Only existing local pinned sources were used. No network fetch or later library/theorem source was consulted. Existing `P/sources.md:5–37` records release/public-workflow evidence for Lean v4.32.2 and the pinned Mathlib release on 2026-07-28, and each transitive package's exact-SHA public witness before 2026-07-31. This pass rechecked the local versions/bytes against that existing evidence; it did not perform a new external availability audit. Mathematical source locators are in the definition audit above; exact inspected source hashes are in `check-record.json`. No external analytic theorem is used.

## Snapshot identities

SHA-256:

| File | Hash |
|---|---|
| Neutral `Declaration.lean` | `bdfb30bcfade7b9df33e48f280125d10a40dd76f365cf5b87047183475fee7ed` |
| Neutral `Dependencies.lean` | `fd4ec312622db449d27d6ac0b18b1decd62a9f76e18f8251bb40ffbabdef7981` |
| Neutral `ListOperations.lean` | `925cbf08a1aac0870075ad56ff2d95c7b0eb94c87853ace32d0043a9c094e2bc` |
| Scratch `Interface.lean` | `d8d4a87650d077b5b28f289055a0f11e58f9579c73b5343c5fa6a0748a27ea7d` |
| Scratch `Check.lean` | `dd7cda0504cb56099a4a1c2f0430e4fd59da03b351d8af156467e7009ef05039` |
| Master `Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| Master `Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |

`check-record.json` also hashes both source requests, prior neutral inputs, checked standard sources, compiled baseline interfaces/traces, runner, and diagnostics. `snapshot.sha256` additionally identifies this report and the command record.

## Independent review request and remaining obligation

Request to `team-lead`: dispatch a fresh blind statement reader with **only** the three exact neutral file paths above and a private output path. Then obtain a separate fresh formal fidelity review comparing that literal readback and frozen declaration with `W/request.md`, `P/request.md`, and the approved definitions. This author audit is not either independent review.

The sole new mathematical target remains entirely unproved: construct an inhabitant of `∀ (m : ℕ), 0 < m → ArithmeticStatement.HasRepresentation (4 * m)`. No proof plan is proposed in this statement-only assignment. Do not integrate a theorem or report mathematical success from these elaboration checks. Any change to the frozen declaration or defining dependencies requires a separate documented revision, fresh readback/fidelity review, and a new snapshot. The original all-even conjecture and earlier accepted artifacts remain untouched.
