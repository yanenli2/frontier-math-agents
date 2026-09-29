# Fresh final review A

Mode: CERTIFICATION.

**Verdict: PASS — mathematical correctness and source/statement fidelity of the exact standalone proof and the exact Lean realization of the positive-multiples-of-four lemma.** This is an LLM mathematical review, not Lean compiler or kernel verification. It does not certify the original all-even `ArithmeticStatement.Target`.

## 1. Identity, inputs, and snapshot boundary

Path abbreviations:

- `P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`
- `W = P/waves/multiples-four`
- `M = P/lean/.lake/packages/mathlib`
- `C = ~/.elan/toolchains/leanprover--lean4---v4.32.2`

I read the assigned request, all of `W/PROOF.md`, the actual Lean files below, the protocol, the listed pin configuration and raw public-availability records, and the needed pinned library declarations/proof excerpts. No previous review, author-confidence material, production-status document, or audit-verdict document was consulted. I did not follow the standalone proof's citation to the older NL draft. No agent was spawned, task board changed, candidate repaired, compilation run, or numerical exhaustion performed.

### Exact mathematical artifacts

The following SHA-256 hashes were computed both before reading the candidate and after completing the mathematical review. **Beginning and ending hashes agree in every row.** They match the supplied hashes, including the supplied baseline prefixes.

| Path | Beginning = ending SHA-256 |
|---|---|
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `W/PROOF.md` | `205df4c7b85c9ce40cccf1b42aa92f174fb0365b058466a3c4f2d3ba6968831b` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `P/lean/Statement/FourPartial.lean` | `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325` |
| `P/lean/Statement/FourWork/Assembly.lean` | `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066` |
| `P/lean/Statement/FourWork/Descent/Cyclic.lean` | `09fbee47a60bf7db94d65e871fc49f5d07d60838c8b01cfbfdecb53033471290` |
| `P/lean/Statement/FourWork/Descent/Ternary.lean` | `d6f231fc9aa372f562b19170268b31ae16bdca178185256131232011fd255753` |
| `P/lean/Statement/FourWork/Character/ResiduePrime.lean` | `518f28a33ab98d1a44ea7b544ca7f695e28c48893982caaf72eb4879956763dd` |
| `P/lean/Statement/FourWork/Character/ResidueValue.lean` | `3df5a3f0a6de6a60c2b8b8ba89dd6e44fa4d47cb28e98c33f1e31d1dfb7d84dd` |
| `P/lean/Statement/FourWork/Character/Rigidity.lean` | `843e4ee562071ef4729a61c715b77510b378add7f19b8c02d1e3d36fa9165f88` |

`P/lean/Statement.lean` was inspected only for integration imports. Its beginning SHA-256 was `dc72b845dbb045593ef3a6212b03a54cc0797a29baac132e870aff324cdc5853`; its ending SHA-256 was `cd6a1dd9bff63ef400559805123c5e6cb7d2d4c9af28cf7f7c24f2cc640abc3c`. A second read showed the sole change: addition of `import Statement.FourWork.Assembly` after the five existing imports. This is the permitted import-only promotion, not a change to any reviewed mathematical file. I did not inspect `Scaffold` or `Smoke` or infer their contents from their names.

## 2. Exact target and accepted conventions

The reviewed endpoint is exactly:

```lean
theorem ArithmeticStatement.representation_multiple_four (m : ℕ) (hm : 0 < m) :
  ArithmeticStatement.HasRepresentation (4 * m)
```

`Definitions.lean:6–8` defines `omega` as the length of `primeFactorsList` and `lambda` as an integer power of `-1`. Thus prime factors are counted with multiplicity, not merely distinctly. `Partial.lean:14–20` expands the conclusion to positive natural witnesses `a,b`, equality `4*m = a+b`, and both Liouville values equal to `-1`. Equal witnesses are permitted. The quantifier is every positive natural `m`, including `1`; there is no prime, parity, sign, or coprimality restriction on `m` or the witnesses in the final theorem.

The standalone theorem and `Assembly.lean:21–24` agree with this interface. The Lean function is defined at zero, but no positive-argument multiplicativity application or witness construction in the reviewed proof relies on `lambda 0`. `IsSquare` means existence of a root with `a = r*r`; when used in `ZMod p`, nonzeroness is checked separately rather than silently built into that definition.

## 3. Standalone proof: step and hypothesis checks

### Elementary identities and reduction (§§1–2)

Complete multiplicativity follows from concatenation, up to permutation, of positive prime-factor lists. The positive-factor guards suffice; no coprimality is required. The values at `1`, primes, `4`, and positive squares, and the two possible signs, are correct.

The reduction covers every positive multiplier:

1. If `lambda(m)=1`, the positive pair `2m,2m` has total `4m` and both signs negative. For `m=1`, this is exactly `2,2`.
2. If `m=2t>0`, then `t>0`. The two exhaustive signs of `t` yield `3t,5t` or `4t,4t`. Both rows give total `8t=4m` and negative signs. The proof correctly notes that under the additional assumption `lambda(m)=-1`, only the first row is necessary; it does not use the impossible second subcase to obtain the conclusion.
3. For odd `m` of negative sign, `m>1`. A prime divisor gives `m=pd` with `d>0`, `p` odd, and `lambda(d)=1`. Multiplying any positive negative-sign representation of `4p` by `d` preserves the desired signs and gives total `4m`. Repeated prime factors cause no problem.

### Missing pair, scaling, and local identities (§3)

For the generic completely multiplicative sign function, `f(1)=1` and `f(t²)=1` follow from nonzero sign values. The pair `p,3p` forces `f(3)=-1`. Every complement used lies strictly between zero and `4p`.

Implication (A) uses `4u,4(p-u)` with `0<u<p`; implication (C) uses `2v,2(2p-v)` with `0<v<2p`. In each case the forbidden sign combination really would give two negative witnesses. Applying (C) to `p-u` after (A) gives (B), within the stated domain. The two sign cases proving each identity in (7) are valid. The bound `0<3x<p` gives positivity of `p-x` and the required complements. No local identity is extended outside its interval.

### Ternary gap descent (§4)

If a positive-positive pair `x+y=p` has `x=3u`, then `u>0`, `u<p`, and `f(u)=-1`. The constructed negative-sign pair is `3(p-u),2p-y`, equivalently `3p-x,p+x`, of total `4p`. Exchanging entries gives the same exclusion for `y`.

Primality and `p≠3` imply `3∤p`. Since neither entry is zero modulo three, their residues must agree; the two unequal nonzero residues would make their sum zero modulo three. Therefore **both** divisions `(p+x)/3` and `(p+y)/3` are exact. The new entries are positive, sum to `p`, and have sign `+1`, by (C) and division by the negative sign `f(3)`.

Oddness excludes equal entries. After ordering the entries, the new positive integer gap is exactly one third of the old gap and hence strictly smaller. The minimum-gap argument is well-founded; it does not admit a zero-gap endpoint. Combining exclusion of positive-positive pairs with (A)'s exclusion of negative-negative pairs gives the full antireflection identity for every `0<n<p`.

### Residue multiplicativity and signed cyclic bound (§5)

`F` is defined only by canonical nonzero representatives; no periodicity of the original function is asserted. Primality supplies cancellation, nonzero products, and inverses. Antireflection proves the oddness of `F`, so `1` and `-1` are good multipliers. Closure under products follows by two uses of goodness on nonzero arguments.

For `2≤n<p`, the `n` listed multiples are distinct. All circular gaps, including the wrapping gap, are positive and sum to `p`. A gap at most `p/n` is strictly smaller, because equality would imply `n∣p`, impossible for a prime with `2≤n<p`. Retaining the original indices produces a signed nonzero `k` with `|k|<n`. In the wrapping case the representative difference is `d-p`, still congruent to `d`; the sign of `k` is not discarded.

For a least bad representative `n`, every signed nonzero `k` with `|k|<n` is already good. The short multiple gives `d>0` and **strictly** `nd<p`, so ordinary multiplicativity applies to `n,d,nd` as their actual representatives. Goodness of `k` is used at `z` and at the nonzero residue `nz`, never goodness of the still-unproved multiplier `n`. Cancelling the nonzero integer sign `F(k)` establishes goodness of `n` for arbitrary `z`. This is neither circular nor an appeal to modular periodicity of `f`. Consequently all nonzero squares have value `+1`.

### Small residue prime and the floor parity calculation (§6)

For `p≥7`, `p≡3 (mod 4)`, the integer `t=(p+1)/4` is at least two. A prime divisor gives `t=rs`, `s≥1`, `2≤r≤t<p`, and `p=4rs-1`. With `h=(p-1)/2=2rs-1`, all `rj` for `1≤j≤h` are nonzero modulo `p`.

The signed representatives have distinct absolute values: equality gives either `i=j` or the impossible congruence `i+j=0 (mod p)` with `2≤i+j≤p-1`. Their absolute values therefore permute `1,…,h`. The product comparison and cancellation of the nonzero residue `h!` give `r^h=(-1)^E (mod p)`.

The indicator formula `floor(2rj/p)-2 floor(rj/p)` is exactly the negative-representative indicator. Neither fractional part zero nor one half occurs. Counting the levels of `floor(2rj/p)`, which lies below `r`, introduces precisely `k=1,…,r-1`. For each such `k`, the threshold `kp/(2r)=2ks-k/(2r)` is nonintegral, has floor `2ks-1`, and this floor lies in `[1,h-2s]`. Thus no endpoint truncation is missing: the number of indices is exactly `h-(2ks-1)=2s(r-k)`, which is even. This covers `r=2` as well as odd `r`.

It follows that `E` is even and `r^h=1 (mod p)`. The explicit positive integer root `A=r^t` works because `2t=h+1`. Since its square is the nonzero residue `r`, the resulting square is nonzero. No Euler-criterion converse or quadratic-reciprocity theorem has been left unproved in the standalone argument.

### Prime cases and final assembly (§§7–8)

For primes `p≥7` congruent to three modulo four, specialization to `lambda` satisfies all generic hypotheses; the small prime `r<p` is both a nonzero square and of negative Liouville sign, contradicting residue multiplicativity.

For primes congruent to one modulo four, the inverse-pairing argument is valid on the finite nonzero residue group. Exactly `1,-1` are self-inverse, so the product is `-1`. Pairing the representatives as `j,p-j`, and using evenness of `(p-1)/2`, makes the same product a nonzero square. This contradicts `F(-1)=-1`. This standalone Wilson-type branch is complete even though the Lean realization uses a different branch.

The excluded prime `3` is handled by `12=5+7`, with positivity and primality of both summands justified. Every odd prime is covered by these cases. Returning to §2 covers every positive `m`, including square multipliers, repeated prime factors, even multipliers, and `m=1`. No finite computational search substitutes for a universal argument.

## 4. Actual Lean realization and dependency compatibility

The implementation is a proof of the same endpoint, not a literal formalization of every generic intermediate statement in the prose. The differences below are justified rather than silently identified.

- **`Partial.lean:43–159`:** supplies precisely the positive-factor Liouville identities, signed scaling, diagonal construction, and the two-sign seed at eight. The scaling theorem preserves both positivity guards and the exact sum.
- **`FourPartial.lean:8–129,207–241`:** supplies the seed at twelve, even-multiplier and positive-sign cases, positive-sign cofactor, and both prime-core equivalences. In the reverse odd-prime reduction a divisor `p=2` would explicitly make `m` even. The reverse three-mod-four reduction separates `p=3`, primes congruent to one modulo four, and the remaining primes, whose lower bound is at least seven. The `.mpr` used by `Assembly` is the required direction, not its converse.
- **`Ternary.lean:8–137`:** specializes immediately to `lambda`. It legitimately uses the already-proved value `lambda(3)=-1`; it need not formalize the generic derivation from `f(p)=-1`. Its two scaling implications have the exact positive and upper-bound hypotheses. The mod-three split establishes divisibility before introducing natural quotients. Equations `3u=p+x`, `3v=p+y` establish positivity, sum, order, and strict gap decrease without truncated-subtraction artifacts. Strong induction is on the natural gap, with the equal-entry case independently excluded using oddness. The final antireflection statement quantifies every positive `n<p`.
- **`Cyclic.lean:10–100`:** uses bins instead of sorting circular gaps. With `r(i)=val(i*z)` and `b(i)=floor(n*r(i)/p)`, bins lie in `range n`; cancellation proves injectivity of `r` on `range n`. If the last bin occurs, its index is nonzero and `k=-i`, `d=p-r(i)` give `nd≤p`; equality is excluded by `n∤p`. If the last bin does not occur, `n` indices map into `n-1` bins. Pigeonhole gives two distinct indices with equal bins. Ordering their distinct residues gives `d>0`, `nd<p` from the floor bounds, and the signed difference of indices satisfies `0<|k|<n`. Both orientations and the wrap case are covered.
- **`ResidueValue.lean:9–51`:** defines `residueLambda` on all residues but restricts `GoodMultiplier` to nonzero multipliers and arguments. The nonzero guards give positive canonical values, and prime `p` gives `val<p`. `residueLambda_natCast` requires the exact strict representative bound. `goodMultiplier_neg` directly implements the sign change permitted by antireflection.
- **`Rigidity.lean:9–91`:** strong induction on positive representatives implements the least-bad argument. `k.natAbs>0` follows from `k≠0`; both integer-sign cases are covered. The only bridge from ordinary multiplication uses `n*d<p`, `n<p`, and `d<p`. Cancellation is by a residue value proved to be `±1`, not by a possibly zero quantity. For an `IsSquare` witness, `0<n<p` first makes the target residue nonzero and then excludes a zero root. The conclusion is the actual integer equality `lambda n=1`.
- **`ResiduePrime.lean:9–59`:** proves the same small-prime conclusion by the pinned supplementary laws and quadratic reciprocity, not the standalone floor calculation. The quarter is exact and positive. Its prime divisor satisfies `r≤(p+1)/4<p`, so the primes are distinct where required. All three branches and theorem directions are checked in §5 below.
- **`Assembly.lean:10–24`:** under the missing-representation assumption, `p≥7` supplies the exclusions `p≠2,3`. Antireflection and the small-prime square lemma apply to the same prime `p`. Primality gives `r>0` and `lambda(r)=-1`; rigidity gives `lambda(r)=1`. Contradiction proves the residual prime case, and the reverse core equivalence yields the exact unrestricted positive-multiplier theorem.

The load-bearing dependency graph has no route back from these intermediate lemmas to the final theorem. The unrelated all-even equivalences and counting statements present in the baseline are not invoked to establish this endpoint and are not independently recertified here. Source `#check` and `#print axioms` commands are not compiler output or axiom evidence.

## 5. Pinned library/source audit

`lakefile.toml` and `lake-manifest.json` pin Mathlib to `905b95818eb32af7874a58b427f50c1711a5e96c`; the local Mathlib checkout's `HEAD` is that commit. Read-only diffs against that commit were empty for the consulted mathematical source files listed below. Both project and Mathlib toolchain files specify `leanprover/lean4:v4.32.2`; the installed header identifies version `4.32.2`.

### Exact usable theorem types and guards

1. `Mathlib/Data/Nat/Factors.lean:196–202`:
   `perm_primeFactorsList_mul {a b} (ha : a ≠ 0) (hb : b ≠ 0)` gives a permutation of `(a*b).primeFactorsList` with the concatenation of the two lists. The caller supplies positivity, hence both nonzero guards. This is the unrestricted multiplicity theorem, not the coprime-only variant. `primeFactorsList_prime` gives `[p]` under `Nat.Prime p`; `prod_primeFactorsList` requires `n≠0`.
2. `Mathlib/Data/Nat/Prime/Defs.lean:407–408`: `n≠1 → ∃p, Prime p ∧ p∣n`. In the two uses, the cofactor reduction has positive negative-sign `m≠1`, and the quarter is at least two. `Prime.eq_one_or_self_of_dvd` excludes divisors strictly between one and the prime. `Prime.eq_two_or_odd` in `Prime/Basic.lean:41–43` supplies the exhaustive parity split.
3. `Mathlib/Data/Finset/Card.lean:451–458`: `card t < card s` and `Set.MapsTo f s t` imply two distinct members of `s` have the same image. `Cyclic` supplies `s=range n`, `t=range(n-1)` and proves the mapping condition before invoking it.
4. `Mathlib/Algebra/Field/ZMod.lean:18–39` provides the field/domain under `[Fact p.Prime]`; each caller installs this from `hp`. The consulted `ZMod` value lemmas have the appropriate nonzero-modulus or representative-bound guards. `natCast_eq_zero_iff a b` is exactly `(a : ZMod b)=0 ↔ b∣a`. `Int.natAbs_eq` covers `k=|k|` or `k=-|k|`, and `Nat.strong_induction_on` permits only strictly smaller indices.
5. `Mathlib/NumberTheory/LegendreSymbol/Basic.lean:269–286`, under `[Fact p.Prime]`:
   `IsSquare (-1 : ZMod p) ↔ p % 4 ≠ 3`.
6. `Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean:45,74–77`, under `[Fact p.Prime]` and explicit `p≠2`:
   `IsSquare (2 : ZMod p) ↔ p % 8 = 1 ∨ p % 8 = 7`.
   In the divisor branch `r=2`, the exact identity `p+1=4*(2*s)` yields the second alternative `p%8=7`; `p≥7` gives the non-two guard.
7. The same file, lines 99,155–160, under `[Fact p.Prime] [Fact q.Prime]`, has
   `p%4=1 → q≠2 → (IsSquare (q : ZMod p) ↔ IsSquare (p : ZMod q))`.
   `ResiduePrime` instantiates its parameters as `p:=r, q:=p` and uses `.mp`. Since the original `p` equals `-1` modulo `r`, the minus-one theorem with `r%4=1` establishes the left side. The original `p≥7` supplies `q≠2`. No unmentioned distinctness guard is needed for this version.
8. The same file, lines 164–167, has
   `p%4=3 → q%4=3 → p≠q → (IsSquare (q : ZMod p) ↔ ¬IsSquare (p : ZMod q))`.
   Here the parameters are the original `p,r`, with distinctness from `r<p`. The caller uses `.mpr`; `p=-1 (mod r)` and `r%4=3` give the required nonsquare via item 5. This is the negative, not positive, reciprocity branch.
9. `Mathlib/NumberTheory/SumTwoSquares.lean:35–38`:
   `{p : ℕ} [Fact p.Prime] (hp : p % 4 ≠ 3) → ∃a b : ℕ, a²+b²=p`.
   `FourPartial` installs the prime instance and derives the explicit guard from `p%4=1`, then reverses the equality. It does not assume the two roots are positive or distinct. Its representation construction orders unequal roots and uses `2(a+b)²,2(a-b)²`; the difference is strictly positive in that branch. If roots are equal, positive `m=2u²` uses the multiple-of-eight lemma instead. A zero root is harmless in the unequal branch. Thus the library's actual conclusion, without stronger root conditions, suffices. The Gaussian-integer source excerpts show this is the genuine prime sum-of-two-squares theorem, independent of the candidate.

These library alternatives justify the actual Lean realization. The standalone text's statement that it does not invoke quadratic reciprocity or sum-of-two-squares is true of that text, not a description of the Lean dependency graph.

### Cutoff evidence

I read `P/formal/environment/public-availability-witnesses.json` as raw evidence, not as a prior audit. Its Mathlib records identify the exact pinned head SHA in public GitHub Actions runs created on **2026-07-28**, including run `30385574037`. Its Lean record identifies SHA `f3b06c705e6c85f5314019d5d3baab0fec5b580c` in run `30368480005`, also created **2026-07-28**. The resolved manifest hashes for plausible, LeanSearchClient, importGraph, proofwidgets, aesop, Qq, batteries, and Cli also match entries with public run timestamps before the cutoff (February 12 or July 13–15, 2026). These supplied records meet the requested `≤2026-07-31` availability boundary; workflow success/failure labels are not being used as mathematical evidence. No current online source or external browsing was used. Compiler/toolchain provenance verification beyond the supplied pins and records remains with the separate formal-verification assignment.

### Additional input fingerprints

Paths below are relative to the stated prefix. Source searches/read excerpts, rather than an audit of all transitive library implementations, supplied the needed declarations and guards.

| Prefix/path | SHA-256 |
|---|---|
| `.clawcodex/skills/math-team/references/protocol.md` | `e712830b3febe6e3fcaf0479c7aa9fc30f23aa4fcc5e1f45088f736f9c161f2b` |
| `P/lean/lean-toolchain` and `M/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `P/lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `P/lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |
| `P/formal/environment/public-availability-witnesses.json` | `051de67ee5bfd81242942075cf9dabacd8cfa96b74abf3733b025456694cc4c1` |
| `M/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean` | `24ffbf256f6f6f7a2617901323c2d532e2d7871c826a8b11f0580b283e994302` |
| `M/Mathlib/NumberTheory/LegendreSymbol/Basic.lean` | `9ac75516bf1585b7af0c71340344ecb3e4c135ac3c06f959d6a3f1e8c2ebd95c` |
| `M/Mathlib/NumberTheory/SumTwoSquares.lean` | `ecc1647de087331c1876ca386b495ff2a83943a428bf140bf6ba8047f9fd80f9` |
| `M/Mathlib/NumberTheory/Zsqrtd/QuadraticReciprocity.lean` | `8b1fa86e4d60240ff76e788a41fa711a762103b08bd3975b00d6f8eb18f38e88` |
| `M/Mathlib/NumberTheory/Zsqrtd/GaussianInt.lean` | `3b1ad71a44a0ba95fe172fff4adb35c1c3d0ab3dacc0cacca37d6024c51fd12b` |
| `M/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `M/Mathlib/Data/Nat/Prime/Defs.lean` | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `M/Mathlib/Data/Nat/Prime/Basic.lean` | `b97e83d65681b68b3ad1f4bdfd36defd0a30aa173cf726b3d2807acf8bde5027` |
| `M/Mathlib/Data/Nat/Init.lean` | `6eac43b5c217af7e02be819026cdbba38b24810659d1fc1dc7d90d6f78c7d3e3` |
| `M/Mathlib/Data/ZMod/Basic.lean` | `9a57047615cf4231f3561aef5c75ededf5a6ed6559308f31e241d1d27b2bc00c` |
| `M/Mathlib/Algebra/Field/ZMod.lean` | `417e8776440d058896b5f05a65d534041a1b7f0b8adb90c011b75486f3e1de22` |
| `M/Mathlib/Algebra/Group/Even.lean` | `1180fa9ac282e55257e95c8402acd7314fcbd0a18bcfdede92a3cde16e1db630` |
| `M/Mathlib/Data/Finset/Card.lean` | `87c674ba5464c7868fb3e253e58a695821bf8841bb4e076bac5d570236dc6229` |
| `C/src/lean/Init/Data/Int/Order.lean` | `06a375f0e855f6b132de56d79be4405691db1a14be3fe52fa8814df9b45cea68` |
| `C/include/lean/version.h` | `50d1962bc70ec9399c6501af7648e4497f9bf1ef72b475336032c2df147a67ad` |

## 6. Open obligations, verdict scope, and next action

**No unresolved load-bearing mathematical gap or statement/source mismatch was found in the assigned snapshot.** The standalone proof covers all its cases, and the Lean source realizes the same positive-multiples-of-four conclusion with valid dependency guards and justified alternative library arguments. No repair is proposed.

This PASS does not assert that Lean accepted the files, that an axiom audit passed, or that all imports outside the assigned source closure were inspected. Those are distinct formal-verification obligations. It also does not assert `ArithmeticStatement.Target` for even numbers congruent to two modulo four.

Recommended next action: the leader should combine this fixed-hash mathematical packet with the separately assigned pinned compiler/kernel and axiom evidence for the unchanged `Assembly` and its import-only promotion. Any later change to a reviewed mathematical file requires a fresh review of the affected snapshot. Only this assigned report was written by this reviewer.
