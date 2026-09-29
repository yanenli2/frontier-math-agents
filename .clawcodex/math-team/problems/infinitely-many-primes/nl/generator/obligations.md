# Obligation ledger — proof attempt `proof-v1.md`

**Mode:** CERTIFICATION candidate. This ledger records, for every load-bearing
construction, theorem application, case split, and assembly bridge in
`proof-v1.md`, either its explicit discharge or a precise unresolved gap. The
author does **not** certify; a fresh verifier does.

**Status vocabulary:** `DISCHARGED` = proved by an explicit argument in
`proof-v1.md` (section given); `OPEN` = not proved, with the gap named.

---

## 0. Disposition summary

All obligations inherited from `nl/sketcher/obligations.md` that are on the
critical path are `DISCHARGED`. The only entry left `OPEN` is `O-DEF2`, an
*optional* completeness item that the route does not use. There is **no
unresolved gap on the critical path**.

| Plan ID | Content | Status | Where |
|---|---|---|---|
| `O-DEF1` | fix `D2` as the prime definition | DISCHARGED | `proof-v1.md` §0.3 |
| `O-DEF2` | `D2 ⟺ D3` (divisor vs. factorization form) | **OPEN** (optional; not used) | §5 below |
| `O-DEF3` | ℕ = positive integers (`N1`,`N2`) | DISCHARGED | §0.2, §5 remark |
| `O-L1` | prime divisor existence (keystone) | DISCHARGED | §2 |
| `O-L2` | small prime divides factorial | DISCHARGED | §3 |
| `O-L3` | `n!+1` coprime to `n!` | DISCHARGED | §4 |
| `O-L4` | case split to `p > n` | DISCHARGED | §5 |
| `O-L5` | finite `⊆ ℕ` ⟹ bounded | DISCHARGED | §6 |
| `O-L5c` | bounded ⟹ finite (converse) | DISCHARGED | §6 |
| `O-L6` | assembly to the target | DISCHARGED | §7 |
| `O-AR1` | trichotomy / total order | DISCHARGED | §1 E1 |
| `O-AR2` | `d|d`, transitivity of `|` | DISCHARGED | §1 E6 |
| `O-AR3` | subtraction-linearity of `|`; `d|1 ⟹ d=1` | DISCHARGED | §1 E9, E8 |
| `O-AR4` | nonempty finite `S ⊆ ℕ` has a max; all finite `S` have a bound | DISCHARGED | §6 L5-g + §6 empty case |
| `O-AR5` | factorial facts | DISCHARGED | §1 E10 |
| `O-T1` | well-ordering of ℕ | DISCHARGED (invoked in L1) | §2 |
| `O-T2` | induction on ℕ | DISCHARGED (invoked in L2, L5, L5c) | §3, §6 |
| `O-B1` | notation bridge `P ⊆ ℕ` | DISCHARGED | §7 step 1 |
| `O-B2` | reading bridge `P infinite ⟺ infinitely many primes` | DISCHARGED | §7 step 4 + §6 |
| `O-B3` | quantifier preservation `∀n∃p` | DISCHARGED | §7 step 2 |

---

## 1. Ambient-framework obligations

| ID | Obligation | Discharge | Circular? |
|---|---|---|---|
| `O-AMB1` | ℕ is a commutative semiring, `1 ≤ a` (AR1) | Stated as the standard model of ℕ; used only via E3, E5. | No primes mentioned. |
| `O-AMB2` | `≤` total order compatible with `+`,`·` (AR2) | Standard order on ℕ; yields E1, E3. | No. |
| `O-AMB3` | `a < b ⟺ ∃c, b = a+c`; discreteness (AR3) | Standard; yields E2, E9. | No. |
| `O-AMB4` | additive/multiplicative cancellation (AR4) | Standard (ℕ has no zero divisors); yields E4, E5, uniqueness of difference. | No. |
| `O-AMB5` | well-ordering (AR5) | Standard; invoked **once**, in L1. | No — order property of ℕ, independent of primes. |

*Gap note:* these are treated as the ambient standard structure of ℕ (Peano
axioms / ordered semiring), consistent with `target-contract.md` §3–§4 which
supplies no separate axiom list. They are not derived from the target; using
them is not circular. If the verifier demands a fully axiom-internal derivation
of E1–E10 from a single closed axiom set, that is a scope extension, not a gap
in the present route.

---

## 2. Definitions and constructions

| ID | Item | Discharge |
|---|---|---|
| `O-DEF1` | Base prime definition is `D2` (`p>1` and all divisors in `{1,p}`). | Fixed verbatim from `target-contract.md` §4 (`N3`); used unchanged. |
| `O-CON-F` | Finiteness of a set (Definition F). | `proof-v1.md` §0.4; matches contract §1. `P ≠ ∅` by E11, so the empty alternative does not arise for `P`. |
| `O-CON-FACT` | Factorial `n!` by recursion `1!:=1`, `(n+1)!:=n!·(n+1)`. | `proof-v1.md` §1 E10; well-defined by recursion on ℕ. |
| `O-CON-S` | Set `S := {d ∈ ℕ : d|m, d>1}` in L1. | `proof-v1.md` §2; nonempty because `m ∈ S` (needs `m ≥ 2`). |
| `O-CON-M` | `M := n!+1` in L4. | `proof-v1.md` §5; `M ≥ 2` by E10(b). |

---

## 3. Lemma obligations (detailed)

### `O-L1` — prime divisor existence (KEYSTONE) — DISCHARGED
- **Construction:** `S = {d ∈ ℕ : d|m, d>1}`, `p := min S`.
- **Nonemptiness:** `m ∈ S` — reflexivity E6(a), and `m > 1` from `m ≥ 2`.
- **`p` prime:** `p > 1` by membership; for `d | p`, E7 gives `d ≤ p`; if
  `d > 1` then E6(c) gives `d | m`, so `d ∈ S`, so `p ≤ d`, so `d = p`.
- **Non-circularity:** uses only `D1`, E6(a,c), E7, E1, AR5. No infinitude of
  primes, no FTA, no Euclid's lemma, no extraction-by-iteration.
- **Verdict:** fully proved, `proof-v1.md` §2. The one well-ordering invocation
  `O-T1` is legitimate because `S ≠ ∅` is checked.

### `O-L2` — small prime divides factorial — DISCHARGED
- **Method:** induction on `n ≥ 1` (uses `O-T2`), recursion `(n+1)! = n!·(n+1)`.
- **Cases:** `p ≤ n` (IH + transitivity E6c) vs. `p > n` (then discreteness E2
  forces `p = n+1`, and `(n+1)! = n!·p`). Exhaustive by E1.
- **Preconditions:** `p ∈ ℕ`, factorial defined for all ℕ; base `n=1` vacuous
  (no prime `≤ 1`).
- **Verdict:** proved, `proof-v1.md` §3.

### `O-L3` — `n!+1` coprime to `n!` — DISCHARGED
- (i) `n!+1 > 1`: E10(a) gives `n! ≥ 1`.
- (ii) `d|n!` and `d|(n!+1)`: apply E9 with `a=n!+1`, `b=n!`, `a>b`;
  `a−b = 1`; then E8 gives `d=1`.
- **Verdict:** proved, `proof-v1.md` §4. No gcd primitive introduced.

### `O-L4` — case split to conclude `p > n` — DISCHARGED
- **Construction:** `M := n!+1 ≥ 2` (E10b), prime `p | M` from L1.
- **Case split:** E1 trichotomy gives `p ≤ n` or `p > n`; exhaustive.
- **Branch `p ≤ n`:** L2 gives `p | n!`; L3(ii) with `d := p` gives `p = 1`;
  contradicts `p > 1` (`D2`). Branch closed.
- **`∀n∃p` order preserved; no finiteness assumption.**
- **Verdict:** proved, `proof-v1.md` §5.

### `O-L5` — finite `⊆ ℕ` ⟹ bounded — DISCHARGED
- **Empty case:** `N := 1`, vacuous.
- **Nonempty:** Definition F + induction on `k` proving L5-g ("a set with a
  bijection `{1,…,k} → S` has a greatest element"): base `k=1`; step uses
  `max(g', f(k+1)) ∈ ℕ`.
- **Bound:** `N := g ∈ S ⊆ ℕ`.
- **Contrapositive `L5*`:** "unbounded ⟹ infinite", used for the target.
- **Verdict:** proved, `proof-v1.md` §6.

### `O-L5c` — bounded ⟹ finite — DISCHARGED
- `S ⊆ {1,…,N}`; induction on `N` proving every subset of `{1,…,N}` is finite;
  step splits on `N+1 ∈ T`.
- **Non-load-bearing** for the target; supplies the second half of the `A1`
  equivalence.
- **Verdict:** proved, `proof-v1.md` §6.

### `O-L6` — assembly — DISCHARGED
- Steps: `P ⊆ ℕ`; L4 ⟹ `P` unbounded (`O-B3`); L5\* with `S:=P` ⟹ `P` infinite;
  definitional reading bridge ⟹ original target.
- **Verdict:** proved, `proof-v1.md` §7.

---

## 4. Elementary-arithmetic obligations

| ID | Fact | Discharge |
|---|---|---|
| `O-AR1` / E1 | trichotomy / totality of `≤` | `proof-v1.md` §1 E1 |
| `O-AR2` / E6 | `d|d`, `1|b`, transitivity of `|` | §1 E6 |
| E7 | `a|b ⟹ a ≤ b`; `a|b ∧ b|a ⟹ a=b` | §1 E7 |
| `O-AR3` / E9 | subtraction-linearity `d|a ∧ d|b ∧ a>b ⟹ d|(a−b)` | §1 E9 |
| `O-AR3'` / E8 | `d|1 ⟹ d=1` | §1 E8 |
| E3 | `ab ≥ a`, `ab ≥ b` | §1 E3 |
| E4 | `ab=1 ⟹ a=b=1` | §1 E4 |
| `O-AR5` / E10 | `n! ≥ 1`, `n!+1 ≥ 2 > 1` | §1 E10 |
| E11 | `2` is prime, `P ≠ ∅` | §1 E11 |

All discharged by explicit arguments.

**Note on `O-AR4` wording (flagged by the plan-level review).** The reviewed
`nl/sketcher/obligations.md` §3 row `O-AR4` reads "All finite subsets of ℕ
(including ∅) have a maximum," which is imprecise: `∅` has no maximum. `L5` in
`proof-v1.md` §6 does **not** inherit this defect. It splits the two facts
explicitly:
* *bound fact* — **all** finite `S ⊆ ℕ`, including `∅`, are bounded above (the
  empty case takes `N := 1`, bound vacuous);
* *max fact* — every **nonempty** finite `S ⊆ ℕ` has a greatest element
  (Lemma L5-g), which is what the inductive step actually uses.

The induction base case is therefore unambiguous: base `k = 1` produces the
maximum `f(1)` of a one-element set, and `∅` is handled entirely outside the
induction by the vacuous `N := 1`.

---

## 5. Theorem applications and remaining gaps

| ID | Theorem | Exact statement | Preconditions & where checked | Circular? | Status |
|---|---|---|---|---|---|
| `O-T1` | Well-ordering of ℕ (AR5) | Every nonempty `S ⊆ ℕ` has a least element. | `S = {d∈ℕ : d|m, d>1}` nonempty since `m ∈ S` (`m ≥ 2`). Checked in §2. | No — order property of ℕ. | DISCHARGED |
| `O-T2` | Induction on ℕ | Standard induction schema. | Used in L2 (§3, on `n`), L5 (§6, on `k`), L5c (§6, on `N`). | No. | DISCHARGED |

**Explicitly NOT used (anti-smuggling record):** Fundamental Theorem of
Arithmetic (existence *or* uniqueness), Euclid's lemma
(`p|ab ⟹ p|a ∨ p|b`), Dirichlet/analytic input, Bertrand's postulate,
"iterate extraction of a prime factor" (which would presuppose L1). Confirmed in
`proof-v1.md` §2 (non-circularity check) and §8 (audit).

### `O-DEF2` — OPTIONAL, left OPEN
- **Statement:** `D2` (divisor form) and `D3` (irreducible/factorization form)
  define the same primes in ℕ.
- **Status: OPEN.** Not proved here. It is **not used** by the route (the route
  uses only `D2`, specifically `p > 1` and the divisor condition), so leaving it
  open does **not** leave the target unproved. Recorded so that ambiguity `A2`
  is not silently dropped. If a verifier or the leader requires the equivalence
  for completeness, it becomes a fresh obligation (one direction, `D2 ⟹ D3`, is
  immediate: `p = ab` gives `a | p`; the other direction needs a least-proper-
  divisor argument and is not needed here).

---

## 6. Assembly bridges

| ID | Bridge | From → To | Discharge | Status |
|---|---|---|---|---|
| `O-B1` | `P := {p∈ℕ : p prime}`; `P ⊆ ℕ`. | definitions → L5 applicability | `proof-v1.md` §7 step 1 | DISCHARGED |
| `O-B2` | "`P` is infinite" ⟺ primary reading "infinitely many primes". | L5\* result → target | §7 step 4 (definitional, per contract §1); `A1` equivalence proved via L5 + L5c in §6 | DISCHARGED |
| `O-B3` | `L4`'s `∀n∃p` order preserved; swapped `∃p∀n` not used. | L4 → L6 | §7 step 2; §8 quantifier audit | DISCHARGED |

---

## 7. Case-split and exhaustion record

| Split | Location | Exhaustive? | Closing argument |
|---|---|---|---|
| `p ≤ n` vs. `p > n` (trichotomy E1) | L4, §5 | Yes | `p ≤ n` branch contradicts `p > 1`; `p > n` gives conclusion |
| `p ≤ n` vs. `p > n` (trichotomy E1) | L2 step, §3 | Yes | both give `p \| (n+1)!` |
| `S = ∅` vs. `S ≠ ∅` | L5, §6 | Yes | vacuous bound / greatest element |
| `d ≤ 1` vs. `d > 1` | L1, §2 | Yes | `d=1` / `d ∈ S` forces `d=p` |
| `N+1 ∈ T` vs. `N+1 ∉ T` | L5c, §6 | Yes | both finite |
| `k=1` vs. `k → k+1` | L5-g, §6 | Yes (induction) | base / greatest element |

---

## 8. Unresolved issues

1. **None on the critical path.** Every obligation feeding the target is
   discharged by an explicit argument in `proof-v1.md`.
2. **`O-DEF2` (optional) is OPEN**, as recorded in §5; it is off the route and
   is not required by the target under the accepted reading `N3`.
3. **Ambient framework scope.** The proof takes the standard structure of ℕ
   (AR1)–(AR5) as given, per `target-contract.md` §3–§4 (which supplies no
   alternative axiom set). E1–E10 are derived from it. This is a scope
   statement, not a gap.
4. **No self-certification.** Acceptance is deferred to a fresh
   `math-nl-verifier`; the author asserts no verdict.
