# Shared informal-to-Lean evidence map

Status: checked and integrated PARTIAL results; the original Target remains UNRESOLVED.

## Authoritative per-declaration map

[Complete 42-theorem and 11-definition map](formal/integration/source-proof-map-v1.txt) records every informal lemma ID, actual declaration and line, immediate dependencies, source provenance, proof status, and common review evidence. Its SHA-256 is `98fe3ef1958403c629e55d0a97fff50f5b2270c3e157e0e8f08664675888e977`. That immutable detailed table is incorporated into this shared map, not replaced by the summary below.

All names are in namespace `ArithmeticStatement`. Master file: `lean/Statement/Partial.lean`, SHA-256 `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0`. Base definitions: `lean/Statement/Definitions.lean`, SHA-256 `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d`.

## Principal dependencies and outcome

| Informal IDs | Lean declarations | Dependency bridge | Status |
|---|---|---|---|
| C01 | omega_one, lambda_one, lambda_sign | factor-list unit; integer exponent parity | Checked, integrated |
| E01 | omega_mul, lambda_mul, lambda_prime, lambda_two/three/four/five, lambda_two_mul, lambda_square | pinned factor-list multiplicativity, positive inputs | Checked, integrated |
| E03 | hasSignedRepresentation_mul, representation_scaled_sign | positive witness scaling, lambda_mul | Checked, integrated |
| E02 | representation_double, representation_diagonal | equal witnesses; doubling changes sign | Checked partial family |
| E04/E05.8 | representation_two_sign_seed, eight_two_sign_seed, representation_multiple_eight | 3+5 and 4+4; sign-adaptive scaling | Checked all positive multiples of 8 |
| C02 | mem_I_iff, interval_eq_Icc, interval_bounds, interval_card_cast, reflection_mem, reflection_involutive, reflection_bijection | exact positive interval; guarded subtraction/casts | Checked, integrated |
| C03 | sum_lambda_interval, sum_lambda_reflection | inclusive endpoint and reflection bijection | Checked, integrated |
| C04 | mem_orderedRepresentations, orderedRepresentations_eq_image, representation_count_eq_card_indices | actual ordered pairs; injective first-coordinate map | Checked, integrated |
| C05/C06 | two_sign_indicator, representation_count_eq_indicator_sum | four sign cases; actual cardinality | Checked, integrated |
| C07 | four_mul_representation_count | C02–C06; integer finite-sum expansion | Checked exact identity |
| C08/C09 | representation_count_pos_iff, count_pos_iff_keystone, keystone_ge_four_iff | positive cardinality and integer margin | Checked equivalences only |
| A01 | target_iff_forall_hasRepresentation, target_iff_count_pos, target_iff_pointwise_keystone | exact Target unfolding and C08/C09 | Checked reductions, not Target |
| PC00 | exists_prime_pair_factor_of_lambda_one | two factor occurrences and positive-sign remainder | Checked; allows equal primes and remainder 1 |
| PC01 | target_iff_prime_product_core | diagonal or positive-sign scaling | Checked equivalence, not uniform core existence |
| K01 | pointwise_keystone (not declared) | new universal strict correlation bound needed | OPEN mathematical gap |
| Core | forall primes p,q, HasRepresentation (2*p*q) | equivalent residual via PC01 | OPEN mathematical gap |
| Final | liouville_goldbach : Target (not declared) | must discharge K01, Core, or another exact full proof | UNRESOLVED |

## Evidence common to every checked declaration

- Exact helper signatures: `formal/blueprinter/interfaces-v1.lean`, hash `89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc`. The two final proof-erased endpoint signatures are explicitly open and never imported.
- Base blind readback and fidelity: `formal/reviews/statement-readback-v1.md`, `statement-fidelity-v1.md`.
- Helper blind readback: `../../review-inputs/r20260924-v1/interfaces-readback.md`; fidelity: `formal/reviews/helper-fidelity-v1.md`.
- Exact checked-candidate review: `formal/reviews/candidate-audit-v1.md` plus actual independent compile log/JSON.
- NL derivations: `nl/generator/proof-v2.md` (v1 partial proof review preserved); self-contained final exposition `FINAL_ARGUMENT.md`, hash `1b93364b818b0eae95875d391ca6f944614f00b963a1e384ba1a0fe2533957a9`.
- Two fresh final reviews of that exact integrated version: `nl/reviews/final-review-a-v2.md`, `nl/reviews/final-review-b-v1.md`. They support the partial argument, not success on Target. `final-review-a-v1.md` is superseded for final certification because of stale metadata and prior-review exposure; it is retained as evidence, not counted.
- Actual default build, explicit Partial build, direct Lean, trust-zero Lean and root-import checks: `formal/integration/audit-v1.json` and `v1-*` raw records. All required positive checks exited 0. Negative endpoint checks exited 1 as expected because no endpoint theorem exists.
- All 42 theorems have only `propext`, `Classical.choice`, `Quot.sound` as transitive axioms; no admitted proof, custom mathematical axiom, native-decide assumption, or circular endpoint premise. Pinned dependencies and trusted artifact mechanisms are documented in `sources.md` and `REPRODUCE.md`.

## Multiples-of-four continuation

The user-directed continuation in `waves/multiples-four/` is PROVED AND ACCEPTED. Exact theorem: `ArithmeticStatement.representation_multiple_four (m : ℕ) (hm : 0 < m) : HasRepresentation (4*m)`, in `lean/Statement/FourWork/Assembly.lean:21–24`, SHA-256 `fb279bfbb469022b119c37d011cfcf47852a3fe25dea03fac966379351437066`. No additional premise remains.

The authoritative [wave lemma map](waves/multiples-four/LEMMA_MAP.md) records all 38 new theorem interfaces, proof dependencies, source provenance and review evidence. Full exposition is `waves/multiples-four/PROOF.md`; exact acceptance is `waves/multiples-four/formal/reviews/final-four-regulator-v1.md`, supported by two independent final NL reviews and integrated compiler/axiom checks. Earlier baseline hashes above remain historical evidence and do not describe the extended root import graph. The original all-even Target remains unresolved; it is not replaced by this lemma.

## Unaccepted, rejected and deferred material

PB and LS/LS-square are unproved sufficient routes, not Lean assumptions. The optional universal strict-prefix route O-M5 is refuted at q=5, L(4)=0. Finite seed/partner/square-template failures concern methods, not counterexamples to Target. Other seed families and the pigeonhole lower bound are not claimed as integrated theorems. The Python audit is finite, non-Lean evidence; its historical PB-label mapping is unresolved. No external analytic paper theorem is a proof dependency.
