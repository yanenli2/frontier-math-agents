Mode: DISCOVERY — conjectural; no proof weight.

# Lean dependency blueprint v1

## 1. Deliverable and next target

**Recommendation:** review the elementary interfaces, then assign the generator `ArithmeticStatement.representation_multiple_eight` as the first substantial partial theorem. Prove its small arithmetic dependencies first. Next review and prove the actual ordered-count bridge and the exact signed identity, independently of any global positivity claim. Defer the optional `2pq` reduction until those deliverables exist.

This is architecture, not a proof or acceptance report. No new mathematical theorem was proved. `interfaces-v1.lean` is a **code-only signature-text bundle**: definitions have bodies, but every proposed theorem's proof body is erased. It is deliberately not a compilable theorem module; do not import it, interpret its signatures as assumptions, or fill the global holes with axioms. Exact helper signatures are there; the source/dependency map is `map-v1.md`.

All new files are under `P/formal/blueprinter/`, where

`P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`.

Protected definitions, existing project files, and master development were not edited. No external search, dependency update, cache download, proof search, or nested agent was used.

## 2. Exact target and existing project

The authoritative imported module is `Statement.Definitions`, namespace `ArithmeticStatement`. The approved snapshot and the project's copy have identical SHA-256:

`79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d`.

Its definitions are exactly:

```lean
def omega (n : ℕ) : ℕ := n.primeFactorsList.length
def lambda (n : ℕ) : ℤ := (-1 : ℤ) ^ omega n

def Target : Prop :=
  ∀ N : ℕ, Even N → 2 < N →
    ∃ a b : ℕ,
      0 < a ∧ 0 < b ∧ N = a + b ∧
        lambda a = (-1 : ℤ) ∧ lambda b = (-1 : ℤ)
```

Source: `request.md:5-14`; approved code: `formal/approved-v1/Definitions.lean:6-14`. Natural inputs are the already-approved encoding of positive integers. This blueprint neither replaces that encoding nor adds a second integer-valued lambda. Any demand for a separate integer/natural transport theorem goes back to statement review, not into an assumed helper.

The project currently has only `Statement.Definitions`, `Statement.Scaffold`, `Statement.Smoke`, and the root import module. `UnfinishedScaffold.result : Target` is a field of an uninhabited-by-this-development structure, **not a proof of Target**. Evaluations in `Smoke.lean` are not general theorems. No helper name proposed here exists in those inspected project modules.

The proposed final declaration name is `ArithmeticStatement.liouville_goldbach : ArithmeticStatement.Target`; the name is new, the type is protected. All proposed helpers remain in the same namespace, with every binder explicit (`autoImplicit = false`).

## 3. Environment and cutoff evidence

Inspected configuration:

- `lean/lean-toolchain`: `leanprover/lean4:v4.32.2`.
- `lean/lakefile.toml`: library/default target `Statement`, `autoImplicit = false`, Mathlib pinned to `905b95818eb32af7874a58b427f50c1711a5e96c`.
- Actual `lean --version`: Lean 4.32.2, `arm64-apple-darwin24.6.0`, compiler commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`.
- Actual Mathlib HEAD matches the pin; `git status --short` there returned no changes. Commit timestamp is `2026-07-28T18:36:13+02:00`, subject `chore: bump toolchain to v4.32.2`.
- Manifest SHA-256: `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03`.

All library inspection was of this local pinned checkout. The assignment supplies eligibility of Mathlib and Lean through 2026-07-31; local revision/timestamp checks are consistent with it. No later/current documentation was consulted. Git timestamps alone are not a new independent publication-date audit.

The manifest's exact dependency revisions match the local HEADs. Dates below are locally observed committer dates, not substituted moving branch labels:

| Package | Revision | Date |
|---|---|---|
| plausible | `e12c1910fe855cbfc38803cd4e55543906d5fa62` | 2026-07-13 |
| LeanSearchClient | `c5d5b8fe6e5158def25cd28eb94e4141ad97c843` | 2026-02-12 |
| importGraph | `7e9612bf0b9ee66db3cb5b9988a35afc706f5a12` | 2026-07-13 |
| proofwidgets | `6e311e2a844da9b2cc3971187df2fe0066947b93` | 2026-07-13 |
| aesop | `a7dbf0c63b694e47f425f3dcddbc0e178bb432d3` | 2026-07-13 |
| Qq | `38d591e778f100aec9762bb582f9c7f55f50e9dc` | 2026-07-13 |
| batteries | `023ce7d62a0531e22a5331e20b587817a80d49ff` | 2026-07-13 |
| Cli | `88679d088c9720c27ebdf2ba4dafe17341747f94` | 2026-07-13 |

Keep `lake-manifest.json` frozen despite some inherited `inputRev` strings saying `main` or `master`. Do not run unconstrained updates.

### Bounded compiler observations

Working directory for both commands:

`.clawcodex/math-team/problems/liouville-goldbach-jul2026/lean`

Commands (with the displayed absolute P substituted):

```text
lake env lean P/formal/blueprinter/api-probe-v1.lean
lake env lean P/formal/blueprinter/count-api-probe-v1.lean
```

Each was bounded by 60 seconds. The first exited **0**; its checked factor, sign, cast, and `Even` API types are in `api-probe-v1.log`. It contains only imports, `#check`, and `#print`, no mathematical proof. The second exited **1** before checking any counting API:

```text
object file '.../Mathlib/Order/Interval/Finset/Nat.olean'
of module Mathlib.Order.Interval.Finset.Nat does not exist
```

The exact diagnostic is in `count-api-probe-v1.log`. This is an **import-cache/setup blocker**, not a mathematical gap. Counting API statements below are source-inspected, not compiler-checked by this run.

### Import/cache recommendation

1. Elementary arithmetic/representations: start from `import Statement.Definitions`. The additional `Mathlib.Algebra.Ring.Parity` import is cached and was tested; it supplies a direct two-valued-power lemma. No `import Mathlib`, arithmetic-function package, or analytic library is needed.
2. Counting: add `Mathlib.Order.Interval.Finset.Nat` and `Mathlib.Algebra.BigOperators.Ring.Finset`. The latter already imports the finite-sum basic/piecewise infrastructure and finite-product/cardinality support; do not redundantly list those as extra imports.
3. These counting modules and their required missing dependencies need a cache fetch/build **at the same pinned revisions**, by the authorized generator. Their oleans were absent. Do not upgrade Mathlib to solve this.
4. `Mathlib.Algebra.BigOperators.Intervals` has a usable specialized reflection lemma but is not necessary: use `Finset.sum_nbij'` and the interval involution already required for fidelity. This avoids its larger ordered-interval import chain.
5. `Mathlib.Tactic.Ring` and the umbrella `Mathlib.Tactic.NormNum` oleans were absent. If the generator elects to use them, fetch the same-pin cache; do not make tactic convenience a new mathematical premise. Small closed factor/sign checks can avoid umbrella imports.

Suggested future module split, **not files created or an authorization to edit the master**: arithmetic; signed representations/8m; counting; optional core reduction; final assembly. Only an integrator merges reviewed, checked implementations.

## 4. Reuse the actual library; do not redefine lambda

There is already a Mathlib arithmetic Liouville function:

`Mathlib/NumberTheory/ArithmeticFunction/Liouville.lean:27-45`, namespace `ArithmeticFunction`.

Its definition is `if n = 0 then 0 else (-1) ^ cardFactors n`, and it has `liouville_apply_one` and `liouville_apply_mul`. `ArithmeticFunction.cardFactors` is defined by `n.primeFactorsList.length` in `ArithmeticFunction/Misc.lean:259-268`.

**Critical mismatch:** the protected lambda has `lambda 0 = 1`, whereas Mathlib's arithmetic function has value 0 at zero. Do not replace the approved definition or claim unconditional equality. A possible later bridge has type

```lean
theorem lambda_eq_liouville {n : ℕ} (hn : 0 < n) :
  ArithmeticStatement.lambda n = ArithmeticFunction.liouville n
```

but is not needed on the minimal-import route and is not in the main interface bundle. In particular, unrestricted `lambda (u*v) = lambda u * lambda v` is false for this totalization (take `u=0`, `v=2`). Both inputs of the proposed multiplication helper are explicitly positive. There is **no coprimality assumption**.

### Narrow load-bearing API inventory

All paths in this table are relative to `lean/.lake/packages/mathlib/Mathlib/`. Source URL template, not a fetched current page:

`https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/<path>#L<line>`.

The source authors are recorded in each pinned file header (not inferred from theorem names). No external mathematical theorem beyond this pinned library is used in the plan.

| API / exact usable shape | Source locator | Application and guards |
|---|---|---|
| `Nat.primeFactorsList_one : primeFactorsList 1 = []` | `Data/Nat/Factors.lean:49-50` | `omega_one`, `lambda_one`; checked in probe. |
| `Nat.perm_primeFactorsList_mul (ha : a ≠ 0) (hb : b ≠ 0) : (a*b).primeFactorsList.Perm (a.primeFactorsList ++ b.primeFactorsList)` | `Data/Nat/Factors.lean:195-202` | Positivity supplies nonzero. `List.Perm.length_eq`, `List.length_append` give `omega_mul`; all three types checked. Avoid the coprime variant. |
| `Nat.primeFactorsList_prime (hp : Nat.Prime p) : p.primeFactorsList = [p]` | `Data/Nat/Factors.lean:83-86` | `lambda_prime`; checked. |
| `pow_add a m n : a^(m+n) = a^m * a^n` | actual type in `api-probe-v1.log:14` | `lambda_mul` after `omega_mul`. |
| `neg_one_pow_eq_ite : (-1 : R)^n = if Even n then 1 else -1` for `[Monoid R] [HasDistribNeg R]` | `Algebra/Ring/Parity.lean:387-391` | Specialize `R=ℤ`, exponent `omega n`; split the condition. Checked. Alternatively induction on the exponent avoids the additional import. |
| `Nat.sub_sub_self (h : a ≤ N) : N-(N-a)=a` | actual type in `api-probe-v1.log:16` | Reflection inverse; derive `a≤N` from interval membership. Checked. |
| `Nat.cast_sub (h : m ≤ n) : ((n-m : ℕ) : R) = (n:R)-(m:R)` | actual type in `api-probe-v1.log:17` | Cast interval cardinality using `1≤N`. Checked. |
| `Nat.card_Ico (a b : ℕ) : (Finset.Ico a b).card = b-a` | `Order/Interval/Finset/Nat.lean:82-85` | `a=1`, `b=N`; cast only after deriving `1≤N`. Source-only here. |
| `Finset.mem_product : p ∈ s.product t ↔ p.1 ∈ s ∧ p.2 ∈ t` | `Data/Finset/Prod.lean:59-61` | Actual ordered-pair set membership, together with `mem_filter` and interval membership. |
| `Finset.card_pos : 0 < s.card ↔ s.Nonempty` | `Data/Finset/Card.lean:78` | Count/existence without using the signed identity. |
| `Finset.card_image_of_injective (s) (H : Function.Injective f) : (s.image f).card = s.card` | `Data/Finset/Card.lean:249-251` | `f a = (a,N-a)` is injective by first projection, including the diagonal. |
| `Finset.sum_nbij' i j hi hj left_inv right_inv h` | `Algebra/BigOperators/Group/Finset/Defs.lean:497-510`, generated by `to_additive` | For `s=t=I N`, `i=j=(N-·)`: membership twice, two inverse laws, and `f a = g (i a)` imply `sum s f = sum t g`. All guards supplied by C02 helpers. |
| `Finset.sum_filter p f : (∑ a ∈ s.filter p, f a) = ∑ a ∈ s, if p a then f a else 0` | `Algebra/BigOperators/Group/Finset/Basic.lean:324-326`, generated by `to_additive` | Use `f a = (1:ℤ)` plus the constant-sum lemma to convert the cardinal to a signed indicator sum. Avoid unnecessary cast-of-sum rewrites. |
| `Finset.card_filter p s : (s.filter p).card = ∑ i ∈ s, if p i then 1 else 0` (sum in ℕ) | `Algebra/BigOperators/Group/Finset/Piecewise.lean:277-278` | Alternative only: must explicitly cast to ℤ; it is not already the signed identity. |
| `Finset.mul_sum s f a : a * ∑ i ∈ s, f i = ∑ i ∈ s, a*f i` | `Algebra/BigOperators/Ring/Finset.lean:56-60` | Specialize to integer sums and scalar 4, then distribute sums of additions/subtractions. |
| `Finset.sum_Ico_reflect f k (h : m ≤ n+1)` rewrites to interval `[n+1-m,n+1-k)` | `Algebra/BigOperators/Intervals.lean:151-153` | Optional alternative with `k=1,m=N,n=N`; normalize resulting endpoints. Not a required import. |

None of these library applications uses the conjecture or a custom axiom.

## 5. Arithmetic, representations, and the first infinite family

Exact signatures: `interfaces-v1.lean:40-109`.

### A. Arithmetic foundation

- `omega_one` then `lambda_one`: empty factor list.
- `lambda_sign {n} (hn : 0<n)`: the exponent gives ±1. The accepted totalization actually permits an all-n version, but the proposed mathematical interface stays on positive inputs.
- `omega_mul {u v} (hu : 0<u) (hv : 0<v)` then `lambda_mul`: permutation/length plus `pow_add`, not distinct-prime counting or coprime multiplication.
- `lambda_prime`, then exact values at 2, 3, 4, 5; no unchecked evaluation is a theorem dependency. `lambda_four` can use `4=2*2`.
- `lambda_two_mul` makes the diagonal bridge explicit. `lambda_square` is optional infrastructure, not a blocker for 8m.

### B. Representation interface and scaling

`HasSignedRepresentation s N` is precisely positive witnesses with `N=a+b` and both signs equal to the **integer** `s`. `HasRepresentation N` specializes `s=-1`. Neither definition includes Even N, primality, witness parity, coprimality, or `a≠b`.

`hasSignedRepresentation_mul` takes `d>0` and a representation of `N`, and returns a representation of `d*N` with sign `lambda d * s`, via `(d*a,d*b)`. It does not require `s=±1`: positive witnesses already constrain a realizable sign, and multiplication itself works for any `s` with the given witness equalities. The more source-literal `representation_scaled_sign` has the explicit `s=1 ∨ s=-1` and `lambda m=-s` premises from E03. Both are consequences to prove, not extra assumptions attached to Target.

`representation_two_sign_seed` consumes actual positive-sign and negative-sign representations at `d`. It omits E04's unnecessary evenness/size restrictions on `d`, because its conclusion is only a representation; positive witnesses already force `d≥2`. This harmless generalization also accommodates the explorer's odd seeds. Its use at 8 requires no new premise.

### C. Diagonal and 8m

`representation_double` uses `(m,m)` given `m>0` and `lambda m=-1`. For E02, unfold `Even N` as `∃ m, N=m+m`; obtain `m>1` from `2<N`. `lambda_two_mul` and `lambda N=1` force `lambda m=-1`. This produces the diagonal witnesses (equivalently `m=N/2`) without importing division infrastructure.

For the first substantial theorem:

```lean
theorem representation_multiple_eight (m : ℕ) (hm : 0 < m) :
  HasRepresentation (8 * m)
```

Use the seed pair `(3,5)` of sign -1 and `(4,4)` of sign +1, then sign-adaptive scaling. Equivalently use `(3*m,5*m)` when `lambda m=1`, and `(4*m,4*m)` when `lambda m=-1`. Positivity follows from `hm`. Commutativity reconciles the general scaling conclusion `m*8` with the displayed target `8*m`. In particular `m=1` is included, and the repeated witness in the second case is allowed.

This proves only an infinite divisibility family. No finite list of constant seeds is asserted to cover the final target; explorer `attempt-v1.md:51-69` explains the surviving `2p²`/`2pq` obstruction for that restricted method. The diagonal already handles `2p`, so do not label those as residual cases.

## 6. The actual ordered count and exact identity

Exact definitions: `interfaces-v1.lean:19-38`. Exact helper signatures: lines 111-179.

### Conventions and source alignment

- `I N := Finset.Ico 1 N`. This is exactly the handoff's `{a in range N : 0<a}`, using the library's native interval rather than an additional filter.
- `L x := ∑ a ∈ Finset.Icc 1 x, lambda a`. It is an **inclusive** sum through x. Thus `L (N-1)`, never `L N`, is the sum on the summand interval.
- `orderedRepresentations N` filters `(I N).product (I N)` by the sum and two sign equalities. **R is defined as its cardinality**, not an algebraic expression, not an unordered count, and not a quotient by reflection.
- `representationIndices N` is an auxiliary filtered first-coordinate interval. It is not silently substituted for the actual pair count.
- `C N := ∑ a ∈ I N, lambda a * lambda (N-a)` in ℤ. The natural subtraction in the argument is safe on this interval.

### C02-C04: bounds, reflection, and pair correspondence

1. `mem_I_iff` gives `0<a ∧ a<N`. For `N≥2`, record `0<N-a` and `N-a<N` before any positive-input sign lemma.
2. `interval_eq_Icc` proves `I N = Icc 1 (N-1)` under `N≥2`. `interval_card_cast` proves `((I N).card : ℤ) = (N:ℤ)-1`. The proof must use `Nat.card_Ico` and a justified cast of the natural difference.
3. `reflection_mem` plus `reflection_involutive` establish the actual map `a ↦ N-a`; `reflection_bijection` states its `Set.BijOn` property. `Nat.sub_sub_self` cannot be used globally without the membership bound.
4. `sum_lambda_interval` establishes the inclusive L endpoint. `sum_lambda_reflection` reindexes using that involution; it requires no multiplicativity or conjectural information.
5. `mem_orderedRepresentations` gives exactly the five positive-witness conditions. No `N≥2` premise is needed on this membership iff: positive pairs imply their own bounds.
6. `orderedRepresentations_eq_image` identifies the pair set with the image of `a ↦ (a,N-a)` on `representationIndices N`. The map is globally injective by first projection; its inverse on the pair set is `Prod.fst`, because `N=a+b` gives `N-a=b`. This is the concrete ordered-pair equivalence requested in C04, expressed as image equality plus injectivity rather than an additional dependent `Equiv` object.
7. `representation_count_eq_card_indices` is then justified, not definitional sleight of hand. When `a≠b`, the two orientations have different first coordinates and count separately; the diagonal has one ordered pair, not two.

### C05-C07: the identity

For positive `a,b`, case-split their two signs to establish the integer-valued identity

`4 * (if lambda a=-1 ∧ lambda b=-1 then (1:ℤ) else 0) = (1-lambda a)*(1-lambda b)`.

Convert the actual count to the sum of these indicators using the pair-image/card bridge and finite-set summation. Sum the identity over `I N`, expand, and use the two interval sums:

```text
4 * (R N : ℤ)
 = Σ[a∈I N] (1-lambda a)*(1-lambda (N-a))
 = ((I N).card : ℤ)
     - Σ[a∈I N] lambda a - Σ[a∈I N] lambda (N-a) + C N
 = ((N : ℤ)-1) - 2*L (N-1) + C N.
```

Proposed exact theorem:

```lean
theorem four_mul_representation_count {N : ℕ} (hN : 2 ≤ N) :
  4 * (R N : ℤ) = ((N : ℤ) - 1) - 2 * L (N - 1) + C N
```

All subtraction outside arguments of `lambda`/`L` is in ℤ. There is no division by 4. The statement covers odd N as well as even N and includes N=2, but not N=0 (where the displayed scalar term would already be wrong). Retaining the requested N≥2 guard avoids spurious boundary obligations.

### C08-C09: existence and assembly

`representation_count_pos_iff` follows directly from `Finset.card_pos` and `mem_orderedRepresentations`; it does **not** depend on the counting identity or a correlation bound. This is a valuable separate early counting deliverable.

The signed identity then gives both:

```text
0 < R N  ↔  2*L(N-1)-((N:ℤ)-1) < C N
0 < R N  ↔  4 ≤ ((N:ℤ)-1)-2*L(N-1)+C N.
```

The second uses that R is a natural count: positivity implies R≥1, not just a positive real number. Cast inequalities explicitly. `target_iff_count_pos` and `target_iff_pointwise_keystone` are equivalences/reductions only; they do not prove their right-hand sides.

## 7. Optional prime-product reduction, not a solution

Exact proposed signatures: `interfaces-v1.lean:181-189`; source: explorer candidate C, `attempt-v1.md:74-90`.

The only extra factor-selection helper is:

```lean
theorem exists_prime_pair_factor_of_lambda_one {m : ℕ}
    (hm : 1 < m) (hSign : lambda m = (1 : ℤ)) :
  ∃ p q d : ℕ,
    Nat.Prime p ∧ Nat.Prime q ∧ 0 < d ∧
      lambda d = (1 : ℤ) ∧ m = d * (p * q)
```

A factor-list route avoids overbuilding a parity API: the list cannot be empty (`m>1`) or singleton (`lambda m=1` versus prime sign -1). Extract two occurrences, set d to the product of the rest, prove each prime and d positive, and use the product factorization plus multiplication signs to recover `lambda d=1`. `Nat.prod_primeFactorsList` and `Nat.prime_of_mem_primeFactorsList` were checked in the probe. The remaining list/product details have not been explored or proved. **No distinctness of p,q and no d>1 condition** are permitted: square cores require p=q, and the core case itself has d=1.

Then propose

```lean
theorem target_iff_prime_product_core :
  Target ↔ ∀ p q : ℕ,
    Nat.Prime p → Nat.Prime q → HasRepresentation (2 * p * q)
```

Forward: prime bounds make `2*p*q` an admissible even N. Reverse: write N=2m with m>1, use the diagonal if `lambda m=-1`; otherwise extract the factorization above and scale a core representation by positive-sign d. This is independent of C07. Its **right-hand side remains unproved**. Explorer PB is only a proposed sufficient route to those core witnesses; it is not supplied by this equivalence or by the original target at `2q`.

## 8. Open obligations, risks, and review gates

### Mathematical obstruction still present

No input supplies the universal pointwise inequality. After every routine helper above, the outstanding counting goal is still:

```lean
N : ℕ
hEven : Even N
hN : 2 < N
⊢ 2 * L (N - 1) - ((N : ℤ) - 1) < C N
```

`pointwise_keystone` is an explicitly **OPEN** signature. `liouville_goldbach : Target` is explicitly **OPEN**. Neither is an axiom, an accepted dependency, or a theorem established by this blueprint. An almost-all estimate, a finite search, a uniform assertion about L without proof, or a conditional helper that assumes this inequality cannot discharge Target.

### Fidelity and implementation hazards

- Do not exchange `primeFactorsList` (multiplicity) for `primeFactors` (distinct factors).
- Keep lambda's signed codomain. Its zero totalization forbids unrestricted multiplicativity and unrestricted identification with library Liouville.
- Every use of `lambda (N-a)` in positive-domain lemmas needs the interval bound; no value at zero repairs missing positivity.
- Do not redefine R by one quarter of the RHS or by unordered representatives; diagonal weights would be wrong.
- Keep the inclusive endpoint `L (N-1)` and distinguish natural index subtraction from signed scalar subtraction.
- `representation_diagonal` covers only its sign class. `representation_multiple_eight` covers only multiples of 8. Conditional reduction/assembly lemmas are not a proof of Target.
- No global bijection of ℕ by `a ↦ N-a` exists; the theorem is on the finite interval.
- Helper normalization/generalization choices in sections 5-6 need new helper fidelity review. They do not license any change to the approved target.
- The count import failure must be resolved before calling any proposed counting module elaborated. Source lookup is not a compiler check.

### Next handoff and acceptance separation

1. Leader supplies the code-only `interfaces-v1.lean` and protected transitive definitions to fresh helper readback/fidelity review; do not include this plan in the blind packet. Since theorem bodies are erased, the bundle is signature text rather than an accepted Lean module.
2. First generator target: elementary arithmetic followed by `representation_multiple_eight`, with exact protected definitions and no extra hypotheses. Retain all positive m, including m=1.
3. Next generator target: count definitions, `representation_count_pos_iff`, reflection and pair-count correspondence; then `four_mul_representation_count` and C09 consequences. Fetch only the required same-pin cache.
4. Only thereafter consider the optional core equivalence. The leader must separately assign mathematical discovery of K01/core witnesses; architecture has not solved it.
5. For every accepted implementation, require exact-file compilation, no admitted obligations or unsupported axioms, `#print axioms` on dependencies, protected hash comparison, and fresh helper statement fidelity. Only the integrator merges. This blueprint has no proof/axiom acceptance result to transfer.

## 9. Artifact identities

| Artifact/input | SHA-256 |
|---|---|
| `request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `nl/sketcher/formal-handoff-v1.md` | `25ce7919c925c8a3d8ae3a6296a65aa92e93fec3fcdd18a4df41675fa0dbdfb7` |
| `nl/explorer/attempt-v1.md` | `5143a167b3ac0e26116b33e934a3e33fff2bc6c44b5a7608e01c7f73d4cf94a2` |
| `formal/blueprinter/interfaces-v1.lean` | `89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc` |
| `formal/blueprinter/api-probe-v1.lean` | `10b99258e301bd5e0ae5427a10b62fbd5c9a14b6ac2ce96779ed355797c5ef42` |
| `formal/blueprinter/count-api-probe-v1.lean` | `7a5ae7d5c9cdcefd4e09d545a8f0f32001ff3a21360688aa4a134ebe52c39fc5` |

Logs: `api-probe-v1.log` (success), `count-api-probe-v1.log` (missing interval olean). These verify only the observations described above, not any proposed theorem.
