Mode: DISCOVERY — conjectural; no proof weight.

# Counting-route lemma statements, version 1

These are proposed statements and proof obligations, not proofs. All mathematical acceptance statuses are OPEN. Definitions are those below; no external theorem is assumed.

For positive integers n, lambda(n)=(-1)^(Omega(n)) in Z, with prime factors counted with multiplicity and Omega(1)=0. For integer m>=0, J_m={n in Z:1<=n<=m} and L(m)=sum_(n in J_m) lambda(n). For integer N>=2, I_N=J_(N-1), B_N={a in I_N:lambda(a)=lambda(N-a)=-1}, R(N)=#B_N in Nat, and C(N)=sum_(a in I_N)lambda(a)lambda(N-a) in Z. [P]_Z denotes the integer indicator of proposition P.

## C01 — Required sign dichotomy

Statement: For every positive integer n,

    lambda(n)=1 or lambda(n)=-1.

Also lambda(1)=1. In particular the two sign cases are exhaustive and mutually exclusive in Z.

Prerequisites: the exponent Omega(n) is a natural number; Omega(1)=0; signed integer exponentiation. No complete-multiplicativity lemma is needed for this node.

Named obligation: O-C01.

## C02 — Interval bounds, cardinality, and reflection bijection

Statement: For every integer N>=2:

- I_N is finite and (#I_N : Z)=N-1.
- For every a in I_N, both a and N-a are positive and belong to I_N.
- rho_N:I_N -> I_N, rho_N(a)=N-a, is a bijection and an involution: rho_N(rho_N(a))=a.

Prerequisites: integer interval arithmetic only. The actual lower bound N>=2 makes I_N nonempty and avoids truncated-subtraction semantics. The identity N-(N-a)=a is an integer identity here.

Named obligations: O-C02 and O-C03a.

## C03 — Reflection reindexing of the finite sum

Statement: For every integer N>=2,

    sum_(a in I_N) lambda(N-a)
      = sum_(a in I_N) lambda(a)
      = L(N-1).

Dependencies: C02. All lambda inputs are positive by C02. This is a sum reindexing, not a claim that lambda(N-a)=lambda(a) termwise.

Named obligation: O-C03b.

## C04 — Ordered-pair parametrization

Statement: For every integer N>=2, the map a |-> (a,N-a) is a bijection from B_N to the set of ordered integer pairs (a,b) satisfying

    a>0, b>0, a+b=N, lambda(a)=-1, lambda(b)=-1.

The inverse takes the first coordinate. The pair set is finite. Its cardinality is R(N). This counts each orientation separately when a!=b, and counts a=b only once.

Dependencies: C02 for positivity/bounds; the defining equality a+b=N for the inverse. No restriction on the parity of either witness is imposed.

Named obligation: O-C04.

## C05 — Signed two-variable indicator identity

Statement: For all positive integers a,b,

    4 * [lambda(a)=-1 and lambda(b)=-1]_Z
      = (1-lambda(a))*(1-lambda(b))
      = 1-lambda(a)-lambda(b)+lambda(a)*lambda(b).

Dependencies: C01. Both variables are positive, so the sign dichotomy is applicable. An eventual proof must explicitly discharge the sign cases or an equivalent exact algebraic argument. There is no natural division or subtraction in the statement.

Named obligation: O-C05.

## C06 — Cardinality as an integer indicator sum

Statement: For every integer N>=2,

    (R(N):Z)
      = sum_(a in I_N) [lambda(a)=-1 and lambda(N-a)=-1]_Z.

Dependencies: the definition of R and finite-set indicator/cardinality arithmetic; C02 ensures all function applications have positive input. C04 is needed to interpret this same R as the ordered-pair count requested by the user, but not to derive this finite-set identity itself.

Named obligation: O-C06.

## C07 — Exact counting identity

Statement: For every integer N>=2,

    4*(R(N):Z) = (N-1) - 2*L(N-1) + C(N).

Dependencies: C02 (cardinality and positive inputs), C03 (one reflected sum), C05 (pointwise expansion), and C06 (indicator sum). The sum is over the whole ordered first-coordinate interval I_N, not just a<=N/2.

Named obligation: O-C07. In particular, every cardinality cast and every occurrence of -1 or subtraction is in Z.

## C08 — Positive count if and only if an actual representation exists

Statement: For every integer N>=2,

    R(N)>0
      if and only if
    there exist integers a,b with
      a>0, b>0, N=a+b, lambda(a)=lambda(b)=-1.

Dependencies: C04 and the finite-set cardinality/nonemptiness equivalence. Positivity of R is a natural-number proposition; the witnesses in the right side are genuinely positive integers.

Named obligation: O-C08. Both directions are required for the exact reformulation, although only the forward direction is needed in final assembly.

## C09 — Integer positivity and the exact keystone threshold

Statement: For every integer N>=2, put K(N)=(N-1)-2*L(N-1)+C(N). Then

    R(N)>0
      iff K(N)>0
      iff C(N)>2*L(N-1)-(N-1)
      iff K(N)>=4.

Also K(N)>=0 and K(N) is divisible by 4.

Dependencies: C07 and order-preserving natural-to-integer coercions. The step K(N)>0 iff K(N)>=4 uses the identity K(N)=4R(N); it does not hold for an arbitrary integer K.

Named obligation: O-C09.

## A01 — Conditional final assembly

Statement: If the following universal inequality has an unconditional proof,

    for every integer N, Even(N) and N>2 imply
      C(N)>2*L(N-1)-(N-1),

then the exact original target T0 follows.

Dependencies: C08 and C09, together with a separately accepted proof of K01 in `keystone-v1.md`. For an admissible N, N>2 supplies the N>=2 precondition of C08 and C09. The witnesses then come from C08 with no additional restrictions.

Named obligation: O-A01. This implication is not an unconditional proof of T0 while K01 is unresolved. Do not discharge K01 by assuming T0 or by importing a theorem whose premise already contains the desired representation.
