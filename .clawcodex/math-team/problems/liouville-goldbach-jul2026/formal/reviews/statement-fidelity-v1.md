# Independent statement-fidelity review v1

Mode: CERTIFICATION — statement fidelity only, not proof truth.

VERDICT: APPROVE

**Protection decision:** YES. The exact `ArithmeticStatement.Target` definition, together with `omega`, `lambda`, and the pinned defining dependencies identified below, may be protected as the target for proof work. This does **not** make `Target` an accepted theorem or an available assumption. No inhabitant of `Target` is supplied by the reviewed declaration.

**Mismatches:** None found. **Unresolved statement-fidelity obligations:** None. The original conjecture's proof is outside this review and remains an obligation; no proof-truth verdict is given.

## 1. Scope and artifact identity

Path abbreviations used throughout:

- `P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`
- `R = .clawcodex/math-team/review-inputs/r20260924-v1`
- `M = P/lean/.lake/packages/mathlib`
- `L = ~/.elan/toolchains/leanprover--lean4---v4.32.2/src/lean`
- `E = P/formal/environment`

Original source: `P/request.md:7–14`; cutoff: `:16–27`; requested definition audits: `:49–57`.

Production declarations: `P/lean/Statement/Definitions.lean:6` (`omega`), `:8` (`lambda`), `:10–14` (`Target`). The whole production file was read. Its SHA-256 equals the hash specified in the review assignment. `R/Declaration.lean` was independently byte-compared with it and is identical.

The literal account in `R/readback.md:5–55` agrees with the production declaration and the pinned definitions. Its label is not used as evidence of source fidelity or truth. `P/formal/formalizer/definition-audit-v1.txt:34–140,179–197` was treated as translation decisions and dependency locators, verified against the source and code rather than adopted as author assurance. No prior fidelity/proof acceptance report was consulted. No candidate, task board, or team state was edited; no agents were spawned.

### Review-input SHA-256 identities

| Artifact | SHA-256 |
|---|---|
| `P/request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| Source slice, lines 7–14 inclusive | `810758754f786198ac3151a7a35b2cad3ca9b424b0c2d4e2fd163b1a15c43fb3` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `Target` declaration slice, lines 10–14 inclusive | `3d826a6faedfc6fc0a8192864f6c8c0db977da3be3af548974f3f10a7f10409a` |
| `R/Declaration.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `R/Dependencies.lean` | `55b5480511d2a2cb749cebafa9b8da29f744090a269bd0ece94df1b37ab0d07c` |
| `R/ListOperations.lean` | `925cbf08a1aac0870075ad56ff2d95c7b0eb94c87853ace32d0043a9c094e2bc` |
| `R/readback.md` | `dbe6c1e5ff159fd8f2f5e21e0c95981829ebb6e6133598a94597975d8b563ca6` |
| `P/lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `P/lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `P/lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |
| `P/formal/formalizer/definition-audit-v1.txt` | `c4abe9f0d774a16e0faa6365d2ec05527fe075b63b5462c69e0c55237b888b3c` |
| `E/environment-report.txt` | `05e10971b80acab2a04139ec6a0647e5f8fbd4a09bb516b1db205b084adac71a` |
| `E/source-file-identities.json` | `1853289c7fd475c3483c68eec07c254c2fd1949e8fb50603ed89a1966b36eaff` |
| `E/public-availability-witnesses.json` | `051de67ee5bfd81242942075cf9dabacd8cfa96b74abf3733b025456694cc4c1` |

Slice hashes preserve the original bytes, including the final LF. Other hashes cover entire files. Hashes were computed independently in this review, not merely copied from the author audit.

## 2. Source-to-declaration audit

The reviewed type expands to:

```lean
∀ N : Nat, (∃ r : Nat, N = r + r) → 2 < N →
  ∃ a b : Nat,
    0 < a ∧ 0 < b ∧ N = a + b ∧
      ArithmeticStatement.lambda a = (-1 : Int) ∧
      ArithmeticStatement.lambda b = (-1 : Int)
```

1. **Multiplicity, not distinct factors.** Source `request.md:7` corresponds to `Definitions.lean:6`. At `M/Mathlib/Data/Nat/Factors.lean:38–44`, the list extracts one `minFac` and recurses on the quotient without deduplication. `:55–65` says every entry is prime, `:70–81` gives product equal to the nonzero input, and `:168–187` provides uniqueness up to permutation and `(p^k).primeFactorsList = List.replicate k p` for prime `p`. These are ordinary prime factors: `Nat.Prime` is defined at `M/Mathlib/Data/Nat/Prime/Defs.lean:42–43`, and its divisor characterization is at `:97–112`. I also inspected `minFacAux`/`minFac` at `:207–219`, with primality/divisibility/minimality at `:287–303`. List length counts every cons (`L/Init/Prelude.lean:3027–3029`); replication repeats elements (`L/Init/Data/List/Basic.lean:705–707`). Thus repeated primes contribute repeatedly to `omega`.

2. **Value at one.** `Factors.lean:39–40,46–53` gives the empty list at 1; list length is zero. The natural exponent zero on the integer base yields `lambda 1 = 1`, not `-1`. This matches the source convention `Ω(1)=0` exactly. Direct evaluation also returned `(1, [], 0, 1)`.

3. **Signed codomain and exponent.** `Definitions.lean:8,14` explicitly uses `Int` for the base, result, and required sign. The exponent has type `Nat`. There is no truncated natural subtraction or natural-valued representation of negative one. The actual elaboration uses `Int.instNegInt` and the natural-power operation through `Int.instMonoid`. Its source at `M/Mathlib/Algebra/Group/Int/Defs.lean:28–35,71–75` uses the ordinary integer power; core negation and power are at `L/Init/Data/Int/Basic.lean:102–134,400–405`. Both sign equations are present, equivalent to the source's chained `λ(a)=λ(b)=-1`; the type does not merely assert equal signs or a product of signs.

4. **Quantifiers and dependencies.** Source `request.md:10–12` corresponds exactly to `Definitions.lean:11–14`: universal `N`, evenness premise, strict lower-bound premise, existential `a`, existential `b`, then all conjunctions. Witnesses may depend on each admissible `N`; no universal pair is demanded and no universal assertion about all decompositions is substituted. The half-witness in `Even N` is local to the antecedent, not a new outer choice controlling the conclusion.

5. **Evenness and full range.** At `M/Mathlib/Algebra/Group/Even.lean:53–57`, `to_additive` generates the additive predicate. An independent `#print Even` confirmed `∃ r, a = r+r`; `pp.all` confirmed its application at `Nat` with `instAddNat`. The universal input has no upper bound; the literal lower bound is exactly `2 < N`. There is no sufficiently-large, finite-range, almost-all, or density replacement and no adjustable threshold.

6. **Positive summands and equal case.** `0 < a` and `0 < b` are explicit and separate. The sum equation is exactly `N = a+b`. No primality, oddness, coprimality, distinctness, ordering, or other extra clause occurs. Equal summands are permitted. In particular the boundary input `N=4` permits `a=b=2`; evenness has half-witness 2 and `lambda 2=-1`. The syntax does not restrict summands to primes: evaluated composite inputs 8, 12, 18, and 27 have sign `-1`.

7. **No aggregate/pointwise mismatch.** Both required signs apply to the individual existential summands. The only aggregate relation is their exact sum. No correlation bound, averaged sign, sum-of-signs identity, or sign-product condition replaces the source conclusion. The readback's derived bounds `2≤a,b≤N−2` are valid consequences of positivity, `lambda 1=1`, and the sum equation, not extra restrictions in the declaration.

8. **Constants.** The target fixes only the source's threshold 2, zero in positivity, and the integer sign `-1`. There are no free/existential constants or unjustified choices of a bound. Constants in the factorization algorithm are internal to its fixed definition, not target hypotheses.

### Natural-number normalization of the integer source

The use of `Nat` is faithful, not a missing integer case. For a source integer `N>2`, there is a unique natural preimage `n=N.toNat`, and its integer inclusion is `N`. The inclusion preserves addition, equality, and strict order on these nonnegative values. The same bijection applies to positive integers `a,b` and strictly positive naturals.

If the integer `N>2` is `r+r`, then `r>0`: otherwise its double is nonpositive. Hence its half has a natural preimage and gives `n=s+s`. Conversely a natural evenness witness casts to an integer evenness witness. Transporting either direction preserves the sum, positivity, and the possibility `a=b`. Positive-integer prime factors are the prime factors of that same natural preimage; no negative-input factorization convention is required by this target. Core `Int.toNat` at `L/Init/Data/Int/Basic.lean:364–366` returns the underlying natural on nonnegative integers, and integer addition on such inputs is natural addition (`:160–169`).

This is the semantic domain identification used for fidelity. It is not represented here as a separately proved Lean transport theorem, and no such theorem is claimed.

### Degenerate cases, vacuity, and assumptions

- Odd inputs and `N≤2` are outside the implication's obligations, exactly as in the source. Negative source integers also fail `N>2`; none are lost by the normalization.
- The joint premises are satisfiable: `N=4` is even and exceeds 2. No contradiction or empty-domain premise makes the whole target vacuous.
- `primeFactorsList 0=[]` totalizes `omega 0=0` and `lambda 0=1`. This is irrelevant to the source assertion because both summands are explicitly positive. Neither zero nor one is a spurious sign witness.
- `Target : Prop` is closed: no section variables, additional hypothesis binders, arbitrary arithmetic instances, or `[Fact Target]` are present. Fully explicit printing fixes ordinary natural order/addition and integer negation/power. `Even`'s generic `[Add α]` is resolved at `Nat`, not carried as a hidden target assumption.
- Axiom diagnostics on `omega`, `lambda`, `Target`, and the factorization semantic declarations listed below found only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or custom/target axiom. These are foundational dependencies, not number-theoretic hypotheses. Checking axioms of a proposition-valued **definition** does not produce a proof of that proposition.

## 3. Pinned dependencies and cutoff

All external mathematical code inspected is in the pinned Mathlib/Lean versions below. No network retrieval, later documentation, paper, current branch, or later mathematical source was used in this review.

- Mathlib commit: `905b95818eb32af7874a58b427f50c1711a5e96c` (`v4.32.2`). Immutable source locators are `https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/<path relative to M>`.
- Lean commit: `f3b06c705e6c85f5314019d5d3baab0fec5b580c` (`leanprover/lean4:v4.32.2`). Core locators are `https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/<path relative to L>`.
- The installed binary independently reported this exact Lean version and commit.

I parsed the saved raw `E/public-ci-<name>.stdout` responses and checked their recorder hashes, exact `head_sha`, public repository flag, and a run creation time before `2026-08-01T00:00:00Z`. The resulting witnesses agree with `public-availability-witnesses.json`; this is a check of the supplied historical metadata, not a new live query. It does not rely solely on Git commit timestamps or current mutable tag pointers.

| Package | Exact commit | Selected public run UTC / run ID |
|---|---|---|
| Lean | `f3b06c705e6c85f5314019d5d3baab0fec5b580c` | 2026-07-28 14:27:52 / 30368480005 |
| Mathlib | `905b95818eb32af7874a58b427f50c1711a5e96c` | 2026-07-28 16:36:37 / 30379053106 |
| plausible | `e12c1910fe855cbfc38803cd4e55543906d5fa62` | 2026-07-13 13:20:50 / 29253419718 |
| LeanSearchClient | `c5d5b8fe6e5158def25cd28eb94e4141ad97c843` | 2026-02-12 00:28:07 / 21928619159 |
| importGraph | `7e9612bf0b9ee66db3cb5b9988a35afc706f5a12` | 2026-07-13 13:50:43 / 29255410348 |
| proofwidgets | `6e311e2a844da9b2cc3971187df2fe0066947b93` | 2026-07-13 13:20:54 / 29253424000 |
| aesop | `a7dbf0c63b694e47f425f3dcddbc0e178bb432d3` | 2026-07-13 14:03:38 / 29256329889 |
| Qq | `38d591e778f100aec9762bb582f9c7f55f50e9dc` | 2026-07-13 13:20:57 / 29253426904 |
| batteries | `023ce7d62a0531e22a5331e20b587817a80d49ff` | 2026-07-13 20:29:43 / 29282598413 |
| Cli | `88679d088c9720c27ebdf2ba4dafe17341747f94` | 2026-07-13 13:20:47 / 29253416514 |

The run URLs, repository names, and date fields are retained in the hashed witness file. The raw release metadata also gives Lean publication `2026-07-28T16:34:35Z` and Mathlib publication `2026-07-28T16:47:51Z`. Each selected source version is therefore eligible under the inclusive July 31 cutoff on the supplied evidence. CI failure for some ancillary packages is not a failure of the historical-availability witness and is not used as local compilation evidence.

I independently ran `git rev-parse HEAD` and `git status --porcelain --untracked-files=no` in each of the nine package checkouts: every HEAD equalled its manifest SHA and every tracked-source status was empty. Nested manifests have no conflicting or additional pins: importGraph points to the listed Cli revision, aesop to the listed batteries revision, and the other ancillary manifests have empty package lists. Historical `inputRev` values `main`/`master` are not the locked `rev` values; no update or resolution of those branch names was performed.

### Defining-source SHA-256 identities

Each Mathlib file below was byte-compared to `git show <pinned SHA>:<path>`. The three installed core files were compared to the saved exact-commit raw source bytes, and their Git blob IDs were independently recomputed and matched `source-file-identities.json`.

| File | SHA-256 |
|---|---|
| `M/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `M/Mathlib/Data/Nat/Prime/Defs.lean` | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `M/Mathlib/Algebra/Group/Even.lean` | `1180fa9ac282e55257e95c8402acd7314fcbd0a18bcfdede92a3cde16e1db630` |
| `M/Mathlib/Algebra/Group/Irreducible/Defs.lean` | `77937179ccfec6ca8acdd4b660525a7f313d4fb0b9c6dc4296d1301fb9e1e731` |
| `M/Mathlib/Algebra/Group/Units/Defs.lean` | `09489226154d6558ad44614501b55883f0dc31b4504f1bb29e6190b2df456bce` |
| `M/Mathlib/Algebra/Group/Nat/Units.lean` | `142ba1775b83ff0713921caf424248eafbc4b31c280a46ef5e505394e3350c7d` |
| `M/Mathlib/Algebra/Group/Int/Defs.lean` | `d609e4c0120a329397c91ef3185ad35d83dba39d75987c39fb989bce338767ea` |
| `L/Init/Prelude.lean` | `44f86ebbb9ab743a05c6ebe2c674aadbf2c822bee874f1b16d7e6c8d56318dc9` |
| `L/Init/Data/List/Basic.lean` | `c6b61f1b5fcac4ea4339625f2e66916d1f2c1ae2531c10ee45b401846ffb6061` |
| `L/Init/Data/Int/Basic.lean` | `e3a3b503e2f89a7dc5dfbfdf610c5b9927ddc0c61809bbb8110053b7982021e5` |

Additional inspected locators: `Irreducible/Defs.lean:44–48`, `Units/Defs.lean:49–57,358–365`, and `Nat/Units.lean:24–38`. These confirm the standard irreducibility/unit interpretation used in the prime characterization. The code-only supplements match the relevant defining equations and signatures; they omit proof/termination bodies and are not new compiling modules or axioms.

### Raw provenance evidence hashes

All paths in this table are relative to `E`.

| File | SHA-256 |
|---|---|
| `public-ci-lean.stdout` | `aeaea1b78e78521606c013a4fafc4b9c0bcaae068cd63f6e97a57bbd26a43826` |
| `public-ci-mathlib.stdout` | `4337fdc10284dc0c90165a0e4926fde19ebb6ce78dfef2505a3112a277452e00` |
| `public-ci-plausible.stdout` | `7db3a5d1c95ca7d1b1906ec25958d6f1d490a9953154fdf3180f09fd57195e7b` |
| `public-ci-LeanSearchClient.stdout` | `3abdd2daec49091e23e2601a2d77322759da75c6967c6ef67d76cd806ad2d5af` |
| `public-ci-importGraph.stdout` | `5551743d19c9b24dc50743a216975cc324b4bb94618b36fd2839785fbc5fb575` |
| `public-ci-proofwidgets.stdout` | `0af1983970539258f9627cde04d59047e20557b9b5d39248ae2018f728f2cce6` |
| `public-ci-aesop.stdout` | `83bc912b7caf04c68210490e75285c2eba39396aad9cad151c68f2322a36c06d` |
| `public-ci-Qq.stdout` | `e8ff8f4e5970e6943179a83cc2be235f3296ef5153f1d550a3dabf86e69a575b` |
| `public-ci-batteries.stdout` | `3bb8ca7972a48ad427bab042620fed56c5a2a71813ec02621723647adc7fa741` |
| `public-ci-Cli.stdout` | `7db04e1305e996408659d75f8c28ea7d2c4415dcb337834ec3c93a4ee7b36844` |
| `lean-release.stdout` | `8c58bfbff7a6fca95e743e7de64de75561d605accd9d31e1179b9e3f17c6cbe2` |
| `mathlib-release.stdout` | `c301e835f278ccfd3a89aaea81d9a549923c846b819832a332845abcb61ab6ef` |

## 4. Independently executed Lean diagnostics

Working directory for all three commands: `P/lean`. Commands were invoked synchronously through Python `subprocess.run`, capturing raw stdout/stderr, without writing a diagnostic Lean file or requesting output artifacts. No proof was attempted and the production file was not modified.

| Actual argv | UTC start (2026-09-25) | Exit | stdout SHA-256 |
|---|---|---|---|
| `lake env lean --version` | 02:27:21.152092 | 0 | `562cd1632273e7efc3f67a6754fa51bd59ec9cf369d6d9bf1d6472593ba5d8b4` |
| `lake env lean Statement/Definitions.lean` | 02:27:25.010968 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `lake env lean --stdin` | 02:27:30.196085 | 0 | `afb34b63b06cd9c77322986534a6810fde506e2d6a12a7e29eabdcd4f12eb380` |

All stderr streams were empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. The second command had no diagnostics. Version output was:

```text
Lean (version 4.32.2, arm64-apple-darwin24.6.0, commit f3b06c705e6c85f5314019d5d3baab0fec5b580c, Release)
```

The third command re-elaborated **the actual production source bytes**, not a potentially stale local `Statement.Definitions.olean`: stdin was the whole `Definitions.lean` file followed by one additional LF and the following UTF-8 lines, including their final LF. Complete stdin SHA-256: `9620143671aa49fb014cead4b34d544361adf23a8b959617deb536c74c8006bd`.

```lean
#print ArithmeticStatement.omega
#print ArithmeticStatement.lambda
#print ArithmeticStatement.Target
#print Even
set_option pp.all true in
#print ArithmeticStatement.Target
set_option pp.all true in
#print ArithmeticStatement.lambda
#check Nat.prime_def_lt
#check Nat.minFac_dvd
#check Nat.minFac_prime
#check Nat.prime_of_mem_primeFactorsList
#check Nat.prod_primeFactorsList
#check Nat.Prime.primeFactorsList_pow
#print axioms ArithmeticStatement.omega
#print axioms ArithmeticStatement.lambda
#print axioms ArithmeticStatement.Target
#print axioms Even
#print axioms Nat.minFac_prime
#print axioms Nat.prime_of_mem_primeFactorsList
#print axioms Nat.prod_primeFactorsList
#print axioms Nat.Prime.primeFactorsList_pow
#eval ([0, 1, 2, 4, 8, 12, 18, 27] : List Nat).map (fun n => (n, n.primeFactorsList, ArithmeticStatement.omega n, ArithmeticStatement.lambda n))
#eval decide ((4 : Nat) = 2 + 2 ∧ 2 < (4 : Nat) ∧ 0 < (2 : Nat) ∧ ArithmeticStatement.lambda 2 = (-1 : Int))
```

Results:

- Printed definitions and semantic signatures matched the source/supplement audit above.
- `pp.all` exposed only fixed `Nat`/`Int` operations, with no additional binders or hypotheses.
- `Even` has no axioms. Each of the other seven axiom queries returned exactly `[propext, Classical.choice, Quot.sound]`.
- The value tuples `(n, primeFactorsList n, omega n, lambda n)` were:

```text
[(0, [], 0, 1), (1, [], 0, 1), (2, [2], 1, -1), (4, [2, 2], 2, 1), (8, [2, 2, 2], 3, -1), (12, [2, 2, 3], 3, -1),
  (18, [2, 3, 3], 3, -1), (27, [3, 3, 3], 3, -1)]
true
```

The final Boolean checks the boundary/equal-summand data, not the universally quantified target. These are definition sanity tests, not a proof of the conjecture. Likewise, successful elaboration is not the basis for source fidelity; the clause-by-clause comparison supplies that review judgment. Imported upstream artifacts were used in the pinned environment; this review did not rebuild all upstream theorem proofs from source or independently certify the toolchain/cache mechanism.

## 5. Handoff and exact limits

The leader may protect the identified statement snapshot and route proof work against it. Preserve both the declaration and its defining dependencies/toolchain pins. Any mathematical change invalidates this fidelity/readback binding and requires fresh review.

No statement repair is requested. This approval does not cover an inhabitant, an integrated proof module, an unfinished wrapper, or a future helper theorem. A final success claim still requires the full original target to be proved and separately checked, without weakening the statement or introducing target assumptions.
