# Independent mathematical review: descent v1

Mode: CERTIFICATION

**Verdict: PASS for the full requested natural-language target.**

The reviewed mathematical content proves

```lean
theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :
  ArithmeticStatement.HasRepresentation (4 * m)
```

This is an LLM mathematical review, not Lean compilation or kernel verification. It does not certify the original all-even conjecture.

## 1. Artifact identity and inputs

Path abbreviations:

- `P = .clawcodex/math-team/problems/liouville-goldbach-jul2026`
- `W = P/waves/multiples-four`
- `M = P/lean/.lake/packages/mathlib`
- Report: `W/nl/reviews/descent-review-v1.md`.

SHA-256 hashes are of entire files, including the candidate's excluded portions; hashing those portions did not supply mathematical evidence.

| Artifact | SHA-256 |
|---|---|
| `W/nl/descent/proof-attempt-v1.md` | `23fc6ad19d1c45dd432945aa84756b190700b8c15394b1554ebb3ecaff82235e` |
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `M/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `M/Mathlib/Algebra/Ring/Parity.lean` | `c710e4b51d5ffc9df4e2cc16bad357ab152b1ae5ff05e8fb68a1e3812e6a3b68` |
| `M/Mathlib/Algebra/Group/Even.lean` | `1180fa9ac282e55257e95c8402acd7314fcbd0a18bcfdede92a3cde16e1db630` |
| `.clawcodex/skills/math-team/references/protocol.md` | `e712830b3febe6e3fcaf0479c7aa9fc30f23aa4fcc5e1f45088f736f9c161f2b` |

Inputs read: protocol; request; candidate **only lines 31–42 and 44–332**; the two permitted Statement files. Mathlib inspection consisted of targeted factorization searches and reads at `Factors.lean:34–90,195–203`, and the parity theorem search around `Parity.lean:389`. A lookup for that parity theorem in `Group/Even.lean` returned no match and supplied no proof evidence. Directory and Git metadata were inspected only for location and source identity.

Mathlib HEAD was verified as `905b95818eb32af7874a58b427f50c1711a5e96c`, with commit timestamp `2026-07-28T18:36:13+02:00`, within the inclusive 2026-07-31 cutoff. The three inspected Mathlib paths had no tracked local changes. The candidate, request, and Statement hashes were checked again and were unchanged.

No prior review, author confidence, excluded status/handoff/history, external source, task board, or other team's proof was read. No agents were spawned. Only this report was written.

## 2. Target, definitions, and dependency audit

The target quantifies over **every positive natural m**, not merely primes. `HasRepresentation N` is exactly the existence of positive natural witnesses a,b with `N = a+b` and both Liouville values -1 (`Partial.lean:14–20`). `omega` counts prime factors with multiplicity, and `lambda` is its signed power in the integers (`Definitions.lean:6–8`). Equal witnesses are allowed.

The baseline used at candidate lines 33–38 is valid:

- `lambda_one`: value 1 at 1.
- `lambda_sign`: the two possible signs on positive arguments.
- `lambda_mul`: complete multiplicativity for positive factors, **without coprimality**.
- `lambda_prime`: value -1 at any prime.

In the pinned source, `Nat.perm_primeFactorsList_mul` requires only that both factors be nonzero. Its permutation identity gives the required additive factor-list lengths. `primeFactorsList_prime` gives the singleton factor list. The inspected `neg_one_pow_eq_ite` supplies the sign dichotomy; its algebraic hypotheses hold for the integers. The candidate also explains these facts through positive prime factorization. No later theorem in `Partial.lean` is needed to establish the new uniform argument.

The abstract f is used only on positive integers. Negative indices in the rigidity argument denote residue classes for F, never forbidden arguments of f. Natural subtraction, division, scaling, and all multiplicativity applications have their requisite positivity or integrality checked below. Nothing concerning lambda(0) is used.

The prime-core wording at line 299 is narrower than the actual request. Acceptance therefore includes the assembly at lines 309–330; it is not acceptance of the prime core alone.

## 3. Missing-pair implications and local identities

**Lines 46–71: accepted.** Complete multiplicativity into the two nonzero signs implies f(1)=1 and f(t²)=f(4)=1. Under the missing-pair assumption, p and 3p force f(3p)=1 and hence f(3)=-1. For (A), scaling u and p-u by 4 would otherwise produce forbidden negative witnesses. For (C), scaling v and 2p-v by 2 would otherwise do so. Their stated intervals ensure positive witnesses. Applying (C) to p-u after (A) correctly gives (B).

**Lines 75–87: accepted.** Both sign cases in (T) use only (A), (B), and the missing-pair complement rule. The complement of 3(p-x) is p+3x. All these numbers are positive and below 4p when 0<3x<p. The second sign case for local reflection produces precisely that forbidden pair. These local identities do not presuppose full reflection and are not needed as an unjustified extension to its full domain.

## 4. Ternary positive-pair gap descent

**Lines 93–146: accepted, including the uniform descent.**

1. A defect has positive x,y<p with x+y=p and both signs +1. Negative-negative pairs at this total are already excluded by (A).
2. If x=3u, positivity gives 0<u<p. Then f(u)=-1, (A) gives f(p-u)=1, and f(3p-x)=-1. Applying (C) to y gives f(p+x)=-1. Their sum is 4p and both are positive, a contradiction. Exchanging x,y handles the other entry.
3. Neither entry is divisible by 3. Since p is prime and p≠3, their nonzero residues modulo 3 must agree. Therefore p+x=2x+y and p+y=x+2y are both divisible by 3.
4. The submitted x'=(p+x)/3 and y'=(p+y)/3 are positive integers of sum p. The two applications of (C), together with f(3)=-1, give both new signs +1. Thus the map really preserves defects.
5. Oddness of p excludes x=y. Among ordered defects with x<y, a minimum positive integral gap exists. The map preserves that ordering and divides its gap by 3. Its integrality follows from the exact divisions already proved, so it is a strictly smaller positive integer gap of another admissible defect.

This rules out both equal-sign possibilities at total p and proves full reflection on **every** 0<n<p. There is no omitted residue class or nonintegral descent step.

## 5. Finite character rigidity

**Lines 152–172: accepted.** Defining F through the unique representative in 1,…,p-1 is legitimate independently of any periodicity of f. Reflection gives F(-z)=-F(z). Prime cancellation ensures closure of nonzero residues and injectivity of multiplication by a nonzero residue; finiteness gives inverses. Good multipliers include 1 and -1 and are closed under multiplication by the calculation given.

**Lines 176–211: accepted, including wrapgap and strict product bound.** If n is the least bad representative, then 2≤n<p and every nonzero integer k with |k|<n has a good residue: positive representatives follow from minimality, negative ones from multiplication by -1.

For any nonzero z, the n multiples 0,z,…,(n-1)z are distinct by prime cancellation. The n positive integral cyclic gaps sum to p. Thus one gap d≤p/n exists. Since 2≤n<p and p is prime, n does not divide p; consequently d<p/n and **nd<p**.

Subtracting the endpoint indices in the direction of this gap gives 0<|k|<n and kz≡d. For the wrapping gap the representative difference is d-p, still congruent to d; no extra index n or zero multiplier is introduced. This explicitly validates that boundary case.

Both d and nd lie in 1,…,p-1. Ordinary complete multiplicativity therefore gives F(nd)=F(n)F(d) without reducing a product outside that interval. Goodness of k gives F(d)=F(k)F(z) and F(nd)=F(k)F(nz). Here nz is nonzero because n<p and p is prime. Cancelling the sign F(k) proves goodness of n for the arbitrary z, contradicting minimality. There is no circular use of the character law or of periodicity of f.

**Lines 215–235: accepted.** Each nonzero square has exactly two square roots: factorization of u²-v² and prime cancellation give u=±v, distinct for odd p. Thus there are (p-1)/2 squares. Multiplicativity makes all their F-values +1. Negation bijects the positive and negative F-fibres, each of size (p-1)/2. Hence the positive fibre is exactly the set of nonzero squares. The obstruction at a negative-sign square strictly below p follows with all hypotheses satisfied.

## 6. Residue prime from a divisor of (p+1)/4

**Lines 241–278: accepted uniformly, without a named residue theorem.**

For prime p≥7 with p≡3 mod 4, t=(p+1)/4≥2 has a prime divisor r. Writing t=rs gives s≥1, 2≤r≤t<p, and p=4rs-1. Thus p divides neither r nor any j in 1,…,h, where h=(p-1)/2=2rs-1.

The least absolute representatives alpha_j exist uniquely. Equal absolute values would imply i=j or p divides i+j; the latter is excluded by 2≤i+j≤2h=p-1. Their absolute values consequently permute 1,…,h. The product calculation and cancellation of the nonzero h! yield r^h≡(-1)^E.

The sign of alpha_j is exactly detected by the fractional part of rj/p exceeding 1/2; neither boundary value occurs. Therefore the stated floor difference counts its negativity exactly. Since 0<2rj/p<r, counting integer levels k=1,…,r-1 is valid. For each such k,

`floor(kp/(2r)) = floor(2ks-k/(2r)) = 2ks-1`.

These thresholds are nonintegral before flooring and their floors lie between 1 and h-2s. Thus the count really is h-floor(kp/(2r)), with no endpoint correction or negative count. It equals 2s(r-k), so the floor sum and E are even. This includes r=2 and s=1.

Finally 2t=h+1, so the submitted explicit root A=r^t satisfies A²≡r^(h+1)≡r. It is nonzero because r is nonzero modulo p. This proves the required prime bound. The nonempty finite set of qualifying primes at most r supplies a global least qualifying prime as claimed. No Euler criterion or quadratic reciprocity is assumed.

## 7. Prime conclusions and full assembly

**Lines 284–303: accepted.** The locally obtained q is prime and 2≤q<p. The stated FSPD prime-sign hypotheses give f(2)=f(q)=-1, while f(p)=-1 is explicit. The obstruction then contradicts the missing representation. This is a local proof, not reliance on an explorer's theorem. Substituting lambda meets every sign and multiplicativity hypothesis. The candidate also explicitly permits the direct use of the residue prime r, so no convention for a character at multiples of p is needed.

**Lines 311–317: accepted.** For p=3, the positive prime witnesses 5 and 7 sum to 12. Their primality is elementary (a composite among these would have prime divisor 2 below its square root, impossible).

For p≡1 mod 4, p≥5 is odd and not 3, so the earlier missing-pair argument applies. Pairing nonzero residues with their inverses leaves exactly 1 and -1, giving product -1. Pairing j with p-j instead gives (-1)^h(h!)². Here h is even and h! is nonzero, so -1 is a nonzero square. This contradicts F(-1)=-1 and F(z²)=1. The inverse-pair calculation is supplied locally, not assumed as Wilson's theorem. Together these cases exhaust all odd primes.

**Lines 321–330: accepted for every positive m.**

- If lambda(m)=1, the positive witnesses 2m,2m have sign -1 and sum 4m. In particular m=1 gives 2+2=4.
- If m is even, writing m=2t gives t>0. For lambda(t)=1 the witnesses 3t,5t work; for lambda(t)=-1 the witnesses 4t,4t work. Both sums are 8t=4m. Under the surrounding lambda(m)=-1 assumption the second subcase is redundant, not erroneous; the displayed pair is valid whenever its stated sign premise holds.
- Otherwise m is odd with lambda(m)=-1, so m>1. A prime divisor p is odd. In m=pd the quotient d is positive, and complete multiplicativity gives lambda(d)=1, even if p divides d. The proved representation of 4p scales by d to positive witnesses of sign -1 and total 4m. No coprimality is needed or assumed.

The sign and parity splits are exhaustive. Prime 2 is covered by the even-m case; there is no missing requirement for a separate odd-prime argument at 2. All witness restrictions match the accepted existential. Classical contradiction establishes existence with the correct quantifier order.

## 8. Remaining obligations, verdict scope, and next action

**Open load-bearing mathematical obligations: none in the reviewed content. No proof repair is requested.** The ternary descent, cyclic-gap rigidity, residue-prime parity calculation, small-prime cases, and all-m assembly are all justified as submitted. No numerical search or computational exhaustion supports this verdict.

PASS applies only to the specified mathematical lines in the identified snapshot, read with the permitted definitions and dependencies, and includes the complete all-positive-m target. It does not approve excluded material, other artifacts, the all-even target, or any future changed snapshot. No Lean build or axiom audit was performed.

Recommended next action: the leader/integrator may route this exact accepted natural-language argument to formalization of the requested theorem. Pinned compilation and axiom checks remain separate formal-validation work; this review must not be presented as their result.
