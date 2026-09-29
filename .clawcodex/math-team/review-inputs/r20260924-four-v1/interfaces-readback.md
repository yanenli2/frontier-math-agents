# Literal readback

Scope: only `Interfaces.lean`, `Declaration.lean`, `Dependencies.lean`, and `ListOperations.lean` at the supplied paths were read. No intent comments were present. The supplied theorem declarations have no proof bodies; this report reads their types, not their proofs.

## 1. Definitions and literal assertion

Write \(F(n)=n.\mathrm{primeFactorsList}\) and \(\Omega(n)=\mathrm{length}(F(n))\). The supplied recursion sets \(F(0)=F(1)=[]\), and for \(n=k+2\) puts the least prime factor \(q=\mathrm{minFac}(n)\) at the front of \(F(n/q)\). Division here is natural-number division. `minFac n` returns 2 when \(2\mid n\); otherwise it starts `minFacAux n` at 3. That auxiliary function, at argument \(k\), returns \(n\) if \(n<k^2\), otherwise returns \(k\) if \(k\mid n\), otherwise continues at \(k+2\).

List length is 0 on the empty list and increases by 1 on each cons. Thus \(\Omega\) counts prime factors **with multiplicity**, not distinct prime factors. In particular, the supplied definitions give \(\Omega(0)=\Omega(1)=0\).

The integer-valued sign is
\[
\lambda(n)=(-1)^{\Omega(n)}.
\]
Consequently, sign \(-1\) means an odd factor count, sign \(+1\) means an even factor count, and \(\lambda(0)=\lambda(1)=1\).

Use these abbreviations throughout the report:
\[
S(s,N)\;:\!\iff\;\exists a:\mathbb N,\ \exists b:\mathbb N,\quad
0<a\ \land\ 0<b\ \land\ N=a+b\ \land\lambda(a)=s\ \land\lambda(b)=s,
\]
\[
R(N)\;:\!\iff\;S(-1,N).
\]
These are exactly `HasSignedRepresentation s N` and `HasRepresentation N`. Each occurrence introduces its own witnesses. The definition of \(S\) has parameters \(s:\mathbb Z\), then \(N:\mathbb N\), followed by witnesses \(a\), then \(b\).

Write \(P(p)\) for `Nat.Prime p`. Its supplied characterization is
\[
P(p)\iff 2\le p\ \land\ \forall r:\mathbb N,\ r<p\to r\mid p\to r=1.
\]

### Main declaration

`representation_multiple_four` literally asserts
\[
\forall m:\mathbb N,\quad 0<m\ \to\
\exists a:\mathbb N,\ \exists b:\mathbb N,\quad
0<a\land0<b\land4m=a+b\land\lambda(a)=-1\land\lambda(b)=-1.
\]

In words: every positive multiple of 4 is a sum of two positive natural numbers, each having an odd number of prime factors counted with multiplicity.

### Interface declarations

All variables in the following formulas are natural numbers unless a sign is explicitly displayed. Universals are written in declaration order; arrows retain the order of the hypotheses. Every \(R\) and \(S\) expands as above at its displayed position.

1. **`lambda_six`:** \(\lambda(6)=1\), an equality in \(\mathbb Z\).
2. **`lambda_seven`:** \(\lambda(7)=-1\), an equality in \(\mathbb Z\).
3. **`twelve_two_sign_seed`:** \(S(-1,12)\land S(1,12)\). There is a negative-sign pair and, independently, a positive-sign pair for 12.
4. **`representation_multiple_twelve`:** \(\forall t,\ 0<t\to R(12t)\).
5. **`representation_multiple_four_of_lambda_one`:** \(\forall m,\ 0<m\to\lambda(m)=1\to R(4m)\).
6. **`representation_multiple_four_of_even`:** \(\forall m,\ 0<m\to\operatorname{Even}(m)\to R(4m)\).
7. **`representation_multiple_four_of_three_dvd`:** \(\forall m,\ 0<m\to3\mid m\to R(4m)\).
8. **`representation_multiple_four_of_sum_two_squares`:** \(\forall m,\forall u,\forall v,\ 0<m\to m=u^2+v^2\to R(4m)\).
9. **`prime_one_mod_four_eq_sum_two_squares`:** \(\forall p,\ P(p)\to p\bmod4=1\to\exists u,\exists v,\ p=u^2+v^2\).
10. **`representation_four_prime_one_mod_four`:** \(\forall p,\ P(p)\to p\bmod4=1\to R(4p)\).
11. **`prime_divisor_positive_sign_cofactor`:** \(\forall m,\forall p,\ 0<m\to\lambda(m)=-1\to P(p)\to p\mid m\to\exists d,\ 0<d\land\lambda(d)=1\land m=dp\).
12. **`exists_prime_factor_of_lambda_neg_one`:** \(\forall m,\ 0<m\to\lambda(m)=-1\to\exists p,\exists d,\ P(p)\land0<d\land\lambda(d)=1\land m=dp\).
13. **`representation_multiple_four_of_prime_divisor`:** \(\forall m,\forall p,\ 0<m\to\lambda(m)=-1\to P(p)\to p\mid m\to R(4p)\to R(4m)\).
14. **`representation_multiple_four_of_prime_one_mod_four_dvd`:** \(\forall m,\forall p,\ 0<m\to P(p)\to p\mid m\to p\bmod4=1\to R(4m)\). There is no sign hypothesis on \(m\) here.
15. **`exists_prime_one_mod_four_of_lambda_neg_one`:** \(\forall m,\ 0<m\to m\bmod4=1\to\lambda(m)=-1\to\exists p,\ P(p)\land p\mid m\land p\bmod4=1\).
16. **`representation_multiple_four_of_mod_four_one`:** \(\forall m,\ 0<m\to m\bmod4=1\to R(4m)\).
17. **`representation_multiple_four_of_mod_four_ne_three`:** \(\forall m,\ 0<m\to m\bmod4\ne3\to R(4m)\).
18. **`multiple_four_iff_odd_prime_core`:**
    \[
    (\forall m,\ 0<m\to R(4m))\quad\iff\quad
    (\forall p,\ P(p)\to p\ne2\to R(4p)).
    \]
19. **`multiple_four_iff_prime_three_mod_four_core`:**
    \[
    (\forall m,\ 0<m\to R(4m))\quad\iff\quad
    (\forall p,\ P(p)\to7\le p\to p\bmod4=3\to R(4p)).
    \]

The last two assertions are equivalences between entire universally quantified propositions. They are not pointwise equivalences between one chosen \(m\) and one chosen \(p\), and an equivalence by itself does not separately assert either side.

## 2. Quantifiers and witness dependencies

- Lean's implicit natural-number parameters in braces are universal, just like the explicit parameters. Hypothesis binders are subsequent implications; they are not existential witnesses.
- In the main declaration the order is \(m\), the assumption \(0<m\), then \(a\), then \(b\). The pair may vary with \(m\); there is no pair chosen before all \(m\).
- For every representation conclusion above, \(a\), then \(b\), occur after all displayed input variables and hypotheses. Thus the sum-of-two-squares representation interface has universal inputs \(m,u,v\), followed by its two hypotheses, followed by representation witnesses. It does not itself existentially choose \(u,v\).
- In the prime sum-of-two-squares interface, \(u\), then \(v\), are existential after the input \(p\) and its two hypotheses.
- In interface 11, \(p\) is an arbitrary supplied prime divisor; only \(d\) is existential, after the inputs \(m,p\) and all four hypotheses.
- In interface 12, \(p\) is existential after \(m\) and its hypotheses, and \(d\) is existential after \(p\). In interface 15, only \(p\) is existential after \(m\) and its three hypotheses.
- The two conjuncts in the seed theorem each have their own \(\exists a\,\exists b\). They do not demand that a single pair have both signs.
- Interface 13 contains \((\exists a_0\,\exists b_0,\ldots)\to(\exists a\,\exists b,\ldots)\). The first representation is a premise. No equation relating the output pair to a particular pair witnessing the premise is asserted.
- In each core equivalence, the \(m\)-quantifier on the left and \(p\)-quantifier on the right have separate scopes. Each representation pair occurs inside the corresponding universal quantifier and its implications.

### Supporting declaration types

For completeness, the other supplied supporting claims read as follows; they introduce no extra assumptions into the main declaration:

- `minFac_dvd`: \(\forall n,\ \mathrm{minFac}(n)\mid n\).
- `minFac_prime`: \(\forall n,\ n\ne1\to P(\mathrm{minFac}(n))\). The hypothesis is not \(n>1\); it also permits 0.
- `minFac_le_of_dvd`: \(\forall n,\forall r,\ 2\le r\to r\mid n\to\mathrm{minFac}(n)\le r\).
- `primeFactorsList_zero`, `primeFactorsList_one`, `primeFactorsList_two`: respectively \(F(0)=[]\), \(F(1)=[]\), and \(F(2)=[2]\).
- `primeFactorsList_add_two`: \(\forall n,\ F(n+2)=\mathrm{minFac}(n+2)::F((n+2)/\mathrm{minFac}(n+2))\).
- `prime_of_mem_primeFactorsList`: \(\forall n,\forall p,\ p\in F(n)\to P(p)\).
- `prod_primeFactorsList`: \(\forall n,\ n\ne0\to\mathrm{prod}(F(n))=n\). The nonzero premise is explicit.
- `Prime.primeFactorsList_pow`: \(\forall p,\ P(p)\to\forall n,\ F(p^n)=\mathrm{replicate}(n,p)\). The exponent is quantified after the primality hypothesis and may be 0.
- `List.replicate` has argument order \(n\), then the repeated element; it returns the empty list at 0 and adds one copy at each successor. `length_nil` says the empty list has length 0; `length_cons` says \(\mathrm{length}(a::as)=\mathrm{length}(as)+1\), universally for the element and tail. Their element type is an arbitrary type in an arbitrary supplied universe; here factor lists specialize it to \(\mathbb N\).

## 3. Pointwise versus aggregate conditions

- Positivity and sign conditions are **pointwise**: each summand separately is positive and separately has the specified sign. Negative representations require two odd factor counts, not merely a condition on their sum or on a product of signs.
- \(N=a+b\), \(m=u^2+v^2\), \(p=u^2+v^2\), and \(m=dp\) are **aggregate equalities** relating their respective variables. There are no average, density, or asymptotic bounds.
- No upper bound on a representation summand is separately written. Positivity and the sum equality entail \(1\le a,b\le N-1\). For \(R(N)\), the signs additionally exclude 1, so \(2\le a,b\le N-2\).
- The square variables are only required to be natural numbers. The sum equality bounds each square by the total, but no separate positivity or balance condition is imposed on \(u,v\).
- The cofactor is pointwise positive with sign \(+1\); its product with the prime equals \(m\). Neither factor receives a separately stated upper bound.
- \(7\le p\) is an inclusive pointwise lower bound in the last core. The other core uses \(p\ne2\), together with primality. Neither has an upper bound on \(p\).
- List length aggregates the number of list entries, including repetitions. No theorem here imposes a fixed numerical upper bound on a factor count.

## 4. Constants, domains, and restrictions

All numerical constants are fixed literals, not existentially selected parameters. There is no hidden threshold, unspecified constant, or uniformity constant.

| Literal | Role and restrictions |
| --- | --- |
| \(0\in\mathbb N\) | Natural-number lower endpoint, empty-list length, empty replication case, and excluded value in strict positivity premises. \(F(0)\) is explicitly empty. |
| \(1\in\mathbb N\) | Empty-factor-list input, list-length increment, successor in replication, sole smaller divisor in the prime characterization, modulus residue, and excluded input in `minFac_prime`. |
| \(+1,-1\in\mathbb Z\) | Fixed sign values; \(-1\) is also the base defining \(\lambda\). `HasRepresentation` fixes sign \(-1\), not an arbitrary sign. |
| \(2\in\mathbb N\) | Square exponent; least possible prime in the supplied characterization; even-divisibility test; factor-list recursion offset; auxiliary-search increment; divisor lower bound; excluded prime in the odd-prime core. |
| \(3\in\mathbb N\) | Auxiliary-search starting value, fixed divisor in interface 7, and residue used in interfaces 17 and 19. |
| \(4\in\mathbb N\) | Fixed multiplier in the main assertion and most representation interfaces, and fixed modulus. |
| \(6\in\mathbb N\) | Fixed argument of `lambda_six`. |
| \(7\in\mathbb N\) | Fixed argument of `lambda_seven` and inclusive prime lower bound in the final core. |
| \(12\in\mathbb N\) | Fixed total in the two-sign seed and fixed multiplier in interface 4. |

The parameter \(s\) in \(S(s,N)\) ranges over all integers without an explicit restriction, but a representation can only have \(s=\pm1\). All other arithmetic variables range over \(\mathbb N\), hence are nonnegative before additional hypotheses. Strict positivity is imposed exactly where shown in the formulas. Prime inputs satisfy \(p\ge2\). Natural remainders modulo 4 lie between 0 and 3, so “not 3” permits residues 0, 1, and 2. There are no explicit upper bounds on \(m,t,p\), or the domain of the main assertion.

## 5. Vacuity, empty objects, and trivial witnesses

- Conditional interfaces make no claim when their hypotheses fail. In particular, \(m=0\) and \(t=0\) are excluded where positivity is required; \(m=1\) cannot meet a negative-sign hypothesis; and nonprimes cannot meet prime hypotheses.
- The final core excludes the prime 3 by \(7\le p\). The odd-prime core excludes 2 but includes 3. These are genuine differences between the literal right-hand propositions.
- The empty factor lists at 0 and 1 give sign \(+1\), not \(-1\). They do not allow a zero or unit summand in \(R(N)\). The positive-sign seed still forbids zero summands through its positivity conditions, but its definition does not forbid unit summands.
- Positive summands make \(S(s,0)\) and \(S(s,1)\) impossible. Likewise, signs other than \(\pm1\) make \(S(s,N)\) impossible. Such sign parameters do not occur in the asserted seed or main representation.
- There is no requirement that \(a\ne b\), that either summand be prime, that the summands be coprime, or that one be smaller than the other. Equal summands are allowed whenever they meet the displayed conditions. Odd factor count is weaker than primality.
- Zero is allowed for either square variable; both being zero is incompatible with the positive total or prime total. The square roots are not asserted to be the representation summands.
- The cofactor \(d=1\) is permitted, since it is positive and has sign \(+1\). There is no requirement that \(d>1\), that it be prime, or that it be coprime to \(p\).
- The conjunction of the two seed representations does not contain a same-witness sign contradiction. No globally contradictory premise was identified from the displayed restrictions; proving satisfiability or validity of the declarations was not undertaken.
- No empty list is itself a representation witness: representation witnesses are two natural numbers. No constant witness pair independent of the target is requested.

## 6. Verdict

**READBACK-CLEAN.** No code-based ambiguity or internal specification conflict was identified in this literal reading. The key scope facts are that representations use separate positive summands of sign \(-1\), factor counts include multiplicity, square roots need not be positive, and the last core covers only primes \(p\ge7\) with residue 3 modulo 4.

This label certifies neither proof validity nor correspondence to any unseen source.
