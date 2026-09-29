# Literal readback

## 1. Literal assertion

`ArithmeticStatement.Target` is a defined proposition, not a supplied proof or theorem establishing that proposition.

Let
\[
\omega(n)=\operatorname{length}(\texttt{Nat.primeFactorsList}(n)),
\qquad \lambda(n)=(-1)^{\omega(n)}\in\mathbb Z.
\]
The factor list counts prime factors **with multiplicity**, not distinct prime divisors. Its values at both 0 and 1 are the empty list, so \(\omega(0)=\omega(1)=0\) and \(\lambda(0)=\lambda(1)=1\).

The assertion is: **For every even natural number \(N>2\), there exist positive natural numbers \(a,b\) such that \(N=a+b\), \(\lambda(a)=-1\), and \(\lambda(b)=-1\).** Equivalently, each summand separately has an odd total number of prime factors counted with multiplicity. Neither summand is required to be prime.

## 2. Quantifier order and witness dependencies

Expanding `Even`, the assertion is exactly
\[
\forall N\in\mathbb N,\quad
(\exists r\in\mathbb N,\ N=r+r)\ \longrightarrow\
2<N\ \longrightarrow\
\exists a\in\mathbb N,\ \exists b\in\mathbb N,\quad
0<a\ \land\ 0<b\ \land\ N=a+b\ \land\
(-1)^{\omega(a)}=-1\ \land\ (-1)^{\omega(b)}=-1,
\]
where the powers and their asserted values lie in \(\mathbb Z\).

The outer order is: universally quantified \(N\); the evenness hypothesis; the strict lower-bound hypothesis; existential \(a\); existential \(b\). The witnesses are chosen separately for each admissible \(N\), under both hypothesis binders; \(b\) is also under the binder for \(a\). There is no single pair required to work for every \(N\), and no universal assertion about all decompositions of \(N\).

The existential \(r\) is local to the evenness antecedent. It is not an outer existential witness chosen jointly with \(a,b\).

## 3. Pointwise versus aggregate conditions

- **Pointwise:** \(a>0\), \(b>0\), \(\lambda(a)=-1\), and \(\lambda(b)=-1\), each separately.
- **On the total/input:** \(N\) is even and \(N>2\).
- **Aggregate relation:** the exact equality \(a+b=N\).

There is no averaged sign condition, bound on a sum of signs, density assertion, or asymptotic estimate. No explicit upper bound on either summand is written. The conditions entail \(2\le a,b\le N-2\); these are consequences, not additional clauses. No ordering between \(a,b\) is imposed.

## 4. Constants, quantification, and restrictions

- \(N\): universal natural number, restricted by evenness and \(N>2\), hence admissible values start at 4; no upper bound.
- \(a,b\): existential natural numbers with the individual and joint restrictions above; no distinctness requirement.
- \(r\): existential natural number inside `Even N`, satisfying \(N=r+r\). No separate inequality is written for it; with the other premise it is at least 2 and is determined by \(N\).
- `omega` and `lambda`: fixed defined functions, not independently quantified choices. `omega` is natural-valued; `lambda` is integer-valued and takes only \(1\) or \(-1\).
- All numeric constants are fixed literals, not adjustable parameters: natural-number 0 for positivity and empty-list length, 1 in the factor-list base cases and length increment, 2 for the strict input threshold and factorization operations, and 3 as the initial odd trial divisor in `minFacAux`. The factorization tests divisibility by 2 first and advances odd trial divisors by 2. Integer \(-1\) is both the power base and the required sign.

There are no existential error constants, unspecified thresholds, or hidden asymptotic parameters in `Target`. Local recursion and trial-divisor variables in helper definitions are not additional parameters of the proposition.

## 5. Vacuity and trivial-witness checks

- For odd \(N\), or for \(N\le2\), the implication is vacuous. The joint premises are not unsatisfiable: \(N=4\) satisfies them.
- Zero summands are explicitly excluded. Both 0 and 1 also fail the required sign, since their empty factor lists give \(\lambda=1\). Thus empty factor lists do not provide witnesses.
- Equal summands are allowed; \(N=4\) admits \(a=b=2\). This is not a pair that works for every admissible input.
- Positivity and the sum equality alone do not discharge the two sign requirements. No syntactic trivial-witness collapse is apparent.

## 6. Verdict

**READBACK-CLEAN.** No code-based vacuity or quantifier defect is apparent in the literal assertion above. The material distinctions are multiplicity-counted factors, separate sign requirements on both positive summands, and a definition of a proposition rather than a supplied proof. This label does not certify truth, successful elaboration, or correspondence to an unseen source.
