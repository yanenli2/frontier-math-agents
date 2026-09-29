Mode: DISCOVERY — conjectural; no proof weight.

# Exact keystone and optional estimate obligations, version 1

These are statements/requests, not proved estimates. In particular, no cancellation theorem is being asserted from memory.

Definitions: For positive n, lambda(n)=(-1)^(Omega(n)) in Z. For integer m>=0, L(m)=sum_(1<=n<=m) lambda(n). For integer N>=2, C(N)=sum_(1<=a<=N-1)lambda(a)lambda(N-a), and R(N) is the ordered positive-pair count with both lambda values -1, equivalently the filtered first-coordinate cardinality after C04 is established. Let M=N-1 and K(N)=M-2L(M)+C(N). All sums and K are integer-valued; R is natural-valued.

## K01 — Exact pointwise keystone (OPEN)

Statement:

    For every integer N, if N is even and N>2, then
      C(N)>2L(N-1)-(N-1).

Equivalent formulations after C07-C09 are accepted:

    K(N)>0;  K(N)>=4;  R(N)>0.

Scope: every admissible N, including small N. No density-one, averaging, unspecified exceptional-set, or ineffective finite-tail replacement is allowed.

Dependency status: K01 has no supplied proof. C07 is an algebraic reformulation, not a source of strict positivity. Deriving K01 from the target itself would be circular as a proof strategy. This is the keystone blocker of the counting branch.

## K02 — A sufficient signed-error margin (conditional arithmetic statement)

Statement: Fix an integer N>=2 and real numbers alpha,beta>=0 with 2alpha+beta<1. If

    L(N-1) <= alpha*(N-1),
    C(N) >= -beta*(N-1),

where integer quantities are coerced to R in these estimates, then

    (N-1)-2L(N-1)+C(N)>0.

An absolute bound |L(N-1)|<=alpha*(N-1) can supply the first hypothesis; an absolute bound |C(N)|<=beta*(N-1) can supply the second. Neither absolute bound is necessary. All constants and the strict margin must be recorded.

This is a proposed elementary implication only. It does not assert either estimate. A weaker bound C(N)>=-(N-1), or the facts lambda=+/-1 alone, do not provide the positive margin when L(N-1)>=0.

Dependencies: M=N-1>0 and elementary ordered-field arithmetic. Application to the target additionally uses C07-C09 and a uniform proof of the displayed hypotheses for the required N.

## K03 — Explicit tail plus exhaustive finite completion

Statement: Let N0 be a specified integer with N0>=4. Suppose both of the following have been proved:

1. For every even integer N>=N0, K(N)>0.
2. For every even integer N with 2<N<N0, R(N)>0.

Then K01, and hence T0 through the counting lemmas, follows.

Dependencies: C09 for the finite branch, the exhaustive split N<N0 or N>=N0, and both listed hypotheses. The convention is strict at the finite upper endpoint and inclusive at the tail endpoint, so there is no boundary gap.

Obligations: the actual threshold must be known if this route is to finish by finite checking; all remaining even N must receive rigorous coverage. A proved but ineffective eventual statement can remain a useful partial result, but it does not supply the missing finite certificates.

## K04 — Optional negative-partial-sum criterion

Statement: For every integer N>=2,

    (R(N):Z) >= -L(N-1).

Consequently L(N-1)<0 implies R(N)>0.

Suggested infrastructure, not a proof: the negative-sign subset of I_N and its reflection have the same cardinality; the size of their intersection is R(N). C01 gives 2*(#negative-sign subset : Z)=(N-1)-L(N-1). The finite-set intersection/cardinality step is an explicit obligation.

Dependencies: C01, C02, and finite-set inclusion-exclusion/cardinality bounds. This criterion is sufficient and not asserted necessary. The universal stronger premise

    L(N-1)<0 for every even N>2

is NOT assumed, claimed, or sourced here. Before investing in it, assign a bounded exact attempt to falsify that premise. A counterexample to this stronger premise would not be a counterexample to T0 or K01.

## Required quantifier and correlation distinctions

- **Pointwise universal target:** for every admissible N, a representation exists. This is K01's scope.
- **Fixed finite computation:** coverage up to a recorded bound B says nothing about N>B without a separate tail theorem.
- **Uniform eventual estimate:** a bound valid for every even N>=N0 can be combined with a rigorous finite completion. The endpoint N0 must be explicit for the proposed computational completion.
- **Asymptotic along all even N:** for example C(N)/(N-1) -> 0 as N -> infinity through all even N has a universal-tail meaning and would support an eventual bound. It does not by itself identify an effective threshold or settle the remaining cases. No such asymptotic is claimed here.
- **Almost-all statement:** an exceptional set with relative density tending to zero may still contain infinitely many failing N. It does not imply the target.
- **Averaged statement:** control of a sum or mean of C(N), R(N), or an error over N does not by itself give K01 at each N. A separate pointwise bridge is required.
- **Weights:** an estimate for logarithmically weighted or other weighted sums does not silently become an estimate for the unweighted sums defining L and C.
- **Shifted versus reflected correlation:** a result about sum_n lambda(n)lambda(n+h) for a fixed shift h is not automatically a result about sum_(a=1)^(N-1)lambda(a)lambda(N-a). Here the second argument decreases as the first increases, and a putative shift N-2a varies with a. A precise transformation with verified hypotheses would be a new obligation.
- **Distribution on residue classes:** any invocation must match its quantifiers, range, effective constants, and modulus dependence. An estimate holding for each fixed modulus cannot be silently applied uniformly to growing moduli.

## Precise information request for the leader

A literature/local-wiki owner may look for an eligible, exact statement that supplies a pointwise lower bound for this reflected C(N), or supplies existence/count positivity directly, with all N-quantifiers and exceptional sets visible. Record the publicly available version date (<=2026-07-31), theorem/page locator, complete preconditions, effectiveness/threshold information, and how it reaches K01. A theorem giving only a weaker scope should be registered as a partial result or a branch input, not as closure of K01.

No literature claim or claim of known open status is made by this request. No local wiki has been supplied to this worker; its absence is not a prerequisite blocker for the elementary frontier.
