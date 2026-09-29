# Multiple-of-four representation: proof attempt v1

Mode: CERTIFICATION — candidate production, not self-acceptance.

**Status: INCOMPLETE. The requested theorem remains unresolved.** This file supplies new elementary partial arguments and an exact smaller prime-core equivalence for independent review. In particular, the argument below covers every positive m not congruent to 3 modulo 4. It does not cover every m congruent to 3 modulo 4.

Let P be `.clawcodex/math-team/problems/liouville-goldbach-jul2026` and W be `P/waves/multiples-four`. The companion ledger is `W/nl/generator/obligations-v1.md`.

## 0. Exact target and inputs

For n > 0, Ω(n) counts prime factors with multiplicity and λ(n) = (-1)^Ω(n), with λ(1) = 1. Write

- P_s(N): there are positive integers a,b with N = a+b and λ(a) = λ(b) = s;
- G(N): P_{-1}(N).

The sole assigned target is

> T4: for every positive integer m, G(4m).

Equal summands are allowed. There is no restriction on parity, primality, or coprimality of witnesses. No use is made of λ(0). The approved type is exactly

```lean
theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :
  ArithmeticStatement.HasRepresentation (4 * m)
```

Inputs read:

1. `W/request.md` and `W/formal/approved-v1/Declaration.lean`;
2. `P/lean/Statement/Definitions.lean` and `P/lean/Statement/Partial.lean`;
3. the self-contained mathematics in `P/FINAL_ARGUMENT.md`;
4. `P/sources.md` and the assigned protocol/workflow files.

No external analytic theorem, literature result, history-review verdict, or original all-even target is used as a premise. The two-squares result needed below is derived here, not imported by name. All new arguments are unreviewed candidates, not new Lean theorems.

Input SHA-256 identities, recomputed for this attempt:

| Path | SHA-256 |
|---|---|
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `W/formal/approved-v1/Declaration.lean` | `bdfb30bcfade7b9df33e48f280125d10a40dd76f365cf5b87047183475fee7ed` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `P/FINAL_ARGUMENT.md` | `1b93364b818b0eae95875d391ca6f944614f00b963a1e384ba1a0fe2533957a9` |
| `P/sources.md` | `9df552348f03fd84ffe0e203f1340f26e6a902f8424f924068fe6fb86c1a7dbb` |

## 1. Accepted elementary dependencies

The following exact statements come from `Partial.lean`; their derivations are also given in `FINAL_ARGUMENT.md` §§2–3.

1. For n > 0, λ(n) is either 1 or -1 (`lambda_sign`, lines 51–55).
2. For u,v > 0, λ(uv) = λ(u)λ(v), with no coprimality hypothesis (`lambda_mul`, lines 62–64). The underlying factor-list product identity is `omega_mul`, lines 57–60.
3. For any prime q, λ(q) = -1 (`lambda_prime`, lines 66–68). Also λ(1)=1, λ(2)=-1, λ(4)=1, and λ(t²)=1 for t>0 (lines 43–49, 70–82, 93–96).
4. Consequently λ(2t)=-λ(t) for t>0 (`lambda_two_mul`, lines 88–91).
5. If d>0 and P_s(N), then P_{λ(d)s}(dN): multiply both positive witnesses by d (`hasSignedRepresentation_mul`, lines 102–109).
6. For every t>0, G(8t) (`representation_multiple_eight`, lines 150–159). Its construction uses 8=3+5 with both signs negative and 8=4+4 with both signs positive, choosing the seed according to λ(t).

Positive prime factorization is the accepted factor-list input: for n>0 the list consists of primes and its product is n. Thus any n>1 has a prime divisor. The permutation statement for the factor list of a product, already used in dependency 2, also supplies the ordinary prime cancellation fact used below: a prime dividing uv divides u or v. Indeed, if it divided neither, neither factor list would contain that prime, whereas the factor list of uv would have to contain it.

## 2. Uniform mechanism I: scaling and a least-counterexample reduction

### 2.1 Cases already covered, with the correct sign

Take m>0.

- If λ(m)=1, use a=b=2m. Each witness is positive, their sum is 4m, and λ(2m)=-1. This includes m=1 and gives 4=2+2.
- If m is even, write m=2t with t>0 and use G(8t) from §1.6.

Consequently a counterexample can only have m odd and λ(m)=-1. In particular m>1, since λ(1)=1.

Let p be **any** prime divisor of such an m, and write m=pd. Then p is odd, d is a positive integer, and

λ(m)=λ(p)λ(d)=-λ(d)=-1,

so λ(d)=1. If a,b witness G(4p), then da,db are positive, sum to 4pd=4m, and retain sign -1. Therefore

> If m is odd, λ(m)=-1, and p divides m is prime, then G(4p) implies G(4m).

No representation for a composite number is divided by p here; witnesses are constructed by multiplication, in the direction justified by §1.5.

### 2.2 Exact first core equivalence

The preceding case split proves

> T4 if and only if G(4p) holds for every odd prime p.

The forward implication simply substitutes m=p in T4. For the reverse implication, the diagonal and all-8t cases settle λ(m)=1 and even m, respectively; otherwise choose a prime divisor p and apply §2.1. These alternatives exhaust all positive m.

Equivalently, if T4 has a least positive counterexample m, then m is an odd prime. Indeed, m is odd with λ(m)=-1. If m were composite, a prime divisor p would satisfy p<m; minimality would give G(4p), and §2.1 would contradict failure at m.

This is a reduction, not a proof that the prime core holds. Minimality gives no smaller positive-sign seed at 4p when m=p.

### 2.3 Why direct use of the seed 4 stops

There is no positive-positive representation of 4. Its positive ordered decompositions are

1+3, 2+2, 3+1,

with signs (+,-), (-,-), (-,+). Thus the successful negative seed 4=2+2 cannot be paired with a positive seed at the same total. Scaling 2+2 by a multiplier of sign -1 gives two positive signs, exactly the wrong output. This refutes this particular two-sign-seed argument at 4, not T4.

There is a useful extra seed at 12:

12=5+7 has signs (-,-), and 12=6+6 has signs (+,+), since λ(6)=λ(2)λ(3)=1.

Here 7 is prime because neither 2 nor 3 divides it and any proper factor would have a prime divisor at most its square root. The two-sign scaling rule proves G(12t) for every t>0. In particular all m divisible by 3 satisfy T4, and G(4p) is settled at p=3.

## 3. A second constructive family: two squares, proved locally

This supplies genuinely new uniform cases beyond all multiples of eight. It will remove every prime p congruent to 1 modulo 4 from the remaining core.

### 3.1 Square-sum construction

Suppose m=u²+v²>0 with nonnegative integers u,v.

If u≠v, put

A=2(u+v)²,  B=2|u-v|².

Both square roots are positive: u+v>0 follows from m>0, and |u-v|>0 follows from u≠v. Consequently λ(A)=λ(B)=-1 by §1.3–4, and

A+B=2((u+v)²+(u-v)²)=4(u²+v²)=4m.

If u=v, then u>0 and 4m=8u², covered by §1.6. Therefore every positive sum of two squares m satisfies G(4m).

### 3.2 Elementary derivation for primes p=1 modulo 4

Let p be a prime congruent to 1 modulo 4; in particular p≥5. We prove p=u²+v².

**A root of -1 modulo p.** For every nonzero residue a modulo p, multiplication by a permutes the nonzero residues: if ai=aj modulo p, prime cancellation gives i=j modulo p. Hence a has an inverse among these residues. The residues equal to their own inverses satisfy a²=1 modulo p. Prime cancellation in (a-1)(a+1)=0 modulo p shows that they are exactly 1 and -1. Pair every other residue with its distinct inverse. Their paired products are 1, so multiplication of all nonzero residues gives

(p-1)! = -1 modulo p.

This is the full inverse-pair proof of the factorial congruence used here; no separate Wilson-theorem input is assumed.

Write h=(p-1)/2. This h is even because p=1 modulo 4. Pair j with p-j for 1≤j≤h to obtain

(p-1)! = (-1)^h (h!)² = (h!)² modulo p.

With t=h!, the last two congruences give t²=-1 modulo p.

**A bounded nonzero lattice vector.** The prime p is not a square: a square r² with r≥2 has the proper divisor r, and 1 is not prime. Choose the integer s with s²<p<(s+1)². Consider the (s+1)² pairs (i,j) with 0≤i,j≤s and their residues i+tj modulo p. There are only p residues, but (s+1)²>p. If every residue had at most one such pair there would be at most p pairs, a contradiction. Thus two distinct pairs have equal residues.

Subtract the two pairs, obtaining integers x,y, not both zero, with |x|≤s, |y|≤s, and x+ty=0 modulo p. It follows that

x²+y² = (t²+1)y² = 0 modulo p.

At the same time,

0 < x²+y² ≤ 2s² < 2p.

A positive integer divisible by p and smaller than 2p must equal p: writing it as kp gives a positive integer k<2, hence k=1. Therefore x²+y²=p. Taking u=|x| and v=|y| yields the desired nonnegative integer squares.

As p is odd, u=v is impossible: that would give p=2u². The pair of §3.1 is consequently positive without invoking its equal-coordinate subcase. This proves, within this candidate,

> Every prime p congruent to 1 modulo 4 satisfies G(4p), with witnesses 2(u+v)² and 2|u-v|² obtained above.

Every load-bearing step here is finite: prime cancellation, inverse pairing, counting (s+1)² residue inputs, the norm bound strictly below 2p, and the displayed witness identity. No distribution theorem about primes is involved.

## 4. Strongest universal reduction established in this attempt

Define the still-unproved assertion

> C3: for every prime p≥7 with p=3 modulo 4, G(4p).

Then the arguments supplied above establish the exact equivalence

> **T4 if and only if C3.**

Proof of the converse, with every case: for an arbitrary m>0, first use the diagonal if λ(m)=1. If m is even, use all-8t. In the remaining case m is odd and λ(m)=-1, choose a prime divisor p and write m=pd with d>0 and λ(d)=1 as in §2.1. The prime p is odd. If p=3, use the seed 12=5+7. If p=1 modulo 4, use §3. If p=3 modulo 4 and p≠3, then p≥7 and C3 supplies G(4p). In every subcase scale the two negative witnesses by d. The forward implication evaluates T4 at the primes in C3.

C3 has not been used anywhere except as the stated hypothesis of this converse implication. In particular it is not a premise appended to the requested theorem and is not asserted as proved.

Further unconditional consequences of the same arguments are:

1. G(4m) whenever m>0 and λ(m)=1, or m is even, or 3 divides m.
2. G(4m) whenever m has a prime divisor p=1 modulo 4. To check the sign case not explicit in §2.1: if λ(m)=1 use the diagonal; if λ(m)=-1, writing m=pd gives λ(d)=1 and the same scaling works, even if m was not first assumed odd.
3. In particular G(4m) for **every positive m=1 modulo 4**. If such an m had λ(m)=-1 and no prime divisor 1 modulo 4, all its prime occurrences would be 3 modulo 4. Their number Ω(m) is odd, so their product would be (-1)^Ω(m)=-1 modulo 4, contradicting m=1 modulo 4. The case m=1 already uses the diagonal.

Thus G(4m) is supplied for all m not congruent to 3 modulo 4. In terms of N, among positive multiples of 4, the only residue class not uniformly settled here is N=12 modulo 16. Many numbers in that class are also settled by the other conditions above. A least counterexample, if one exists, must be a prime m=p≥7 with p=3 modulo 4.

## 5. Uniform mechanism II: additive reflection and doubling

We now confront the remaining prime cores rather than invoking an already covered family. Fix a prime p≥7 with p=3 modulo 4 and suppose, for the following implications only, that G(4p) fails.

### 5.1 Three exact forbidden-sign implications

All differences in this subsection are positive by their stated ranges.

- For 0<x<4p, if λ(x)=-1, then λ(4p-x)=1. Otherwise x and its reflection would witness G(4p).
- For 0<x<2p, if λ(x)=1, then λ(2p-x)=-1. Otherwise doubling a positive-positive pair of total 2p would give a negative-negative pair of total 4p.
- For 0<x<p, if λ(x)=-1, then λ(p-x)=1. Otherwise multiplying a negative-negative pair of total p by 4 would preserve both signs and give total 4p.

Each deduction uses only the dichotomy of signs and a forbidden actual witness, not an assertion about a mean value of λ.

In particular, take 0<t<2p with λ(t)=1. The second implication gives λ(2p-t)=-1. Reflecting this negative number at 4p using the first implication gives λ(2p+t)=1. Thus failure would impose the simultaneous condition

(**)  λ(2p-t)=-1 and λ(2p+t)=1 for every 0<t<2p with λ(t)=1.

There is no derivation here of a contradiction from (**). Complete multiplicativity alone does not evaluate either of these translates from the value at t.

### 5.2 The exact missing construction on this route

The sufficient shift assertion for a given p is

S(p): there exists t with 0<t<2p and λ(t)=1 such that

λ(2p-t)=1  or  λ(2p+t)=-1.

If the first alternative holds, take

(a,b)=(2t, 2(2p-t)).

Both factors being doubled have positive sign, so both witnesses have negative sign, are positive, and sum to 4p. If only the second alternative is known, split on λ(2p-t). Its positive case is the preceding construction; its negative case gives

(a,b)=(2p-t, 2p+t),

again a positive negative-negative pair of total 4p. This proves S(p) implies G(4p). It does not prove S(p) for all remaining primes. No equivalence between S(p) and G(4p) is claimed.

### 5.3 Failure of a substantially enlarged fixed list

The following five possible pairs cover several first reflection/doubling choices:

(2,4p-2), (8,4p-8), (12,4p-12),
(2p-2,2p+2), (2p-1,2p+1).

For all p≥7 every entry is positive and the sum is 4p. Their respective sufficient sign tests are

- λ(2p-1)=1;
- λ(p-2)=-1;
- λ(p-3)=-1;
- λ(p-1)=λ(p+1)=1;
- λ(2p-1)=λ(2p+1)=-1.

They do **not** constitute a uniform construction. The prime p=163 is 3 modulo 4 and defeats all five. Its primality can be checked by the primes 2,3,5,7,11, which are all primes at most its square root. The exact factorizations give:

| Pair, at 4p=652 | Factorizations | Signs |
|---|---|---|
| (2,650) | 2; 2·5²·13 | (-,+) |
| (8,644) | 2³; 2²·7·23 | (-,+) |
| (12,640) | 2²·3; 2⁷·5 | (-,+) |
| (324,328) | 2²·3⁴; 2³·41 | (+,+) |
| (325,327) | 5²·13; 3·109 | (-,+) |

All displayed factors are primes. For the largest new factor 109, trial division by 2,3,5,7 suffices because its square root is below 11; the smaller factors are checked by the smaller applicable subsets. Thus the failures follow from parity of the displayed exponent sums, not merely from a search output.

This is not a counterexample to the target: 652=50+602, with 50=2·5² and 602=2·7·43, has two negative signs. Here 43 is prime by trial division by 2,3,5. This example also shows why adding a few more fixed pairs is not the uniform missing argument.

### 5.4 A structural limit of the two-squares construction

For p=3 modulo 4, it is impossible to solve 4p=2u²+2v² with integer u,v. Such a solution would give 2p=u²+v², but 2p=6 modulo 8, whereas squares modulo 8 belong to {0,1,4} and their pairwise sums belong to {0,1,2,4,5}. Thus the successful construction in §3 cannot be extended to these primes merely by finding a different pair of square roots. This does not obstruct general witnesses, which need not be twice squares.

## 6. One concrete alternative left open

An adaptive square-shift assertion would suffice:

> Q(p): there is an integer k≥1 with k²<2p and λ(2p-k²)=1.

If Q(p) holds, set a=2k² and b=2(2p-k²). Positivity follows from the strict inequality, the total is 4p, and the square law and doubling give λ(a)=λ(b)=-1. This is S(p) with t=k² and its first alternative.

The precise proposed next mathematical task is to prove Q(p) for every prime p≥7 congruent to 3 modulo 4, or identify a genuine counterexample to Q(p) and enlarge the adaptive family. Q(p) is strictly a proposed sufficient route; it is not supplied as a theorem or silently attached to T4. The complement is allowed to be any positive-sign integer, not another square: requiring another square is ruled out by §5.4. For example p=163 admits k=5, since 326-25=301=7·43 has positive sign, giving the pair (50,602).

### Bounded diagnostics, not proof

Two in-memory Python 3 experiments were run, with no output or source files written outside the two assigned artifacts. They used an exact smallest-prime-factor sieve and the recurrence λ(n)=-λ(n/spf(n)), starting with λ(1)=1.

1. Sieve bound 200000. The five-pair search had the range cap 7≤p<50000, restricted to primes p=3 modulo 4, and stopped on its fifth failure at p=1531. Its first five failures were 163, 367, 827, 907, 1531. The factorization argument above independently proves the first failure. A separate diagnostic in the same run scanned all odd primes 3≤p<50000 and found no prime p≥5 lacking a negative-negative representation of p; p=3 was its only exception. This is not a proof of an odd-prime representation theorem, and that theorem is not a dependency here.
2. Sieve bound 400000. For every tested prime 7≤p<200000 with p=3 modulo 4, some 1≤k≤floor(sqrt(2p-1)) passed Q(p). The largest observed least successful k was 14, at p=170243. The command also returned k=2 at p=7, k=5 at p=163, and k=4 at p=367.

No finite run proves C3, S(p), or Q(p). The record explicitly stops at the stated bounds; there is no effective all-large-p argument, nor any claimed finite-to-infinite inference.

## 7. Final assembly status

The proposed partial proof contains complete local arguments for:

- the sign-preserving reduction from an arbitrary unresolved m to a prime divisor;
- the exact reduction T4 to odd prime cores;
- G(4m) for positive sums of two squares, including a self-contained proof that primes 1 modulo 4 are such sums;
- G(12t) for all t>0;
- the sharper equivalence T4 iff C3 and, in particular, every m not congruent to 3 modulo 4;
- the reflection/doubling implications and the conditional witness constructions S(p) and Q(p).

The single universal endpoint still missing is

> For every prime p≥7 with p=3 modulo 4, there are positive a,b with a+b=4p and λ(a)=λ(b)=-1.

Neither minimal-counterexample scaling, the additive sign implications, the five fixed pairs, nor the square construction supplies that statement. No contradiction to the requested theorem has been found. No Lean source was edited or newly compiled. A fresh verifier must review the proposed partial deductions; only the leader can route or publish an accepted extension.
