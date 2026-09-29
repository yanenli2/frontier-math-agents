# Descent helper-graph statement-fidelity review

Mode: CERTIFICATION — statement fidelity only.

**VERDICT: APPROVE.** The supplied 19 signatures and two new definitions are faithful interfaces for the requested all-positive-multiples-of-four target. **This exact statement snapshot may be protected for proof work.** No required signature correction was identified.

This approves neither proofs nor elaboration. The supplied candidate is a signature inventory, without theorem bodies. In particular, protection of `positive_pair_gap_step` covers its stated existential strict decrease, **not** an unstated exact factor-three contraction formula; see the precision discussion below. This review does not certify the source's more general arbitrary-function FSPD theorem or its full quadratic-character classification.

## 1. Inputs and scope

Path abbreviations:

- `P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`
- `W = P/waves/multiples-four`
- `R = .clawcodex/math-team/review-inputs/r20260924-four-v1`
- `M = P/lean/.lake/packages/mathlib`
- `C = ~/.elan/toolchains/leanprover--lean4---v4.32.2/src/lean`
- `D = W/formal/descent-blueprint/Readback.lean.txt`
- `S = W/nl/descent/proof-attempt-v1.md`

Target: `W/request.md:9–14`, especially the unrestricted positive-natural parameter in

```lean
theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :
  ArithmeticStatement.HasRepresentation (4 * m)
```

Mathematical source considered: **only `S:31–42` and `S:44–332`**. No other prose sections of that file were consulted. The whole-file hash below identifies the artifact, not an extension of the reviewed source scope.

Read the supplied neutral definition extracts and current literal readback in `R`. Independently compared the actual declarations and definitions, rather than adopting a readback verdict. No historical acceptance reports or author-confidence material were consulted. Read the fixed base `P/lean/Statement/{Definitions,Partial,FourPartial}.lean`; none was modified.

The project specifies Lean `leanprover/lean4:v4.32.2`. `elan show` reported that installed toolchain, Lean commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`. The lakefile, manifest, and actual mathlib `HEAD` agree on **`905b95818eb32af7874a58b427f50c1711a5e96c`**; mathlib `git status --porcelain` was empty. Only this checkout was consulted. No external mathematical literature or later source was introduced; the specified external-source cutoff remains 2026-07-31. No compiler, build, proof, or axiom-certification result is claimed.

`D` and `R/DescentInterfaces.lean.txt` are byte-identical. The four base definition bodies in `D:9–19` also match the corresponding fixed-base text exactly.

## 2. Definition fidelity

### Fixed definitions

`D:9–19`, `Definitions.lean:6–8`, and `Partial.lean:14–20` agree with `W/request.md:14` and `S:33–38`:

- `omega` counts **all** entries of `primeFactorsList`, hence factors with multiplicity, not distinct primes.
- `lambda` has values in **ℤ**, as `(-1 : ℤ) ^ omega n`.
- `HasRepresentation N` requires two natural witnesses, both strictly positive, total exactly `N`, and each individual sign exactly `-1`. Equal witnesses are allowed. No prime, coprimality, ordering, or unequal-witness requirement appears.

Inspected the actual pinned `primeFactorsList` definition (`M/Mathlib/Data/Nat/Factors.lean:38–44`), `minFac`/`minFacAux` (`M/Mathlib/Data/Nat/Prime/Defs.lean:207–219`), and the core list-length definition (`C/Init/Prelude.lean:3027–3029`). Empty lists at 0 and 1 give `lambda 0 = lambda 1 = 1`. Positive-domain complete multiplicativity in `Partial.lean:57–64` has no coprimality hypothesis; the pinned factor-list product interface at `Factors.lean:196–197` agrees.

`Nat.Prime` is the actual natural-number primality predicate: inspected its definition as `Irreducible` and its characterization `prime_def_lt` (`Prime/Defs.lean:42–43,107–112`), together with `Irreducible` and `IsUnit`. In particular, primality excludes 0 and 1.

### Two new definitions

| Definition | Source locator | Audit |
|---|---|---|
| `FourWork.residueLambda`, `D:23–24` | `S:156–160` | Exactly `lambda z.val`, not a chosen lift, absolute-minimum representative, or assumed periodic value of lambda. For positive modulus, `.val` is the canonical natural representative; for nonzero residues it lies in `1,…,p−1`. |
| `FourWork.GoodMultiplier`, `D:26–28` | `S:164–170` | Exactly a **nonzero** multiplier satisfying the multiplication identity for **every nonzero** test residue. It does not mention representation, its negation, an endpoint theorem, or an equivalent encoding of the desired final conclusion. |

Checked `ZMod` and `.val` against `M/Mathlib/Data/ZMod/Defs.lean:142–144` and `Basic.lean:51–64,89–93`. The total definition has `ZMod 0 = ℤ` with `.val = Int.natAbs`; it is not a finite residue model at modulus zero. The prime-modulus uses exclude this case. Also `residueLambda p 0 = 1`, not the zero value of an extended quadratic character. This is harmless because the character/multiplication assertions concern nonzero residues, and primality keeps products of those residues nonzero. There is no claim that this total function is the quadratic character at zero.

`IsSquare` was inspected, not inferred from its name: `M/Mathlib/Algebra/Group/Even.lean:50–57` defines it as `∃ r, a = r * r`. Its witnesses here belong to **`ZMod p`**, not to ℕ.

## 3. All 19 signature comparisons

Names 1–17 are in `ArithmeticStatement.FourWork`; 18–19 are in `ArithmeticStatement`. Line references in the second column are to `D`.

| # | Signature / lines | Source locator and fidelity finding |
|---|---|---|
| 1 | `lambda_reflection_eq_one_of_neg`, 30–33 | `S:59–64`, implication (A). The negative input sign implies the positive complement sign. `0 < n < p` makes `p - n` a genuinely positive difference. Omitting primality is a valid lambda-specific generalization: this implication does not need it. |
| 2 | `lambda_double_reflection_eq_neg_one_of_pos`, 35–38 | `S:65–68`, implication (C). The domain is exactly `0 < n < 2*p`, not incorrectly restricted to `n < p`; `2*p - n` is positive. The sign direction is correct. No primality is needed here either. |
| 3 | `three_not_dvd_of_positive_pair`, 40–44 | `S:99–109`. Both positive members have sign `+1` and sum to `p`; the conclusion excludes `3 ∣ x`. The corresponding assertion for `y` follows by exchanging inputs, so no symmetric premise is lost. The fixed lambda value at 3 removes the general source function's need to derive that sign under prime hypotheses. |
| 4 | `positive_pair_gap_step`, 46–52 | `S:111–138`. Returns another ordered positive-positive pair of the same total with a strictly smaller positive natural gap. `0 < x < y` and `0 < u < v` prevent truncated subtraction. `y > 0` and `v > 0` are implied, not missing. No explicit `p ≠ 2` is needed: an ordered positive pair cannot sum to 2. The precise scope of the ternary construction is discussed below. |
| 5 | `no_positive_pair`, 54–58 | `S:128–140`. Rules out the conjunction of two positive signs for every positive pair of total `p`, not just an ordered pair. Primality plus `p ≠ 2` supplies oddness for the unequal-member argument; `p ≠ 3` retains the descent's other restriction. |
| 6 | `lambda_antireflection_of_no_representation`, 60–63 | `S:97,140–146`. Full antireflection is a **conclusion derived under nonrepresentation**, over every natural `n` with `0 < n < p`. It is not introduced as a premise of the descent that is supposed to establish it. |
| 7 | `cyclic_short_multiple`, 65–69 | `S:174–190`, with the strict bridge emphasized at `S:211`. For each nonzero `z`, witnesses are a signed integer `k ≠ 0` with `k.natAbs < n` and a natural `d > 0` with **`n*d < p`**. The cast equation is precisely `k*z = d` modulo `p`. Negative wrapping-gap indices are allowed. The bound is neither weakened to `≤` nor put on `abs(k)*d`. No lambda, antireflection, or nonrepresentation premise appears. |
| 8 | `residueLambda_natCast`, 71–72 | `S:156–158,194–196`. Identifies lambda and the residue function only for `n < p`; it does not assert lambda periodicity at large integers. Allowing `n = 0` is a harmless extension under the fixed total definitions. |
| 9 | `residueLambda_sign`, 74–75 | `S:49,156–158` and baseline `S:35`. Correct integer two-sign conclusion. Primality is unnecessary for this total-definition fact. Its extra modulus-zero cases use absolute values, not a false finite-representative assertion. |
| 10 | `residueLambda_neg`, 77–80 | `S:158–162`, equation (2). Full antireflection is explicitly a conditional hypothesis; only nonzero residues are tested. No unconditional character law is asserted. |
| 11 | `goodMultiplier_one`, 82–83 | `S:158,168`. Gives goodness, including nonzeroness, of 1 for a prime modulus. The source's `F(1)=1` is supported by fixed `lambda_one`. |
| 12 | `goodMultiplier_neg`, 85–88 | `S:160,168–176`. Closure under negation is conditional on antireflection and the original multiplier's goodness. This is the source's closure with `-1`, not a hypothesis that every signed multiplier is already good. |
| 13 | `goodMultiplier_natCast_step`, 90–94 | `S:174–211`. Strong-induction form of the least-bad-multiplier argument. Goodness is assumed only for positive representatives **strictly below `n`**, while the conclusion demands full goodness of `n`. Signed small multipliers are handled through signature 12, not silently included as an unsupported character law. At `n = 1`, the smaller range is empty and signature 11 supplies the base case. |
| 14 | `residueLambda_mul`, 96–99 | `S:192–211`. Multiplicativity on all pairs of nonzero residues is concluded under primality and antireflection. It is not assumed in `GoodMultiplier` for arbitrary multipliers. |
| 15 | `lambda_eq_one_of_isSquare`, 101–104 | `S:215,231–235`. Extracts the square-implies-positive direction needed at the endpoint. `0 < n < p` ensures the square residue is nonzero; any square root is therefore nonzero as well. There is no assertion that `n` itself is a natural square. The source's converse character classification is not claimed by this type. |
| 16 | `prime_dvd_quarter_isSquare`, 106–109 | `S:243–278`. Any prime divisor of the exact positive quarter is a square modulo `p`. From `p ≥ 7` and `p % 4 = 3`, `(p+1)/4 ≥ 2` and the division is exact. Primality/divisibility imply `2 ≤ r ≤ (p+1)/4 < p`, so no zero-residue square can satisfy this input situation. No antireflection or target-negation premise is smuggled into the residue-prime lemma. |
| 17 | `exists_small_prime_isSquare`, 111–114 | `S:241–243,278` and the direct-r route at `S:301`. Supplies a prime divisor `r` together with the explicit quarter bound, `r < p`, and genuine modular squareness. Divisibility is supported by the source construction. Leastness of a prime `q` is not asserted or required by the direct route. |
| 18 | `representation_four_prime_three_mod_four`, 118–120 | `S:297–303`. Exactly the prime core: prime `p ≥ 7`, `p % 4 = 3`, then the required positive negative-negative pair. Neither nonrepresentation, antireflection, a square witness, nor a restriction on representation witnesses remains as an endpoint premise. |
| 19 | `representation_multiple_four`, 122–123 | `W/request.md:9–14` and `S:319–332`. Exactly every `m : ℕ` with `0 < m`, including 1. No sign, congruence, primality, coprimality, or size restriction was added. The namespace makes the unqualified conclusion the requested `ArithmeticStatement.HasRepresentation (4*m)`. |

### Precision of the ternary gap interface

The source explicitly chooses `(p+x)/3` and `(p+y)/3` after proving exact divisibility (`S:113–126`), and states

`0 < y' - x' = (y - x)/3 < y - x` (`S:134–138`).

**The snapshot does not encode those choices or the equality to `(y-x)/3`.** It encodes their consequence: existence of another defect with a positive, strictly smaller gap. That is the interface needed for the source's well-founded descent, so this is an acceptable extraction for the assigned helper graph, not a weakening of the requested representation theorem. It must not be advertised as a protected exact quotient/quantitative contraction theorem. Such an additional theorem or strengthened signature would need its own reviewed snapshot.

Similarly, specializing the abstract function to fixed lambda and extracting only the square-positive consequence is deliberate scope reduction of intermediate interfaces, supported by `S:297–301`. It does not certify every assertion of the abstract rigidity/FSPD discussion.

## 4. Quantifiers, domains, bounds, and hidden assumptions

- Implicit natural/residue parameters are universal, not existential. Hypotheses are implications. There are no ambient section variables or undeclared mathematical premises; `autoImplicit` is false.
- In the gap step, `u` and then `v` may depend on `p,x,y` and the preceding premises. In the cyclic lemma, `k` and then `d` are selected **after** `z`; no one pair is required to work uniformly for all residues.
- The small prime is selected after `p`; its modular square root may depend on that prime. The representation witnesses are selected after the input `p` or `m`. There is no unjustified uniform constant, universal square root, or fixed representation pair.
- The test-residue quantifier in `GoodMultiplier`, the full antireflection range below `p`, and the smaller-multiplier range below `n` remain separate universal ranges. No bound on one chosen point replaces one of those universal assertions.
- The cyclic source's average-gap argument yields **some** gap with the displayed bound. The signature asserts precisely an existential short multiple, not that every cyclic gap is small. There is no aggregate-to-pointwise strengthening elsewhere.
- Every natural subtraction in signatures 1–6 is on a strictly ordered positive domain. The two natural gaps in signature 4 are positive, not zero produced by truncation. The quotient in signatures 16–17 is natural division, with exactness supplied by the modulo-4 hypothesis.
- Constants 2, 3, 4, and 7 retain their stated source roles. In particular, `2 ≤ n < p` is retained in the cyclic lemma; `d > 0`, `k ≠ 0`, and strict `n*d < p` prevent trivial zero or boundary witnesses. They imply `d < p` and a nonzero cast of `k` in the prime modulus.
- `IsSquare` uses the canonical multiplication on `ZMod p`; the canonical ring structure exists without primality. None of the 19 types hides a `[Fact p.Prime]`, field, finite-type, or nonzero-modulus premise. Proof implementations may derive the usual instances from the displayed `hp`; they may not add them as stronger independent assumptions. `ZMod.val_lt` itself needs `[NeZero p]`, which is available from primality in the relevant uses.
- Complete multiplicativity is needed only for positive natural arguments. The arbitrary total value at zero is not used to assert complete multiplicativity on all naturals, nor is lambda silently assumed periodic.

## 5. Contradiction premises and dependency direction

The source/signature graph has the intended direction:

1. Baseline lambda facts and a hypothetical missing representation give the two one-sided implications and the defect descent (`S:44–146`; signatures 1–6).
2. **Independently conditional on full antireflection**, the short-multiple/least-bad-multiplier argument supplies residue multiplicativity and positivity on nonzero squares (`S:148–217`; signatures 7–15).
3. The small residue-prime construction is independent of nonrepresentation and antireflection (`S:237–280`; signatures 16–17).
4. At the prime endpoint, a contradiction argument under nonrepresentation supplies the antireflection premise using signature 6, then uses the small square prime and its fixed negative lambda sign (`S:291–303`). Thus antireflection is discharged **inside the endpoint argument**, not left as an assumption of signature 18 or 19.
5. The all-multiplier assembly is `S:309–332`. The fixed base also exposes precisely the corresponding reduction at `FourPartial.lean:226–241`, an equivalence between the full positive-multiplier statement and signature 18's prime core. An equivalence is not an already assumed proof of either endpoint. Its direction from the prime core to all multipliers is the usable assembly direction.

No helper signature mentions either new endpoint theorem. No occurrence of either exact endpoint name was found in the three fixed base files. In the supplied snapshot their names occur only in their own declarations. The source does not invoke the final theorem to justify its helpers.

**Implementation boundary:** no new theorem bodies were supplied. Accordingly this review establishes absence of circular assumptions in the types and source dependency plan, not absence of circular or endpoint-dependent reasoning in an unseen implementation. Later proof acceptance must check the actual dependency/axiom graph; the final theorem must not be used to discharge its own helper obligations.

### Vacuity and degenerate cases

- Signatures 1–6 deliberately assume nonrepresentation. Their other premises force `p > 0`, so an eventual proof of signature 19 makes their complete premise bundles impossible. That is ordinary proof by contradiction, not a fidelity defect and not permission to prove them by citing that endpoint.
- At `p = 2`, full antireflection would contradict `lambda 1 = 1`. Some conditional rigidity signatures allow this vacuous case, but the source-derived antireflection theorem excludes it and the prime endpoint has `p ≥ 7`.
- At modulus 1 there is no nonzero residue. `GoodMultiplier` is nevertheless not vacuously true, because it explicitly requires its multiplier to be nonzero. Modulus-zero cases occur only in harmless total-definition/sign extensions, not in the prime finite-field argument.
- The ordered-gap hypotheses exclude equal members where strict decrease is needed. Signature 5 itself addresses every positive pair, with oddness excluding an equal-member defect.
- `IsSquare` alone permits zero, but the displayed positive-below-prime or prime-divisor bounds exclude zero in every load-bearing use. The quarter is at least 2, so the prime-divisor choice does not concern 0 or 1.
- `m = 0` is outside the requested positive domain. `m = 1` is included; equal witnesses are allowed. Strict witness positivity and the sign requirements cannot be bypassed by empty factorizations or zero summands.

## 6. Exact artifact identities

All hashes below are SHA-256. File hashes use complete raw bytes. Declaration hashes use the exact inclusive line ranges of `D`, with their existing trailing line feeds, without whitespace normalization or proof text. They are **textual signature hashes**, not hashes of elaborated Lean constants. The whole-snapshot hash also protects imports and namespace context.

### Supplied files and fixed base

| Artifact | SHA-256 |
|---|---|
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `S`, whole artifact | `23fc6ad19d1c45dd432945aa84756b190700b8c15394b1554ebb3ecaff82235e` |
| `S:31–42` | `030f0acd4a1184cab6301480bba7cba7385ac07e7284c261869a7a00046872a8` |
| `S:44–332` | `cff9ddfc0869dce34c765192f609b8898cbb096b2ecce527bc58a8ddaeb45a2c` |
| Allowed source ranges concatenated in that order | `0ee4911dfcbda16c62e3fe9aba787ff63f52c3913598402946215089c2d375d0` |
| `D` and identical `R/DescentInterfaces.lean.txt` | `372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763` |
| `R/ModularDefinitions.lean.txt` | `5c073db2b07ba2ccd729dd9c0218fd7ca6d1d6767e18d81c74bc19975188ec56` |
| `R/Dependencies.lean` | `fd4ec312622db449d27d6ac0b18b1decd62a9f76e18f8251bb40ffbabdef7981` |
| `R/ListOperations.lean` | `925cbf08a1aac0870075ad56ff2d95c7b0eb94c87853ace32d0043a9c094e2bc` |
| `R/descent-readback.md` | `460c911b32d72948da676c52e3f0edba52ad724aa505bd4d650b94375165e6ab` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `P/lean/Statement/FourPartial.lean` | `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325` |
| `P/lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `P/lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `P/lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |

### Definitions and all new signatures in `D`

| Declaration | Lines | SHA-256 |
|---|---|---|
| `omega` | 9 | `a18ad88e5c21b3d4cd0456bc5c6630120bbe709b7e4ee78b808d0ac9c0763df7` |
| `lambda` | 11 | `45dec5178043a88d833d8af6f661f1b8f958437be8e3113fef145c10d9406807` |
| `HasSignedRepresentation` | 13–16 | `33135bf373e28568b48384ae7a04f13fc2485e0e0b5ffcaf330c9a9ec5edb343` |
| `HasRepresentation` | 18–19 | `1b2d477a3c489713ec3d780a42523545e7ae74f7ac486e9ec434c82ed3c67d2e` |
| `residueLambda` | 23–24 | `304359790e4b777fd60844807f7d3dce06791e78a091f965090cd8106906a9b7` |
| `GoodMultiplier` | 26–28 | `28608b53e4ebe1e22ad9fa41b5655b393105f56ee0f4ebe59e6f2df716a59d60` |
| `lambda_reflection_eq_one_of_neg` | 30–33 | `f65b58b57c96085fd4c6f24c388988301bfd6a9a4024d3b3ab7d47053be51529` |
| `lambda_double_reflection_eq_neg_one_of_pos` | 35–38 | `6b2eeb821e58532ffbd1a21a16107129f31efc184c23a5a92e327cf7b623284e` |
| `three_not_dvd_of_positive_pair` | 40–44 | `9f380c462b87b1bef9d7c683893e808359726460a40fbd96ee776648bb1d57ae` |
| `positive_pair_gap_step` | 46–52 | `04c8c1983e2ddef6edf6051463bb4b1d4a2c0455e6c77dd8b3e5bd6601ccb35e` |
| `no_positive_pair` | 54–58 | `f712da17ce78c49776ee2e33ae75399a99657f1a163d9b39ae0aca6cb7166d52` |
| `lambda_antireflection_of_no_representation` | 60–63 | `2e98d41965376ae2e1b5b1813e25d83ef3e5bf875dfcea49c4e89b98320e32cd` |
| `cyclic_short_multiple` | 65–69 | `aad618b6d15cfbf061dc18936d91becbf4d2e2816c199aa1a0153ce255188182` |
| `residueLambda_natCast` | 71–72 | `354660c059b4a0d9d8567b3157b2f3358efa781e3f8a83dacb7e947cd58027c5` |
| `residueLambda_sign` | 74–75 | `2d91748d279e49d12b72deb1b910399ee08a040041b94c40857ff3dd105969e7` |
| `residueLambda_neg` | 77–80 | `f23fdfd79509335d4e48a974ba5acfefe73bc503e3da50569182e7d7b6d86cae` |
| `goodMultiplier_one` | 82–83 | `a3d6bea78c6c2258015b9a94189483c593e85d81deb4abcdf215815a082f2bc2` |
| `goodMultiplier_neg` | 85–88 | `e21f680968765b2e663079c7ed64c84b73d8571ae6d87e1e913f61d8a36ba11e` |
| `goodMultiplier_natCast_step` | 90–94 | `73fa8f8bf445ec7d72bb45f692cc4a7de8702891e23f72b4f73df5039d22f425` |
| `residueLambda_mul` | 96–99 | `f2e2d9afe2f79e72f70ad8298fa3943d0afdcfe1a52a968358fd6845a9dc495f` |
| `lambda_eq_one_of_isSquare` | 101–104 | `f14b0bfde0c27ef9089c6096b51228da247d6da72fbdc4d9e99cedf6a99abaed` |
| `prime_dvd_quarter_isSquare` | 106–109 | `8fbcf7e66d56f074517ac016b3c8e18466737bc0f80b0a27e6f1732596b40b92` |
| `exists_small_prime_isSquare` | 111–114 | `27e25215e9236c61cd56faea29ad94ce05d31c40d103b5bb735dcb9a7a2dce75` |
| `representation_four_prime_three_mod_four` | 118–120 | `dfd44352a26873c9bdcf1991d5e5c5df3911e1e96f1cff87f8c0e6113fb7e22a` |
| `representation_multiple_four` | 122–123 | `7a9e41b3137280c725f18e0fa08aa019a0103351b40f3e0440675c0356ec88bd` |

### Inspected pinned defining-library files

| Artifact | SHA-256 |
|---|---|
| `M/Mathlib/Data/ZMod/Defs.lean` | `7c3719a4e2c38f9549f5f61a0882fa10e220505dc4b61968186d0a4d30f335f1` |
| `M/Mathlib/Data/ZMod/Basic.lean` | `9a57047615cf4231f3561aef5c75ededf5a6ed6559308f31e241d1d27b2bc00c` |
| `M/Mathlib/Algebra/Group/Even.lean` | `1180fa9ac282e55257e95c8402acd7314fcbd0a18bcfdede92a3cde16e1db630` |
| `M/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `M/Mathlib/Data/Nat/Prime/Defs.lean` | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `M/Mathlib/Algebra/Group/Irreducible/Defs.lean` | `77937179ccfec6ca8acdd4b660525a7f313d4fb0b9c6dc4296d1301fb9e1e731` |
| `M/Mathlib/Algebra/Group/Units/Defs.lean` | `09489226154d6558ad44614501b55883f0dc31b4504f1bb29e6190b2df456bce` |
| `C/Init/Prelude.lean` | `44f86ebbb9ab743a05c6ebe2c674aadbf2c822bee874f1b16d7e6c8d56318dc9` |
| `C/Init/Data/List/Basic.lean` | `c6b61f1b5fcac4ea4339625f2e66916d1f2c1ae2531c10ee45b401846ffb6061` |

## 7. Disposition

- **Statement corrections required:** none for the stated helper interfaces and exact requested final type.
- **Protection:** yes, for precisely the definitions/signatures identified above, together with their fixed defining dependencies and the explicit precision limits. Any mathematical change requires fresh fidelity/readback review.
- **Remaining obligations:** all new proof bodies, actual pinned elaboration/compilation, endpoint-independent helper dependencies, and transitive axiom checks. Absence of proof text or of a `sorry` token in a readback inventory is not evidence of a proof.
- **Next owner:** leader, for routing protected proof work and subsequent independent checks. No candidate, task board, or fixed base was changed; only this assigned report was written.
