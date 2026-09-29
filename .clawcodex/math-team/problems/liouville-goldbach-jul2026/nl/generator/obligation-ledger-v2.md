Mode: CERTIFICATION — versioned correction ledger, not an acceptance report.

# Obligation ledger for generator proof v2

Owner: `nl-generator`; original production task `987c8d91ddff`; v2 repair requested by `team-lead`.
Problem root P: `.clawcodex/math-team/problems/liouville-goldbach-jul2026`.
Candidate: `P/nl/generator/proof-v2.md`.

## 1. Status vocabulary and scope

- **CANDIDATE-PROOF** marks a written proof. The corresponding v1 partial claims received the fresh review described below; this label itself does not certify this v2 revision or Lean verification.
- **CONDITIONAL-PROOF** means only the stated implication/equivalence has a written proof; no open premise is declared true.
- **OPEN-MATH** means no proof is supplied for that mathematical assertion.
- **REFUTED-AUXILIARY** means the exact auxiliary assertion has a counterexample and is removed from the viable obligation queue; it is not a counterexample to the original target.
- **OPEN-REVIEW / OPEN-FORMAL** are separate acceptance gates, not extra mathematical hypotheses.

The fresh report `P/nl/reviews/partial-proof-review-v1.md`, SHA-256 `199feafd2fa03956516c7142861cb3ebb61bdf61bad2ec7acc159cc3287f2a2a`, passes v1's stated partial proofs and conditional implications but refutes the optional O-M5 assertion at q=5 (§6, lines 169–177). This v2 preserves the passed derivations and corrects the rejected appendix. No threshold change, replacement inequality, or new bridge is proposed. Review of v1 is not blanket acceptance of this v2 correction.

Preserved baselines: `P/nl/generator/proof-v1.md`, SHA-256 `eb6974f5493f7b77773ba5e685240e8d608f43e6fb2a1156d627d7a0dbca86f5`; `P/nl/generator/obligation-ledger-v1.md`, SHA-256 `69c2efa85c08e5d14437cb66f663784bc59d89fc61dce81dc7c91f10a9f7b48b`. Both v1 files remain unchanged.

The artifact-producing assignment is satisfied when this ledger and proof candidate are saved and delivered. The original target is **unresolved**. Only `P/formal/approved-v1/Definitions.lean` fixes the protected definitions/target; no Lean file was edited, no compiler was invoked by this worker, and no shared source ledger was modified.

## 2. Exact input/source dependencies

| ID | Exact dependency | Locator, hypotheses, and use |
|---|---|---|
| D0 | Original request | `P/request.md:5–14,76–85`; every even N>2, positive witnesses, negative signs, diagonal allowed, ordered count and signed identity |
| D1 | Protected definitions | `P/formal/approved-v1/Definitions.lean:6–14`; Ω is length of `Nat.primeFactorsList`; λ has integer codomain; natural target |
| D2 | Candidate interface plan | `P/nl/sketcher/formal-handoff-v1.md:29–80`; conventions and proposed declaration names only, not a proved input |
| D3 | Candidate dependency plan | `P/nl/sketcher/decomposition-v1.md:19–66`; no lemma assumed on its authority |
| D4 | Explorer candidate | `P/nl/explorer/attempt-v1.md:21–29,74–106,140–172`; source of proposed routes, with all load-bearing uses reproved in proof-v2 |
| F1 | `Nat.primeFactorsList_one` | Pinned `Mathlib/Data/Nat/Factors.lean:49–50`; no hypotheses; list at 1 is empty |
| F2 | `Nat.prime_of_mem_primeFactorsList` | Same file:55–65; list membership implies primality; used for extracted factors and positive tail product |
| F3 | `Nat.prod_primeFactorsList` | Same file:70–81; requires n!=0, supplied by m>1; list product is n |
| F4 | `Nat.primeFactorsList_prime` | Same file:83–88; requires primality, supplied either as a hypothesis or by the exact small trial-divisor proof; prime list is singleton |
| F5 | `Nat.primeFactorsList_unique` | Same file:167–179; finite list product n and every entry prime imply permutation with the standard list; exposes foundational unique factorization behind F6 |
| F6 | `Nat.perm_primeFactorsList_mul` | Same file:195–202; requires both factors nonzero, always supplied by positivity; concatenation counts repeated prime occurrences, without coprimality |
| ENV | Eligible pinned environment evidence | `P/formal/environment/environment-report.txt:17–30,115–125`; Mathlib SHA `905b95818eb32af7874a58b427f50c1711a5e96c`, Lean v4.32.2, public exact-SHA records before cutoff |

F1–F6 belong to the one factorization file actually read by this worker. Its local absolute path is `P/lean/.lake/packages/mathlib/Mathlib/Data/Nat/Factors.lean`. The exact theorem statements, immutable URL, authors, and input hashes are recorded in proof-v2 §§0.3–0.4. A local git check returned the required HEAD and no tracked modification to this file. This worker relies on the supplied environment record for public availability and did not re-audit upstream publication metadata.

No analytic/literature theorem, later version, or unsupported remembered external result enters any proof. Finite sums, signs, list lengths, small primalities, and elementary inequalities are justified locally in the candidate. Their formal implementation remains an eligible-library obligation. The explorer's bounded Python observations have **no proof dependency** here; q=59 and the few small primes are justified by exact displayed arithmetic instead.

## 3. Candidate theorem/dependency map

The proposed Lean names below are interfaces for the leader/blueprinter. They are not assertions that declarations with these names already exist. Splitting a sketcher's lemma ID into suffixes exposes proof components while preserving its original statement.

| NL ID | Exact claim / output | Dependencies | Candidate status | Proposed Lean connection |
|---|---|---|---|---|
| C01.1 | Positive λ is ±1; λ²=1; sign corresponds to parity of Ω | D1; local induction on exponents/parity | CANDIDATE-PROOF, proof-v2 §1 | `liouville_sign`, helper exponent parity |
| C01.2 | Ω(1)=0 and λ(1)=1 | D1,F1 | CANDIDATE-PROOF, §1 | `liouville_one` |
| E01.1 | For u,v>0, Ω(uv)=Ω(u)+Ω(v), λ(uv)=λ(u)λ(v) | F6; locally proved length/exponent rules | CANDIDATE-PROOF, §1 | `omega_mul_positive`, `liouville_mul_positive` |
| E01.2 | Prime sign -1; positive square sign +1; λ(2x)=-λ(x); exact needed constants | F4,E01.1,C01.1; local exact primality tests | CANDIDATE-PROOF, §1 | `liouville_square_positive`, `liouville_small_values`, prime/doubling helpers |
| E03 | Common positive scaling multiplies both signs by λ(d); opposite sign yields G | E01.1,C01.1 | CANDIDATE-PROOF, §2 | `representation_scaled_sign` |
| E02 | Diagonal: even N>2 and λ(N)=1 imply G(N); also direct half-sign criterion | E01.2; exact even halving | CANDIDATE-PROOF, §2 | `representation_diagonal` |
| E04 | Both-sign seed at d implies G(dm) for all m>0 | C01.1,E03 | CANDIDATE-PROOF, §2 | `representation_two_sign_seed` |
| E05.8 | All 8m,m>0; witnesses (3m,5m) or (4m,4m) by multiplier sign | C01.1,E01.1,E01.2 | CANDIDATE-PROOF, §2 | `representation_multiple_eight` |
| C02 | I_N=J_(N-1); card/cast; positive reflected input; reflection involution | N>=2; elementary exact subtraction/interval enumeration | CANDIDATE-PROOF, §3 | `mem_interval_bounds`, `interval_card_cast`, `reflection_bijection` |
| C03 | Reflected sum equals L(N-1) | C02; finite-sum permutation argument | CANDIDATE-PROOF, §3 | `sum_liouville_reflection` |
| C04 | a↦(a,N-a) bijects filtered interval and ordered positive negative-sign pairs | C02; sum cancellation and positivity | CANDIDATE-PROOF, §3 | `ordered_pair_count_equiv` |
| C05 | Integer two-sign indicator identity | C01.1; positive a,b; exhaustive four sign cases | CANDIDATE-PROOF, §3 | `two_sign_indicator` |
| C06 | Natural count cast equals integer indicator sum | C02; finite partition/count argument | CANDIDATE-PROOF, §3 | `count_eq_indicator_sum` |
| C07 | `4*(R N:Z)=((N:Z)-1)-2*L(N-1)+C N`, all N>=2 | C02,C03,C05,C06; integer distributivity | CANDIDATE-PROOF, §3 | `four_mul_representation_count` |
| C08 | R(N)>0 iff exact positive-witness conclusion G(N) | C04; finite nonempty/cardinality argument | CANDIDATE-PROOF, §3 | `representation_count_pos_iff` |
| C09 | R>0 iff strict C bound iff K>=4 iff G; all N>=2 | C07,C08; natural cast and ordered integer arithmetic | CANDIDATE-PROOF, §3 | `count_pos_iff_keystone`, `keystone_ge_four_iff` |
| A01 | Target iff universal strict counting keystone K01 | C09; N>2 implies N>=2 | CONDITIONAL-PROOF, §3 | exact assembly implication only, no open-premise final theorem |
| PC00 | m>1 and λ(m)=1 imply m=dpq, p,q prime, d>0, λ(d)=1 | F2,F3,C01.1,E01.1,E01.2 | CANDIDATE-PROOF, §4 | proposed `positive_sign_prime_pair_factorization` |
| PC01 | `Target iff forall primes p,q, G(2pq)`; equality of primes allowed | C01.1,E02,E03,PC00 | CONDITIONAL-PROOF of equivalence, §4 | proposed `target_iff_prime_product_cores` |
| PC01.cor | Any counterexample yields failing prime-product core no larger; least one is a core | PC00,E02,E03 | CONDITIONAL-PROOF, §4 | optional consequence, not needed for equivalence |
| PB00 | Uniform positive representations of 2q for primes q>=5 imply Core/Target | E03,E01.2,PC01; explicit cores 8,12,18 | CONDITIONAL-PROOF, §5 | proposed `target_of_prime_positive_bridge` |
| PB01 | Even-even positive pair at 2q iff negative pair at q; L(q-1)<0 suffices | E01.2,C01.1,C02; reflected injection/count | CANDIDATE-PROOF of stated implications, §5 | optional bridge helpers; not PB itself |
| PB02 | PB failure forces exact three shifts; the three-test menu fails at prime 59 | C01.1,E01.1,E01.2,PB01; exact factorizations | CANDIDATE-PROOF of stated implications/example, §5 | optional obstruction helper, not an obstruction to PB |
| LS01 | LS implies Target; failure of G(2m) forces the indicated two shifted signs | C01.1,E01.2,E02; positive domain checks | CONDITIONAL-PROOF, §5 | optional `target_of_shift_bridge`, not LS itself |

Acyclic core graph:

`definitions + F1/F4/F6 -> signs/multiplicativity -> scaling/diagonal/8m`

`definitions -> intervals/reflection -> pair/count infrastructure -> identity -> strict-bound equivalence`

`factor-list existence + signs/multiplicativity -> PC00 -> (Core implies Target)`

`Target -> Core` is separately a direct instantiation, used only to conclude the equivalence. The reverse implication never calls Target or its own result as a hypothesis.

## 4. Preconditions and compatibility obligations explicitly discharged in the candidate

| Obligation | Where discharged |
|---|---|
| Prime factors are counted with multiplicity, not by a set of distinct values | D1 and E01.1: take lengths of concatenated lists; no deduplication |
| λ(1)=1 and codomain contains -1 | C01.2; D1 uses Z |
| No multiplicativity at zero, no hidden coprimality | E01.1 invokes F6 only with positive factors; F6 has no coprimality premise |
| All scaled witnesses are positive; same multiplier applies to both | E03; reused in E05.8, PC01, PB00 |
| Every even N>2 has a natural half m>1 | E02 and PC01: N=2m and 2m>2 |
| Diagonal allowed, not counted twice | E02; C04 explicitly identifies the unique first-coordinate index |
| All m>0 cases for 8m covered | E05.8's exhaustive ±1 split; no extra arithmetic premise |
| Both a and N-a positive on the counting domain | C02; positivity repeated before C05/C06 applications |
| Natural subtraction used only where exact | C02,C04; signed identity and estimates are in Z |
| Ordered, not unordered, count | C04 maps every first coordinate to its ordered pair; off-diagonal reverse counted separately |
| Reflection is globally compatible with the same finite domain | C02 involution; C03 finite reindexing |
| Natural-to-integer casts match the stated RHS | C02 casts `(N-1)+1=N`; C06 casts natural cardinality; C07 uses Z throughout |
| Strict, not non-strict, existence criterion | C09 distinguishes K>0 and K>=4 from automatic K>=0 |
| Prime cores include repeated primes and prime 2 | PC00 selects occurrences, not distinct values; PC01 has no prime restriction |
| Factor-list selection exists even for m with exactly two factors | PC00: nonempty even length >=2; empty tail yields d=1 and λ(d)=1 |
| Conditional core hypothesis is not silently assumed true | PC01 labels each direction and discharges Core only as a premise of one implication |
| PB small-prime endpoint cases exhaust all primes below 5 | PB00 uses primes >=2 and composite 4; cores 8,12,18 explicitly represented |
| PB not confused with the target at 2q | PB00: desired signs +1 versus target's -1 diagonal |
| Odd-prime auxiliary claim not confused with original even target | PB01 labels `P_(-1)(q)` an additional odd-target assertion |
| Shift expressions lie in positive domain | LS01 imposes 0<t<m; all candidate pairs positive |
| No post-cutoff theorem supplies a missing bridge | Only F1–F6 and local derivations are used; no literature input |

## 5. Open mathematical obligations and rejected auxiliary route

| ID | Assertion and current status | Remaining issue or exact rejection | Next owner/action |
|---|---|---|---|
| O-M1 / Core | `forall p,q : Nat, Prime p -> Prime q -> G(2*p*q)` | PC01 reduces Target to this statement but does not prove any uniform representation of these cores | Leader route to a focused generator/explorer; seek a uniform construction or new accepted theorem, not more fixed seeds |
| O-M2 / K01 | `forall N, Even N -> 2<N -> 2*L(N-1)-((N:Z)-1)<C(N)` | Identity gives K=4R and K>=0 only; strict positivity is equivalent to missing target existence | Leader route to a pointwise estimate/construction task; any estimate must retain effective constants and full coverage |
| O-M3 / PB | `forall prime q>=5, P_1(2q)` | PB00 proves sufficiency only; the even route and the three local shifted tests leave uncovered cases | Targeted mathematical work on uniform positive representations, with all primes quantified |
| O-M4 / odd-prime subroute | `forall prime q>=5, P_(-1)(q)` | Would imply PB by doubling, but concerns odd targets not supplied by original Target; reflected injection gives only a necessary condition under failure | Optional stronger branch; do not silently assume |
| O-M5 / partial-sum subroute | **REFUTED-AUXILIARY:** `forall prime q>=5, L(q-1)<0` | At prime q=5, `L(4)=1-1-1+1=0`, so the strict bound fails under all hypotheses. PB01's pointwise sufficient implication remains valid, but this universal premise is false | Remove this exact assertion from the viable proof queue; retain the counterexample. No adjusted threshold or replacement assertion is proposed |
| O-M6 / LS | For every m>1 with λ(m)=1, some 0<t<m with λ(t)=1 has λ(m-t)=1 or λ(m+t)=-1 | LS01 converts it into witnesses but gives no uniform t; failure's forced pattern has not been contradicted | Alternative focused shift-lemma investigation |

O-M1–O-M4 and O-M6 describe alternative open routes, not simultaneous required hypotheses. O-M5 is refuted and is no longer a viable route. Proving Core suffices; proving K01 is equivalent; proving PB or LS would suffice by the proved conditional assemblies. No necessity of PB, LS, O-M4, or the rejected O-M5 for Target is claimed. No replacement for O-M5 is introduced.

## 6. Preserved focused attempt and exact rejection scope

The generator pursued PB by:

1. reducing its even-even witness option exactly to negative representations at the odd prime q;
2. obtaining the necessary failure condition L(q-1)>=0 by a reflected injection and proposing a universal strict-negativity subroute, subsequently refuted by the fresh reviewer at q=5;
3. deriving the exact three shifted constraints from PB failure;
4. rigorously checking their simultaneous occurrence at prime q=59;
5. inspecting product-parity continuations and identifying the missing second sign for the resulting polynomial rather than assigning one from λ(q).

The three candidate pairs `(1,2q-1)`, `(4,2(q-2))`, `(6,2(q-3))` all fail at q=59. This is an exact falsification of that **three-pair cover** only. PB holds at q=59 by the explicit pair 14+104. The stronger conclusion “PB fails”, “Core fails”, or “the target is false” is not licensed. Nor is the entire product-identity route refuted: this attempt merely lacks a uniform sign identity/case cover.

The separate exact counterexample to O-M5 is q=5. It is prime by E01.2, satisfies q>=5 with equality, and has J_(q-1)={1,2,3,4}. Hence C01.2/E01.2 give `L(4)=lambda(1)+lambda(2)+lambda(3)+lambda(4)=1-1-1+1=0`, not a negative integer. The unchanged universal assertion is therefore refuted. The valid local implication `L(q-1)<0 -> G(q)` is unaffected, and `5=2+3` shows its conclusion can hold when that sufficient condition fails. This rejects only the optional sufficient route, not PB, Core, or Target. No altered threshold or substitute universal inequality is proposed.

The fixed source attempt `P/nl/explorer/attempt-v1.md` and both generator v1 files were not edited. No prior accepted artifact was overwritten. Broader finite seed tables and unreviewed computational ranges were deliberately not polished into purported universal evidence.

## 7. Acceptance and formalization gates still open

| Gate | Required evidence / next owner |
|---|---|
| O-R1: independent NL review of correction | The listed fresh v1 report passes the partial proofs and rejects O-M5. Leader routes this exact v2 correction/ledger for review; no blanket acceptance of v2 is inferred and the author cannot self-accept |
| O-R2: provenance integration | Leader/source-ledger owner may register the exact factor-list source/declarations using the supplied eligible environment evidence; this worker did not edit sources.md |
| O-F1: counting definitions/interfaces | Blueprinter/formal generator aligns R,L,C and interval definitions with the reviewed handoff and exact protected λ; signed arithmetic and count convention must remain unchanged |
| O-F2: local Lean proofs | Assigned formal generator proves accepted C01/E01/scaling/diagonal/8m, C02–C09, and PC00/PC01, in the pinned environment, using no sorry/custom target axiom |
| O-F3: actual kernel evidence | Compile actual files, compare protected statements, run `#print axioms`, inspect transitive dependencies, preserve hashes/commands/exits |
| O-F4: integration | Only designated integrator merges accepted formal artifacts and rechecks the designated modules |
| O-F5: final full target | Requires a proof of one missing uniform bridge and its complete formalization; partial families and equivalent statements do not meet the user's success conditions |

No task status or artifact existence is intended to close any of these acceptance gates.

## 8. Delivery and immediate next action

Deliver both owned paths:

- `P/nl/generator/proof-v2.md`
- `P/nl/generator/obligation-ledger-v2.md`

The immediate next step is **independent review of the v2 correction**, retaining the open-bridge boundary and marking O-M5 refuted rather than pending. The passed v1 partial derivations need no mathematical reworking for this repair; formal work on those independently reviewed lemmas can proceed while the leader separately routes the genuine uniform blocker. The generator remains available for a specific repair packet; no new review verdict is asserted here.
