# Lean implementation blueprint: exact positive-multiple-of-four target

Mode: CERTIFICATION — implementation planning only. No new theorem is established here.

## 1. Deliverables and exact scope

Let:

- `P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`;
- `W = P/waves/multiples-four`;
- `B = W/formal/descent-blueprint`;
- `M = P/lean/.lake/packages/mathlib`.

The target remains, in namespace `ArithmeticStatement`:

```lean
theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :
  HasRepresentation (4 * m)
```

No prime, residue, sign, coprimality, or witness-inequality premise is added to this target. Equal summands and `m = 1` remain allowed. The original all-even target is not claimed.

Artifacts:

- `B/Readback.lean.txt`: the complete code-only signature packet, containing the four exact defining dependencies `omega`, `lambda`, `HasSignedRepresentation`, `HasRepresentation`, both proposed new definitions, and all 19 proposed theorem headers. It has no proof bodies, comments, `sorry`, or axioms. The `.txt` extension is intentional: incomplete theorem headers are a specification, not an importable Lean module.
- `B/SignatureTypeProbe.lean` and `B/signature-type-probe.log`: the same 19 proposed proposition types elaborated by `#check`, using the actual imported baseline and the two proposed definitions. Exit status 0. Only unused-proof-binder-name linter warnings occurred; they are NOT a reason to remove mathematical premises. No theorem proofs are present.
- `B/api-audit.md`: exact inspected library APIs, guards, source locations, hashes, cache limitations, and failed-name corrections.
- `B/ApiProbeVerified.lean` and `B/api-probe-verified.log`: successful cached-API type/axiom probe. Earlier failed exploratory names are preserved separately in `ApiProbe.lean` / `api-probe.log` and excluded from the plan.
- `B/next-target.md`: operational priorities, two-slot schedule, and acceptance gates.

For blind readback, give only `Readback.lean.txt` and a private output path, not this blueprint, the NL proof, prior verdicts, or API commentary. Its baseline definitions are explanatory exact copies, not replacements for `Statement.Partial`. Actual implementation must import `Statement.Partial`, never duplicate them.

## 2. Input identity, installed environment, and status boundaries

Inspected project:

- `P/lean/lean-toolchain`: `leanprover/lean4:v4.32.2`.
- `lake env lean --version`: Lean 4.32.2, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`, arm64-apple-darwin24.6.0.
- `lakefile.toml`: library `Statement`, default target `Statement`, `autoImplicit = false`, mathlib revision `905b95818eb32af7874a58b427f50c1711a5e96c`.
- `lake-manifest.json`: same mathlib revision.
- Local mathlib HEAD: that exact commit, timestamp `2026-07-28T18:36:13+02:00`, within the inclusive 2026-07-31 cutoff.
- `Statement.lean` currently imports only Definitions, Scaffold, Smoke, Partial. No FourWork module exists in that import graph.

Input SHA-256 values checked:

| Input | SHA-256 |
|---|---|
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `W/nl/descent/proof-attempt-v1.md` | `23fc6ad19d1c45dd432945aa84756b190700b8c15394b1554ebb3ecaff82235e` |
| `W/nl/reviews/descent-review-v1.md` | `3a07d36077a0fc824201ce3a788fa82ad666f45c7b9cc0e0b2d468a9b61b6a04` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `W/formal/generator/FourCandidate.lean` | `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325` |

The supplied fresh NL review accepts §§1–8 at the natural-language level. It is not a Lean result. The candidate's 19 residue/square helpers are supplied as compiled but are not yet present in the baseline master; I inspected their exact source and hash, not a new proof build of that candidate. Their independent acceptance/integration gates remain separate. This blueprint changes no master, protected statement, proof body, dependency pin, or project configuration.

## 3. Existing material to reuse, not redeclare

`Statement.Definitions:6–8` defines Omega with multiplicity by `primeFactorsList.length`, and the integer-valued Liouville function by `(-1 : ℤ) ^ omega n`.

`Statement.Partial` already provides:

| Needed fact | Existing declaration / lines |
|---|---|
| Exact positive-witness existential | `HasSignedRepresentation`, `HasRepresentation`, 14–20 |
| Value at 1 | `lambda_one`, 47–49 |
| Two possible signs for a positive argument | `lambda_sign`, 51–55 |
| Complete multiplicativity, no coprimality requirement | `lambda_mul`, 62–64 |
| Prime sign | `lambda_prime`, 66–68 |
| Values at 2, 3, 4 | `lambda_two`, `lambda_three`, `lambda_four`, 70–82 |
| Multiplication by 2 | `lambda_two_mul`, 88–91 |
| Positive integer squares | `lambda_square`, 93–96 |
| Positive scaling of signed representations | `hasSignedRepresentation_mul`, 102–109 |
| All multiples of 8 | `representation_multiple_eight`, 157–159 |

Do not introduce another Liouville function, multiplicative-sign structure, prime-factor count, modular square predicate, units-valued sign type, or generic character infrastructure.

The exact `FourCandidate.lean:226–241` reduction is the final bridge:

```lean
theorem multiple_four_iff_prime_three_mod_four_core :
  (∀ m : ℕ, 0 < m → HasRepresentation (4 * m)) ↔
    ∀ p : ℕ, Nat.Prime p → 7 ≤ p → p % 4 = 3 →
      HasRepresentation (4 * p)
```

Its dependencies already handle primes 2 and 3, primes congruent to 1 modulo 4, even multipliers, positive-sign multipliers, negative-sign prime-factor cofactors, and positive scaling. It uses `multiple_four_iff_odd_prime_core` at 207–224. The sum-of-two-squares branch at 55–92 is already in that candidate; do not formalize the optional Wilson argument in NL §8.1 again.

For inventory, the 19 existing declarations are: `lambda_six`, `lambda_seven`, `twelve_two_sign_seed`, `representation_multiple_twelve`, `representation_multiple_four_of_lambda_one`, `representation_multiple_four_of_even`, `representation_multiple_four_of_three_dvd`, `representation_multiple_four_of_sum_two_squares`, `prime_one_mod_four_eq_sum_two_squares`, `representation_four_prime_one_mod_four`, `prime_divisor_positive_sign_cofactor`, `exists_prime_factor_of_lambda_neg_one`, `representation_multiple_four_of_prime_divisor`, `representation_multiple_four_of_prime_one_mod_four_dvd`, `exists_prime_one_mod_four_of_lambda_neg_one`, `representation_multiple_four_of_mod_four_one`, `representation_multiple_four_of_mod_four_ne_three`, `multiple_four_iff_odd_prime_core`, `multiple_four_iff_prime_three_mod_four_core`. Preserve these earlier artifacts even where the shortest final dependency path does not use every declaration.

## 4. Minimal source-aligned proof graph

All new internal names below are in `ArithmeticStatement.FourWork`; the final two representation declarations are in `ArithmeticStatement`. Exact binders and types are in the code-only packet. Labels here are prose graph IDs, not new definitions.

| ID | Proposed declaration | New dependencies | NL alignment |
|---|---|---|---|
| A1 | `lambda_reflection_eq_one_of_neg` | none | §1, implication (A), lines 61–63 |
| A2 | `lambda_double_reflection_eq_neg_one_of_pos` | none | §1, implication (C), lines 65–66 |
| A3 | `three_not_dvd_of_positive_pair` | A1, A2 | §3.1, lines 99–109 |
| A4 | `positive_pair_gap_step` | A2, A3 | §3.2–3.3, lines 111–138 |
| A5 | `no_positive_pair` | A4 | §3.3 well-founded gap descent |
| A6 | `lambda_antireflection_of_no_representation` | A1, A5 | §3 conclusion, lines 140–146 |
| G | `cyclic_short_multiple` | none | §4.2, lines 176–190 |
| B1 | `residueLambda_natCast` | new definition only | §4.1, representatives below p |
| B2 | `residueLambda_sign` | new definition only | §4.1, nonzero representatives |
| B3 | `residueLambda_neg` | definition; conditional antireflection | §4.1 equation (2) |
| B4 | `goodMultiplier_one` | B1 | §4.1 identity multiplier |
| B5 | `goodMultiplier_neg` | B3 | §4.1 closure under multiplication by −1 |
| B6 | `goodMultiplier_natCast_step` | G, B1, B2, B4, B5 | §4.2–4.3 least-bad-multiplier contradiction |
| B7 | `residueLambda_mul` | B6 | §4.3 all nonzero residues good |
| B8 | `lambda_eq_one_of_isSquare` | B1, B2, B7 | §4.4 first sentence; §5 square obstruction |
| C1 | `prime_dvd_quarter_isSquare` | no new helpers | §6 prime-divisor square assertion, via audited library reciprocity |
| C2 | `exists_small_prime_isSquare` | C1 | §6 choice of prime divisor and bound |
| D1 | `representation_four_prime_three_mod_four` | A6, B8, C2 | §7 direct Liouville specialization |
| D2 | `representation_multiple_four` | D1, existing exact core equivalence | §8 / existing 19-helper assembly |

Dependency diagram:

```text
baseline --> A1,A2 --> A3 --> A4 --> A5 --> A6 --+
                                              |
baseline/ZMod --> B1..B5 --> B6 --> B7 --> B8 --+--> D1 --> exact existing iff --> D2
                               ^              |
finite pigeonhole --> G -------+              |
audited reciprocity --> C1 --> C2 ------------+
```

A and C are completely independent. B accepts the source's full antireflection as an explicit conditional premise, so its implementation does not import A. The premise is discharged by A6 only in D1; it is not an added assumption on D1 or D2.

Only two new definitions are required:

1. `residueLambda p z := lambda z.val`;
2. `GoodMultiplier p a := a ≠ 0 ∧ ∀ z ≠ 0, residueLambda p (a*z) = residueLambda p a * residueLambda p z`.

No explicit defect structure, least-bad selector, minimum-gap function, quadratic character, least residue prime, or general-f setup is needed. All gap/quotient/index functions below are local lets, not transitive defining dependencies of theorem statements.

Omissions are deliberate: NL §2 local ternary identities and implication (B) are not used by §3; f(3) = −1 is already `lambda_three`; the full equality with the quadratic character and square-counting half-cardinality argument are stronger than needed; FSPD and the least residue prime are not needed; Wilson and a second all-m scaling proof duplicate the existing reduction. None becomes a speculative helper endpoint.

## 5. A: missing representation to full antireflection

### A1 and A2: keep their full natural-number domains

These two helpers do not need primality or oddness. They use exactly `hno : ¬ HasRepresentation (4*p)` and the displayed positivity/range/sign premises.

- A1: a negative value at `p-n` would give witnesses `4*n`, `4*(p-n)`, both positive and negative. Use `lambda_four` and `lambda_mul` only on positive factors. The complementary sign is therefore +1 by `lambda_sign`.
- A2: a positive value at `2*p-n` would give witnesses `2*n`, `2*(2*p-n)`, both negative by `lambda_two_mul`. Sign dichotomy gives the conclusion −1.

The constructors require `4*p = a+b`, whereas the input sum relations in the descent are often written `x+y=p`. Supply the correct equality orientation explicitly. Natural subtraction is safe only after recording the relevant `n ≤ p` or `n ≤ 2*p` bound.

### A3: no entry divisible by 3

Inputs: `0<x`, `0<y`, `x+y=p`, both signs +1, and `hno`. Suppose `x=3*u`. Then `u>0`, `u<p`, and `lambda_mul` with `lambda_three` gives `lambda u = -1`. A1 gives `lambda (p-u) = 1`, hence `lambda (3*(p-u)) = -1`.

A2 at `y` gives `lambda (2*p-y) = -1`, with `2*p-y=p+x`. These two positive arguments sum to `4*p`, using `x=3*u`. This contradicts `hno`. Apply the same declaration with the pair swapped for the right entry. No assumption `lambda p=-1` is used in this specialized argument: the source needed it only to derive f(3), which the baseline already supplies for lambda.

### A4: exact quotients before descent inequalities

From A3 for both entries and primality with `p≠3`, obtain nonzero residues of `x`, `y`, `p` modulo 3. Finite arithmetic of the residues and `x+y=p` gives

- `3 ∣ p+x`;
- `3 ∣ p+y`.

Use local witnesses `u=(p+x)/3`, `v=(p+y)/3`, and first prove exact equations `3*u=p+x`, `3*v=p+y` via `Nat.mul_div_cancel'`. These equations, not truncating-division heuristics, establish:

- `0<u`, `u<v`, `u+v=p`;
- A2 at `y`, respectively `x`, gives signs of `p+x`, respectively `p+y`, equal to −1;
- `lambda_three` and positive multiplicativity give both new signs +1;
- `3*(v-u)=y-x`, so `v-u<y-x`.

Most remaining arithmetic involves multiplication by the constant 3 and is suitable for `omega` after the exact equations are exposed. The helper returns a smaller ordered positive pair; it need not expose its particular quotient witnesses in the public type.

### A5 and A6: well-foundedness without a minimum selector

A5 can use strong induction on the natural gap of an ordered positive-positive pair. Use an induction predicate quantifying over both entries and their equality to the current gap. A4 produces another admissible pair with a strictly smaller gap. Its gap is positive because `u<v`.

For an arbitrary pair, primality and `p≠2` give oddness. Thus `x=y` is impossible when `x+y=p`; otherwise `p=2*x`. Swap the entries when necessary and invoke the ordered descent. Do not induct on `x`, `y`, or `p`; the construction does not necessarily shrink those quantities.

For A6, fix `0<n<p`. Both `n` and `p-n` are positive. Split the sign of `n`: the negative case is A1; in the positive case A5 excludes a positive complement, so sign dichotomy forces −1. This obtains exactly `lambda (p-n)=-lambda n` for the entire interval, not just `3*n<p`.

## 6. G: short cyclic multiple, with an implementable finite route

This is the most important proof-search dependency. Its exact conclusion is:

```text
∃ k : ℤ, ∃ d : ℕ,
  k ≠ 0 ∧ k.natAbs < n ∧ 0 < d ∧ n*d < p ∧ (k : ZMod p)*z = d.
```

Both bounds must be strict. `|k|≤n` is insufficient for the induction, and `n*d≤p` is insufficient for the representative product bridge. The hypothesis `z≠0` is essential.

### Recommended implementation: integer bins of the same circle

This proves precisely the source's short-multiple lemma, replacing sorted adjacent-gap bookkeeping by the finite pigeonhole version of the same circle argument. It needs no new general-purpose theorem or real-number import. Its only combinatorial library input is the probed `Finset.exists_ne_map_eq_of_card_lt_of_maps_to`.

For `i<n`, locally set

```text
r(i) = ((i : ZMod p)*z).val,
b(i) = n*r(i)/p.
```

Install `Fact p.Prime` locally. Then `r(i)<p`, `r(0)=0`, and `b(i)<n`. Also `r(i)=r(j)` implies `i=j` when `i,j<n`: cast the equality back to `ZMod p`, cancel `z`, then apply `ZMod.val` and simplify the casts using `i,j<n<p`.

Split into two cases:

1. **A point is in bin `n-1`.** Choose `i<n` with `b(i)=n-1`. Since `b(0)=0` and `2≤n`, `i≠0`. Set `k=-(i : ℤ)` and `d=p-r(i)`. We have `d>0`, `k≠0`, `k.natAbs=i<n`, and the required residue equality from `ZMod.natCast_zmod_val` and the cast of a bounded natural subtraction. The floor lower bound `(n-1)*p≤n*r(i)` gives `n*d≤p`. Equality would imply `n∣p`; primality and `2≤n<p` exclude it, giving the required strict bound. This branch handles the wraparound gap to 0.
2. **No point is in bin `n-1`.** Then `b` maps `range n` into `range (n-1)`. Pigeonhole gives distinct indices with equal bins. Their representatives are distinct. Exchange indices if needed so `r(i)<r(j)`. Set `d=r(j)-r(i)` and `k=(j : ℤ)-(i : ℤ)`. Both indices lie in `[0,n)`, so `k≠0` and `k.natAbs<n`. The common quotient `q` gives `q*p≤n*r(i)` and `n*r(j)<p*(q+1)`; subtraction yields `n*d<p`. Casting the difference of the two representative equalities gives `(k : ZMod p)*z=d`.

`Nat.mul_div_le`, `Nat.lt_mul_div_succ`, `Nat.div_lt_iff_lt_mul`, `Int.natCast_natAbs`, and `Int.natAbs_natCast` are available in the successful probe. Expanding bounded natural subtractions into addition equations before `nlinarith` or `omega` is safer than asking automation to infer truncation bounds. For the signed-difference absolute-value bound, one can use `Int.natCast_natAbs` and two linear inequalities; an exact source lemma also exists in uncached `Mathlib.Data.Int.Lemmas` (see API audit), but is not required.

This plan does not assert that a dedicated cyclic-short-multiple theorem is already in mathlib. The new theorem G still needs a complete Lean proof.

### Narrowly inspected alternative

`Real.exists_int_int_abs_mul_sub_le` really exists at the pin with bound `1/(N+1)` and multiplier `0<k≤N`. Set `N=n-1` and `ξ=z.val/p`, clear positive denominators, and obtain the same signed error/strictness proof. This is a valid alternate API route, not a guessed theorem. Its `.olean` is not cached here, so it was source-inspected but not elaboration-probed. Prefer the finite-bins route to avoid real casts and a larger build. No need to pursue AddCircle topology or sorted-interval-gap libraries.

## 7. B: residue multiplicativity and only the needed square consequence

### Definitions and their domain boundary

`residueLambda p z` is lambda of the canonical natural representative. It is a function on all of `ZMod p`, but every character identity is explicitly restricted to nonzero residues. Its value at zero is not forced to 0, so do not package it as a monoid-with-zero homomorphism or a Dirichlet character. Nothing in the graph uses lambda at 0.

`GoodMultiplier` includes `a≠0` as well as the universal nonzero-input multiplication law. This makes the nonzero guard explicit and reusable in cancellation. It is not a claim that lambda is periodic.

- B1 follows from `ZMod.val_natCast_of_lt`; it may only be used for a natural argument strictly below p.
- B2 uses `ZMod.val_pos` and the baseline sign dichotomy.
- B3 uses `ZMod.neg_val`, `z≠0`, `z.val>0`, `z.val<p`, and the conditional full antireflection. Install `Fact p.Prime` to obtain `NeZero p` and field cancellation where needed.
- B4 uses lambda(1)=1 and p>1.
- B5 is the special case of the source's good-multiplier closure that is actually needed: good `a` implies good `-a`. Apply B3 at `a` and `a*z`, the latter nonzero by `ha.1` and `z≠0`. There is no need to export general product closure or a separate good-minus-one theorem.

### B6: least-bad reasoning as a strong-induction step

The statement assumes every positive natural `j<n` is a good multiplier and proves that `n` is good for `0<n<p`. These hypotheses are exactly the source's minimality information, not global character axioms. The case `n=1` is B4.

For `n≥2`, fix nonzero `z` and apply G. Since `0<k.natAbs<n`, the induction hypothesis makes the positive residue `k.natAbs` good. According to the sign of k, either it is k or its negative in `ZMod p`; B5 supplies goodness of k in the negative case. No negative integer is ever an input to lambda.

Write `F=residueLambda p`, `a=(n : ZMod p)`, and `c=(k : ZMod p)`. The strict bounds from G imply `0<d<p` and `0<n*d<p`. B1 plus ordinary `lambda_mul` gives

```text
F((n*d : ℕ) : ZMod p) = F(a)*F((d : ℕ) : ZMod p).
```

This is the only multiplication bridge needed before the full residue law is known, and both arguments have unreduced representatives below p. Do NOT assert `lambda t = F(t mod p)` for general t.

Goodness of c, applied to z and to `a*z`, gives

```text
F(d) = F(c)*F(z),
F(n*d) = F(c)*F(a*z).
```

The second identity uses equality inside the residue ring, `(n*d : ZMod p)=c*(a*z)`, obtained from G and commutativity/associativity. It does not use goodness of a. Since c is nonzero, B2 gives `F(c)≠0`; integer multiplication cancellation yields `F(a*z)=F(a)*F(z)`. This completes the exact universal quantifier required by `GoodMultiplier`.

### B7 and B8: finish without character classification

Use `Nat.strong_induction_on` with the property `0<n → n<p → GoodMultiplier p (n : ZMod p)` and B6. For any nonzero residue a, apply it to `a.val`, then rewrite its natural cast back to a. This yields B7.

For B8, `0<n<p` implies `(n : ZMod p)≠0`. Unpack `IsSquare (n : ZMod p)` as `n=x*x` (or use the probed `isSquare_iff_exists_sq`, whose equality is oriented `n=x^2`). The root x is nonzero. Apply B7 at x,x, then B2 to see its integer sign square is 1, and B1 to identify the value at n with lambda(n).

No counting of the positive fiber, counting of square roots, or identification with `legendreSym` is needed. This is exactly the first consequence used by NL §5 and §7. The B statements only assume prime p and full antireflection; oddness is not separately needed by their implementations. Allowing p=2 in those conditional statements does not weaken the final target or discharge any obligation: full antireflection at p=2 is incompatible with lambda(1)=1, and A6 is used only with p≥7.

## 8. C: prime divisor of the quarter is square, via audited reciprocity

This is the explicitly permitted replacement of the NL §6 floor-count proof, with the same conclusion and no stronger premise. It is shorter than formalizing Gauss's product and the double floor sum. Full details of theorem directions/guards and provenance are in `api-audit.md`.

For `p≥7`, `p%4=3`, let `t=(p+1)/4`. Establish first:

```text
4*t=p+1,  2≤t,  t<p.
```

For a prime r dividing t, `Nat.le_of_dvd` gives `r≤t<p`. Write `t=r*s`. Consequently `(p : ZMod r)=-1` and `p≠r`. Install `Fact p.Prime` and `Fact r.Prime` locally.

Three exhaustive cases prove C1:

1. `r=2`: the exact quotient relation gives `p+1=8*s`, hence `p%8=7`. Apply `ZMod.exists_sq_eq_two_iff` with `p≠2`.
2. `r≠2`, `r%4=1`: `-1` is square modulo r by `ZMod.exists_sq_eq_neg_one_iff`. Transfer `(p : ZMod r)=-1`, then use `ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_one` with its parameters swapped: library `(p:=r)`, `(q:=p)`. Its forward direction gives that r is square modulo p; the required second-prime-not-2 guard is our `p≥7`.
3. `r≠2`, `r%4=3`: `-1` is not square modulo r by the same neg-one criterion. Use `ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_three` with library `(p:=p)`, `(q:=r)` and `p≠r`. Its reverse direction takes the nonsquare assertion modulo r to the square assertion modulo p.

The odd r cases are exhaustive by `Nat.Prime.eq_two_or_odd` and `Nat.odd_mod_four_iff`, both probed. No sign claim about lambda is used anywhere in C.

For C2, `t≥2` supplies `t≠1`, so `Nat.exists_prime_and_dvd` gives r. Return its prime status, divisibility, `r≤t`, `r<p`, and C1. The division is natural division, but its exactness was proved from `p%4=3`; it is not assumed by notation.

The reciprocity `.olean` is currently absent. The source and exact statements are present at the approved pin and clean in Git. The implementation owner must arrange an explicitly authorized same-pin targeted build/cache acquisition before compiling the C module, then run the API and axiom checks. No build or dependency download outside B was attempted here. If this setup step cannot be authorized, C remains a setup/proof obligation; do not silently assume reciprocity or replace it with an axiom. The NL floor-count route is a genuine fallback but is not in the minimal graph.

## 9. D: source-to-target assembly without a second general proof

D1: argue by contradiction with exactly `hno : ¬ HasRepresentation (4*p)`. From `p≥7`, supply the `p≠2` and `p≠3` guards for A6. Obtain r from C2. Apply B8 with antireflection from A6, positivity from `hr.pos`, and `r<p` from C2. This gives `lambda r=1`, contradicting `lambda_prime hr = -1` in the integers. No witness restriction is added by this classical existence argument.

D2: use the reverse direction `.mpr` of the existing `multiple_four_iff_prime_three_mod_four_core`, supplying the uniform D1 proof for arbitrary p and its three guards, then specialize to m and hm. This includes m=1 and the excluded small primes through the already present reduction. The final statement is not a conditional theorem mentioning antireflection, a good-multiplier hypothesis, a residue-prime existence hypothesis, or a numerical bound on m.

The final two proof bodies belong to the integrator only after the approved helper proofs and the exact reduction artifact are available. There is no proof body for either in this blueprint.

## 10. Proposed project modules and nonoverlap ownership

These are future locations, not write permissions exercised by this assignment. I created nothing under `P/lean`.

| Future owner | Exclusive paths | Contents / imports |
|---|---|---|
| Proof worker 1 (current `flgenerator`) | `P/lean/Statement/FourWork/Descent/Ternary.lean` | A1–A6; imports `Statement.Partial` and needed narrow tactics |
| Same worker | `P/lean/Statement/FourWork/Descent/Cyclic.lean` | G; imports `Mathlib.Data.ZMod.Basic`, `Mathlib.Data.Finset.Card`, needed arithmetic tactics; no Character import |
| Proof worker 2 | `P/lean/Statement/FourWork/Character/ResidueValue.lean` | Exactly the two new definitions and B1–B5; imports `Statement.Partial`, `Mathlib.Data.ZMod.Basic` |
| Same worker | `P/lean/Statement/FourWork/Character/ResiduePrime.lean` | C1–C2; imports `Mathlib.NumberTheory.LegendreSymbol.QuadraticReciprocity`; no A or G import |
| Same worker | `P/lean/Statement/FourWork/Character/Rigidity.lean` | B6–B8; imports ResidueValue and the completed Descent.Cyclic module |
| Integrator, after proof phase | `P/lean/Statement/FourWork/Reduction.lean` | Mechanical importable copy of the fixed 19-helper candidate, with its declarations unchanged and reviewed identity tracked |
| Integrator, after proof phase | `P/lean/Statement/FourWork/Assembly.lean` | D1–D2; imports Reduction, Descent.Ternary, Character.Rigidity, Character.ResiduePrime |

Keep the `ArithmeticStatement.FourWork` namespace for internal declarations regardless of which directory contains the module. The two representation endpoints remain directly in `ArithmeticStatement`. No shared header is edited concurrently: worker 2 alone owns ResidueValue and its definitions. G contains no reference to those definitions, so there is no import cycle.

Do not import the root `Statement` from these modules: use `Statement.Partial` to avoid dragging the full-target scaffold into proof artifacts. A source under W is not automatically an importable `Statement.*` module. That is why both proof workers should receive scratch subdirectories of `P/lean/Statement/FourWork` from the leader.

From `P/lean`, targeted commands such as `lake build Statement.FourWork.Descent.Cyclic` and `lake build Statement.FourWork.Character.Rigidity` build modules without touching `Statement.lean`. `lake env lean path/to/Module.lean` alone does not build missing imported scratch modules; build their `.olean`s first. Do not modify the root import list until integration review. Build outputs are compiler-generated, not permission for cross-editing another worker's source.

### Two persistent slots, not a third worker

Use the current proof-generator slot for the Descent directory. During the parallel proof phase, the leader should recycle/re-dispatch the idle integrator slot as a second **proof-generator** role for the Character directory; do not assign a substantial new proof to a still-restricted integration-only role. Restore/dispatch the integrator role serially after both proof packages pass their gates, keeping at most two persistent workers throughout.

Worker 1 can prioritize G first to unblock B6, then A. Worker 2 first does C and the independent B1–B5, then B6–B8 once G is compiled. A need not be finished for worker 2 to prove B, because the latter has the legitimate conditional antireflection interface. This is a real dependency split, not two workers attempting the same theorem with overlapping files.

## 11. Acceptance and principal failure risks

1. **Highest proof-search risk: G.** Preserve the coefficient and product strictness, nonzero coefficient, wraparound branch, and distinct-index-to-distinct-residue argument. The successful finite pigeonhole API is real; G itself is still unproved.
2. **A arithmetic risk:** exact thirds must precede all division/order claims; handle both residue classes modulo 3 and the swapped pair. A descent on the wrong parameter is invalid.
3. **B circularity risk:** do not reduce lambda of arbitrary large products modulo p. Only B1 at `n`, `d`, `n*d<p` justifies the unreduced multiplicativity bridge. k is an integer residue coefficient, never a lambda argument.
4. **Sign/nonzero risk:** cancel an integer F-value only after deriving it is ±1 on a nonzero residue. `GoodMultiplier` and B7 deliberately exclude zero.
5. **C guard risk:** r=2 needs the supplementary law, not odd-prime reciprocity; the mod-1 theorem is used with parameters swapped; the mod-3 theorem requires distinct primes. The quarter exactness supplies p=-1 modulo r.
6. **Library/setup risk:** reciprocity and Dirichlet source exist, but neither `.olean` is cached. Only the neg-one criterion and finite-cardinality API were actually probed. Do not report unrun library axiom checks as passing.
7. **Integration risk:** the 19-helper snapshot is not yet in the master; importing or pretending it is in `Statement.Partial` would fail or change the evidence boundary.
8. **Review risk:** code-only headers are not checked proofs, and successful `#check` does not establish them. Each implemented helper and final endpoint needs fresh fidelity/readback coverage of the actual signatures/definitions, pinned compilation, absence of admissions, and `#print axioms` without `sorryAx` or unsupported added axioms.

No missing mathematical premise in the accepted NL route was identified. The remaining obligations are implementation of A/G/B/C, the C setup step, and checked integration. They are not discharged by this plan or its type-probe logs.
