# Lemma plan — infinitely-many-primes

Mode: DISCOVERY — conjectural; no proof weight.

Author: `nl-sketcher`. Definitions, domain, and normalizations are fixed by
`target-contract.md` (same directory) and are used here without restatement.
**Every lemma below is UNPROVED.** Nothing here carries proof weight. The
statements are written so each is self-contained: all symbols are either
defined in `target-contract.md` §3–§4 or quantified inside the statement.

Notation: ℕ = {1,2,3,…}; `d | b` as in `D1`; "prime" as in `D2`.

---

## 1. Lemma graph (dependency-ordered)

```
  L1  (prime divisor exists)      ─┐
  L2  (small prime divides n!)    ─┤
  L3  (n!+1 is coprime to n!)     ─┼──►  L4  (unboundedness: ∀n ∃ prime > n)
                                   │              │
  L5  (finite ⊆ ℕ ⟹ bounded)  ─────┼──────────────┴──►  L6  (TARGET: P infinite)
                                   │
                          (L5 does not feed L4)
```

Independence: `L1`, `L2`, `L3`, `L5` are mutually independent and depend only on
the definitions plus elementary arithmetic/order facts (§3). `L4` depends on
`L1, L2, L3`. `L6` depends on `L4` and `L5`.

---

## 2. Lemma statements

### `L1` — Every integer greater than 1 has a prime divisor
> For every `m ∈ ℕ` with `m ≥ 2`, there exists `p ∈ ℕ` such that `p | m` and
> `p` is prime (in the sense of `D2`).

- **Dependency preconditions:** none beyond `D1`, `D2` and the well-ordering of
  ℕ (every nonempty subset of ℕ has a least element). Checked: the statement
  quantifies `m` explicitly, so no ambient hypothesis is needed.
- **Route sketch (obligations, not proofs):** set `S := { d ∈ ℕ : d | m, d > 1 }`.
  `S ≠ ∅` because `m ∈ S`; let `p := min S`, which exists by well-ordering.
  Show `p` is prime: if `d | p` and `1 < d < p`, then by transitivity of `|`,
  `d | m`, so `d ∈ S` with `d < p`, contradicting minimality; hence the only
  divisors of `p` in ℕ are `1` and `p`, and `p > 1` by construction.
- **Circularity check (required):** the argument uses only well-ordering of ℕ,
  the definition of `|`, and transitivity of `|`. It does **not** use the
  infinitude of primes, nor uniqueness of prime factorization (FTA). Hence it is
  non-circular with respect to `L6`. Assigned to `O-L1`.
- **Keystone:** YES — see §5.

### `L2` — A prime no larger than `n` divides `n!`
> For all `n ∈ ℕ` and all primes `p`, if `p ≤ n` then `p | n!`.

- **Dependency preconditions:** `n! := 1·2⋯n` for `n ≥ 1`; the factorial is
  defined for all `n ∈ ℕ`. Checked: `n = 1` gives `n! = 1` and no prime
  `p ≤ 1`, so the statement is vacuous there; the case `n ≥ 2` is the content.
- **Route sketch:** `n! ` is the product of all integers `1,…,n`; since
  `p ∈ ℕ` and `2 ≤ p ≤ n`, the factor `p` occurs in that product, so `p | n!`.
- **Circularity check:** none needed; purely a property of the product.

### `L3` — `n! + 1` is coprime to `n!`
> For every `n ∈ ℕ`: `n! + 1 > 1`, and every `d ∈ ℕ` with `d | n!` and
> `d | (n! + 1)` satisfies `d = 1`.

- **Dependency preconditions:** `n! ≥ 1` for `n ∈ ℕ`, so `n! + 1 ≥ 2 > 1`.
  Checked: holds for all `n ∈ ℕ` including `n = 1`.
- **Route sketch:** if `d | n!` and `d | (n! + 1)` then `d | (n! + 1) − n! = 1`
  (linearity of `|` under subtraction, legitimate because `n! + 1 ≥ n!`);
  in ℕ, `d | 1` forces `d = 1`.
- **Note:** no coprimality notion (gcd) is introduced; the statement is
  deliberately phrased with `|` alone to keep it self-contained.

### `L4` — Unboundedness of the primes
> For every `n ∈ ℕ` there exists a prime `p` with `p > n`.

- **Dependency preconditions:** `L1` (applied to `m := n! + 1`, which satisfies
  `m ≥ 2 > 1` — the hypothesis `m ≥ 2` of `L1` is checked using `L3`'s first
  clause); `L2` (applied to `n` and the prime `p` found, in the branch
  `p ≤ n`); `L3` (second clause, with `d := p`, in the branch `p ≤ n`);
  order trichotomy on ℕ (`p ≤ n` or `p > n`), available for all `p, n ∈ ℕ`.
  All preconditions are met unconditionally because `L4` has no hypothesis.
- **Route sketch (case split):** fix `n ∈ ℕ`; put `M := n! + 1`, so `M ≥ 2`. By
  `L1` pick a prime `p | M`. By trichotomy, either `p > n` (done) or `p ≤ n`; in
  the latter case `L2` gives `p | n!`, and with `p | M` `L3` gives `p = 1`,
  contradicting that `p` is prime (`p > 1` by `D2`). Hence `p > n`.
- **Case exhaustion:** the trichotomy is exhaustive and the two branches are
  exhaustive; the contradiction branch is closed. Assigned to `O-L4`.
- **Key point:** no finiteness assumption on the set of primes is made anywhere
  in `L4`; it is a direct `∀n ∃p` statement.

### `L5` — Finite subsets of ℕ are bounded above (bridge)
> For every `S ⊆ ℕ`: if `S` is finite, then `S` is bounded above, i.e.
> `∃ N ∈ ℕ, ∀ s ∈ S, s ≤ N`. Equivalently (contrapositive):
> if `S` is unbounded above, i.e. `∀ n ∈ ℕ ∃ s ∈ S, s > n`, then `S` is infinite.

- **Dependency preconditions:** none beyond the definitions of finite set and
  subset of ℕ, and induction on ℕ. Checked: the statement is universally
  quantified over `S ⊆ ℕ`.
- **Route sketch:** by induction on the cardinality `k` of `S`: the empty set is
  bounded by `N = 1` vacuously; a set of size `k+1` is a set of size `k` plus one
  point, and the bound is the max of the old bound and the new point. Both
  operations stay in ℕ because `S ⊆ ℕ` is nonempty in the inductive step.
- **Completeness note (not load-bearing):** the converse — bounded above
  implies finite, because `S ⊆ {1,…,N}` and subsets of a finite set are finite —
  is recorded for the equivalence claimed in `target-contract.md` §1 but is
  **not** needed for `L6`; assigned to `O-L5c`, marked non-keystone.
- **Scope note:** `L5` is a general fact about ℕ, not about primes; it is listed
  as a lemma precisely so that the "infinitely many" reading choice does not
  hide inside the assembly step.

### `L6` — TARGET
> `P := { p ∈ ℕ : p is prime }` is an infinite set; equivalently, for every
> `n ∈ ℕ` there exists `p ∈ P` with `p > n`.

- **Dependency preconditions:** `L4` (gives the working form), `L5` (converts it
  to the cardinality form). `P ⊆ ℕ` by `D2`, so `L5` applies to `S := P`.
  Both preconditions are unconditional.
- **This is the original target** under the primary reading; see §3.

---

## 3. Assembly argument (how the terminal lemmas give the original target)

Let `P := { p ∈ ℕ : p prime }` and let the original claim be
"there are infinitely many primes".

1. `P ⊆ ℕ` by `D2` (`N1`: primes are positive natural numbers).
2. `L4` supplies the working form: `∀ n ∈ ℕ, ∃ p ∈ P, p > n`.
3. Applying `L5` with `S := P` (contrapositive clause) to step 2 yields
   "`P` is infinite".
4. By `target-contract.md` §1, "`P` is infinite" is exactly the primary reading
   of "there are infinitely many primes". Hence the original target holds.

**Assembly checks.**

- *Statement match:* step 4 is the same proposition as the primary reading in
  the contract; no weakening, no strengthening, no extra hypothesis is inserted.
- *Quantifier match:* the `∀∃` order of `L4` is preserved through `L5`; the
  cardinality statement is about the same set `P`.
- *No circularity at assembly:* `L4` does not assume `P` finite or infinite;
  `L5` is a general statement about subsets of ℕ and does not mention primes.
- *Conditional status:* the assembly is **conditional on `L1`–`L5`**. Until
  those are independently accepted, this argument is a plan, not a proof.
  Each dependency is therefore labelled unproved in `obligations.md`.
- *Bridge necessity:* without `L5`, `L4` alone yields the working form; the
  bridge is where the "infinitely many" reading is spent. It is listed as a
  named dependency (`O-L5`), not left implicit.

---

## 4. Equivalent variant (recorded, not a second branch)

**Route B (classical contradiction form).** Assume the set of primes is finite,
say `p₁,…,p_k`, put `N := p₁⋯p_k + 1`, and apply `L1` to `N` to get a prime
divisor not equal to any `pᵢ`. This is not an independent route: it uses the same
`L1` and, in addition, must name the list `p₁,…,p_k`, which presupposes exactly
the finiteness hypothesis under attack. It is recorded because generators often
produce it; steps of it can be reused, but the plan's dependency structure
follows Route A (`L4` + `L5`), which is stated for all `n ∈ ℕ` and needs no
finiteness assumption.

---

## 5. Independent frontier and keystone blocker

**Independent frontier (can be attacked in parallel, no mutual dependencies):**

| Lemma | Content | Depends on |
|---|---|---|
| `L1` | prime divisor of any `m ≥ 2` | definitions + well-ordering |
| `L2` | `p ≤ n`, `p` prime ⟹ `p | n!` | definition of factorial |
| `L3` | `n!+1` coprime to `n!` | divisibility arithmetic |
| `L5` | finite `S ⊆ ℕ` is bounded above | induction |

**Keystone blocker: `L1`.**
It is the only place where a non-trivial existence result is invoked
(well-ordering of ℕ, via a minimal-element argument). It is also the place with
the highest circularity risk, because a careless generator may "prove" it by
extracting a prime factor and iterating, or may invoke uniqueness of prime
factorization, either of which can smuggle in facts that presuppose the
conclusion. Failure or handwaving at `L1` blocks the entire route.

**Secondary risk (assembly): `L5`.** If `L5` is taken for granted rather than
stated, the cardinality reading of "infinitely many" is silently assumed. It is
independently easy but must not be omitted; assigned `O-L5`.

**Not blockers:** `L2`, `L3` are immediate; `L6` is pure bookkeeping once `L4`
and `L5` are accepted.

---

## 6. Size discipline

This is an elementary target. The graph deliberately contains five small
lemmas and no extra machinery: no `gcd`, no Fundamental Theorem of Arithmetic
(uniqueness), no Euclid's lemma (`p | ab ⟹ p | a ∨ p | b`), no analytic or
combinatorial estimate. `L1` is the only lemma requiring a genuine argument.
