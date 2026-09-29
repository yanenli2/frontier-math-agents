# Independent multiples-of-four review B, v1

Mode: CERTIFICATION.

**Verdict: PASS for the exact requested multiples-of-four lemma, at the identities below.** The standalone prose argument establishes the claim. The actual Lean dependency chain implements a mathematically valid alternative at three identified points and has the same unconditional endpoint. No unresolved load-bearing mathematical obligation was found.

This is an LLM mathematical review, not Lean kernel verification. Recorded compiler evidence is distinguished below from this review. The original all-even `ArithmeticStatement.Target` is **not** certified by this conclusion.

## 1. Scope, independence, and input identities

Path abbreviations:

- `R = .`
- `P = R/.clawcodex/math-team/problems/liouville-goldbach-jul2026`
- `W = P/waves/multiples-four`
- `M = P/lean/.lake/packages/mathlib/Mathlib`
- `E = P/formal/environment`
- `I = W/formal/integration-full`

Read the required protocol, `W/request.md`, the complete `W/PROOF.md`, all ten specified local Lean files listed below, the pinned configuration, relevant pinned library source statements/proofs, the permitted availability metadata, and the specified raw integration evidence. No older draft cited by `PROOF.md` was opened or relied upon. No previous review, confidence statement, production-status report, task board, or verdict summary was read. No agents were spawned, no candidate was repaired, and no mathematical file was edited. This report is the only file written.

### Frozen candidate and local dependencies

Each following file was hashed before substantive inspection and rehashed after the audit. **Before and after hashes agree**, including both hashes supplied in the assignment.

| Path relative to P | SHA-256, before = after |
|---|---|
| `waves/multiples-four/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `waves/multiples-four/PROOF.md` | `205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b` |
| `lean/Statement/FourWork/Assembly.lean` | `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066` |
| `lean/Statement/FourWork/Descent/Cyclic.lean` | `09fbee47a60bf7db94d65e871fc49f5d07d60838c8b01cfbfdecb53033471290` |
| `lean/Statement/FourWork/Descent/Ternary.lean` | `d6f231fc9aa372f562b19170268b31ae16bdca178185256131232011fd255753` |
| `lean/Statement/FourWork/Character/ResiduePrime.lean` | `518f28a33ab98d1a44ea7b544ca7f695e28c48893982caaf72eb4879956763dd` |
| `lean/Statement/FourWork/Character/ResidueValue.lean` | `3df5a3f0a6de6a60c2b8b8ba89dd6e44fa4d47cb28e98c33f1e31d1dfb7d84dd` |
| `lean/Statement/FourWork/Character/Rigidity.lean` | `843e4ee562071ef4729a61c715b77510b378add7f19b8c02d1e3d36fa9165f88` |
| `lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `lean/Statement/FourPartial.lean` | `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325` |
| `lean/Statement.lean` | `cd6a1dd9bff63ef400559805123c5e6cb7d2d4c9af28cf7f7c24f2cc640abc3c` |

Protocol: `R/.clawcodex/skills/math-team/references/protocol.md`, SHA-256 `e712830b3febe6e3fcaf0479c7aa9fc30f23aa4fcc5e1f45088f736f9c161f2b`.

## 2. Exact statement and conventions

The endpoint is precisely

```lean
ArithmeticStatement.representation_multiple_four (m : ℕ) (hm : 0 < m) :
  ArithmeticStatement.HasRepresentation (4 * m)
```

Expanding the definitions gives positive natural witnesses `a,b`, equality `4*m = a+b`, and both integer Liouville values equal to `-1`. `omega n = n.primeFactorsList.length` counts factors **with multiplicity**, not distinct prime factors. `lambda n = (-1 : ℤ)^omega n`; in particular `lambda 1 = 1`. There is no distinctness requirement. No parity, sign, primality, coprimality, lower bound beyond positivity, or other premise on `m` survives into the endpoint.

`Definitions.lean:10–14` retains the different all-even `Target`. Neither the prose conclusion nor `Assembly.lean:21–24` claims that target. Values at zero are not used in the positive-argument multiplicativity or witness constructions. Although `residueLambda` is defined at zero too, every substantive residue multiplicativity/square application excludes zero explicitly.

## 3. Standalone prose: substantive step checks

References in this section are to `W/PROOF.md`.

### 3.1. Factorization and reduction (§§1–2)

- Additivity of factor-list length under multiplication of positive integers gives complete multiplicativity without a coprimality premise. The sign dichotomy, prime values, `lambda(4)=1`, and positivity of square signs follow correctly. Repeated prime factors are retained throughout.
- If `lambda(m)=1`, witnesses `2m,2m` are positive and each has sign `-1`. This handles **m=1** with `2,2`.
- If `m=2t>0`, exact division gives `t>0`. The pairs `3t,5t` for positive sign of `t`, and `4t,4t` for negative sign of `t`, each sum to `8t=4m` with the required signs. Under the additional negative sign of `m`, only the first case is possible; including the second as a uniform even-m construction is harmless.
- For odd negative-sign `m`, `m≠1`; a prime divisor `p` is odd. In `m=pd`, positivity forces `d>0`, and `-1=(-1)lambda(d)` forces `lambda(d)=1`. Scaling a representation of `4p` by `d` preserves both negative signs and gives exactly `4m`. Removing one occurrence of a prime, even a repeated one, is legitimate. No coprimality is introduced.
- These cases exhaust positive `m`. The converse odd-prime restriction is immediate, so the reduction has the stated logical direction.

### 3.2. Missing-pair implications and local identities (§3)

For the generic completely multiplicative sign-valued `f`, the pair `p,3p` forces `f(3p)=1`, hence `f(3)=-1`. The complement rule only uses arguments strictly between zero and `4p`.

(A) correctly scales a hypothetical negative-negative pair summing to `p` by four. (C) correctly scales a hypothetical positive-positive pair summing to `2p` by two. (B) applies (C) at `p-u`, which is positive and below `2p`. No converse of these one-way implications is silently used.

Both cases in the first local identity (7) are valid: the negative-sign case uses `3(p-x)` and its complement, and the positive-sign case uses (B) at `3x`. The second identity uses (A) or the contradictory pair `p+3x,3(p-x)`. The interval `0<3x<p` makes all these arguments positive and validates all applications. The later global antireflection is proved separately, not extrapolated from this local interval.

### 3.3. Exact ternary division and strict descent (§4)

- For a defect `x+y=p`, both entries are positive and below `p`. If `x=3u`, then `u>0`, `u<p`, and `f(u)=-1`. Implication (A) makes `3(p-u)=3p-x` negative in sign. Implication (C) at `y` makes `2p-y=p+x` negative in sign. Their sum is `4p`, and the stated strict bounds put both in the valid positive range. The same argument excludes divisibility of `y` by three.
- Primality and `p≠3` give `3∤p`. Thus the two nonzero residues of `x,y` modulo three cannot be distinct. If both are 1, or both are 2, both `p+x=2x+y` and `p+y=x+2y` are divisible by three. Therefore the two quotients in (8) are **exact integers**, not floor approximations.
- These quotients are positive and sum to `p`. Applying (C) to the opposite old entry gives sign `-1` at each numerator, and division by the factor with sign `f(3)=-1` gives sign `+1` at both quotients. Hence the construction remains inside the defect class.
- Oddness of `p` excludes `x=y`: equality would make `p=2x` even. After ordering, the integer gap is positive. The new ordered gap is exactly `(y-x)/3`, also an integer and strictly between zero and the old gap. The finite nonempty defect set, if it existed, would have a minimum positive gap; the construction contradicts its minimality.
- Consequently positive-positive pairs of total `p` do not exist; negative-negative pairs are already excluded by (A). The two-valued sign hypothesis then gives antireflection at **every** `0<n<p`.

### 3.4. Circular gaps and signed coefficients (§5.1)

The `n` residues `0,z,...,(n-1)z` are distinct because `z≠0` is cancellable modulo the prime and differences of distinct indices have absolute value below `n<p`. Their ordered circular gaps are positive and sum to `p`. A gap at most `p/n` exists; equality is impossible because `2≤n<p` implies `n∤p`. Thus `d>0` and the essential **strict** bound `nd<p` hold.

Keeping the original indices supplies a nonzero signed coefficient with `|k|<n`. For an ordinary gap, the index difference represents `d`; for the wrapping gap, it represents `d-p`, which is the same residue as `d`. The wrapping case is explicitly covered, not discarded. These bounds also ensure `k` is a nonzero residue. No negative integer is ever passed to `f`.

### 3.5. Least bad multiplier, without periodicity (§§5.2–5.3)

`F` is defined using the unique representative in `1,...,p-1`; it is not asserted to equal `f` at arbitrary congruent positive integers. Antireflection gives the claimed oddness of `F`, so 1 and -1 are good. The proof that good multipliers are closed under products uses goodness twice and is valid on the nonzero residue group.

For a least bad representative `n`, every signed coefficient with `0<|k|<n` is good, by minimality and goodness of -1. For arbitrary nonzero `z`, the short-multiple lemma gives `kz=d`. Crucially, `n,d,nd` are positive representatives below `p`. Therefore (15) follows from **ordinary** complete multiplicativity, without reducing an out-of-range product. Goodness of `k` applied to `z` and to the nonzero residue `nz` gives (16) and (17). Cancelling the nonzero integer sign `F(k)` proves goodness of `n` for every `z`, contradicting minimality.

It follows that every nonzero square has `F`-value 1. A negative-sign integer representative `r` with `0<r<p` that is such a square yields the stated contradiction. This does not presume that `f` itself is periodic or that its value at `p` belongs to a residue character.

### 3.6. Small quadratic-residue prime: local floor/parity proof (§6)

For `p≥7`, `p≡3 (mod 4)`, the exact integer `t=(p+1)/4` is at least two and below `p`. A prime divisor gives `t=rs`, `s≥1`, `2≤r≤t<p`, and `p=4rs-1`.

The signed representatives of `rj`, for `1≤j≤h=(p-1)/2`, exist and are nonzero: neither factor is divisible by `p`. Equal absolute values would force either equal indices or `p∣i+j`; the latter is excluded by `2≤i+j≤p-1`. Their absolute values therefore permute `1,...,h`, and multiplying and cancelling the nonzero `h!` gives `r^h≡(-1)^E`.

The floor indicator in (23) is exactly the indicator of fractional part greater than one half. Fractional parts zero and one half are excluded, respectively, by primality/nondivisibility and oddness of `p`. Reducing modulo two leaves the parity of `S`.

The level count uses precisely `k=1,...,r-1`, because `0<2rj/p<r`. Its threshold is

`kp/(2r) = 2ks - k/(2r)`, with `0<k/(2r)<1`.

Thus its floor is `2ks-1`. The bounds `1≤2ks-1≤h-2s<h` validate the untruncated count at both endpoints. The number of allowed indices is exactly `h-(2ks-1)=2s(r-k)`, which is even. Hence `E` is even and `r^h≡1`.

Finally `2t=h+1`, so the explicitly supplied `A=r^t` has `A²≡r`; it is nonzero modulo `p` because `r` is. This last step needs neither an unstated Euler criterion nor quadratic reciprocity. All estimates include `r=2`, `s=1`, and the boundary prime `p=7`.

### 3.7. Remaining prime cases and assembly (§§7–8)

For `p≥7`, `p≡3 (mod 4)`, the prime `r` supplied above has `lambda(r)=-1`, contradicting residue-square positivity under the missing-representation hypothesis. Every prerequisite of antireflection holds here.

For `p≡1 (mod 4)`, primality implies `p≥5`, so `p` is odd and not three. Inverse pairing of the nonzero residues has only the self-inverse elements ±1: `(a-1)(a+1)=0` in a field proves this assertion. All other inverse pairs have product 1. Pairing instead as `j,p-j` yields `(-1)^h(h!)²=-1`; `h` is even, so `(h!)²=-1`. The factorial residue is nonzero, making this a legitimate contradiction to `F(-1)=-1` and square positivity.

The separate `p=3` witnesses are `5,7`, with sum 12 and both prime. The stated elementary primality check is valid since a composite 5 or 7 would have a factor 2. The three prime cases exhaust odd primes. Applying the already proved reduction covers every positive multiplier, including one. There is no reliance on numerical sampling or an unproved finite search.

## 4. Actual Lean proof and source/dependency audit

### 4.1. Descent, residue values, and finite-bin alternative

`Ternary.lean:8–137` specializes the sign arguments to `lambda`; it already has `lambda_three`, so it need not derive the generic `f(3)` identity. The mod-three exclusions and exact equalities `3*u=p+x`, `3*v=p+y` precede every quotient sign calculation. Its strong induction is on the natural gap; all uses of natural subtraction are protected by the proved strict ordering. The equality branch is separately contradicted by `p%2=1`. Thus its hypotheses `Prime p`, `p≠2`, `p≠3`, and missing representation are sufficient and correctly used.

`Cyclic.lean:10–100` is not the literal sorted-gap proof. It uses representatives `r(i)` and bins `b(i)=floor(n*r(i)/p)`:

1. Representatives below `p` imply `b(i)<n`; field cancellation gives injectivity of `r` for indices below `n`.
2. If an index occupies bin `n-1`, it is not zero. Taking `k=-i`, `d=p-r(i)` gives positivity, `|k|<n`, and `nd≤p`. Equality would imply `n∣p`, impossible for `2≤n<p`, so the bound is strict. The residue equation includes the wrap correctly.
3. Otherwise `n` indices map to `n-1` bins. The finite pigeonhole theorem supplies distinct indices with the same bin. After ordering their distinct representatives, take `d=r(j)-r(i)>0` and `k=j-i`. Common-bin lower/strict-upper inequalities imply `nd<p`. The two index bounds give `|k|<n`, regardless of its sign.

This proves the same quantified short-multiple statement without assuming that equally many points and bins automatically cause a collision.

`ResidueValue.lean` defines `residueLambda p z = lambda z.val`, restricts `GoodMultiplier` to nonzero multipliers and arguments, proves the representative-value bridge only under `n<p`, and derives negation from antireflection. `Rigidity.lean:9–91` implements least-bad reasoning as strong induction on positive representatives. It obtains goodness of a signed `k` from its smaller positive `natAbs` and the proved negation lemma. The bridge to `lambda_mul` has `n>0`, `d>0`, `n<p`, `d<p`, **and `nd<p`**. Both applications of goodness have nonzero arguments, and cancellation is of a proved nonzero integer sign. The square lemma excludes a zero root using `0<n<p`. No modular periodicity is assumed.

### 4.2. Pinned reciprocity alternative in `ResiduePrime.lean`

The exact library statements used are:

- With `[Fact p.Prime]`, `ZMod.exists_sq_eq_neg_one_iff`:
  `IsSquare (-1 : ZMod p) ↔ p % 4 ≠ 3`.
- With `[Fact p.Prime]` and `p≠2`, `ZMod.exists_sq_eq_two_iff`:
  `IsSquare (2 : ZMod p) ↔ p % 8 = 1 ∨ p % 8 = 7`.
- With both prime instances, `exists_sq_eq_prime_iff_of_mod_four_eq_one` takes `p%4=1` and `q≠2` and concludes
  `IsSquare (q : ZMod p) ↔ IsSquare (p : ZMod q)`.
- With both prime instances, `exists_sq_eq_prime_iff_of_mod_four_eq_three` takes `p%4=3`, `q%4=3`, **p≠q**, and concludes
  `IsSquare (q : ZMod p) ↔ ¬ IsSquare (p : ZMod q)`.

These signatures were checked in pinned `LegendreSymbol/Basic.lean:269–286` and `LegendreSymbol/QuadraticReciprocity.lean:45–77,99–167`, not inferred from theorem names.

The local proof establishes exact quarter division, a positive quarter, and `r≤(p+1)/4<p`. For `r=2`, `p+1=8s` gives `p%8=7` and `p≠2`. For odd `r`, `r∣p+1` gives `p=-1` in `ZMod r`. If `r%4=1`, -1 is square modulo `r`, and the reciprocity equivalence is used in the correct direction with library parameters `p:=r, q:=p`. If `r%4=3`, -1 is nonsquare modulo `r`, and the negative reciprocity direction gives the desired square modulo `p`; `r<p` supplies the required distinctness. The two prime instances are installed explicitly. `Nat.exists_prime_and_dvd` requires only that the quarter differ from one, supplied by its bound at least two. This is a valid alternative to, not a formal verification of, the prose floor calculation.

### 4.3. Two-squares alternative and all-m reduction

Pinned `SumTwoSquares.lean:35–38` states:

```lean
Nat.Prime.sq_add_sq {p : ℕ} [Fact p.Prime] (hp : p % 4 ≠ 3) :
  ∃ a b : ℕ, a ^ 2 + b ^ 2 = p
```

`FourPartial.lean:81–92` supplies the prime instance and derives the weaker inequality premise from `p%4=1`, then reverses the sum equality correctly. Its representation construction handles **all** possible returned summands, not merely positive distinct roots: for unequal roots, order them as `a>b`, write `a=b+w` with `w>0`, and use `2(a+b)²,2w²`. Their sum is `4(a²+b²)`, both roots being positive. If the roots coincide, `m=2u²>0` and the already proved multiples-of-eight result applies. A zero smaller root is also permitted in the unequal case. Thus no unjustified positivity is extracted from the library existential.

The source proof of the two-squares theorem goes through the Gaussian-integer nonirreducibility theorem and prime classification. The pertinent statements/proofs at `Zsqrtd/GaussianInt.lean:243–255` and `Zsqrtd/QuadraticReciprocity.lean:34–85` were inspected: they use Gaussian norms and the pinned criterion for -1, not this Liouville representation claim. There is no circular local dependency.

The remaining load-bearing `FourPartial` reductions agree with §2 of the prose: positive-sign diagonal, even multiplier via the two signs at eight, positive-sign cofactor of a prime divisor, and scaling. Its final equivalence first reduces to odd primes, then splits odd primes into residues 1 and 3 modulo four; it separately handles `p=3` by the two-sign seed at 12. Thus `.mpr` in `Assembly.lean:23–24` is the direction that produces **all positive m**, not a conditional reduction presented as a finished endpoint.

The additional mod-four-one factor-list argument in `FourPartial.lean:140–205` also preserves multiplicity: if every prime factor were 3 modulo four, the product modulo four would equal `(-1)^length`, contradicting `m≡1` and `lambda(m)=-1`. These extra lemmas are not required to close the chosen final equivalence. The counting and all-even equivalences elsewhere in `Partial.lean` are not invoked to prove the requested endpoint.

### 4.4. Elementary source preconditions and dependency direction

- `Nat.perm_primeFactorsList_mul` in `Factors.lean:195–202` requires `u≠0`, `v≠0` and gives permutation with the **append** of the two lists. `Partial.omega_mul` supplies these from positivity. `primeFactorsList_prime` gives the singleton list for a prime; `prod_primeFactorsList` requires nonzero input. These are the correct multiplicity-sensitive facts.
- `Nat.exists_prime_and_dvd` in `Prime/Defs.lean:407–408` requires `n≠1`; local applications additionally establish positivity. The prime-divisor classification used to exclude `3∣p` or `n∣p` has exactly the prime and divisibility premises supplied.
- `Finset.exists_ne_map_eq_of_card_lt_of_maps_to`, `Finset/Card.lean:451–458`, requires strictly smaller target cardinality and a map into that target. Both are proved for the no-last-bin branch, with cardinalities `n-1<n`.
- The field instance in `Algebra/Field/ZMod.lean:18–39` requires `[Fact p.Prime]`; each relevant local proof installs it. `val_lt`, `natCast_zmod_val`, and `neg_val` require a nonzero modulus, supplied by primality. `val_natCast_of_lt` has the explicit strict representative bound used locally; `val_pos` supplies positivity from nonzeroness.

The local import/proof graph is acyclic:

`Definitions → Partial → {FourPartial, Ternary, Cyclic, ResidueValue}`;
`{Cyclic, ResidueValue} → Rigidity`;
pinned reciprocity independently supplies `ResiduePrime`;
`{FourPartial, Ternary, Rigidity, ResiduePrime} → Assembly → root Statement`.

No proof on this path invokes `Target`, a scaffold result, or `representation_multiple_four` before proving it. The missing-representation assumption is discharged by contradiction in the prime core. The conditional antireflection premise is supplied by descent, and the prime-core premise of the reduction is supplied by the new unconditional core theorem. Root imports of `Scaffold` and `Smoke` are not backwards dependencies of Assembly; their separate source files were not opened.

## 5. Pinned sources and availability cutoff

Configuration hashes, checked again at the end:

| File | SHA-256 |
|---|---|
| `P/lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `P/lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `P/lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |

They specify Lean `leanprover/lean4:v4.32.2` and Mathlib commit `905b95818eb32af7874a58b427f50c1711a5e96c`. Local Mathlib `git rev-parse HEAD` agrees. A read-only comparison of the following inspected source files with that exact commit returned no differences. The ten substantive source hashes were rechecked unchanged; the last two files were only encountered as locator/search snippets and carry no additional proof weight.

| Path relative to M | SHA-256 |
|---|---|
| `Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `Data/Nat/Prime/Defs.lean` | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `Algebra/Field/ZMod.lean` | `417e8776440d058896b5f05a65d534041a1b7f0b8adb90c011b75486f3e1de22` |
| `Data/ZMod/Basic.lean` | `9a57047615cf4231f3561aef5c75ededf5a6ed6559308f31e241d1d27b2bc00c` |
| `Data/Finset/Card.lean` | `87c674ba5464c7868fb3e253e58a695821bf8841bb4e076bac5d570236dc6229` |
| `NumberTheory/LegendreSymbol/Basic.lean` | `9ac75516bf1585b7af0c71340344ecb3e4c135ac3c06f959d6a3f1e8c2ebd95c` |
| `NumberTheory/LegendreSymbol/QuadraticReciprocity.lean` | `24ffbf256f6f6f7a2617901323c2d532e2d7871c826a8b11f0580b283e994302` |
| `NumberTheory/SumTwoSquares.lean` | `ecc1647de087331c1876ca386b495ff2a83943a428bf140bf6ba8047f9fd80f9` |
| `NumberTheory/Zsqrtd/QuadraticReciprocity.lean` | `8b1fa86e4d60240ff76e788a41fa711a762103b08bd3975b00d6f8eb18f38e88` |
| `NumberTheory/Zsqrtd/GaussianInt.lean` | `3b1ad71a44a0ba95fe172fff4adb35c1c3d0ab3dacc0cacca37d6024c51fd12b` |
| `Data/Set/Card.lean` | `088329ca6b1aeff8522b289ec5cfa6dc3955c0addadfe0e1c33c4954635ecb90` |
| `Data/Fintype/Pigeonhole.lean` | `fa4604d2b1ae480f910e6000ca8814a632299082b48a14f598314303b68cc582` |

The supplied `E/public-availability-witnesses.json` has SHA-256 `051de67ee5bfd81242942075cf9dabacd8cfa96b74abf3733b025456694cc4c1`. I cross-checked its revisions against the manifest and parsed the associated raw public-CI responses, checking exact `head_sha`, public repository status, and creation time before the inclusive cutoff. Relevant witnesses include:

| Component | Public run ID | Created UTC |
|---|---:|---|
| Mathlib pinned commit | 30379053106 | 2026-07-28 16:36:37 |
| Lean `f3b06c705e6c85f5314019d5d3baab0fec5b580c` | 30368480005 | 2026-07-28 14:27:52 |
| plausible | 29253419718 | 2026-07-13 13:20:50 |
| LeanSearchClient | 21928619159 | 2026-02-12 00:28:07 |
| importGraph | 29255410348 | 2026-07-13 13:50:43 |
| proofwidgets | 29253424000 | 2026-07-13 13:20:54 |
| aesop | 29256329889 | 2026-07-13 14:03:38 |
| Qq | 29253426904 | 2026-07-13 13:20:57 |
| batteries | 29282598413 | 2026-07-13 20:29:43 |
| Cli | 29253416514 | 2026-07-13 13:20:47 |

A public workflow's failure does not negate publication of its commit; these records are availability witnesses, not mathematical evidence. The Lean tag metadata maps `v4.32.2` to the above Lean commit, and the release metadata records publication at `2026-07-28T16:34:35Z`. Thus the supplied offline evidence supports availability of all pinned external versions by **2026-07-31 inclusive**. Later metadata collection or proof compilation dates are not being substituted for publication dates. No web request or current-library lookup was made.

Raw availability input hashes:

| Path relative to E | SHA-256 |
|---|---|
| `public-ci-mathlib.json` | `bc12929af93d0eafc008d4d56e287842ef6f682d797b6bb50e7f1481d6f0eeba` |
| `public-ci-mathlib.stdout` | `4337fdc10284dc0c90165a0e4926fde19ebb6ce78dfef2505a3112a277452e00` |
| `public-ci-lean.stdout` | `aeaea1b78e78521606c013a4fafc4b9c0bcaae068cd63f6e97a57bbd26a43826` |
| `public-ci-plausible.stdout` | `7db3a5d1c95ca7d1b1906ec25958d6f1d490a9953154fdf3180f09fd57195e7b` |
| `public-ci-LeanSearchClient.stdout` | `3abdd2daec49091e23e2601a2d77322759da75c6967c6ef67d76cd806ad2d5af` |
| `public-ci-importGraph.stdout` | `5551743d19c9b24dc50743a216975cc324b4bb94618b36fd2839785fbc5fb575` |
| `public-ci-proofwidgets.stdout` | `0af1983970539258f9627cde04d59047e20557b9b5d39248ae2018f728f2cce6` |
| `public-ci-aesop.stdout` | `83bc912b7caf04c68210490e75285c2eba39396aad9cad151c68f2322a36c06d` |
| `public-ci-Qq.stdout` | `e8ff8f4e5970e6943179a83cc2be235f3296ef5153f1d550a3dabf86e69a575b` |
| `public-ci-batteries.stdout` | `3bb8ca7972a48ad427bab042620fed56c5a2a71813ec02621723647adc7fa741` |
| `public-ci-Cli.stdout` | `7db04e1305e996408659d75f8c28ea7d2c4415dcb337834ec3c93a4ee7b36844` |
| `lean-tag.stdout` | `4628281beec64d5f20c18d62f1004f8675be4f437be6263eb30e72fae9813db4` |
| `lean-release.stdout` | `8c58bfbff7a6fca95e743e7de64de75561d605accd9d31e1179b9e3f17c6cbe2` |

## 6. Raw compiler evidence: what it does and does not show

Read the five allowed command JSON records, the relevant default/Assembly build-output entries, the complete trust-zero Assembly output, and the root-import stdin/output. Verified every recorded stdout/stderr byte count and hash; direct Assembly stdout is byte-identical to the trust-zero output. No compiler command was rerun.

The records report exit code zero for `lake build`, `lake build Statement.FourWork.Assembly`, direct `lake env lean Statement/FourWork/Assembly.lean`, `lake env lean -t0 Statement/FourWork/Assembly.lean`, and the root-import `lake env lean -t0 --stdin`. Build output includes replayed dependencies, so it is not described here as a fresh rebuild of all library proofs. The shown warnings are unused-variable warnings in `Partial.lean`, not admitted proof obligations.

The Assembly output prints the exact unconditional endpoint and its axiom list `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` or additional assumption axiom. The same standard axiom set is reported for the load-bearing local theorems and advanced source theorems. Root-import stdin explicitly ascribes the fully expanded positive-witness, multiplicity-counting target to `representation_multiple_four`; the successful output also prints the accepted definitions. The printed `UnfinishedScaffold` is merely a structure requiring a `Target` proof, not a proof of `Target` supplied to this endpoint.

| Stem under I | JSON SHA-256 | stdout SHA-256 |
|---|---|---|
| `01-default-build` | `22bebba237c116219fe39afbeddaa8a9b7b135a17d91da7baa57a0307393aa9f` | `358a0099f8f8f08bfbeecbf9aea658d025fdbb7d9b1019b55474935ce0b0aba1` |
| `02-assembly-build` | `40e7f8bed227c5e1915b5c1133257912ce4d24deafa693b91ae95a7520698ca7` | `32280ddd537c96b38f80e9baf1d101ee1d5d218de9109581c3a4c0b297d6dc9c` |
| `03-assembly-direct` | `ef6fe4e24e8d3331cbcdfcf1fb519519bb2548d44890ccfa6bf63cd322ff9c22` | `c5521b5f017771799eb20205ab92731e45bb20ee241ec108db562d32983e20fd` |
| `04-assembly-trust0` | `f45e2bbb2f269376d806d5998bb14ad80e18b2af00a0a1a1d1fefbbb047b7f1d` | `c5521b5f017771799eb20205ab92731e45bb20ee241ec108db562d32983e20fd` |
| `06-root-import` | `234aa554a767690e0170559004a9966723365d57965a0758464b4872725659db` | `c60cb0c1cc5724afa5f60231819f98a2c88c5a83831992671adbb3f66bc3f2d9` |

All five `.stderr` files are empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
`I/06-root-import.stdin.lean` has SHA-256 `72fd1288ed3d620b02482608fddce0d8dcaf18a227ff6835d71ed66db3c367b0`.

These are inspected historical raw outputs, not this reviewer's execution of the Lean kernel. Hash comparisons establish artifact identity, not mathematical validity; the substantive reasoning above supplies the mathematical review.

## 7. Open obligations, verdict scope, and next action

- **Open load-bearing mathematical obligations for this snapshot: none found.** No repair, additional hypothesis, or counterexample is proposed.
- **Certified scope:** the supplied standalone proof and the mathematical correctness/fidelity of the specified integrated Lean route to `∀ m : ℕ, 0 < m → HasRepresentation (4*m)`, with equal positive witnesses allowed and the prescribed source cutoff.
- **Outside scope:** proving the original all-even `Target`, certifying every unrelated theorem imported by the root, or replacing independent compiler/kernel verification with an LLM verdict. The prose circular-gap, local floor-parity, and inverse-pairing arguments were reviewed in their own right; the finite-bin, pinned-reciprocity, and two-squares Lean alternatives do not constitute line-by-line formalizations of those prose arguments.
- **Recommended next action, leader-owned:** record this scoped PASS against the exact frozen hashes and retain the separate raw formal evidence. Do not promote it to an all-even result. Any mathematical change requires a fresh review of the changed snapshot.
