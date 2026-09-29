# Full exact-candidate formal review v1

Mode: CERTIFICATION

**VERDICT: APPROVE — exact candidate, not integrated-root publication.**

The frozen candidate proves the requested representation theorem for **every positive natural multiplier**, including `m = 1`. No statement mismatch, admitted proof obligation, unsupported axiom, residual nonrepresentation/antireflection premise, or unverified mathematical source version was found in the reviewed candidate. **The exact declarations and defining dependencies may be protected for proof/integration work.** No candidate repair is requested.

This is a fresh, one-shot formal review. I read the required protocol and Lean workflow, the supplied source/signature snapshots, the neutral literal readback, the actual code, and local source-provenance records. I did not read prior formal/mathematical reviewer reports, edit declarations, author proofs, invoke agents, or touch task/team state. The literal readback was used for its formulas and qualifications, not as proof evidence.

## 1. Scope and frozen identities

Here `P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`, `W = P/waves/multiples-four`, and local Lean paths below are relative to `P/lean`.

| Input | SHA-256 |
|---|---|
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `W/PROOF.md` | `205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b` |
| `Statement/FourWork/Assembly.lean` | `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066` |
| `Statement/FourWork/Descent/Cyclic.lean` | `09fbee47a60bf7db94d65e871fc49f5d07d60838c8b01cfbfdecb53033471290` |
| `Statement/FourWork/Descent/Ternary.lean` | `d6f231fc9aa372f562b19170268b31ae16bdca178185256131232011fd255753` |
| `Statement/FourWork/Character/ResiduePrime.lean` | `518f28a33ab98d1a44ea7b544ca7f695e28c48893982caaf72eb4879956763dd` |
| `Statement/FourWork/Character/ResidueValue.lean` | `3df5a3f0a6de6a60c2b8b8ba89dd6e44fa4d47cb28e98c33f1e31d1dfb7d84dd` |
| `Statement/FourWork/Character/Rigidity.lean` | `843e4ee562071ef4729a61c715b77510b378add7f19b8c02d1e3d36fa9165f88` |
| `Statement/FourPartial.lean` | `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325` |
| `Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `W/formal/descent-blueprint/Readback.lean.txt` | `372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763` |
| `W/formal/approved-v1/Declaration.lean` | `bdfb30bcfade7b9df33e48f280125d10a40dd76f365cf5b87047183475fee7ed` |
| `W/formal/generator/four-interfaces-v1.lean` | `be55b4df2e640ec4645a2544b0013de5d6f366439162820af4233162766a0cee` |
| Neutral `r20260924-four-v1/descent-readback.md` | `460c911b32d72948da676c52e3f0edba52ad724aa505bd4d650b94375165e6ab` |
| `Statement.lean` | `dc72b845dbb045593ef3a6212b03a54cc0797a29baac132e870aff324cdc5853` |

All dispatched full hashes match; the abbreviated old-definition hashes also match. The neutral `DescentInterfaces.lean.txt` has the same bytes/hash as the supplied full-signature snapshot. The complete 24-file begin/end inventory includes the original request, configuration, and neutral modular definitions. Eleven additional provenance/library source files were also hashed and rechecked. **No change was detected**; all nine package revisions remained unchanged with no tracked modifications. Evidence: `full-candidate-review-v1.snapshot-{begin,end}.json` and `.provenance.json`.

The final declaration header, after removing whitespace only, has SHA-256 `cf97da2e3c43201a99605f2385942bb2abd7c3ba8a9377a4f5899bf01fc1c9e4`. Per-declaration header/definition hashes, exact text, and source locations are recorded in `.signatures.json`.

## 2. Exact target and definitions

Source locators: `W/request.md:7–16`; `W/PROOF.md:3–17,481–485`; original `P/request.md:7–27` for conventions/cutoff. Approved target: `approved-v1/Declaration.lean:5–18`. Actual endpoint: `Assembly.lean:21–24`.

Literal final claim:

```text
∀ m : ℕ, 0 < m →
  ∃ a b : ℕ, 0 < a ∧ 0 < b ∧ 4*m = a+b ∧ λ(a)=-1 ∧ λ(b)=-1.
```

Witnesses are chosen after `m`; no common pair, distinctness, parity, coprimality, primality, or sign condition on `m` is added. There is no threshold beyond positivity. Both signs are required individually, not merely their product or an average. No extra section variables or typeclass parameters appear in the elaborated endpoint (`.types2.log:78–80,165–169`).

The defining chain is unchanged:

- `Definitions.lean:6–8`: `omega n = n.primeFactorsList.length`, `lambda n = (-1 : ℤ)^omega n`.
- `Partial.lean:14–20`: positive natural witnesses with exact sum and both prescribed integer signs; `HasRepresentation` specializes the sign to `-1`.
- Pinned Mathlib `Data/Nat/Factors.lean:38–44,55–88,167–187,196–202`: recursive extraction of a least prime factor, prime entries, product equal to each nonzero input, uniqueness, repeated prime powers, and concatenation for multiplication. This counts factors **with multiplicity**, without a coprimality hypothesis.
- `Data/Nat/Prime/Defs.lean:42–43,107–112,207–219,287–303` identifies primality and the least-prime-factor operation. The compiled definitions were also printed, not inferred from names.

Thus this is the true positive-argument Liouville function. Empty factorization gives `λ(1)=1`; the totalization also gives `λ(0)=1`, but no zero representation witness or zero-argument multiplicativity is used.

The two new definitions match the snapshot exactly: `ResidueValue.lean:9–14` versus `Readback.lean.txt:23–28`. `residueLambda p z = lambda z.val`; `GoodMultiplier p a` includes **both** `a ≠ 0` and the multiplication identity for every nonzero `z`. Pinned `ZMod`/`.val` definitions give least representatives for positive modulus, and absolute value for modulus zero. `IsSquare t` means `∃ r, t=r*r` in its specified multiplication type (`Algebra/Group/Even.lean:53–57`), here `ZMod p`, not an ordinary natural square. Extending `residueLambda` to zero residues does not enlarge the domain of any asserted nonzero-residue multiplication law.

## 3. All full signatures and older interfaces

Whitespace-only comparison found **19/19 full theorem signatures and 6/6 definitions identical**, including the four original definitions and the two new definitions. All 19 older helper signatures also match. Actual elaborated types were independently printed with `#check @...`; no extra implicit hypotheses appeared.

In this table `R` denotes `W/formal/descent-blueprint/Readback.lean.txt`; proof sections/line references denote `W/PROOF.md`. Each row passed.

| Declaration | Approved lines | Actual header | Source intent |
|---|---:|---|---|
| `lambda_reflection_eq_one_of_neg` | R 30–33 | Ternary 8–11 | (A), 119–125 |
| `lambda_double_reflection_eq_neg_one_of_pos` | R 35–38 | Ternary 22–25 | (C), 126–131 |
| `three_not_dvd_of_positive_pair` | R 40–44 | Ternary 36–40 | §4.1 |
| `positive_pair_gap_step` | R 46–52 | Ternary 56–62 | §§4.2–4.3 |
| `no_positive_pair` | R 54–58 | Ternary 103–107 | §4.3 |
| `lambda_antireflection_of_no_representation` | R 60–63 | Ternary 124–127 | (9), 215–219 |
| `cyclic_short_multiple` | R 65–69 | Cyclic 10–14 | (13), §5.1 |
| `residueLambda_natCast` | R 71–72 | ResidueValue 16–17 | 225–233 |
| `residueLambda_sign` | R 74–75 | ResidueValue 21–22 | representative sign values |
| `residueLambda_neg` | R 77–80 | ResidueValue 25–28 | (10), 235–239 |
| `goodMultiplier_one` | R 82–83 | ResidueValue 33–34 | 241–246 |
| `goodMultiplier_neg` | R 85–88 | ResidueValue 43–46 | negation and good products, 235–249 |
| `goodMultiplier_natCast_step` | R 90–94 | Rigidity 9–13 | §5.2 |
| `residueLambda_mul` | R 96–99 | Rigidity 60–63 | (18), 313–316 |
| `lambda_eq_one_of_isSquare` | R 101–104 | Rigidity 76–79 | (19) and §5.3 |
| `prime_dvd_quarter_isSquare` | R 106–109 | ResiduePrime 9–12 | §6, any prime divisor chosen there |
| `exists_small_prime_isSquare` | R 111–114 | ResiduePrime 50–53 | §6 lemma |
| `representation_four_prime_three_mod_four` | R 118–120 | Assembly 10–12 | §7.1 |
| `representation_multiple_four` | R 122–123 | Assembly 21–22 | theorem and §8 |

The generic sign-function discussion in the prose is specialized to the actual `lambda` in these approved interfaces; this review does not claim Lean formalization of the more general auxiliary theorem for arbitrary functions.

Older interface inventory, all in `FourPartial.lean`, compared against `four-interfaces-v1.lean:7–85`:

| Declaration | Actual header lines |
|---|---:|
| `lambda_six` | 8–9 |
| `lambda_seven` | 14–15 |
| `twelve_two_sign_seed` | 18–20 |
| `representation_multiple_twelve` | 25–26 |
| `representation_multiple_four_of_lambda_one` | 29–31 |
| `representation_multiple_four_of_even` | 37–39 |
| `representation_multiple_four_of_three_dvd` | 46–48 |
| `representation_multiple_four_of_sum_two_squares` | 55–57 |
| `prime_one_mod_four_eq_sum_two_squares` | 81–83 |
| `representation_four_prime_one_mod_four` | 88–90 |
| `prime_divisor_positive_sign_cofactor` | 94–97 |
| `exists_prime_factor_of_lambda_neg_one` | 109–112 |
| `representation_multiple_four_of_prime_divisor` | 121–125 |
| `representation_multiple_four_of_prime_one_mod_four_dvd` | 131–134 |
| `exists_prime_one_mod_four_of_lambda_neg_one` | 140–143 |
| `representation_multiple_four_of_mod_four_one` | 190–192 |
| `representation_multiple_four_of_mod_four_ne_three` | 198–200 |
| `multiple_four_iff_odd_prime_core` | 207–209 |
| `multiple_four_iff_prime_three_mod_four_core` | 226–229 |

## 4. Dependencies, vacuity, and case coverage

- **No final conditional escape.** `Assembly:13–19` introduces `hno` only inside proof by contradiction, derives antireflection, obtains a prime `r<p` that is a square, and contradicts `lambda r=1` with `lambda_prime`. `Assembly:23–24` discharges the remaining-prime core through the **reverse** implication of the proved equivalence. Neither `hno`, `hanti`, nor a prime-core assumption survives either representation endpoint.
- **Intentional contradiction premises.** Ternary interfaces assume nonrepresentation; with the final theorem their positive-input premise bundles are inconsistent. That is the intended contradiction argument, not a vacuity defect in the endpoint. Ternary does not import Assembly or assume its conclusion. Antireflection at prime 2 is itself impossible; uses here have `p≥7`, while the general conditional residue helpers do not promise that antireflection exists.
- **Natural subtraction/division.** Reflection complements are positive from the strict bounds. The defect descent explicitly proves exact divisibility by 3 before using `(p+x)/3,(p+y)/3` (`Ternary:64–101`). Ordered positive gaps strictly decrease; the equal-entry case is excluded by odd primality (`103–122`). No truncated subtraction supplies a false decrease.
- **Short multiple.** The witnesses occur after each `z`: signed `k : ℤ`, positive `d : ℕ`, `k≠0`, `|k|<n`, and **`n*d<p`**. No aggregate estimate has been replaced by a stronger pointwise assumption. The implementation uses residue bins/pigeonhole rather than sorting circular gaps. The wrapping case is present, and strictness there uses `n∤p` from `2≤n<p` and primality (`Cyclic:33–63`); the other case is `64–100`.
- **Residue rigidity.** Negatives are used only as residue multipliers, not as natural arguments of `lambda`. The induction premise concerns positive `j<n`, separately from antireflection on `0<j<p`. The empty `n=1` induction range is explicitly handled. The crucial ordinary-product bridge uses `n*d<p` before applying the representative formula (`Rigidity:38–43`). Cancellation is by a proved nonzero sign. A square root cannot be zero because `0<n<p` makes its square nonzero (`76–91`).
- **Small prime and constants.** `p≥7`, `p%4=3` imply exact division of `p+1` by 4 and quotient at least 2. Any prime divisor has `2≤r≤(p+1)/4<p`; zero residues and an empty prime-divisor choice are excluded. The constants 3, 4, and 7 have their stated arithmetic roles, not an unexplained sufficiently-large threshold.
- **All multipliers.** `FourPartial:207–241` handles even `m` using the two-sign seed for 8; odd `m` of sign +1 diagonally; and odd `m` of sign -1 through a prime divisor and positive sign-+1 cofactor. The prime cases are `p=3` via `12=5+7`, `p%4=1` via the proved library-assisted branch, and the remaining `p≥7,p%4=3` via Assembly. Cofactor multiplicativity requires no coprimality.
- **Smallest and degenerate cases.** `m=1` is included through `lambda_one` and diagonal witnesses `2,2`; `m=0` is excluded by the requested hypothesis. Equal representation witnesses are allowed. The older sum-two-squares helper permits zero roots and equal roots: unequal roots give positive `2(u+v)^2,2(u-v)^2`, while equal roots use the 8-seed; `m>0` excludes both roots zero (`FourPartial:55–79`). Prime 2 is handled by the even-multiplier branch, not silently omitted.
- **Typeclasses.** Every local `Fact p.Prime`/`Fact r.Prime` is constructed from explicit `hp`/`hr`. Field/nonzero-modulus instances are consequences of these facts, not additional endpoint assumptions. `GoodMultiplier` itself has no primality premise, but its field-based uses do.

## 5. Actual Lean checks and axioms

Working directory for every check: `P/lean`. Actual toolchain: Lean **4.32.2**, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`, arm64 Apple Darwin release.

| Check | Exit |
|---|---:|
| `lake build Statement.FourWork.Assembly` | 0 |
| `lake env lean Statement/FourWork/Assembly.lean` | 0 |
| `lake env lean -t0 Statement/FourWork/Assembly.lean` | 0 |
| `lake env lean -t0 <file>` for all eight other local closure files | 0 each |
| `lake env lean -t0 --stdin`, read-only `#check @...`/`#print` inspection | 0 on corrected inspection command |

The eight dependencies were `Definitions`, `Partial`, `FourPartial`, `Descent/Cyclic`, `Descent/Ternary`, `Character/ResidueValue`, `Character/Rigidity`, and `Character/ResiduePrime`. They were actually re-elaborated, not merely accepted from replayed build messages. Trust level zero was requested explicitly. The local build did reuse existing library/build artifacts; no new fetch or source lookup occurred.

One reviewer-only inspection attempt exited 1 because `pp.width` is not a supported option. Its complete log is preserved in `.types.log/.types.json`. Removing that display option from stdin produced `.types2.log/.types2.json`, exit 0. **No candidate file was changed.** All actual candidate/dependency compilation runs succeeded. Only the four pre-existing unused-variable warnings in `Partial.lean:51,171,187,291` occurred.

I inspected every printed axiom result: Assembly's **69/69 requested prints** were present; the dependency recompilations printed another 184 results. Across the build and explicit compilations there were 154 distinct printed declarations. Every set was a subset of:

```text
{propext, Classical.choice, Quot.sound}
```

Both representation endpoints have exactly that set. There was no `sorryAx`, custom axiom, native-reduction axiom, or other unsupported assumption. Details, coverage counts, and each printed set are in `.audit.json`; raw output is in `.compile.log`, `.trust0.log`, and `.dependencies.log`.

A dedicated source scan and complete manual reading of the nine-file local closure found no `sorry`, `admit`, custom `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, or custom elaborator/macro shortcut. Ordinary `decide`, `omega`, `ring`, `nlinarith`, and simplification produce kernel-checked proofs. This is not a claim that all library tactic implementation internals are free of unsafe implementation code; their resulting theorem dependencies were checked as above.

The local import graph is acyclic and has nine modules. It bottoms out in the frozen definitions and Mathlib. No dependency imports Assembly, the project root, or an assumed proof of `Target`. `Scaffold.lean` merely declares a structure with an unprovided `result : Target` field and is not in this candidate's closure.

## 6. Exact external theorem applications and cutoff

The candidate is **not a line-by-line formalization of the prose's elementary-only route**. `PROOF.md:489–490` describes a direct floor-parity proof and inverse-pairing proof. Lean instead uses quadratic reciprocity for the small-prime-square lemma and Fermat's two-squares theorem for the 1-mod-4 branch; Cyclic also uses an equivalent bin argument. These are proof-method differences, not statement weakenings. Do not describe the Lean proof as avoiding those imported theorems.

All following library locators refer to the clean immutable Mathlib commit **`905b95818eb32af7874a58b427f50c1711a5e96c`**, not a current webpage/version. The first three files have authors **Chris Hughes and Michael Stoll**.

1. **Sums of two squares**, `Mathlib/NumberTheory/SumTwoSquares.lean:33–38`:
   ```text
   Nat.Prime.sq_add_sq {p : ℕ} [Fact p.Prime]
     (hp : p % 4 ≠ 3) : ∃ a b : ℕ, a^2+b^2=p.
   ```
   `FourPartial:81–86` supplies the prime instance from `hp`, derives the inequality of remainders from `p%4=1`, and reverses the resulting equality. It does not assume positive roots; the receiving helper handles their degenerate cases. Its Gaussian-integer proof dependencies are proved in the same pinned tree, including `Zsqrtd/QuadraticReciprocity.lean:34–85`.
2. **Legendre symbol**, `Mathlib/NumberTheory/LegendreSymbol/Basic.lean:269–286`:
   ```text
   [Fact p.Prime] → (IsSquare (-1 : ZMod p) ↔ p % 4 ≠ 3).
   ```
   `ResiduePrime:43,48` uses this at prime `r`, in the appropriate direction for `r%4=1` or `r%4=3`.
3. **Quadratic reciprocity**, `Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean:45,73–77,99,153–167`:
   ```text
   [Fact p.Prime], p≠2:
     IsSquare (2 : ZMod p) ↔ p%8=1 ∨ p%8=7.

   [Fact p.Prime] [Fact q.Prime], p%4=1, q≠2:
     IsSquare (q : ZMod p) ↔ IsSquare (p : ZMod q).

   [Fact p.Prime] [Fact q.Prime], p%4=3, q%4=3, p≠q:
     IsSquare (q : ZMod p) ↔ ¬ IsSquare (p : ZMod q).
   ```
   Application audit (`ResiduePrime:13–48`): both prime instances are constructed; `p+1=4rs` follows from exact division. If `r=2`, this gives `p%8=7`, and `p≥7` gives `p≠2`. If `r%4=1`, instantiate the reciprocity theorem with its `p=r,q=original p` and use `.mp`; `(original p : ZMod r)=-1` supplies the left square. If `r%4=3`, use `.mpr` with original `p,q=r`; `r<p` supplies distinctness, and the nonsquare of -1 modulo r supplies the right side. No distinct-prime requirement is omitted or circularly assumed.

Immutable source URL prefix for these locators:
`https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/`.

Public-availability evidence was audited **offline**, using retained exact-SHA workflow metadata, not commit timestamps alone:

- Mathlib release workflow `https://github.com/leanprover-community/mathlib4/actions/runs/30379912464`, created **2026-07-28T16:47:39Z**, names the exact pinned SHA.
- Lean workflow `https://github.com/leanprover/lean4/actions/runs/30368480005`, created **2026-07-28T14:27:52Z**, names the actual compiler SHA.
- Each of the eight other manifest packages has a matching recorded exact-SHA public witness before cutoff: Plausible, importGraph, ProofWidgets, Aesop, Qq, Batteries, and Cli on **2026-07-13**, LeanSearchClient on **2026-02-12**. Installed HEADs match every manifest revision; nested manifests have no conflicting pins and tracked package trees are clean.

Evidence source: `P/formal/environment/public-availability-witnesses.json`, SHA-256 `051de67ee5bfd81242942075cf9dabacd8cfa96b74abf3733b025456694cc4c1`; supporting ledger `P/sources.md:5–45`. `.provenance.json` records all exact revisions, URLs, witness dates, local Git commands/results, source-file hashes, and nested-manifest checks. These witnesses establish eligible versions no later than **2026-07-31 inclusive**. No network lookup, new mathematical source, dependency update, or toolchain installation was performed in this review.

## 7. Gate boundary and remaining work

**Statement fidelity: APPROVE. Exact-candidate proof gate: APPROVE. Protection: YES**, for these hashes and defining dependencies.

There is no unresolved mathematical/formal obligation in the reviewed multiple-of-four candidate. However:

1. **Root integration is not certified here.** Frozen `Statement.lean:1–5` imports through `FourPartial`, not Assembly. The complete theorem is available through `Statement.FourWork.Assembly`; this report does not claim it is exposed by the integrated root. Only the integrator should perform the authorized merge/import change and rerun the integrated gate.
2. **Publication should preserve the proof-method distinction and source locators above.** The prose's statement that its own proof avoids reciprocity/two-squares must not be transferred to the Lean proof. The leader owns carrying these additional library locators into the published source ledger/reproduction notes.
3. **The original all-even `Target` is not proved or claimed.** The new theorem covers positive multiples of four; no conclusion for every even `N>2` follows merely from this gate. This formal review also does not replace separately required independent natural-language reviews or the final regulator review.

Next owner: leader for routing; integrator for integration. Any mathematical statement/definition change invalidates the affected protection and requires fresh review.

### Owned evidence files

All are beside this report, with prefix `full-candidate-review-v1`:

- `.snapshot-begin.json`, `.snapshot-end.json`: frozen inputs and end comparison.
- `.signatures.json`: all 38 helper/endpoint signature comparisons plus definitions and target snapshot.
- `.compile.log/.compile.json`, `.trust0.log/.trust0.json`: actual build and Assembly checks.
- `.dependencies.log/.dependencies.json`: eight actual dependency recompilations.
- `.types.log/.types.json`: preserved failed reviewer display-option attempt.
- `.types2.log/.types2.json`: successful elaborated type/definition inspection.
- `.audit.json`: every axiom set, coverage, source-scan scope, and acyclic imports.
- `.provenance.json`: exact external versions, offline public witnesses, and source identities.
