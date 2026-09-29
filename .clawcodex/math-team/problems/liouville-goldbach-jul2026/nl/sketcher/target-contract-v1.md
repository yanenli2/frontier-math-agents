Mode: DISCOVERY — conjectural; no proof weight.

# Exact target contract, version 1

Task: 058f7f3988b0. Author role: nl-sketcher. This is a statement/decomposition artifact, not a proof or an acceptance report. Every proposed lemma remains unproved and unreviewed in this artifact.

## Authoritative inputs and scope

- Problem input: `../../request.md`, read in full.
- Protocols: project `.clawcodex/skills/math-team/references/protocol.md` and `natural-language.md`, read in full.
- Output ownership: this `nl/sketcher/` directory only.
- No external mathematical source, cached theorem, mathematical library result, or remembered theorem is being used as proof. No external browsing was performed. The elementary constructions below are new local candidates awaiting justification and independent review.
- External source versions, including library code, must be demonstrably publicly available on or before **2026-07-31, inclusive**. An eligible first publication does not authorize a later revision. Source registration and toolchain pinning belong to the leader/designated owners, not this artifact.

## T0: Exact assertion

For every integer N,

    [N is even and N > 2]
      implies
    there exist integers a,b such that
      a > 0, b > 0, N = a+b, lambda(a) = -1, lambda(b) = -1.

Here Omega(n), for a positive integer n, counts prime factors with multiplicity, Omega(1)=0, and

    lambda(n) = (-1)^(Omega(n)) in Z.

Even means divisibility by 2, equivalently N=2k for an integer k. The witnesses can depend on N. There are no primality, distinctness, oddness, coprimality, relative-size, or other restrictions on a,b. In particular a=b is allowed. The conclusion is existence, not uniqueness and not an assertion about all representations.

The target is unconditional and pointwise for every admissible N. It is not a conditional theorem, a positive-density result, an almost-all result, an average over N, a finite computation, or an unspecified sufficiently-large-N statement.

## Domain and definition contract

1. Only positive inputs to Omega and lambda are required mathematically. Do not assign mathematical significance to lambda(0) or lambda at negative integers.
2. An implementation may use natural inputs to a total lambda function, but its value at 0 must be isolated and never used as a positive-input premise. Totalization is a formal implementation convention, not an extra hypothesis or a change to T0.
3. A natural-number encoding must be accompanied by the equivalence with T0: every integer N>2 and its positive integer witnesses identify with natural numbers, and the reverse coercions preserve addition, positivity, evenness, and lambda values.
4. The output of lambda is signed: +1 and -1 are distinct integer values. Natural subtraction must not turn -1 into 0.
5. Multiplicity is mandatory. Audit examples, themselves requiring local verification before acceptance: Omega(1)=0, Omega(4)=2, Omega(8)=3, Omega(12)=3; therefore lambda(1)=+1, lambda(4)=+1, lambda(8)=-1, lambda(12)=-1. Counting distinct prime divisors is not the intended definition.
6. No material ambiguity remains in the assigned mathematical reading. Choices of integer versus natural indexing, the totalization at 0, and implementation names remain formalization decisions to record explicitly; none authorizes changing T0.

## Finite-index conventions for the counting route

The following definitions use integer indices. Their proposed natural-number implementations must be proved equivalent.

For an integer m >= 0, let

    J_m = {n in Z : 1 <= n <= m},
    L(m) = sum over n in J_m of lambda(n), with values in Z.

J_0 is empty and L(0)=0. Only integer arguments m=N-1 >= 1 are needed; no extension of L to real arguments is required.

For an integer N >= 2, let

    I_N = J_(N-1) = {a in Z : 1 <= a <= N-1},
    B_N = {a in I_N : lambda(a)=-1 and lambda(N-a)=-1},
    R(N) = cardinality(B_N), with values in Nat,
    C(N) = sum over a in I_N of lambda(a)*lambda(N-a), with values in Z.

The interval assumptions must establish 1 <= N-a <= N-1 before lambda(N-a) is used. The bounds are inclusive: a=1 and a=N-1 occur; a=0 and a=N do not.

The requested meaning of R is the number of ordered positive pairs. The mandatory parametrization obligation is that

    a |-> (a,N-a)

is a bijection from B_N onto

    {(a,b) in Z x Z : a>0, b>0, a+b=N,
                         lambda(a)=-1, lambda(b)=-1}.

Thus an off-diagonal pair and its reversal are distinct counted pairs, while a diagonal pair is counted once. No division by 2 is permitted to change this convention.

If P is a proposition, [P]_Z is 1 in Z when P holds and 0 in Z otherwise. All displayed sums of indicators are integer sums. Every use of R in an integer equality has an explicit natural-to-integer cast.

## Proposed identity and exact terminal obligation

For every integer N >= 2, the proposed identity is

    4 * (R(N) : Z) = (N-1) - 2*L(N-1) + C(N).

Evenness is not required for this identity. It is required for the original target's quantified domain, and must not be silently dropped from that target.

Write

    K(N) = (N-1) - 2*L(N-1) + C(N) in Z.

The counting route's **exact keystone** is

    for every integer N, if N is even and N>2, then
      C(N) > 2*L(N-1) - (N-1),

or equivalently K(N)>0. Once the identity is accepted, this is equivalent to R(N)>0, and also equivalent to K(N)>=4. The constant 4 in the last formulation comes from K(N)=4R(N), not merely from K(N) being an integer.

This is an exact reformulation of the original existence problem, not an already supplied estimate and not evidence that the problem has been solved. The identity only gives K(N)>=0 unconditionally through nonnegativity of the count; strict positivity is the missing mathematical content.

## Success and incompleteness boundary

For this task, success means production of this contract, the dependency plan, lemma statements, obligation ledger, branch queue, and formalization handoff. That status is separate from mathematical acceptance.

For the original problem, success requires a faithful approved Lean statement, a complete proof in an eligible pinned environment, compilation of the actual integrated final theorem, no prohibited axioms or admitted obligations, and the specified independent reviews. None of those facts is asserted here.

There is no claim in this sketch that the target is false, proved, or known to be open. Such a status claim would require appropriate evidence. Failure to supply the keystone or an intermediate construction is an open obligation of this work, not a defect of the problem.
