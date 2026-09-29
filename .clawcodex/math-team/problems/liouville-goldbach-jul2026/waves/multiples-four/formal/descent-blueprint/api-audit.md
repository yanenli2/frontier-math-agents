# Pinned API and provenance audit

Mode: CERTIFICATION — library inspection and type probes, not proof of any proposed helper.

Paths use the P/W/B/M abbreviations from `blueprint.md`. All library source below is from local mathlib commit `905b95818eb32af7874a58b427f50c1711a5e96c`, commit timestamp `2026-07-28T18:36:13+02:00`. The inspected primary files have no tracked local changes. No external source, network retrieval, toolchain installation, or dependency update was used.

## 1. Cache and actual probe status

| Module / API family | Source present | `.olean` present at inspection | Actual status |
|---|---|---|---|
| `Statement.Partial` | yes | yes | imported successfully in both passing probes |
| `Mathlib.Data.ZMod.Basic` | yes | yes | successful type probe |
| `Mathlib.Data.Finset.Card` | yes | available transitively | successful type and axiom probe |
| `Mathlib.NumberTheory.LegendreSymbol.Basic` | yes | yes | successful type and neg-one-criterion axiom probe |
| `Mathlib.NumberTheory.LegendreSymbol.QuadraticReciprocity` | yes | **no** | exact source types/guards inspected; no elaboration or axiom result claimed |
| `Mathlib.NumberTheory.DiophantineApproximation.Basic` | yes | **no** | exact source type inspected; no elaboration or axiom result claimed |
| `Mathlib.NumberTheory.WellApproximable` | yes | **no** | narrow AddCircle alternative inspected and rejected as unnecessarily heavy |
| `Mathlib.Data.Int.Lemmas` | yes | **no** | exact signed-difference bound exists in source; not imported by passing probes |

Working directory for all probes: `P/lean`.

Commands actually run, each bounded by a 90-second tool timeout:

```text
lake env lean B/ApiProbe.lean              -> exit 1
lake env lean B/ApiProbeVerified.lean      -> exit 0
lake env lean B/SignatureTypeProbe.lean    -> exit 0
```

The actual commands used absolute B paths and redirected output only into B. No `.olean` output was requested from these probe files. The signature probe contains definitions and `#check` expressions, not theorem bodies or axioms. Its warnings concern unused names of proof binders in types; the hypotheses must not be removed on that basis.

The initial failed probe is retained. Corrections:

- `ZMod.natCast_injOn_lt` was not a known constant in that environment. The plan does not use it; recover injectivity on `[0,p)` by applying `ZMod.val` and `ZMod.val_natCast_of_lt` instead.
- `Int.natAbs_ofNat` was not a known constant. The actually probed name is `Int.natAbs_natCast`.
- `Int.natAbs_coe_sub_coe_lt_of_lt` was unavailable under the tested imports, but is an actual theorem in `Mathlib.Data.Int.Lemmas:77–81`; that separate module is not cached. Use the elementary absolute-value argument or build/import that narrow module explicitly.

A successful probe of known API types is not acceptance of any proposed new theorem.

## 2. Exact C APIs and guard audit

Source: `M/Mathlib/NumberTheory/LegendreSymbol/Basic.lean:282–286`.

```lean
namespace ZMod
variable {p : ℕ} [Fact p.Prime]
theorem exists_sq_eq_neg_one_iff :
  IsSquare (-1 : ZMod p) ↔ p % 4 ≠ 3
end ZMod
```

This exact constant was probed. `#print axioms` returned `[propext, Classical.choice, Quot.sound]`. It does not require `p≠2`. In C, instantiate it with the prime r. For `r%4=1`, its right side is true, so −1 is a square. For `r%4=3`, an `IsSquare (-1)` witness would yield the false inequality `r%4≠3`, so −1 is not a square.

Source: `M/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean:71–77`.

```lean
namespace ZMod
variable {p : ℕ} [Fact p.Prime]
theorem exists_sq_eq_two_iff (hp : p ≠ 2) :
  IsSquare (2 : ZMod p) ↔ p % 8 = 1 ∨ p % 8 = 7
end ZMod
```

C's `r=2` case derives `p%8=7` from `p+1=8*s`. The guard `p≠2` follows from `7≤p`. Apply the reverse implication to the right disjunct. Do not apply odd-prime reciprocity at r=2.

Source: same file, section variables at line 99 and theorem at 153–160.

```lean
namespace ZMod
variable {p q : ℕ} [Fact p.Prime] [Fact q.Prime]
theorem exists_sq_eq_prime_iff_of_mod_four_eq_one
    (hp1 : p % 4 = 1) (hq1 : q ≠ 2) :
  IsSquare (q : ZMod p) ↔ IsSquare (p : ZMod q)
end ZMod
```

For C's `r%4=1` case, use library parameters `(p:=r)`, `(q:=p)`. Both primality instances come from explicit `hp`, `hr`. The mod-4 premise is about r; the not-2 premise is about the original p. The resulting iff is

```text
IsSquare (original p : ZMod r) ↔ IsSquare (r : ZMod original p).
```

Prove the left side from `(original p : ZMod r)=-1` and the neg-one criterion; take `.mp`. This theorem does not need a distinctness hypothesis.

Source: same file, 162–167.

```lean
namespace ZMod
variable {p q : ℕ} [Fact p.Prime] [Fact q.Prime]
theorem exists_sq_eq_prime_iff_of_mod_four_eq_three
    (hp3 : p % 4 = 3) (hq3 : q % 4 = 3) (hpq : p ≠ q) :
  IsSquare (q : ZMod p) ↔ ¬ IsSquare (p : ZMod q)
end ZMod
```

For C's `r%4=3` case, use `(p:=p)`, `(q:=r)` in the original naming. Distinctness follows from `r≤(p+1)/4<p`; never omit this guard. Rewrite the right-hand residue as −1 and use its nonsquareness modulo r; take `.mpr`. The mod-4 premises already exclude 2 for both primes.

### Exact arithmetic bridge for C

Before using these APIs, prove `4*((p+1)/4)=p+1` from `p%4=3`. Positivity and `p≥7` give `2≤(p+1)/4<p`. For r prime dividing the quarter, choose `s` with `(p+1)/4=r*s`. This gives `p+1=4*(r*s)`, hence `(p : ZMod r)=-1`. In the r=2 case it gives `p+1=8*s`.

This bridge supplies every modulus, nonzero, distinct-prime, and special-prime guard. It is independent of lambda and of any representation or character law, so the library applications are not circular.

### Acceptance boundary for the reciprocity replacement

The three reciprocity/supplementary declarations above were inspected in exact pinned source; they were **not** successfully imported or axiom-printed during this assignment because their module is uncached. No placeholder axiom was introduced. The C implementation owner must obtain/build the same-pin module with authorization, then probe these constants and print their axiom sets. An example targeted project command for that owner is:

```text
lake build Mathlib.NumberTheory.LegendreSymbol.QuadraticReciprocity
```

That is a proposed future setup action, not a command run by the blueprinter. If it fails or exceeds budget, report the setup blocker. Do not replace a failed import with a mathematical assumption.

The source implementation uses the Legendre symbol and finite-field quadratic characters/Gauss sums, not the submitted NL floor-count derivation. This proof-method replacement is explicitly allowed by the assignment, but its exact theorem application still requires fidelity review. No post-cutoff library or literature theorem is needed.

## 3. Cyclic short-multiple search: what exists and what does not follow automatically

### A real Dirichlet API with exactly the useful denominator

Source: `M/Mathlib/NumberTheory/DiophantineApproximation/Basic.lean:95–129`.

```lean
namespace Real
theorem exists_int_int_abs_mul_sub_le (ξ : ℝ) {n : ℕ} (n_pos : 0 < n) :
  ∃ j k : ℤ, 0 < k ∧ k ≤ n ∧
    |(k : ℝ) * ξ - j| ≤ 1 / ((n : ℝ) + 1)
end Real
```

The source writes the final casts by elaboration; the displayed type makes them explicit. This result holds for every real ξ, including the rational ratio needed here. No irrationality hypothesis is required. Its source proof is finite pigeonhole plus the end interval near 1.

For target G with natural parameter n, instantiate the library theorem at `N=n-1` and `ξ=(z.val : ℝ)/(p : ℝ)`. The guard `N>0` follows from `2≤n`. Let `e=k*(z.val : ℤ)-j*(p : ℤ)`. Clearing the strictly positive denominators gives `n*|e|≤p`. Cast e modulo p to get `(k : ZMod p)*z`; it is nonzero because `0<k<n<p`, primality, and `z≠0`. Thus e is nonzero. Set `d=e.natAbs`, and choose coefficient k or −k according to e's sign to obtain a positive residue representative d. The bound is strict because equality `n*d=p` would give `n∣p` with `2≤n<p`. This proves exactly the proposed signed-coefficient conclusion, not just a non-strict approximation.

This API is genuinely usable mathematically, but not cached or probed here. The recommended direct finite-bins proof avoids its import and real/integer denominator clearing.

A second source theorem at lines 135–140 is:

```lean
namespace Real
theorem exists_nat_abs_mul_sub_round_le (ξ : ℝ) {n : ℕ} (n_pos : 0 < n) :
  ∃ k : ℕ, 0 < k ∧ k ≤ n ∧
    |(k : ℝ) * ξ - round ((k : ℝ) * ξ)| ≤ 1 / ((n : ℝ) + 1)
end Real
```

It has the same relevant bound but introduces rounding unnecessarily. It is not a new dependency in the proposed graph.

### Finite API actually probed and recommended

Source: `M/Mathlib/Data/Finset/Card.lean:447–458`.

```lean
namespace Finset
variable {α β : Type*} {s : Finset α} {t : Finset β}
theorem exists_ne_map_eq_of_card_lt_of_maps_to
    (hc : t.card < s.card) {f : α → β} (hf : Set.MapsTo f s t) :
  ∃ x ∈ s, ∃ y ∈ s, x ≠ y ∧ f x = f y
end Finset
```

Exact guard application: `s=Finset.range n`, `t=Finset.range (n-1)`, and `f i=n*r(i)/p`, in the branch where no representative lies in bin n−1. `Finset.card_range` and `2≤n` give the strict card comparison. Quotient bounds and the branch assumption give MapsTo. The separate final-bin branch is necessary: without it there is no reason n points should fit into only n−1 bins.

The axiom probe returned `[propext, Classical.choice, Quot.sound]`. This supplies only two distinct indices with the same bin; all modular nonzero, orientation, short-gap, and signed-coefficient obligations remain in G's proof.

### Inspected alternatives not adopted

- `Mathlib.NumberTheory.WellApproximable:356–361` has `AddCircle.exists_norm_nsmul_le`, with bound `T/(n+1)` and period/typeclass parameters. It requires more topology/measure/norm infrastructure than the integer or Real route. It is not cached and is not an assumed dependency.
- `Mathlib.Order.Interval.Finset.Gaps` computes complements of finitely many ordered closed intervals, and `Mathlib.Algebra.BigOperators.Group.Finset.Gaps` sums those gaps. These are not an already packaged cyclic short-multiple theorem. Translating n points to n cyclic gaps would still require endpoint and wraparound work. No name from those files is used in the proof graph.

The bounded inspection did not find a direct `ZMod` theorem with the full desired G signature. This is a search result, not a claim that no equivalent result exists anywhere in the library.

## 4. Representation and sign APIs, exact probed types

From the approved `Statement.Partial`:

```lean
namespace ArithmeticStatement
theorem lambda_sign {n : ℕ} (hn : 0 < n) :
  lambda n = (1 : ℤ) ∨ lambda n = (-1 : ℤ)
theorem lambda_mul {u v : ℕ} (hu : 0 < u) (hv : 0 < v) :
  lambda (u * v) = lambda u * lambda v
theorem lambda_prime {p : ℕ} (hp : Nat.Prime p) :
  lambda p = (-1 : ℤ)
theorem lambda_three : lambda 3 = (-1 : ℤ)
end ArithmeticStatement
```

No coprimality guard occurs in `lambda_mul`; adding one to a new helper would break the intended source bridge and needlessly complicate repeated-prime cofactors.

## 5. Residue representatives and positivity APIs

Exact useful forms, elaboration-probed under `Statement.Partial` plus `LegendreSymbol.Basic`:

```lean
namespace ZMod
theorem val_pos {n : ℕ} {a : ZMod n} : 0 < a.val ↔ a ≠ 0
theorem val_lt {n : ℕ} [NeZero n] (a : ZMod n) : a.val < n
lemma val_natCast_of_lt {n a : ℕ} (h : a < n) : (a : ZMod n).val = a
theorem natCast_zmod_val {n : ℕ} [NeZero n] (a : ZMod n) :
  (a.val : ZMod n) = a
theorem neg_val {n : ℕ} [NeZero n] (a : ZMod n) :
  (-a).val = if a = 0 then 0 else n - a.val
theorem natCast_eq_zero_iff (a b : ℕ) : (a : ZMod b) = 0 ↔ b ∣ a
theorem intCast_zmod_eq_zero_iff_dvd (a : ℤ) (b : ℕ) :
  (a : ZMod b) = 0 ↔ (b : ℤ) ∣ a
theorem natCast_eq_natCast_iff (a b c : ℕ) :
  (a : ZMod c) = (b : ZMod c) ↔ Nat.ModEq c a b
end ZMod
```

Principal source locations: `Data/ZMod/Basic.lean:61–96,205–211,518–519,965–970,1015–1032`. In prime-modulus proofs, `letI : Fact p.Prime := ⟨hp⟩` provides the needed field and nonzero-modulus instances. Do not accidentally substitute the special `ZMod 0` representative conventions for prime-modulus representatives.

The exact square-witness equivalence was also probed:

```lean
theorem isSquare_iff_exists_sq {α : Type*} [Monoid α] (a : α) :
  IsSquare a ↔ ∃ r, a = r ^ 2
```

Its equality orientation is `a=r^2`, not `r^2=a`. At B8, the positive representative `0<n<p` excludes a zero square root.

## 6. Small arithmetic APIs actually probed

```lean
Nat.Prime.eq_one_or_self_of_dvd :
  ∀ {p : ℕ}, Nat.Prime p → ∀ m : ℕ, m ∣ p → m = 1 ∨ m = p
Nat.Prime.dvd_iff_eq :
  ∀ {p a : ℕ}, Nat.Prime p → a ≠ 1 → (a ∣ p ↔ p = a)
Nat.Prime.eq_two_or_odd :
  ∀ {p : ℕ}, Nat.Prime p → p = 2 ∨ p % 2 = 1
Nat.odd_mod_four_iff :
  ∀ {n : ℕ}, n % 2 = 1 ↔ n % 4 = 1 ∨ n % 4 = 3
Nat.exists_prime_and_dvd :
  ∀ {n : ℕ}, n ≠ 1 → ∃ p, Nat.Prime p ∧ p ∣ n
Nat.le_of_dvd : ∀ {m n : ℕ}, 0 < n → m ∣ n → m ≤ n
Nat.mul_div_le : ∀ m n : ℕ, n * (m / n) ≤ m
Nat.div_lt_iff_lt_mul : ∀ {k x y : ℕ}, 0 < k → (x / k < y ↔ x < y * k)
Nat.div_mul_le_self : ∀ m n : ℕ, m / n * n ≤ m
Nat.lt_mul_div_succ : ∀ {b : ℕ} (a : ℕ), 0 < b → a < b * (a / b + 1)
Nat.mul_div_cancel' : ∀ {n m : ℕ}, n ∣ m → n * (m / n) = m
Nat.div_mul_cancel : ∀ {n m : ℕ}, n ∣ m → m / n * n = m
Int.natAbs_neg : ∀ a : ℤ, (-a).natAbs = a.natAbs
Int.natCast_natAbs : ∀ n : ℤ, (n.natAbs : ℤ) = |n|
Int.natAbs_natCast : ∀ n : ℕ, (n : ℤ).natAbs = n
Nat.strong_induction_on : ∀ {P : ℕ → Prop} (n : ℕ),
  (∀ n : ℕ, (∀ m < n, P m) → P n) → P n
```

`Nat.exists_prime_and_dvd` only requires `n≠1`, which includes n=0. Therefore C must establish the separate positive quarter bound before using the returned divisor bound. `Nat.mul_div_cancel'` and `Nat.div_mul_cancel` require exact divisibility: do not apply them before proving the third/quarter is integral.

Source-only optional signed difference API (`Data/Int/Lemmas.lean:77–81`):

```lean
namespace Int
theorem natAbs_coe_sub_coe_lt_of_lt {a b n : ℕ}
    (a_lt_n : a < n) (b_lt_n : b < n) :
  natAbs (a - b : ℤ) < n
end Int
```

Here `a-b : ℤ` is integer subtraction of the two natural casts, not a cast of truncated natural subtraction. This exact distinction is why G's coefficient type is ℤ.

## 7. Primary source hashes

| Relative path under M | SHA-256 |
|---|---|
| `Mathlib/NumberTheory/LegendreSymbol/Basic.lean` | `9ac75516bf1585b7af0c71340344ecb3e4c135ac3c06f959d6a3f1e8c2ebd95c` |
| `Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean` | `24ffbf256f6f6f7a2617901323c2d532e2d7871c826a8b11f0580b283e994302` |
| `Mathlib/NumberTheory/DiophantineApproximation/Basic.lean` | `abc84df69b88508535f62fd151f496b3587000aca07e5e3a2f098ce3ffb6b87d` |
| `Mathlib/Data/Finset/Card.lean` | `87c674ba5464c7868fb3e253e58a695821bf8841bb4e076bac5d570236dc6229` |
| `Mathlib/Data/ZMod/Basic.lean` | `9a57047615cf4231f3561aef5c75ededf5a6ed6559308f31e241d1d27b2bc00c` |
| `Mathlib/Data/Int/Lemmas.lean` | `bbaef1cd08f146a8ab0125221eb704808fe24d7583b9cebb50516c0238cc9b44` |

These identify inspected source files, not a new audit of every transitive library proof. The implementation's actual imports, successful compilation, final transitive axiom sets, and frozen statement/definition identities must be recorded at acceptance.
