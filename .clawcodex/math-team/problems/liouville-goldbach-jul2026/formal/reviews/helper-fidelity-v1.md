# Helper-interface fidelity review v1

Mode: CERTIFICATION — source/statement fidelity only, not proof acceptance.

VERDICT: APPROVE

**Protection decision:** YES for the exact eight helper definitions and 42 helper signatures at `interfaces-v1.lean:11–189`, with the unchanged protected base definitions. The two endpoint signatures at lines 191–195 may likewise be frozen **as OPEN goals only**. They are not accepted theorems, available assumptions, or importable declarations. Required semantic changes before proving these interfaces: **none**.

This decision covers the meanings of this proof-erased snapshot, not elaboration, a proof, an integrated build, or the truth of the conjecture. No declaration was proved, repaired, or edited. Only this assigned report was written. No prior fidelity verdict, task board, author-confidence report, or other review conversation was consulted; the supplied literal readback was used as an input, not as authority for source correspondence.

## 1. Exact inputs and identity

Paths below use:

- `P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`
- `B = .clawcodex/math-team/review-inputs/r20260924-v1`
- `M = P/lean/.lake/packages/mathlib`
- `T = ~/.elan/toolchains/leanprover--lean4---v4.32.2/src/lean`

SHA-256 hashes were computed from the files, not copied from the dispatch. Both supplied candidate hashes match.

| Input | SHA-256 |
|---|---|
| `P/request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `P/nl/sketcher/formal-handoff-v1.md` | `25ce7919c925c8a3d8ae3a6296a65aa92e93fec3fcdd18a4df41675fa0dbdfb7` |
| `P/nl/explorer/attempt-v1.md` | `5143a167b3ac0e26116b33e934a3e33fff2bc6c44b5a7608e01c7f73d4cf94a2` |
| `P/formal/blueprinter/interfaces-v1.lean` | `89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc` |
| `P/formal/approved-v1/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `B/interfaces-readback.md` | `88a3bb1152043c2eb245914cbec5a569cbf81ab47e4031f1330e1ba27d139e9e` |
| `B/Interfaces.lean` | `89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc` |
| `B/Declaration.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `B/Dependencies.lean` | `55b5480511d2a2cb749cebafa9b8da29f744090a269bd0ece94df1b37ab0d07c` |
| `B/ListOperations.lean` | `925cbf08a1aac0870075ad56ff2d95c7b0eb94c87853ace32d0043a9c094e2bc` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `P/lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `P/lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |

`cmp` also returned success for the candidate versus `B/Interfaces.lean`, and for the protected definitions versus the active `Statement/Definitions.lean`. Thus the supplied literal readback concerns the same interface and base-definition bytes. Its literal quantifiers and domain account agree with my inspection; no discrepancy affecting this review was found.

Protocol inputs, under `.clawcodex/skills/math-team/references/`:

- `protocol.md`: `e712830b3febe6e3fcaf0479c7aa9fc30f23aa4fcc5e1f45088f736f9c161f2b`
- `lean.md`: `69bcc256c8c33d77efd973da509c147260be5d2b153f4cd5015b0e6859aaab72`

The full interface-file hash, together with the line locators below and the defining-dependency hashes, identifies every reviewed declaration type. No separate proof-body snapshot exists in this packet.

## 2. Authoritative source locators

Abbreviations used in the audit tables:

- **Q**: `P/request.md`. Lines 7–14 prescribe multiplicity, the even-integer target, positivity, and permission for equal summands. Lines 51–57 reiterate the nonvacuity/sign checks. Lines 76–85 prescribe the exact identity, actual ordered-pair count, inclusive partial sum, correlation range, and signed arithmetic. Lines 125–127 disallow partial/averaged results being reported as full success.
- **H**: `P/nl/sketcher/formal-handoff-v1.md`. Lines 9–25 give the integer target and natural-index normalization; lines 31–45 give interval/count conventions; lines 54–81 list proposed interfaces; line 83 fixes the unrestricted positive-witness meaning of G; lines 91–98 identify the OPEN pointwise goal. This is a source-intention specification, not accepted proof evidence.
- **E**: `P/nl/explorer/attempt-v1.md`. Lines 15–29 define signed representations and propose multiplicativity/scaling. Lines 35–49 give sign-adaptive seeds, including the seed 8 and odd seeds. Lines 76–90 propose the exact prime-product equivalence and repeated-prime factor extraction. This is likewise candidate mathematics, not accepted proof evidence.
- **I**: `P/formal/blueprinter/interfaces-v1.lean`.
- **D**: `P/formal/approved-v1/Definitions.lean`.

## 3. Base definitions and hidden assumptions

`D:6–14` is preserved exactly. `omega` is the length of a prime-factor **list**, not a prime-factor finset. The pinned `M/Mathlib/Data/Nat/Factors.lean:37–50` recursively removes one factor occurrence and sets the lists at 0 and 1 to empty. Its prime-power statement at lines 181–187 uses `List.replicate`; the product and prime-membership statements are at lines 55–81. `T/Init/Prelude.lean:3027–3029` counts every list entry. Thus the encoded Ω counts multiplicity, Ω(1)=0, and λ(1)=1. The integer base and codomain in `D:8` represent −1 correctly. The totalization Ω(0)=0, λ(0)=1 is visible and is not used to admit zero summands.

`Even` comes from the additive translation at `M/Mathlib/Algebra/Group/Even.lean:53–60`: on naturals it means `∃ r : ℕ, N = r + r`. `Nat.Prime` is `Irreducible` on the natural-number monoid (`Data/Nat/Prime/Defs.lean:38–43`); its standard characterization at lines 107–112 excludes 0 and 1. The actual irreducibility/unit definitions were inspected, not inferred from the name.

All helper number types are concrete `ℕ` and `ℤ`, with ordinary addition, order, multiplication, casts and power. In particular, `T/Init/Data/Int/Basic.lean:63` casts naturals using `Int.ofNat`, and lines 400–402 define integer powers. Finite sums use the integer additive structure, not arithmetic modulo 2 or natural subtraction.

The relevant interval instance is the concrete natural `LocallyFiniteOrder` at `Order/Interval/Finset/Nat.lean:33–41`; the interval membership laws are at `Order/Interval/Finset/Defs.lean:278–306`. Finset filtering/images use decidability of concrete number equalities and predicates; this does not add an arithmetic hypothesis. `Set.BijOn` really requires mapping into, injectivity on, and surjectivity onto the specified sets (`Data/Set/Operations.lean:282–309`). Finset-to-set coercion preserves membership (`Data/Finset/Defs.lean:100–127`). There is no variable typeclass, hidden `Fact Target`, abstract possibly empty number domain, or section parameter in the candidate.

The protected natural-number target is the faithful positive-integer normalization: every integer N>2 and every positive integer summand is in the image of ℕ, with the same sum and evenness conditions. This is a semantic domain comparison, **not** a supplied Lean integer/natural coercion theorem. `H:53`'s optional `integer_nat_target_equiv` is not among these interfaces and is not certified as proved here.

## 4. Every local helper definition

Write `H_s(N)` for `HasSignedRepresentation s N` and `G(N)` for `HasRepresentation N` in this report only.

| Definition / locator | Literal meaning and source comparison |
|---|---|
| `HasSignedRepresentation`, I:11–14 | For the given `s : ℤ` and `N : ℕ`, `∃ a b : ℕ, 0<a ∧ 0<b ∧ N=a+b ∧ λ(a)=s ∧ λ(b)=s`. Witnesses depend on s,N. Matches E:15–19; no parity, primality, coprimality, ordering or distinctness of witnesses. |
| `HasRepresentation`, I:16–17 | Exactly `H_{−1}(N)`. No evenness or size restriction is baked into this conclusion predicate; outer target quantifiers supply those. Matches H:83 and Q:10–14. |
| `I`, I:19–20 | `Finset.Ico 1 N`: precisely `1≤a<N`, equivalently `0<a<N`. Agrees with H:33,39. |
| `representationIndices`, I:22–24 | Filters all of I(N) for both negative signs at a and N−a. The latter is natural subtraction; interval membership ensures the intended positive complement. This is an auxiliary index set, not the definition of R. |
| `orderedRepresentations`, I:26–29 | Filters the full Cartesian product I(N)×I(N) by N=a+b and both negative signs. The two upper bounds follow from positivity and the sum equation, so no source representation is lost. `Finset.product`, not `offDiag`, a quotient, or an a≤b restriction, is used. |
| `R`, I:31–32 | Cardinality of that actual ordered-pair finset in ℕ. Distinct (a,b) and (b,a) count separately; a diagonal pair counts once. R is **not** defined by the identity, positivity, or an unordered count. Matches Q:81. |
| `L`, I:34–35 | Integer sum over `Finset.Icc 1 x`, including x and excluding 0. Exactly Q:82; not the half-open prefix ending at x−1. |
| `C`, I:37–38 | Integer sum of λ(a)λ(N−a) over all 1≤a<N, including the midpoint when it exists. Exactly Q:83. |

The choice to define R by ordered pairs, rather than H:36's optional index implementation, follows Q's authoritative count definition. I:144–160 separately states the required bridges to the index/indicator implementation; the identity is not true by a circular definition of R.

## 5. Every helper signature

All names below are in `ArithmeticStatement`. Variables are natural except s, which is integer. Implicit braces are universal binders, not existential choices. Premises have the displayed source-code order; every `G(K)` or `H_s(K)` conclusion introduces its own `∃ a` then `∃ b` after the outer parameters and premises. The table reviews types only; **none of its rows certifies a proof**.

| Signature / I lines | Quantifiers, hypotheses and conclusion checked | Source |
|---|---|---|
| `omega_one`, 40–41; `lambda_one`, 43–44 | Closed equalities Ω(1)=0 and λ(1)=1. | Q:7; H:25,55; E:25 |
| `lambda_sign`, 46–47 | ∀n, 0<n → (λ(n)=1 ∨ λ(n)=−1). No choice of a sign uniform in n. | H:54 |
| `omega_mul`, 49–50 | ∀u v, 0<u → 0<v → Ω(uv)=Ω(u)+Ω(v). No coprimality assumption. | H:69; E:21–27 |
| `lambda_mul`, 52–53 | Same positive-input guards, with λ(uv)=λ(u)λ(v) in ℤ. | H:70; E:23–25 |
| `lambda_prime`, 55–56 | ∀p, Nat.Prime p → λ(p)=−1. Primality is confined to this helper, not imposed on target summands. | E:25 |
| `lambda_two`, 58–59; `lambda_three`, 61–62; `lambda_four`, 64–65; `lambda_five`, 67–68 | Closed values −1, −1, +1, −1 respectively, all in ℤ. | H:72,76; E:25,43,49 |
| `lambda_two_mul`, 70–71 | ∀m, 0<m → λ(2m)=−λ(m). | E:25 |
| `lambda_square`, 73–74 | ∀t, 0<t → λ(t²)=1. Exponent 2 is natural. | H:71; E:25 |
| `target_iff_forall_hasRepresentation`, 76–77 | Target ↔ ∀N, Even N → 2<N → G(N). Both directions, exactly the same witness conclusion. | Q:10–14; H:19–23,83 |
| `hasSignedRepresentation_mul`, 79–81 | ∀s N d, 0<d → H_s(N) → H_{λ(d)s}(dN). s is any integer; H_s(N) already forces a valid sign when inhabited. | E:17,29 |
| `representation_scaled_sign`, 83–88 | ∀u v m s, positivity of u,v,m → (s=1 ∨ s=−1) → λ(u)=s → λ(v)=s → λ(m)=−s → G(m(u+v)). Integer negation and multiplication. | H:74 |
| `representation_double`, 90–92 | ∀m, 0<m → λ(m)=−1 → G(2m). The sign premise rules out m=1. | E:82–84 |
| `representation_diagonal`, 94–96 | ∀N, Even N → 2<N → λ(N)=1 → G(N). The positive sign is on N, not mistakenly on N/2. | H:73 |
| `representation_two_sign_seed`, 98–102 | ∀d, H_{−1}(d) → H_1(d) → ∀m, 0<m → G(dm). Two independent seed witnesses are chosen before the multiplier; final witnesses may vary with m. | H:75; E:35–49 |
| `eight_two_sign_seed`, 104–106 | H_{−1}(8) ∧ H_1(8); distinct existential scopes, not one pair required to have opposite signs. | E:43,49; H:76 |
| `representation_multiple_eight`, 108–109 | ∀m, 0<m → G(8m). Only this infinite subfamily, not Target. | H:76; Q:125 |
| `mem_I_iff`, 111–112 | ∀N a, a∈I(N) ↔ 0<a ∧ a<N, including small/empty cases. | H:33,39 |
| `interval_eq_Icc`, 114–115 | ∀N, 2≤N → I(N)=Icc 1 (N−1). N−1 here is a guarded natural index. | H:39 |
| `interval_bounds`, 117–118 | ∀N a, 2≤N → a∈I(N) → 0<a ∧ a<N ∧ 0<N−a ∧ N−a<N. | H:56 |
| `interval_card_cast`, 120–121 | ∀N, 2≤N → (card I(N):ℤ)=(N:ℤ)−1. Subtraction on the RHS is signed. | H:57 |
| `reflection_mem`, 123–124 | ∀N a, 2≤N → a∈I(N) → N−a∈I(N). | H:39,58 |
| `reflection_involutive`, 126–128 | Same binder/guard order, concluding N−(N−a)=a in ℕ. Not an unguarded natural-subtraction identity. | H:58 |
| `reflection_bijection`, 130–131 | ∀N, 2≤N → BijOn (a↦N−a) I(N) I(N), as sets. Injectivity and surjectivity are restricted to the interval. | H:58 |
| `sum_lambda_interval`, 133–134 | ∀N, 2≤N → Σ_{a∈I(N)}λ(a)=L(N−1). | H:35,39 |
| `sum_lambda_reflection`, 136–137 | Same guard, concluding Σ_{a∈I(N)}λ(N−a)=L(N−1). No claim about reflection outside the interval. | H:59 |
| `mem_orderedRepresentations`, 139–142 | ∀N a b, pair membership iff precisely positive a,b, N=a+b, both signs −1. No N≥2 premise is needed: the RHS already forces it. | Q:81; H:60 |
| `orderedRepresentations_eq_image`, 144–146 | ∀N, 2≤N → ordered pairs equal the image of representationIndices under a↦(a,N−a). The first coordinate retains the index; no unordered identification. | H:60 |
| `representation_count_eq_card_indices`, 148–149 | ∀N, 2≤N → R(N)=card representationIndices(N), natural counts. | H:36,60 |
| `two_sign_indicator`, 151–154 | ∀a b, 0<a → 0<b → 4·1_{λ(a)=λ(b)=−1}=(1−λ(a))(1−λ(b)), entirely in ℤ. | H:61 |
| `representation_count_eq_indicator_sum`, 156–160 | ∀N, 2≤N → (R(N):ℤ)=Σ_{a∈I(N)}1_{λ(a)=λ(N−a)=−1}, with integer 1/0. | H:62 |
| `four_mul_representation_count`, 162–163 | ∀N, 2≤N → 4(R(N):ℤ)=((N:ℤ)−1)−2L(N−1)+C(N). No evenness restriction and no natural-valued RHS or division. | Q:78–85; H:41–45,63 |
| `representation_count_pos_iff`, 165–166 | ∀N, 2≤N → (0<R(N) ↔ G(N)); natural positivity, both directions. | H:64 |
| `count_pos_iff_keystone`, 168–169 | ∀N, 2≤N → (0<R(N) ↔ 2L(N−1)−((N:ℤ)−1)<C(N)). Strict inequality in ℤ, correct direction. | H:65 |
| `keystone_ge_four_iff`, 171–172 | Same guard, with 0<R(N) ↔ 4≤((N:ℤ)−1)−2L(N−1)+C(N). Four bounds the expression 4R, not R. | H:66 |
| `target_iff_count_pos`, 174–175 | Target ↔ ∀N, Even N → 2<N → 0<R(N). No missing small even case or exceptional set. | Q:85; H:64,81 |
| `target_iff_pointwise_keystone`, 177–179 | Target ↔ ∀N, Even N → 2<N → the same strict keystone inequality. A closed equivalence, not an assumption granting the RHS. | H:65,67,93–96 |
| `exists_prime_pair_factor_of_lambda_one`, 181–185 | ∀m, 1<m → λ(m)=1 → ∃p q d, Prime p ∧ Prime q ∧ 0<d ∧ λ(d)=1 ∧ m=d(pq). Witness order p,q,d is inside the m hypotheses. Repeated primes and d=1 are allowed. | E:82–86 |
| `target_iff_prime_product_core`, 187–189 | Target ↔ ∀p q, Prime p → Prime q → G((2p)q). Both directions, all primes including 2 and p=q; witnesses depend on both primes. No primality of summands. | E:76–90 |

The remaining two signatures are separately scoped:

| OPEN signature / I lines | Fidelity decision |
|---|---|
| `pointwise_keystone`, 191–192 | APPROVE **as an OPEN goal**: ∀N, Even N → 2<N → 2L(N−1)−((N:ℤ)−1)<C(N). Exact H:67,91–96; no assumed keystone premise, averaging, density statement or threshold. |
| `liouville_goldbach`, 194–195 | APPROVE **as an OPEN goal**: the closed proposition Target, exactly D:10–14 and the protected positive-integer normalization of Q:10–14. No residual/core/keystone hypothesis on the final assertion. |

## 6. Critical edge cases, scope differences and mismatch findings

**Material mismatches: none.** The following distinctions delimit the approval rather than authorizing stronger claims.

1. **Zero and empty cases.** I(0)=I(1)=∅, so their index/pair sets are empty and R=C=0; L(0)=0. Inhabited representations require positive summands. Consequently λ(0)=1 cannot manufacture a representation. The signed scalar `(N:ℤ)−1` would be −1 at N=0; that case is deliberately excluded from the identity by N≥2. N=2 is included in the identity but not in any universal positivity conclusion: its only positive split is 1+1 and R(2)=0. The target begins at N=4 and is not vacuous.
2. **Multiplicity and the diagonal.** The definitions permit the example N=4, a=b=2; the ordered count contains the diagonal once. No off-diagonal filter, a<b bound, division by two, or distinct-prime assumption is hidden anywhere. In prime-factor extraction the case m=4 requires the permitted p=q=2, d=1; dropping either permission would change the interface materially.
3. **Reflection guards.** Every term in the correlation and indicator sums is indexed by 0<a<N, so N−a is positive and exact natural subtraction. The interval/reflection assertions retain their membership guards; they do not invoke a sign at zero to avoid proving a complement positive. N−1 in L is a natural index guarded by N≥2, while the scalar N−1 in the identity/inequalities is explicitly integer subtraction.
4. **Quantifiers and seeds are nonvacuous.** Arbitrary s outside {±1} makes H_s(N) impossible, so that portion of the general scaling implication is intentionally vacuous; the −1 target is not. Two-sign seed premises contain independent existential pairs, not an inconsistent simultaneous sign demand on one pair. The source's seed 8 supplies distinct negative/positive pairs (E:43,49). Factor extraction excludes m=1, whose empty factor list could not supply two primes.
5. **General seed scope is intentional.** I:98–102 omits H:75's explicit even d>2 restriction. This is the more general signed-scaling interface in E:35–49, which explicitly includes odd seeds 5 and 7. The representation premises enforce a positive seed size. This broader conditional helper must not be described as a proof covering all even targets; the only unconditional family signature here is multiples of 8.
6. **Existence versus named constructions.** `representation_double`, `representation_diagonal`, the scaling lemmas and the seed-8 lemmas conclude only G or H. Their types do not assert that the chosen output witnesses equal m,m; N/2,N/2; or the displayed scaled seed pairs. H's construction descriptions can guide proof work, but this approval is only for the existential interfaces actually written. If a downstream user needs a prescribed-witness theorem, a separate strengthened interface needs fresh review. No such strengthening is required for the present existence-only uses.
7. **Image versus an equivalence object.** H:60's correspondence is rendered as exact finset image equality plus cardinal equality, not as a Lean `Equiv` value. The map retains a as first coordinate and hence does not collapse distinct indices. These interfaces preserve the required ordered count, but do not expose a reusable equivalence structure as data.
8. **Aggregate versus pointwise.** L, C and R aggregate over summands of one fixed N. The keystone goal and target equivalences nevertheless quantify over each individual admissible N. No average-in-N bound is substituted, no asymptotic constant is chosen, and no unspecified cutoff occurs. The fixed coefficient/threshold 4 agrees with the source indicator/count identity; it is not an unjustified analytic bound or a requirement for four representations.
9. **Not the entire handoff.** No `count_ge_neg_partial_sum`, other seed-multiple family, residual theorem, square/power family, or integer/natural Lean bridge appears in this snapshot. Their absence is not a defect in the selected interfaces, but none is approved or proved by this report. The prime-product equivalence itself remains an unproved helper signature; in particular the prime-product family has not been established.

## 7. Local source cutoff and environment checks

Only the pinned local library/source files and existing factual provenance records were used. No web source, new package, newer revision, or external analytic theorem was fetched or imported. The cutoff is Q:16–27, inclusive through 2026-07-31.

`P/lean/lakefile.toml:8–11` pins Mathlib to `905b95818eb32af7874a58b427f50c1711a5e96c`; the manifest fixes all package revisions. Although the upstream Mathlib lakefile names branches for several dependencies, this review used the manifest checkouts, not those branches' current tips. Local `git show`/`git status` checks found each package HEAD equal to its manifest pin, with no tracked modifications. Relevant Mathlib source comparisons against HEAD also returned success.

The following exact-SHA public-availability witnesses were checked against the cached raw GitHub run records `P/formal/environment/public-ci-<name>.stdout`. These are provenance metadata, not mathematical proof evidence. The timestamps below are all before the cutoff; whether a particular CI run succeeded is irrelevant to public availability.

| Package | Exact commit | Public witness UTC / GitHub run ID |
|---|---|---|
| Mathlib | `905b95818eb32af7874a58b427f50c1711a5e96c` | 2026-07-28 16:36:37 / `30379053106` |
| Lean | `f3b06c705e6c85f5314019d5d3baab0fec5b580c` | 2026-07-28 14:27:52 / `30368480005` |
| plausible | `e12c1910fe855cbfc38803cd4e55543906d5fa62` | 2026-07-13 13:20:50 / `29253419718` |
| LeanSearchClient | `c5d5b8fe6e5158def25cd28eb94e4141ad97c843` | 2026-02-12 00:28:07 / `21928619159` |
| importGraph | `7e9612bf0b9ee66db3cb5b9988a35afc706f5a12` | 2026-07-13 13:50:43 / `29255410348` |
| proofwidgets | `6e311e2a844da9b2cc3971187df2fe0066947b93` | 2026-07-13 13:20:54 / `29253424000` |
| aesop | `a7dbf0c63b694e47f425f3dcddbc0e178bb432d3` | 2026-07-13 14:03:38 / `29256329889` |
| Qq | `38d591e778f100aec9762bb582f9c7f55f50e9dc` | 2026-07-13 13:20:57 / `29253426904` |
| batteries | `023ce7d62a0531e22a5331e20b587817a80d49ff` | 2026-07-13 20:29:43 / `29282598413` |
| Cli | `88679d088c9720c27ebdf2ba4dafe17341747f94` | 2026-07-13 13:20:47 / `29253416514` |

Full witness URLs and exact `head_sha` fields are preserved in `P/formal/environment/public-availability-witnesses.json` (Mathlib lines 3–73, Lean 76–91, dependencies 94–1401) and agree with the raw records. Cached release records give Lean v4.32.2 publication at `2026-07-28T16:34:35Z` and Mathlib v4.32.2 at `2026-07-28T16:47:51Z`:

- `https://github.com/leanprover/lean4/releases/tag/v4.32.2`
- `https://github.com/leanprover-community/mathlib4/releases/tag/v4.32.2`

The installed binary reported `Lean 4.32.2`, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`; Lake reported `5.0.0-src+f3b06c7 (Lean version 4.32.2)`. The inspected installed core source files also match the cached corresponding pinned raw source bytes. These checks establish the locally inspected versions and their recorded pre-cutoff availability; they are not an independent reconstruction of compiler binaries or a proof-dependency/axiom audit.

Commands were limited to reading, hashing/comparison, local Git identity/status checks, JSON provenance cross-checks, and installed `lean --version`, `lean --print-prefix`, `lake --version`, `elan toolchain list`. No build or elaboration of the intentionally non-importable signature file was attempted. No compilation success is claimed or used as fidelity evidence.

Additional provenance/input SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `P/formal/environment/public-availability-witnesses.json` | `051de67ee5bfd81242942075cf9dabacd8cfa96b74abf3733b025456694cc4c1` |
| `P/formal/environment/lean-release.stdout` | `8c58bfbff7a6fca95e743e7de64de75561d605accd9d31e1179b9e3f17c6cbe2` |
| `P/formal/environment/mathlib-release.stdout` | `c301e835f278ccfd3a89aaea81d9a549923c846b819832a332845abcb61ab6ef` |
| `M/lakefile.lean` | `e3e8ac4d3ea441b062dbd29a2910165e55d8463c8bd9a3feb830cf6fb64a1b7a` |

The ten raw CI records have evidence-set SHA-256 `018b6e1f68d1e8879de4a0610a40de8ad6f60a90c7cf68fd299d7721d2952878`: hash the concatenation of records `filename<TAB>sha256(file bytes)<LF>`, sorted by filename, for the ten `public-ci-<name>.stdout` files listed above (with filename `public-ci-mathlib.stdout` for Mathlib and `public-ci-lean.stdout` for Lean).

### Inspected defining-library file hashes

Mathlib paths are relative to M; core paths are relative to T. These hashes bind the actual definition sources inspected by Read/Grep, in addition to the repository/toolchain pins.

| File | SHA-256 |
|---|---|
| `Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `Mathlib/Data/Nat/Prime/Defs.lean` | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `Mathlib/Algebra/Group/Even.lean` | `1180fa9ac282e55257e95c8402acd7314fcbd0a18bcfdede92a3cde16e1db630` |
| `Mathlib/Algebra/Group/Irreducible/Defs.lean` | `77937179ccfec6ca8acdd4b660525a7f313d4fb0b9c6dc4296d1301fb9e1e731` |
| `Mathlib/Algebra/Group/Units/Defs.lean` | `09489226154d6558ad44614501b55883f0dc31b4504f1bb29e6190b2df456bce` |
| `Mathlib/Order/Interval/Finset/Defs.lean` | `5a40d40b2569bea01fcf259d1644068fe565163c8dfea2e480a15293912eff3c` |
| `Mathlib/Order/Interval/Finset/Nat.lean` | `e1a7b1cf7d86209af1d6f894e05f2a4cc40997840ff64461d98476fcd5e248e2` |
| `Mathlib/Data/Finset/Defs.lean` | `16e20640a595641c7aa07dcc04ccb880bbe0aba3fba473c84e6106b190637551` |
| `Mathlib/Data/Finset/Prod.lean` | `b1914aee3fc42f07fd860a162e47485a5e146fa1bd5027c0f5f4cea95e0cef1c` |
| `Mathlib/Data/Finset/Filter.lean` | `c777e9b830557d7b4f903a0fa81c27bec2d89f546dd4ae146122f4bb4882a06d` |
| `Mathlib/Data/Finset/Card.lean` | `87c674ba5464c7868fb3e253e58a695821bf8841bb4e076bac5d570236dc6229` |
| `Mathlib/Data/Finset/Image.lean` | `fbb8c87acb75dd13ef3de01d27d29c2ab1fd989ccf26916f829d2b049ce1ef02` |
| `Mathlib/Data/Set/Operations.lean` | `62f30a8f571aae1d9de46b14b90ded8bc9facec98f01ab697d783ddd16ee8db1` |
| `Mathlib/Data/Set/Function.lean` | `24ce35b55301b88c5d46794570cd02e143de24c84c3e652411e6f5baadaa0a21` |
| `Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean` | `562dacf916c63c599b7c4becbf3bafdbb7fa0b493eb2f6e594f4126a6d91e62c` |
| `Init/Prelude.lean` | `44f86ebbb9ab743a05c6ebe2c674aadbf2c822bee874f1b16d7e6c8d56318dc9` |
| `Init/Data/List/Basic.lean` | `c6b61f1b5fcac4ea4339625f2e66916d1f2c1ae2531c10ee45b401846ffb6061` |
| `Init/Data/Int/Basic.lean` | `e3a3b503e2f89a7dc5dfbfdf610c5b9927ddc0c61809bbb8110053b7982021e5` |

## 8. Handoff and remaining gates

The leader may protect these exact **statement meanings** and route helper proof work without changing the base definitions. All 42 helper proofs still require their own evidence; this review does not promote any signature to an accepted dependency. In particular, the counting identity/bridges and both directions of the prime-product reduction are obligations, not granted facts. The pointwise keystone and final target remain OPEN.

For later acceptance, the assigned proof worker/integrator must supply actual declarations with these exact types, compile in the pinned environment, inspect transitive axioms/admitted obligations, and obtain the required independent mathematical/proof checks. Do not introduce either OPEN endpoint as a custom axiom, an unnoticed premise, or an assumed helper. Any semantic change to a signature or defining dependency invalidates the affected fidelity/readback protection and requires fresh review.

**Final scoped result: APPROVE for interface fidelity and protection for proof work; no semantic changes requested; no proof or full-conjecture acceptance.**
