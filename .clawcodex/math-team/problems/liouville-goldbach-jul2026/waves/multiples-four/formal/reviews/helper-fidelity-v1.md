# Helper-interface fidelity review v1

Mode: CERTIFICATION — statement fidelity only.

**VERDICT: APPROVE.** All 19 supplied helper signatures faithfully express the corresponding assertions or intermediate conclusions in the supplied source §§1–4, with the normalizations recorded below. No statement-fidelity mismatch or missing review input was identified.

**Protection for proof work: YES**, for these exact 19 signatures under the exact defining dependencies identified below. This is not approval of a proof, completion of T4, or completion of the original all-even target. The candidate consists of theorem headers without proof bodies.

## 1. Scope and snapshot identity

Path abbreviations:

- `R = .clawcodex/math-team`
- `P = R/problems/liouville-goldbach-jul2026`
- `W = P/waves/multiples-four`
- `N = R/review-inputs/r20260924-four-v1`
- `M = P/lean/.lake/packages/mathlib`
- `L = ~/.elan/toolchains/leanprover--lean4---v4.32.2/src/lean`

The comparison uses `W/request.md`, the mathematics of `W/nl/generator/proof-attempt-v1.md` §§1–4, the exact candidate, the supplied literal readback and neutral dependencies, and the actual fixed definitions. No earlier review or author-confidence judgment was used. No candidate was edited, no proof was supplied, and no agent or team/task tool was invoked. The only output written is this report.

SHA-256 hashes were computed from file bytes:

| Input, in manifest order | SHA-256 |
|---|---|
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `W/nl/generator/proof-attempt-v1.md` | `1730e39b6ef4eb33bc4621e26642d63b4c775415a4cdeec7de00ccff71fa89ef` |
| `W/formal/generator/four-interfaces-v1.lean` | `be55b4df2e640ec4645a2544b0013de5d6f366439162820af4233162766a0cee` |
| `N/Interfaces.lean` | `be55b4df2e640ec4645a2544b0013de5d6f366439162820af4233162766a0cee` |
| `N/Declaration.lean` | `bdfb30bcfade7b9df33e48f280125d10a40dd76f365cf5b87047183475fee7ed` |
| `N/Dependencies.lean` | `fd4ec312622db449d27d6ac0b18b1decd62a9f76e18f8251bb40ffbabdef7981` |
| `N/ListOperations.lean` | `925cbf08a1aac0870075ad56ff2d95c7b0eb94c87853ace32d0043a9c094e2bc` |
| `N/interfaces-readback.md` | `693e7d4a45e5e3e0e1afefbee6c4232b2f4b5a5eb308c85344881afe0e0f1a6d` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `P/lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` |
| `P/lean/lakefile.toml` | `0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4` |
| `P/lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` |

The 13-input snapshot digest is **`8763777f5cb862137281280e0850ac6fde4ad0bb2b66e06e37b1e2699ff4486a`**. Its reproducible encoding is the concatenation, in table order, of `<file SHA-256><two ASCII spaces><file path relative to R><LF>`, UTF-8 encoded, then SHA-256 hashed. The source fragment comprising lines 47–180 inclusive, preserving line endings (8835 bytes), has SHA-256 `8bc4f3601ce91697a3688a278d59924265a5b8d43b8387e53ded26f4039f5376`.

The candidate matches the user-supplied hash and is byte-identical to `N/Interfaces.lean`. Direct byte comparisons also confirmed:

- `N/Declaration.lean:5–7` equals `Definitions.lean:6–8` (`omega`, `lambda`).
- `N/Declaration.lean:9–15` equals `Partial.lean:14–20` (the two representation predicates).

Thus the literal readback concerns the same interface text and defining predicates, rather than a differently normalized candidate. Its literal account was checked against the code; its label was not used as a source-fidelity verdict.

## 2. Definitions, target, and normalization audit

The exact requested T4 is `∀ m : ℕ, 0 < m → HasRepresentation (4 * m)` (`W/request.md:9–14`; `N/Declaration.lean:17–18`). Positive integers are encoded by natural numbers with explicit strict positivity. This includes `m = 1`.

`omega n` is the **length of the prime-factor list, counting multiplicity**, not the number of distinct primes (`Definitions.lean:6`). The actual pinned recursion removes one least prime factor per list entry (`M/Mathlib/Data/Nat/Factors.lean:38–44`); its prime-power list has repeated entries (`:181–182`). `lambda n = (-1 : ℤ) ^ omega n` is integer-valued (`Definitions.lean:8`), so the negative sign is not natural-number subtraction.

Expanding `Partial.lean:14–20`, a representation of `N` means exactly:

`∃ a b : ℕ, 0 < a ∧ 0 < b ∧ N = a + b ∧ lambda a = (-1 : ℤ) ∧ lambda b = (-1 : ℤ)`.

Consequently:

- Both summands must individually be positive and individually have sign **−1**. A product-of-signs condition or an unspecified common sign has not replaced this requirement.
- Equal summands are allowed. There is no primality, coprimality, parity, distinctness, or ordering restriction on representation witnesses.
- `HasSignedRepresentation` has parameters `s : ℤ`, then `N : ℕ`. The seed theorem uses separate witness pairs for its −1 and +1 conjuncts; it does not require one pair to have contradictory signs.
- Empty factor lists at 0 and 1 give `lambda 0 = lambda 1 = 1`. The extension at zero does not supply a representation witness or a positive input: the relevant strict positivity premises prevent that loophole.
- Actual `Even m` is `∃ r : ℕ, m = r + r`, generated by the additive counterpart of `IsSquare` (`M/Mathlib/Algebra/Group/Even.lean:50–57`). It imposes no unintended sign condition.
- Actual `Nat.Prime p` is `Irreducible p`, with the supplied smaller-divisor characterization verified in the pinned source (`M/Mathlib/Data/Nat/Prime/Defs.lean:42–43,97–112`). In particular it excludes 0 and 1 and includes 2.

The candidate has exactly 19 theorem headers, no new `def`, structure, axiom, local variable block, or target redefinition. Its namespace and `autoImplicit false` introduce no extra hypotheses. Arithmetic operations and the typeclass argument of `Even` specialize to the fixed natural/integer instances; there is no quantified algebraic structure, `Fact` assumption, or hidden mathematical typeclass premise.

The original `Target` remains the fixed all-even assertion `∀ N : ℕ, Even N → 2 < N → ...` (`Definitions.lean:10–14`; `Partial.lean:98–100`). Neither T4 nor the residue-class helper replaces or narrows that definition.

### Source normalizations, not mismatches

1. Source nonnegative square coordinates are `u v : ℕ`. Source positive totals are expressed by `0 < m`; primality already ensures a positive prime total.
2. `m = p*d` is encoded as `m = d*p`, using commutativity, with no altered factor restriction.
3. Helpers 11–13 do not retain the oddness assumption from the initial presentation in §2.1. This is supported by the source's explicit extension of the same sign/cofactor/scaling calculation beyond odd `m` in §4, line 176, together with §1's positive factorization and unrestricted multiplicativity. Their prime input may be 2; no odd-prime conclusion was silently retained after dropping oddness.
4. For a natural prime, `p ≠ 2` expresses the source's odd-prime restriction. It is not used to restrict arbitrary representation witnesses.
5. The square-sum helpers express the source's existential representation conclusion, not its particular witness algorithm. They therefore do not introduce an ordering condition on `u,v` or accidentally replace the source's absolute difference by truncated natural subtraction.

## 3. Audit of all 19 signatures

In this table, `G(N)` abbreviates the exact negative representation predicate above, and `S(s,N)` abbreviates the fixed signed predicate; these are report notation only, not new Lean definitions. All input variables are natural numbers. Header parameters in braces are universal in their displayed order, just like explicit parameters. Subsequent hypotheses are implications; each representation conclusion introduces its own `a`, then `b`, after all inputs and hypotheses.

`I` denotes `W/formal/generator/four-interfaces-v1.lean`; source locators refer to `W/nl/generator/proof-attempt-v1.md`.

| # | Exact declaration and code locator | Source locator | Signature finding |
|---|---|---|---|
| 1 | `lambda_six`, I:7–8 | §2.3, 101–105 | `lambda 6 = (1 : ℤ)`. Correct fixed positive sign; no hypothesis. |
| 2 | `lambda_seven`, I:10–11 | §1.3, 53; §2.3, 103–105 | `lambda 7 = (-1 : ℤ)`. Correct fixed negative sign; source supplies primality of 7, not a new premise. |
| 3 | `twelve_two_sign_seed`, I:13–15 | §2.3, 101–105 | `S(-1,12) ∧ S(1,12)`. Two independent positive-witness existentials, in the stated sign order. |
| 4 | `representation_multiple_twelve`, I:17–18 | §2.3, 105 | Every `t > 0` has `G(12*t)`, with no condition on `lambda t`. |
| 5 | `representation_multiple_four_of_lambda_one`, I:20–22 | §2.1, 64–66; §4, 175 | For arbitrary `m`, `0 < m → lambda m = 1 → G(4*m)`. Includes `m=1`; equal witnesses are permitted. |
| 6 | `representation_multiple_four_of_even`, I:24–26 | §1.6, 56; §2.1, 67 | `0 < m → Even m → G(4*m)`. No sign restriction; the even case is a partial sufficient condition. |
| 7 | `representation_multiple_four_of_three_dvd`, I:28–30 | §2.3, 105; §4, 175 | `0 < m → 3 ∣ m → G(4*m)`. No oddness or sign premise. |
| 8 | `representation_multiple_four_of_sum_two_squares`, I:32–34 | §3.1, 113–123 | Universal inputs `m,u,v`, then `0 < m` and `m=u^2+v^2`, then `G(4*m)`. **Both the equal-coordinate case and either zero coordinate are allowed.** |
| 9 | `prime_one_mod_four_eq_sum_two_squares`, I:36–38 | §3.2, 127–151 | Arbitrary prime `p` with `p % 4 = 1`, then `∃ u v : ℕ, p=u^2+v^2`. Coordinates depend on `p`; no positivity/distinctness requirement was added to them. |
| 10 | `representation_four_prime_one_mod_four`, I:40–42 | §3.2, 153–155 | The same prime/residue hypotheses imply `G(4*p)`. No square decomposition is assumed as an extra endpoint premise. |
| 11 | `prime_divisor_positive_sign_cofactor`, I:44–47 | §1, 52,58; §2.1, 69–75; §4, 176 | Inputs `m,p`; hypotheses `m>0`, `lambda m=-1`, primality, divisibility; then `∃ d, 0<d ∧ lambda d=1 ∧ m=d*p`. The prime divisor is **arbitrary**, not a specially chosen one. |
| 12 | `exists_prime_factor_of_lambda_neg_one`, I:49–52 | §1, 58; §2.1, 69–75; §4, 176 | After `m>0` and `lambda m=-1`, existential `p`, then `d`, with primality, positive cofactor, cofactor sign +1, and `m=d*p`. No fixed prime is selected before `m`. |
| 13 | `representation_multiple_four_of_prime_divisor`, I:54–58 | §2.1, 75–79; §4, 176 | Same universal `m,p` and four arithmetic hypotheses as 11, then **premise** `G(4*p)`, then conclusion `G(4*m)`. This is the source's conditional forward scaling implication, not division of witnesses or unconditional prime-core solvability. |
| 14 | `representation_multiple_four_of_prime_one_mod_four_dvd`, I:60–63 | §4, 176 | `m>0`, prime `p`, `p∣m`, and `p%4=1` imply `G(4*m)`. Omitting a sign hypothesis matches the source's two-sign case split. |
| 15 | `exists_prime_one_mod_four_of_lambda_neg_one`, I:65–68 | §4, 177 | `m>0`, `m%4=1`, and `lambda m=-1` imply existence of a prime divisor with residue 1. It does not assert that every prime divisor has that residue. |
| 16 | `representation_multiple_four_of_mod_four_one`, I:70–72 | §4, 177 | `m>0` and `m%4=1` imply `G(4*m)`. The negative-sign subcase is not imposed on this final partial-family conclusion. |
| 17 | `representation_multiple_four_of_mod_four_ne_three`, I:74–76 | §4, 179 | `m>0` and `m%4≠3` imply `G(4*m)`. This covers residues 0,1,2 **only as a partial result**, not as T4. |
| 18 | `multiple_four_iff_odd_prime_core`, I:78–80 | §2.2, 83–91 | `(∀ m, 0<m → G(4*m)) ↔ (∀ p, Nat.Prime p → p≠2 → G(4*p))`. Exact equivalence of whole universal propositions, including both logical directions. The right side includes prime 3. |
| 19 | `multiple_four_iff_prime_three_mod_four_core`, I:82–85 | §4, 161–171 | The same unrestricted T4 left side is equivalent to `∀ p, Nat.Prime p → 7≤p → p%4=3 → G(4*p)`. Bound 7 is inclusive, prime 3 is excluded, and no upper bound or other restriction is present. Neither endpoint is assumed or separately asserted. |

Every row passes fidelity review. The source seed values 6, 7, and 12, multiplier/modulus 4, odd-prime exclusion 2, and final inclusive threshold 7 are fixed source constants, not unjustifiably chosen existential constants.

## 4. Degeneracy, logical scope, and residual obligations

- `m=0` and `t=0` are explicitly excluded in positive-input helpers. `m=1` is included wherever its other hypotheses hold; its failure to satisfy a negative-sign premise is expected, not a contradictory global assumption.
- For helper 8, `u=v` is not excluded; either coordinate may be zero. Only `u=v=0` is incompatible with the positive total. The square coordinates are not themselves required to be representation witnesses.
- Prime inputs exclude 0 and 1 by their actual definition. The exclusions of 2 in helper 18 and of 3 in helper 19 are exactly the source reductions, not changes to T4's domain.
- Cofactor `d=1` is allowed. Repeated prime factors are allowed; neither `p` and `d` nor any witness pair is required to be coprime. The positive cofactor sign is explicitly +1, preserving the required output sign −1.
- No global hypothesis set is accidentally unsatisfiable. The two-sign seed has separate witnesses, and the final core has genuine prime inputs, including its boundary prime 7. Local impossibility at excluded inputs is ordinary conditional scope.
- Quantification is pointwise in each total, followed by existential witnesses that may vary with that total. No single universal witness pair is requested. The source's sum/product equalities remain aggregate equalities; no estimate or aggregate bound has been rendered pointwise.
- Helper 13 is expressly conditional on its particular prime representation. Helpers 18–19 unconditionally state **equivalences**, not either universal endpoint. The source expressly leaves C3 unproved (§4, 161–171). No C3 assumption has been appended to the requested unconditional theorem.
- The `m%4≠3` helper cannot be substituted for T4. The helper file contains no standalone unconditional `representation_multiple_four` proof and no proof of C3. The original all-even target is also unchanged and not settled by this approval.

**Mismatch details:** none. The domain/sign/quantifier normalizations in §2 are source-supported and introduce neither new mathematical assumptions nor a narrowed original target.

All 19 helper proofs remain obligations of subsequent proof work. This review does not certify the mathematical derivations in the prose, elaboration of future proof bodies, kernel checking, or an axiom audit. Adding proof bodies will change the whole-file hash; the protected signature text and defining dependencies must remain unchanged. Any mathematical signature or defining-dependency change requires fresh readback and fidelity review.

## 5. Pinned dependencies and execution boundary

The actual `lakefile.toml:8–11`, manifest mathlib entry, and checked-out mathlib HEAD all identify **`905b95818eb32af7874a58b427f50c1711a5e96c`**. Local git author and committer dates are both `2026-07-28T18:36:13+02:00`, within the inclusive 2026-07-31 cutoff. All nine local manifest package HEADs match their locked revisions; their recorded author/committer dates are also no later than the cutoff. No package was fetched, updated, installed, or substituted, and no external literature result was introduced.

Project and mathlib `lean-toolchain` files both specify `leanprover/lean4:v4.32.2`. The installed binaries report Lean 4.32.2, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`, and Lake `5.0.0-src+f3b06c7`. Available commands were inspected, not presumed. Only version/identity checks were run; **no candidate compilation or proof/axiom check was performed or claimed**. The headers have no proof bodies and are not a completed Lean development.

Additional inspected defining-source identities:

| File | SHA-256 |
|---|---|
| `M/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `M/Mathlib/Data/Nat/Prime/Defs.lean` | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` |
| `M/Mathlib/Algebra/Group/Even.lean` | `1180fa9ac282e55257e95c8402acd7314fcbd0a18bcfdede92a3cde16e1db630` |
| `L/Init/Prelude.lean` | `44f86ebbb9ab743a05c6ebe2c674aadbf2c822bee874f1b16d7e6c8d56318dc9` |
| `L/Init/Data/List/Basic.lean` | `c6b61f1b5fcac4ea4339625f2e66916d1f2c1ae2531c10ee45b401846ffb6061` |

The three mathlib defining-source files have no diff from pinned HEAD. `Nat.minFacAux/minFac` were inspected at `Prime/Defs.lean:207–219`; list length at `Init/Prelude.lean:3027–3029`; and list replication/length equations at `Init/Data/List/Basic.lean:84–90,705–707`. These confirm the supplied neutral dependencies' intended operations rather than merely trusting their names.

Next owner: the leader, for protection and routing of the exact approved helper types. Proof production, independent mathematical review, pinned compilation, and axiom checks remain separate acceptance stages.
