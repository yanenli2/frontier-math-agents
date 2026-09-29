# Literal code-only readback

Scope: only the four supplied Lean files were read. No intent comments were present. This report reads definitions and declaration types; it does not verify proofs or elaboration.

## 1. Literal assertion and defined objects

The final declaration, `ArithmeticStatement.liouville_goldbach` (`Interfaces.lean:194–195`), asserts `Target` without additional hypotheses:

> For every natural number \(N\), if \(N\) is even and \(N>2\), there exist positive natural numbers \(a,b\) such that \(N=a+b\) and \(\lambda(a)=\lambda(b)=-1\).

Here the supplied definitions mean:

- \(\operatorname{Even}(N)\) is \(\exists r\in\mathbb N,\ N=r+r\).
- \(\omega(n)\) is the length of `n.primeFactorsList`. This counts prime factors **with multiplicity**, not distinct prime factors. The list is empty at both 0 and 1. For \(n\ge2\), it prepends `minFac n` and recurses on \(n/\operatorname{minFac}(n)\). `List.length` assigns length 0 to the empty list and adds 1 for each cons; repetitions count separately.
- `minFac n` returns 2 if \(2\mid n\), and otherwise invokes `minFacAux n 3`. The auxiliary function at \(k\) returns \(n\) if \(n<k^2\), otherwise returns \(k\) if \(k\mid n\), and otherwise advances to \(k+2\). The supplied prime-power list statement uses `List.replicate`, which repeats an entry the specified number of times.
- \(\lambda(n)=(-1)^{\omega(n)}\in\mathbb Z\). In particular, the definitions give \(\omega(0)=\omega(1)=0\) and \(\lambda(0)=\lambda(1)=1\).
- The supplied primality characterization is \(\operatorname{Prime}(p)\iff 2\le p\land\forall m\in\mathbb N,\ m<p\to m\mid p\to m=1\).

Thus the final assertion can also be read as requiring each summand to have an odd number of prime factors counted with multiplicity. Neither summand is required to be prime, and the summands need not be distinct.

For the remaining interface types, use these abbreviations solely for this report:

\[
\begin{aligned}
H_s(N)&\iff\exists a\in\mathbb N\,\exists b\in\mathbb N,\
 &\qquad 0<a\land0<b\land N=a+b\land\lambda(a)=s\land\lambda(b)=s,\\
H(N)&:=H_{-1}(N),\\
I_N&:=\{a\in\mathbb N:1\le a<N\},\\
J_N&:=\{a\in I_N:\lambda(a)=-1\land\lambda(N-a)=-1\},\\
O_N&:=\{(a,b)\in I_N\times I_N:N=a+b\land\lambda(a)=-1\land\lambda(b)=-1\},\\
R(N)&:=|O_N|\in\mathbb N,\\
L(x)&:=\sum_{1\le a\le x}\lambda(a)\in\mathbb Z,\\
C(N)&:=\sum_{a\in I_N}\lambda(a)\lambda(N-a)\in\mathbb Z.
\end{aligned}
\]

These are respectively `HasSignedRepresentation`, `HasRepresentation`, `I`, `representationIndices`, `orderedRepresentations`, `R`, `L`, and `C`. Subtractions in natural-number arguments, such as \(N-a\) and \(N-1\), are natural subtraction. Expressions written \((N:\mathbb Z)-1\) instead subtract in the integers. Counts are cast to integers in the displayed integer identities below.

`R` counts **ordered** pairs: different pairs \((a,b)\) and \((b,a)\) are separate elements; a diagonal pair is one element.

The other final declaration, `pointwise_keystone` (`Interfaces.lean:191–192`), asserts, for each even natural \(N>2\), the strict integer inequality

\[
2L(N-1)-\bigl((N:\mathbb Z)-1\bigr)<C(N).
\]

## 2. Quantifier order, interface assertions, and witness dependencies

Implicit Lean binders such as `{N : ℕ}` are universal, not existential. In the list below all variables are natural unless explicitly identified as integers. Arrows preserve the order of premises in the declarations.

### Main assertion

Expanding `Target` gives precisely

\[
\forall N\in\mathbb N,\quad
(\exists r\in\mathbb N,\ N=r+r)\ \to\ 2<N\ \to\
\exists a\in\mathbb N\,\exists b\in\mathbb N,\quad
0<a\land0<b\land N=a+b\land\lambda(a)=-1\land\lambda(b)=-1.
\]

The evenness witness \(r\) is internal to the antecedent, not an outer parameter. The summands are selected separately for each admissible \(N\); \(a\) precedes \(b\), so \(b\) may depend on the selected \(a\). There is no single pair required to work for different \(N\).

### Sign and multiplicative declarations

- `omega_one`: \(\omega(1)=0\).
- `lambda_one`, `lambda_two`, `lambda_three`, `lambda_four`, `lambda_five`: respectively \(\lambda(1)=1\), \(\lambda(2)=-1\), \(\lambda(3)=-1\), \(\lambda(4)=1\), and \(\lambda(5)=-1\).
- `lambda_sign`: \(\forall n,\ 0<n\to(\lambda(n)=1\lor\lambda(n)=-1)\).
- `omega_mul`: \(\forall u\,\forall v,\ 0<u\to0<v\to\omega(uv)=\omega(u)+\omega(v)\).
- `lambda_mul`: the same ordered binders and premises, concluding \(\lambda(uv)=\lambda(u)\lambda(v)\).
- `lambda_prime`: \(\forall p,\ \operatorname{Prime}(p)\to\lambda(p)=-1\).
- `lambda_two_mul`: \(\forall m,\ 0<m\to\lambda(2m)=-\lambda(m)\).
- `lambda_square`: \(\forall t,\ 0<t\to\lambda(t^2)=1\).

### Representation declarations

- `target_iff_forall_hasRepresentation`: \(\mathrm{Target}\iff\forall N,\ \operatorname{Even}(N)\to2<N\to H(N)\).
- `hasSignedRepresentation_mul`: \(\forall s\in\mathbb Z\,\forall N\,\forall d,\ 0<d\to H_s(N)\to H_{\lambda(d)s}(dN)\). There is no separate \(s=\pm1\) premise.
- `representation_scaled_sign`: \(\forall u\,\forall v\,\forall m\,\forall s\in\mathbb Z,\ 0<u\to0<v\to0<m\to(s=1\lor s=-1)\to\lambda(u)=s\to\lambda(v)=s\to\lambda(m)=-s\to H(m(u+v))\).
- `representation_double`: \(\forall m,\ 0<m\to\lambda(m)=-1\to H(2m)\).
- `representation_diagonal`: \(\forall N,\ \operatorname{Even}(N)\to2<N\to\lambda(N)=1\to H(N)\).
- `representation_two_sign_seed`: \(\forall d,\ H_{-1}(d)\to H_1(d)\to\forall m,\ 0<m\to H(dm)\). The two seed premises precede the quantifier over \(m\).
- `eight_two_sign_seed`: \(H_{-1}(8)\land H_1(8)\), with separate existential pairs in the two conjuncts.
- `representation_multiple_eight`: \(\forall m,\ 0<m\to H(8m)\).

Each conclusion \(H_s(K)\) introduces a fresh \(a\), then \(b\), after the displayed outer parameters and premises. These witnesses can vary with those parameters. Existentials inside premises have their own scopes. In particular, the two seed representations are not required to use the same pair, and the resulting representation can vary with \(m\). None of these types prescribes the actual output summands: even `representation_diagonal` and `representation_double` conclude only existence, not an equation saying the two summands are equal.

### Interval declarations

- `mem_I_iff`: \(\forall N\,\forall a,\ a\in I_N\iff0<a\land a<N\).
- `interval_eq_Icc`: \(\forall N,\ 2\le N\to I_N=\{a\in\mathbb N:1\le a\le N-1\}\).
- `interval_card_cast`: \(\forall N,\ 2\le N\to(|I_N|:\mathbb Z)=(N:\mathbb Z)-1\).
- `reflection_bijection`: \(\forall N,\ 2\le N\to[a\mapsto N-a\text{ is a bijection from }I_N\text{ to }I_N]\).
- `sum_lambda_interval`: \(\forall N,\ 2\le N\to\sum_{a\in I_N}\lambda(a)=L(N-1)\).
- `sum_lambda_reflection`: \(\forall N,\ 2\le N\to\sum_{a\in I_N}\lambda(N-a)=L(N-1)\).

The next three statements each have the exact prefix \(\forall N\,\forall a,\ 2\le N\to a\in I_N\to\):

- `interval_bounds`: \(0<a\land a<N\land0<N-a\land N-a<N\).
- `reflection_mem`: \(N-a\in I_N\).
- `reflection_involutive`: \(N-(N-a)=a\).

### Counting declarations

- `mem_orderedRepresentations`: \(\forall N\,\forall a\,\forall b,\ (a,b)\in O_N\iff0<a\land0<b\land N=a+b\land\lambda(a)=-1\land\lambda(b)=-1\).
- `two_sign_indicator`: \(\forall a\,\forall b,\ 0<a\to0<b\to 4\mathbf1_{\{\lambda(a)=-1\land\lambda(b)=-1\}}=(1-\lambda(a))(1-\lambda(b))\). The indicator and arithmetic are integer-valued.

Each of the following has the exact prefix \(\forall N,\ 2\le N\to\); none adds an evenness premise:

- `orderedRepresentations_eq_image`: \(O_N=\{(a,N-a):a\in J_N\}\), as a finite-set image.
- `representation_count_eq_card_indices`: \(R(N)=|J_N|\).
- `representation_count_eq_indicator_sum`: \((R(N):\mathbb Z)=\sum_{a\in I_N}\mathbf1_{\{\lambda(a)=-1\land\lambda(N-a)=-1\}}\).
- `four_mul_representation_count`: \(4(R(N):\mathbb Z)=((N:\mathbb Z)-1)-2L(N-1)+C(N)\).
- `representation_count_pos_iff`: \(0<R(N)\iff H(N)\).
- `count_pos_iff_keystone`: \(0<R(N)\iff2L(N-1)-((N:\mathbb Z)-1)<C(N)\).
- `keystone_ge_four_iff`: \(0<R(N)\iff4\le((N:\mathbb Z)-1)-2L(N-1)+C(N)\).

The closed equivalences are:

- `target_iff_count_pos`: \(\mathrm{Target}\iff\forall N,\ \operatorname{Even}(N)\to2<N\to0<R(N)\).
- `target_iff_pointwise_keystone`: \(\mathrm{Target}\iff\forall N,\ \operatorname{Even}(N)\to2<N\to2L(N-1)-((N:\mathbb Z)-1)<C(N)\).

The quantifiers inside each side of an equivalence retain their own scopes. These are not assertions about an average over \(N\).

### Prime-factor declarations and final declarations

- `exists_prime_pair_factor_of_lambda_one` has the exact order
  \[
  \forall m,\ 1<m\to\lambda(m)=1\to
  \exists p\,\exists q\,\exists d,\quad
  \operatorname{Prime}(p)\land\operatorname{Prime}(q)\land0<d\land\lambda(d)=1\land m=d(pq).
  \]
  Here \(p\) may depend on \(m\); \(q\) may additionally depend on \(p\); \(d\) may additionally depend on \(q\). All three witnesses are natural numbers. Neither \(p\ne q\) nor \(d>1\) nor coprimality is required.
- `target_iff_prime_product_core`:
  \[
  \mathrm{Target}\iff\forall p\,\forall q,\
  \operatorname{Prime}(p)\to\operatorname{Prime}(q)\to H((2p)q).
  \]
  The concluding summands may depend on both primes; equal primes are allowed. This does not require the summands themselves to be prime.
- `pointwise_keystone`: \(\forall N,\ \operatorname{Even}(N)\to2<N\to2L(N-1)-((N:\mathbb Z)-1)<C(N)\).
- `liouville_goldbach`: the closed proposition `Target`, expanded above.

## 3. Pointwise versus aggregate bounds

- Positivity, sign equalities, interval membership, and bounds on individual summands are pointwise restrictions.
- \(L(x)\) is a finite aggregate over \(1\le a\le x\). \(C(N)\) is a finite aggregate over \(1\le a<N\), pairing \(a\) with \(N-a\). \(R(N)\) aggregates ordered representations of one fixed \(N\).
- Despite involving aggregate quantities, the final inequality is required **separately for every even \(N>2\)**. There is no averaging over \(N\), density qualification, exceptional set, or sufficiently-large threshold.
- The lower bound on \(C(N)\) is strict and one-sided. There is no absolute value, separate upper bound on \(L\), or assertion that \(C(N)>0\).
- The counting identities are exact identities. The positivity conclusion is merely \(R(N)>0\), equivalently at least one ordered representation, not a lower bound proportional to \(N\).
- The threshold 4 in `keystone_ge_four_iff` bounds the integer expression equal to \(4R(N)\). It does not assert that there are at least four representations.

## 4. Constants, domains, and restrictions

There are no existentially chosen numerical constants, error parameters, or unspecified thresholds. All numerical constants in the interfaces are fixed.

- **0:** empty-list length; lower endpoint in strict positivity hypotheses; the false indicator value; the comparison in \(R(N)>0\). Natural-number variables also have their intrinsic nonnegative domain.
- **1 and −1:** the two signs; −1 is the base in \(\lambda\) and the required representation sign. The summation intervals start at 1. The formulas use \(N-1\), \(1-\lambda\), and the indicator value 1. The factorization lemma requires \(1<m\).
- **2:** final cutoff \(2<N\); interval/counting cutoff \(2\le N\); the multipliers in \(2m\), \((2p)q\), and \(2L\); the square exponent. Prime parameters satisfy \(p,q\ge2\). In the dependencies, 2 is the even-factor test and the auxiliary search increment.
- **3:** the fixed evaluation \(\lambda(3)=-1\) and the starting argument of the odd-factor search.
- **4:** the fixed evaluation \(\lambda(4)=1\), the indicator/count coefficient, and the lower bound in `keystone_ge_four_iff`.
- **5:** the fixed evaluation \(\lambda(5)=-1\).
- **8:** the fixed two-sign seed and the multiplier in `representation_multiple_eight`.

Variable restrictions, in addition to the exact premises listed in Section 2:

- Definitions of \(\omega,\lambda,I,J,O,R,L,C,H_s,H\) accept all natural arguments, including zero. \(s\) in \(H_s\) ranges over all integers.
- Final \(N\) is even and strictly greater than 2, so its admissible values begin at 4. The interval/counting results explicitly guarded by \(2\le N\) also apply to odd \(N\).
- Representation witnesses satisfy \(a,b>0\) and \(a+b=N\); hence each is less than \(N\). For sign −1, neither can equal 1. No order such as \(a\le b\), distinctness, primality, or coprimality is imposed.
- Multiplicativity/scaling variables have exactly the displayed positive-input guards. `representation_scaled_sign` additionally restricts \(s\) to 1 or −1 and prescribes three sign equalities. `hasSignedRepresentation_mul` does not separately restrict \(s\).
- The factorization lemma requires \(m>1\), \(\lambda(m)=1\), prime \(p,q\), and positive \(d\) with \(\lambda(d)=1\), together with \(m=d(pq)\). The value \(d=1\) and the equality \(p=q\) are allowed. There are no additional explicit upper bounds on these factors.
- No upper bound on the outer parameters appears. Bounds on interval elements and constraints from the displayed sum/product equations are not replaced by any hidden size condition.

## 5. Vacuity, empty-object, and trivial-witness risks

1. **The final domain is nonempty.** Its implications impose no obligation at \(N\le2\) or odd \(N\), but do impose obligations at every even \(N\ge4\). `liouville_goldbach` has no extra antecedent assuming `Target` or the keystone inequality.
2. **Empty intervals and zero conventions are real but excluded from the guarded counting identities.** \(I_0=I_1=\varnothing\), so \(J_N,O_N\) are empty and \(R(N)=C(N)=0\) for \(N=0,1\). Also \(L(0)=0\). The convention \(\lambda(0)=1\) cannot supply a representation witness because the witnesses must be positive.
3. **Some signed-representation premises can be unsatisfiable.** Positive witnesses force their common sign to be 1 or −1. Thus \(H_s(N)\) is impossible for other integer \(s\), making implications with that premise vacuous there. No positive two-summand representation exists for \(N<2\); with sign −1, neither summand can be 1, so \(H(N)\) is impossible for \(N<4\). The final cutoff avoids these cases.
4. **Separate seed witnesses matter.** \(H_{-1}(d)\land H_1(d)\) is not a requirement that one pair have both signs. The two existentials are independent. The type of `representation_two_sign_seed` contains no explicit lower bound on \(d\), but its premises already constrain it.
5. **Small or repeated witnesses are allowed where stated.** Equal summands, repeated primes, and \(d=1\) are not ruled out. They do not automatically discharge the sign and sum/product equations. Conversely, theorem names mentioning doubling, diagonals, or scaling do not add witness equations absent from the types.
6. **Natural subtraction is truncated outside its valid range.** Within \(I_N\), the stated bounds ensure \(0<N-a<N\). The guarded formulas use \(N\ge2\), so there is no endpoint truncation ambiguity there. The unguarded definitions still use natural subtraction literally.
7. **Ordered counting and multiplicity are substantive.** Replacing \(R\) by an unordered-pair count, or replacing \(\omega\) by the number of distinct prime factors, would change the literal statements.
8. **No proof validity follows from these extracts.** The supplied theorem entries show signatures without proof bodies. This readback cannot determine their axiom dependencies or certify their proofs.

## 6. Verdict

**READBACK-CLEAN — literal statement audit only.** The final type is the unconditional universal existence assertion for every even \(N>2\), with positive, possibly equal summands of sign −1 under the multiplicity-counting definition of \(\lambda\). The separate keystone declaration is a strict pointwise inequality for the same range, not an aggregate-in-\(N\) substitute. No empty final domain or additional vacuity-inducing premise appears in that endpoint type.

The exact code-based scope caveats are the multiplicity convention, ordered counting, independently scoped seed witnesses, and absence of distinctness or prescribed witness formulas. This label does not certify correspondence to an unseen source, or correctness of any proof.
