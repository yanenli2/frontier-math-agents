# Exact informal-to-Lean map: positive multiples of four

Mode: CERTIFICATION — unchanged approved interfaces, now integrated and compiler-checked.
The original [../../LEMMA_MAP.md](../../LEMMA_MAP.md) and original all-even target are preserved.

## Status and identity contract

- **Integrated endpoint:** `ArithmeticStatement.representation_multiple_four (m : ℕ) (hm : 0 < m) : HasRepresentation (4*m)`, in `Statement/FourWork/Assembly.lean:21–24`, imported by root `Statement`.
- Exact claim: for each natural `m>0`, there exist positive natural `a,b` with `a+b=4m` and both `(-1 : ℤ)^primeFactorsList.length` equal to `-1`. Includes `m=1`; equal witnesses allowed. No residual nonrepresentation, antireflection, prime-core, parity, or sign premise.
- Assembly SHA-256: `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066`.
- Integrated root SHA-256: `cd6a1dd9bff63ef400559805123c5e6cb7d2d4c9af28cf7f7c24f2cc640abc3c`.
- Frozen informal source `PROOF.md`: `205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b`.
- All **38 wave theorem headers**, including the two final endpoints, and all six relevant definition bodies/types agree with protected snapshots. Every theorem below was actually checked after the root import change and has exactly `{propext, Classical.choice, Quot.sound}`; none has an admission/custom/native proof axiom.
- These are compiler/integration statuses, not the integrator's independent mathematical acceptance. The exact candidate has formal approval; fresh final NL reviews [A](nl/reviews/final-four-review-a-v1.md) and [B](nl/reviews/final-four-review-b-v1.md) both report PASS at the same mathematical hashes. A records the root-only promotion and B the integrated root. Final regulator/publication acceptance remains leader-owned at this handoff.

Precise headers, full names, source/snapshot line numbers and per-header hashes are in [`formal/integration-full/signatures-integrated.json`](formal/integration-full/signatures-integrated.json). Elaborated types and all 156 named transitive axiom reports are in `06-root-import.stdout`; the expanded endpoint is displayed in `08-root-expanded-type.stdout`. Main dependencies listed below are explanatory, not an exhaustive kernel proof-term dependency graph. Transitive axiom prints cover that proof closure.

## Review/source keys

| Key | Exact artifact / scope |
|---|---|
| REQ | [request.md:7–16](request.md): exact user continuation. |
| P | [PROOF.md](PROOF.md), frozen exposition; section/line references below use this file. |
| N | [nl/generator/proof-attempt-v1.md](nl/generator/proof-attempt-v1.md), earlier families/reductions §§1–4. |
| D | [nl/descent/proof-attempt-v1.md](nl/descent/proof-attempt-v1.md), full helper source, hash `23fc6ad19d1c45dd432945aa84756b190700b8c15394b1554ebb3ecaff82235e`. |
| B | Unchanged `Statement.Definitions`/`Statement.Partial`; [original map](../../LEMMA_MAP.md) and [original sources](../../sources.md). |
| S-P | [formal/generator/four-interfaces-v1.lean](formal/generator/four-interfaces-v1.lean), hash `be55b4df2e640ec4645a2544b0013de5d6f366439162820af4233162766a0cee`; earlier 19 signatures. |
| S-F | [formal/descent-blueprint/Readback.lean.txt](formal/descent-blueprint/Readback.lean.txt), hash `372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763`; full 19 signatures and six definitions. |
| R-P | [formal/reviews/helper-fidelity-v1.md](formal/reviews/helper-fidelity-v1.md), [four-candidate-review-v1.md](formal/reviews/four-candidate-review-v1.md), [neutral earlier readback](../../../../review-inputs/r20260924-four-v1/interfaces-readback.md); scoped NL [partial-review-v1.md](nl/reviews/partial-review-v1.md). |
| R-F | [formal/reviews/descent-fidelity-v1.md](formal/reviews/descent-fidelity-v1.md), [neutral full literal readback](../../../../review-inputs/r20260924-four-v1/descent-readback.md), [full-candidate-review-v1.md](formal/reviews/full-candidate-review-v1.md). Literal readback hash `460c911b32d72948da676c52e3f0edba52ad724aa505bd4d650b94375165e6ab`. |
| LIB | [sources.md](sources.md): eligible same-pin SQ, NEG, QR, FIELD, REP, SQUARE, PH and arithmetic/tactic infrastructure, with exact preconditions/locators. |
| I | [formal/integration-full/audit-v1.json](formal/integration-full/audit-v1.json), source identities/diff/commands in [REPRODUCE.md](REPRODUCE.md). Mechanical integration, not a new fidelity certification. |

The original target snapshot `formal/approved-v1/Declaration.lean` (hash `bdfb30bcfade7b9df33e48f280125d10a40dd76f365cf5b87047183475fee7ed`) agrees with Assembly's endpoint header after whitespace removal only. S-F and all actual full-packet headers are internally byte-identical after removing proof assignments/bodies and outer whitespace.

## Fixed and new definitions

Names are under `ArithmeticStatement`; the last two are under `ArithmeticStatement.FourWork`.

| Declaration / actual location | Literal content and informal locator | Status / review |
|---|---|---|
| `omega`, Definitions:6 | `n.primeFactorsList.length`; P:3–5 counts multiplicity, not distinct factors. | Fixed B; identical S-F:9; R-F/I. |
| `lambda`, Definitions:8 | `(-1 : ℤ)^omega n`; P:3–5. | Fixed B; identical S-F:11; R-F/I. |
| `HasSignedRepresentation`, Partial:14–17 | Positive natural witnesses with exact sum and each sign equal to `s`. | Fixed B; identical S-F:13–16; R-F/I. |
| `HasRepresentation`, Partial:19–20 | Specialize the preceding definition to integer `-1`; P:7–12. | Fixed B; identical S-F:18–19; R-F/I. |
| `residueLambda`, Character/ResidueValue:9–10 | `lambda z.val`; P:225–233, restricted to canonical representatives in applications. | New definition, identical S-F:23–24; R-F/I. |
| `GoodMultiplier`, Character/ResidueValue:12–14 | `a≠0` and multiplication identity for **every** `z≠0`; P:241–246. No representation statement encoded in the definition. | New definition, identical S-F:26–28; R-F/I. |

`lambda 0=lambda 1=1` by totalization, but no zero representation witness or unrestricted-at-zero multiplicativity is used. `IsSquare` below is a square **in `ZMod p`**, not necessarily a natural square.

## Earlier 19 wave theorems: FourPartial

All names below are in `ArithmeticStatement`, in `Statement/FourPartial.lean`. Every row has status **integrated / checked**, snapshot **S-P**, reviews **R-P and full exact-candidate R-F**, evidence **I**. These helpers retain their stated hypotheses even though the new unconditional theorem is now available.

| # | Declaration / actual lines | Informal source and exact role | Main proved dependencies |
|---|---|---|---|
| 1 | `lambda_six`, 8–12 | N §2.3: `lambda 6=1`. | B `lambda_mul`, `lambda_two`, `lambda_three`. |
| 2 | `lambda_seven`, 14–16 | N §1/§2.3; P:473–477: prime 7 has sign −1. | B `lambda_prime`; `Nat.prime_seven`. |
| 3 | `twelve_two_sign_seed`, 18–23 | N §2.3; P §7.3 negative pair: `12=5+7`; independently `12=6+6` has two positive signs. | B `lambda_five`, rows 1–2; explicit positive witnesses. |
| 4 | `representation_multiple_twelve`, 25–27 | N §2.3: every `12t`, `t>0`, represented. | Row 3; B `representation_two_sign_seed`. |
| 5 | `representation_multiple_four_of_lambda_one`, 29–35 | N §2.1/§4; P:55–59: diagonal pair `2m,2m` if `m>0`, `lambda m=1`. | B doubling/diagonal representation. |
| 6 | `representation_multiple_four_of_even`, 37–44 | N §2.1; P:61–69: positive even multiplier. | B `representation_multiple_eight`; positive half-multiplier. |
| 7 | `representation_multiple_four_of_three_dvd`, 46–53 | N §2.3/§4: positive multiplier divisible by 3. | Row 4; positive quotient. |
| 8 | `representation_multiple_four_of_sum_two_squares`, 55–79 | N §3.1: `m>0`, `m=u²+v²`; roots may be zero or equal. | B `lambda_square`, `lambda_two_mul`, 8-seed. Unequal roots give `2(u+v)²,2(u−v)²`; equal roots use the 8-family. |
| 9 | `prime_one_mod_four_eq_sum_two_squares`, 81–86 | N §3.2 same-conclusion two-squares assertion. | LIB SQ `Nat.Prime.sq_add_sq`, with derived prime instance and remainder premise. |
| 10 | `representation_four_prime_one_mod_four`, 88–92 | N §3.2; conclusion of P §7.2 for prime `p%4=1`. **Different proof route from P**. | Rows 8–9; not P's inverse-pairing argument. |
| 11 | `prime_divisor_positive_sign_cofactor`, 94–107 | N §2.1/§4; P:71–87: from `m>0`, `lambda m=-1`, prime `p∣m`, obtain positive sign-+1 cofactor. | B positive-domain multiplicativity and prime sign; no coprimality. |
| 12 | `exists_prime_factor_of_lambda_neg_one`, 109–119 | N §1/§2.1; P:71–79: choose such a prime and cofactor. | B `lambda_one`; `Nat.exists_prime_and_dvd`; row 11. |
| 13 | `representation_multiple_four_of_prime_divisor`, 121–129 | N §2.1/§4; P:79–87: scale a representation of `4p` by the sign-+1 cofactor. **`HasRepresentation (4p)` is a premise of this helper.** | Row 11; B signed scaling; exact sum identity. |
| 14 | `representation_multiple_four_of_prime_one_mod_four_dvd`, 131–138 | N §4: sufficient condition that `m>0` has a prime divisor 1 mod 4. | Sign split, rows 5,10,13. |
| 15 | `exists_prime_one_mod_four_of_lambda_neg_one`, 140–188 | N §4: `m>0`, `m%4=1`, `lambda m=-1` force a prime divisor 1 mod 4. | Prime-factor list product/multiplicity; ZMod 4 sign/cast contradiction. Auxiliary family, not needed by final prime-core reduction. |
| 16 | `representation_multiple_four_of_mod_four_one`, 190–196 | N §4: all positive `m%4=1`. | Sign split, rows 5,14–15. |
| 17 | `representation_multiple_four_of_mod_four_ne_three`, 198–205 | N §4: all positive `m%4≠3`. | Even branch row 6 or odd-remainder-one row 16. |
| 18 | `multiple_four_iff_odd_prime_core`, 207–224 | N §2.2; P §2: equivalence with all odd prime multipliers. | Rows 5–6,12–13. An equivalence alone is not a proof of either side. |
| 19 | `multiple_four_iff_prime_three_mod_four_core`, 226–241 | N §4; P §§2,7–8: equivalence with prime `p≥7`, `p%4=3`. | Row 18, prime 3 via row 4, prime 1 mod 4 via row 10. The reverse direction is used only after full row 18 below proves the core. |

## Full 19-theorem packet: descent, residues, assembly

Rows 1–17 below are in `ArithmeticStatement.FourWork`; rows 18–19 are in `ArithmeticStatement`. Locations are relative to `Statement/FourWork/`. Every row has status **integrated / checked**, snapshot **S-F**, formal/readback gate **R-F**, evidence **I**.

| # | Declaration / actual location | Informal source and exact scope | Main proved dependencies |
|---|---|---|---|
| 1 | `lambda_reflection_eq_one_of_neg`, Descent/Ternary:8–20 | P:119–125, implication (A): under nonrepresentation of `4p`, `0<n<p`, `lambda n=-1` imply `lambda(p−n)=1`. | B sign dichotomy/multiplicativity and `lambda_four`; explicit scaled contradiction pair. |
| 2 | `lambda_double_reflection_eq_neg_one_of_pos`, Ternary:22–34 | P:126–131, (C): under nonrepresentation, `0<n<2p`, `lambda n=1` imply `lambda(2p−n)=-1`. | B sign dichotomy and `lambda_two_mul`; explicit positive contradiction pair. |
| 3 | `three_not_dvd_of_positive_pair`, Ternary:36–54 | P §4.1: positive sign-+1 pair `x+y=p` under nonrepresentation implies `3∤x`. | Rows 1–2, B `lambda_three`, positive quotient/complements. |
| 4 | `positive_pair_gap_step`, Ternary:56–101 | P §§4.2–4.3: ordered positive defect gives another with a **strictly smaller natural gap**. Protected type does not assert an exact factor-three formula. | Row 3 both orders; prime `p≠3`; exact divisibility of `p+x,p+y` by 3; row 2; B multiplicativity. |
| 5 | `no_positive_pair`, Ternary:103–122 | P §4.3: no positive-positive pair of total prime `p≠2,3` under nonrepresentation. | Row 4, strong induction on the positive gap; oddness excludes equal entries. |
| 6 | `lambda_antireflection_of_no_representation`, Ternary:124–137 | P:215–219, (9): derive reflection for every `0<n<p`. | Rows 1,5 and B sign dichotomy. Antireflection is a conclusion, not assumed here. |
| 7 | `cyclic_short_multiple`, Descent/Cyclic:10–100 | P §5.1, (13): for each `z≠0`, prime `p`, `2≤n<p`, get signed `k≠0`, `abs k<n`, positive `d`, **`n*d<p`**, `k*z=d` mod p. | LIB FIELD/REP/PH; bin/pigeonhole implementation, wrapping case explicit; `n∤p` makes the boundary strict. No lambda or nonrepresentation premise. |
| 8 | `residueLambda_natCast`, Character/ResidueValue:16–19 | P:225–233: agreement with ordinary lambda only for `n<p`. | REP canonical representative formula; definition. No large-integer periodicity claim. |
| 9 | `residueLambda_sign`, ResidueValue:21–23 | P:223–233 sign values for nonzero residues. | B `lambda_sign`; REP `.val_pos`. |
| 10 | `residueLambda_neg`, ResidueValue:25–31 | P:235–239, (10): residue negation law **assuming antireflection**. | REP negated representative, positive/bounded representative, explicit prime instance. |
| 11 | `goodMultiplier_one`, ResidueValue:33–41 | P:241–246: 1 is good for a prime modulus. | Row 8; B `lambda_one`; field identity and nonzeroness. |
| 12 | `goodMultiplier_neg`, ResidueValue:43–51 | P:235–249: goodness closed under negation, conditional on antireflection. | Row 10, original goodness, nonzero product/casts. |
| 13 | `goodMultiplier_natCast_step`, Character/Rigidity:9–58 | P §5.2: if all positive smaller representatives are good, the current positive `n<p` is good. | Rows 7–12. Strict `nd<p` justifies ordinary multiplicativity; smaller `abs k` and negation handle signed k; cancel a nonzero sign. Base `n=1` handled by row 11. |
| 14 | `residueLambda_mul`, Rigidity:60–74 | P:313–316, (18): multiplicativity for every pair of nonzero residues, conditional on prime modulus and antireflection. | Row 13 by strong induction, representative bounds/cast. |
| 15 | `lambda_eq_one_of_isSquare`, Rigidity:76–91 | P:318–338, (19)/§5.3: a natural `0<n<p` that is a modular square has sign +1, under antireflection. | Row 14 and sign values; positive/bounded n forces nonzero residue and square root. |
| 16 | `prime_dvd_quarter_isSquare`, Character/ResiduePrime:9–48 | P §6: any prime divisor of `(p+1)/4` is a square mod prime `p≥7`, `p%4=3`. **Lean uses QR/NEG, not the prose floor-parity calculation.** | Exact quarter division, divisor bound, local prime instances, LIB QR/NEG; no antireflection or representation premise. |
| 17 | `exists_small_prime_isSquare`, ResiduePrime:50–59 | P §6 lemma: supplies prime `r∣(p+1)/4`, `r≤(p+1)/4`, `r<p`, and modular squareness. | Quarter at least 2; prime divisor existence; row 16. |
| 18 | `representation_four_prime_three_mod_four`, Assembly:10–19 | P §7.1: prime `p≥7`, `p%4=3` has the required representation. | Assume absence only inside proof; derive row 6; obtain row 17; row 15 gives `lambda r=1` but B prime sign gives −1; contradiction discharges absence. |
| 19 | `representation_multiple_four`, Assembly:21–24 | REQ; P theorem/§8: every natural `m>0` represented, unconditionally beyond positivity. | Reverse implication of FourPartial row 19 applied to full row 18, then specialized to `m,hm`. All former core assumptions are discharged. |

## Dependency direction, mathematical scope, and omissions

The local graph is acyclic:

```text
Definitions → Partial → FourPartial
Partial → Ternary
Partial + FIELD → ResidueValue
Partial + FIELD + LIN → Cyclic
ResidueValue + Cyclic → Rigidity
QR + RING → ResiduePrime
FourPartial + Ternary + Rigidity + ResiduePrime → Assembly → root Statement
```

Arrows here point from dependency to dependent. Existing root-only Scaffold/Smoke depend on Definitions and do not feed an assumed target proof into Assembly. No helper imports Assembly or the root. The nonrepresentation/antireflection premise bundles in conditional helpers are intentional contradiction premises; they do not survive either endpoint. `GoodMultiplier` explicitly requires a nonzero multiplier and is not vacuously true on an empty nonzero-residue type. Naturals in gap/reflection subtractions have the stated strict bounds, and exact division is proved before quotient use.

Lean formalizes the necessary **lambda-specific** interfaces, not all generic-function statements from P/D. It does not separately formalize P §3's optional local ternary identity (7), closure of arbitrary good products as a named theorem, the floor-sum substeps (22)–(26), inverse pairing in P §7.2, or a full quadratic-character classification. The required consequences are proved by the mapped routes; no such omitted substep is silently assumed. This proof-method distinction is recorded in R-F and [sources.md](sources.md).

No mathematical obligation remains for the exact new `4m` theorem in the compiled candidate. Both independent final NL reviews now report PASS; final regulator/publication acceptance remains pending at integration handoff. **The broader all-even `Target` is not proved**; no `ArithmeticStatement.liouville_goldbach` or `ArithmeticStatement.pointwise_keystone` declaration has been added. Checked equivalences involving the original Target are not proofs of it.
