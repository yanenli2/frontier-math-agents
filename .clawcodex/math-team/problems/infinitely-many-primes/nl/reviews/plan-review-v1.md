# Plan review packet v1 — infinitely-many-primes

Mode: **CERTIFICATION** (fresh, independent). Reviewer has no prior context.
This is an LLM mathematical review of a *plan*; it is **not** a Lean
kernel/compiler result and does not verify any lemma's truth.

## 1. Artifact identity (hashes recomputed by the reviewer)

All three reviewed files are under
`.clawcodex/math-team/problems/infinitely-many-primes/nl/sketcher/`.

| File | SHA-256 (recomputed) | Matches supplied? |
|---|---|---|
| `target-contract.md` | `1cc7975d9ef0888a58d85efc3ed75f1f48a1e69aa1fea2bdf114897b0ac53a83` | YES |
| `lemma-plan.md` | `e9d61a7cf1bccf4b1efa6fc5506d01dce400c59a86f9a44fb797dd984cce16d9` | YES |
| `obligations.md` | `501c581d5d112b59fb335bf6ac71596ddf1e20c227a43fc9ab0f12e8856c0914` | YES |

Snapshot is current and self-consistent; no file changed since dispatch. All three
carry `Mode: DISCOVERY` internally, which is expected for a sketcher-produced
plan; the *review* is conducted in CERTIFICATION mode against the plan criteria
(a)–(c).

## 2. Inputs read

- `.clawcodex/skills/math-team/references/protocol.md`
- `.../infinitely-many-primes/request.md` (verbatim source of the target)
- `.../nl/sketcher/target-contract.md`
- `.../nl/sketcher/lemma-plan.md`
- `.../nl/sketcher/obligations.md`
- Directory listing of `.../nl/` and `.../nl/reviews/` (to confirm no competing/older snapshots).

Verbatim target confirmed: `request.md` reads
`> Prove that there are infinitely many primes.` — the contract (§ header) quotes
it identically. No reinterpretation introduced at the source.

## 3. Check (a) — Target fidelity

**Exact assertion.** Contract §1 fixes `P := {p ∈ ℕ : p prime}` and takes the
primary reading to be "`P` is infinite" (no `k ∈ ℕ` with a bijection
`{1,…,k} → P`), with the working form `∀ n ∈ ℕ, ∃ p ∈ P, p > n`. This is the
correct, standard formalization of the request. No free variable, parameter,
hypothesis, or implication is added; the target is an unconditional closed
statement (contract §2). ✔

**Quantifier order.** Contract §2 explicitly states the working form order is
`∀∃` and load-bearing, and that the swapped `∃ p ∀ n, p > n` is **false** and is
**not** the target. Correct: no prime exceeds every natural. The plan's L4 is
stated as `∀n ∃p` (lemma-plan §2, L4) and obligations `O-B3` guards that the
swapped form is not used. The distinction is handled correctly and is not
smuggled. ✔

**Domain / boundary conventions.** `N1` fixes `ℕ = {1,2,3,…}`; `N4`/`A3`
exclude negatives; `A4` records that ℚ is not intended. The boundary table
(§5) fixes: `1` not prime (`D2` requires `p > 1`), `2` the least prime, finite/
empty case in scope. The `N2` argument that "does `0 ∈ ℕ`" is immaterial is
correct and I re-verified it: over `ℕ_+:={1,2,…}` the instance `n = 1` yields a
prime `p > 1 > 0`, so the extra `n = 0` case of a `{0,1,2,…}` reading is implied;
hence the two `ℕ` conventions give equivalent working forms, and `0 ∉ P` either
way. ✔

**`A1` (cardinality vs. unboundedness).** The contract does **not** silently
choose a reading. It names `A1`, states the primary (cardinality) reading, gives
the working (unboundedness) form, asserts their equivalence for `S ⊆ ℕ`, and
supplies the bridge `L5` so the reading is *spent* at a named obligation
(`O-L5`) rather than hidden in assembly. lemma-plan §5 and obligations §5
(`O-B2`) make the bridge explicit, and the contract even notes the plan is robust
if the leader instead fixes the target as the working form (then `L5` becomes
optional). This is honest handling. ✔

Minor, non-blocking remark on §1: "finite ⟺ ∃ k ∈ ℕ, bijection {1,…,k} → P"
technically fails for the empty set under `ℕ = {1,2,…}`; since `P ∋ 2 ≠ ∅`, this
is immaterial here. Recorded for precision only.

## 4. Check (b) — Adequacy of the decomposition

Lemma statements are self-contained and correctly quantified:

- **L1** `∀ m ∈ ℕ (m ≥ 2) ∃ p ∈ ℕ (p | m ∧ p prime)`. Explicitly quantified; no
  ambient hypothesis. Route sketch (minimal element of `S = {d ∈ ℕ : d | m, d>1}`)
  is internally complete: `S ≠ ∅` since `m | m` and `m ≥ 2`; `p := min S` exists
  by well-ordering; for any `d | p` with `d ∉ {1,p}`, a divisor of `p` satisfies
  `d ≤ p`, so `1 < d < p`, whence `d | m` (transitivity) contradicts minimality.
  I checked the divisor case is exhaustive (`d ≤ p` because `p = d·c`, `c ≥ 1`).
  ✔
- **L2** `∀ n ∈ ℕ ∀ prime p (p ≤ n ⟹ p | n!)`. Vacuous at `n = 1`; content at
  `n ≥ 2`. Definitional product property. ✔
- **L3** `∀ n ∈ ℕ (n!+1 > 1 ∧ ∀ d ∈ ℕ (d | n! ∧ d | (n!+1) ⟹ d = 1))`.
  `n! ≥ 1 ⟹ n!+1 ≥ 2`. Subtraction-linearity step is legitimate since
  `n!+1 ≥ n!`. Phrased without `gcd`, self-contained. ✔
- **L4** `∀ n ∈ ℕ ∃ prime p (p > n)`. Case split via trichotomy on `p` vs `n`,
  with `M := n!+1 ≥ 2`, `p | M` from L1; branch `p ≤ n` closed by L2 (`p | n!`)
  + L3 (`p = 1`), contradicting `p > 1`. Both branches exhaustive; the closing
  contradiction is valid. ✔
- **L5** finite `S ⊆ ℕ` ⟹ bounded above; contrapositive unbounded ⟹ infinite.
  Stated for all `S ⊆ ℕ`; induction sketc. handles `∅` by `N = 1`. ✔
- **L6** the target, with both readings named. ✔

**Sufficiency.** `L4` (working form) + `L5` (contrapositive, `S := P`) ⟹ `P`
infinite = primary reading. I find **no missing lemma and no smuggled
assumption**:
- The only non-trivial existence fact on the critical path is `L1`, which is a
  stated lemma, not an invoked background theorem.
- `L4` uses exactly `L1, L2, L3` + order trichotomy; `L6` uses exactly `L4, L5`.
- Factorial/arith/order infrastructure used by the routes (trichotomy,
  transitivity/reflexivity of `|`, subtraction linearity, `n! ≥ 1`) is itemized
  as `O-AR1…O-AR5`, not left as "obvious".

The dependency graph (lemma-plan §1) is accurate, including the parenthetical
"(L5 does not feed L4)" — correct, and important: it certifies that L4 does not
presuppose any finiteness/infiniteness of `P`.

## 5. Check (c) — Assembly implication and circularity

Assembly (lemma-plan §3): (1) `P ⊆ ℕ`; (2) L4 gives `∀n ∃p∈P, p>n`; (3) L5
contrapositive with `S := P` gives "`P` infinite"; (4) that is the primary
reading. Each step is a valid application of the named terminal/lemma statement;
no step uses an unproved fact outside the lemma set. ✔

**Circularity, especially the keystone L1.** L1's minimal-element argument uses
only well-ordering of `ℕ`, the definition of `|`, and transitivity of `|`. It
does **not** assume infinitude of primes, and does **not** invoke uniqueness (or
existence) of prime factorization. Non-circular. `L4` makes no assumption about
`P` being finite or infinite; `L5` is a statement about arbitrary subsets of `ℕ`
and never mentions primes. The assembly therefore does not presuppose its
conclusion. ✔

**Verification of the plan's own "not used" list.** I traced every route:
- FTA (existence and uniqueness): not used — L1 returns a *single* prime divisor
  via well-ordering, never a factorization; nothing else needs unique
  factorization.
- Euclid's lemma (`p | ab ⟹ p | a ∨ p | b`): not used — L2 is the product-factor
  property of `n!`, and L3 is subtraction-linearity of `|`; neither is Euclid's
  lemma.
- Dirichlet / Bertrand / analytic or density input: not used — no estimate,
  bound, or asymptotic appears anywhere on the critical path.

The claim in obligations §4 ("explicitly NOT used …") and lemma-plan §6 is
therefore **accurate** against the actual assembly and lemma routes. ✔

One wording nuance (non-blocking): lemma-plan §6 says "no FTA (uniqueness)",
while obligations §4 says "existence *and* uniqueness". Since FTA *existence*
is likewise unused, the obligations phrasing is the more complete one and is the
correct claim; the lemma-plan parenthetical is merely narrower wording, not a
contradiction.

## 6. Load-bearing concerns (precise locations)

No concern rises to a break point. The following are recorded for the leader,
all repairable and none affecting the assembly:

1. **`obligations.md` §3, row `O-AR4`** — "All finite subsets of ℕ (**including
   ∅**) have a **maximum**, hence a bound." The empty set has **no maximum** (it
   is bounded by `N = 1` vacuously). The `O-AR4` text is imprecise; the L5
   statement and its route sketch correctly handle `∅` separately (lemma-plan §2,
   L5). Recommend rewording `O-AR4` to "nonempty finite `S ⊆ ℕ` has a maximum;
   all finite `S` (including `∅`) have a bound" before lemma proofs are written,
   so an induction base case cannot be misread. Non-blocking.

2. **`target-contract.md` §1 / §6 `A1` (judgment call, not a defect)** — The
   contract declines to escalate `A1` to a definition audit, arguing both
   readings are equivalent and the route covers both. Given `L5` supplies the
   equivalence and the plan is robust to either fixed reading, this is defensible
   and is explicitly flagged (not silent). I note it only because `A1` is the one
   convention that changes the obligation set; the leader retains authority to
   pin the reading, which the contract itself states.

3. **`target-contract.md` §1 (precision only)** — the finite-set characterization
   via `{1,…,k}` omits the empty set; immaterial because `P ≠ ∅`. No action
   required for this target.

## 7. Scope of this verdict

- This review certifies only: **(a)** that the contract faithfully captures the
  original request (quantifier order, domain, boundary conventions, honest `A1`
  handling); **(b)** that the lemma decomposition is self-contained, correctly
  quantified, and sufficient; **(c)** that the assembly validly derives the
  original target from the terminal lemma statements, without circularity and
  without silently invoking unproved facts.
- This review does **not** certify that any lemma `L1`–`L6` is true, nor any
  obligation's discharge. All lemmas and obligations remain **unproved**; the
  assembly is *conditional* on `L1`–`L5`.
- This is an LLM mathematical review, not Lean kernel/compiler verification.

## 8. Recommended next action

1. Accept (or record as accepted) the target contract and lemma plan structure.
2. Optionally apply the `O-AR4` rewording in §6.1 above.
3. Dispatch proofs of the independent frontier `L1, L2, L3, L5` — `L1` first, as
   the keystone and highest circularity risk — then `L4` (case split / keystone
   `O-L4`) and the `L6` assembly (`O-L6`, `O-B1..O-B3`).
4. Route each completed lemma proof to a fresh independent reviewer; do not treat
   the plan's plausibility as evidence for any lemma.

VERDICT: PASS

Scoped verdict: the contract is target-faithful, the decomposition is adequate,
and the assembly implication is valid (with two minor, non-blocking wording
notes in §6). Lemma proofs remain outstanding and are not certified here.
