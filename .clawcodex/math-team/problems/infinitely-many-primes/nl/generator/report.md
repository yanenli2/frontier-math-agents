# Report — NL proof attempt for `infinitely-many-primes`

**Worker:** `nl-generator`. **Task:** `c8cda8d1feb1`.
**Mode:** CERTIFICATION (proof attempt; carries no proof weight until an
independent `math-nl-verifier` accepts it).
**Deliverable status:** artifact production **complete**. The author does **not**
self-certify and asserts no proof verdict.

## 1. Inputs read

| Path | Role | Reviewed hash (sha256) |
|---|---|---|
| `.../infinitely-many-primes/request.md` | original target, verbatim | — |
| `.../nl/sketcher/target-contract.md` | definitions, domain, readings, normalizations | `1cc7975d9ef0888a58d85efc3ed75f1f48a1e69aa1fea2bdf114897b0ac53a83` |
| `.../nl/sketcher/lemma-plan.md` | lemma statements `L1`–`L6`, dependency graph | `e9d61a7cf1bccf4b1efa6fc5506d01dce400c59a86f9a44fb797dd984cce16d9` |
| `.../nl/sketcher/obligations.md` | obligation IDs to discharge | `501c581d5d112b59fb335bf6ac71596ddf1e20c227a43fc9ab0f12e8856c0914` |
| `.../.clawcodex/skills/math-team/references/protocol.md` | team protocol | — |

The leader confirmed the sketcher bundle passed plan-level review (fidelity,
decomposition, assembly implication) and is frozen at the hashes above; this
attempt was written against exactly that version. The PASS certified no lemma as
true; `L1`–`L6` were proved here from scratch.

## 2. Outputs produced (this worker, absolute paths)

- `.clawcodex/math-team/problems/infinitely-many-primes/nl/generator/proof-v1.md`
- `.clawcodex/math-team/problems/infinitely-many-primes/nl/generator/obligations.md`
- `.clawcodex/math-team/problems/infinitely-many-primes/nl/generator/report.md` (this file)

## 3. What was proved

The exact target: `P := { p ∈ ℕ : p prime }` is infinite, under contract
definitions `D2` (`p > 1` and every divisor in ℕ is `1` or `p`), domain
`ℕ = {1,2,…}` (`N1`), and the recorded normalizations. Route: prove the working
`∀n ∃p` form (unboundedness), then convert to the cardinality reading through the
`A1` bridge.

Structure of `proof-v1.md`:

- **§0** Target, two readings, domain (`N1`,`N2`), definitions `D1`,`D2`,
  finiteness Definition F, and the ambient framework (AR1)–(AR5) for ℕ.
- **§1** Elementary facts E1–E11, each proved: trichotomy, discreteness, product
  domination, no-zero-divisor, cancellation, divisibility basics, `| ⇒ ≤`,
  `d|1 ⇒ d=1`, subtraction-linearity of `|`, factorial facts, and `2` prime.
- **§2 (L1, keystone)** Every `m ≥ 2` has a prime divisor, via
  `S = {d : d|m, d>1}`, well-ordering `p := min S`, and a minimality argument.
  Includes the explicit non-circularity check (no infinitude, no FTA, no
  Euclid's lemma, no factor-extraction loop).
- **§3 (L2)** `p ≤ n` prime `⟹ p | n!`, by induction on `n` on the factorial
  recursion.
- **§4 (L3)** `n!+1 > 1` and `d | n! ∧ d | (n!+1) ⟹ d = 1`, via
  subtraction-linearity (E9) and E8.
- **§5 (L4)** `∀ n ∈ ℕ ∃ prime p > n`, with `M := n!+1`, `L1`, and the
  `p ≤ n` vs. `p > n` split closed by `L2`+`L3`.
- **§6 (L5, L5\*, L5c)** Finite `⊆ ℕ` ⟹ bounded (with `L5-g`: nonempty finite
  sets have a greatest element) and its contrapositive `L5*`, plus the converse
  `L5c` completing the `A1` equivalence.
- **§7 (L6)** Assembly to the original target.
- **§8** Global hypothesis, circularity, quantifier, and boundary audits.
- **§9** Status and scope caveats.

## 4. Dependencies and how they were satisfied

- **Inherited from the plan:** definitions/domain from the contract (`D1`,`D2`,
  `N1`–`N4`, `A1`); lemma statements `L1`–`L6`; obligation IDs.
- **Proved here (not inherited):** all of `L1`–`L6` and the elementary facts
  E1–E11; every `O-*` on the critical path is discharged in
  `obligations.md`.
- **Ambient, standard:** structure of ℕ (AR1)–(AR5). No external source or
  knowledge-base page was needed; no toolchain/computation was required.

## 5. Reading bridge `A1` (handled explicitly, not silently)

`target-contract.md` records `A1` (cardinality vs. unboundedness) as an explicit
bridge. This attempt proves both halves: `L5*` (unbounded ⟹ infinite, the
direction used for the target) and `L5c` (bounded ⟹ finite, its converse),
giving the equivalence for subsets of ℕ. The assembly `§7 step 4` spends the
reading bridge definitionally, matching contract §1.

## 6. Reviewer finding addressed

The plan-level review flagged that `nl/sketcher/obligations.md` §3 row `O-AR4`
("all finite subsets of ℕ (including ∅) have a maximum") is imprecise, since `∅`
has no maximum. `proof-v1.md` §6 does not inherit this: it states separately
that **all** finite subsets (including ∅, bound `N := 1`) are bounded above, and
that **nonempty** finite subsets have a greatest element (Lemma L5-g, used in the
induction). This is documented in `obligations.md` §4 and summarized in the
`O-AR4` row of §0.

## 7. Unresolved issues

- **Critical path: none.** Every obligation feeding the target is discharged by
  an explicit argument.
- **`O-DEF2` (optional) remains OPEN:** the equivalence of `D2` (divisor form)
  and `D3` (irreducible form) is not proved here. It is off the route and is not
  required for the target under accepted reading `N3`; recorded in
  `obligations.md` §5 so ambiguity `A2` is not silently dropped.
- **Ambient-framework scope:** E1–E11 are derived from the standard structure of
  ℕ (AR1)–(AR5), which the contract does not replace. This is a scope statement,
  not a gap in the route.

## 8. Next action

Hand `proof-v1.md` (+ `obligations.md`) to a **fresh** independent
`math-nl-verifier` for acceptance in a separate, leader-owned task. The generator
does not self-certify and claims no verdict. If the verifier requests the
`O-DEF2` equivalence or an axiom-internal derivation of the ambient facts, that
is a scope extension to be routed back through the leader.
