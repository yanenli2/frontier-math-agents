# Final review A, v1

Mode: CERTIFICATION.

P = `.clawcodex/math-team/problems/liouville-goldbach-jul2026`.

## 1. Scoped verdict

**Full review-packet verdict: UNRESOLVED.** Two nonmathematical qualifications prevent an unqualified exact-snapshot/fresh-review certification: the cited `sources.md` no longer has the candidate's recorded identity, and reading the referenced proof source unexpectedly exposed embedded historical review metadata. Details and corrective routing obligations are in §7.

**Mathematical assessment of the partial argument:** no load-bearing mathematical error or unfilled step was found in the claimed unconditional partial results, counting equivalences, prime-core equivalence, or expressly conditional PB/LS deductions. The integrated declarations match those claims. This assessment does not discharge the packet qualifications.

**Original-request verdict: UNRESOLVED, not success.** Neither the universal strict inequality nor the universal prime-core assertion is proved. No theorem of type `ArithmeticStatement.Target` is supplied. The exposition correctly identifies this boundary. Nothing reviewed establishes that the original statement is false.

This is an LLM mathematical review and an inspection of preserved compiler evidence, **not a new Lean kernel verification**. No Lean command or finite arithmetic test was rerun, no candidate was repaired, and no team/task/agent operation was performed. Only this assigned report was written.

## 2. Exact identities and inputs

The following digests were recomputed locally. The three assigned candidate hashes matched both initially and immediately before reporting.

| Path relative to P | SHA-256 |
|---|---|
| `request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `FINAL_ARGUMENT.md` | `0481eb74c5d954d3cb24b0ab696dcb588f24e0d4e8b5974140babfa14627d76d` |
| `lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `nl/generator/proof-v2.md` | `bdcf57b670ed1e1410bacad5a2f9182c565add056714ef85e0155f939a6b7735` |
| `lean/.lake/packages/mathlib/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `formal/integration/audit-v1.json` | `4d32b5248d82c827edcb958ecd63ea62d68504bedf9fb396aa56edbcc7ca4db3` |
| `formal/environment/public-availability-witnesses.json` | `051de67ee5bfd81242942075cf9dabacd8cfa96b74abf3733b025456694cc4c1` |
| `knowledge/mangerel-v2/paper.pdf` | `ae26a659220985c55576a18d05a84d5a56988024f8781ae4ccbe04847ac16505` |
| `knowledge/mangerel-v2/arxiv-metadata.txt` | `8a1d1b2d965215664c00abbbf02af8d72ff72947e3443698b767eb7607059771` |
| `nl/code-executor/finite_certify.py` | `00a9d66bd81ca58e5cf0148fba6fa5b742c6a3285c82f46d5a1e3952aeab98f5` |
| `nl/code-executor/evidence.json` | `b42b9544e632431476c872b5696679d2908f05858737f6718f7d8c5a626fd72e` |
| `nl/code-executor/run.json` | `7ec4412954f806dffb7423c85b5f6a50d54dd1256998dc3bb407940107cf6593` |
| `nl/code-executor/run.log` | `656020dc378a129bf6f4800f153728e8fcbc8c4ca2b2b9348a917c6447a5da11` |
| `sources.md`, current file | `9df552348f03fd84ffe0e203f1340f26e6a902f8424f924068fe6fb86c1a7dbb` |

Inputs read: the protocol at root `.clawcodex/skills/math-team/references/protocol.md`; the request and complete assigned exposition/Lean files; the referenced `proof-v2.md`; `Factors.lean` lines 1–205; the PDF's printed pages 1–3 and version metadata; selected raw audit fields and command outputs; the public-availability witnesses; the finite Python script, run records, and relevant evidence fields/rows; and the root Lean module, Scaffold, Smoke, toolchain, Lake configuration and manifest. Only the relevant citation/exclusion lines of the current source ledger were inspected. Printed upstream definitions/signatures and axiom outputs were also inspected.

Additional inspected build-input identities:

| Path relative to P | SHA-256 |
|---|---|
| `lean/Statement.lean` | `426a0b62a141387e22f0e5481a705e3ffe3d64e0f8ad100daea3101c802e8458` |
| `lean/Statement/Scaffold.lean` | `0bd0952096ebf027fa956458dfb1c1bb08e6396cd89c77b24a3eaadbe1070d1a` |
| `lean/Statement/Smoke.lean` | `50fcf1606d7bf7c52cf84cc7ebc60f0e05a151745339f295c86c1a37ffab8e19` |
| `lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |
| `lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |

A read-only SHA-256 comparison of all 15 rows in `FINAL_ARGUMENT.md` §11 found 14 matches and only the source-ledger mismatch. The integration prose report, source-proof map, REPRODUCE, literature extraction, and code-executor prose report were hashed for that comparison, not read as acceptance evidence. No prior-review file was opened. See §7 for the inadvertent embedded-metadata exposure.

## 3. Target and mathematical step checks

All `Partial` line references below refer to the exact assigned integrated hash.

1. **Definitions and domain fidelity (Definitions:6–14; exposition §1).** `primeFactorsList.length` counts occurrences, not distinct prime values. The pinned list definition, its prime-entry/product properties, and its concatenation-permutation multiplication theorem support precisely this interpretation. The list at 1 is empty; hence Ω(1)=0 and λ(1)=1. The codomain is ℤ, so −1 is not truncated. `Target` has the required universal N, evenness and strict lower bound before its existential positive witnesses. It imposes no primality, parity, coprimality or distinctness restrictions on them. Every integer N>2 and every positive integer witness has a unique natural representative; addition, order and positive factorization agree. Conversely natural witnesses coerce to integer witnesses. Thus the Nat normalization loses no original case. The candidate expressly does not claim a separate Lean Int/Nat transport theorem.

2. **Sign and multiplicative arithmetic (Partial:43–96).** Natural exponent parity exhausts the two integer signs. Length preservation under `Nat.perm_primeFactorsList_mul` gives Ω(uv)=Ω(u)+Ω(v), and `pow_add` gives λ(uv)=λ(u)λ(v). That upstream theorem requires only u≠0 and v≠0, obtained from the stated positive hypotheses; there is no hidden coprimality premise. Singleton prime lists give the prime signs; doubling, λ(4)=1 and positive-square signs follow. Repeated prime factors are retained. All downstream multiplicative uses satisfy positivity. The unused positivity parameter of `lambda_sign` does not create vacuity or an extra assumption.

3. **Scaling and explicit families (Partial:102–159).** Scaling uses the same positive multiplier on both witnesses, preserving their sum and multiplying both signs by λ(d). For s=±1 and λ(d)=−s the result is −s²=−1. At even N>2, N=2m gives m>1; λ(N)=1 forces λ(m)=−1 and legitimizes (m,m). The seeds 8=3+5 and 8=4+4 cover both possible multiplier signs, giving (3m,5m) or (4m,4m) for every m>0. These are unconditional statements for their stated families, not coverage of every admissible even N.

4. **Intervals, reflection and casts (Partial:161–213).** With N≥2, `I N = Ico 1 N = Icc 1 (N−1)`. Membership ensures 0<a<N and 0<N−a<N; hence natural subtraction is exact and reflection squares to the identity. Its injectivity and surjectivity supply the finite-sum reindexing. `Nat.cast_sub` has 1≤N available, so the integer cardinality is `(N:ℤ)−1`. Both direct and reflected sign sums equal L(N−1). None of these uses λ(0), and evenness is unnecessary.

5. **Actual ordered count (Partial:215–250).** The code genuinely defines R as the cardinality of a filtered product of two intervals. Positivity and N=a+b imply both coordinates lie below N, so these interval restrictions exclude no original witness. The map a↦(a,N−a) is bijective between the negative-sign index set and the ordered-pair set; first-coordinate projection proves injectivity and provides the inverse. This proves, rather than assumes, equality with the prose source's index count. Off-diagonal orders are separate; the diagonal is counted once. No factor of two is lost.

6. **Indicator and identity (Partial:252–289).** The four sign cases give `4δ=(1−λ(a))(1−λ(b))`. Summing the filtered indicator is the integer cast of the actual count. Expansion and reflection give exactly `4(R(N):ℤ)=((N:ℤ)−1)−2L(N−1)+C(N)`. Every summand has positive arguments. The sign arithmetic and exterior subtraction are in ℤ; the only natural subtractions are bounded indices. This is valid for every N≥2, including odd N and the boundary N=2.

7. **Existence and strict equivalences (Partial:291–327).** Positive finite cardinality is equivalent to a witness, in both directions. Writing K for the integer right side, K=4r with r the nonnegative integer cast of R. Thus R>0 iff K>0 iff K≥4. Rearrangement gives `2L(N−1)−((N:ℤ)−1)<C(N)` with the displayed strict direction. The universal equivalence retains `Even N` and `2<N`; these imply every intermediate N≥2 precondition. K≥0 alone supplies no existence result. These are equivalences, not proofs of the equivalent universal assertion.

8. **Two prime occurrences and core equivalence (Partial:329–386).** For m>1 with λ(m)=1, the factor list is neither empty (its product would be 1) nor singleton (its sign would be −1). Removing its first two occurrences supplies primes p,q and positive tail product d. The product identity gives m=d(pq), and complete multiplicativity gives λ(d)=1. Equal values p=q are allowed: these are occurrences, not distinct primes. Empty tail gives d=1 and is not excluded. Target implies Core since primes are at least 2, so 2pq≥8 and is even. Conversely write arbitrary admissible N=2m. The negative m case is diagonal; the positive m case scales the hypothesized core witnesses by this same d. All cases, including prime 2, equal primes and d=1, survive. Core is discharged into an implication, not assumed as an unconditional theorem. No circularity was found.

9. **Conditional/exploratory prose (exposition §7).** PB⇒Core correctly scales a positive pair at 2q by the other prime; when both primes are below 5 the possibilities 2,3 give exactly the cores 8,12,18, with the stated pairs. The even-even positive bridge at 2q is equivalent to a negative pair at q by doubling/halving positive witnesses. Failure of G(q) injects negative indices into positive indices by reflection, giving L(q−1)≥0. The strict-negative sufficient condition is valid pointwise, but its asserted universal O-M5 version is genuinely false at the prime q=5, where L(4)=0. This is not a counterexample to Target or PB. For q=59, the displayed prime factorizations and bounded primality checks yield the claimed signs and failure of precisely the three fixed pairs; 14+104 remains positive-positive. Multiplicativity gives no missing additive sign. LS⇒Target has exhaustive cases: the first disjunct gives the doubled pair; otherwise sign dichotomy and the second disjunct give (m−t,m+t). The bounds 0<t<m guarantee positivity. No proof of PB or LS, and no unwarranted equivalence for LS, is claimed.

The full prose-to-declaration table agrees with the integrated file. The additional conditional prose is not silently represented as further Lean theorems.

## 4. Sources and dependency preconditions

- **Foundational mathematics:** the pinned `Factors.lean` supplies exactly the stated unit, prime-entry, product, singleton, uniqueness and multiplicative-permutation facts. Its positive/nonzero conditions are met where invoked. The remaining count manipulations use finite-set bijections, finite sums, ordered integer arithmetic and exponent identities with the preconditions checked above. No additive conjecture or analytic theorem is a proof dependency.
- **Pinned environment:** an actual read-only `git -C P/lean/.lake/packages/mathlib rev-parse HEAD` returned `905b95818eb32af7874a58b427f50c1711a5e96c`; `git ... status --porcelain=v1 --untracked-files=no` was empty. Both exited 0. The raw Lean version is 4.32.2, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`; Lake is `5.0.0-src+f3b06c7`.
- **Cutoff:** the preserved public witnesses associate those exact Mathlib and Lean SHAs with 2026-07-28 public runs. All nine package `rev` values in the current manifest match exact-SHA witnesses dated before 2026-08-01. Inherited `inputRev` branch names are not substituted for the locked revisions. Failed/skipped CI conclusions do not negate the narrower public-availability evidence. This review used the supplied local provenance data, made no web request and fetched no source.
- **Literature:** the PDF hash matches, its first-page marker identifies arXiv:2404.12117v2, 2 May 2024, and the metadata records 2024-05-02 14:48:54 UTC. Page 1 Theorem 1.2 is an eventual bound `|C(N)|<N−1` for all sufficiently large integers, not an almost-all result and not a negative-negative representation theorem. Page 2 explicitly calls its threshold ineffective. Page 3 Remark 2 asks the original target and describes a hypothetical stronger bound; the candidate does not import either it or PNT/Siegel results. The source's printed inequality following its exact zero identity has the noted N versus N−1/strictness mismatch. The candidate adopts no repair or quantitative consequence of that display. The literature claims are correctly limited to this version, not a global assertion about the state of the problem at the cutoff.
- **Excluded snippet:** the current source ledger still records exclusion of the automatically returned post-cutoff MathOverflow snippet, now at line 62 rather than the candidate's cited lines. Neither that snippet nor its mathematical assertions were consulted here.

## 5. Preserved Lean evidence, not a new execution

Recorded commands, all with cwd `P/lean`:

| Command | Recorded exit | Raw prefix under `formal/integration/` |
|---|---:|---|
| `lake build` | 0 | `v1-04-default-build` |
| `lake build Statement.Partial` | 0 | `v1-05-partial-build` |
| `lake env lean Statement/Partial.lean` | 0 | `v1-06-partial-direct` |
| `lake env lean -t 0 Statement/Partial.lean` | 0 | `v1-07-partial-trust-zero` |
| `lake env lean --stdin < ../formal/integration/v1-08-root-import-check.stdin.lean` | 0 | `v1-08-root-import-check` |
| `lake env lean --stdin < ../formal/integration/v1-09-absent-endpoints.stdin.lean` | 1, expected | `v1-09-absent-endpoints` |

The raw default output explicitly builds Partial and Statement and reports 925 completed jobs. The root stdin checks all 50 added declarations and prints the definitions and axioms. Root output was inspected, including the actual target, identity and prime-core signatures. The final diagnostic contains exactly the two unknown endpoint identifiers, not a supplied proof.

Read-only JSON/hash validation in this review exited 0 and matched all 58 recorded stdout/stderr/stdin digests. In particular direct and trust-zero stdout have identical SHA-256 `6569201315dbd4f85bb46b3a1325837b33029f1cfc742252ab335188aab030b9`; root stdout has `a4c33f9b1f6b2e91d84c3dc06192f0b60a566050a355de2e9ac4c2af621621c1`. The three recorded axiom maps agree on all 82 queried declarations. Direct and root axiom outputs support 42 partial theorems, 11 local/base definitions, and 29 upstream queries, all using only subsets of `{propext, Classical.choice, Quot.sound}`.

The inspected proof scripts and local-source scan contain no sorry/admit/custom axiom/native-decide proof shortcut. Four unused-variable warnings are accurately described. Smoke's `#eval` commands are diagnostic computations, not assumptions in the partial proofs. The uninhabited Scaffold interface requires a Target proof as a field and supplies none; Partial does not import it. Axiom checks of the definition `Target` do not establish its proposition.

The trust boundary remains the pinned Lean implementation/kernel, its foundational axioms and installed pinned library artifacts. No complete from-source upstream rebuild or independent kernel implementation was checked here. There was no concrete concern warranting repetition of the recorded Lean tests.

## 6. Finite computation scope

The Python script and raw data support only the finite claims stated in exposition §9. Its Eratosthenes sieve flips one sign for each dividing prime power, hence counts prime factors with multiplicity. Trial division independently removes all powers and reconstructs the input; the divisor certificates exclude every possible small factor. The ordered-pair loop counts actual pairs by the first index, without reconstructing R from the identity or dividing by symmetry. The separate representative loop has both indices.

A read-only evidence-inventory check, not a rerun of the arithmetic experiment, confirmed 255 rows with exactly N=2,…,256, 271 used-factor rows, 1,260 assertions after summing categories, and empty failure/exception lists. The run manifest records CPython 3.9.6 and actual worker/parent exit 0. The sieve bound 2608 is not a verified target range. The N=10 data have L(9)=−1, C(10)=9, R=5 and exactly the five displayed ordered pairs. The q=37 examples and the seven m=1304 square-template rows have the stated scope and signs; neither failed templates nor these successful examples settle an infinite family. The unresolved historical PB-label correspondence is not silently certified by the exposition. No finite-computation result is needed for the universal Lean identity or partial constructions.

## 7. Packet qualifications and remaining obligations

### D1 — ancillary source-ledger snapshot drift

`FINAL_ARGUMENT.md:458` records `sources.md` as
`a8230ab9eb2e6e43d4c860fa1d35ecc74380995361973122500f750cd474b18a`.
The current file instead hashes to
`9df552348f03fd84ffe0e203f1340f26e6a902f8424f924068fe6fb86c1a7dbb`.
Moreover `FINAL_ARGUMENT.md:382` cites ledger lines 27–28 for the exclusion record; those current lines belong to the package table, and the record is at line 62.

This is a precise current cross-file identity/citation break, not evidence that the recorded historical preparation hash was false. The primary candidate, Lean files, PDF and raw audit remain at their assigned hashes. Direct PDF/metadata/public-witness checks independently support the substantive source claims, so D1 is not a mathematical counterexample or a gap in a partial proof. It nevertheless prevents certifying the entire current packet as the exact cross-referenced snapshot. Owner: leader; freeze/reconcile the ledger reference before final packet acceptance.

### D2 — inadvertent exposure to embedded historical review metadata

While inspecting the candidate's referenced `nl/generator/proof-v2.md`, its returned text included a prior-review summary in lines 10–16 and historical acceptance language in its closing metadata. I did not open the prior review, seek author confidence, or use any historical verdict as evidence. The mathematical checks above were made from statements, proof bodies, the integrated source and raw outputs. Nevertheless, I cannot claim the requested pristine no-old-verdict-exposure condition after this tool return.

Owner: leader; if this is to count as one of the required strictly fresh reviews, dispatch a replacement clean review with historical-verdict metadata excluded from supporting proof excerpts. This report should not be counted as satisfying that stronger procedural condition merely because no reliance was intended. No agent was spawned by this reviewer.

### M1 — the original universal mathematical goal is still missing

The missing obligation is exactly either of the equivalent types:

```lean
∀ N : ℕ, Even N → 2 < N →
  2 * ArithmeticStatement.L (N - 1) - ((N : ℤ) - 1) <
    ArithmeticStatement.C N
```

or

```lean
∀ p q : ℕ, Nat.Prime p → Nat.Prime q →
  ArithmeticStatement.HasRepresentation (2 * p * q)
```

There is also no substitute proof with an effective sufficiently-large threshold and complete finite remainder. PB and LS are optional unproved sufficient premises, not additional established results. O-M5 is refuted at q=5 and must not be used. No amount of compiler success on these equivalences, or finite template evidence, supplies M1.

## 8. Recommended next action

The leader should retain the sound partial mathematical content, resolve D1 and route a clean replacement review for D2 before counting full packet acceptance. Further mathematical work must address M1 rather than rebrand an equivalence as a proof. No mathematical repair to the checked partial deductions is requested by this report. If any proof or statement changes, a new exact-snapshot review is required.

**Bottom line:** partial deductions withstand the mathematical audit; full review-packet certification is withheld for the stated identity/hygiene qualifications; the original conjecture remains unproved in this delivery.
