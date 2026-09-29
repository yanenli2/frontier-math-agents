# Literal readback

Scope: only Declaration.lean, Dependencies.lean, and ListOperations.lean were read. No intent comments were present.

## 1. Literal assertion

Let Ω(n) be the length of `Nat.primeFactorsList n`, and let λ(n) = (−1)^Ω(n), with values in ℤ. Prime factors are counted **with multiplicity**, not merely as distinct prime divisors: the list recursively removes one minimum prime factor at a time, and the supplied prime-power identity gives a list of n repeated copies of p for p^n. For 0 and 1 the factor list is empty, so Ω(0) = Ω(1) = 0 and λ(0) = λ(1) = 1.

The declaration asserts:

For every natural number m > 0, there exist natural numbers a, b > 0 such that

    4m = a + b,    λ(a) = −1,    λ(b) = −1.

Equivalently, every positive multiple of four is a sum of two positive natural numbers, each having an odd total number of prime factors counted with multiplicity.

## 2. Quantifier order and witness dependencies

After unfolding the representation predicates, the binder order is:

    ∀ (m : ℕ), ∀ (hm : 0 < m), ∃ (a : ℕ), ∃ (b : ℕ),
      0 < a ∧ 0 < b ∧ 4 * m = a + b ∧
      λ(a) = −1 ∧ λ(b) = −1.

The binder hm is a proof of the premise, not an additional numerical parameter. Formally a may depend on m and hm, and b may additionally depend on a. Mathematically the pair can be chosen separately for each positive m; neither summand must be uniform across m.

`HasSignedRepresentation` takes parameters s : ℤ and then N : ℕ, before its existential a and b. `HasRepresentation N` fixes s to −1. Neither s nor N is independently quantified in this theorem: N is 4m, and s is −1.

## 3. Pointwise versus aggregate conditions

- Input restriction: 0 < m.
- Pointwise witness restrictions: 0 < a, 0 < b, λ(a) = −1, and λ(b) = −1, separately for each summand.
- Aggregate restriction: the exact sum a + b = 4m.
- There is no averaged estimate, counting estimate, or bound on a combined prime-factor count. The two sign equalities are not merely a condition on their sum or product.

## 4. Constants and restrictions

- m is universally quantified in ℕ, with m ≥ 1 and no upper bound.
- a and b are existentially quantified in ℕ, each explicitly positive. No upper bound is written. Since λ(1) = 1, the sign conditions also exclude 1; hence each witness is at least 2 and, from the sum, at most 4m − 2.
- N = 4m is at least 4 and divisible by 4, with no upper bound. The helper's standalone N parameter is otherwise unrestricted.
- s is unrestricted as a standalone helper parameter, but is the fixed integer −1 here; there is no existential choice of sign.
- Ω and λ are fixed defined functions, not adjustable constants. Ω is natural-valued; on each witness it is odd and at least 1, with no explicit upper bound. λ is integer-valued and always ±1; its required witness value is exactly −1.
- The multiplier 4, the base and target −1, and the positivity threshold 0 are fixed literals. The defining code also uses fixed 0 and 1 for the empty factor-list cases and list lengths, 1 for the length increment, 2 for even-divisor selection, the factorization branch offset and odd-candidate increment, and 3 for the initial odd divisor candidate. None is a quantified free constant. There are no unspecified constants or asymptotic thresholds.

## 5. Vacuity and trivial-witness risks

The premise is satisfiable, for example at m = 1. The case m = 0 is excluded; viewed as an implication there, the premise would be false. No other contradictory hypothesis appears.

Zero cannot be a summand, and neither 0 nor 1 satisfies the required sign. Empty factor lists therefore cannot supply a witness. Equal summands are allowed, but must still satisfy the sum and both sign conditions. Distinctness, ordering, coprimality, and primality of the summands are not required. There is no assertion about other residue classes or nonpositive integer summands.

## 6. Verdict

**READBACK-CLEAN.** No vacuity or witness-scope defect is apparent in the literal assertion. The exact semantic caveat is `Declaration.lean:5`: `omega` uses `primeFactorsList.length`; `Dependencies.lean:46–47` confirms multiplicity on prime powers. It does not count distinct prime divisors.

This label describes the literal code reading only. It certifies neither correspondence to an unseen source nor a proof or compilation of the supplied declaration excerpts.
