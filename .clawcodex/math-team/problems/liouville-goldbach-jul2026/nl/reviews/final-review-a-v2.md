# Independent review of the exact partial argument

**Mode: CERTIFICATION.**

**Scoped verdict: PASS — the assigned partial mathematical argument and its limitations are supported. The original Target remains UNRESOLVED.** This is not certification of a proof of Target, and this LLM review is not Lean kernel verification.

Here `P` is `.clawcodex/math-team/problems/liouville-goldbach-jul2026`. This is one independent review of the supplied snapshot. No candidate repair, source browsing, compiler rerun, finite-audit rerun, agent spawning, or task-board modification was performed. Only this report was written.

## 1. Artifact identity and input boundary

The following SHA-256 hashes were independently recomputed. All hashes specified in the assignment match, as do all entries in FINAL_ARGUMENT's §11 identity table.

| Path relative to P | SHA-256 |
|---|---|
| `FINAL_ARGUMENT.md` | `1b93364b818b0eae95875d391ca6f944614f00b963a1e384ba1a0fe2533957a9` |
| `request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `lean/Statement.lean` | `426a0b62a141387e22f0e5481a705e3ffe3d64e0f8ad100daea3101c802e8458` |
| `lean/Statement/Scaffold.lean` | `0bd0952096ebf027fa956458dfb1c1bb08e6396cd89c77b24a3eaadbe1070d1a` |
| `lean/Statement/Smoke.lean` | `50fcf1606d7bf7c52cf84cc7ebc60f0e05a151745339f295c86c1a37ffab8e19` |
| `lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |
| `sources.md` | `9df552348f03fd84ffe0e203f1340f26e6a902f8424f924068fe6fb86c1a7dbb` |
| `formal/integration/audit-v1.json` | `4d32b5248d82c827edcb958ecd63ea62d68504bedf9fb396aa56edbcc7ca4db3` |
| `formal/environment/public-availability-witnesses.json` | `051de67ee5bfd81242942075cf9dabacd8cfa96b74abf3733b025456694cc4c1` |
| `knowledge/mangerel-v2/paper.pdf` | `ae26a659220985c55576a18d05a84d5a56988024f8781ae4ccbe04847ac16505` |
| `knowledge/mangerel-v2/arxiv-metadata.txt` | `8a1d1b2d965215664c00abbbf02af8d72ff72947e3443698b767eb7607059771` |
| `nl/code-executor/finite_certify.py` | `00a9d66bd81ca58e5cf0148fba6fa5b742c6a3285c82f46d5a1e3952aeab98f5` |
| `nl/code-executor/evidence.json` | `b42b9544e632431476c872b5696679d2908f05858737f6718f7d8c5a626fd72e` |
| `nl/code-executor/run.json` | `7ec4412954f806dffb7423c85b5f6a50d54dd1256998dc3bb407940107cf6593` |
| `nl/code-executor/run.log` | `656020dc378a129bf6f4800f153728e8fcbc8c4ca2b2b9348a917c6447a5da11` |

The mandatory protocol was read at `.clawcodex/skills/math-team/references/protocol.md`, hash `e712830b3febe6e3fcaf0479c7aa9fc30f23aa4fcc5e1f45088f736f9c161f2b`.

Content inspection comprised the above permitted inputs, PDF pages 1–3 only, the pinned source passages listed below, and the permitted raw evidence:

- `formal/integration/v1-00` through `v1-09` command/output records and the two stdin files; the recorded package head/status streams. All 58 stream hashes attached to the audit's 28 commands were recomputed without mismatch. Direct, trust-zero, root-import, default-build, and endpoint-absence output was inspected; the three recorded axiom maps agree on all 82 entries.
- `formal/environment/public-ci-{mathlib,lean,plausible,LeanSearchClient,importGraph,proofwidgets,aesop,Qq,batteries,Cli}.{json,stdout}` and the Lean/Mathlib release stdout metadata. Structured inspection checked exact-SHA/date/public-repository fields against the witness file and manifest.
- The finite program was read in full. Evidence inspection covered definitions, scope, counts, explicit examples, and structured coverage records. Recorded status labels were not treated as mathematical or independent-review evidence.

The following referenced prose artifacts were **hashed only, never read**; no obligation is discharged by their contents:

| Path | SHA-256 |
|---|---|
| `nl/generator/proof-v2.md` | `bdcf57b670ed1e1410bacad5a2f9182c565add056714ef85e0155f939a6b7735` |
| `formal/integration/integration-report-v1.txt` | `0f008c380573638e8b52796e8252eda83ee5e1eb79fd7a0caed6ef58a81984f7` |
| `formal/integration/source-proof-map-v1.txt` | `98fe3ef1958403c629e55d0a97fff50f5b2270c3e157e0e8f08664675888e977` |
| `REPRODUCE.md` | `cb982a4687549930a398cec4b3d81449ebec7cd0bb2eb9ed8fc75f8d30e301c0` |
| `nl/searcher/extraction-v2.md` | `787e83caae80656c7874f2a1e133f57e88dfcbde60a88b3d3b2e78653a954a6f` |
| `nl/code-executor/report.md` | `9df3e8eef714c3e16ebaa76e336b726eca1d36c15c63257869da9696e32e4ba4` |

No other NL proof, review, or author-confidence packet was consulted. The mathematical checks below use FINAL_ARGUMENT itself, the actual Lean source, and eligible source passages, not its citations to excluded exposition.

## 2. Target fidelity and accepted definitions

The requested quantifiers are preserved: every even integer N>2, followed by two positive witnesses whose sum is N and whose individual Liouville values are -1. Natural-number normalization loses no such N or witness. `Even N` means an additive double; at N>2 its half m satisfies m>1. No formal integer/natural transport theorem is claimed in the candidate.

`omega` is the length of a **list** of prime occurrences, not the cardinality of distinct prime divisors. The factor-list product, prime-entry, and uniqueness statements establish the intended multiplicities. The empty list at 1 gives Ω(1)=0 and λ(1)=1. `lambda : ℕ → ℤ` represents -1 without natural-number truncation. Both witness positivity conditions are explicit. There is no distinctness, primality, oddness, or coprimality restriction in Target or HasRepresentation. The auxiliary interval restrictions in the count are subsequently proved automatic, not silently added target hypotheses. No load-bearing step evaluates λ(0).

## 3. Checks of every unconditional partial proof

Line references here are to the hashed `Partial.lean`.

### Signs, multiplicativity, and families (43–159)

1. **Unit and sign dichotomy:** powers of -1 give exactly ±1, hence square 1. The unused positivity parameter in `lambda_sign` does not make any application vacuous or introduce a stronger assumption into Target.
2. **Multiplicity and complete multiplicativity:** `Nat.perm_primeFactorsList_mul` requires only u≠0 and v≠0, supplied by positive factors. Taking lengths gives Ω(uv)=Ω(u)+Ω(v), including repeated primes shared by u and v. The exponent law in ℤ then gives λ(uv)=λ(u)λ(v). No coprimality premise is missing.
3. **Primes, squares, doubling:** prime singleton lists give λ(p)=-1. The signs of 2,3,5,4 follow, and for positive m,t the equations λ(2m)=-λ(m) and λ(t²)=1 follow from the proved multiplication rule. Every factor used here is positive.
4. **Scaling:** if a,b witness P_s(n) and d>0, da,db are positive, sum to dn, and each has sign λ(d)s. For s=±1 and λ(d)=-s this product is -1. The same multiplier is used for both witnesses; no incompatible choices are assembled.
5. **Diagonal:** λ(m)=-1 and m>0 give witnesses (m,m) for 2m. For even N>2 with λ(N)=1, writing N=2m and applying the doubling sign rule forces λ(m)=-1. The extra sign hypothesis belongs only to this partial family.
6. **Two-sign seed and all 8m:** the two cases λ(m)=1 and λ(m)=-1 are exhaustive for m>0. Scaling 8=3+5 in the first case and 8=4+4 in the second gives exactly (3m,5m) and (4m,4m), respectively. All summands are positive and have sign -1. This proves every positive multiple of eight, not every even integer.

### Intervals, reflection, ordered counting, and strictness (161–327)

7. **Index arithmetic:** for N≥2, I_N={1,…,N-1}. Its natural cardinality casts to `(N : ℤ)-1` because 1≤N. Membership supplies 0<a<N and 0<N-a<N; thus natural subtraction agrees with the intended positive difference. The involution identity requires a≤N, supplied by a<N.
8. **Reflection and sums:** a↦N-a maps I_N to itself and is its own inverse. This verifies both directions and inverse conditions of the finite-sum reindexing theorem. Therefore the reflected λ sum equals L(N-1), with L inclusive at its endpoint.
9. **Ordered-pair bridge:** a↦(a,N-a) maps exactly the filtered negative indices to the ordered representation set. For any positive pair summing to N, both coordinates are below N and the second is N-a. First-coordinate projection proves injectivity. Hence R=|F_N| without dividing by two: off-diagonal orders count separately, a diagonal counts once.
10. **Indicator and expansion:** the four sign pairs give `4δ=(1-λ(a))(1-λ(b))`. Summation, integer casting of cardinalities, distributivity, and reflection give

    `4 * (R N : ℤ) = ((N : ℤ)-1) - 2*L(N-1) + C N`.

    The right-hand arithmetic is in ℤ; only the bounded indices are natural differences. Evenness is unnecessary, and N≥2 is sufficient. At the boundary N=2, R=0, L(1)=1, C(2)=1, consistent with the formula.
11. **Existence and strict inequality:** finite cardinality is positive iff the set has a member, and the member condition is precisely HasRepresentation. If K denotes the displayed right side, the identity makes K a nonnegative multiple of four. Thus R>0 iff K>0 iff K≥4, not merely K≥0. Rearranging K>0 yields exactly `2*L(N-1)-((N : ℤ)-1)<C N`. The universal equivalences retain `Even N` and `2<N`; their use of N≥2 is justified by the latter. Neither equivalence proves its universally quantified right side.

### Prime-product core, including repeats (329–386)

12. **Prime-occurrence extraction:** for m>1 the list cannot be empty because its product is m. Under λ(m)=1 it cannot have length one, which would give -1. The remaining list is `p :: q :: t`, with prime p,q. These are occurrences, so p=q is allowed. The tail product d is positive: otherwise the complete product would be zero, contradicting m>1. Empty tail gives d=1 and is retained. The product identity gives m=d(pq); multiplicativity gives λ(d)=1 because λ(p)λ(q)=1.
13. **Target ⇒ Core:** primes p,q are at least 2, so 2pq≥8>2 and 2pq is even. Target applies with no new witness restrictions.
14. **Core ⇒ Target:** for arbitrary admissible N=2m, m>1. A negative half gives the diagonal. A positive half gives m=d(pq) with d>0 and λ(d)=1; Core supplies a representation of 2pq and scaling by d preserves both negative signs and sums to N. This covers both signs, p or q equal to 2, repeated primes, and d=1. Core is only a hypothesis inside this implication. There is no circular use of the sought theorem or replacement of the infinite prime-pair quantifier by finite checks.

These checks cover all 42 theorems grouped by their load-bearing steps. No unresolved mathematical gap was found in their claimed scopes.

## 4. Prose-only conditional routes and explicit rejection

These statements in FINAL_ARGUMENT §7 are not asserted as extra Lean theorems.

- **PB ⇒ Core:** if either prime is at least 5, its positive-positive representation of twice that prime, multiplied by the other prime of sign -1, gives negative-negative signs and total 2pq. If both primes are below 5, they lie in {2,3}; the complete remaining totals are 8,12,18. The displayed pairs (3,5), (5,7), (5,13) have prime, positive summands and the correct sums. Repeated primes are covered. PB itself is unproved and is not Target evaluated at 2q, which asks for the opposite signs.
- **Even-even PB pairs iff G(q):** doubling a negative pair summing to positive q gives a positive even-even pair at 2q. Conversely, positive even coordinates can be halved to positive integers summing to q; λ(2x)=-λ(x) forces both halves negative. No assertion about odd q is obtained from Target's even-N quantifier.
- **Reflection counting under failure of G(q):** for q≥2, reflection sends each negative index into a positive index, or it would itself give a prohibited negative-negative representation. Reflection is injective, so |A|≤|B|. Since the two sign sets partition I_q, L(q-1)=|B|-|A|≥0. Its contrapositive is the stated sufficient pointwise test, not a universal estimate.
- **O-M5 is genuinely refuted:** q=5 is prime and satisfies q≥5; λ(1),…,λ(4) are 1,-1,-1,1, so L(4)=0 violates strict negativity. This is a counterexample to O-M5 only. It is not a counterexample to PB or Target, and 5=2+3 confirms G(5).
- **Three fixed PB tests:** q=59 is prime (possible prime divisors up to its square root are 2,3,5,7, none dividing it). The displayed factorizations of 57,56,117 give signs +,+,-, respectively. The three first summands 1,4,6 have sign +, whereas their complementary summands have sign -. Meanwhile 14 and 104 have respectively two and four prime occurrences and sum to 118. Thus the template failure and positive-positive alternative are correct, but supply no uniform bridge.
- **LS ⇒ Target:** in the positive-half case, 0<t<m guarantees all needed differences and summands positive. If λ(m-t)=1, the pair `(2t,2(m-t))` has both signs -1. Otherwise sign dichotomy gives λ(m-t)=-1 and the LS disjunction forces λ(m+t)=-1; `(m-t,m+t)` works. Both sums are 2m. The negative-half case uses the diagonal. The uniformly quantified LS premise is not proved, and necessity/equivalence is not claimed.

No threshold change, substitute estimate, or other repair of these routes is accepted by this review.

## 5. Source and dependency audit

### Pinned elementary mathematics

All eight inspected Mathlib files were byte-compared with their git objects at commit `905b95818eb32af7874a58b427f50c1711a5e96c`; all match. Paths below are relative to `P/lean/.lake/packages/mathlib/`.

| Source and inspected passage | SHA-256 |
|---|---|
| `Mathlib/Data/Nat/Factors.lean`, 1–235 | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `Mathlib/Data/Nat/Prime/Defs.lean`, definition, positivity, prime characterization, small primes | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `Mathlib/Algebra/Group/Even.lean`, 40–67 | `1180fa9ac282e55257e95c8402acd7314fcbd0a18bcfdede92a3cde16e1db630` |
| `Mathlib/Algebra/Ring/Parity.lean`, 370–398 | `c710e4b51d5ffc9df4e2cc16bad357ab152b1ae5ff05e8fb68a1e3812e6a3b68` |
| `Mathlib/Order/Interval/Finset/Nat.lean`, 68–98 | `e1a7b1cf7d86209af1d6f894e05f2a4cc40997840ff64461d98476fcd5e248e2` |
| `Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean`, 480–515 | `562dacf916c63c599b7c4becbf3bafdbb7fa0b493eb2f6e594f4126a6d91e62c` |
| `Mathlib/Algebra/BigOperators/Ring/Finset.lean`, 35–71 | `472cd5000412d8ec35c8b9ee919b2aeedbf0a830033a55009aad436595923809` |
| `Mathlib/Data/Finset/Card.lean`, injective-image cardinality passage | `87c674ba5464c7868fb3e253e58a695821bf8841bb4e076bac5d570236dc6229` |

The factor-list theorem signatures and source proofs support precisely the nonzero guards, singleton/empty cases, prime entries, uniqueness, and multiplicative concatenation used here. Integer sign, finite cardinality, injective-image, sum-bijection, and distribution applications have their required algebraic structures and domain conditions. In particular the sum-bijection needs inverses only on the finite domains, exactly as supplied. No analytic theorem or additive conjecture is a proof dependency.

### Cutoff provenance

The toolchain file specifies Lean v4.32.2; raw compiler metadata identifies commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`. Mathlib is pinned by immutable revision in the lakefile and manifest. The nine manifest package revisions agree with recorded installed heads and clean tracked-source statuses. The preserved exact-SHA workflow metadata contains pre-cutoff witnesses for all nine packages and Lean: Lean and Mathlib on 2026-07-28, LeanSearchClient on 2026-02-12, and the other seven packages on 2026-07-13. Failing/skipped CI outcomes do not invalidate a source-availability witness; they are not used as proof-checking evidence. Release publication times separately agree with the ledger. Later retrieval/checking dates do not change the source versions.

The corresponding raw `public-ci-*.stdout` hashes, independently checked against their command records, are:

| Name | SHA-256 |
|---|---|
| mathlib | `4337fdc10284dc0c90165a0e4926fde19ebb6ce78dfef2505a3112a277452e00` |
| lean | `aeaea1b78e78521606c013a4fafc4b9c0bcaae068cd63f6e97a57bbd26a43826` |
| plausible | `7db3a5d1c95ca7d1b1906ec25958d6f1d490a9953154fdf3180f09fd57195e7b` |
| LeanSearchClient | `3abdd2daec49091e23e2601a2d77322759da75c6967c6ef67d76cd806ad2d5af` |
| importGraph | `5551743d19c9b24dc50743a216975cc324b4bb94618b36fd2839785fbc5fb575` |
| proofwidgets | `0af1983970539258f9627cde04d59047e20557b9b5d39248ae2018f728f2cce6` |
| aesop | `83bc912b7caf04c68210490e75285c2eba39396aad9cad151c68f2322a36c06d` |
| Qq | `e8ff8f4e5970e6943179a83cc2be235f3296ef5153f1d550a3dabf86e69a575b` |
| batteries | `3bb8ca7972a48ad427bab042620fed56c5a2a71813ec02621723647adc7fa741` |
| Cli | `7db04e1305e996408659d75f8c28ea7d2c4415dcb337834ec3c93a4ee7b36844` |

This is an audit of the preserved provenance, not a fresh online authentication or complete upstream rebuild. No later external mathematical version was consulted. The ledger's excluded later MathOverflow snippet was not opened, followed, or used.

### Mangerel v2: distinct contextual assertion

PDF pages 1–3 directly confirm the May 2, 2024 v2 identification; preserved arXiv metadata gives 2024-05-02 14:48:54 UTC. Theorem 1.2 states eventual strict non-extremality `|C(N)|<N-1` for all N beyond a threshold, not an almost-all result. Remark 1 explicitly calls the threshold ineffective. Remark 2 poses the negative-negative representation problem as a question and says the paper's methods appear too rigid to address it directly.

The exposition correctly distinguishes the paper's correlation notation from this project's summatory L. Positive correlation terms can arise from positive-positive signs, so non-extremality alone is not the strict counting bound established as necessary and sufficient here. The paper's subsequent display changes the preceding exact N-1 expression to a strict inequality with N; FINAL_ARGUMENT appropriately flags the mismatch rather than importing or repairing it. Neither that display nor a quantitative PNT claim is used. This review checks attribution and applicability, not the paper's proof beyond the supplied pages, and makes no worldwide open-problem claim at the cutoff.

## 6. Recorded Lean evidence and trust boundary

The recorded default build includes `Statement.Partial` and root `Statement` and ends successfully with 925 jobs. Explicit module build, direct Lean, trust-zero Lean, and root-import checks have exit 0. The absence check has exit 1 with exactly the two expected unknown identifiers. The source inspected here agrees with these statements and does not declare either endpoint.

Selected raw evidence identities under `formal/integration/`:

| File | SHA-256 |
|---|---|
| `v1-04-default-build.stdout` | `8409d3cdd555c3d8173b495547033298258ca2089eea5b1ed0ed7cb7ff43b0c1` |
| `v1-05-partial-build.stdout` | `63105f63cf9927d0670210b44f6cfd8485c66abe7f809d663ec7b1f804005903` |
| `v1-06-partial-direct.stdout` | `6569201315dbd4f85bb46b3a1325837b33029f1cfc742252ab335188aab030b9` |
| `v1-07-partial-trust-zero.stdout` | `6569201315dbd4f85bb46b3a1325837b33029f1cfc742252ab335188aab030b9` |
| `v1-08-root-import-check.stdout` | `a4c33f9b1f6b2e91d84c3dc06192f0b60a566050a355de2e9ac4c2af621621c1` |
| `v1-08-root-import-check.stdin.lean` | `c01f72503302b7917c7c2e1b44aeee9a9cfa92eeff5871bde16535de63241120` |
| `v1-09-absent-endpoints.stdout` | `8e8f8e11e2b7324c752c36ea5a992f19f999656b89a7a1fafd8eb1c07105e590` |
| `v1-09-absent-endpoints.stdin.lean` | `0314a0c6994f5bd1ea17d69de15457c10eae9b2231dab38ac401a5f3317c7bd8` |

The 42 partial theorems and 11 local/base definitions have the recorded transitive axiom set `{propext, Classical.choice, Quot.sound}`; the 29 upstream queries have subsets. The root check exposes all 50 added declarations, with definitions and signatures matching the inspected source. There is no admitted proof, unsupported custom axiom, hidden Target assumption, or native-evaluation assumption in the inspected local proof closure and recorded axiom outputs. The four unused-variable lints do not affect the mathematics.

`UnfinishedScaffold` only has a constructor requiring a Target proof; it supplies none. Partial does not import that scaffold. Smoke evaluations are tests, not proof terms of Target. The retained trust boundary includes the Lean implementation/kernel, standard foundational axioms, and installed pinned dependency artifacts. Trust-zero checking of the local module is not described here as a complete fresh source rebuild of every upstream dependency.

## 7. Finite evidence: checked limitations

The finite program uses integer trial division and an independently structured prime-power sign-flip sieve. Each prime-power flip counts one prime occurrence, so multiplicity is handled correctly. It enumerates actual ordered pairs before comparing the identity, rather than defining R from the desired equation. It deliberately leaves λ(0) undefined and bounds every used argument. The independent representative loop retains both orders and diagonal pairs.

The raw records support 1,260 checks, zero failures/exceptions, and parent/worker exits 0. Structured record checks confirm exactly 255 consecutive identity rows N=2,…,256 and 271 used Liouville arguments. The N=10 values and five listed ordered pairs agree with direct sign arithmetic. At q=37, 73 is prime, 70=2·5·7, 68=2²·17, whereas 9=3² and 65=5·13; the claimed failed and successful positive-pair examples are consistent. The m=1304 records test exactly k=1,…,7; the successful pair 98=2·7² and 2510=2·5·251 has two negative signs and sum 2608.

This is bounded non-Lean evidence only. The sieve bound 2608 is not a target-verification range. Failed selected templates do not refute representation existence. The historical correspondence of the computational “PB three-test” label to its dispatch remains unestablished in the supplied packet, exactly as disclosed; this review does not resolve that label obligation. None of these data are needed for the universal partial proofs in §3.

## 8. Open obligations, verdict scope, and next action

No additional load-bearing gap was found in the **claimed partial results**. The original unconditional conclusion is nevertheless still missing. One equivalent remaining obligation is

```lean
∀ N : ℕ, Even N → 2 < N →
  2 * ArithmeticStatement.L (N - 1) - ((N : ℤ) - 1) <
    ArithmeticStatement.C N
```

Alternatively it is

```lean
∀ p q : ℕ, Nat.Prime p → Nat.Prime q →
  ArithmeticStatement.HasRepresentation (2 * p * q)
```

Neither universal proposition is proved. PB and LS remain unproved optional sufficient premises; O-M5 in its stated form is false. No effective sufficiently-large threshold plus complete remaining-case proof has been delivered. The equivalences, partial families, context paper, finite evidence, and successful partial-module compilation do not remove this obligation. There is no counterexample to the original Target in this packet.

**Recommended next action:** the leader should retain this exact snapshot as an accepted partial development, keep Target unresolved, and route either explicit universal obligation back to mathematical development. Any eventual completion requires the faithful Target theorem, its actual Lean checking and dependency audit, and fresh review of the changed integrated snapshot. No repair of this partial argument is required by this review, and no global success declaration is warranted.
