Mode: DISCOVERY — conjectural; no proof weight.

# Elementary alternative-route statements, version 1

All statements below are local, unreviewed candidates. They have unconditional mathematical hypotheses as displayed, but are NOT yet established partial results. No proofs are supplied by this sketcher. Constant evaluations, multiplicativity, sign cases, and witness checks are assigned obligations.

Definitions: lambda(n)=(-1)^(Omega(n)) in Z for positive integers n, with Omega counting prime factors with multiplicity and Omega(1)=0. For any integer N, G(N) denotes the existence of positive integers a,b with a+b=N and lambda(a)=lambda(b)=-1. The original target is G(N) for every even integer N>2; G itself imposes no extra parity condition.

## E01 — Positive-input arithmetic infrastructure

Statements, for positive integers u,v,t and a prime p:

    Omega(uv)=Omega(u)+Omega(v),
    lambda(uv)=lambda(u)*lambda(v),
    lambda(t^2)=1,
    lambda(p)=-1.

Also record exact signs needed for the seed table:

    positive sign: 1,4,6,9,10;
    negative sign: 2,3,5,7,13.

Dependencies: the approved multiplicity-counting definition and local prime-factorization arithmetic. Every required small primality/factorization fact is a proof obligation, not an unsupported library import. Only positive inputs occur.

Named obligations: O-E01 and O-E02.

## E02 — Diagonal family

Statement: For every even integer N>2 with lambda(N)=1, G(N) holds with

    a=b=N/2.

Equivalent positive-parameter statement: for every integer m>=1 with lambda(m)=-1, G(2m) holds with a=b=m. The condition lambda(m)=-1 excludes m=1 once lambda(1)=1 is established.

Dependencies: C01's sign facts, E01, the identity lambda(2)=-1, and the exact integral half of an even N. This is a partial family, not permission to add lambda(N)=1 to the final target.

Named obligation: O-E03.

## E03 — Sign-controlled scaling of a fixed representation

Statement: Let u,v,m be positive integers and let s be either +1 or -1. If

    lambda(u)=lambda(v)=s and lambda(m)=-s,

then G(m(u+v)) holds with a=mu and b=mv.

Specializations:

- A negative-negative representation is preserved under a multiplier m with lambda(m)=+1.
- A positive-positive representation becomes negative-negative under a multiplier m with lambda(m)=-1.
- Consequently, if G(S) holds and t>=1, then G(St^2) holds.

Dependencies: E01. Positivity, the exact sum, and both signs must be checked with the SAME multiplier m. This statement does not assert that an arbitrary multiplier preserves a negative-negative representation.

Named obligation: O-E04.

## E04 — Two-sign seed transfer

Statement: Let d>2 be an even integer. Suppose positive integers u_-,v_-,u_+,v_+ satisfy

    u_-+v_-=d,   lambda(u_-)=lambda(v_-)=-1,
    u_++v_+=d,   lambda(u_+)=lambda(v_+)=+1.

Then for every integer m>=1, G(dm) holds. The proposed witness selection is

    if lambda(m)=+1: (a,b)=(m*u_-,m*v_-);
    if lambda(m)=-1: (a,b)=(m*u_+,m*v_+).

Dependencies: C01 for an exhaustive two-case split and E03 for both branches. The conditions d even, d>2, m>=1 ensure dm is in the target's domain. This transfer lemma gives a universal-in-m family from a FIXED, independently checked seed d; it is not circular when only the finite seeds below are used.

Named obligation: O-E05a.

## E05 — Explicit sign-universal seeds and unconditional-family candidates

Proposed seed table:

| d | Negative-negative seed (u_-,v_-) | Positive-positive seed (u_+,v_+) |
|---|---|---|
| 8 | (3,5) | (4,4) |
| 10 | (5,5) | (1,9) |
| 12 | (5,7) | (6,6) |
| 14 | (7,7) | (4,10) |
| 18 | (5,13) | (9,9) |

Candidate conclusion: every positive multiple of any one of 8,10,12,14,18 satisfies the original representation condition G(N). No assumption on lambda(m) is required in the conclusion; E04 handles both signs.

Most useful first concrete target:

    For every m>=1, G(8m), with
      (3m,5m) when lambda(m)=+1,
      (4m,4m) when lambda(m)=-1.

Dependencies: E01's exact seed values, E04, and the finite sum/positivity checks in the table. The appearances of (4,4), (5,5), (6,6), (7,7), and (9,9) deliberately use the allowed equality a=b.

Named obligation: O-E05b. These are candidate partial theorems with explicit constructions, NOT accepted partial results until proved and reviewed.

## E06 — Square families and powers of two

Statements: For every integer t>=1,

    G(4t^2), with witness (2t^2,2t^2),
    G(8t^2), with witness (3t^2,5t^2).

Consequently, for every integer k>=2, G(2^k).

Dependencies: E01 and E03; the final consequence additionally requires an exhaustive parity split of the exponent, or the separate case 2^2=4 followed by the multiple-of-8 family for k>=3. No assertion for N=2 is made.

Named obligation: O-E06. These families overlap E02/E05; their value is transparent boundary testing and easy formal regression targets, not extra generality beyond every displayed family.

## Elementary frontier and residual coverage

The immediate proof frontier is E01 (positive multiplicativity and exact constants) together with C01 (sign dichotomy). E03 and the fixed seed table then unlock E04/E05 without analytic estimates or a source theorem. E02 provides an independent large partial family.

Even if all these statements are proved, the original target remains unresolved until the complementary cases are covered. For the explicitly listed diagonal condition and fixed seed divisibility conditions, the exact residual class is

    even N>2,
    lambda(N)=-1,
    8 does not divide N, 10 does not divide N,
    12 does not divide N, 14 does not divide N, 18 does not divide N.

Proposed sanity-check instance: N=242 lies outside those displayed coverage predicates (242=2*11^2). This is NOT asserted to be a counterexample to G(242); it only prevents mistaking this finite family list for universal coverage. Its elementary arithmetic check belongs to the finite-test obligation.

A generic square lift of an unspecified already-proved G(S) is a closure rule, not evidence that all residual N have been covered. Likewise, taking d=N in E04 requires the very negative-negative representation one is trying to obtain and cannot be used as an unconditional argument.
