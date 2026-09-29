# Reproduce the checked partial Lean development

**Status: partial results only. The original conjecture remains unresolved.**
There is no theorem `ArithmeticStatement.liouville_goldbach` and no theorem
`ArithmeticStatement.pointwise_keystone` in the built development.
`ArithmeticStatement.Target` defines the requested proposition; it does not prove it.

## Exact environment

- Lean toolchain: `leanprover/lean4:v4.32.2`.
- Lean commit: `f3b06c705e6c85f5314019d5d3baab0fec5b580c`.
- Recorded platform: `arm64-apple-darwin24.6.0`.
- Lake: `5.0.0-src+f3b06c7`.
- Mathlib release: v4.32.2, pinned by commit, not by a mutable tag.
- Root manifest SHA-256: `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03`.

All nine manifest packages are locked:

| Package | Revision |
|---|---|
| mathlib | `905b95818eb32af7874a58b427f50c1711a5e96c` |
| plausible | `e12c1910fe855cbfc38803cd4e55543906d5fa62` |
| LeanSearchClient | `c5d5b8fe6e5158def25cd28eb94e4141ad97c843` |
| importGraph | `7e9612bf0b9ee66db3cb5b9988a35afc706f5a12` |
| proofwidgets | `6e311e2a844da9b2cc3971187df2fe0066947b93` |
| aesop | `a7dbf0c63b694e47f425f3dcddbc0e178bb432d3` |
| Qq | `38d591e778f100aec9762bb582f9c7f55f50e9dc` |
| batteries | `023ce7d62a0531e22a5331e20b587817a80d49ff` |
| Cli | `88679d088c9720c27ebdf2ba4dafe17341747f94` |

The source cutoff is **2026-07-31 inclusive**. Preserved exact-SHA public CI
witnesses predate it for every package and Lean. Lean and Mathlib releases were
published on 2026-07-28. See
`formal/environment/public-availability-witnesses.json`, its matching
`public-ci-*.stdout` raw responses, and `formal/integration/audit-v1.json`.
Integration rechecked installed revisions and clean tracked package sources;
it performed no network fetch, package update, or installation.

Do **not** run `lake update`, replace the manifest, resolve its historical
`main`/`master` input labels, or substitute a newer toolchain/library. Those
labels are metadata; the fixed `rev` fields are the dependencies actually used.

## Build and check

These commands check the supplied checkout with its already provisioned pinned
Lean toolchain and same-pin dependency artifacts. Run from this problem's
`lean/` directory:

```bash
lake env lean --version
lake --version
lake build
lake build Statement.Partial
lake env lean Statement/Partial.lean
lake env lean -t 0 Statement/Partial.lean
lake env lean --stdin < ../formal/integration/v1-08-root-import-check.stdin.lean
```

Every command above actually ran successfully during integration, with exit 0.
The default build completed 925 jobs and explicitly built `Statement.Partial`
then root `Statement`. The root module imports `Statement.Partial`, so this is
not merely a successful scratch-file compilation. The direct module check
prints all 82 axiom reports. The last command imports **only root `Statement`**,
checks all 50 added declarations, prints the 11 local/base defining bodies,
and repeats all 82 axiom reports from the imported compiled module.

There are four harmless unused-variable warnings at `Partial.lean` lines
51, 171, 187, and 291. Their protected hypotheses were not removed.

To check the deliberately missing endpoints:

```bash
lake env lean --stdin < ../formal/integration/v1-09-absent-endpoints.stdin.lean
```

This negative check is expected to exit **1**, with exactly the two
`Unknown identifier` diagnostics for `ArithmeticStatement.pointwise_keystone`
and `ArithmeticStatement.liouville_goldbach`. This is an absence check, not a
failed proof accepted as a theorem.

The same-pin cache's original setup commands and results are preserved in
`formal/environment/cache-factors.json` and
`formal/environment/fl-generator-cache-required-v1.json`; toolchain and exact
checkout setup are documented in `formal/environment/environment-report.txt`.
A cold-machine bootstrap was not repeated during integration. Existing upstream
compiled artifacts are trusted build artifacts; the checks above are not a
from-source rebuild of every upstream library. The `-t 0` check requests Lean's
trust-zero checking of imports and also passed.

## Available declarations

Master: `lean/Statement/Partial.lean`; namespace: `ArithmeticStatement`.
Its SHA-256 is
`9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0`,
identical to the independently approved candidate.

Principal proved results:

- `ArithmeticStatement.representation_multiple_eight`: every `8*m`, `m>0`, has the required positive negative-sign pair.
- `ArithmeticStatement.representation_diagonal`: covers even `N>2` with `lambda N=1`.
- `ArithmeticStatement.four_mul_representation_count`: for `N≥2`, the exact integer identity `4*(R N : ℤ) = ((N : ℤ)-1)-2*L(N-1)+C N`.
- `ArithmeticStatement.target_iff_pointwise_keystone`: equivalence with a strict bound required separately at every admissible `N`.
- `ArithmeticStatement.target_iff_prime_product_core`: equivalence with representations of `2*p*q` for every pair of primes, including repeated primes.

Complete 42-theorem inventory, with the common namespace omitted:

```text
omega_one                         lambda_one
lambda_sign                       omega_mul
lambda_mul                        lambda_prime
lambda_two                        lambda_three
lambda_four                       lambda_five
lambda_two_mul                    lambda_square
target_iff_forall_hasRepresentation
hasSignedRepresentation_mul       representation_scaled_sign
representation_double             representation_diagonal
representation_two_sign_seed      eight_two_sign_seed
representation_multiple_eight     mem_I_iff
interval_eq_Icc                   interval_bounds
interval_card_cast                reflection_mem
reflection_involutive             reflection_bijection
sum_lambda_interval               sum_lambda_reflection
mem_orderedRepresentations        orderedRepresentations_eq_image
representation_count_eq_card_indices
two_sign_indicator                representation_count_eq_indicator_sum
four_mul_representation_count     representation_count_pos_iff
count_pos_iff_keystone             keystone_ge_four_iff
target_iff_count_pos               target_iff_pointwise_keystone
exists_prime_pair_factor_of_lambda_one
target_iff_prime_product_core
```

The eight helper definitions and per-declaration informal IDs, dependency/source
map, proof status, line numbers, and review links are recorded in
`formal/integration/source-proof-map-v1.txt`.

## Proof and statement checks

- All 42 theorem signatures and eight helper definition bodies exactly match
  `formal/blueprinter/interfaces-v1.lean` under proof-body removal and trailing
  separator-whitespace removal. Internal signature text is unchanged.
- The base `lean/Statement/Definitions.lean` remains byte-identical to
  `formal/approved-v1/Definitions.lean`, SHA-256
  `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d`.
- Fidelity/readback coverage is bound to these exact snapshots by
  `formal/reviews/candidate-audit-v1.md`; integration introduces no semantic change.
- Each of the 42 theorems and 11 local/base definitions has exactly the transitive
  axioms `{propext, Classical.choice, Quot.sound}`. The 29 printed library
  dependencies use subsets of that set. No `sorryAx`, custom mathematical axiom,
  `Lean.ofReduceBool`, `native_decide`, or admitted obligation occurs in the accepted proof closure.
- The retained old `UnfinishedScaffold` is only a structure requiring a `Target`
  field. No inhabitant is supplied, and `Partial` neither imports nor uses it.

Full commands, exit codes, raw output hashes, proof/snapshot hashes, resolved
imports and axiom maps: `formal/integration/audit-v1.json` and `v1-*` records.
Human-readable integration report: `formal/integration/integration-report-v1.txt`.
Change patch: `formal/integration/integration-v1.diff`.

## Remaining exact goals

These are **not declarations or assumptions in the master**:

```lean
-- Given N : ℕ, hEven : Even N, hN : 2 < N, prove:
2 * ArithmeticStatement.L (N - 1) - ((N : ℤ) - 1) < ArithmeticStatement.C N

-- Equivalently, prove:
∀ p q : ℕ, Nat.Prime p → Nat.Prime q →
  ArithmeticStatement.HasRepresentation (2 * p * q)

-- Final missing theorem type:
ArithmeticStatement.Target
```

The identity and equivalences do not prove their positivity/core premise.
Multiples of eight and the diagonal family do not cover all admissible inputs.
No full conjecture proof or counterexample is claimed. Independent final-wave
regulation/acceptance is separate from this mechanical integration record.
