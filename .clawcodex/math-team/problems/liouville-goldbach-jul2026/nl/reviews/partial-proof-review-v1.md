Mode: CERTIFICATION — fresh independent natural-language review of partial arguments.

# Partial proof review v1

## 1. Verdict and exact scope

**PASS for the statements actually proved in the candidate, including its equivalences and conditional assembly implications only.** No load-bearing mathematical gap was found in those partial proofs.

**UNRESOLVED for the original Target.** Core, K01, PB, and LS have not been proved. Neither an equivalence nor a sufficient condition establishes its open premise.

**FAIL / FALSE for the proposed optional assertion O-M5:** `forall prime q>=5, L(q-1)<0`. The prime q=5 satisfies every hypothesis but has L(4)=0. This assertion is explicitly unproved in the candidate and is not used by any accepted partial proof. Its falsity therefore does not invalidate those proofs, but the ledger must not continue to present this exact assertion as a viable proof obligation. Details appear in §6.

This is not a blanket certification of the conjectural ledger entries, a full proof of the request, or a Lean compiler/kernel certificate. The scope assigned here is the supplied partial proofs and their assembly implications, not production of the missing global theorem.

Root R: `.`.

Problem root P: `.clawcodex/math-team/problems/liouville-goldbach-jul2026`.

Mathlib root M: `P/lean/.lake/packages/mathlib`.

Owned report: `P/nl/reviews/partial-proof-review-v1.md`.

## 2. Snapshot identity and inputs read

SHA-256 values below were computed from local bytes, not copied as evidence from the candidate. Both dispatched candidate hashes match exactly.

| Input path, relative to P unless stated otherwise | SHA-256 |
|---|---|
| `request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `nl/generator/proof-v1.md` | `eb6974f5493f7b77773ba5e685240e8d608f43e6fb2a1156d627d7a0dbca86f5` |
| `nl/generator/obligation-ledger-v1.md` | `69c2efa85c08e5d14437cb66f663784bc59d89fc61dce81dc7c91f10a9f7b48b` |
| `formal/approved-v1/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `lean/.lake/packages/mathlib/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `lean/.lake/packages/mathlib/Mathlib/Data/Nat/Prime/Defs.lean` | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `lean/.lake/packages/mathlib/Mathlib/Algebra/Group/Even.lean` | `1180fa9ac282e55257e95c8402acd7314fcbd0a18bcfdede92a3cde16e1db630` |
| `formal/environment/environment-report.txt` | `05e10971b80acab2a04139ec6a0647e5f8fbd4a09bb516b1db205b084adac71a` |
| `formal/environment/public-ci-mathlib.stdout` | `4337fdc10284dc0c90165a0e4926fde19ebb6ce78dfef2505a3112a277452e00` |
| `formal/environment/public-ci-mathlib.json` | `bc12929af93d0eafc008d4d56e287842ef6f682d797b6bb50e7f1481d6f0eeba` |
| `formal/environment/mathlib-release.stdout` | `c301e835f278ccfd3a89aaea81d9a549923c846b819832a332845abcb61ab6ef` |
| `formal/environment/source-file-identities.json` | `1853289c7fd475c3483c68eec07c254c2fd1949e8fb50603ed89a1966b36eaff` |
| `R/.clawcodex/skills/math-team/references/protocol.md` | `e712830b3febe6e3fcaf0479c7aa9fc30f23aa4fcc5e1f45088f736f9c161f2b` |

Read in full: protocol, request, candidate, ledger, protected definitions, and the four supplemental provenance files listed after the environment report. Read relevant portions: Factors.lean lines 1–220; Prime/Defs.lean lines 1–128, with a declaration search in its directory; Even.lean lines 1–67 and matching declaration-search context; environment-report.txt lines 1–40 and 105–133.

The candidate's plan references D2–D4 were not read or accepted as theorem dependencies. Every mathematical use of those plans is reargued in the supplied candidate. Their interface/name-alignment claims are not separately certified here. No other review report, old verdict, task board, author-confidence artifact, or explorer computation was consulted. No nested agent was used. Only this assigned report was written; the candidate and protected files were not edited.

## 3. Source eligibility and dependency preconditions

### 3.1 Version and public-availability evidence

All external mathematical source text inspected belongs to Mathlib commit

`905b95818eb32af7874a58b427f50c1711a5e96c`.

Local `git rev-parse HEAD` returned that exact SHA. `git status --short -- Mathlib/Data/Nat/Factors.lean` returned no changes. More strongly, `git rev-parse <SHA>:<path>` and `git hash-object <local-file>` agreed for each inspected source:

| Source path relative to M | Matching Git blob |
|---|---|
| `Mathlib/Data/Nat/Factors.lean` | `292355d305be37499c8415d15b430aa241132c9b` |
| `Mathlib/Data/Nat/Prime/Defs.lean` | `5a4bb9cd22784d65a0ade53b88c3641f38c19f85` |
| `Mathlib/Algebra/Group/Even.lean` | `de3397af958e079008db2a0126fff3fe64e73b06` |

The stored raw GitHub response `public-ci-mathlib.stdout` explicitly associates that head SHA with the public repository (`private:false`) and these pre-cutoff workflow records:

- Release run `https://github.com/leanprover-community/mathlib4/actions/runs/30379912464`: created `2026-07-28T16:47:39Z`, updated `2026-07-28T16:47:53Z`.
- CI run `https://github.com/leanprover-community/mathlib4/actions/runs/30385574037`: created `2026-07-28T18:01:52Z`, updated `2026-07-28T18:16:52Z`.

The capture record identifies the exact-SHA `gh api` query, exit 0, and the matching stdout hash. The release response records v4.32.2 published `2026-07-28T16:47:51Z`. Its tag/release is mutable, so the exact-SHA public workflow records, not the present tag pointer alone, are the availability evidence. The local commit metadata additionally agrees with `2026-07-28T16:36:13Z`, but a commit date alone would not suffice.

Thus the inspected mathematical source version meets the inclusive 2026-07-31 cutoff on the supplied raw provenance evidence. I inspected the recorded metadata; I did not repeat the network request. The later capture date is not a later mathematical revision. No post-cutoff mathematical source or remembered analytic theorem was used.

Source citations:

1. Leonardo de Moura, Jeremy Avigad, Mario Carneiro, *Prime numbers*, `Mathlib.Data.Nat.Factors`, at the SHA above: <https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Data/Nat/Factors.lean>. Exact declarations audited below.
2. Same file authors and title, `Mathlib.Data.Nat.Prime.Defs`, same SHA: <https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Data/Nat/Prime/Defs.lean>, lines 38–43, 66–78, 88–105. This corroborates the accepted primality convention and the candidate's elementary divisor argument.
3. Damiano Testa, *Squares and even elements*, `Mathlib.Algebra.Group.Even`, same SHA: <https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Algebra/Group/Even.lean>, lines 53–60, where `to_additive` supplies `Even a := ∃ r, a=r+r`.

Registration in the team's `sources.md`, and a full toolchain/transitive compiled-dependency audit for future Lean proofs, remain separate formal/provenance gates. This review does not certify them merely from the environment report's conclusions.

### 3.2 Exact factorization facts

Let F mean the pinned Factors.lean, not a recalled unique-factorization theorem.

| Fact | Exact usable statement and preconditions | Applicability / verdict |
|---|---|---|
| F1, lines 49–50 | `primeFactorsList 1 = []` | PASS. No premise. Gives Ω(1)=0 and λ(1)=1. |
| F2, lines 55–65 | For any natural n,p, `p ∈ primeFactorsList n → Nat.Prime p` | PASS. PC00 obtains membership from actual list positions, including tail entries. No distinctness premise. |
| F3, lines 70–81 | `n ≠ 0 → (primeFactorsList n).prod = n` | PASS. PC00 supplies this from m>1. It is not applied to zero. |
| F4, lines 83–88 | `Nat.Prime p → p.primeFactorsList = [p]` | PASS. Primality is either quantified or established by the displayed finite divisor checks. |
| F5, lines 167–179 | For natural n and list l, `l.prod=n` and `(∀ p∈l, Nat.Prime p)` imply `l ~ primeFactorsList n` | PASS. No extra sortedness, squarefreeness, or separately stated nonzero hypothesis. The source proof derives nonzeroness from prime entries if needed. |
| F6, lines 195–202 | `a≠0 → b≠0 → (a*b).primeFactorsList ~ a.primeFactorsList ++ b.primeFactorsList` | PASS. E01.1 supplies both nonzero premises by positivity. Source proof uses F5, the two F3 product equalities, and F2. It does not require coprimality. |

The nearby coprime variant at lines 204–211 is not the theorem used. Confusing these two variants would materially alter the proof; the candidate has not done so. F1–F6 have actual proof bodies in the pinned source; no custom axiom was substituted. This is a source/precondition audit, not a fresh kernel check of the library's entire transitive proof graph.

## 4. Target, definitions, and hypothesis audit

- The protected Ω is list length, not the number of distinct prime divisors. F3, F2, and F5 identify this list as the full prime factorization; F6 preserves repeated occurrences by concatenation.
- λ has codomain ℤ, so -1 is a genuine negative integer. λ(1)=1 is proved, not assumed as a convention inconsistent with the definition.
- `Target` is literally `∀ N : ℕ, Even N → 2<N → ∃ a b : ℕ, 0<a ∧ 0<b ∧ N=a+b ∧ λ(a)=-1 ∧ λ(b)=-1`.
- Positive integer inputs and witnesses in the original request are exactly their natural representatives. Even N>2 has N=2m with m>1; coercion preserves the positive factorizations and the sum. There is no lost negative-N case under N>2.
- No primality, oddness, coprimality, or distinctness is added to target witnesses. Primes occur only in the explicitly proved reduction/auxiliary conditions. In particular a=b is both permitted and used.
- Multiplicativity is claimed only for positive factors. The totalized λ(0) is not needed in any construction or finite summand.
- For counting, R is a natural cardinality; L,C,K and the identity are signed integer quantities. Natural `N-a` occurs only with `0<a<N`. C02–C09 assume N>=2, which includes every target input and does not add evenness to the counting identity.

Verdict: PASS for target fidelity in these partial arguments. This is not a replacement for the separate blind formal-statement workflow required by the request.

## 5. Statement-by-statement proof checks

References in this section are to the exact `proof-v1.md` snapshot.

### 5.1 Signs, multiplicity, and constructions

| ID / lines | Verdict | Load-bearing checks |
|---|---|---|
| C01.1, 79–85 | PASS | Induction exhausts the disjoint forms 2r and 2r+1. Successor-power multiplication gives the respective integer signs. Distinctness of 1 and -1 gives the converse parity assertions and λ²=1. No factorization result is presumed here. |
| C01.2, 87–91 | PASS | F1 and length of the empty list give Ω(1)=0; exponent zero gives λ(1)=1. |
| E01.1, 93–101 | PASS | Positive u,v meet F6. Permutation preserves length and concatenation adds lengths, including repeated/common primes. The separately justified exponent-addition law gives complete multiplicativity with no coprimality premise. |
| E01.2, 103–119 | PASS | F4 gives prime length one; primes are positive. Multiplicativity and λ²=1 give the positive-square rule; primality of 2 gives doubling. The local composite-factor argument reduces each listed primality to all d>=2 with d²<=n. The divisor ranges and every displayed remainder for 13,19,59 are correct; 2,3,5,7 are also covered. This finite verification establishes only those primes. |
| E03, 123–127 | PASS | One common positive multiplier d makes both da,db positive and preserves the sum by distributivity. Their signs are exactly λ(d)s. The specialization uses s∈{1,-1}, so (-s)s=-1; it is not asserted for arbitrary integer s without that restriction. |
| E02, 129–133 | PASS | Even N>2 supplies m>1 with N=2m. Doubling converts λ(N)=1 to λ(m)=-1. The diagonal witnesses are legal. The direct half-sign version has precisely the needed sign assumption, not arbitrary m. |
| E04, 135–139 | PASS | The sign of each positive multiplier selects one of two actual seed pairs. Both sign cases are exhausted, and the same multiplier scales both witnesses. Seed hypotheses already force a positive seed sum. |
| E05.8, 141–153 | PASS | For λ(m)=1, (3m,5m) has two negative signs; for λ(m)=-1, (4m,4m) does. Both pairs sum to 8m and are positive. Every m>0 has one of these signs; 8m>=8 and is even. This proves all multiples of eight, not all even numbers. |

### 5.2 Ordered counting and exact assembly

| ID / lines | Verdict | Load-bearing checks |
|---|---|---|
| Counting definitions, 155–172 | PASS | The domains are finite positive intervals. F_N filters first coordinates, and natural subtraction is guarded by membership in I_N. The two meanings of N-1, as an index and as a signed term, are distinguished. |
| C02, 174–185 | PASS | For N>=2, I_N is exactly 1 through N-1, with N-1 elements. Casting `(N-1)+1=N` justifies the integer cardinality formula. For 0<a<N, exact subtraction gives positive b=N-a<N, a+b=N and N-b=a. Reflection is therefore a self-inverse bijection of this same interval. N=2 is included without a missing endpoint case. |
| C03, 187–193 | PASS | The proved bijection, not an unverified change of domain, reindexes the reflected sum. Finite addition is invariant under this permutation, yielding L(N-1). |
| C04, 195–211 | PASS | The inverse to a↦(a,N-a) is first-coordinate projection. From any positive pair summing to N, b>0 gives a<N and exact subtraction gives b=N-a. Off-diagonal ordered pairs are counted twice through different indices, while a diagonal pair is counted once. No erroneous division by two occurs. |
| C05, 213–223 | PASS | Four exhaustive integer sign pairs prove `4δ=(1-λ(a))(1-λ(b))`. The positive-input conditions are respected. |
| C06, 225–231 | PASS | Partition into F_N and its complement gives exactly the integer cast of the natural cardinality. It is not a signed count or a natural subtraction. |
| C07, 233–249 | PASS | Summing the indicator identity and expanding in ℤ gives one constant sum, two single-λ sums, and C(N). C02 supplies N-1; C03 identifies the reflected sum. The result is exactly `4*(R(N):ℤ)=((N:ℤ)-1)-2L(N-1)+C(N)` for all N>=2, with no evenness premise. |
| C08, 251–257 | PASS | Positive finite cardinality iff nonemptiness, followed by the explicit C04 bijection, yields precisely the positive-witness statement G(N) in both directions. |
| C09, 259–277 | PASS | With r=(R(N):ℤ)>=0, K=4r gives `R>0 ↔ K>0 ↔ K>=4`. Rearranging K>0 yields `2L(N-1)-((N:ℤ)-1)<C(N)` with the correct strict direction. C08 gives the equivalence with G. Mere K>=0 cannot be substituted. |
| A01, 279–285 | PASS, equivalence only | At each admissible even N>2, C09 applies because N>=2. Hence Target iff the universal pointwise strict bound K01. Neither direction proves that bound. |

There is no sign/division/truncation defect in the displayed counting identity. Its global compatibility condition is exactly the same pointwise strict inequality at every admissible N; no averaged statement or finite range discharges it.

### 5.3 Prime-core reduction and attempted bridges

| ID / lines | Verdict | Load-bearing checks |
|---|---|---|
| PC00, 289–305 | PASS | F3 makes the factor list nonempty when m>1. Its positive even length is at least two, so two actual positions can be removed. F2 proves the chosen entries prime, without making their values distinct. The tail product d is positive, including empty tail d=1. From m=dpq and the two prime signs, multiplicativity yields λ(d)=1. No unproved factor-selection or division step is hidden. |
| PC01, 307–322 | PASS, equivalence only | Target applies to every 2pq because p,q>=2 imply 2pq>=8 and evenness. Conversely, split the sign of m=N/2: the negative case is diagonal; the positive case uses PC00 and the assumed Core, scaled by its positive-sign d. The two signs exhaust all m>1. The hypothesis Core is scoped only to that implication; no circular invocation of Target occurs. Cases p=q, p=2, q=2 are all retained. |
| PC01 counterexample consequence, 324 | PASS, conditional only | Failure at N rules out the negative half-sign. If its extracted core had witnesses, the same d would scale them to N, a contradiction. Since d>=1, the failing core is no larger, and strictly smaller when d>1. Thus a least counterexample, if one exists, must be a core. This neither produces nor rules out a counterexample. |
| PB00, 330–342 | PASS, implication only | A positive pair at 2q scales by prime p to a negative pair at 2pq. Exchange p,q if necessary. If neither is >=5, primality leaves only 2 and 3, yielding exactly cores 8,12,18; the displayed negative pairs (3,5),(5,7),(5,13) check all of them, including repeated primes. PB is sufficient but not asserted necessary. |
| PB01 even-summand equivalence, 344–350 | PASS | Doubling a negative pair at positive q gives an even-even positive pair at 2q. Conversely positive even summands have positive halves, and cancellation plus doubling gives the negative pair at q. The odd-prime statement is genuinely additional to the even Target. |
| PB01 reflection obstruction, 352–358 | PASS, stated implications only | Under failure at q>=2, reflection injects negative-sign indices into positive-sign indices. Hence |A|<=|B| and L(q-1)=|B|-|A|>=0. Its contrapositive makes strict negativity sufficient, not necessary. It supplies no uniform strict-negativity theorem; the proposed universal version is false (§6). |
| PB01 parity disjunction, 360 | PASS | Summands of an even number have the same parity. Thus even-even and odd-odd positive pairs are the exhaustive options, but the text proves neither option uniformly. |
| PB02 forced signs and three tests, 362–397 | PASS | Under PB failure, PB01 forbids a negative pair at q. Positive complements then force λ(q-2)=λ(q-3)=1, while (1,2q-1) forces λ(2q-1)=-1. Each proposed test has the claimed sign criterion. At prime 59, the exact factorizations 57=3·19, 56=2³·7, 117=3²·13 give +,+,-, so all three tests fail. Meanwhile 14=2·7 and 104=2³·13 both have positive sign and sum to 118. This refutes only the three-test cover, not PB. No general computational exhaustion is claimed. |
| PB02 product-parity discussion, 391–397 | PASS as identification of a missing step | Multiplicativity computes the product of the two known shifted signs but does not compute λ of an expanded sum or infer a λ equality from congruence modulo q. No unsupported sign identity or contradiction is inserted. This is not a proof that every possible product-identity approach fails. |
| LS01, 399–413 | PASS, stated implications only | For admissible m>1, a supplied t has t,m-t,m+t positive. If λ(m-t)=1, (2t,2(m-t)) is a negative pair. Otherwise the dichotomy gives λ(m-t)=-1 and the LS disjunction gives λ(m+t)=-1, so (m-t,m+t) works. Both pairs sum to 2m. Under failure of G(2m), the diagonal is excluded and the same constructions force the stated two shifted signs for every eligible t. No uniform t or contradiction to that pattern is proved. |

The local dependency graph is acyclic. The two directions of PC01 and A01 are ordinary deductions under separately scoped premises. PB and LS are not used by the unconditional elementary, counting, or factor-list results.

## 6. Precise open and rejected obligations

| Ledger obligation | Review status | Remaining issue |
|---|---|---|
| O-M1 / Core: every prime pair p,q has G(2pq) | UNRESOLVED | The equivalence PC01 is proved, but no uniform core representation is provided. |
| O-M2 / K01: the strict C bound for every even N>2 | UNRESOLVED | The identity gives K=4R>=0, not the strict positivity equivalent to existence. |
| O-M3 / PB: P_1(2q) for every prime q>=5 | UNRESOLVED | The three-test cover is demonstrably incomplete. The correct sufficiency proof is not a proof of PB. |
| O-M4: G(q) for every prime q>=5 | UNRESOLVED | The doubling implication is valid; no uniform odd-prime result is supplied. |
| O-M5: L(q-1)<0 for every prime q>=5 | FAIL / FALSE | q=5 is a counterexample under exactly the candidate's sum convention. |
| O-M6 / LS | UNRESOLVED | The constructions require an eligible t; none is supplied uniformly. |

### Counterexample to O-M5, not to Target

Take q=5. Primality is covered by the candidate's exact check, and 5<=q holds with equality. Its defined interval is J_(q-1)={1,2,3,4}. The proved local signs give

`L(4) = λ(1)+λ(2)+λ(3)+λ(4) = 1-1-1+1 = 0`.

Therefore the required strict inequality `L(4)<0` is false. This is an exact deduction from the accepted definitions, not an empirical search or an external theorem. It falsifies precisely proof-v1 lines 358 / ledger line 114's optional universal assertion. PB01's implication `L(q-1)<0 → G(q)` remains valid. Indeed 5=2+3 already has the negative pair; failure of a sufficient condition is not failure of the conclusion.

The candidate explicitly labels O-M5 unproved and does not rely on it. Accordingly this finding is not a gap repaired inside another proof. It is a rejected auxiliary proposition that needs a ledger/status correction. No modified threshold, replacement assertion, or repaired proof is supplied in this review.

The original Target has neither been proved nor refuted here. In particular, q=59 only refutes a finite menu, and q=5 only refutes the stronger partial-sum assertion.

## 7. Formal boundary and recommended next action

1. **Generator/leader:** reclassify the exact O-M5 assertion as refuted, preserving its q=5 witness. Do not route that unchanged assertion for proof. The other open bridges remain open; this report does not add a replacement bridge.
2. **Formal generator/blueprinter:** the PASS partial results can be implemented against the protected definitions, retaining every positivity premise, repeated prime occurrence, ordered count, signed cast, and conditional assumption listed above. No change to the protected Target is warranted by this review.
3. **Source-ledger owner:** register the exact pinned sources/declarations and raw availability evidence in the designated provenance ledger. This report records evidence but does not edit `sources.md`.
4. **Formal reviewer/integrator:** compile actual theorem files in the pinned environment, inspect statements and transitive axioms, eliminate placeholders and unsupported custom axioms, and preserve command/diagnostic/hash records. I did not run Lean or `#print axioms`; source inspection and this LLM review do not discharge these gates.
5. **Leader:** route the genuinely missing uniform mathematical statement separately. A proof of Core or K01, or a proved sufficient PB/LS bridge, must still cover every quantified input before the original success conditions can be met.

No repairs to the accepted partial derivations are required by this review. The necessary correction is to the status of the false optional subroute, while the substantive global proof and Lean obligations remain unfinished. Certification attaches only to the listed snapshot and stated partial conclusions; later mathematical changes require review of the affected claims.
