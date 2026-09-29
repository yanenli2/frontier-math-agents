Mode: CERTIFICATION

# Independent candidate statement/dependency audit v1

**VERDICT: APPROVE — partial candidates only.**

The actual 42 proved helper/partial theorems and eight new definitions meet this review's pre-integration gate. Their exact statements and defining dependencies may be protected for subsequent proof work and handed to the designated integrator. No mathematical repair is requested.

**The original conjecture is not proved by this file.** Neither `ArithmeticStatement.pointwise_keystone` nor `ArithmeticStatement.liouville_goldbach` is present. Approval does not extend to a complete proof, an integrated master, or fulfillment of the original success conditions.

## 1. Scope, sources, and immutable identities

Here `P` is `.clawcodex/math-team/problems/liouville-goldbach-jul2026`; `Q` is `.clawcodex/math-team/review-inputs/r20260924-v1`.

This fresh review read the skill's `references/lean.md` and `references/protocol.md`, the original source, actual candidate and definitions, supplied literal readbacks and their code inputs, mathematical descriptions, pinned library definitions, and local environment provenance records. It did not consult earlier fidelity reviews or production confidence reports, spawn agents, alter declarations, or edit task/team state. Only this report and its `.log`/`.json` evidence were written.

Authoritative source locators:

- `P/request.md:7–14`: multiplicity-counting Liouville function; every even integer greater than 2; positive, possibly equal summands, each of sign −1; no added restrictions.
- `P/request.md:76–85`: ordered-pair count, finite sums, exact signed counting identity and positivity goal.
- `P/request.md:89–125`: exact-file checking, axiom restrictions, integration and completion requirements.
- `P/nl/sketcher/formal-handoff-v1.md:7–45, 51–81, 85–98`: domains, counting helpers, scaling, diagonal and all-positive-multiples-of-8 partial result; open pointwise inequality.
- `P/nl/explorer/attempt-v1.md:13–29, 33–49, 74–90`: multiplicativity, signed scaling, seed construction, and exact prime-product-core equivalence including repeated primes. These are mathematical descriptions, not prior certification evidence.

SHA-256 identities, independently computed and unchanged across checking:

| Artifact | SHA-256 |
|---|---|
| `P/request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `P/formal/generator/Candidate.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `P/formal/approved-v1/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/formal/blueprinter/interfaces-v1.lean` | `89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc` |
| `Q/readback.md` | `dbe6c1e5ff159fd8f2f5e21e0c95981829ebb6e6133598a94597975d8b563ca6` |
| `Q/interfaces-readback.md` | `88a3bb1152043c2eb245914cbec5a569cbf81ab47e4031f1330e1ba27d139e9e` |
| `P/lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |
| `candidate-audit-v1.log` | `f9be352c079cf3addf5b43988f35c59650fef2e84dd38988576bdb6274ea9523` |
| `candidate-audit-v1.json` | `cf36dd42c567308de978da49921092b994d95cc31184d12e6aeb9896b4e437ec` |

The production `P/lean/Statement/Definitions.lean` and blind `Q/Declaration.lean` are byte-identical to the protected base. `Q/Interfaces.lean` is byte-identical to the helper snapshot. Consequently the supplied literal readbacks cover the same defining bodies and helper signatures compared here; their labels were not used as proof evidence.

The JSON records all 50 candidate declarations individually: exact comparison text, candidate/snapshot line spans, signature-or-definition SHA-256, and full candidate-declaration SHA-256. The theorem comparison excludes only the proof assignment/body and trailing separator whitespace; it preserves all internal signature text. Definition comparisons include the entire defining body. All 42 signatures and eight definition bodies match exactly under that extraction. In particular:

| Statement-header hash | SHA-256 |
|---|---|
| `representation_multiple_eight` | `14cd405d22b504deb4572b1d2612d1c0841d7fe6cbd7fdd4ab929a41f2582684` |
| `four_mul_representation_count` | `a4c1fbc578406009c0cc4eaf26bd8eee05f6e77b3016ff69a2ce8aed426a152d` |
| `target_iff_prime_product_core` | `aa800bcc8cefa81ce74c06732d3b377a4a679227428f8973dd0ec2e8c79f5c79` |

## 2. Definition and literal-statement fidelity

### Base domain and multiplicity

`Definitions.lean:6–14` defines `omega n := n.primeFactorsList.length`, integer-valued `lambda n := (-1 : ℤ) ^ omega n`, and the proposition `Target`. It does not postulate its truth.

I inspected the pinned implementation, rather than relying on the factor-list name: `Mathlib/Data/Nat/Factors.lean:38–44` recursively removes one smallest-prime-factor occurrence; lines 47–53 give the empty lists at 0 and 1; lines 55–81 establish prime entries and their product. The prime-power statement at 181–187 explicitly uses a repeated list. `Init/Prelude.lean:3027–3029` counts every list entry; `Init/Data/List/Basic.lean:705–715` confirms repetition and its length. Thus factors are counted with multiplicity, `omega 1 = 0`, and `lambda 1 = 1`. The totalization `lambda 0 = 1` has no effect on the positive-input source problem.

`Even` is the additive definition generated at `Mathlib/Algebra/Group/Even.lean:55–57`; the independent compiler print confirms `∃ r, a = r + r` (`.log:460–461`). `Nat.Prime` is actually `Irreducible` (`Data/Nat/Prime/Defs.lean:42–43`); its defining structure and unit predicate were inspected, and the same file's proved characterization at 97–112 is the ordinary natural-prime condition. There is no nonstandard prime domain.

The protected target universally quantifies `N : ℕ`, then assumes `Even N`, then `2 < N`, then chooses positive `a,b : ℕ` separately for that input. This is a faithful positive-natural normalization of the original integer statement: every admissible integer input and every permitted witness is positive. There are no negative-integer cases to lose. A separate Lean integer/natural coercion-equivalence theorem proposed in the handoff is not supplied here; this review does not claim one was checked.

There is no distinctness, ordering, oddness, primality or coprimality requirement on the summands. The domain is nonempty (`N=4`); `a=b` is allowed. No witness is required to work uniformly for all inputs.

### Eight new definitions

`Candidate.lean:14–41` matches `interfaces-v1.lean:11–38` exactly:

- `HasSignedRepresentation s N` has two positive natural witnesses with sum `N` and separately prescribed common integer sign `s`.
- `HasRepresentation N` specializes that sign to −1; it does not include evenness, primality or a hidden proof.
- `I N = Finset.Ico 1 N`, i.e. `1 ≤ a < N`. The actual natural locally-finite-order instance was inspected (`Order/Interval/Finset/Nat.lean:33–41`).
- `representationIndices` is the indicated filtered interval.
- `orderedRepresentations` filters the actual Cartesian product `I N × I N`; `R` is its cardinality, not initially a renamed index count. The product, filter and cardinality definitions were inspected (`Data/Finset/Prod.lean:45–61`, `Filter.lean:46–53`, `Card.lean:44–53`). Reversed unequal pairs are distinct; a diagonal pair occurs once.
- `L x` is an integer sum over `1 ≤ a ≤ x`; `C N` is an integer sum over `1 ≤ a < N` of `lambda a * lambda (N-a)`. The finite-sum definition is the additive counterpart of the mapped-multiset product (`Algebra/BigOperators/Group/Finset/Defs.lean:59–69`). Neither sum averages over the input `N`.

The source's ordered positive-pair count is exactly captured: positive summands adding to `N` automatically lie below `N`. The candidate proves that membership characterization and the injective index-to-pair image bridge; it does not silently change `R` to an unordered count. The handoff's optional index-count convention is therefore reconciled by a proved equality, not assumed.

### Context, vacuity and endpoint guards

There are no section variables, implicit target hypotheses, custom instances, local notation overrides, axioms or opaque postulates in the candidate or production base. `autoImplicit` is false. Additional imports relative to the signature snapshot are pinned parity, integer and ring-tactic infrastructure, not a theorem assuming the desired result. An independent diagnostic pass printed the loaded base definitions and checked all 50 fully qualified declarations with `@`; their elaborated types have no additional typeclass/hypothesis parameters (`.log:447–624`). Natural/integer arithmetic and finite-set instances are fixed standard instances.

`I 0` and `I 1` are empty; counts/correlations there are zero. Identity and counting-bridge declarations explicitly assume `2 ≤ N`; natural differences `N-a` on interval members and the index `N-1` are then exact, not an unnoticed truncation. For `N=2`, the interval is `{1}`, `R=0`, `L(1)=1`, `C(2)=1`, and the identity has both sides zero. The original target excludes this nonrepresentable case by `2<N`.

For a signed-representation premise, signs other than ±1 are impossible, but that is a legitimate conditional scaling lemma, not vacuity of `Target`. The two-sign seed has independent existential pairs, not one pair required to have contradictory signs. Its concrete instance at 8 supplies both premises. The four unused-variable warnings concern redundant guards, not missing proofs or unsatisfiable added assumptions.

## 3. Coverage of every actual theorem

Every row below is an exact signature match. Numbers are actual candidate lines and interface-snapshot lines respectively; declaration hashes and verbatim signatures are in the JSON.

| Declaration in `ArithmeticStatement` | Candidate | Snapshot |
|---|---:|---:|
| `omega_one` | 43–45 | 40–41 |
| `lambda_one` | 47–49 | 43–44 |
| `lambda_sign` | 51–55 | 46–47 |
| `omega_mul` | 57–60 | 49–50 |
| `lambda_mul` | 62–64 | 52–53 |
| `lambda_prime` | 66–68 | 55–56 |
| `lambda_two` | 70–72 | 58–59 |
| `lambda_three` | 74–76 | 61–62 |
| `lambda_four` | 78–82 | 64–65 |
| `lambda_five` | 84–86 | 67–68 |
| `lambda_two_mul` | 88–91 | 70–71 |
| `lambda_square` | 93–96 | 73–74 |
| `target_iff_forall_hasRepresentation` | 98–100 | 76–77 |
| `hasSignedRepresentation_mul` | 102–109 | 79–81 |
| `representation_scaled_sign` | 111–122 | 83–88 |
| `representation_double` | 124–127 | 90–92 |
| `representation_diagonal` | 129–137 | 94–96 |
| `representation_two_sign_seed` | 139–148 | 98–102 |
| `eight_two_sign_seed` | 150–155 | 104–106 |
| `representation_multiple_eight` | 157–159 | 108–109 |
| `mem_I_iff` | 161–163 | 111–112 |
| `interval_eq_Icc` | 165–169 | 114–115 |
| `interval_bounds` | 171–174 | 117–118 |
| `interval_card_cast` | 176–180 | 120–121 |
| `reflection_mem` | 182–184 | 123–124 |
| `reflection_involutive` | 186–189 | 126–128 |
| `reflection_bijection` | 191–198 | 130–131 |
| `sum_lambda_interval` | 200–203 | 133–134 |
| `sum_lambda_reflection` | 205–213 | 136–137 |
| `mem_orderedRepresentations` | 215–225 | 139–142 |
| `orderedRepresentations_eq_image` | 227–245 | 144–146 |
| `representation_count_eq_card_indices` | 247–250 | 148–149 |
| `two_sign_indicator` | 252–257 | 151–154 |
| `representation_count_eq_indicator_sum` | 259–266 | 156–160 |
| `four_mul_representation_count` | 268–289 | 162–163 |
| `representation_count_pos_iff` | 291–298 | 165–166 |
| `count_pos_iff_keystone` | 300–303 | 168–169 |
| `keystone_ge_four_iff` | 305–308 | 171–172 |
| `target_iff_count_pos` | 310–317 | 174–175 |
| `target_iff_pointwise_keystone` | 319–327 | 177–179 |
| `exists_prime_pair_factor_of_lambda_one` | 329–360 | 181–185 |
| `target_iff_prime_product_core` | 362–386 | 187–189 |

Substantive source/dependency findings:

1. **Multiplicativity is on positive inputs, without coprimality.** The load-bearing pinned theorem is `Nat.perm_primeFactorsList_mul`, `Data/Nat/Factors.lean:196–202`, whose hypotheses are merely nonzero factors. Taking list lengths and applying `pow_add` matches the explorer's M dependency. Prime evaluation uses the actual singleton-factor-list theorem at 83–88. No restriction to squarefree inputs appears.
2. **The scaling/diagonal declarations are genuinely partial.** The common-sign scaling hypotheses and their order agree with the source descriptions. `representation_two_sign_seed` works even without an explicit even-seed hypothesis: the proof uses just its two seed representations and positive multiplier. This is a justified generalization of handoff E04 and agrees with the explorer's general seed mechanism; it does not weaken the final target. The existence-only conclusions do not themselves prescribe witness formulas, although the checked proofs implement the stated constructions.
3. **The multiple-of-8 result is universal.** `representation_multiple_eight` asserts `∀ m : ℕ, 0<m → HasRepresentation (8*m)`, with no search bound or additional sign assumption. The checked seeds are `3+5` of sign −1 and `4+4` of sign +1; the scaling proof splits the multiplier's sign. This matches handoff E05 and `attempt-v1.md:49`. It is not coverage of all even inputs.
4. **The identity is exactly signed and ordered.** For every natural `N≥2`, `four_mul_representation_count` gives `4*(R N : ℤ) = ((N : ℤ)-1) - 2*L(N-1) + C N`. Reflection is an actual `Set.BijOn` (its definition was inspected at `Data/Set/Operations.lean:282–309`). The count/image and indicator bridges justify summation over one coordinate. All scalar subtraction is in integers; there is no natural subtraction on the signed expression and no division. This matches `request.md:78–85` and handoff C02–C08.
5. **The positivity equivalences preserve logical strength.** `count_pos_iff_keystone` uses the strict inequality `2*L(N-1)-((N:ℤ)-1) < C N`; the alternative threshold 4 is justified by the exact expression `4R`, not an arbitrary analytic constant or a claim of four representations. The closed target equivalences require the inequality separately for every even `N>2`. No averaged bound has been rendered pointwise or substituted for a missing pointwise result. An equivalence is not a proof of either side.
6. **The core equivalence includes repeated primes.** The factor lemma has `m>1`, `lambda m=1`, and chooses `p,q,d` afterward, with ordinary primality of `p,q`, `d>0`, `lambda d=1`, and `m=d*(p*q)`. Neither `p≠q`, coprimality, squarefreeness nor `d>1` is imposed. Its checked proof extracts two list occurrences; for `m=p²`, `p=q` and `d=1` remain permitted. `target_iff_prime_product_core` is a two-way equivalence with **all** prime pairs. The forward direction has admissible `2*p*q≥8`; the reverse uses the diagonal sign case or the factor/scaling case exactly as described at `attempt-v1.md:82–86`. The core's summands are not required to be prime. No proof of the universal core itself is supplied.

**Mismatch details:** none among the actual 42 signatures, eight defining bodies, their referenced base definitions, and the source intent for those partial results. The two snapshot-only endpoints are omissions of unfinished results, not quietly assumed dependencies. They would be decisive failures if this artifact were presented as the full original theorem.

## 4. Independent exact-file compiler and axiom evidence

All commands ran from the actual pinned project:

`.clawcodex/math-team/problems/liouville-goldbach-jul2026/lean`

- `lake env lean --version`: Lean **4.32.2**, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`, arm64 macOS; exit 0.
- `lake env lean .clawcodex/math-team/problems/liouville-goldbach-jul2026/formal/generator/Candidate.lean`: **exit 0**, 5.694 seconds; `.log:229–337`.
- `lake env lean --stdin`: unchanged candidate bytes followed only by diagnostic `#print`/`#check` commands; **exit 0**. The exact appendix and stdin hash are in the JSON. This supplements, and does not replace, exact-file compilation.
- `lake env lean -t 0 .clawcodex/math-team/problems/liouville-goldbach-jul2026/formal/generator/Candidate.lean`: **exit 0**, 9.083 seconds; `.log:631–739`. This also invokes Lean's trust-zero checking mode for imports; it is not a source rebuild of every library package.

The only diagnostics are four `linter.unusedVariables` warnings at `51:29`, `171:35`, `187:5`, and `291:46`. No admitted-obligation warning or error appears. Full source inspection and dedicated scans found no `sorry`, `admit`, `sorryAx`, custom `axiom`, unsafe/opaque postulate, `native_decide`, `implemented_by`, or candidate metaprogramming that introduces proof assumptions. The imported local base consists only of the three visible definitions.

All **82** requested `#print axioms` responses were inspected: 42 candidate theorems, 11 local/base definitions, and 29 named library dependencies (`.log:254–335`, repeated at trust zero at 656–737). Each candidate theorem and local/base definition has exactly:

`{propext, Classical.choice, Quot.sound}`.

Every printed library dependency has a subset of that set. In particular `Finset.sum_nbij'` has `{propext, Quot.sound}`; its apostrophe is retained in the complete JSON mapping. `pow_add` and `List.prod_cons` report no axioms. There is **no `sorryAx`, unsupported custom axiom, `Lean.ofReduceBool`, or additional mathematical assumption**. The candidate introduces no axiom beyond those already visible in the protected base's factorization infrastructure.

Trusted mechanisms are the pinned Lean implementation/kernel, its standard foundational axioms above, and the installed pinned library/toolchain artifacts. `simp`, `omega`, `ring`, ordinary `decide`, and related tactics produce checked proof terms; no native-evaluation proof oracle is used here. The direct resolved `.olean` paths and their hashes are recorded, and the loaded base bodies were printed to check import identity. This review is neither an independent implementation of Lean's kernel nor a rebuild of all historical binary artifacts. Compilation establishes the encoded propositions; source fidelity is the separate audit in Sections 2–3.

## 5. Cutoff and dependency provenance

No network fetch, installation, current documentation lookup, or external literature theorem was used in this review. Mathematical deductions in the candidate are local; the Mangerel paper mentioned in the project ledger is not a candidate dependency.

`lean-toolchain` pins `leanprover/lean4:v4.32.2`; `lakefile.toml:8–11` pins Mathlib to `905b95818eb32af7874a58b427f50c1711a5e96c`. All nine package HEADs were independently compared with the manifest, and all tracked package worktrees were clean. Inherited `inputRev` labels such as `main` are resolved by the fixed manifest hashes, not fetched as current branches. Actual `LEAN_PATH` and direct import resolution are in the log.

Local preserved public-availability metadata supports the cutoff, not just Git author dates:

- `formal/environment/lean-release.stdout`: Lean v4.32.2, publicly released `2026-07-28T16:34:35Z`, `https://github.com/leanprover/lean4/releases/tag/v4.32.2`.
- `formal/environment/mathlib-release.stdout`: Mathlib v4.32.2, published `2026-07-28T16:47:51Z`, `https://github.com/leanprover-community/mathlib4/releases/tag/v4.32.2`.
- `formal/environment/public-availability-witnesses.json`: dated public CI records bound to the exact Lean/Mathlib and package commit SHAs. For Mathlib, for example, `https://github.com/leanprover-community/mathlib4/actions/runs/30385574037` records the exact pin on July 28. The JSON evidence retains a matching pre-cutoff witness and URL for every manifest package.

| Package | Manifest/actual commit | Recorded public witness date |
|---|---|---|
| plausible | `e12c1910fe855cbfc38803cd4e55543906d5fa62` | 2026-07-13 |
| LeanSearchClient | `c5d5b8fe6e5158def25cd28eb94e4141ad97c843` | 2026-02-12 |
| importGraph | `7e9612bf0b9ee66db3cb5b9988a35afc706f5a12` | 2026-07-13 |
| proofwidgets | `6e311e2a844da9b2cc3971187df2fe0066947b93` | 2026-07-13 |
| aesop | `a7dbf0c63b694e47f425f3dcddbc0e178bb432d3` | 2026-07-15 |
| Qq | `38d591e778f100aec9762bb582f9c7f55f50e9dc` | 2026-07-13 |
| batteries | `023ce7d62a0531e22a5331e20b587817a80d49ff` | 2026-07-15 |
| Cli | `88679d088c9720c27ebdf2ba4dafe17341747f94` | 2026-07-13 |
| mathlib | `905b95818eb32af7874a58b427f50c1711a5e96c` | 2026-07-28 |

These dates precede the inclusive 2026-07-31 cutoff. This audit independently binds local revisions to the preserved metadata; it did not repeat the historical GitHub queries. The inspected library-source hashes are in the JSON. The leader should carry these dependency records into the final provenance ledger; this reviewer did not edit `sources.md`.

## 6. Remaining exact obligations and routing

The helper snapshot has 44 theorem signatures. The actual file implements precisely the first 42 and omits these final two:

```lean
ArithmeticStatement.pointwise_keystone
  (N : ℕ) (hEven : Even N) (hN : 2 < N) :
  2 * L (N - 1) - ((N : ℤ) - 1) < C N

ArithmeticStatement.liouville_goldbach : Target
```

They remain mathematical proof obligations, not declarations accepted from the signature-only snapshot. Equivalently, the unresolved core goal is:

```lean
∀ p q : ℕ,
  Nat.Prime p → Nat.Prime q → HasRepresentation (2 * p * q)
```

The checked equivalences do not discharge that goal. Universal coverage of multiples of 8 and the diagonal sign class does not supply all other even inputs. No sufficiently-large threshold plus finite remainder, all-input positivity estimate, or unconditional proof of `Target` is present.

**Protection/integration decision:** yes for these exact 42 statements and their eight definitions, with the protected base unchanged. The unproved endpoint types remain legitimate protected goals, not accepted dependencies. Any semantic change invalidates this review and the matching readback coverage.

**Next owner:** the leader may route this exact partial artifact to the designated integrator, who must mechanically integrate it and rerun the integrated build, exact module compilation, statement/dependency and axiom checks. The leader must separately route the unresolved universal theorem to proof development. Final exact-target proof, integrated-version review/regulation and original-request completion remain open. No candidate source was merged or repaired by this reviewer.
