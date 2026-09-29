# Every positive multiple of four has a Liouville-negative representation

For a positive integer \(n\), let \(\Omega(n)\) be the number of prime factors of \(n\), counted with multiplicity, and put
\[
\lambda(n)=(-1)^{\Omega(n)}\in\mathbb Z.
\]
In particular, \(\Omega(1)=0\). Write \(\operatorname{HasRepresentation}(N)\) for the assertion that there exist \(a,b\in\mathbb N\) such that
\[
0<a,\qquad 0<b,\qquad N=a+b,\qquad
\lambda(a)=\lambda(b)=-1.
\]
Equal witnesses are allowed.

**Theorem.** For every \(m\in\mathbb N\) with \(m>0\),
\[
\operatorname{HasRepresentation}(4m).
\]

## 1. Elementary Liouville facts

Positive prime factorization gives, for all positive integers \(u,v\),
\[
\Omega(uv)=\Omega(u)+\Omega(v),
\qquad
\lambda(uv)=\lambda(u)\lambda(v).
\tag{1}
\]
No coprimality assumption is needed: multiplicities add even when the two factors have common prime divisors. Also,
\[
\lambda(1)=1,\qquad \lambda(n)\in\{1,-1\}\quad(n>0),
\qquad \lambda(r)=-1\quad(r\text{ prime}).
\tag{2}
\]
Consequently,
\[
\lambda(2)=\lambda(3)=\lambda(5)=-1,
\qquad \lambda(4)=1,
\qquad \lambda(t^2)=1\quad(t>0).
\tag{3}
\]
These are the positive-argument factorization identities; no value of \(\lambda(0)\) will be used.

We also use two elementary consequences of prime factorization. A prime dividing a product divides at least one factor, so cancellation by a nonzero residue is valid modulo a prime. Every integer greater than \(1\) has a prime divisor: its least divisor greater than \(1\) must be prime, since a nontrivial proper factor of that divisor would be a smaller divisor greater than \(1\).

## 2. Reduction to odd primes

It suffices to prove
\[
\operatorname{HasRepresentation}(4p)
\quad\text{for every odd prime }p.
\tag{4}
\]
Indeed, suppose (4) holds and let \(m>0\).

If \(\lambda(m)=1\), choose
\[
a=b=2m.
\]
Both witnesses are positive, their sum is \(4m\), and (1) gives \(\lambda(2m)=-1\). This includes \(m=1\), with witnesses \(2,2\).

Next suppose \(\lambda(m)=-1\) and \(m\) is even. Write \(m=2t\); the division is exact and \(t>0\). The following two sign cases give positive witnesses of total \(8t=4m\):
\[
\begin{array}{c|c|c}
\text{condition}&a&b\\ \hline
\lambda(t)=1&3t&5t\\
\lambda(t)=-1&4t&4t
\end{array}
\]
In the first row, (1) and the prime values at \(3,5\) give both signs \(-1\). In the second, \(\lambda(4)=1\) gives both signs \(-1\). Thus the displayed construction works for every positive even \(m\); under the present additional assumption \(\lambda(m)=-1\), only the first row is needed.

It remains to consider odd \(m\) with \(\lambda(m)=-1\). Since \(\lambda(1)=1\), we have \(m>1\). Choose a prime divisor \(p\) of \(m\), and write
\[
m=pd,\qquad d>0.
\]
The prime \(p\) is odd, since it divides the odd integer \(m\). By (1),
\[
-1=\lambda(m)=\lambda(p)\lambda(d)=-\lambda(d),
\]
so \(\lambda(d)=1\). If \(a,b>0\) witness (4), then \(da,db>0\),
\[
da+db=d(4p)=4m,
\qquad
\lambda(da)=\lambda(d)\lambda(a)=-1,
\qquad
\lambda(db)=-1.
\]
There is no requirement that \(d\) be coprime to \(p,a\), or \(b\). These cases prove the reduction. Conversely, the theorem for every positive \(m\) immediately includes every odd prime \(m=p\).

We now prove (4).

## 3. Consequences of a missing representation

For the next two sections, let \(p\) be an odd prime with \(p\ne3\), and let
\[
f:\mathbb Z_{>0}\longrightarrow\{1,-1\}
\]
be completely multiplicative, with
\[
f(2)=f(p)=-1.
\]
Assume, for contradiction, that there are no positive integers \(a,b\) with
\[
a+b=4p,\qquad f(a)=f(b)=-1.
\tag{5}
\]
All arguments of \(f\) below are positive integers.

Complete multiplicativity and the nonzero sign values imply
\[
f(1)=1,\qquad f(t^2)=1\quad(t>0),\qquad f(4)=1.
\]
Since \(p+3p=4p\) and \(f(p)=-1\), assumption (5) forces \(f(3p)=1\). Therefore
\[
f(3)=-1.
\tag{6}
\]
More generally, whenever \(0<a<4p\) and \(f(a)=-1\), the positive complement \(4p-a\) has sign \(1\).

Two useful implications follow by scaling positive pairs:
\[
0<u<p,\quad f(u)=-1
\quad\Longrightarrow\quad f(p-u)=1;
\tag{A}
\]
otherwise \(4u\) and \(4(p-u)\) would be positive negative-sign witnesses of total \(4p\), since \(f(4)=1\). Likewise,
\[
0<v<2p,\quad f(v)=1
\quad\Longrightarrow\quad f(2p-v)=-1;
\tag{C}
\]
otherwise \(2v\) and \(2(2p-v)\) would both have sign \(-1\), since \(f(2)=-1\).

Combining (A) with (C) applied to \(v=p-u\) gives
\[
0<u<p,\quad f(u)=-1
\quad\Longrightarrow\quad f(p+u)=-1.
\tag{B}
\]
Here \(0<p-u<p<2p\), so this application of (C) is within its stated domain.

For completeness, the same implications give local ternary identities. If \(0<3x<p\), then
\[
f(p+3x)=-f(x)=f(3x),\qquad f(p-x)=-f(x).
\tag{7}
\]
To see the first identity, if \(f(x)=-1\), then (A) gives \(f(p-x)=1\). Equation (6) makes \(3(p-x)\) negative in sign, so its complement \(p+3x\) has sign \(1=-f(x)\). If instead \(f(x)=1\), then \(f(3x)=-1\), and (B) applied to \(3x<p\) gives \(f(p+3x)=-1=-f(x)\).

For the second identity in (7), the case \(f(x)=-1\) is (A). If \(f(x)=1\) and also \(f(p-x)=1\), then both \(p+3x\) and \(3(p-x)\) have sign \(-1\), contradicting (5). Every complement just used is positive: \(p-x>0\), \(0<3(p-x)<3p<4p\), and \(0<p+3x<2p\).

The local identity (7) is not being assumed outside its interval. The following descent proves the full identity separately.

## 4. Ternary gap descent and full antireflection

Call a pair \((x,y)\) a defect if
\[
x>0,\qquad y>0,\qquad x+y=p,\qquad f(x)=f(y)=1.
\]
In particular, both \(x\) and \(y\) lie strictly below \(p\). We prove that no defect exists.

### 4.1. Neither entry of a defect is divisible by three

Suppose \(x=3u\) in a defect. Then \(0<u<p\), and (6) gives \(f(u)=-1\). By (A), \(f(p-u)=1\), whence
\[
f(3p-x)=f(3(p-u))=-1.
\]
On the other hand, (C) applied to \(v=y\), where \(0<y<p<2p\), gives
\[
f(p+x)=f(2p-y)=-1.
\]
These arguments are positive and have total \(4p\). More precisely,
\[
2p<3p-x<3p,\qquad p<p+x<2p.
\]
This contradicts (5). Thus \(3\nmid x\); the same argument with \(x,y\) exchanged gives \(3\nmid y\).

### 4.2. Exact division gives another defect

Because \(p\) is prime and \(p\ne3\), we also have \(3\nmid p\). The nonzero residues of \(x,y\) modulo \(3\) must therefore agree: distinct nonzero residues would be \(1,2\), whose sum is \(0\) modulo \(3\). It follows that
\[
p+x=2x+y\equiv0\pmod3,
\qquad
p+y=x+2y\equiv0\pmod3.
\]
Thus the divisions in
\[
x'=\frac{p+x}{3},\qquad y'=\frac{p+y}{3}
\tag{8}
\]
are exact. Both new integers are positive, and
\[
x'+y'=\frac{2p+x+y}{3}=p.
\]
By (C), applied to \(y\) and \(x\) respectively,
\[
f(p+x)=f(p+y)=-1.
\]
Since \(p+x=3x'\), \(p+y=3y'\), and \(f(3)=-1\), complete multiplicativity gives
\[
f(x')=f(y')=1.
\]
Hence \((x',y')\) is again a defect. Its entries, being positive and summing to \(p\), are both strictly less than \(p\).

### 4.3. The positive integer gap decreases

As \(p\) is odd, a defect cannot have \(x=y\). If any defect exists, exchange its entries to arrange \(x<y\), and choose one for which the positive integer gap
\[
\delta=y-x
\]
is minimal. Such a minimum exists, since the possible pairs form a finite set. Construction (8) preserves the order and gives
\[
0<y'-x'=\frac{y-x}{3}=\frac{\delta}{3}<\delta.
\]
The new gap is an integer because both divisions in (8) have already been proved exact. We have obtained another defect with a smaller positive integer gap, a contradiction.

There are therefore no positive-positive sign pairs of total \(p\). There are also no negative-negative sign pairs of that total, by (A). Since the only signs are \(1,-1\), we conclude that
\[
\boxed{\ f(p-n)=-f(n)\quad\text{for every }0<n<p.\ }
\tag{9}
\]

## 5. Antireflection forces multiplicativity on nonzero residues

We now prove an independent lemma: if \(p\) is an odd prime, \(f\) is completely multiplicative on positive integers with values in \(\{1,-1\}\), and (9) holds, then its values on \(1,\ldots,p-1\) define a multiplicative function on nonzero residues modulo \(p\). In particular that function is positive on every nonzero square. This lemma requires no assumption about \(f(p)\).

Let
\[
R_p=(\mathbb Z/p\mathbb Z)\setminus\{0\},
\]
and write \(\bar n\) for the residue of an integer \(n\). For \(z\in R_p\), let \(n\in\{1,\ldots,p-1\}\) be its unique representative and define
\[
F(z)=f(n).
\]
This definition does not assert that \(f\) is periodic. Prime cancellation ensures that products of nonzero residues are nonzero. Also, multiplication by a nonzero residue is injective on the finite set \(R_p\), hence is a permutation. It therefore attains \(1\), so each nonzero residue has an inverse.

By (9),
\[
F(-z)=-F(z)\quad(z\in R_p),\qquad F(1)=1,
\qquad F(-1)=-1.
\tag{10}
\]
Call \(a\in R_p\) a good multiplier if
\[
F(az)=F(a)F(z)\quad\text{for every }z\in R_p.
\tag{11}
\]
The residues \(1\) and \(-1\) are good. The product of two good multipliers \(a,b\) is good: goodness first gives \(F(ab)=F(a)F(b)\), and then, for every \(z\in R_p\),
\[
F(abz)=F(a)F(bz)=F(a)F(b)F(z)=F(ab)F(z).
\tag{12}
\]

### 5.1. A cyclic short-multiple lemma

Let \(2\le n<p\), and let \(z\in R_p\). We claim that there are integers \(k,d\) satisfying
\[
0<|k|<n,\qquad d>0,\qquad nd<p,
\qquad \bar k z=\bar d.
\tag{13}
\]

Consider the \(n\) residues
\[
0,z,2z,\ldots,(n-1)z.
\]
They are distinct. Indeed, an equality between the multiples with distinct indices would, by cancellation of \(z\), make \(p\) divide a nonzero integer of absolute value less than \(n<p\).

Sort their representatives in \(\{0,\ldots,p-1\}\) as
\[
c_1<c_2<\cdots<c_n.
\]
The circular gaps are
\[
c_2-c_1,\ c_3-c_2,\ \ldots,\ c_n-c_{n-1},\ p+c_1-c_n.
\]
All \(n\) gaps are positive integers, and their sum is \(p\). Thus some gap \(d\) satisfies \(d\le p/n\). Since \(p\) is prime and \(2\le n<p\), the integer \(n\) does not divide \(p\). The integer \(d\) therefore cannot equal \(p/n\), so
\[
1\le d<\frac pn,\qquad nd<p.
\tag{14}
\]

For each representative \(c_j\), retain its original index \(i_j\in\{0,\ldots,n-1\}\), so that \(c_j\) represents \(i_jz\). If the chosen gap is \(c_{j+1}-c_j\), take \(k=i_{j+1}-i_j\). If it is the wrapping gap \(p+c_1-c_n\), take \(k=i_1-i_n\). In either case the indices are distinct, so \(0<|k|<n\). In the first case their representatives differ by \(d\); in the wrapping case they differ by \(d-p\). Both differences are congruent to \(d\) modulo \(p\). Thus \(\bar k z=\bar d\), proving (13), including the wrapping case.

### 5.2. The least bad multiplier cannot exist

Suppose some multiplier is not good, and choose the least representative
\[
n\in\{1,\ldots,p-1\}
\]
of a bad multiplier. Since \(1\) is good, \(2\le n<p\). Every positive integer \(j<n\) represents a good multiplier. Because \(-1\) is good and good multipliers are closed under products, every nonzero integer \(k\) with \(|k|<n\) also represents a good multiplier. Here negative integers are used only as representatives of residue classes, never as arguments of \(f\).

Fix any \(z\in R_p\), and choose \(k,d\) from (13). Since \(d\) and \(nd\) are positive integers less than \(p\), ordinary complete multiplicativity gives
\[
F(\overline{nd})=f(nd)=f(n)f(d)
               =F(\bar n)F(\bar d).
\tag{15}
\]
No product has been reduced past \(p\) in this application of \(f\).

On the other hand, \(\bar k\) is good and \(\bar k z=\bar d\), so
\[
F(\bar d)=F(\bar k)F(z).
\tag{16}
\]
Also \(\bar n z\ne0\), and \(\bar k\bar n z=\overline{nd}\). Goodness of \(\bar k\) therefore gives
\[
F(\overline{nd})=F(\bar k)F(\bar n z).
\tag{17}
\]
Combining (15)–(17) and cancelling the nonzero sign \(F(\bar k)\) yields
\[
F(\bar n z)=F(\bar n)F(z).
\]
The residue \(z\) was arbitrary, so \(\bar n\) is good, contradicting its choice. All multipliers are therefore good, and
\[
F(ab)=F(a)F(b)\quad(a,b\in R_p).
\tag{18}
\]
In particular,
\[
F(z^2)=F(z)^2=1\quad(z\in R_p).
\tag{19}
\]
The strict bound \(nd<p\) from the circular-gap argument is what justifies the passage from ordinary multiplicativity in (15) to the residue identity (18).

### 5.3. The obstruction supplied by a nonzero square

Combining §§3–5, under the missing-pair assumption (5), the induced function satisfies both
\[
F(-1)=-1
\quad\text{and}\quad
F(z^2)=1\quad(z\in R_p).
\tag{20}
\]
Consequently, if a positive integer \(r<p\) has \(f(r)=-1\) and is a nonzero square modulo \(p\), then
\[
-1=f(r)=F(\bar r)=1,
\]
a contradiction. Only the values of \(f\) at the representatives \(1,\ldots,p-1\) define \(F\); no periodicity of \(f\) at larger integers has been used.

## 6. A small quadratic-residue prime for \(p\equiv3\pmod4\)

**Lemma.** If \(p\ge7\) is prime and \(p\equiv3\pmod4\), there exists a prime \(r\) such that
\[
r\le\frac{p+1}{4}<p
\]
and \(r\) is a nonzero square modulo \(p\).

**Proof.** The integer
\[
t=\frac{p+1}{4}
\]
is at least \(2\). Choose a prime divisor \(r\) of \(t\), and write \(t=rs\) with \(s\ge1\). All these divisions are exact, and
\[
r\ge2,\qquad r\le t<p,\qquad p=4rs-1.
\tag{21}
\]
We will prove directly that this \(r\) is a square modulo \(p\).

Set
\[
h=\frac{p-1}{2}=2rs-1.
\]
For each \(j\in\{1,\ldots,h\}\), let \(\alpha_j\) be the unique representative of \(rj\) modulo \(p\) in
\[
\{-h,\ldots,-1,1,\ldots,h\}.
\]
It exists because \(p\nmid rj\): both \(r\) and \(j\) are positive and less than \(p\), and \(p\) is prime.

The absolute values \(|\alpha_j|\) permute \(1,\ldots,h\). Indeed, if \(|\alpha_i|=|\alpha_j|\), then \(ri\equiv rj\) or \(ri\equiv-rj\pmod p\). Cancellation of \(r\) gives \(i\equiv j\) or \(i+j\equiv0\pmod p\). The first implies \(i=j\), since both indices lie between \(1\) and \(h<p\). The second is impossible, since
\[
2\le i+j\le2h=p-1.
\]
Thus the absolute values are distinct, and there are \(h\) of them in a set of size \(h\).

Let \(E\) be the number of negative \(\alpha_j\). Taking products gives
\[
r^h h!\equiv\prod_{j=1}^h\alpha_j
             =(-1)^E h!\pmod p.
\]
Every factor of \(h!\) lies strictly between \(0\) and \(p\), so \(h!\) is nonzero modulo \(p\) and can be cancelled. Therefore
\[
r^h\equiv(-1)^E\pmod p.
\tag{22}
\]

We now determine the parity of \(E\) by a finite floor calculation. The representative \(\alpha_j\) is negative precisely when the fractional part of \(rj/p\) exceeds \(1/2\). The fractional part is not \(0\), since \(p\nmid rj\), and is not \(1/2\), since a residue divided by the odd integer \(p\) cannot equal \(1/2\). Hence
\[
E=\sum_{j=1}^h
\left(\left\lfloor\frac{2rj}{p}\right\rfloor
      -2\left\lfloor\frac{rj}{p}\right\rfloor\right).
\tag{23}
\]
Each summand is \(0\) or \(1\), and is \(1\) exactly for a negative representative. In particular, \(E\) has the same parity as
\[
S=\sum_{j=1}^h\left\lfloor\frac{2rj}{p}\right\rfloor.
\]
Since
\[
0<\frac{2rj}{p}\le\frac{r(p-1)}p<r,
\]
we may count the integer levels \(k=1,\ldots,r-1\) to obtain
\[
S=\sum_{k=1}^{r-1}
\#\left\{j\in\{1,\ldots,h\}:\frac{2rj}{p}\ge k\right\}.
\tag{24}
\]
For each such \(k\), (21) gives
\[
\frac{kp}{2r}=2ks-\frac{k}{2r}.
\]
Here \(0<k/(2r)<1\), so the threshold is nonintegral and
\[
\left\lfloor\frac{kp}{2r}\right\rfloor=2ks-1.
\tag{25}
\]
Moreover,
\[
1\le2ks-1\le2s(r-1)-1=h-2s<h.
\]
Thus there is no truncation at either endpoint of \(\{1,\ldots,h\}\). Because the threshold is nonintegral, the number of indices in (24) is exactly
\[
h-\left\lfloor\frac{kp}{2r}\right\rfloor
=(2rs-1)-(2ks-1)=2s(r-k).
\tag{26}
\]
Every term in (26) is even. Consequently \(S\), and hence \(E\), is even. Equation (22) gives
\[
r^h\equiv1\pmod p.
\]
Finally, \(2t=h+1\), so the explicit integer \(A=r^t\) satisfies
\[
A^2=r^{2t}=r^{h+1}\equiv r\pmod p.
\]
Since \(r\not\equiv0\pmod p\), this is a nonzero square, proving the lemma. \(\square\)

## 7. Representations for every odd prime

We apply the preceding arguments with \(f=\lambda\). Equations (1)–(3) give complete multiplicativity, the two sign values, and \(f(2)=f(p)=-1\) whenever \(p\) is prime.

### 7.1. Primes congruent to three modulo four

Let \(p\ge7\) be prime with \(p\equiv3\pmod4\). Suppose \(\operatorname{HasRepresentation}(4p)\) fails. All hypotheses of §§3–5 hold, so a negative-sign nonzero square strictly below \(p\) would contradict §5.3.

The lemma in §6 supplies precisely such an integer: it gives a prime \(r<p\) that is a nonzero square modulo \(p\), while \(\lambda(r)=-1\). This contradiction proves
\[
\operatorname{HasRepresentation}(4p).
\]

### 7.2. Primes congruent to one modulo four

Let \(p\equiv1\pmod4\) be prime. Then \(p\ge5\), so \(p\) is odd and \(p\ne3\). If \(\operatorname{HasRepresentation}(4p)\) failed, §§3–5 would again yield (20). We show directly that \(-1\) is a nonzero square modulo \(p\), contradicting (20).

Every residue in \(R_p\) has an inverse, as proved in §5. Pair each residue with its inverse. The self-inverse residues satisfy \(a^2=1\), hence
\[
(a-1)(a+1)=0.
\]
Prime cancellation shows that they are exactly \(1\) and \(-1\), which are distinct because \(p\) is odd. Every other inverse pair has product \(1\). Therefore the product of all nonzero residues is \(-1\).

Put \(h=(p-1)/2\). Pairing the integer representatives instead as \(j,p-j\), for \(j=1,\ldots,h\), gives
\[
\prod_{a=1}^{p-1}\bar a
=\prod_{j=1}^{h}\bar j\,\overline{p-j}
=(-1)^h\bigl(\overline{h!}\bigr)^2.
\]
Since \(p\equiv1\pmod4\), the integer \(h\) is even. Comparing the two products yields
\[
\bigl(\overline{h!}\bigr)^2=-1.
\]
The residue \(\overline{h!}\) is nonzero because all its factors lie in \(\{1,\ldots,p-1\}\). Thus (19) gives \(F(-1)=1\), whereas (10) gives \(F(-1)=-1\), a contradiction. This proves \(\operatorname{HasRepresentation}(4p)\) in this case also.

### 7.3. The prime three

For \(p=3\), take the positive witnesses
\[
12=5+7.
\]
The integers \(5,7\) are prime: a composite among them would have a proper factor between \(2\) and its square root, hence an integer factor \(2\), but both are odd. Thus \(\lambda(5)=\lambda(7)=-1\).

Every odd prime is either \(3\), congruent to \(1\) modulo \(4\), or congruent to \(3\) modulo \(4\) and at least \(7\). The three cases prove (4).

## 8. Conclusion for every positive multiplier

The odd-prime assertion (4), together with the reduction in §2, proves the theorem for every \(m>0\). Explicitly, the diagonal witnesses \(2m,2m\) handle \(\lambda(m)=1\); the positive scaled pairs from \(8=3+5=4+4\) handle even \(m\); and for odd \(m\) with \(\lambda(m)=-1\), a prime factorization \(m=pd\) with \(\lambda(d)=1\) scales a representation of \(4p\) to one of \(4m\).

In every case the witnesses are positive natural numbers, their sum is exactly \(4m\), and each has Liouville value \(-1\). No distinctness, parity, or coprimality condition is imposed on the witnesses. \(\square\)

## Mathematical sources

- The definitions are those of [`Statement/Definitions.lean`](../../lean/Statement/Definitions.lean), `omega` and `lambda`, and [`Statement/Partial.lean`](../../lean/Statement/Partial.lean), `HasSignedRepresentation` and `HasRepresentation`. The elementary identities in §1 are `omega_mul`, `lambda_one`, `lambda_sign`, `lambda_mul`, and `lambda_prime` in `Partial.lean`; the factor-list inputs are `Nat.perm_primeFactorsList_mul` and `Nat.primeFactorsList_prime`.
- The local arguments are from [`nl/descent/proof-attempt-v1.md`](nl/descent/proof-attempt-v1.md), with the following scope: its §0 baseline supplies §1 above; its §§1–2 supply §3; its §3 supplies §4; its §§4–5 supply §5; its §6 supplies §6; and its §§7–8 supply the prime cases, reduction, and final assembly in §§2, 7–8. The floor-parity and inverse-pairing arguments are proved here directly; neither quadratic reciprocity nor a sum-of-two-squares theorem is invoked.
