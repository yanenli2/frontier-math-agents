Mode: DISCOVERY — conjectural; no proof weight.

# Two new residual routes: reduced forms and real-norm reflections

## Scope and outcome

Owner: divergent route explorer. This file alone is the deliverable. Target: for every prime p >= 7 with p = 3 (mod 4), construct positive a,b with a+b=4p and lambda(a)=lambda(b)=-1. Here lambda(n)=(-1)^Omega(n), counting prime factors with multiplicity; all uses have n>0. Complete multiplicativity, lambda(2)=lambda(3)=-1, and the square law are the elementary inputs from the supplied candidate.

**No uniform proof for the entire residual is supplied.** The following are new, locally argued proof candidates, not independently accepted claims:

* A two-reflection construction combined with norm reduction in Z[sqrt(2)] supplies every prime p=7 (mod 8).
* An explicit discriminant -24 form reduction supplies every prime p=11 (mod 24).
* Together these would leave only p=19 (mod 24), rather than all p=3 (mod 4). This is a candidate consequence, not an edit to the canonical decomposition.
* A finite list of fixed negative-coefficient square forms cannot cover that last class: an explicit local-obstruction argument below produces arbitrarily large omitted primes. This statement uses the permitted pinned Dirichlet and reciprocity theorems with their metadata recorded below.
* A concrete **unproved first-split-prime descent lemma** is proposed for the remaining class. Its parameter genuinely grows with p; it is not an enlarged finite witness list or a restatement of the old square-shift experiment.

Recommendation order: (1) independently review the two-reflection/norm argument; (2) review the short -24 reduction; (3) investigate the first-split-prime descent, with its missing step explicit. Do not spend the next budget merely enlarging a fixed form list or rerunning Q(p).

## 1. Route A: positive binary forms, with an actual class calculation

### 1.1 A uniform family: p=11 (mod 24)

**Candidate statement.** Every prime p=11 (mod 24) has a representation

    p = 2x^2 + 3y^2,

with nonzero integers x,y. Consequently

    4p = 8x^2 + 12y^2

has two positive negative-lambda summands, since lambda(8)=lambda(12)=-1.

Here is a derivation, including the splitting and class issues.

**Elementary square test.** For an odd prime p, put h=(p-1)/2. Multiplication by any nonzero residue permutes the nonzero residues, so product cancellation gives a^(p-1)=1. The h distinct nonzero squares therefore satisfy X^h=1. A degree-h polynomial over the field has at most h roots (induction using division by X-r), so these are exactly its roots.

For an integer a coprime to p, reduce a,2a,...,ha to least absolute nonzero residues. Their absolute values permute 1,...,h: equality of two absolute values would give i=j or i+j=p, and the latter is impossible in this range. If E of these residues are negative, multiplication and cancellation yield

    a^h = (-1)^E (mod p).

This proves the particular square tests needed here, without importing a remembered supplementary law.

Write p=24s+11. For a=2, the negative count is

    h-floor(p/4) = (12s+5)-(6s+2) = 6s+3,

which is odd. For a=3, only p/2 < 3j < p contributes a negative least residue: after subtracting p, the terms with p < 3j < 3p/2 are positive. The negative count is

    floor((p-1)/3)-floor(p/6) = (8s+3)-(4s+1) = 4s+2,

which is even. Also h is odd. Thus (-6)^h=(-1)^h 2^h 3^h=1 modulo p, and the square test gives an integer r with r^2=-6 modulo p.

**From a root to a form.** The integral form

    F(X,Y) = p X^2 + 2r XY + ((r^2+6)/p) Y^2

has discriminant -24, represents p, and is positive definite: it equals

    p (X+rY/p)^2 + (6/p)Y^2.

It is primitive because p does not divide 2r: p>3 and r^2=-6 modulo p.

**Reduction, proved in this instance.** Among primitive integer pairs choose one minimizing the positive integer F-value, called A. A primitive vector extends to an integer determinant-one basis by Bezout's identity. In this basis write the form as A X^2+B XY+C Y^2. Adding an integer multiple of the first basis vector to the second makes |B|<=A. The second basis vector is primitive, so minimality gives C>=A. Integer determinant-one substitutions preserve the discriminant, by direct expansion. Hence

    24 = 4AC-B^2 >= 3A^2,

and A is either 1 or 2. Since B is even:

* A=1 forces B=0, C=6;
* A=2 allows B=0 or +/-2, but +/-2 would give C=28/8, not an integer. Thus B=0, C=3.

The inverse basis substitution is integral, so p is represented by one of X^2+6Y^2 and 2X^2+3Y^2. The former is impossible modulo 3, since p=2 (mod 3). This proves the asserted second representation. Neither coordinate can vanish: p is neither 2 times a square nor 3 times a square.

This is the needed class calculation, not the assertion that every splitting prime is automatically represented by a preferred form. Indeed, the principal form would be the wrong one for the witness construction; the modulo-3 check is what removes it.

### 1.2 Why finitely many fixed negative-coefficient forms cannot finish

**Precise scope.** Fix finitely many positive integer coefficient pairs (A_i,B_i), each satisfying lambda(A_i)=lambda(B_i)=-1. Consider constructions requiring

    4p = A_i x^2 + B_i y^2.

The following obstruction also covers fixed integer linear substitutions into such square summands. It does not purport to cover every conceivable use of forms with cross terms: a negative-lambda coefficient alone says nothing about the lambda of a general quadratic polynomial.

Let S consist of 2,3 and all prime factors of all A_i,B_i. There are arbitrarily large primes p=19 (mod 24) such that

    chi_p(q) = (q/p) = -1 for every q in S.

Construction and dependencies:

1. Require p=3 (mod 8).
2. For each odd q in S choose a nonzero residue r_q modulo q having

       (r_q/q) = -(-1)^((q-1)/2).

   Such a residue exists: exactly half the nonzero residues are squares. For q=3 this chooses r_q=1.
3. Chinese remainder combination gives a residue a modulo M=8 product_{q in S, q odd} q satisfying these requirements. Explicitly, combine local residues using M/m times its inverse modulo m for each pairwise coprime modulus m; their sum has the desired reductions. Each local residue is a unit, so gcd(a,M)=1.
4. Pinned Dirichlet gives a prime p in that residue class above any prescribed bound. In particular choose p greater than every coefficient and every member of S. Quadratic reciprocity gives chi_p(q)=-1 for odd q; the supplementary law for 2 gives the same for q=2. The requirements at 8 and 3 give p=19 (mod 24).

For these p, multiplicativity of the quadratic character gives

    chi_p(A_i)=chi_p(B_i)=-1,

because the character assigns -1 to every prime occurrence in their factorizations, just as lambda does. Also chi_p(-1)=-1. If A_i x^2+B_i y^2=0 modulo p and y is nonzero modulo p, then

    (x/y)^2 = -B_i/A_i

would make a quadratic nonresidue a square: its character is (-1)(-1)/(-1)=-1. Thus y=0 modulo p and then x=0 modulo p. An equality A_i x^2+B_i y^2=4p would therefore imply p^2 divides 4p, impossible for this odd prime.

For clarity, character multiplicativity here follows from the nonzero squares forming an index-two subgroup of the finite field's multiplicative group. Their number is (p-1)/2 by the two-to-one squaring map. The nonzero nonsquares are its other coset. The value at -1 follows from the elementary square test above.

**Implication for planning.** This is a genuine local obstruction to finishing by any fixed finite list of this type, irrespective of class-number calculations. Additional forms may still provide worthwhile uniform subclasses. It does not refute adaptive coefficients or the target.

## 2. Route B: two reflections plus a reduced real norm

### 2.1 A sign-choice bridge, not a fixed partner list

Let p>0. Suppose an integer d satisfies

    0<d<p,   lambda(d)=-1,   lambda(p+d)=1.

Then G(4p) follows by a complete two-case construction:

* If lambda(p-d)=-1, use (a,b)=(4d,4(p-d)).
* If lambda(p-d)=1, use (a,b)=(2(p-d),2(p+d)).

All entries are positive. Each pair sums to 4p, and multiplication by 4 preserves signs whereas multiplication by 2 reverses them.

Equivalently, failure of G(4p) would force

    lambda(p+d)=-1 whenever 0<d<p and lambda(d)=-1.       (B)

To derive this directly: the reflected pair at total p cannot be negative-negative, since scaling by 4 would solve the target. Thus lambda(p-d)=1. The pair (p-d,p+d) at total 2p cannot be positive-positive, since doubling would solve the target. Therefore lambda(p+d)=-1.

This gives a concrete target for a multiplicative collision: a negative d whose translate p+d is a square. It uses a reflection at p and another at 2p, not the earlier fixed partners or the assumption Q(p).

### 2.2 Uniform construction when p=7 (mod 8)

**Candidate norm lemma.** For every prime p=7 (mod 8) there are integers a,b with

    p = a^2-2b^2,    0<2b^2<p.

**Root input.** The permitted pinned theorem `ZMod.exists_sq_eq_two_iff` gives a square root of 2 modulo p. Its exact statement and guards are in section 4. Alternatively the elementary least-residue proof in section 1.1 gives the same input: for p=8s+7 the negative count for 2 is (4s+3)-(2s+1)=2s+2, which is even.

**Euclidean construction in Z[sqrt(2)].** Let R={u+v sqrt(2): u,v integers}, with norm N(u+v sqrt(2))=u^2-2v^2. A nonzero element has nonzero norm: an integer equality u^2=2v^2 with v nonzero would contradict parity of the exponent of 2 in the two sides. The norm is multiplicative by expansion.

For nonzero beta and any alpha, write alpha/beta=x+y sqrt(2) with rational x,y, and choose integers m,n within 1/2 of x,y. The remainder rho=alpha-beta(m+n sqrt(2)) satisfies

    |N(rho)|/|N(beta)| = |(x-m)^2-2(y-n)^2| <= 1/2 < 1.

The ordinary Euclidean algorithm on the nonnegative integer absolute norm therefore terminates and gives a greatest common divisor with a Bezout expression (successive substitutions recover that expression).

Take t^2=2 modulo p and let delta be a gcd of p and t+sqrt(2). Evaluation sqrt(2) -> -t modulo p is a ring map R -> F_p annihilating both inputs and hence their Bezout combination delta. Thus p divides N(delta). Also delta divides p, so N(delta) divides p^2 and is nonzero. Therefore |N(delta)| is p or p^2.

The second possibility is impossible. If |N(delta)|=p^2, the quotient p/delta has norm +/-1 and is a unit: its inverse is its conjugate divided by that norm, still in R. Thus delta is associated to p; since delta divides t+sqrt(2), p would divide that element in R, contradicting its sqrt(2)-coefficient 1. Consequently |N(delta)|=p. Multiplication by the unit 1+sqrt(2), whose norm is -1, changes the norm sign if necessary. We obtain an element of norm p.

**The essential size reduction.** Put epsilon=3+2sqrt(2), a positive unit of norm 1. Change the element's sign so its real embedding z is positive. Its conjugate is p/z>0. Multiplying by an appropriate integer power of epsilon puts z in

    (sqrt(2)-1)sqrt(p) <= z < (sqrt(2)+1)sqrt(p).

Such a power exists because the ratio of the endpoints is epsilon>1, whose positive powers are unbounded and negative powers approach zero. The new element still has integer coordinates a,b and norm p. Since

    b = (z-p/z)/(2sqrt(2)),

these bounds give |b|<=sqrt(p/2). Equality would require 2b^2=p, impossible for odd p. Also b cannot vanish, since p is not a square. This proves 0<2b^2<p and completes the norm lemma.

Now take d=2b^2. It has negative lambda, whereas p+d=a^2 has positive lambda. Section 2.1 gives the desired representation. More explicitly, with T=p-2b^2>0:

* if lambda(T)=1, use (2a^2,2T);
* if lambda(T)=-1, use (8b^2,4T).

This construction works uniformly over every p=7 (mod 8); it is not inferred from a sample. The lambda(T)=-1 branch does not require the old Q(p).

### 2.3 An exact limit of the simplest extension

It is tempting to replace 2 by any d with lambda(d)=-1 and seek

    p=x^2-dy^2,  0<dy^2<p.

That would again solve the target by section 2.1. However, **this entire strengthened square-collision ansatz fails at p=43**, even with d allowed to depend arbitrarily on p. The only integers x with 43<x^2<86 have |x|=7,8,9, and

    7^2-43=6=2*3,
    8^2-43=21=3*7,
    9^2-43=38=2*19.

All three differences have lambda +1. They cannot equal d y^2 with lambda(d)=-1 and y nonzero. The primality of 43 and of the displayed factors is checked by division by primes at most their square roots. This is a counterexample to that ansatz, not to G(172): for example 172=44+128 has both signs negative.

Thus a successful extension of the reflection route must permit a positive-sign translate p+d that is not necessarily a square, or use more than this particular two-square norm collision.

## 3. Concrete unproved next lemma: first-split-prime descent

This is the recommended genuinely adaptive obligation; it is not asserted proved.

Write chi_p(n)=(n/p) for p not dividing n. For p>=7, p=3 (mod 4), let q be the least prime with chi_p(q)=1.

### 3.1 The parameter exists with a useful elementary bound

Let t=(p+1)/4>=2 and choose a prime r dividing t. Then r<=t<p.

* If r=2, then p=7 (mod 8), so chi_p(2)=1.
* If r is odd, then p=-1 modulo r. Reciprocity, together with p=3 (mod 4), gives

      chi_p(r)=(-1)^((r-1)/2) chi_r(p)
              =(-1)^((r-1)/2) chi_r(-1)=1.

The value chi_r(-1)=(-1)^((r-1)/2) follows from the square test of section 1.1. Consequently

    q <= (p+1)/4.

All prime factors below q have character -1. Thus lambda(n)=chi_p(n) for 1<=n<q, while lambda(q)=-1 differs from chi_p(q)=1. More generally the same agreement holds for numbers whose prime factors are all below q. This identifies a least discrepancy, rather than guessing a small shift.

### 3.2 Proposed descent lemma, precise statement

**FSPD — unproved.** Let p>=7 be prime with p=3 (mod 4), and let q be its least quadratic-residue prime. Let f be any completely multiplicative function from the positive integers to {+1,-1} such that f(p)=-1 and f(r)=-1 for every prime r<=q. Then there are positive a,b with a+b=4p and f(a)=f(b)=-1.

Taking f=lambda would close the original residual. This proposed lemma is stronger than the desired lambda assertion: values at primes greater than q, except p, are unrestricted. It is therefore a substantive descent hypothesis, not a supplied theorem. A countermodel to FSPD would only refute this stronger route.

The arguments above establish its q=2 and q=3 instances: q=2 corresponds to p=7 (mod 8); when q=3, the other allowed residual congruence is p=11 (mod 24). The character counts in section 1.1 also give chi_p(3)=-1 for p=19 (mod 24): the negative count is (8s+6)-(4s+3)=4s+3. Hence the remaining case has q>=5.

**Mechanism to attempt.** Under a hypothetical missing pair, the reflections at totals p, 2p and 4p give one-sided sign implications; in particular (B) remains valid for f because f(2)=-1. Multiplication or division by a prime less than q has a known sign and agrees with the quadratic character. One should try to transport the first discrepancy f(q) != chi_p(q) through these reflections and such divisions until it becomes a discrepancy at a smaller positive argument. A usable proof must provide an integer descent parameter, keep every reflected argument inside its positive permitted interval, and justify every division. None of those global descent steps has been supplied here.

**Main blocker.** Absence of negative-negative pairs does not itself give the exact identity f(x)f(p-x)=-1: positive-positive pairs at total p are still allowed. Importing a character-rigidity argument that assumes an exact reflection-product identity would be an unjustified strengthening. The one-sided-to-rigidity step is the open mathematical obligation.

### 3.3 Why the small-prime data must be adaptive

The obstruction in section 1.2 gives more than a problem for forms. Fix any finite set S of prescribed negative primes containing 2 and 3. Choose p as there, and define for n=p^v m, p not dividing m,

    f(n)=(-1)^v chi_p(m).

This is completely multiplicative, satisfies f(p)=-1 and f(r)=-1 for all r in S, yet has no negative-negative pair summing to 4p. If neither summand is divisible by p, their characters are opposite because chi_p(-1)=-1. Otherwise the pair is (p,3p), its reverse, or (2p,2p); the signs are respectively (-,+), (+,-), or (+,+), since chi_p(2)=chi_p(3)=-1.

This explicit model proves that complete multiplicativity plus any *fixed finite* list of negative prime values and f(p)=-1 cannot establish the uniform target for arbitrary f. It does not model lambda at all primes. FSPD avoids this obstruction by requiring the negative value precisely at the first split prime, a parameter not uniformly bounded as p varies by the same CRT/Dirichlet construction.

## 4. Sources, guards, and computational record

### Pinned mathematical source dependencies

Local root for all source paths below:

    .clawcodex/math-team/problems/liouville-goldbach-jul2026/lean/.lake/packages/mathlib/

`git rev-parse HEAD` returned exactly `905b95818eb32af7874a58b427f50c1711a5e96c`. The existing P/sources.md records this release as publicly available 2026-07-28, before the cutoff. No web or current-branch source was used.

1. **Dirichlet:** Michael Stoll, `Mathlib/NumberTheory/LSeries/PrimesInAP.lean`, lines 501–506, `Nat.forall_exists_prime_gt_and_modEq`:

       (n : Nat) {q a : Nat} (hq : q != 0) (h : a.Coprime q) :
         exists p > n, p.Prime and p congruent a modulo q.

   Used only for the structural noncoverage statements, not to construct target witnesses. Application: modulus M>0, CRT residue a coprime to M, bound n above all fixed coefficients and S. All guards were checked in section 1.2. Source URL: https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/NumberTheory/LSeries/PrimesInAP.lean

2. **Quadratic reciprocity:** Chris Hughes and Michael Stoll, `Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean`, lines 99–108, `legendreSym.quadratic_reciprocity`, with prime instances for p,q and guards p!=2, q!=2, p!=q:

       legendreSym q p * legendreSym p q
         = (-1)^(p/2 * (q/2)).

   `legendreSym p a` denotes (a/p). Used in sections 1.2 and 3.1. In 1.2 choose p above all fixed odd q; in 3.1 the odd divisor r satisfies r<p. Thus all oddness, primality and distinctness guards hold. The natural quotients p/2, q/2 are (p-1)/2, (q-1)/2 for these odd primes.

3. **Supplement for 2:** same file/authors, lines 71–77, `ZMod.exists_sq_eq_two_iff`, with `[Fact p.Prime]` and p!=2:

       IsSquare (2 : ZMod p) iff p % 8 = 1 or p % 8 = 7.

   Used for the root in section 2.2, the nonresidue at p=3 (mod 8) in 1.2, and the divisor-2 case of 3.1. Every such p is odd prime. Section 1.1 also supplies a local elementary alternative for the residue cases. Source URL for items 2–3: https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean

These are mathematical source applications, not new Lean compilation or kernel-check claims. The source theorems do not assume any Liouville representation statement, so there is no circular target dependency. Form reduction, Euclidean norm reduction, reflection assembly, and the explicit obstruction at 43 are local deductions with their arguments above.

Context read, not imported as a theorem: Alexander P. Mangerel, *On a Goldbach-type problem for the Liouville function*, arXiv:2404.12117v2 (2024-05-02), preserved `P/knowledge/mangerel-v2/paper.pdf`, SHA-256 `ae26a659220985c55576a18d05a84d5a56988024f8781ae4ccbe04847ac16505`, PDF pages 1–5. The proof-strategy discussion on page 2 and exact-product hypothesis on page 4 motivate the character comparison. Their stronger hypothesis has not been inferred from failure of the present target, and no asymptotic theorem from that paper is a dependency.

### Exactly two bounded structural diagnostics

Both were in-memory Python 3 tests of abstract multiplicative sign constraints, **not** extensions of the lambda or Q(p) no-counterexample sample. Prime-factor exponent parities encode each f(n). A reflected pair forbids both encoded parities from being 1; linear equations over F_2 propagate the forced signs. Each diagnostic had an 8-second and 200000-search-node cap. Both ended at one search node, without branching.

1. p=43, numbers below 172, with f(r)=-1 for r in {2,3,5,7,11,43}: the program returned inconsistent missing-pair constraints. Independently, the displayed pair 44+128 proves this instance already from f(11)=f(2)=-1.
2. p=31, numbers below 124, with f(2)=f(3)=f(31)=-1: the program returned inconsistent constraints. An independent elementary certificate is: if f(13)=-1 use 72+52; if f(13)=1 use 26+98. Their signs follow from 72=2*6^2, 52=4*13, 26=2*13, and 98=2*7^2. The initial execution hit a Python-version `int.bit_count` compatibility error; the identical mathematical scope was rerun with `bin(...).count("1")`. No third diagnostic scope was tested.

These computations carry no proof weight. The explicit certificates and the general arguments do not rely on their output. No further computation is needed to review the two proposed uniform subfamilies. Any substantial search for or against FSPD should be routed by the leader to the code executor; the next priority is a mathematical descent or an exact countermodel, not a larger sample of the original assertion.

## 5. Precise unresolved endpoint

Neither route closes all p=19 (mod 24). The finite fixed-square-form ansatz is locally obstructed in that class. The simple arbitrary-negative-coefficient real-norm extension already fails at 43. The adaptive first-split-prime descent lemma remains unproved, and it is not an added assumption of the target. No claim in this file has been marked independently verified, and no canonical artifact or Lean source was changed.
