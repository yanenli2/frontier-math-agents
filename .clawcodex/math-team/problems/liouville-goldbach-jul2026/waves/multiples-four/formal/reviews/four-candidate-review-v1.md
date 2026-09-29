# Exact-candidate partial integration review v1

Mode: CERTIFICATION

**VERDICT: APPROVE — the exact 19-declaration partial candidate only.**

The candidate matches the supplied interface and the mathematical assertions in the assigned source sections. Its pinned dependency build and exact-file compilation succeeded. All 48 requested transitive axiom reports contain only the standard base `propext`, `Classical.choice`, and `Quot.sound` (or subsets). This is **not** approval of a proof of the full multiple-of-four statement T4.

**Protection decision:** Yes: these exact 19 theorem types, with the fixed defining dependencies and pins identified below, may be protected for subsequent proof/integration work. No declaration was repaired, proved anew, or edited by this reviewer. Only the integrator may merge them and must rerun the checks on the integrated artifact.

## 1. Scope, sources, and exact identities

Path abbreviations:

- `P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`
- `W = P/waves/multiples-four`
- `M = P/lean/.lake/packages/mathlib`
- `B = .clawcodex/math-team/review-inputs/r20260924-four-v1`

Source locators:

- `W/request.md:9–16`: every natural `m > 0`, including `m = 1`; positive summands, each with sign −1; equal summands allowed; no extra witness or multiplier restrictions.
- `W/nl/generator/proof-attempt-v1.md:47–180`: §§1–4 only. These supply elementary dependencies, the diagonal/even/12-seed cases, prime-divisor scaling, the two-squares family, and the two scoped core equivalences. No other section supplies evidence for this review.
- `B/interfaces-readback.md:17–87,103–140`: the supplied neutral literal readback. Its 19 interfaces are compared with the source independently here; its label is not proof or fidelity evidence by itself.

SHA-256 identities:

| Artifact | SHA-256 |
| --- | --- |
| `W/formal/generator/FourCandidate.lean` | `4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325` |
| `W/formal/generator/four-interfaces-v1.lean` | `be55b4df2e640ec4645a2544b0013de5d6f366439162820af4233162766a0cee` |
| `B/Interfaces.lean` | `be55b4df2e640ec4645a2544b0013de5d6f366439162820af4233162766a0cee` |
| Normalized 19-declaration header snapshot | `20d393bd6cd7e9528ec555c41c00bf610ede2a731d97668bdb81f4cc2d63590c` |
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| Source excerpt, UTF-8 lines 47–180 | `8bc4f3601ce91697a3688a278d59924265a5b8d43b8387e53ded26f4039f5376` |
| `B/interfaces-readback.md` | `693e7d4a45e5e3e0e1afefbee6c4232b2f4b5a5eb308c85344881afe0e0f1a6d` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `M/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `M/Mathlib/NumberTheory/SumTwoSquares.lean` | `ecc1647de087331c1876ca386b495ff2a83943a428bf140bf6ba8047f9fd80f9` |

The normalized snapshot consists of each complete theorem header before `:=`, with whitespace collapsed, in file order, one header per line with a final newline. The JSON records each individual header and its hash. All 19 match both interface files exactly after whitespace normalization, including binder order, implicit/explicit binders, hypotheses, domains, conclusions, and parentheses. A separate compiler diagnostic inspection of all 19 elaborated `#check @...` types confirms that no extra parameters or typeclass premises appear.

## 2. Fixed definitions and readback correspondence

Let `S(s,N)` denote `HasSignedRepresentation s N`, and `G(N)` denote `HasRepresentation N` (not the unrelated counting definition `ArithmeticStatement.R`). The actual imported definitions are:

- `Definitions.lean:6–8`: `omega n = n.primeFactorsList.length` and `lambda n = (-1 : ℤ) ^ omega n`.
- `Partial.lean:14–20`: `S(s,N) = ∃ a b : ℕ, 0<a ∧ 0<b ∧ N=a+b ∧ lambda a=s ∧ lambda b=s`; `G(N) = S(-1,N)`.

These match the request and neutral snapshot `B/Declaration.lean:5–15`. The compiler's printed definitions agree with these source bodies.

I inspected the referenced factor-list definition, not just its name: `Factors.lean:38–44` returns `[]` at 0 and 1 and otherwise conses `minFac n` onto the factorization of `n / minFac n`. Thus repetitions count. `Factors.lean:55–76,181–202` supplies prime membership, product reconstruction for nonzero input, prime-power replication, and the product-list permutation without a coprimality premise. `Prime/Defs.lean:207–219` matches the readback's `minFacAux`/`minFac` recursion. The installed Lean source has `List.length` at `Init/Prelude.lean:3027–3029` and `List.replicate` at `Init/Data/List/Basic.lean:705–707`, matching the neutral list operations.

`Nat.Prime` is actually `Irreducible` on naturals (`Prime/Defs.lean:42–43`); its inspected characterization at lines 107–112 is exactly the readback's natural prime predicate. `Even` is the additive definition `∃ r, m=r+r` (`Algebra/Group/Even.lean:55–57`, generated by `to_additive` and confirmed by `#print`), specialized here to the ordinary addition on naturals.

Consequences relevant to fidelity: `lambda 0 = lambda 1 = 1`; zero summands are explicitly forbidden, and negative-sign summands also cannot be 1. No primality, distinctness, ordering, or coprimality condition is imposed on representation witnesses. The baseline imports `Statement.Definitions`, not an unfinished target scaffold.

## 3. All 19 theorem-type comparisons

All variables displayed below range over `ℕ`; signs are in `ℤ`. Universals and hypotheses are listed in declaration order. Each `G` introduces its own `∃ a ∃ b` after those inputs and hypotheses. `C` and `I` locate the candidate and supplied interface respectively. Every row passes.

| # / declaration | Literal type, abbreviating only fixed definitions | C / I lines | Source locator |
| --- | --- | --- | --- |
| 1. `lambda_six` | `lambda 6 = 1` | C8–9 / I7–8 | §2.3:103 |
| 2. `lambda_seven` | `lambda 7 = -1` | C14–15 / I10–11 | §1:53; §2.3:103–105 |
| 3. `twelve_two_sign_seed` | `S(-1,12) ∧ S(1,12)` | C18–20 / I13–15 | §2.3:101–105 |
| 4. `representation_multiple_twelve` | `∀ t, 0<t → G(12*t)` | C25–26 / I17–18 | §2.3:105 |
| 5. `representation_multiple_four_of_lambda_one` | `∀ m, 0<m → lambda m=1 → G(4*m)` | C29–31 / I20–22 | §2.1:64–66; §4:175 |
| 6. `representation_multiple_four_of_even` | `∀ m, 0<m → Even m → G(4*m)` | C37–39 / I24–26 | §2.1:67; §4:175 |
| 7. `representation_multiple_four_of_three_dvd` | `∀ m, 0<m → 3∣m → G(4*m)` | C46–48 / I28–30 | §2.3:105; §4:175 |
| 8. `representation_multiple_four_of_sum_two_squares` | `∀ m u v, 0<m → m=u^2+v^2 → G(4*m)` | C55–57 / I32–34 | §3.1:113–123 |
| 9. `prime_one_mod_four_eq_sum_two_squares` | `∀ p, Prime p → p%4=1 → ∃ u v, p=u^2+v^2` | C81–83 / I36–38 | §3.2:127–151 |
| 10. `representation_four_prime_one_mod_four` | `∀ p, Prime p → p%4=1 → G(4*p)` | C88–90 / I40–42 | §3.2:153–155 |
| 11. `prime_divisor_positive_sign_cofactor` | `∀ m p, 0<m → lambda m=-1 → Prime p → p∣m → ∃ d, 0<d ∧ lambda d=1 ∧ m=d*p` | C94–97 / I44–47 | §2.1:71–75; §4:176 |
| 12. `exists_prime_factor_of_lambda_neg_one` | `∀ m, 0<m → lambda m=-1 → ∃ p d, Prime p ∧ 0<d ∧ lambda d=1 ∧ m=d*p` | C109–112 / I49–52 | §1:58; §2.1:69–75 |
| 13. `representation_multiple_four_of_prime_divisor` | `∀ m p, 0<m → lambda m=-1 → Prime p → p∣m → G(4*p) → G(4*m)` | C121–125 / I54–58 | §2.1:75–79; §4:176 |
| 14. `representation_multiple_four_of_prime_one_mod_four_dvd` | `∀ m p, 0<m → Prime p → p∣m → p%4=1 → G(4*m)` | C131–134 / I60–63 | §4:176 |
| 15. `exists_prime_one_mod_four_of_lambda_neg_one` | `∀ m, 0<m → m%4=1 → lambda m=-1 → ∃ p, Prime p ∧ p∣m ∧ p%4=1` | C140–143 / I65–68 | §4:177 |
| 16. `representation_multiple_four_of_mod_four_one` | `∀ m, 0<m → m%4=1 → G(4*m)` | C190–192 / I70–72 | §4:177 |
| 17. `representation_multiple_four_of_mod_four_ne_three` | `∀ m, 0<m → m%4≠3 → G(4*m)` | C198–200 / I74–76 | §4:179 |
| 18. `multiple_four_iff_odd_prime_core` | `(∀ m, 0<m → G(4*m)) ↔ (∀ p, Prime p → p≠2 → G(4*p))` | C207–209 / I78–80 | §2.2:83–91 |
| 19. `multiple_four_iff_prime_three_mod_four_core` | `(∀ m, 0<m → G(4*m)) ↔ (∀ p, Prime p → 7≤p → p%4=3 → G(4*p))` | C226–229 / I82–85 | §4:161–171 |

Rows 5–17 use implicit natural parameters in Lean; row 4's `t` and the universals in rows 18–19 are explicit. In row 8, `u,v` are universal supplied square roots, not existentially chosen before `m`. In row 9 they are existential after the prime and residue hypotheses. Row 11 applies to **any supplied** prime divisor, with only `d` existential; row 12 existentially chooses `p` and then `d`. No witness is moved outside its intended dependency scope.

## 4. Positivity, boundaries, logical scope, and vacuity

- The seed's two conjuncts have independent witnesses, namely `(5,7)` and `(6,6)` in C21–23. It does not demand that one pair have both signs. Scaling at C25–27 uses the inspected two-sign lemma `Partial.lean:139–159`, which chooses the correct seed according to the multiplier's sign.
- `m=0` and `t=0` are excluded where needed. `m=1` is retained by the positive-sign case, giving `4=2+2`; it is not accidentally discarded as nonprime. Negative-sign hypotheses exclude `m=1` only in the lemmas that require them.
- The square roots may be zero. In the unequal case, C58–71 orders the roots and writes the larger as the smaller plus a strictly positive natural `w`. Both constructed summands are positive, and the identity is proved in naturals without truncated-subtraction errors. A zero smaller root is allowed. In the equal case C74–78, positivity of `m` implies positivity of `u^2`, permitting the all-8t lemma. Both roots zero cannot satisfy `hm`.
- Cofactors are strictly positive, not merely nonzero informally. `d=1` is allowed. No coprimality of `d,p` is assumed. `Nat.exists_prime_and_dvd` actually requires only `m≠1` (`Prime/Defs.lean:407–408`); C113–118 establishes this from the negative sign and separately retains `hm`, so its possible zero-input use is irrelevant here.
- The prime-divisor implication points from `G(4*p)` to `G(4*m)`, multiplying witnesses by the positive-sign cofactor. It neither divides witnesses nor asserts the core premise. Rows 11–13 do not require oddness of `m`; this is the valid algebraic generalization already reflected in the supplied interface and §4:176, not a weakening of a conclusion.
- C140–188 counts prime **occurrences**. Product reconstruction uses `m≠0` from `hm`; prime 2 is excluded using `m%4=1`; residues are then 1 or 3. Casting the sign identity to `ZMod 4` and using `1≠-1` there faithfully implements §4:177. This does not replace multiplicity by distinct-prime counting, nor assume that `ZMod 4` is a field.
- Both iff statements relate entire universally quantified propositions. Neither is a pointwise `m,p` equivalence, nor a theorem separately asserting either side. The converse in C230–241 explicitly handles prime 3 by the 12-seed and primes 1 modulo 4 by the two-squares result. The residual bound is the inclusive `7≤p`; prime 7 is not silently excluded. Prime 2 is handled by the even case in the first equivalence.
- No contradictory global hypotheses, empty-domain shortcut, aggregate-to-pointwise substitution, or unjustified adjustable constant occurs. The sum equalities are aggregate equalities; positivity and signs apply separately to each summand. There is no uniform witness pair or hidden asymptotic threshold.

## 5. Actual pinned sum-of-two-squares dependency

The actual source at `M/Mathlib/NumberTheory/SumTwoSquares.lean:35–38`, also printed by the exact compilation, is:

```lean
theorem Nat.Prime.sq_add_sq {p : ℕ} [Fact p.Prime]
    (hp : p % 4 ≠ 3) : ∃ a b : ℕ, a ^ 2 + b ^ 2 = p
```

C84 supplies the local `Fact p.Prime` from the explicit `hp`; C85 derives `p%4≠3` from `p%4=1`; C86 reverses the output equality. Thus no hidden primality instance is left as an unmentioned assumption. The output roots are naturals without individual positivity requirements, as needed by the square-sum interface. C92 supplies total positivity using `hp.pos`.

I inspected its actual Gaussian-integer dependencies:

- `Zsqrtd/GaussianInt.lean:243–255`, `sq_add_sq_of_nat_prime_of_not_irreducible`: natural prime plus nonirreducibility of its Gaussian cast yields two natural squares via absolute values of Gaussian coordinates.
- `Zsqrtd/QuadraticReciprocity.lean:34–85`, especially `prime_iff_mod_four_eq_three_of_nat_prime`: with `Fact p.Prime`, Gaussian primality is equivalent to residue 3 modulo 4. Its proof uses quadratic-residue and Gaussian-norm results, not T4 or any representation lemma in this project.

Their SHA-256 hashes are respectively `3b1ad71a44a0ba95fe172fff4adb35c1c3d0ab3dacc0cacca37d6024c51fd12b` and `8b1fa86e4d60240ff76e788a41fa711a762103b08bd3975b00d6f8eb18f38e88`. Both have clean transitive axiom reports in the candidate's 48 checks.

**Proof-route distinction, not a statement mismatch:** §3.2 gives a local inverse-pair/counting argument. The Lean candidate instead imports the pinned Gaussian-integer proof of the same required two-squares assertion. This review does not claim that the prose proof's individual intermediate steps were formalized. The replacement theorem's exact statement, prerequisites, provenance, and noncircularity have been checked.

## 6. Compiler, axiom, and cutoff evidence

All commands ran with working directory `P/lean` and the installed pinned toolchain; no toolchain or dependency was installed or updated.

| Check | Result |
| --- | --- |
| `lake env lean --version` | Exit 0: Lean 4.32.2, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`, release build |
| `lake build Statement.Partial Mathlib.NumberTheory.SumTwoSquares` | Exit 0; build successful. Four replayed unused-variable warnings in baseline `Partial.lean` at 51,171,187,291; no admission diagnostics. |
| `lake env lean .clawcodex/math-team/problems/liouville-goldbach-jul2026/waves/multiples-four/formal/generator/FourCandidate.lean` | Exit 0, 9.829 seconds; all requested diagnostics emitted; no candidate errors or warnings. |
| Secondary `lake env lean --stdin` diagnostic inspection | Exit 0. Input was unchanged candidate text followed only by `#check @` for all 19 declarations and `#print` for defining dependencies. No source file was altered. |

All **48** axiom results match the candidate's 48 `#print axioms` commands in order (the separate `#check Nat.Prime.sq_add_sq` is not an axiom result). All 19 candidate theorems are included. Of the 48:

- 44 report exactly `[propext, Classical.choice, Quot.sound]`.
- `Nat.exists_eq_add_of_le` and `Nat.Prime.eq_two_or_odd` report `[propext]`.
- `ZMod.natCast_mod` and `Int.cast_pow` report `[propext, Quot.sound]`.

No `sorryAx`, custom axiom, native-evaluation/compiler-trust axiom, or other unsupported axiom occurs. Source inspection/search of the candidate and imported project definitions/helpers found no `sorry`, `admit`, custom `axiom`, `native_decide`, unsafe proof bypass, or custom elaborator. The standard base is the same as the inspected fixed baseline. The core assumptions occur only as explicit premises or the appropriate side of an iff, not as an imported axiom or circular proof of T4. Ordinary `decide`, `omega`, `ring`, and rewriting generate checked proof terms here.

Version cutoff: actual mathlib HEAD is the manifest pin `905b95818eb32af7874a58b427f50c1711a5e96c`, author/committer date `2026-07-28T18:36:13+02:00`. Its committed `lean-toolchain` is exactly the project's `leanprover/lean4:v4.32.2`, providing a pre-cutoff reference for that toolchain version. Every package HEAD matches its manifest revision, and all tracked dependency worktrees are clean. Every transitive revision equals the manifest committed at that mathlib pin.

| Package | Revision prefix | Commit date |
| --- | --- | --- |
| mathlib | `905b95818eb3` | 2026-07-28 |
| plausible | `e12c1910fe85` | 2026-07-13 |
| LeanSearchClient | `c5d5b8fe6e51` | 2026-02-12 |
| importGraph | `7e9612bf0b9e` | 2026-07-13 |
| proofwidgets | `6e311e2a844d` | 2026-07-13 |
| aesop | `a7dbf0c63b69` | 2026-07-13 |
| Qq | `38d591e778f1` | 2026-07-13 |
| batteries | `023ce7d62a05` | 2026-07-13 |
| Cli | `88679d088c97` | 2026-07-13 |

Full revisions, author/committer timestamps, commands, outputs, exit statuses, all 48 axiom lists, individual statement hashes, and before/after input hashes are retained in the JSON. All checked source baselines, candidate/interface files, neutral snapshots, and project pins remained unchanged. Only generated build artifacts and the assigned review outputs were written.

Evidence files, relative to `W/formal/reviews`:

- `four-candidate-review-v1.compile.log`: exact-file compiler stdout/stderr, SHA-256 `2275f1fe8774affbdf27f43476dbb493b1dfd8f820f2e7a63c28ce3390816b12`.
- `four-candidate-review-v1.compile.json`: structured checks and raw command outputs, SHA-256 `7b380889526d86a557ba3c389c4f97a3a6f40392349340d7ef5cdcc23e0a79f5`.

## 7. Mismatches, remaining target, and handoff

**Statement/interface/source mismatches: none in the reviewed partial scope.** No required input is missing for this gate. Compilation is supporting proof-status evidence, not the reason for the source-fidelity decision above.

The candidate does **not** declare or prove `representation_multiple_four`. It proves unconditional families (including every positive `m` with `m%4≠3`, and additional cases) and reduces T4 to:

```lean
∀ p : ℕ, Nat.Prime p → 7 ≤ p → p % 4 = 3 →
  ArithmeticStatement.HasRepresentation (4 * p)
```

That prime-core assertion itself remains unproved here, exactly as source §4:161–171 states. The candidate therefore cannot be reported as a proof of every positive multiple of four, still less of the original all-even target.

Next owner: the leader may route this exact partial artifact to the integrator. Preserve the identified types, definitions, baselines, pins, and partial status; rerun compilation and axiom checks after mechanical integration. Any mathematical statement or defining-dependency change invalidates this approval and the corresponding readback coverage.
