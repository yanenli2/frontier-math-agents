Mode: DISCOVERY — conjectural; no proof weight.

# Exact formalization handoff, version 1

This is a mathematical interface specification, not Lean code, a compiled scaffold, or a request to alter an approved statement. No Lean file was created. The actual protected declaration, approved definitions, eligible environment, and existing declaration names were not supplied to this worker. The formalizer/blueprinter must align these proposed interfaces with that snapshot and send any semantic change back for fresh readback/fidelity review.

## Protected target and normalization

Authoritative mathematical type:

    forall N : Z,
      Even N -> 2 < N ->
      exists a b : Z,
        0 < a and 0 < b and N = a+b
        and lambda(a)=-1 and lambda(b)=-1.

Lambda is only mathematically prescribed on positive inputs. If the approved formalization uses natural inputs, the following target is equivalent after a separate domain/coercion lemma:

    forall N : Nat,
      Even N -> 2 < N ->
      exists a b : Nat,
        0 < a and 0 < b and N = a+b
        and lambda(a)=-1 and lambda(b)=-1.

Required type-level facts: Omega counts prime factors WITH MULTIPLICITY and has Omega(1)=0; lambda has signed codomain Z and agrees with (-1)^Omega on positive inputs; neither definition nor hypotheses assume the conclusion. The lambda(0) totalization is irrelevant but must be visible to the statement review if transitive definitions contain it.

## Proposed natural-index implementation conventions

These conventions are optional and must not silently replace accepted definitions.

- `Omega : Nat -> Nat` as in the approved snapshot.
- `lambda : Nat -> Z` as in the approved snapshot.
- `I N = {a in range N : 0<a}` as a finite set of Nat.
- `J m = {a in range (m+1) : 0<a}` as a finite set of Nat.
- `L m : Z = sum_(a in J m) lambda a`.
- `R N : Nat = cardinality {a in I N : lambda a=-1 and lambda (N-a)=-1}`.
- `C N : Z = sum_(a in I N) lambda a * lambda (N-a)`.

For N>=2, prove I N is exactly the interval 1<=a<=N-1, `card(I N)=N-1`, and membership implies 0<N-a<N. Natural subtraction in the argument N-a is exact only under this bound. Do not use a lemma about lambda at 0 to fill a missing positivity proof.

The identity must use signed arithmetic on its right side:

    4*(R N : Z) = ((N:Z)-1) - 2*L(N-1) + C N.

Here the `N-1` used as the input of L is a natural index, guarded by N>=2. The scalar term is `(N:Z)-1`, not an unguarded natural subtraction cast or a natural-valued expression. No division by 4 is needed. An integer-index implementation may instead use the contract's finite integer intervals directly and prove equivalence to any existing natural lambda interface.

## Declaration-by-declaration handoff

The proposed names below are identifiers for the blueprinter's map, not existing declarations and not a claim of successful elaboration.

| NL ID | Proposed declaration identifier | Exact mathematical content / guards |
|---|---|---|
| O-T01 | `integer_nat_target_equiv` | equivalence of the full integer and natural target types, preserving positivity, evenness and lambda on positive coercions |
| C01 | `liouville_sign` | n>0 -> lambda(n)=1 or lambda(n)=-1 |
| C01 | `liouville_one` | lambda(1)=1 |
| C02 | `mem_interval_bounds` | N>=2 and a in I N -> 0<a, a<N, 0<N-a, N-a<N |
| C02 | `interval_card_cast` | N>=2 -> (card(I N):Z)=(N:Z)-1 |
| C02 | `reflection_bijection` | N>=2 -> a |-> N-a is a bijection of I N, with square equal to identity |
| C03 | `sum_liouville_reflection` | N>=2 -> sum_(a in I N) lambda(N-a)=L(N-1) |
| C04 | `ordered_pair_count_equiv` | a |-> (a,N-a) is an equivalence between the filtered interval and ordered positive pairs with the required sum/signs |
| C05 | `two_sign_indicator` | positive a,b -> 4*[lambda(a)=lambda(b)=-1]_Z=(1-lambda(a))*(1-lambda(b)) |
| C06 | `count_eq_indicator_sum` | N>=2 -> (R N:Z)=sum over I N of the integer two-negative-sign indicator |
| C07 | `four_mul_representation_count` | exact signed identity above, for every N>=2 |
| C08 | `representation_count_pos_iff` | N>=2 -> (0<R N iff exists positive a,b with N=a+b and both signs -1) |
| C09 | `count_pos_iff_keystone` | N>=2 -> (0<R N iff 2*L(N-1)-((N:Z)-1)<C N) |
| C09 | `keystone_ge_four_iff` | N>=2 -> (0<R N iff 4<=((N:Z)-1)-2*L(N-1)+C N) |
| K01 | `pointwise_keystone` | forall N, Even N -> 2<N -> 2*L(N-1)-((N:Z)-1)<C N; OPEN, no proof supplied |
| K04 | `count_ge_neg_partial_sum` | N>=2 -> -L(N-1)<=(R N:Z) |
| E01 | `omega_mul_positive` | u,v>0 -> Omega(uv)=Omega(u)+Omega(v) |
| E01 | `liouville_mul_positive` | u,v>0 -> lambda(uv)=lambda(u)*lambda(v) |
| E01 | `liouville_square_positive` | t>0 -> lambda(t^2)=1 |
| E01 | `liouville_small_values` | exact positive/negative constant evaluations listed in E01, with no implicit primality assumptions |
| E02 | `representation_diagonal` | Even N, N>2, lambda(N)=1 -> G(N), with a=b=N/2 |
| E03 | `representation_scaled_sign` | u,v,m>0, s in {+1,-1}, lambda(u)=lambda(v)=s, lambda(m)=-s -> G(m(u+v)) |
| E04 | `representation_two_sign_seed` | positive ++ and -- seed pairs summing to fixed even d>2 -> forall m>0, G(dm) |
| E05 | `representation_multiple_eight` | forall m>0, G(8m); explicit case witnesses (3m,5m)/(4m,4m) |
| E05 | `representation_other_seed_multiples` | separate d=10,12,14,18 instances of E04 with the exact table |
| E06 | `representation_square_families` | forall t>0, G(4t^2) and G(8t^2), with displayed witnesses |
| E06 | `representation_power_two` | forall k>=2, G(2^k) |
| ER01 | `representation_residual` | exact residual-domain statement in lemmas/residual-v1.md; OPEN |
| A01/A02 | approved final theorem name | must have EXACT protected target type and no residual keystone/coverage premise |

Here G(N) is only an abbreviation for the original positive-witness conclusion. It does not bake in a proof, primality, coprimality, parity of witnesses, or a restriction a!=b.

## Recommended proof order and exact missing goals

1. First statement fidelity and environment eligibility; these are not inferred from this handoff.
2. Prove C01 and E01; independently prove C02/C04. Compile meaningful increments.
3. Prove the explicit multiple-of-8 family early and label it a partial theorem.
4. Prove C03/C05/C06, then C07-C09. The identity's RHS is signed; a well-typed natural-number substitute would be the wrong theorem.
5. Keep K01 as an explicit unresolved task, NOT as a custom axiom and NOT as an unnoticed hypothesis on the purported final theorem.

Once the count bridge/identity are available, the exact unresolved counting goal for an arbitrary admissible natural N is:

    Given hEven : Even N and hN : 2<N,
    prove 2*L(N-1)-((N:Z)-1) < C N.

For the family-first route, the exact unresolved goal is G(N) given hEven, hN, lambda(N)=-1, and nondivisibility by every d in {8,10,12,14,18}. Neither goal has a proof in this sketch.

## Review and provenance gates

- Every imported mathematical library theorem must come from the eligible pinned version, including apparently elementary factorization, finite-set, interval, and coercion infrastructure. Do not silently update Mathlib to obtain a convenience lemma.
- An eligible external paper theorem is not already a Lean proof. If used load-bearingly, its proof/dependencies must be supplied in the accepted formal development or its missing formalization must remain an obligation. Do not add it as an unsupported axiom.
- Mangerel v2 Theorem 1.2 does not state `pointwise_keystone`; its C-versus-L notation map and insufficiency are in `source-scope-v1.md`.
- Require actual compilation, exact statement comparison, no sorry/admit or sorryAx, and #print axioms on accepted declarations/dependency closure. Record hashes and actual commands/results.
- Do not send proof plans or source-intent comments to the blind statement readback worker. The leader handles its restricted packet and fresh-review workflow.
- Only the designated integrator merges accepted artifacts into the master development. This file neither authorizes a merge nor certifies a theorem.
