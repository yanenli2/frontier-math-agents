Mode: DISCOVERY — conjectural; no proof weight.

# NL-to-Lean map v1

## Scope and status legend

Root `P` is `.clawcodex/math-team/problems/liouville-goldbach-jul2026`.

- `H` = `P/nl/sketcher/formal-handoff-v1.md`.
- `X` = `P/nl/explorer/attempt-v1.md`.
- `S` = `P/formal/blueprinter/interfaces-v1.lean`, SHA-256 `89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc`.
- `D` = protected `P/formal/approved-v1/Definitions.lean`, SHA-256 `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d`.
- Every unqualified proposed Lean name below is in namespace `ArithmeticStatement`.
- **DEFINED/PROTECTED** means an existing definition, not a proved target.
- **PROPOSED** means exact signature in S, no proof supplied or accepted.
- **OPEN** marks the unresolved mathematical target, not an axiom or available premise.
- **DEFERRED** means no declaration scheduled in this bundle.

`S` is code-only signature text with theorem bodies erased, not a compilable or proved development. All new helper statements still require fidelity/readback review; no such review is claimed here. The successful API probe checked existing library types only. See `blueprint-v1.md` for pinned provenance, import blockers, full assembly details, and input hashes.

## Protected definitions and new definitional interfaces

| NL/source | Lean declaration / locator | Meaning and dependencies | Status |
|---|---|---|---|
| request:7; H:25 | `omega`, D:6 | Length of `Nat.primeFactorsList`; counts multiplicity. | DEFINED/PROTECTED |
| request:7; H:25 | `lambda`, D:8 | Integer power `(-1)^omega n`; totalized at zero, not Mathlib's zero-valued arithmetic function there. | DEFINED/PROTECTED |
| A01/A02; request:9-14 | `Target`, D:10-14 | For every even natural N>2, positive a,b, exact sum, both signs -1; equality a=b allowed. | DEFINED/PROTECTED; no proof |
| H:83; X:15-19 | `HasSignedRepresentation`, S:11; `HasRepresentation`, S:16 | Exact witness conclusions only; latter specializes the sign to -1. Depend only on approved lambda. | PROPOSED definitions |
| C02; H:33,39 | `I`, S:19 | `Finset.Ico 1 N`, equivalent to the specified positive filter of `range N`. | PROPOSED definition |
| C04; H:36,60 | `representationIndices`, S:22 | First-coordinate filter with two negative signs. | PROPOSED definition |
| C04; request:81 | `orderedRepresentations`, S:26; `R`, S:31 | Actual finset of ordered pairs, R its natural cardinal. Positive pair bounds are enforced by the interval product. | PROPOSED definitions |
| C03; request:82; H:34-35 | `L`, S:34 | Signed inclusive sum over `Icc 1 x`; no new lambda. | PROPOSED definition |
| C07; request:83; H:37 | `C`, S:37 | Signed sum over `I N` of `lambda a * lambda (N-a)`. | PROPOSED definition |

## Elementary arithmetic and representations

`EX-M` and `EX-S` below are map labels for the explorer's named candidates M and S; they are not claimed to be pre-existing formal IDs.

| NL ID and exact source | Proposed declarations / S lines | Immediate dependencies and source-aligned assembly | Status / priority |
|---|---|---|---|
| C01; H:54-55; EX-M, X:21-27 | `omega_one` 40; `lambda_one` 43 | Approved definitions; `Nat.primeFactorsList_one`; power at exponent 0. | PROPOSED; first |
| C01; H:54; X:15-17 | `lambda_sign` 46 | Approved power definition; `neg_one_pow_eq_ite` specialized to ℤ (or exponent induction). Positive input interface. | PROPOSED; first |
| E01; H:69; EX-M, X:21-27 | `omega_mul` 49 | `Nat.perm_primeFactorsList_mul`, positivity → nonzero, permutation lengths, append length. No coprimality. | PROPOSED; first |
| E01; H:70; EX-M, X:23-25 | `lambda_mul` 52 | `omega_mul`, `pow_add`. Both factors positive; false without these guards for the approved totalization. | PROPOSED; first |
| E01; H:72; EX-M, X:25 | `lambda_prime` 55; `lambda_two` 58; `lambda_three` 61; `lambda_four` 64; `lambda_five` 67 | Prime factor-list singleton; closed prime facts; 4=2*2 and multiplication. Only needed small values are scheduled. | PROPOSED; first |
| E01/E02; X:25 | `lambda_two_mul` 70 | `lambda_two`, `lambda_mul`, integer sign algebra; m>0. | PROPOSED; elementary |
| E01; H:71; X:25 | `lambda_square` 73 | `lambda_mul` and `lambda_sign` (or factor-list powers). t>0. | PROPOSED; optional |
| A01/A02; H:17-23,83 | `target_iff_forall_hasRepresentation` 76 | Unfold the two new representation definitions and protected Target. No new assumptions. | PROPOSED; bridge |
| EX-S; X:29; E03, H:74 | `hasSignedRepresentation_mul` 79 | `lambda_mul`, positive multiplier, original positive witnesses. Produces sign `lambda d*s` at `d*N`. | PROPOSED; early |
| E03; H:74 | `representation_scaled_sign` 83 | Previous scaling or direct `(m*u,m*v)` witnesses; s=±1 and multiplier sign -s. | PROPOSED; early corollary |
| E02; H:73; X:59-63,84 | `representation_double` 90 | Direct witnesses `(m,m)` for sign -1; no need for multiplicativity here. | PROPOSED; early |
| E02; H:73 | `representation_diagonal` 94 | Even N gives N=m+m; N>2 gives m>1; `lambda_two_mul` and lambda N=1 force lambda m=-1; `representation_double`. | PROPOSED; early partial theorem |
| E04; H:75; X:33-35 | `representation_two_sign_seed` 98 | Actual seed witnesses, `lambda_sign` at m, and signed scaling. No unnecessary restriction on seed parity. | PROPOSED; early |
| E05; H:76; X:43,49 | `eight_two_sign_seed` 104 | `(3,5)` negative, `(4,4)` positive; exact small signs. | PROPOSED; first family |
| E05; H:76,89; X:49 | `representation_multiple_eight` 108 | Two-sign seed plus multiplier m>0; equivalently direct case witnesses `(3m,5m)` or `(4m,4m)`. Covers every positive m. | PROPOSED; recommended first substantial target |

## Ordered counting, reflection, and exact signed identity

The count branch depends on `lambda_sign`, not on `lambda_mul`, seed coverage, diagonal coverage, or the optional prime-core branch.

| NL ID and exact source | Proposed declarations / S lines | Immediate dependencies / obligations | Status / priority |
|---|---|---|---|
| C02; H:39,56 | `mem_I_iff` 111; `interval_eq_Icc` 114; `interval_bounds` 117 | `Finset.mem_Ico`, `Finset.mem_Icc`, natural inequalities. Show both summands positive and below N. | PROPOSED; counting foundation |
| C02; H:57 | `interval_card_cast` 120 | `Nat.card_Ico`, `Nat.cast_sub` with 1≤N from N≥2. Result is `(N:ℤ)-1`. | PROPOSED; counting foundation |
| C02; H:58 | `reflection_mem` 123; `reflection_involutive` 126; `reflection_bijection` 130 | Bounds and `Nat.sub_sub_self`. The map is explicitly `N-·` on I N, not a permutation of all naturals. | PROPOSED; counting foundation |
| C03; H:59 | `sum_lambda_interval` 133 | `interval_eq_Icc`; agrees with **L(N-1)**. | PROPOSED |
| C03; H:59 | `sum_lambda_reflection` 136 | `reflection_mem`, `reflection_involutive`, `Finset.sum_nbij'`, `sum_lambda_interval`. `reflection_bijection` is a parallel certificate; the nbij' route uses membership/inverse facts directly. | PROPOSED |
| C04; H:60; request:81 | `mem_orderedRepresentations` 139 | Unfold interval product/filter; positivity and sum give strict upper bounds in the reverse direction. No guard on N is needed for this iff. | PROPOSED; count/existence first |
| C04; H:60 | `orderedRepresentations_eq_image` 144 | Forward `(a,b) ↦ a`; backward `a ↦ (a,N-a)`; exact natural subtraction under sum/bounds. Image theorem plus injectivity supplies the ordered-pair equivalence without a separate subtype Equiv. | PROPOSED |
| C04/C06; H:60,62 | `representation_count_eq_card_indices` 148 | Image theorem and `Finset.card_image_of_injective`, injectivity by first coordinate. Diagonal counted once, non-diagonal orientations separately. | PROPOSED |
| C05; H:61 | `two_sign_indicator` 151 | `lambda_sign` for both positive inputs; four sign cases. Indicator and factor 4 are in ℤ. | PROPOSED |
| C06; H:62 | `representation_count_eq_indicator_sum` 156 | Actual R-to-index cardinal equality, `Finset.sum_filter`, integer constant sum. No algebraic redefinition of R. | PROPOSED |
| C07; H:63; request:76-85 | `four_mul_representation_count` 162 | C02 card, C03 both sums, C05 pointwise identity, C06 indicator sum; finite-sum distribution in ℤ. Precisely `4*(R N:ℤ)=((N:ℤ)-1)-2*L(N-1)+C N`, N≥2. | PROPOSED; principal counting target |
| C08; H:64 | `representation_count_pos_iff` 165 | `Finset.card_pos`, `mem_orderedRepresentations`; independent of C07 and all bounds on C/L. | PROPOSED; early counting target |
| C09; H:65 | `count_pos_iff_keystone` 168 | C07 plus integer arithmetic and natural/integer positivity cast. | PROPOSED |
| C09; H:66 | `keystone_ge_four_iff` 171 | C07; R is a natural count, so R>0 iff R≥1. | PROPOSED |
| A01/A02; H:81,93-96 | `target_iff_count_pos` 174 | Representation/Target definitional bridge, C08 at every admissible N (2<N implies 2≤N). | PROPOSED; reduction only |
| A01/A02/K01; H:67,93-96 | `target_iff_pointwise_keystone` 177 | Previous iff plus C09. | PROPOSED; reduction only |

### Counting branch graph

```text
approved lambda → lambda_sign ───────────────────────────→ C05
I → bounds → reflection/involution → C03 reflected sum
I → Icc endpoint equality ─────────→ C03 direct sum
I → cardinal cast ──────────────────────────────────────→ C07
I, pair filter → exact pair membership → C08 ──────────→ Target ↔ count-positive
                         └→ pair image/cardinality → C06
C03, C05, C06, cardinal cast → C07 → C09 ────────────────→ Target ↔ keystone
OPEN pointwise keystone ───────────────────────────────→ Target
```

The last arrow requires an actual new proof of the open node. Neither the graph nor any reduction supplies it.

## Optional core reduction and the open global nodes

| NL ID/source | Proposed declaration / S line | Dependencies and scope | Status |
|---|---|---|---|
| EX-C = explorer candidate C; X:74-90, especially 85 | `exists_prime_pair_factor_of_lambda_one` 181 | m>1 and lambda m=1; factor list cannot be empty or singleton, extract two prime occurrences, positive residual product d. `Nat.prod_primeFactorsList`, prime membership, `lambda_prime`, `lambda_mul`. Allows p=q and d=1. | PROPOSED; optional after main deliverables |
| EX-C; X:76-90 | `target_iff_prime_product_core` 187 | Forward instantiate Target at 2pq. Reverse Even decomposition N=2m; negative center gives diagonal, positive center gives factor extraction and positive-sign scaling of a core witness. | PROPOSED; optional reduction, not core theorem |
| K01; H:67,91-96 | `pointwise_keystone` 191 | For arbitrary even N>2, prove the strict pointwise C-versus-L inequality. No source proof supplied; routine lemmas only express its equivalence to the target. | **OPEN mathematical gap** |
| A01/A02; H:81; request:9-14 | `liouville_goldbach` 194, exact type `Target` | Either a proof of K01 plus the proved iff, or all core witnesses plus the proved core iff, or another unconditional complete argument. No global premise may remain on the final declaration. | **OPEN final goal** |

## Deferred source items; no silent claims of coverage

| NL ID/source | Disposition |
|---|---|
| O-T01; H:53 | The approved natural Target is unchanged. No new integer lambda/target or transport theorem is introduced. The handoff predates access to the approved declarations; do not let its optional conventions override D. |
| E01, remaining constants; H:72 | Only 2,3,4,5 scheduled. Other seed constants are not presumed evaluated/proved. |
| E05, other seeds; H:77; X:39-47 | d=10,12,14,18 and odd seeds 5,7 are optional later instances of signed scaling. No declarations/proofs for them are claimed here. |
| E06; H:78-79 | `lambda_square` proposed; representation square/power-of-two families deferred because they do not advance the prioritized count/core bottleneck. |
| ER01; H:80,98 | No residual-coverage theorem proposed or assumed. The referenced separate residual file was not among inspected inputs; nothing here depends on it. |
| K04; H:68 | Pigeonhole lower bound `-L(N-1) ≤ (R N:ℤ)` not scheduled. It is not needed for C07-C09 and gives no universal positivity by itself. |
| Explorer finite-seed limitation; X:51-69 | Used as an architectural warning, not a Lean theorem in this bundle. It concerns only fixed seed sizes/common scaling. It is not a counterexample to Target. |
| Explorer PB; X:92-106 | Sufficient prime-indexed positive-seed conjecture, unproved. No axiom or assumed theorem introduced. |
| Explorer failed-core constraints; X:108-135 | Not used to prove a contradiction; the listed three shifts are explicitly insufficient in the source. |
| Explorer LS / LS-square; X:156-205 | Unproved sufficient alternative constructions, not equivalent replacements claimed for Target. No formal interface scheduled. |
| Explorer bounded observations; X:208-275 | No computational result promoted to a universal theorem or accepted dependency. |

## Verification/provenance handoff

- Existing mathematical APIs come only from Mathlib revision `905b95818eb32af7874a58b427f50c1711a5e96c` (2026-07-28); Lean is v4.32.2. Exact file/line locators, dependency pins, and cutoff limits are in the blueprint.
- `api-probe-v1.lean` compiled successfully with the pinned project, exit 0; no helper proof is in it.
- `count-api-probe-v1.lean` failed at imports, exit 1, missing `Mathlib.Order.Interval.Finset.Nat.olean`. Generator needs same-revision interval/sum cache; no unconstrained update.
- Proposed definitions and all helper types in S need fresh code-only readback plus fidelity comparison. Their current proof status remains PROPOSED even if a reviewer finds the mathematics faithful.
- First implementation target: 8m family. Next: actual count/existence, reflection/pair count, exact integer identity. Then optional 2pq reduction. Mathematical discovery of the open universal node remains a separate task.
- No theorem was proved, no helper acceptance evidence exists, and no master integration was performed by this one-shot blueprinter.
