Mode: DISCOVERY — conjectural; no proof weight.

# Source-scope supplement received during sketching, version 1

This file records a source supplied by the leader after the initial contract was written. It does not close any proof obligation and does not edit or replace the leader-owned `sources.md`.

## Supplied primary source and provenance boundary

- Author: Alexander P. Mangerel.
- Title: *On a Goldbach-type problem for the Liouville function*.
- Version: arXiv:2404.12117v2.
- Version URL: https://arxiv.org/abs/2404.12117v2
- PDF URL: https://arxiv.org/pdf/2404.12117v2
- Version date: 2024-05-02. The leader reported verified metadata; the read PDF's first-page arXiv stamp also identifies v2 and 2 May 2024.
- Local supplied file: `../../knowledge/mangerel-v2/paper.pdf` relative to this directory.
- This worker directly read PDF pages 1-4 using the Read tool, with `pages: "1-4"`.
- This is an eligible dated version relative to the 2026-07-31 cutoff. No later version or current changing webpage was consulted by this worker.
- Retrieval hashes and registration in shared provenance records remain leader/source-owner responsibilities. Reading statements here is not a verification of the entire paper's proof or a Lean import of its theorems.

## Exactly relevant statements read

**Theorem 1.2, printed page 1:** There exists N0 in Nat such that if N>=N0, then

    |L_lambda(N)| < N-1,

where the paper's L_lambda(N) is

    sum_(1<=n<=N-1) lambda(n)lambda(N-n).

Thus the paper's L_lambda is this sketch's **C**, not this sketch's partial sum **L**. Preserve this notation conversion explicitly.

**Remark 1, printed page 2:** The proof of Theorem 1.2 relies on Siegel's theorem concerning lower bounds for L(1,chi); consequently the lower bound N0 is ineffective. This is the paper's effectiveness statement. No independent invocation of Siegel's theorem is proposed here.

**Remark 2, printed page 3:** The paper asks whether, for an even integer N>=4, there must exist 1<=a,b<=N with a+b=N and lambda(a)=lambda(b)=-1, and states that its methods appear too rigid to address this problem directly. Positivity plus a+b=N makes the redundant upper bounds on a,b harmless; this is the same representation target as the user's even N>2 formulation.

The same remark discusses a stronger convolution saving as a possible sufficient approach and displays the no-representation expansion corresponding to K(N)=0. That discussion is NOT an established theorem supplying the stronger saving. The external prime-number-theorem estimate mentioned there is not being imported as a proved dependency by this sketch.

## Exact applicability gap

Theorem 1.2 gives eventual

    C(N)>-(N-1)

(and also C(N)<N-1). Our keystone requires, for every admissible N,

    C(N)>2L(N-1)-(N-1).

When L(N-1)>0, the required lower bound is strictly stronger by 2L(N-1). The theorem does not provide that margin. Independently, its unspecified ineffective threshold leaves a finite-completion problem. Neither gap is removed merely by displaying the counting identity.

Convolution nonconstancy means that not all products lambda(a)lambda(N-a) have the same sign. A positive product can come from a positive-positive pair, not only a negative-negative pair. For even N the middle product lambda(N/2)^2 is already positive. Hence nonconstancy must NOT be reported as the desired negative-negative representation.

Optional finite sanity-test request: use an arbitrary sign sequence (not the Liouville function) on {1,...,5} with values (+1,-1,+1,+1,+1), and check the predicted values L=3, C(6)=1, R(6)=0. This would test the invalid implication from sign/count identities plus |C|<N-1 to R>0. It would NOT be a counterexample to the original problem, because this arbitrary sequence is not asserted multiplicative or equal to lambda.

## Consequence for the branch queue

The supplied source is useful for scope discipline and for requesting a genuinely stronger eligible theorem. It does not settle K01. Do not spend formalization effort on importing Theorem 1.2 as though it directly yields T0. The elementary partial-family branch remains independently available.

The remark supports only the recorded 2024 source-specific statement about what this paper asks and proves. This sketch makes no unverified assertion about the complete literature's status by the July 2026 cutoff or at any later time.
