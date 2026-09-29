# Target contract — infinitely-many-primes

Mode: DISCOVERY — conjectural; no proof weight.

Author: `nl-sketcher`. Source of the target: `request.md`, verbatim:

> Prove that there are infinitely many primes.

No formal statement, no domain restriction, and no conventions document were
supplied. Everything below that is not literally in the request is a recorded
normalization, labelled `N1`, `N2`, … . Ambiguities that remain are listed in
§6 and are **not** silently decided.

---

## 1. Exact assertion

**Primary reading (cardinality reading of "infinitely many").**

Let
```
P := { p ∈ ℕ : p is prime }.
```
The assertion is:

> `P` is an infinite set, i.e. there is no k ∈ ℕ and no bijection {1,…,k} → P.
> Equivalently, `P` is not finite.

**Equivalent working form (unboundedness reading).** For the same `P`:

> ∀ n ∈ ℕ, ∃ p ∈ P with p > n.

"Infinitely many primes" is true in the primary reading **iff** it is true in
the working form; the two readings are equivalent for subsets of ℕ (see §6,
ambiguity `A1`, and Lemma `L5` in `lemma-plan.md`). The intended proof route
establishes the working form and converts it to the primary reading through
`L5`. This makes the reading choice an **explicit obligation** rather than a
silent convention.

## 2. Quantifier structure

- Working form: `∀ n ∈ ℕ, ∃ p ∈ P, p > n`. Order is `∀∃` and is **load-bearing**.
- The swapped form `∃ p ∈ P, ∀ n ∈ ℕ, p > n` is **false** (no prime exceeds
  every natural number) and is **not** the target.
- Primary form: a statement about cardinality — `¬ ∃ k ∈ ℕ, ∃ bijection
  {1,…,k} → P`.
- There is no free variable, no parameter, no hypothesis, and no implication:
  the target is an unconditional closed statement.

## 3. Domain

- **Normalization `N1` (domain of the primes):** primes are drawn from the
  **positive integers**, written ℕ = {1, 2, 3, …}. This is the standard reading
  of an unrestricted request. Rationals are excluded: in ℚ every nonzero element
  is a unit, so "prime of ℚ" is not a standard notion and is not intended
  (recorded as `A4`).
- **Normalization `N2` (does ℕ contain 0?):** immaterial. If 0 ∈ ℕ, the case
  `n = 0` of the working form is implied by the case `n = 1` (any prime `p > 1`
  satisfies `p > 0`), and 0 is not prime under both candidate definitions since
  primes must exceed 1. The two readings of ℕ therefore yield statements that
  are equivalent, so no audit is required.

## 4. Accepted definitions

**`D1` (divisibility).** For `a, b ∈ ℕ`: `a | b` iff `∃ c ∈ ℕ, b = a·c`.

**`D2` (prime — divisor form; the normalized definition for this problem).**
`p ∈ ℕ` is **prime** iff
```
p > 1   and   ∀ d ∈ ℕ, ( d | p  ⟹  d = 1 ∨ d = p ).
```
Consequences used explicitly below: a prime `p` satisfies `p > 1`; and `1` is
**not** prime (it fails `p > 1`). `2` is prime and is the least prime, since it
is the least element of ℕ greater than 1.

**`D3` (composite / factorization form; recorded alternative).** `p ∈ ℕ` is
irreducible iff `p > 1` and for all `a, b ∈ ℕ`, `p = a·b ⟹ a = 1 ∨ b = 1`.

**Normalization `N3`:** we adopt the divisor form `D2` as the definition of
"prime". Both `D2` and `D3` are standard. Their equivalence in ℕ is a genuine
(and easy) claim, recorded as `A3` and as obligation `O-DEF2`; it is **not
needed** by the proof route below, which uses only "prime ⟹ p > 1" and the
divisor condition from `D2`.

**Normalization `N4` (no sign ambiguity).** Primes are positive by `D2`
(`p > 1` excludes `−2, −3, …`). Recorded, not ambiguous: the standard reading of
an unrestricted request in this context is primes in ℕ.

## 5. Boundary conventions (explicit)

| Question | Answer used | Why |
|---|---|---|
| Is `1` prime? | No | `D2` requires `p > 1`. |
| Is `2` the first prime? | Yes, least prime | least element of ℕ above 1 |
| Are primes drawn from ℕ, ℤ, or ℚ? | ℕ (positive integers) | `N1`; ℚ has no primes, `D2` excludes negatives |
| Is the empty/finite case of "infinitely many" in scope? | Yes — the negation `P` finite must be refuted | primary reading §1 |
| Does the argument need `n ≥ 1` or `n ≥ 2`? | Any `n ∈ ℕ` works; `n = 1` gives `p = 2` | `L4` is stated for all `n ∈ ℕ` |

## 6. Recorded ambiguity

**`A1` — "infinitely many" as cardinality vs. unboundedness above.**
These are equivalent for `S ⊆ ℕ`, but the equivalence is a lemma, not a
definition. **Resolution adopted here:** prove the working (unboundedness) form
and supply the bridge `L5`. No audit is strictly required, and the plan is
robust to either reading: if the leader fixes the target as the working form,
`L5` becomes optional and the target is unchanged in content. *This is the one
convention that changes the shape of the obligation set*, so it is flagged
rather than assumed.

**`A2` — "prime" defined by divisors (`D2`) vs. by factorization (`D3`).**
Does not affect the truth value or the route; tracked as `O-DEF2`.

**`A3` — sign convention for primes.** Resolved by `N4`; does not affect the
truth value.

**`A4` — ℚ has no primes in the standard sense.** Not intended; recorded.

**Assessment.** No listed ambiguity changes the *truth value* of the target: all
admissible readings give a true statement, and the same argument settles all of
them. The only reading that changes the *obligation set* is `A1`, and it is
handled by an explicit lemma. Therefore **no definition-audit request to the
leader is raised as a blocker**; the leader may nonetheless overrule `N3`/`A1`.

## 7. What this contract does NOT claim

- It does not claim any lemma in `lemma-plan.md` is proved.
- It does not assert that the chosen route (Euclid's argument) is the only
  route; it is the route the generator will be asked to follow, with an
  equivalent variant noted in `lemma-plan.md` §4.
- Mathematical acceptance of this contract and of the plan is a separate,
  leader-owned review.
