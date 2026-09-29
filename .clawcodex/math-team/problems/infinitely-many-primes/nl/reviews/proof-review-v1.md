# Independent review packet — `proof-v1.md` (infinitely many primes)

**Review type:** CERTIFICATION (fresh, one-shot, LLM mathematical referee).
**Problem:** `infinitely-many-primes`.
**Date of review snapshot:** the exact files hashed below; no later version reviewed.
**Note on method:** This is an LLM mathematical review. It is **not** a Lean
kernel or compiler verification, and it does not constitute formal machine-checked
proof. Verdicts are mathematical judgments about the written argument. I did not
read author confidence statements, prior verdicts, or any other review file; the
pre-existing `nl/reviews/plan-review-v1.md` was **not** opened (observed to exist
via directory listing only).

---

## 1. Artifacts, paths, and computed hashes

All paths absolute. Hashes recomputed by me with `shasum -a 256` on the exact
current snapshot.

| Role | Path | SHA-256 (computed) | Supplied | Match |
|---|---|---|---|---|
| Verbatim request | `.clawcodex/math-team/problems/infinitely-many-primes/request.md` | `9f00e717c176b535507ed6bb4b4e88f54efc9f860eaff4e9aa887b0786309616` | (none supplied) | n/a |
| Target/definition baseline | `.../nl/sketcher/target-contract.md` | `1cc7975d9ef0888a58d85efc3ed75f1f48a1e69aa1fea2bdf114897b0ac53a83` | same | ✅ |
| Baseline decomposition | `.../nl/sketcher/lemma-plan.md` | `e9d61a7cf1bccf4b1efa6fc5506d01dce400c59a86f9a44fb797dd984cce16d9` | same | ✅ |
| Baseline obligations | `.../nl/sketcher/obligations.md` | `501c581d5d112b59fb335bf6ac71596ddf1e20c227a43fc9ab0f12e8856c0914` | same | ✅ |
| **Candidate proof** | `.../nl/generator/proof-v1.md` | `8a9cfda30bb3667442155db72547857cf6eac98f19687bf03bc236feb1260053` | same | ✅ |
| Candidate ledger | `.../nl/generator/obligations.md` | `81cc4c1d0063bae7ec882563666d142e33973ab4077a48142fd4df35b1062fb8` | same | ✅ |
| Candidate report | `.../nl/generator/report.md` | `735b8c3e5ca5fe24b07fb45e71efa74abf467e55c7f97a3a6973d96af7391e31` | same | ✅ |

**Snapshot integrity:** every supplied hash matches. No file has changed; I
reviewed exactly the version described. The baseline sketcher artifacts were
treated as the accepted target/definition baseline only, not as evidence of truth.

**Inputs read:** `request.md`, `nl/sketcher/target-contract.md`,
`nl/sketcher/lemma-plan.md`, `nl/sketcher/obligations.md`, `nl/generator/proof-v1.md`,
`nl/generator/obligations.md`, `nl/generator/report.md`,
`.clawcodex/skills/math-team/references/protocol.md`. No external sources or
knowledge-base pages were required or used.

---

## 2. Target fidelity

**Request (verbatim, `request.md`):** "Prove that there are infinitely many primes."

**Baseline reading (`target-contract.md` §1):** primary reading is cardinality —
`P := {p ∈ ℕ : p prime}` is infinite; equivalent working form is
`∀n ∈ ℕ ∃p ∈ P, p > n`. Domain fixed by `N1` as `ℕ = {1,2,3,…}`; prime fixed by
`D2` (divisor form). Reading ambiguity `A1` (cardinality vs. unboundedness) is
recorded as an obligation to be bridged, not silently assumed.

**What the candidate establishes (`proof-v1.md` §7, §0.1):**
`∀ n ∈ ℕ ∃ p ∈ P, p > n` (working form, `∀∃` order), and `P` is infinite
(cardinality), together with the equivalence of the two.

Checks:

- **Quantifier order.** The candidate proves `∀n ∃p` and explicitly disclaims the
  false swapped form `∃p ∀n` (§0.1, §7 step 2, §8 quantifier audit). The order is
  preserved verbatim from `L4` to assembly. ✅
- **No weakening.** The cardinality statement is the full original claim; the
  working form is *equivalent* to it for subsets of ℕ, so proving it is not a
  weakening (§6 L5 + L5c, §7). ✅
- **No problematic strengthening.** Only equivalent forms are asserted. ✅
- **Conversion legitimacy.** The candidate does not merely assert `A1`; it proves
  both directions: `L5` (finite ⟹ bounded above) and `L5c` (bounded above ⟹
  finite), yielding `infinite ⟺ unbounded above` (§6 Remark). The bridge `L5*`
  (unbounded ⟹ infinite) is the literal contrapositive of `L5`. This is the
  exact direction needed, and it is discharged, not assumed. ✅
- **Reading convention.** The reliance on the contract's primary (cardinality)
  reading is the accepted baseline, and the candidate additionally proves the
  equivalence, so the reading choice is justified regardless of which admissible
  reading the leader fixes. ✅

**Conclusion (fidelity):** the candidate proves the exact original claim.

---

## 3. Step-by-step load-bearing checks

I independently re-derived each step; "✅ = verified" means I reproduced the
argument and found it correct and non-circular.

### 3.1 Ambient framework `AR1`–`AR5` (§0.5)
Standard true properties of `ℕ = {1,2,…}`: commutative/associative
multiplication with identity `1` and `1 ≤ a` (AR1); total order compatible with
`+`,`·` (AR2); `a < b ⟺ ∃c∈ℕ, b=a+c` plus discreteness (AR3); additive and
multiplicative cancellation (AR4); well-ordering (AR5). All are true of ℕ and
mention no primes, so invoking them is not circular. Minor: calling `ℕ={1,2,…}` a
"commutative semiring" is terminologically loose (no additive identity in this
truncation), but none of the *used* clauses depends on the semiring label. ✅
(non-load-bearing label).

### 3.2 Elementary facts E1–E11 (§1)
- **E1 trichotomy/totality** — derives strict order from total order + antisymmetry.
  ✅
- **E2 discreteness** — restates AR3. ✅
- **E3 product domination** `ab ≥ a, ab ≥ b` — from `b ≥ 1` and monotonicity. ✅
- **E4 no-zero-divisor** `ab=1 ⟹ a=b=1` — correct, uses E2/E3. ✅
- **E5 cancellation** — AR4. ✅
- **E6 divisibility basics** `a|a`, `1|b`, transitivity — correct from `D1`. ✅
- **E7** `a|b ⟹ a ≤ b`, and `a|b ∧ b|a ⟹ a=b` — correct in ℕ since the
  cofactor lies in ℕ (≥1). ✅
- **E8** `d|1 ⟹ d=1` — correct via E4. ✅
- **E9 subtraction-linearity of `|`** — needs `a>b` so `a−b∈ℕ` exists (AR3) and
  is unique (E5). The argument (`a=dx≤dy=b` contradiction if `x≤y`, else
  `x=y+c'`, `a=b+dc'`) is correct. Note the discipline: `a−b` is only formed when
  `a>b`, so no invalid ℕ-subtraction. ✅
- **E10 factorial** — recursion `1!:=1`, `(n+1)!:=n!·(n+1)`; `n! ≥ 1` by induction;
  `n!+1 ≥ 2 > 1`. Base and step valid. ✅
- **E11** `2` prime, `P ≠ ∅` — `2>1`, divisors of 2 in ℕ are `{1,2}` via E7+E2.
  ✅

### 3.3 `L1` — prime divisor existence (keystone) (§2)
Construct `S = {d∈ℕ : d|m, d>1}`; nonempty since `m|m` (E6a) and `m>1`
(given `m≥2`). AR5 gives `p := min S`, so `p|m`, `p>1`. Prime check: for `d|p`,
E7 gives `d≤p`; E1 splits `d≤1` (⟹ `d=1`) vs `d>1` (⟹ `d|m` by E6c, so `d∈S`,
so `p≤d`, hence `d=p`). Thus divisors of `p` in ℕ are only `1,p`, and `p>1`, so
`p` is prime by `D2`. **Verified correct.** Non-circularity: uses only `D1`,
`E6a`, `E6c`, `E7`, `E1`, `AR5`; no infinitude, no FTA (existence or uniqueness),
no Euclid's lemma, no iterative factor-extraction loop. The minimal element is
produced directly by well-ordering. ✅ **This is the key auditor concern and it
passes.**

### 3.4 `L2` — a prime `≤ n` divides `n!` (§3)
Induction on `n≥1`. Base `n=1`: vacuous (no prime `≤1`). Step: for prime
`p≤n+1`, E1 splits `p≤n` (IH + `n!|(n+1)!` via recursion + E6c) vs `p>n`
(then `n<p≤n+1`, E2 forces `p=n+1`, and `(n+1)!=n!·p`). Cases exhaustive; base
valid. ✅

### 3.5 `L3` — `n!+1` coprime to `n!` (§4)
(i) `n!+1>1` from E10a. (ii) For `d|n!` and `d|(n!+1)`: set `a:=n!+1`, `b:=n!`,
so `a>b`; E9 gives `d|(a−b)`, `a−b=1`, E8 gives `d=1`. Subtraction precondition
`a>b` satisfied. ✅

### 3.6 `L4` — unboundedness `∀n ∃p prime, p>n` (§5)
Fix `n`, `M:=n!+1≥2` (E10b), so `L1` applies to `m:=M`; get prime `p|M`. E1 on
`(p,n)` splits `p>n` (done) vs `p≤n`: then `L2` gives `p|n!`, `L1` gave
`p|(n!+1)`, so `L3(ii)` with `d:=p` gives `p=1`, contradicting `p>1` (`D2`).
Case closed; first case holds. No finiteness assumption on `P` anywhere.
Exhaustive split, valid contradiction closure, valid use of each precondition. ✅

### 3.7 `L5`, `L5*`, `L5c` (§6)
- **`L5`** (finite ⟹ bounded above). `S=∅`: `N:=1`, vacuous. `S≠∅` finite: from
  Definition F get a bijection `{1,…,k}→S`, `k≥1`. Prove `L5-g` by induction on
  `k≥1`: base `k=1` gives the singleton's maximum; step restricts to
  `S'=S\{f(k+1)}` (a genuine bijection `{1,…,k}→S'`), applies IH to get `g'`, and
  takes `g=max(g',f(k+1))∈ℕ`. This yields a greatest element, hence bound `N:=g`.
  **Correctly founded induction** (base k=1, step k→k+1). ✅
- **`L5*`** — literal contrapositive of `L5`; "unbounded above" is exactly
  `∀n∃s>n` = ¬(∃N∀s,s≤N) via trichotomy/De Morgan. ✅
- **`L5c`** (bounded ⟹ finite, converse; non-load-bearing) — reduce to subsets of
  `{1,…,N}`, induction on `N`, split on `N+1∈T`; both branches finite. ✅

### 3.8 `L6` — assembly (§7)
`P⊆ℕ` (from `D2`); `L4` gives `P` unbounded above preserving `∀∃`; `L5*` with
`S:=P` gives `P` infinite; contract §1 identifies this with "infinitely many
primes". Each step uses only already-verified lemmas plus the definitional reading
bridge fixed by the accepted baseline. ✅

---

## 4. Hypothesis / source / dependency audit

- **Hypotheses.** The target is an unconditional closed statement; the candidate
  inserts no hypothesis (no finiteness of `P`, no genericity, no existence
  assumption). Every divisibility use has arguments in ℕ; the "`d≥1`/`d>1`"
  conditions are forced by `D2`, `E1`, `E10`, as shown. Verified in §2–§7 and
  checked against §8's audit. ✅
- **Sources.** No external theorem is cited. The only ambient principles are
  AR1–AR5, all standard true properties of ℕ, none mentioning primes. No
  knowledge-base page or toolchain output is required or relied upon. ✅
- **Dependencies.** The dependency graph used is
  `D1,D2,AR* → {L1,L2,L3,L5(g)} → L4 → L5* → L6`, matching `lemma-plan.md`'s
  intended route (Route A). `L1,L2,L3,L5` are mutually independent as claimed. ✅
- **Preconditions of the one nontrivial invocation (`O-T1`, well-ordering in L1).**
  `S` is shown nonempty (`m∈S`, using `m≥2`); AR5 then legitimately yields a least
  element. ✅
- **Counted/uncounted case splits.** `p≤n` vs `p>n` (L4 and L2), `S=∅` vs `≠∅`
  (L5), `d≤1` vs `d>1` (L1), `N+1∈T` vs `∉T` (L5c), base `k=1` vs step (L5-g):
  all exhaustive; recorded in the candidate ledger §7 and independently confirmed. ✅
- **"NOT used" list, independently re-checked against the actual argument.**
  FTA (existence *and* uniqueness), Euclid's lemma, Dirichlet/Bertrand/analytic
  input, and iterative factor-extraction are genuinely **not** invoked anywhere in
  §1–§7. The keystone `L1` is a pure well-ordering/minimality argument. ✅

---

## 5. Boundary and precision audit

- **Is `1` prime?** No, by `D2` (`p>1`); used in L1's case split and L3's
  conclusion — consistent. ✅
- **Is `2` the least prime / is `P≠∅`?** `E11` proves `2∈P`; used only to note the
  empty alternative of Definition F never applies to `P` — not load-bearing for
  the cardinality conclusion (Definition F handles `∅` directly). ✅
- **Empty set.** Handled separately in `L5` (bound `N:=1`, vacuous) and in `L5c`
  (base case). ✅
- **"Greatest element" claim.** `L5-g` claims a maximum only for sets admitting a
  bijection from `{1,…,k}` (`k≥1`, hence nonempty); `∅` is never given a maximum.
  The candidate explicitly corrects the baseline ledger's imprecise `O-AR4` row
  ("all finite subsets including ∅ have a maximum") and does not inherit the
  defect (candidate `obligations.md` §4; `proof-v1.md` §6). This auditor agrees the
  candidate's split (bound-whenever-finite / maximum-when-nonempty) is correct. ✅
- **Subtraction in ℕ.** `a−b` is only formed when `a>b` (E9, L3), with existence
  from AR3 and uniqueness from E5. No ℕ-subtraction outside its domain. ✅
- **Factorial domain.** Defined for all `n∈ℕ` by recursion with base `1`; `L2`'s
  base `n=1` is vacuous as required. ✅
- **`N2` (does `0∈ℕ`?).** The candidate notes the `n=0` case is implied by
  `n=1` and that primes are `>1` in both readings (§0.2, §5 remark). This is a
  scope remark, consistent with the baseline; it does not affect the proof under
  the adopted `ℕ={1,2,…}`. ✅

---

## 6. Remaining unresolved load-bearing obligations

**None on the critical path.** Every load-bearing obligation feeding the target is
discharged by an explicit argument in `proof-v1.md`:

`O-DEF1`, `O-DEF3`, `O-L1`, `O-L2`, `O-L3`, `O-L4`, `O-L5`, `O-L5c`, `O-L6`,
`O-AR1`–`O-AR5`, `O-T1`, `O-T2`, `O-B1`–`O-B3` — all verified above.

**Off critical path:**
- `O-DEF2` (`D2 ⟺ D3`, divisor form vs. irreducible form) is left **OPEN** by the
  author. This is genuinely off the route: the proof uses only `D2` (specifically
  `p>1` and the divisor condition). Leaving it open does **not** leave the target
  unproved. Not a gap in the present claim. ✅

No obligation is claimed discharged that is in fact open. No required case, base
case, or precondition is left unchecked. No circular reasoning found.

---

## 7. Scope and limits of this verdict

- **In scope:** whether `proof-v1.md` proves the exact original claim ("there are
  infinitely many primes") under the accepted contract (`D1`, `D2`, `N1`–`N4`,
  reading `A1`), with all load-bearing steps, preconditions, case splits, and
  boundary conventions checked.
- **Not in scope / not claimed:** formal (Lean/kernel/compiler) verification;
  acceptance of the optional `O-DEF2` completeness item; and exhaustion of any
  alternative admissible reading the leader might fix (the proof is written for
  `ℕ={1,2,…}` and transferable to `0∈ℕ`, per §0.2). This report is an LLM
  mathematical review, not machine-checked proof.
- **Independence:** this review is fresh; it used no author-confidence statements
  and no prior verdicts. The baseline sketcher files were used only as the accepted
  statement/definition baseline, never as evidence of truth.

---

## 8. Recommended next action

The candidate is mathematically sound as written. Recommended: the leader accepts
`proof-v1.md` for the `infinitely-many-primes` task under the frozen contract
(hashes above). The optional `O-DEF2` item may be left open or scheduled as a
separate, non-blocking completeness task; it does not affect the target. If a
formal off-route is later desired, a Lean formalization against `D1`/`D2` would be
the appropriate independent re-check — this review is not a kernel result.

---

**VERDICT: PASS** — the candidate proves the exact original statement
("there are infinitely many primes") under the accepted definitions, domain, and
readings; every required hypothesis, source, case split, boundary convention, and
load-bearing obligation on the critical path checked out; the keystone prime-divisor
lemma is proved non-circularly by well-ordering; the cardinality bridge is proved,
not assumed; and the sole open obligation (`O-DEF2`) is genuinely off the critical
path.
