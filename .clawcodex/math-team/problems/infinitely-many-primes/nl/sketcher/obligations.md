# Obligation ledger — infinitely-many-primes

Mode: DISCOVERY — conjectural; no proof weight.

Author: `nl-sketcher`. Every entry below is **UNPROVED**. This ledger assigns
each load-bearing construction, estimate, theorem application, case split, and
assembly bridge to a named obligation, and marks the keystone(s). Definitions
and normalizations live in `target-contract.md`; lemma statements in
`lemma-plan.md`.

Status vocabulary: `open` = unproved and unassigned; `open → L#` = unproved,
located inside lemma `L#` of the plan.

---

## 1. Definition obligations

| ID | Obligation | Notes | Keystone |
|---|---|---|---|
| `O-DEF1` | Fix the base definition of "prime" as the divisor form `D2`: `p > 1` and every `d ∈ ℕ` dividing `p` is `1` or `p`. | Normalization `N3`. Determines "1 is not prime", "2 is the least prime". | no |
| `O-DEF2` | (Optional, completeness) Show `D2` (divisor form) and `D3` (irreducible/factorization form) define the same primes in ℕ. | **Not needed** by Route A; recorded so `A2`/`A3` are not silently dropped. | no |
| `O-DEF3` | Fix the ordinary reading of ℕ and of the target's domain as the positive integers (`N1`, `N2`). | Both readings of "does 0 ∈ ℕ" yield equivalent statements (contract §3). | no |

## 2. Lemma-level obligations

| ID | Obligation | Depends on | Keystone |
|---|---|---|---|
| `O-L1` | **Prime divisor existence:** every `m ∈ ℕ` with `m ≥ 2` has a prime divisor. Minimal-element argument by well-ordering of ℕ. Include the explicit non-circularity check (no use of infinitude of primes, no use of FTA uniqueness). | `O-DEF1`, well-ordering of ℕ, transitivity of `|` (`O-AR2`) | **YES** |
| `O-L2` | **Small prime divides the factorial:** for `n ∈ ℕ` and `p` prime with `p ≤ n`, `p | n!`. | `O-DEF1`, definition of factorial | no |
| `O-L3` | **`n!+1` coprime to `n!`:** `n! + 1 > 1` and any `d ∈ ℕ` dividing both `n!` and `n! + 1` equals `1`. | `O-AR3` | no |
| `O-L4` | **Case split to conclude `p > n`:** fix `n`, set `M := n!+1`, take a prime `p | M` from `L1`, split on `p ≤ n` vs `p > n` via trichotomy, close the `p ≤ n` branch with `L2` + `L3`. Includes exhaustion of the two branches and the contradiction `p > 1 ∧ p = 1`. | `O-L1`, `O-L2`, `O-L3`, `O-AR1` | no (assembly-critical) |
| `O-L5` | **Bridge:** finite `S ⊆ ℕ` is bounded above; contrapositive: unbounded above ⟹ infinite. Induction on `|S|`. | `O-AR4` | no (assembly-critical) |
| `O-L5c` | (Optional) bounded above ⟹ finite, via `S ⊆ {1,…,N}`. Recorded for the equivalence in the contract §1; not needed for `L6`. | `O-L5` | no |
| `O-L6` | **Assembly:** `L4` gives `∀n ∃p ∈ P, p > n`; `L5` with `S := P` gives `P` infinite; by contract §1 this is the original target. | `O-L4`, `O-L5` | no (terminal) |

## 3. Elementary-arithmetic / order obligations (shared infrastructure)

| ID | Obligation | Used by |
|---|---|---|
| `O-AR1` | Trichotomy/linear order on ℕ: for all `a, b ∈ ℕ`, exactly one of `a < b`, `a = b`, `a > b`; hence `a ≤ b` or `a > b`. | `O-L4` |
| `O-AR2` | Divisibility facts: `d | d`; `d | p ∧ p | m ⟹ d | m` (transitivity). | `O-L1` |
| `O-AR3` | Divisibility linearity with subtraction on ℕ: `d | a ∧ d | b ∧ a ≥ b ⟹ d | (a − b)`; and `d ∈ ℕ ∧ d | 1 ⟹ d = 1`. | `O-L3` |
| `O-AR4` | All finite subsets of ℕ (including ∅) have a maximum, hence a bound; subsets of `{1,…,N}` are finite. | `O-L5`, `O-L5c` |
| `O-AR5` | Factorial facts: for `n ∈ ℕ`, `n! ≥ 1`, so `n! + 1 ≥ 2 > 1`; `n! ` is the product `1·2⋯n`. | `O-L2`, `O-L3`, `O-L4` |

These are stated separately because a generator may treat them as "obvious" and
skip them; each is cheap but each is load-bearing at exactly the place named.

## 4. Theorem applications (exact statement, preconditions, non-circularity)

| ID | Theorem used | Exact usable statement | Preconditions, and where they hold | Circular? |
|---|---|---|---|---|
| `O-T1` | Well-ordering of ℕ | Every nonempty `S ⊆ ℕ` has a least element. | `S = {d ∈ ℕ : d | m, d > 1}` is nonempty since `m ∈ S` (needs `m ≥ 2`; supplied by `O-AR5` in `L4`). | No — a property of ℕ's order, independent of primes. |
| `O-T2` | Mathematical induction on ℕ | Standard induction schema; used for `L5`/`L5c`. | `S ⊆ ℕ` arbitrary. | No. |

**Explicitly NOT used (recorded to prevent smuggling):** Fundamental Theorem of
Arithmetic (existence *and* uniqueness), Euclid's lemma
(`p | ab ⟹ p | a ∨ p | b`), Dirichlet/analytic input, Bertrand's postulate,
Euclid numbers machinery beyond `L1`. The target is elementary and none of these
is required.

## 5. Assembly bridges

| ID | Bridge | From → To | Keystone |
|---|---|---|---|
| `O-B1` | Notation bridge: `P := {p ∈ ℕ : p prime}` and `P ⊆ ℕ`. | `O-DEF1` → `O-L5` applicability | no |
| `O-B2` | Reading bridge: "`P` is infinite" ⟺ "there are infinitely many primes" (primary reading, contract §1). | `O-L5` result → original target | no |
| `O-B3` | Quantifier preservation: `L4`'s `∀n ∃p` order is preserved; the banned swapped form `∃p ∀n` is *not* used. | `O-L4` → `O-L6` | no |

## 6. Explicit non-obligations

- No construction of an explicit infinite sequence of primes is required.
- No estimate, bound, asymptotic, or density statement is required.
- No numerical or computational certificate is required, and none exists that
  could certify a general theorem.
- `O-DEF2`, `O-L5c` are optional completeness items; leaving them undone does
  not leave the target unproved.

## 7. Keystone summary and dependency-critical path

- **Keystone blocker: `O-L1`** (via well-ordering `O-T1`). Highest risk of
  handwaving and the only plausible circularity site.
- **Assembly-critical: `O-L4`** (case split and contradiction closure) and
  **`O-L5`** (the bridge that spends the "infinitely many" reading).
- **Critical path:** `O-DEF1` → `O-T1`/`O-AR2` → `O-L1` → `O-L4` → `O-L6`;
  second path: `O-AR4` → `O-L5` → `O-L6`.
- **Independent frontier:** `O-L1`, `O-L2`, `O-L3`, `O-L5` can be worked in any
  order; none depends on another.

## 8. Status

All obligations listed above are **open**. No obligation has been discharged,
no lemma has been proved, and no part of the original target has been
established. Mathematical acceptance of this ledger, the target contract, and
the lemma plan is a separate, leader-owned review.
