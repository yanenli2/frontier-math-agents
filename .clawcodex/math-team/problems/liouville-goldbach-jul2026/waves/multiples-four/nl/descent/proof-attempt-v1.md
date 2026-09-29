# Uniform prime-core proof attempt: ternary gap descent and character rigidity

Mode: CERTIFICATION — candidate production; not independently accepted.

**Status: a full rigorous candidate is supplied. No mathematical step is intentionally left open. Fresh independent verification is required, especially for §§3–5. No Lean compilation or acceptance is claimed.**

Let P be `.clawcodex/math-team/problems/liouville-goldbach-jul2026` and W be `P/waves/multiples-four`. The companion obligation ledger is `W/nl/descent/obligations-v1.md`.

## 0. Exact target, scope, and dependency boundary

The assigned uniform target is:

> For every prime p >= 7 with p congruent to 3 modulo 4, there are positive integers a,b such that a+b=4p and lambda(a)=lambda(b)=-1.

Here lambda(n)=(-1)^Omega(n), and Omega counts prime factors with multiplicity. Equal summands are allowed. The parent target is `ArithmeticStatement.HasRepresentation (4*m)` for every positive natural m. All occurrences of lambda below have positive arguments.

This attempt proves a stronger intermediate assertion: under absence of a negative-negative representation of 4p, an arbitrary completely multiplicative sign function with f(2)=f(p)=-1 must agree on 1,...,p-1 with the quadratic character modulo p. The missing full reflection identity is obtained by an explicit integer descent. A finite, locally proved small-residue-prime lemma then closes FSPD and the assigned Liouville case.

The explorer's real-norm and discriminant -24 arguments are **not** dependencies. Neither its unproved FSPD nor the CE hunter's computations or local identities are assumed. The CE identities are rederived in §2 before the stronger step in §3. The first-split-prime hypothesis is not abandoned: FSPD is a corollary in §7. The descent parameter is not q; it is first the gap in a hypothetical positive-positive pair, followed by the least representative of a nonmultiplicative residue multiplier.

Inputs read:

- the protocol and `W/request.md`;
- `W/nl/generator/proof-attempt-v1.md`;
- `W/nl/explorer/residual-v1.md`;
- `W/nl/ce-hunter/fspd-v1.md` and the supplied `fspd_exact.py` (the latter only as discovery context, not as a theorem);
- the exact definitions and elementary baseline declarations in `P/lean/Statement/Definitions.lean` and `P/lean/Statement/Partial.lean`.

No prior review/verdict was read. No search, solver run, or bound enlargement was performed. No external literature theorem is invoked: the finite-field, counting, character-rigidity, and residue-prime arguments are proved below. Thus no additional literature provenance or cutoff exception is needed. In particular, quadratic reciprocity, Dirichlet's theorem, norm-form classification, and an analytic Liouville theorem are not premises.

### Baseline facts and their exact provenance

The following are the elementary accepted interface from `Partial.lean`:

1. For n>0, lambda(n) is 1 or -1 (`lambda_sign`, lines 51–55).
2. For u,v>0, lambda(uv)=lambda(u)lambda(v), without a coprimality hypothesis (`lambda_mul`, lines 62–64). This follows from `omega_mul`, lines 57–60, itself the positive factor-list product identity.
3. For a prime r, lambda(r)=-1 (`lambda_prime`, lines 66–68); lambda(1)=1 (`lambda_one`, lines 47–49).
4. The definition of `HasRepresentation` is precisely the positive-witness existential with sign -1 (`Partial.lean`, lines 14–20).

These facts also follow immediately from positive prime factorization and the specified definition. Later seed and scaling arguments are written out rather than importing the generator's unreviewed extensions.

Elementary arithmetic used locally includes prime cancellation, finite counting, and a least positive integer in a nonempty set. Prime cancellation follows from prime factorization: a prime dividing a product occurs in at least one factor's prime factorization. Every integer t>1 has a prime divisor: its least divisor greater than 1 is prime, since otherwise a proper factor greater than 1 would be a smaller divisor. No additional sign hypothesis is attached to the target.

## 1. Abstract setup and missing-pair implications

For §§1–5, assume:

- p is an odd prime different from 3;
- f maps the positive integers to {1,-1} and satisfies f(uv)=f(u)f(v) for every pair of positive integers;
- f(2)=f(p)=-1;
- there is no positive pair a,b with a+b=4p and f(a)=f(b)=-1.

All statements in §§1–5 are consequences of this hypothetical missing pair, not extra assumptions in the desired conclusion. Complete multiplicativity implies f(1)=1, f(t^2)=1 for t>0, and f(4)=1.

The pair p+3p=4p, with f(p)=-1, forces f(3p)=1. Since f(3p)=f(3)f(p)=-f(3),

    f(3)=-1.                                               (1)

The following implications use only actual positive pairs of total 4p and the two possible signs:

    0<u<p, f(u)=-1  ==>  f(p-u)=1.                         (A)

Indeed, otherwise 4u and 4(p-u) both have sign -1 and sum to 4p. Likewise

    0<v<2p, f(v)=1  ==>  f(2p-v)=-1.                       (C)

Otherwise 2v and 2(2p-v) both have sign -1 and sum to 4p. Combining (A) and (C), with v=p-u, gives

    0<u<p, f(u)=-1  ==>  f(p+u)=-1.                        (B)

Here 0<p-u<p<2p, so the application of (C) is inside its domain. More generally, any known negative-sign positive a<4p has positive-sign complement 4p-a.

## 2. Independent verification of the CE hunter's local identities

Fix an integer x with 0<3x<p.

If f(x)=-1, (A) gives f(p-x)=1, so (1) gives f(3(p-x))=-1. Its positive complement at total 4p is p+3x. Thus f(p+3x)=1=-f(x).

If f(x)=1, then f(3x)=-1. Since 0<3x<p, (B) applied to u=3x gives f(p+3x)=-1=-f(x). Consequently

    f(p+3x)=-f(x)=f(3x),       0<3x<p.                     (T)

For the reflection, if f(x)=-1, (A) already gives f(p-x)=-f(x). If f(x)=1 and f(p-x)=1, (T) would give f(p+3x)=-1, while (1) gives f(3(p-x))=-1. Those two positive numbers sum to 4p, a contradiction. Hence

    f(p-x)=-f(x),              0<3x<p.                     (R-local)

Every complement used above is positive: p-x>0, 3(p-x)<3p<4p, and 0<p+3x<2p. There has been no use of a full reflection identity to prove these local ones.

The next argument supplies the missing full domain. It uses only (1), (A), and (C), rather than assuming that (R-local) extends.

## 3. New descent: remove every positive-positive pair at total p

Call an ordered pair x,y a defect if

    x>0, y>0, x+y=p, and f(x)=f(y)=1.

By (A), a negative-negative pair at total p is already impossible. Thus ruling out defects will give the exact reflection identity on all of 1,...,p-1.

### 3.1 Neither member of a defect can be divisible by 3

Suppose x=3u in a defect. Then u>0, u<p, and (1) gives f(u)=-1. By (A), f(p-u)=1. Therefore

    f(3p-x)=f(3(p-u))=-1.

On the other hand, (C) applied to v=y gives

    f(p+x)=f(2p-y)=-1.

The arguments 3p-x and p+x are positive: 0<x<p, hence 2p<3p-x<3p and p<p+x<2p. Their sum is 4p, contradicting the missing-pair assumption. Thus 3 does not divide x. The identical argument with x,y exchanged shows that 3 does not divide y.

### 3.2 Exact divisions and the smaller defect

Since p is prime and p is not 3, p is not divisible by 3. The nonzero residues of x and y modulo 3 must therefore be equal. If they were distinct, they would be 1 and 2 and their sum p would be divisible by 3. Write their common residue as r in {1,2}. Then

    p+x = 2x+y = 0 modulo 3,
    p+y = x+2y = 0 modulo 3.

Thus the following are positive integers, with exact division by 3:

    x'=(p+x)/3,       y'=(p+y)/3.

They have sum p. Applying (C) to y and x, respectively, gives f(p+x)=f(p+y)=-1. Since f(3)=-1 and p+x=3x', p+y=3y', complete multiplicativity gives

    f(x')=f(y')=1.

Therefore (x',y') is another defect.

### 3.3 Well-founded descent parameter

Because p is odd, a pair summing to p cannot have equal members. If any defect exists, exchange its entries so x<y, and choose one minimizing the positive integer

    delta=y-x.

This minimum exists; indeed there are at most p-1 ordered candidate pairs. The construction above preserves the order and gives

    0<y'-x'=(y-x)/3=delta/3<delta.

This is a smaller positive integer gap of another defect, contrary to minimality. All divisions have already been proved integral in §3.2; the new arguments are positive and sum to p, hence are themselves less than p.

There are no defects. Since neither equal sign is possible at total p, the two signs must be opposite:

> **Full reflection:** for every integer n with 0<n<p,
>
>     f(p-n)=-f(n).                                      (R-full)

This is the first global compatibility bridge. It does not follow by silently strengthening a one-sided implication; the gap descent supplies it.

## 4. Finite character-rigidity lemma, with its own descent argument

We prove the following lemma independently of the missing-pair construction.

> **Rigidity lemma.** Let p be an odd prime. Let f be completely multiplicative from the positive integers to {1,-1}. If f(p-n)=-f(n) for every 0<n<p, then the values f(1),...,f(p-1) induce a multiplicative function F on the nonzero residues modulo p. Moreover F is the quadratic character: F is 1 exactly on the nonzero squares.

No condition on f(p) is part of this lemma. No character law is assumed before its proof.

### 4.1 Residues and good multipliers

Every nonzero residue modulo p has a unique integer representative in {1,...,p-1}. Define F on that residue to be f of this representative. Then F(1)=1. Full reflection gives

    F(-z)=-F(z)          for every nonzero residue z.       (2)

In particular F(-1)=-1. Multiplication of nonzero residues stays nonzero by prime cancellation. If needed, the inverse of a nonzero residue a exists because multiplication by a is injective on the finite nonzero residue set, hence is a permutation and attains 1.

Call a nonzero residue a a good multiplier if

    F(az)=F(a)F(z)       for every nonzero residue z.

The residue 1 is good, and (2) says that -1 is good. The product of two good multipliers a,b is good: first F(ab)=F(a)F(b), and for every z,

    F(abz)=F(a)F(bz)=F(a)F(b)F(z)=F(ab)F(z).

We will show that every residue is good.

### 4.2 Cyclic short-multiple lemma

Suppose not, and let n be the least integer in {1,...,p-1} whose residue is not good. Then 2<=n<p, and every positive integer k<n represents a good multiplier. By closure with -1, every nonzero integer k with |k|<n does also.

Fix any nonzero residue z. The n residues

    0, z, 2z, ..., (n-1)z

are distinct: equality would, by cancellation of z, make p divide a nonzero integer of absolute value less than p. Put their representatives in increasing order around the circle of residues 0,...,p-1. There are n positive integral gaps between successive representatives, including the gap across p back to the first, and the gaps sum to p. Some gap d is at most p/n. As 2<=n<p and p is prime, p/n is not an integer; hence

    1<=d<p/n.                                             (3)

The endpoints of that gap came from two different indexed multiples of z. Subtract their indices in the order of the gap (also for the wrapping gap). This gives a nonzero integer k with

    |k|<n,       kz=d modulo p.                            (4)

For the wrapping gap the difference of representatives is d-p, which has the same residue as d. Thus (4) holds there as well. In particular the residue k is good.

### 4.3 Why the least bad multiplier is in fact good

By (3), d and nd are positive integers less than p. Therefore **ordinary** complete multiplicativity of f, with no reduction of a product past p, gives

    F(nd)=f(nd)=f(n)f(d)=F(n)F(d).                          (5)

By (4) and goodness of k,

    F(d)=F(kz)=F(k)F(z),
    F(nd)=F(knz)=F(k)F(nz).                                (6)

In the second equality, knz and nd are the same residue. This is an equality for F on residue classes; it is not a claim about f at a large integer or an assumed periodicity of f.

Combining (5) and (6) and cancelling the nonzero sign F(k) gives

    F(nz)=F(n)F(z).

The initial z was arbitrary, so n is good, contradicting its choice. Thus all residues are good and F is multiplicative on the nonzero residues modulo p.

The precise minimal parameter was n, the least bad representative. The only smaller multipliers used were k with 0<|k|<n, and the cyclic counting lemma supplied the strict product bound nd<p needed to bridge from f to F.

### 4.4 Identification with the quadratic character

Multiplicativity implies F(z^2)=F(z)^2=1 for every nonzero residue z. There are exactly (p-1)/2 nonzero squares: the equality u^2=v^2 implies u=v or u=-v by prime cancellation, and these two roots are distinct because p is odd.

By (2), negation is a bijection between the F-positive and F-negative nonzero residues. Hence exactly (p-1)/2 residues have F-value 1. The nonzero squares are a subset of this size, so they are exactly the residues with F-value 1. This proves the lemma, including the claimed classification.

Notice that its proof does not assume that f and the quadratic character already agree below any q.

## 5. Consequence of a missing representation

Combining §3 and §4 yields the following candidate theorem:

> If p is an odd prime different from 3, f is completely multiplicative into {1,-1}, f(2)=f(p)=-1, and 4p has no positive negative-negative f-representation, then
>
>     f(n)=chi_p(n)       for every 1<=n<p,
>
> where chi_p is 1 on nonzero squares modulo p and -1 on nonzero nonsquares.

In particular:

> Any integer r with 1<=r<p, f(r)=-1, and r a nonzero square modulo p contradicts the missing-pair hypothesis.

This proves the needed passage from one-sided constraints to character rigidity. No values of f above p-1 are classified, and none are silently made periodic. Values at larger arguments in §§1–3 occur only in the indicated positive pairs of total 4p.

## 6. Locally proved small quadratic-residue prime

To apply §5 uniformly, we need a residue prime strictly below p. We prove the explorer's useful bound without invoking quadratic reciprocity.

> **Small-residue-prime lemma.** If p>=7 is prime and p=3 modulo 4, some prime r<=(p+1)/4 is a nonzero quadratic residue modulo p. Consequently the least such prime q exists and satisfies q<=(p+1)/4<p.

Put t=(p+1)/4. Then t is an integer at least 2. Choose a prime r dividing t, and put s=t/r. Thus r>=2, s>=1, r<=t<p, and

    p=4rs-1.

We prove directly that this r is a square modulo p. In fact the following calculation works for any integer r>=2 in an identity p=4rs-1 with p prime and s>=1.

Let h=(p-1)/2=2rs-1. For each j=1,...,h choose the least absolute nonzero representative alpha_j of rj modulo p, in {-h,...,-1,1,...,h}. This is possible because p does not divide rj. Their absolute values permute 1,...,h. Indeed, an equality |alpha_i|=|alpha_j| gives ri=rj or ri=-rj modulo p; after cancellation this gives i=j or i+j=p. The latter is impossible because 2<=i+j<=2h=p-1.

Let E be the number of negative alpha_j. Taking products and cancelling h!, which is nonzero modulo p, gives

    r^h = (-1)^E modulo p.                                (7)

We now calculate the parity of E, rather than importing a residue-symbol rule. An alpha_j is negative exactly when the fractional part of rj/p exceeds 1/2. There is no equality at 0 or 1/2 because p is an odd prime and p does not divide rj. Hence

    E = sum_{j=1}^h (floor(2rj/p)-2 floor(rj/p)).

In particular E has the parity of S=sum_{j=1}^h floor(2rj/p). Since 0<2rj/p<r, a finite count by integer levels gives

    S = sum_{k=1}^{r-1} #{j in {1,...,h}: 2rj/p >= k}
      = sum_{k=1}^{r-1} (h-floor(kp/(2r))).                (8)

The quotients kp/(2r) are nonintegral for 1<=k<=r-1; this also follows directly from the next displayed expression. Using p=4rs-1,

    floor(kp/(2r)) = floor(2ks-k/(2r)) = 2ks-1.

Thus each summand in (8) is

    (2rs-1)-(2ks-1)=2s(r-k),

an even integer. Therefore E is even, and (7) gives r^h=1 modulo p.

Because 2t=h+1, the explicit integer A=r^t satisfies

    A^2 = r^(2t) = r^(h+1) = r modulo p.

This is a nonzero square root, since r is nonzero modulo p. The selected r is prime and r<=t, proving the lemma. The least residue prime q exists already among the finite nonempty set of qualifying primes at most r; any qualifying prime outside that interval is larger, so this also gives the global least prime.

All counting, parity, divisions, and bounds in this lemma have been provided. There is no assumed Euler criterion, reciprocity law, asymptotic theorem, or numerical search.

## 7. FSPD and the assigned uniform Liouville case

Take exactly the FSPD hypotheses from the explorer:

- p>=7 is prime and p=3 modulo 4;
- q is the least prime with chi_p(q)=1;
- f is completely multiplicative from the positive integers to {1,-1};
- f(p)=-1 and f(r)=-1 for every prime r<=q.

Section 6 proves q exists and q<=(p+1)/4<p. In particular q>=2, so f(2)=-1, and the hypothesis at r=q gives f(q)=-1. The integer p is odd and different from 3. If the conclusion of FSPD failed, §5 would give

    f(q)=chi_p(q)=1,

contradicting f(q)=-1. Therefore positive negative-negative witnesses of total 4p exist. This is a candidate proof of FSPD, not an invocation of FSPD as an unproved premise.

Substitute f=lambda on the positive integers. Baseline facts 1–3 in §0 verify every function hypothesis: all signs are in {1,-1}, multiplicativity is complete, and the value at every prime, including p, 2, and q, is -1. Thus

> **Assigned target:** every prime p>=7 with p=3 modulo 4 satisfies `HasRepresentation (4*p)`.

Equivalently one can bypass the name FSPD: choose the residue prime r supplied in §6; its Liouville value is -1; §5 contradicts the absence of witnesses. The primes between 2 and q are not needed in the rigidity argument, so FSPD has in fact been proved through a stronger obstruction statement.

The conclusion is an ordinary classical existence proof: absence of every allowed positive witness leads to a contradiction. No genericity, coprimality, unequal-witness, or bounded-search assumption is used.

## 8. Optional complete assembly to T4, without unreviewed route dependencies

This section records the bridge to the parent target; it is not a change to the assigned prime-core statement. We do not need to import the generator's two-squares proof.

### 8.1 The other odd primes

For p=3, 12=5+7 is a valid pair: 5 and 7 are primes and hence have Liouville value -1. Their primality is elementary; for 7 the only possible prime proper divisor at most its square root is 2, which does not divide it.

Now let p>=5 be prime with p=1 modulo 4. If `HasRepresentation (4*p)` failed, §§1–5 with f=lambda would produce a multiplicative F on the nonzero residues with F(-1)=-1 and F(z^2)=1. We show directly that -1 is a square modulo this p, a contradiction.

Every nonzero residue has an inverse by the finite permutation argument in §4.1. Pairing each residue with its inverse leaves exactly the self-inverse residues 1 and -1, since a^2=1 implies (a-1)(a+1)=0 and prime cancellation applies. Thus the product of all nonzero residues is -1 modulo p. With h=(p-1)/2, pairing the integer factors j and p-j instead gives that product as (-1)^h(h!)^2. Since p=1 modulo 4, h is even. Therefore (h!)^2=-1 modulo p, with h! nonzero. This contradicts the properties of F.

Consequently `HasRepresentation (4*p)` holds for every odd prime p: the p=3 seed, the p=1 modulo 4 argument, and §7 exhaust those primes.

### 8.2 All positive multipliers

Let m>0.

- If lambda(m)=1, take a=b=2m. Each sign is lambda(2)lambda(m)=-1, and their sum is 4m.
- Suppose lambda(m)=-1 and m is even, say m=2t with t>0. If lambda(t)=1, use (3t,5t); if lambda(t)=-1, use (4t,4t). In the first case the prime signs at 3 and 5 are negative; in the second the sign at 4 is positive and multiplication by t reverses it. Every pair is positive, negative-negative, and has total 8t=4m.
- In the remaining case m is odd and lambda(m)=-1. Since lambda(1)=1, m>1. Choose a prime divisor p of m and write m=pd with d>0. The prime p is odd. Complete multiplicativity and lambda(p)=-1 give lambda(d)=1. By §8.1 there are positive a,b with a+b=4p and lambda(a)=lambda(b)=-1. Then da,db are positive, retain sign -1, and sum to 4pd=4m.

These cases exhaust every positive natural m, including m=1. Thus the candidate also supplies the exact parent statement

    theorem representation_multiple_four (m : Nat) (hm : 0 < m) :
      ArithmeticStatement.HasRepresentation (4 * m)

at the natural-language level. No master or Lean file was changed.

## 9. Review handoff and artifact identities

The genuinely new critical steps are:

1. §3: a hypothetical positive-positive pair at total p has neither member divisible by 3, and the map (x,y) -> ((p+x)/3,(p+y)/3) yields a smaller positive integer gap;
2. §4: full reflection plus local complete multiplicativity gives global multiplicativity on nonzero residues by the least-bad-multiplier/cyclic-gap argument;
3. §6: every prime divisor of (p+1)/4 is a quadratic residue, with the full finite least-residue count supplied.

These statements require fresh verification. The author records no unresolved mathematical step, but does not certify their correctness or the final theorem. The next action is an independent mathematical review of this file and its ledger, followed only if accepted by leader-routed formalization. No review or compilation result should be inferred from artifact completion.

Input SHA-256 snapshots:

| Path | SHA-256 |
|---|---|
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` |
| `W/nl/generator/proof-attempt-v1.md` | `1730e39b6ef4eb33bc4621e26642d63b4c775415a4cdeec7de00ccff71fa89ef` |
| `W/nl/explorer/residual-v1.md` | `4725c57ed85ddeb6591e2b59e7fb4952ea0e0a8aee5fbb19f5c7669ef1002fa4` |
| `W/nl/ce-hunter/fspd-v1.md` | `1d88311deaff46496b6e33cab879003766419611da55727eb51e786e5c96eef9` |
| `W/nl/ce-hunter/fspd_exact.py` | `9af5932c7ab2e5466ea48f4b8a490aaf048baf9696032e4ab7e89def3a5f9d3a` |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
