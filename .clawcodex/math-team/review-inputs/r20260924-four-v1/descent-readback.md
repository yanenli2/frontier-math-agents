# Literal code-only readback

Scope: only the four supplied code files were read. No intent comments were present or used. The inputs contain theorem signatures without proof bodies; this report does not check proofs or elaboration.

## 1. Literal assertions

### Definitions and notation

All subtraction and division on ℕ below are natural-number subtraction and division. Write `[t]ₚ` for the displayed cast of a natural number or integer into `ZMod p`.

- `Nat.minFac n` is 2 when 2 divides n; otherwise it calls `minFacAux n 3`. At an index k, that auxiliary returns n if n < k², otherwise returns k if k divides n, otherwise continues at k + 2.
- `primeFactorsList 0 = []` and `primeFactorsList 1 = []`. For n ≥ 2, the list starts with `minFac n` and continues recursively with the list for `n / minFac n`.
- List length is 0 for the empty list and increases by 1 on adding a head. Thus Ω(n) := `omega n` is the number of prime factors **with multiplicity**, not the number of distinct prime factors. λ(n) := `lambda n` is the integer (−1)^Ω(n). In particular λ(0) = λ(1) = 1.
- `HasSignedRepresentation s N`, for s ∈ ℤ and N ∈ ℕ, means

  `∃ a : ℕ, ∃ b : ℕ, 0 < a ∧ 0 < b ∧ N = a + b ∧ λ(a) = s ∧ λ(b) = s`.

  `HasRepresentation N`, abbreviated H(N), fixes s = −1. Both individual signs must be −1.
- `ZMod 0` has carrier ℤ and `z.val = |z|` as a natural number. For p > 0, `ZMod p` has carrier `Fin p`, and `z.val` is its natural-number representative, less than p. Put Rₚ := `ZMod p` and ℓₚ(z) := `residueLambda p z` = λ(z.val). In particular, ℓₚ takes values in ℤ, not in Rₚ.
- `IsSquare t`, in any supplied multiplication type, means `∃ w, t = w * w`. In the interfaces its witness is an element of Rₚ, not a natural-number square root.
- Gₚ(a) := `GoodMultiplier p a` means

  `a ≠ 0 ∧ ∀ z : Rₚ, z ≠ 0 → ℓₚ(a * z) = ℓₚ(a) * ℓₚ(z)`.

  This definition itself has no primality hypothesis on p.
- P(p) abbreviates `Nat.Prime p`. The supplied characterization is

  `P(p) ↔ 2 ≤ p ∧ ∀ m : ℕ, m < p → m ∣ p → m = 1`.
- For readability only, put NR(p) := ¬H(4p),

  `A(p) := ∀ j : ℕ, 0 < j → j < p → λ(p − j) = −λ(j)`,

  and q(p) := (p + 1) / 4, with natural-number division.

### Main interfaces, in declaration order

The formulas preserve the order of the data binders and hypothesis binders. An arrow is an implication from the corresponding hypothesis. Consecutive universal or existential variables are ordered left to right.

1. **`lambda_reflection_eq_one_of_neg`**

   `∀ p n : ℕ, NR(p) → 0 < n → n < p → λ(n) = −1 → λ(p − n) = 1`.

   There is no primality assumption on p.

2. **`lambda_double_reflection_eq_neg_one_of_pos`**

   `∀ p n : ℕ, NR(p) → 0 < n → n < 2p → λ(n) = 1 → λ(2p − n) = −1`.

   The upper bound is 2p, not p; again p need not be prime.

3. **`three_not_dvd_of_positive_pair`**

   `∀ p x y : ℕ, NR(p) → 0 < x → 0 < y → x + y = p → λ(x) = 1 → λ(y) = 1 → ¬(3 ∣ x)`.

   Only the displayed conclusion about x is asserted. No primality assumption is present.

4. **`positive_pair_gap_step`**

   `∀ p x y : ℕ, P(p) → p ≠ 3 → NR(p) → 0 < x → x < y → x + y = p → λ(x) = 1 → λ(y) = 1 →`

   `∃ u : ℕ, ∃ v : ℕ, 0 < u ∧ u < v ∧ u + v = p ∧ λ(u) = 1 ∧ λ(v) = 1 ∧ v − u < y − x`.

   There is no explicit hypothesis p ≠ 2. Positivity of y and v follows from their strict ordering after positive x and u.

5. **`no_positive_pair`**

   `∀ p : ℕ, P(p) → p ≠ 2 → p ≠ 3 → NR(p) → ∀ x y : ℕ, 0 < x → 0 < y → x + y = p → ¬(λ(x) = 1 ∧ λ(y) = 1)`.

   This excludes both signs being +1; it does not assert that both signs are −1. The x and y binders occur after the four hypotheses concerning p.

6. **`lambda_antireflection_of_no_representation`**

   `∀ p : ℕ, P(p) → p ≠ 2 → p ≠ 3 → NR(p) → ∀ n : ℕ, 0 < n → n < p → λ(p − n) = −λ(n)`.

7. **`cyclic_short_multiple`**

   `∀ p n : ℕ, P(p) → 2 ≤ n → n < p → ∀ z : Rₚ, z ≠ 0 →`

   `∃ k : ℤ, ∃ d : ℕ, k ≠ 0 ∧ k.natAbs < n ∧ 0 < d ∧ n * d < p ∧ [k]ₚ * z = [d]ₚ`.

   k may be negative. The product bound is strict, n·d < p; it is not a bound involving |k|·d.

8. **`residueLambda_natCast`**

   `∀ p n : ℕ, n < p → ℓₚ([n]ₚ) = λ(n)`.

   Neither primality nor 0 < n is assumed.

9. **`residueLambda_sign`**

   `∀ p : ℕ, ∀ z : Rₚ, z ≠ 0 → (ℓₚ(z) = 1 ∨ ℓₚ(z) = −1)`.

   There is no restriction on p, including no requirement p > 0.

10. **`residueLambda_neg`**

    `∀ p : ℕ, P(p) → A(p) → ∀ z : Rₚ, z ≠ 0 → ℓₚ(−z) = −ℓₚ(z)`.

11. **`goodMultiplier_one`**

    `∀ p : ℕ, P(p) → Gₚ([1]ₚ)`.

12. **`goodMultiplier_neg`**

    `∀ p : ℕ, P(p) → A(p) → ∀ a : Rₚ, Gₚ(a) → Gₚ(−a)`.

13. **`goodMultiplier_natCast_step`**

    `∀ p n : ℕ, P(p) → A(p) → 0 < n → n < p →`

    `(∀ j : ℕ, 0 < j → j < n → Gₚ([j]ₚ)) → Gₚ([n]ₚ)`.

    The A(p) premise ranges over all positive j below p. The separate small-multiplier premise ranges only over positive j below n.

14. **`residueLambda_mul`**

    `∀ p : ℕ, P(p) → A(p) → ∀ a b : Rₚ, a ≠ 0 → b ≠ 0 → ℓₚ(a * b) = ℓₚ(a) * ℓₚ(b)`.

15. **`lambda_eq_one_of_isSquare`**

    `∀ p n : ℕ, P(p) → A(p) → 0 < n → n < p → (∃ t : Rₚ, [n]ₚ = t * t) → λ(n) = 1`.

    The square-root existential is a premise, not a promised output witness.

16. **`prime_dvd_quarter_isSquare`**

    `∀ p r : ℕ, P(p) → 7 ≤ p → p % 4 = 3 → P(r) → r ∣ q(p) → ∃ t : Rₚ, [r]ₚ = t * t`.

    No antireflection or no-representation premise occurs. Bounds r ≤ q(p) and r < p are not separate hypotheses in this declaration.

17. **`exists_small_prime_isSquare`**

    `∀ p : ℕ, P(p) → 7 ≤ p → p % 4 = 3 →`

    `∃ r : ℕ, P(r) ∧ r ∣ q(p) ∧ r ≤ q(p) ∧ r < p ∧ (∃ t : Rₚ, [r]ₚ = t * t)`.

18. **`representation_four_prime_three_mod_four`**

    `∀ p : ℕ, P(p) → 7 ≤ p → p % 4 = 3 →`

    `∃ a : ℕ, ∃ b : ℕ, 0 < a ∧ 0 < b ∧ 4p = a + b ∧ λ(a) = −1 ∧ λ(b) = −1`.

19. **`representation_multiple_four`**

    `∀ m : ℕ, 0 < m →`

    `∃ a : ℕ, ∃ b : ℕ, 0 < a ∧ 0 < b ∧ 4m = a + b ∧ λ(a) = −1 ∧ λ(b) = −1`.

    m need not be prime and has no congruence restriction or upper bound. This assertion has no NR or A premise.

### Supporting declarations supplied with the interfaces

These are separate declarations, not additional hypotheses silently attached to the main interfaces.

- `ZMod.val_lt`: for each n : ℕ, given an instance asserting n ≠ 0, every a : Rₙ satisfies a.val < n.
- `Nat.prime_def_lt`: the characterization P(p) above, universally quantified over p.
- `Nat.minFac_dvd`: for every n : ℕ, minFac(n) divides n.
- `Nat.minFac_prime`: for every n : ℕ, n ≠ 1 implies P(minFac(n)).
- `Nat.minFac_le_of_dvd`: for every n : ℕ, then every m : ℕ, 2 ≤ m implies that m ∣ n implies minFac(n) ≤ m.
- `primeFactorsList_zero`, `primeFactorsList_one`, and `primeFactorsList_two` assert that the respective lists are [], [], and [2].
- `primeFactorsList_add_two`: for every n : ℕ, the list for n + 2 equals `minFac(n + 2) :: primeFactorsList((n + 2) / minFac(n + 2))`.
- `prime_of_mem_primeFactorsList`: for every n : ℕ and then p : ℕ, membership of p in n's factor list implies P(p).
- `prod_primeFactorsList`: for every n : ℕ, n ≠ 0 implies that the product of n's factor list is n.
- `Prime.primeFactorsList_pow`: for every p : ℕ, then a proof P(p), then every n : ℕ, the factor list of pⁿ is `List.replicate n p`.
- `List.replicate n a` is empty at n = 0 and adds one copy of a at each successor. Its parameters are any type α, n : ℕ, and a : α.
- `List.length_nil`: for any type α, the empty list of α has length 0.
- `List.length_cons`: for any type α, any a : α, and any list as of α, the length of `a :: as` is the length of as plus 1.

## 2. Quantifier order and witness dependencies

The formulas in §1 give the actual binder order, including hypotheses that precede later data binders. Lean's implicit braces around parameters do not make them existential: they remain universally quantified. Proof binders are implications in this mathematical reading.

- In `HasSignedRepresentation s N`, a is chosen after s and N; b is chosen after a as well. Neither is required to be a uniform choice for different s or N.
- In the gap step, u may depend on p, x, y and all preceding premises. v is chosen after u and may additionally depend on u.
- In `cyclic_short_multiple`, k may depend on p, n, z and all preceding premises. d is chosen after k and may depend on k. The order is not a single pair k,d working for every z, nor one d chosen before z.
- In `prime_dvd_quarter_isSquare`, the square witness t may depend on p, r and the preceding premises.
- In `exists_small_prime_isSquare`, r is chosen after p and its premises; its square witness t is chosen inside the final conjunct, after r. No least-prime, uniqueness, or uniform-root requirement is stated.
- In the two representation conclusions, a and then b may depend on the relevant p or m and the preceding premises. There is no common pair asserted to work for different inputs.
- The `IsSquare` premise in interface 15 supplies an existential assumption. It does not change that theorem's output into an existence assertion.
- A(p), the small-multiplier premise, and the z clause of Gₚ(a) are universally quantified conditions. Each local n or j or z is scoped within its condition; these binders are not shared witnesses between different conditions.
- NR(p) is a negated existence claim. It supplies no chosen pair: it rules out every positive pair summing to 4p with both signs −1.

## 3. Pointwise versus aggregate conditions

- Sign equalities are pointwise at the displayed integer or residue. A(p) imposes a pointwise reflection equality at every positive integer below p. Gₚ(a) imposes a pointwise multiplication equality for every nonzero residue z, for that fixed a.
- The conditions 0 < n < p, 0 < n < 2p, n < p, r < p, r ≤ q(p), and k.natAbs < n constrain individual variables. The condition n·d < p constrains each selected d relative to its input n and p; it is not a sum or average over z or over witnesses.
- The equations x + y = p, u + v = p, and a + b = 4p or 4m constrain a pair's total. They do not replace the separate sign requirements on each summand.
- The gap condition v − u < y − x compares the two selected pair differences. It gives strict decrease, with no stated contraction factor or quantitative iteration count.
- Ω(n) counts an entire finite factor list for one n. Its parity determines λ(n); no bound or average over a range of n is asserted.
- There is no asymptotic, density, probabilistic, or averaged conclusion and no aggregate estimate over all residues or primes.

## 4. Constants, domains, and restrictions

There are no unspecified real constants, existential thresholds, or hidden numerical parameters. All variable restrictions appear in §1; the fixed numerals have these roles:

- **0:** natural-number lower endpoints, the excluded residue/integer zero, empty-list length, and the exceptional carrier case `ZMod 0`.
- **1 and −1:** the integer signs of λ and ℓ; 1 is also the multiplier identity, the excluded n in `minFac_prime`, and the allowed proper divisor in `prime_def_lt`.
- **2:** the primality lower bound, first trial factor and auxiliary step size, successor pattern n + 2, the lower bound for n in `cyclic_short_multiple`, the double-reflection factor, and an explicitly excluded p in interfaces 5–6.
- **3:** the initial odd trial factor, divisor excluded in interface 3, excluded value of p in interfaces 4–6, and remainder modulo 4 in interfaces 16–18.
- **4:** the factor in the representation target, the modulus in p % 4 = 3, and the denominator of q(p).
- **7:** the non-strict lower bound for p in interfaces 16–18.

Variable/domain details:

- All p, n, m, x, y, u, v, d, prime witnesses r, and bounded indices j in the main assertions are natural numbers. The signed multiplier k is an integer. Residue variables and square roots belong to Rₚ. The parameter s in `HasSignedRepresentation` is an integer with no imposed bound or sign in the definition itself.
- P(p) imposes p ≥ 2. With p ≠ 2 and p ≠ 3 it restricts p to primes at least 5. With 7 ≤ p and p % 4 = 3 it imposes exactly those further displayed lower/congruence restrictions, with no upper bound.
- Interface 4 excludes p = 3 but not explicitly p = 2; its ordered positive-pair premises themselves leave no pair at p = 2.
- In interface 7, 2 ≤ n < p, 0 < |k| < n, and d ≥ 1 with n·d < p. There is no requirement that n or d be prime, or that k be positive.
- In interfaces 16–17, P(r) gives r ≥ 2. The quotient q(p) is natural-number division; the displayed congruence makes (p + 1) divisible by 4. The lower bound p ≥ 7 makes q(p) ≥ 2. Interface 17 explicitly includes both r ≤ q(p) and r < p; interface 16 instead states primality and divisibility as its premises.
- In each positive pair summing to p, each member is less than p. In a representation, both summands are positive and less than their total. No distinctness, ordering, primality, coprimality, or specified balance condition is imposed on representation witnesses a,b.
- All natural differences used in the reflection and gap assertions have the displayed strict ordering that makes them ordinary positive differences. No integer-subtraction interpretation is being silently substituted for a potentially truncated difference.

## 5. Vacuity, inconsistent-premise, empty-object, and trivial-witness audit

1. **Conditional nonrepresentation premises.** Interfaces 1–6 assume NR(p). Each interface's other premises force p > 0. If the supplied final declaration `representation_multiple_four` is accepted, it gives H(4p) for every such p. Consequently the full premise bundles of interfaces 1–6 are unsatisfiable relative to that final declaration. These signatures must not be read as asserting that a no-representation case exists. This conditional vacuity does not weaken interfaces 18–19, which have no NR premise.

2. **Antireflection is assumed, not universally supplied.** Interfaces 10 and 12–15 require A(p); they do not assert it for every prime. The quantified range in A(p) is empty for p = 0 or 1, but their primality hypotheses exclude those cases. At p = 2, A(p) would require λ(1) = −λ(1), incompatible with λ(1) = 1. Thus their premise bundles are also empty at p = 2, despite not explicitly excluding it.

3. **Empty small-multiplier range.** At n = 1 the premise `∀ j, 0 < j → j < n → Gₚ([j]ₚ)` is vacuous. Interface 13 nevertheless retains its other premises and its nonempty conclusion Gₚ([1]ₚ).

4. **Residue edge cases.** For p = 1 there is no nonzero residue, so a condition universally quantified over nonzero residues is empty. G₁(a) is not thereby true: its separate a ≠ 0 conjunct is impossible. For p = 0, `residueLambda_sign` uses integer absolute values through `.val`, not a representative less than p. The premise n < p in interface 8 excludes p = 0 but allows n = 0 when p > 0.

5. **Empty factor lists.** Both 0 and 1 have empty factor lists and sign +1. The factor-list product declaration explicitly excludes n = 0. Empty factorization does not create a −1 representation summand; zero is independently forbidden by positivity.

6. **Representation witnesses.** No empty or zero summand is permitted. A summand 1 also cannot have sign −1. Equal summands are allowed: for the admitted input m = 1, a = b = 2 satisfies the displayed representation requirements. Thus the final assertion does not demand two different summands. At m = 0 its implication is vacuous, not a claim that 0 has a representation. A general signed representation can only use s = ±1 because λ has only those values, although the definition does not separately impose this restriction on s.

7. **Strict descent and short-multiple witnesses.** The gap witness cannot simply be the original ordered pair because its gap must be strictly smaller. In interface 7, k = 0 and d = 0 are both explicitly excluded; the equality of zero residues is not an available trivial witness. No one fixed witness pair is required across different inputs.

8. **Square and prime witnesses.** `IsSquare` alone permits zero as a square root of zero. In the displayed uses, the positive/smallness conditions on n, or the prime-divisor conditions with p ≥ 7, keep the asserted cast away from zero. Interface 17 cannot choose r = 0 or r = 1 because r must be prime. Its q(p) ≥ 2 restriction avoids the empty-prime-divisor case q(p) = 1.

9. **No existence from an antecedent.** Neither a conditional theorem using NR(p), nor one using A(p), nor one assuming an `IsSquare` witness establishes the existence of inputs satisfying that antecedent. Conversely, the final two conclusions explicitly require positive representation witnesses for every input satisfying their stated premises; they are not merely conditionals on the existence of such witnesses.

## 6. Verdict

**READBACK-CLEAN**, as a literal statement readback, with the code-based qualifications above. In particular, `DescentInterfaces.lean.txt:30–63` contains conditional NR(p) interfaces whose positive-p premise bundles conflict with the final signature at lines 122–123 if all supplied declarations are accepted. This is recorded as conditional-premise vacuity, not as an existence conclusion or a discrepancy with unseen intent.

No additional code-local divergence is identified. This label certifies neither proof correctness nor correspondence with any unseen source statement.
