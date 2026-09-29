# Independent certification review B — exact final snapshot

**Mode: CERTIFICATION. Overall verdict: UNRESOLVED for the original request.**

The supplied argument establishes the stated partial results and reductions, not the requested universal theorem. I found no mathematical defect in those partial deductions or an undisclosed assumption that purports to finish the theorem. Its explicit incomplete status is accurate. This is not a counterexample to the conjecture and is not a certification of success under `request.md`.

`P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`.
All problem-relative paths below use this prefix. The only output of this review is `P/nl/reviews/final-review-b-v1.md`.

## 1. Snapshot identity and review boundaries

Recomputed SHA-256 values:

| Artifact | SHA-256 |
|---|---|
| `request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `FINAL_ARGUMENT.md` | `1b93364b818b0eae95875d391ca6f944614f00b963a1e384ba1a0fe2533957a9` |
| `lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `sources.md` | `9df552348f03fd84ffe0e203f1340f26e6a902f8424f924068fe6fb86c1a7dbb` |
| `knowledge/mangerel-v2/paper.pdf` | `ae26a659220985c55576a18d05a84d5a56988024f8781ae4ccbe04847ac16505` |
| `formal/integration/audit-v1.json` | `4d32b5248d82c827edcb958ecd63ea62d68504bedf9fb396aa56edbcc7ca4db3` |

All supplied hashes match. All 15 entries of `FINAL_ARGUMENT.md` §11 were also independently hashed and match its table. Hashing the excluded files in that table was strictly an identity check, not reading or accepting their contents.

### Inputs actually examined

- The required `.clawcodex/skills/math-team/references/protocol.md`, the original request, the complete standalone final argument, and both supplied Lean files.
- `lean/Statement.lean`, `lean/Statement/{Scaffold,Smoke}.lean`, `lean/{lean-toolchain,lakefile.toml,lake-manifest.json}`.
- Pinned Mathlib source portions listed in §7 below, including the factor-list definition and multiplication theorem, ordinary primality/evenness definitions, parity, interval cardinality, and finite-sum transport/distribution.
- `sources.md`; `formal/environment/public-availability-witnesses.json`; preserved `public-ci-{mathlib,lean,plausible,LeanSearchClient,importGraph,proofwidgets,aesop,Qq,batteries,Cli}.{json,stdout,stderr}`. Large raw JSON responses were also examined by structured field extraction/comparison.
- The allowed integration audit's identity, source-scan, version, provenance, import-resolution, endpoint and artifact fields; raw command records and outputs for `v1-00`, `v1-01`, and `v1-04` through `v1-09`, including both stdin files. The trust-zero stdout was checked byte-for-byte equal to the direct stdout already read; stderr hashes establish empty contents.
- Mangerel PDF **pages 1–3 only**, and `knowledge/mangerel-v2/arxiv-metadata.txt`.
- `nl/code-executor/finite_certify.py`, `run.json`, `run.log`, and selected `evidence.json` fields covering definitions, counts, scope, exceptions, examples and limitations. I did not independently re-exhaust its entire arithmetic table.

No other NL proof, review report, task board, author-confidence material, integration prose or source-proof map was opened. References in the candidate were not followed into those artifacts. An integration summary-status string incidentally surfaced while locating fields in the expressly allowed audit JSON; it was disregarded, not used as evidence. No agent was spawned, no network source was accessed, and neither Lean builds nor the finite arithmetic suite were rerun. Fresh mechanical work comprised hashes, record comparisons, and local Mathlib revision/cleanliness inspection. Mathematical checks below are independent reasoning, not conclusions inherited from status labels.

## 2. Target fidelity, definitions and nonvacuity

The literal definition is

`∀ N : ℕ, Even N → 2 < N → ∃ a b : ℕ, 0 < a ∧ 0 < b ∧ N = a+b ∧ lambda a = -1 ∧ lambda b = -1`.

- `Even N` is the ordinary `∃ m, N = m+m`, not a restricted predicate. `N=4` satisfies the hypotheses, so they are nonvacuous.
- Since every integer in the request has `N>2`, and both witnesses must be positive, passage to natural representatives loses no integer case. This is a mathematical normalization; the module does not claim an additional Lean integer/natural transport theorem.
- `omega` is the **length of a list**, not the cardinality of a set of prime divisors. The pinned recursion repeatedly removes a least prime factor. Prime entries, product recovery and uniqueness give the required multiplicity convention, including prime powers. No coprimality assumption appears in the multiplication theorem used.
- The empty list at 1 gives `omega 1 = 0`, hence `lambda 1 = 1`. The codomain is `ℤ`, so `-1` is genuinely negative.
- Both witnesses are explicitly positive. No distinctness, oddness, primality or coprimality restriction was added. Diagonal witnesses are intentionally used.
- The formal extension to 0 is irrelevant: every factor/sign application and every counting index used in the proof is positive. The unused positivity binder in `lambda_sign` is not a vacuity device.
- `HasRepresentation` unfolds to exactly the witness predicate in `Target`. The root imports the actual partial module. `UnfinishedScaffold.mk` requires a proof of `Target`; neither its declaration nor its projection manufactures one.

**Finding:** the statement and conventions are faithful; the missing issue is proof, not target drift.

## 3. Load-bearing mathematical checks

Here `Partial` means the supplied `lean/Statement/Partial.lean`; references to final-argument sections refer to the standalone candidate, not its cited predecessor.

| Step | Independent check and scope |
|---|---|
| Signs and multiplication — §2; Partial 43–96 | Parity of the natural exponent gives precisely ±1. Factor-list concatenation preserves length with only nonzero-factor hypotheses, supplied by positivity. Thus complete multiplicativity, prime signs, doubling and square signs follow. Repeated prime factors cause no exception. |
| Scaling — §3; 102–122 | The same positive multiplier sends witnesses to `da,db`, preserves positivity and changes each sign to `lambda d * s`. The special sign rule uses `s∈{1,-1}`; it is not asserted for arbitrary integers without that hypothesis. |
| Diagonal — §3; 124–137 | For `N=2m>2`, `m>1`. If `lambda N=1`, doubling gives `lambda m=-1`; `(m,m)` is admissible. The extra sign hypothesis is visibly confined to this partial family. |
| Two-sign seed — §3; 139–159 | The signs of a positive multiplier exhaust two cases. The seeds `8=3+5` and `8=4+4` therefore yield respectively `(3m,5m)` or `(4m,4m)`. Both sums are `8m`; no assertion about all other even integers follows. |
| Interval and reflection — §4; 161–213 | For `a∈I_N`, `0<a<N` gives `0<N-a<N`, `a+(N-a)=N`, and `N-(N-a)=a`. Hence reflection is an involutive bijection. The finite-sum transport theorem receives both membership and inverse conditions. `N≥2` supplies the cast guard for `(N-1 : ℕ)` and the interval endpoint. |
| Ordered count — §4; 215–250 | Positive coordinates summing to `N` automatically lie below `N`. The map `a↦(a,N-a)` is onto the filtered ordered-pair set and injective by its first coordinate. Consequently `R=|F_N|` is proved, not silently assumed. A non-diagonal pair has two orders; a diagonal has one. There is no division by two. |
| Indicator and expansion — §4; 252–289 | For each of the four sign pairs, `4δ=(1-lambda a)(1-lambda b)`. Summing gives `|I_N|-Σlambda(a)-Σlambda(N-a)+C(N)`. Reflection identifies both middle sums with the **inclusive** `L(N-1)`. Thus `4(R:ℤ)=(N:ℤ)-1-2L(N-1)+C(N)`. All signed operations and casts are correct. Natural index subtractions are guarded, not used as signed arithmetic. Evenness is unnecessary here. |
| Positivity and strict margin — §4; 291–327 | Nonempty ordered pairs are equivalent to `R>0`. Since `R` is a natural count, `4(R:ℤ)>0` is equivalent to `4(R:ℤ)≥4`. Rearrangement yields exactly `2L(N-1)-((N:ℤ)-1)<C(N)`, with the correct strict direction. Nonnegativity alone is insufficient. Both universal implications retain `Even N` and `2<N`. |
| Two prime occurrences — §5; 329–360 | For `m>1`, product recovery excludes an empty factor list. `lambda m=1` excludes a singleton. Removing the first two occurrences yields primes `p,q` and tail product `d`; product recovery and `m>1` force `d>0`. Multiplicativity then gives `lambda d=1`. Neither `p≠q` nor `d>1` is required: `p=q` and an empty tail `d=1` are both covered. |
| Prime-product equivalence — §5; 362–386 | Forward: primes are ≥2, so `2pq≥8>2` and is even. Reverse: write arbitrary admissible `N=2m`. The negative sign of `m` gives the diagonal. The positive sign gives `m=d(pq)` and scales a **hypothesized** core representation by positive `d` with sign +1. This exhausts the sign cases. Primes equal to 2, equal primes, and repeated factors in `d` cause no incompatibility. |

No circular use of `Target` occurs: its appearance in the forward directions of equivalences is an explicit assumption discharged by implication introduction. The reverse directions depend on the other side of the equivalence, not on an already asserted endpoint.

### Prose-only conditional and rejected routes (§7)

These deductions are not additional Lean theorems, and the document correctly says so.

- **PB ⇒ Core:** a prime at least 5 supplies the positive-sign pair; multiplication by the other prime reverses both signs. If both primes are below 5, their possible values are 2 and 3, giving cores 8, 12 and 18. The stated pairs `(3,5)`, `(5,7)`, `(5,13)` are valid. The small primes used here meet the usual divisor test. This does not establish PB.
- **Even-even positive pairs at `2q` iff `G(q)`:** doubling negative summands and halving positive even summands are inverse constructions, with positive halves and the sign flip justified. Applying this to odd prime targets would require a new assertion, not `Target`'s even quantifier.
- **Failed `G(q)` implies `L(q-1)≥0`:** reflection takes every negative index injectively into positive indices, since a second negative sign would be a forbidden representation. Sign dichotomy and the partition of the interval give the claimed cardinality difference. Thus the strict-negative-sum condition is sufficient, not necessary.
- **O-M5 counterexample:** 5 is prime and at least 5, while `L(4)=1-1-1+1=0`. This genuinely refutes that universally strict condition. It does not refute PB or the target; `5=2+3` has negative signs.
- **Three PB templates at 59:** 59 is prime (no divisor among 2, 3, 5, 7). The displayed factorizations of 57, 56 and 117 have respectively 2, 4 and 3 prime occurrences. The three proposed pairs therefore have signs `(+1,-1)`. Conversely 14 and 104 have 2 and 4 occurrences, giving the claimed positive-positive pair at 118. This is only a failure of those templates.
- **LS ⇒ Target:** when `lambda(m-t)=1`, doubling `t,m-t` gives two negative signs. Otherwise positivity of `m-t` and dichotomy force its sign to be negative, and the LS disjunction then supplies `lambda(m+t)=-1`. The bounds on `t` ensure positivity in both branches and both sums are `2m`. The uniformly quantified LS premise is not proved or claimed equivalent to the target.

The displayed partial proofs and conditional deductions are mathematically coherent as written. No repair has been supplied by this review.

## 4. Source and dependency audit

### Pinned library

The local Mathlib checkout reports commit `905b95818eb32af7874a58b427f50c1711a5e96c`; the tracked-source cleanliness check returned no changes. Its factor-list multiplication theorem requires exactly `u≠0` and `v≠0`. All uses in the candidate meet these guards, including tail product 1 and repeated primes. The finite-sum theorem requires a bijection on the finite domains, which the local reflection lemmas establish. Integer ring and finite-set operations introduce no analytic hypothesis.

The manifest has nine exact package revisions. Although some upstream `inputRev` labels say `main` or `master`, the resolved `rev` values are immutable hashes. I compared all nine, and the recorded Lean commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`, against the preserved raw CI responses and the availability-witness file. For each, the response contains an exact matching `head_sha`, a nonprivate repository, and a workflow creation date before 2026-08-01. The selected witness fields agree with the raw records and their recorded hashes. In particular the Lean and Mathlib exact-SHA witnesses are dated 2026-07-28. The remaining package witnesses are in February or July 2026.

This supports cutoff eligibility of the pinned versions on the supplied provenance record. It is not a new online provenance inquiry, a rebuild of every dependency, or authentication independent of the preserved records. A workflow's success/failure is not being used as a mathematical theorem or as the criterion for public availability.

### Mangerel v2: context only

The PDF version stamp and preserved metadata identify **arXiv:2404.12117v2, 2 May 2024**, with metadata time 14:48:54 UTC. This version is eligible.

Direct inspection confirms:

1. Theorem 1.2 (p.1) states eventual `|C(N)|<N-1` for every `N` above a threshold, not merely almost all `N`.
2. Remark 1 (p.2) explicitly calls the threshold ineffective and identifies reliance on Siegel's theorem.
3. Remark 2 (p.3) asks the exact negative-negative representation question for even `N≥4` and says the methods appear too rigid to address it directly.
4. The hypothetical stronger estimate and the printed off-by-one/strictness issue are accurately distinguished from established project input. The exact zero identity has `N-1`; the later printed inequality with `N` and strict `>` is not an immediate consequence of it. The candidate adopts neither this display nor a repair.

Non-extremality of the product correlation does not select two negative signs rather than two positive signs. The paper supplies neither the missing pointwise inequality nor a usable effective finite-remainder argument. Its proof and its cited analytic literature are not imported dependencies and were not audited beyond the allowed pages. No claim about the complete literature through July 2026 follows.

The excluded later MathOverflow snippet is disclosed in the permitted ledger; its body was not opened or used here. No later mathematical source was consulted by this reviewer.

## 5. Recorded Lean evidence versus this review

The compiler records bind the exact current `Partial`, `Definitions`, root and configuration hashes to the integrated snapshot. I recomputed the raw output hashes and checked their command-record digests. The recorded commands, all in `P/lean`, are:

| Command | Recorded exit | Evidence prefix in `formal/integration/` |
|---|---:|---|
| `lake build` | 0 | `v1-04-default-build` |
| `lake build Statement.Partial` | 0 | `v1-05-partial-build` |
| `lake env lean Statement/Partial.lean` | 0 | `v1-06-partial-direct` |
| `lake env lean -t 0 Statement/Partial.lean` | 0 | `v1-07-partial-trust-zero` |
| `lake env lean --stdin` with root-check stdin | 0 | `v1-08-root-import-check` |
| `lake env lean --stdin` with endpoint-check stdin | 1, expected | `v1-09-absent-endpoints` |

The default build output explicitly says it built `Statement.Partial` and root `Statement`, completing 925 jobs. The later named-module build is a replay, not a second fresh compilation; direct and trust-zero checks are separately recorded. The root-check input checks the 50 added declarations, and its output matches the actual types, including ordered `R` and the guarded equivalences.

The direct output reports the standard set `{propext, Classical.choice, Quot.sound}` for all 42 local theorems and 11 local/base definitions. The 29 upstream queries use subsets of that set. The root output agrees; the trust-zero output is byte-identical to the direct one. The local proof bodies contain no `sorry`, `admit`, custom axiom, or native-evaluation proof shortcut. Four unused-variable lints are exactly those disclosed at lines 51, 171, 187 and 291.

The endpoint-check input imports `Statement`; its two output diagnostics are genuinely `Unknown identifier` for `ArithmeticStatement.pointwise_keystone` and `ArithmeticStatement.liouville_goldbach`. They prove absence of those names, not a proof of their planned types. Inspection of the complete local modules also reveals no differently named inhabitant of `Target`. `Smoke` evaluations are not proof terms for it.

**Scope:** these are actual preserved Lean outputs reviewed for consistency, not Lean executions performed by me. The trusted boundary includes the pinned Lean implementation/kernel and installed dependency artifacts. This LLM review is not Lean kernel verification and does not strengthen the recorded checks into a from-source rebuild of every upstream library.

## 6. Finite evidence and exact remaining obligations

### Finite evidence

The program uses exact integer arithmetic, a prime-power sign-flip sieve, and trial-factorization cross-checks; it does not derive `R` from the identity it tests. The ordered enumeration retains both orientations and the diagonal. The loop bounds are exactly `N=2,…,256`, 255 identity instances, plus the specified examples. The category totals add to the recorded 1,260 checks; the records show no failures or exceptions and worker/parent exits 0.

The stated `N=10` data are consistent: the five listed ordered pairs give `4R=20`, and `9-2(-1)+9=20`. The raw q=37 and m=1304 entries match the exposition's explicit examples. The sieve bound 2608 and the 271 used Liouville arguments do **not** establish the target up to 2608, much less universally. The unresolved PB-label attribution in the executor record remains an ancillary reporting limitation, not a mathematical premise accepted by this review. These data are not used to justify any universal lemma in §3.

### Break points preventing full certification

1. **No universal strict positivity step.** `FINAL_ARGUMENT` §4 ends with an equivalence. It does not prove, for arbitrary even `N>2`,
   `2 * L (N - 1) - ((N : ℤ) - 1) < C N`.
   Neither the identity nor nonnegativity of a count supplies strict positivity.
2. **No universal core construction.** §5 proves `Target ↔ Core`, but its reverse direction explicitly assumes
   `∀ p q : ℕ, Nat.Prime p → Nat.Prime q → HasRepresentation (2*p*q)`.
   This premise remains unproved, including its unbounded quantifiers. The reduction itself is sound.
3. **No completed Lean endpoint.** The types displayed in §6 are specifications of work still required, not active discharged goals or theorem declarations. The recorded environment lacks the planned endpoint names. There is no fully checked inhabitant of the exact `Target` proposition.
4. **No substitute eventual-plus-finite proof.** No effective threshold and rigorous coverage of every remaining admissible case are given. The paper's different ineffective conclusion and the finite Python tests cannot fill that role.
5. **Optional routes are still optional premises.** PB and LS have valid sufficient-direction arguments, not universal proofs. O-M5 is genuinely false. These facts leave the original statement unresolved, not false.

These are substantive missing mathematical/formal obligations, not formatting problems or mere library-infrastructure failures. They are disclosed, not disguised as theorems. I found no additional defect requiring rejection of the established partial content.

**Recommended next action:** the leader should retain this delivery as partial progress, not declare the original request complete. Route one of the universal obligations in items 1–2 (or a genuinely complete alternative) back to mathematical development; only after such a proof exists should the exact Lean endpoint be built and its transitive axioms and integrated snapshot reviewed afresh. This review supplies no repair or proposed proof of those obligations.

## 7. Supporting identity inventory

Hashes below were independently recomputed. The protocol path is relative to the repository root; other paths use `P` unless a prefix is specified.

| Input | SHA-256 |
|---|---|
| `.clawcodex/skills/math-team/references/protocol.md` | `e712830b3febe6e3fcaf0479c7aa9fc30f23aa4fcc5e1f45088f736f9c161f2b` |
| `lean/Statement.lean` | `426a0b62a141387e22f0e5481a705e3ffe3d64e0f8ad100daea3101c802e8458` |
| `lean/Statement/Scaffold.lean` | `0bd0952096ebf027fa956458dfb1c1bb08e6396cd89c77b24a3eaadbe1070d1a` |
| `lean/Statement/Smoke.lean` | `50fcf1606d7bf7c52cf84cc7ebc60f0e05a151745339f295c86c1a37ffab8e19` |
| `lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |
| `formal/environment/public-availability-witnesses.json` | `051de67ee5bfd81242942075cf9dabacd8cfa96b74abf3733b025456694cc4c1` |
| `knowledge/mangerel-v2/arxiv-metadata.txt` | `8a1d1b2d965215664c00abbbf02af8d72ff72947e3443698b767eb7607059771` |
| `nl/code-executor/finite_certify.py` | `00a9d66bd81ca58e5cf0148fba6fa5b742c6a3285c82f46d5a1e3952aeab98f5` |
| `nl/code-executor/evidence.json` | `b42b9544e632431476c872b5696679d2908f05858737f6718f7d8c5a626fd72e` |
| `nl/code-executor/run.json` | `7ec4412954f806dffb7423c85b5f6a50d54dd1256998dc3bb407940107cf6593` |
| `nl/code-executor/run.log` | `656020dc378a129bf6f4800f153728e8fcbc8c4ca2b2b9348a917c6447a5da11` |

### Library source actually examined

Prefix: `lean/.lake/packages/mathlib/Mathlib/`. The ranges describe content read, not a claim to have audited every transitive library proof.

| Path and portions | Whole-file SHA-256 |
|---|---|
| `Data/Nat/Factors.lean`, 1–205 | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `Data/Nat/Prime/Defs.lean`, 1–65 and primality/minimum-bound statements around 72–128 | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `Algebra/Group/Even.lean`, 1–80 | `1180fa9ac282e55257e95c8402acd7314fcbd0a18bcfdede92a3cde16e1db630` |
| `Algebra/Ring/Parity.lean`, 375–404 | `c710e4b51d5ffc9df4e2cc16bad357ab152b1ae5ff05e8fb68a1e3812e6a3b68` |
| `Order/Interval/Finset/Nat.lean`, 65–94 | `e1a7b1cf7d86209af1d6f894e05f2a4cc40997840ff64461d98476fcd5e248e2` |
| `Algebra/BigOperators/Group/Finset/Defs.lean`, 490–518 | `562dacf916c63c599b7c4becbf3bafdbb7fa0b493eb2f6e594f4126a6d91e62c` |
| `Algebra/BigOperators/Ring/Finset.lean`, 45–69 | `472cd5000412d8ec35c8b9ee919b2aeedbf0a830033a55009aad436595923809` |

### Compiler record identities

Prefix: `formal/integration/`. Each JSON contains the command, working directory, exit status and raw stdout/stderr hashes; those raw hashes were recomputed and matched. All eight stderr files are empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Record | JSON SHA-256 | stdout SHA-256 |
|---|---|---|
| `v1-00-lean-version` | `d056059d022243219a5bcfd6d9f65dbfc071de8ca14978d87eb0bd79acd80cbd` | `562cd1632273e7efc3f67a6754fa51bd59ec9cf369d6d9bf1d6472593ba5d8b4` |
| `v1-01-lake-version` | `ebb63e80d5878f06a8a2b4868cd4202581ac32e1f6c16ddbe1c2279ec959b03b` | `0feab4bdc383edf5478cd0d049548ba465e87c1446360527c0e8e7f6ff137c73` |
| `v1-04-default-build` | `c3d9786b6e31e46895b8af5e2709607ef19c03fbc419a618750b982136721dfb` | `8409d3cdd555c3d8173b495547033298258ca2089eea5b1ed0ed7cb7ff43b0c1` |
| `v1-05-partial-build` | `6bf5780a4fe5d0cd376bfb13daa509eb6533fe610337b72970466e1794ed913a` | `63105f63cf9927d0670210b44f6cfd8485c66abe7f809d663ec7b1f804005903` |
| `v1-06-partial-direct` | `406c96c5a5054f7f76baaf39ec58df0b2d9aae3ce5bb73775f77fbffeda593dd` | `6569201315dbd4f85bb46b3a1325837b33029f1cfc742252ab335188aab030b9` |
| `v1-07-partial-trust-zero` | `eb974c333e93a39f1d6d2547cdf2ee0dc0de75a775326aed496f9289b6065680` | `6569201315dbd4f85bb46b3a1325837b33029f1cfc742252ab335188aab030b9` |
| `v1-08-root-import-check` | `151b02c02552b59c6620616e4dd0cd6d7fe5806a7b8670ae0c0b5d54478ec495` | `a4c33f9b1f6b2e91d84c3dc06192f0b60a566050a355de2e9ac4c2af621621c1` |
| `v1-09-absent-endpoints` | `ae628ce7832805c7656ab4e0822f7bf71bc468cf5768626261e56c102fc5b87e` | `8e8f8e11e2b7324c752c36ea5a992f19f999656b89a7a1fafd8eb1c07105e590` |

The two stdin files are `v1-08-root-import-check.stdin.lean`, hash `c01f72503302b7917c7c2e1b44aeee9a9cfa92eeff5871bde16535de63241120`, and `v1-09-absent-endpoints.stdin.lean`, hash `0314a0c6994f5bd1ea17d69de15457c10eae9b2231dab38ac401a5f3317c7bd8`.

### Public-availability raw records

Prefix: `formal/environment/public-ci-`; each row names the stem before `.json` and `.stdout`. Recorded stderr files are empty with the same empty-file hash above. All command records report exit 0.

| Stem | JSON SHA-256 | stdout SHA-256 |
|---|---|---|
| `mathlib` | `bc12929af93d0eafc008d4d56e287842ef6f682d797b6bb50e7f1481d6f0eeba` | `4337fdc10284dc0c90165a0e4926fde19ebb6ce78dfef2505a3112a277452e00` |
| `lean` | `ab20b13c1a5bd4b511a1c4b32e4b8b5c2a4576c59520c72aa713837c4f3c9272` | `aeaea1b78e78521606c013a4fafc4b9c0bcaae068cd63f6e97a57bbd26a43826` |
| `plausible` | `347c5dd0c0a457c264730b4204e873dd2f119f1c4a290932a7a4cfefce8f011f` | `7db3a5d1c95ca7d1b1906ec25958d6f1d490a9953154fdf3180f09fd57195e7b` |
| `LeanSearchClient` | `36e3a9858cb8c504781881b8c18bc33e0e8cc13e5773674df19cbbd698dde1d4` | `3abdd2daec49091e23e2601a2d77322759da75c6967c6ef67d76cd806ad2d5af` |
| `importGraph` | `79420d8fc87b7aa6a6adaae2036a59291a7a32e5b1ed6589594b0a489b12056b` | `5551743d19c9b24dc50743a216975cc324b4bb94618b36fd2839785fbc5fb575` |
| `proofwidgets` | `d999f8dbb5e943a1c5ed884db326d0a1808eab552d0ce0a6945c2adefc6fbc95` | `0af1983970539258f9627cde04d59047e20557b9b5d39248ae2018f728f2cce6` |
| `aesop` | `f955e0be176664bc65cf81b19f2b9c04a37c3d80d6e0bfb188f88de5511362bf` | `83bc912b7caf04c68210490e75285c2eba39396aad9cad151c68f2322a36c06d` |
| `Qq` | `85ff62d3ed47b5a6434b9021748ebba431ae8602086f2d850c2ec88c384fb7b3` | `e8ff8f4e5970e6943179a83cc2be235f3296ef5153f1d550a3dabf86e69a575b` |
| `batteries` | `bed0b1b5d11fe06fa133b85679b3d6b60ea0e475862af03aa1374d9d75761264` | `3bb8ca7972a48ad427bab042620fed56c5a2a71813ec02621723647adc7fa741` |
| `Cli` | `b2ffee0bba69c9a019afe0f7a97d4b9f32ea1942935d4c2f0f39397195b15460` | `7db04e1305e996408659d75f8c28ea7d2c4415dcb337834ec3c93a4ee7b36844` |

### Excluded contents hashed only for §11 identity validation

| Path | SHA-256 |
|---|---|
| `nl/generator/proof-v2.md` | `bdcf57b670ed1e1410bacad5a2f9182c565add056714ef85e0155f939a6b7735` |
| `formal/integration/integration-report-v1.txt` | `0f008c380573638e8b52796e8252eda83ee5e1eb79fd7a0caed6ef58a81984f7` |
| `formal/integration/source-proof-map-v1.txt` | `98fe3ef1958403c629e55d0a97fff50f5b2270c3e157e0e8f08664675888e977` |
| `REPRODUCE.md` | `cb982a4687549930a398cec4b3d81449ebec7cd0bb2eb9ed8fc75f8d30e301c0` |
| `nl/searcher/extraction-v2.md` | `787e83caae80656c7874f2a1e133f57e88dfcbde60a88b3d3b2e78653a954a6f` |
| `nl/code-executor/report.md` | `9df3e8eef714c3e16ebaa76e336b726eca1d36c15c63257869da9696e32e4ba4` |

**Final scope:** the exact snapshot is a sound, candid partial development on this review. The original unconditional all-even theorem and its fully checked Lean endpoint remain **UNRESOLVED**.
