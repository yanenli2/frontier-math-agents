# Liouville–Goldbach: the integrated partial argument

**Mode: PROGRESS_NOTES. Status: PARTIAL — the original Target remains UNRESOLVED.**

The development proves the diagonal sign family, every positive multiple of eight, an exact ordered counting identity, and two equivalences that isolate the missing universal assertion. It does **not** prove that assertion. Successful checking of the partial Lean module is not a proof of `Target`.

Here `P` denotes `.clawcodex/math-team/problems/liouville-goldbach-jul2026`. Paths below are relative to `P`. The mathematical exposition follows `nl/generator/proof-v2.md` and the actual integrated `lean/Statement/Partial.lean`; their exact identities are recorded in §11. References of the form `Partial:268–289` mean lines in that integrated file, not a proposed interface. All its declaration names below have namespace `ArithmeticStatement`.

## 1. The unchanged problem and conventions

For a positive integer n, let Ω(n) count its prime factors **with multiplicity**, with Ω(1)=0, and put

\[
\lambda(n)=(-1)^{\Omega(n)}\in\mathbb Z.
\]

The requested statement is: **for every even integer N>2, there exist positive integers a,b such that N=a+b and λ(a)=λ(b)=−1.** Equality a=b is allowed. Neither witness is required to be prime, odd, coprime to the other, or distinct from it.

The protected natural-number formulation is exactly:

```lean
def omega (n : ℕ) : ℕ := n.primeFactorsList.length

def lambda (n : ℕ) : ℤ := (-1 : ℤ) ^ omega n

def Target : Prop :=
  ∀ N : ℕ, Even N → 2 < N →
    ∃ a b : ℕ,
      0 < a ∧ 0 < b ∧ N = a + b ∧
        lambda a = (-1 : ℤ) ∧ lambda b = (-1 : ℤ)
```

This is `lean/Statement/Definitions.lean:6–14`. Natural representatives of positive integers preserve the relevant arithmetic and positive prime factorization, so this is the positive-natural normalization of the request, not an extra restriction on admissible N or witnesses. No separate Lean integer/natural transport theorem is claimed in this module. No argument below uses λ(0). [Sources: `request.md:5–14`; `proof-v2.md` §0.1; integration report:278–297.]

For an integer sign s, write

\[
P_s(n):\Longleftrightarrow
\exists a,b\in\mathbb N,\quad
0<a,\ 0<b,\ n=a+b,\ \lambda(a)=s,\ \lambda(b)=s,
\qquad G(n):=P_{-1}(n).
\]

These are `HasSignedRepresentation` and `HasRepresentation` (`Partial:14–20`). Thus `Target` is definitionally equivalent to `∀ N : ℕ, Even N → 2 < N → HasRepresentation N` (`target_iff_forall_hasRepresentation`, 98–100).

## 2. Sign arithmetic and complete multiplicativity

The foundational external mathematical input is the pinned Mathlib factor-list module, not a paper about the additive problem:

> Leonardo de Moura, Jeremy Avigad and Mario Carneiro, *Prime numbers*, `Mathlib.Data.Nat.Factors`, commit `905b95818eb32af7874a58b427f50c1711a5e96c`. Immutable source: <https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Data/Nat/Factors.lean>.

The local file supplies the following exact facts:

- `Nat.primeFactorsList_one` (49–50): the factor list of 1 is empty.
- `Nat.prime_of_mem_primeFactorsList` (55–65): every listed entry is prime.
- `Nat.prod_primeFactorsList` (70–81): for n≠0, the product of the list is n.
- `Nat.primeFactorsList_prime` (83–88): a prime p has factor list `[p]`.
- `Nat.perm_primeFactorsList_mul` (196–202): for u≠0 and v≠0, the list for uv is a permutation of the concatenation of the lists for u and v. Its derivation uses factorization uniqueness (`Nat.primeFactorsList_unique`, 167–179).

Crucially, the last fact has **no coprimality hypothesis**: repeated occurrences of the same prime remain repeated entries. The integration record binds this Mathlib revision to a public exact-SHA witness dated 2026-07-28, before the inclusive 2026-07-31 cutoff (§10 below).

For a natural exponent k, writing k as 2r or 2r+1 gives `(-1)^(2r)=1` and `(-1)^(2r+1)=-1`. Hence, for every positive n, λ(n) is either 1 or −1, and λ(n)²=1. The empty factor list gives Ω(1)=0 and λ(1)=1.

For u,v>0, taking lengths in the factor-list permutation gives

\[
\Omega(uv)=\Omega(u)+\Omega(v).
\]

The exponent rule then yields the complete multiplicativity statement

\[
\lambda(uv)=(-1)^{\Omega(u)+\Omega(v)}
             =\lambda(u)\lambda(v).
\]

For a prime p the singleton list gives λ(p)=−1. Consequently, for positive t and m,

\[
\lambda(t^2)=1,\qquad \lambda(2m)=-\lambda(m),
\qquad \lambda(2)=\lambda(3)=\lambda(5)=-1,\quad \lambda(4)=1.
\]

All later multiplicative uses have positive factors. These deductions are the local proofs in `proof-v2.md` §1 and the theorems `omega_one` through `lambda_square` (`Partial:43–96`); no analytic theorem or additive conjecture is involved.

## 3. Explicit unconditional families

### Scaling and the diagonal family

If d>0 and a,b witness P_s(n), then da,db are positive and sum to dn. Complete multiplicativity gives the exact sign rule

\[
P_s(n)\ \Longrightarrow\ P_{\lambda(d)s}(dn).
\]

In particular, if s∈{1,−1} and λ(d)=−s, the resulting two signs are both −1. The same multiplier acts on both witnesses. This is `hasSignedRepresentation_mul` and `representation_scaled_sign` (`Partial:102–122`).

The direct diagonal lemma is

\[
m>0,\quad\lambda(m)=-1\quad\Longrightarrow\quad G(2m),
\]

with witnesses (m,m). Now suppose N is even, N>2 and λ(N)=1. Write N=2m; then m>1 and `1=λ(2m)=−λ(m)`. Thus λ(m)=−1, so the diagonal works. These are `representation_double` and `representation_diagonal` (`Partial:124–137`). The assumption λ(N)=1 is part of this partial family, not part of `Target`.

### Every positive multiple of eight

A number d with both a negative-sign seed P₋₁(d) and a positive-sign seed P₁(d) satisfies G(dm) for every m>0: use the negative seed when λ(m)=1, and the positive seed when λ(m)=−1. These two cases exhaust the possible multiplier signs.

At d=8 the seeds are

\[
8=3+5\quad(-1,-1),\qquad 8=4+4\quad(1,1).
\]

Thus the witnesses at 8m can be written explicitly:

| Multiplier sign | Witnesses | Their Liouville values |
|---|---|---|
| λ(m)=1 | (3m,5m) | (−1,−1) |
| λ(m)=−1 | (4m,4m) | (−1,−1) |

Both pairs are positive and sum to 8m. Since m≥1, this N is even and at least 8. The unrestricted quantifier here is **every m>0**, but the represented numbers still form only the family N=8m. [Sources: `proof-v2.md` §2; `representation_two_sign_seed`, `eight_two_sign_seed`, `representation_multiple_eight`, `Partial:139–159`.]

## 4. Exact ordered counting, reflection, and positivity

### Definitions and the ordered-pair bridge

Let

\[
I_N=\{a\in\mathbb N:0<a<N\},\qquad
F_N=\{a\in I_N:\lambda(a)=\lambda(N-a)=-1\}.
\]

The **actual integrated definition** of R counts ordered pairs:

\[
Q_N=\{(a,b)\in I_N\times I_N:
       N=a+b,\ \lambda(a)=\lambda(b)=-1\},\qquad R(N)=|Q_N|\in\mathbb N.
\]

Also set

\[
L(x)=\sum_{1\le a\le x}\lambda(a)\in\mathbb Z,
\qquad
C(N)=\sum_{a\in I_N}\lambda(a)\lambda(N-a)\in\mathbb Z.
\]

These are `I`, `representationIndices`, `orderedRepresentations`, `R`, `L`, and `C` (`Partial:22–41`). The prose source defines its count first as |F_N|; the integrated code starts with |Q_N| and **proves their equality**, rather than silently identifying the two definitions.

Throughout the counting argument assume **N≥2**; evenness is not needed. Then I_N is exactly `{1,…,N−1}`, its cardinality is N−1, and

\[
(|I_N|:\mathbb Z)=(N:\mathbb Z)-1.
\]

For a∈I_N, the natural difference b=N−a satisfies 0<b<N, a+b=N and N−b=a. Therefore reflection ρ(a)=N−a maps I_N to itself and is its own inverse. In particular,

\[
\sum_{a\in I_N}\lambda(N-a)
 =\sum_{a\in I_N}\lambda(a)=L(N-1).
\]

This supplies both positivity of every Liouville argument and the reflected-sum bridge (`Partial:161–213`).

The map `a ↦ (a,N−a)` sends F_N to Q_N. Conversely, a positive pair with N=a+b has a<N and b=N−a, so its first coordinate belongs to F_N. These maps are inverse. The formal image equality and injectivity of the first coordinate give

\[
R(N)=|F_N|.
\]

If a≠b, the orders (a,b) and (b,a) are counted separately; a diagonal pair is counted once. There is no division by two. Moreover, positivity and the sum equation imply that both coordinates are below N, so the interval restriction in Q_N excludes no pair from the original target. [Sources: `proof-v2.md` C02–C04; `mem_orderedRepresentations`, `orderedRepresentations_eq_image`, `representation_count_eq_card_indices`, `Partial:215–250`.]

### Indicator expansion

For positive a,b, let δ(a,b) be the integer 1 when both Liouville values are −1, and 0 otherwise. The four possible sign pairs give

\[
4\delta(a,b)=(1-\lambda(a))(1-\lambda(b)).
\]

When both signs are −1 the right side is 4; otherwise one factor is zero. Summing this indicator over I_N and using the count bridge yields

\[
\begin{aligned}
4(R(N):\mathbb Z)
 &=\sum_{a\in I_N}(1-\lambda(a))(1-\lambda(N-a))\\
 &=|I_N|-\sum_{a\in I_N}\lambda(a)
          -\sum_{a\in I_N}\lambda(N-a)
          +\sum_{a\in I_N}\lambda(a)\lambda(N-a)\\
 &=\boxed{\ ((N:\mathbb Z)-1)-2L(N-1)+C(N)\ }.
\end{aligned}
\]

The cardinality in the middle line is understood as its integer cast. All displayed arithmetic on sums and signs is in ℤ. In contrast, `N−a` in λ and `N−1` as the argument of L are natural indices; their bounds have already been justified. The result involves no signed division or truncated subtraction. It is `four_mul_representation_count` (`Partial:268–289`), supported by `two_sign_indicator` and `representation_count_eq_indicator_sum` (252–266). Its sole N-hypothesis is N≥2. [Prose source: C05–C07.]

### The strict inequality that is still missing

A finite set has positive cardinality exactly when it has an element. Applied to Q_N, this gives

\[
0<R(N)\quad\Longleftrightarrow\quad G(N).
\]

Write K(N) for the integer right side of the boxed identity; K is notation here, not an additional Lean definition. Since K(N)=4(R(N):ℤ), for N≥2 we have

\[
\begin{aligned}
G(N)
&\Longleftrightarrow R(N)>0
\Longleftrightarrow K(N)>0
\Longleftrightarrow K(N)\ge4\\
&\Longleftrightarrow
 2L(N-1)-((N:\mathbb Z)-1)<C(N).
\end{aligned}
\]

Indeed the integer count is nonnegative, and a positive count is at least 1; multiplying by 4 gives the exact margin 4. Rearranging K(N)>0 gives the displayed strict bound. The weaker conclusion K(N)≥0 is automatic and is insufficient for existence.

Thus the counting route is an **equivalence**, not a positivity proof:

\[
\mathrm{Target}\ \Longleftrightarrow\
\forall N\in\mathbb N,\quad
\operatorname{Even}(N)\ \Longrightarrow\ 2<N\ \Longrightarrow\
2L(N-1)-((N:\mathbb Z)-1)<C(N).
\]

[Sources: `proof-v2.md` C08–C09 and A01; `representation_count_pos_iff`, `count_pos_iff_keystone`, `keystone_ge_four_iff`, `target_iff_count_pos`, `target_iff_pointwise_keystone`, `Partial:291–327`.]

## 5. Exact reduction to all prime-product cores

Define the still-unproved universal assertion

\[
\mathrm{Core}:\quad
\forall p,q\in\mathbb N,\quad
\operatorname{Prime}(p)\ \Longrightarrow\ \operatorname{Prime}(q)
\ \Longrightarrow\ G(2pq).
\]

**Both equal primes p=q and the prime 2 are included.** The proved statement is `Target ↔ Core`.

First, if m>1 and λ(m)=1, its prime-factor list cannot be empty, since its product is m. It also cannot be a singleton, which would make λ(m)=−1. Hence the actual list has the form `p :: q :: t`. Its first two entries p,q are primes; they are two occurrences, not necessarily distinct values. Let d be the product of the tail. The product identity gives

\[
m=d(pq),\qquad d>0.
\]

The tail can be empty, giving **d=1**. Complete multiplicativity now shows

\[
1=\lambda(m)=\lambda(d)\lambda(p)\lambda(q)
            =\lambda(d)(-1)(-1)=\lambda(d).
\]

This is `exists_prime_pair_factor_of_lambda_one` (`Partial:329–360`), whose exact conclusion includes both d>0 and λ(d)=1.

For the forward implication, fix any primes p,q. They are at least 2, so 2pq≥8>2 and 2pq is even. `Target` therefore gives G(2pq).

Conversely, assume Core for this implication and take an arbitrary even N>2. Write N=2m, so m>1. If λ(m)=−1, use (m,m). If λ(m)=1, the factor selection gives m=d(pq) with d>0 and λ(d)=1. Core supplies positive negative-sign witnesses a,b for 2pq. Scaling both by d preserves their negative signs and gives total

\[
d(2pq)=2m=N.
\]

The sign dichotomy exhausts the cases. This proves the converse and hence `target_iff_prime_product_core` (`Partial:362–386`; `proof-v2.md` PC00–PC01). Core is used only as a hypothesis of the converse; it has not been supplied as a theorem, and no finite set of prime pairs replaces its universal quantifiers.

## 6. Exact unresolved Lean obligations

One sufficient—and, by §4, equivalent—remaining obligation is the following goal for **every** admissible N:

```text
N : ℕ
hEven : Even N
hN : 2 < N
⊢ 2 * ArithmeticStatement.L (N - 1) - ((N : ℤ) - 1) <
    ArithmeticStatement.C N
```

Alternatively, by §5 the exact unresolved type is:

```lean
∀ p q : ℕ, Nat.Prime p → Nat.Prime q →
  ArithmeticStatement.HasRepresentation (2 * p * q)
```

Either universal proof would yield the final missing type `ArithmeticStatement.Target`. These are **goals, not assumptions or theorem declarations in the integrated module**. The planned names `ArithmeticStatement.pointwise_keystone` and `ArithmeticStatement.liouville_goldbach` are absent from the built environment; the signature-only endpoint lines in `formal/blueprinter/interfaces-v1.lean:191–195` are not imported proof evidence.

There is no proved uniform strict bound, no uniform prime-core construction, and no effective large-N threshold together with complete finite remainder coverage in this delivery. The identity, the two equivalences, and the explicit partial families do not supply any of these missing steps. [Evidence: integration report:278–297; `REPRODUCE.md:159–178`; endpoint-absence output cited in §10.]

## 7. Rejected and exploratory routes outside the integrated proof

This section records the boundary of `proof-v2.md` §5. Its additional route arguments are **prose-only**, not further theorems in `Partial.lean`. Their proposed universal premises remain unproved. Additional finite-seed covers and shift templates are exploratory; the particular all-multiples-of-eight construction in §3 is separate and already implemented.

### The positive prime bridge and the rejected O-M5 condition

The proposed bridge is

\[
\mathrm{PB}:\quad
\forall q\in\mathbb N,\quad \operatorname{Prime}(q)
\ \Longrightarrow\ 5\le q\ \Longrightarrow\ P_1(2q).
\]

The prose gives the conditional implication PB ⇒ Core: when one of p,q is at least 5, scale the corresponding positive-sign pair by the other prime, whose sign is −1. When both primes are below 5, they are 2 or 3; the remaining cores 8,12,18 have negative pairs (3,5), (5,7), (5,13). The small primality checks are supplied in v2 E01.2. This implication is not a proof of PB. In particular PB is not `Target` evaluated at 2q: the latter has the negative diagonal (q,q), whereas PB asks for two **positive** signs.

For positive q, an even-even positive-sign pair at 2q exists exactly when G(q): doubling two negative summands reverses both signs, and halving a positive even-even pair reverses the argument. Thus G(q) for every prime q≥5 would suffice for PB, but this is an odd-target assertion not furnished by `Target`'s even-N quantifier.

The local counting attempt in v2 is precise. If q≥2 and G(q) fails, reflection on I_q injects the negative-sign indices into the positive-sign indices: a reflected negative sign would otherwise produce a forbidden pair. If A and B are those two sets, respectively, then |A|≤|B| and

\[
L(q-1)=(|B|:\mathbb Z)-(|A|:\mathbb Z)\ge0.
\]

Consequently the **pointwise** condition L(q−1)<0 would imply G(q). But the optional universal assertion O-M5,

\[
\text{“for every prime }q\ge5,\quad L(q-1)<0\text{,”}
\]

is **false**, with the counterexample already proved in v2 PB01:

\[
q=5,\qquad L(4)=\lambda(1)+\lambda(2)+\lambda(3)+\lambda(4)
              =1-1-1+1=0.
\]

Here q is prime and meets q≥5. This rejects the unchanged strict-negative-partial-sum route, not PB or `Target`; indeed 5=2+3 already has two negative signs. No repaired threshold or replacement universal inequality is asserted.

### Finite tests and the shift bridge

V2 PB02 tries the three PB pairs `(1,2q−1)`, `(4,2(q−2))`, and `(6,2(q−3))`. They do not cover all primes. Its exact q=59 example has

\[
57=3\cdot19,\quad 56=2^3\cdot7,\quad117=3^2\cdot13,
\]

so λ(q−2)=λ(q−3)=1 and λ(2q−1)=−1. Every candidate then has signs (+1,−1). Nevertheless `118=14+104`, with `14=2·7` and `104=2³·13`, is positive-positive. These are the local factorization and primality checks in v2, not a uniform construction. Multiplicativity alone supplies no value of λ at a sum or at an unfactored polynomial in q, so the proposed product-parity continuation has no established contradiction.

The separate shift proposal is exactly

\[
\mathrm{LS}:\quad
\forall m\in\mathbb N,\quad
1<m\ \Longrightarrow\ \lambda(m)=1\ \Longrightarrow\
\exists t\in\mathbb N,\quad
0<t<m,\ \lambda(t)=1,\quad
[\lambda(m-t)=1\ \lor\ \lambda(m+t)=-1].
\]

V2 LS01 gives a conditional route to `Target`: at N=2m use the diagonal if λ(m)=−1; otherwise LS would give either the negative pair `(2t,2(m−t))`, or, when λ(m−t)≠1, the pair `(m−t,m+t)`. The bounds on t ensure positivity. There is no proof of the uniformly quantified LS premise, and no claimed equivalence between LS and `Target`.

## 8. Eligible literature context, not a proof dependency

The only mathematical paper used for context here is Alexander P. Mangerel, *On a Goldbach-type problem for the Liouville function*, **arXiv:2404.12117v2**, 2 May 2024, <https://arxiv.org/abs/2404.12117v2>, <https://arxiv.org/pdf/2404.12117v2>. The local PDF is `knowledge/mangerel-v2/paper.pdf`. Its first-page version/date and printed pages 1–3 were inspected directly for this exposition, against `nl/searcher/extraction-v2.md`. The preserved metadata gives v2 availability as 2024-05-02 14:48:54 UTC. The extraction is explicitly literature context, not a project proof or a Lean import.

The paper denotes our C(N), **not our summatory L**, by `𝓛_λ(N)`. Its page 1 states:

> **Theorem 1.2.** There exists \(N_0\in\mathbb N\) such that if \(N\ge N_0\) then \(|\mathcal L_\lambda(N)|<N-1\).

This is an eventual statement for every integer above its threshold, without an evenness restriction; it is not an almost-all assertion. Its conclusion is non-extremality of the correlation, not a negative-negative representation. **Remark 1**, page 2, attributes reliance to Siegel's theorem and explicitly says:

> “Thus, the lower bound \(N_0\) is ineffective.”

By contrast, **Remark 2**, page 3, asks the target as a question:

> “One may also ask another natural Goldbach-type problem regarding the Liouville function: given an even integer \(N\ge4\), must there exist \(1\le a,b\le N\) with \(a+b=N\), such that \(\lambda(a)=\lambda(b)=-1\)?”

It then says:

> “The methods of this paper appear to be far too rigid to address this problem directly.”

For even integers, N≥4 is N>2, and positive summands of N are automatically below N. Thus this question has the target's scope, but it is **not Theorem 1.2's conclusion**. A positive product λ(a)λ(N−a) can come from two positive signs; correlation non-extremality by itself does not isolate the negative-negative pairs counted by R.

Remark 2 proposes the stronger estimate `|C(N)|<N−g(N)`, with g increasing “sufficiently quickly” and g(x)=o(x), as a hypothetical route. That estimate is not proved there. Its conditional zero identity agrees with §4 when R(N)=0. The subsequent PNT-based display, however, prints `|C(N)|>N−2|L(N−1)|`, although the preceding exact identity has N−1. The extraction flags this apparent off-by-one/strictness mismatch. **No repair of that display, quantitative PNT inequality, constant choice, or sufficient-rate theorem is adopted here.** The source's analytic dependencies are not imported into the partial proof.

These observations describe this specific May 2024 version only. They make **no global claim that the target was open at the July 2026 cutoff**, and no claim that other eligible literature contains no further result.

The existing exclusion record is retained: `sources.md:27–28` reports an automatically returned MathOverflow snippet with footer `rev 2026.9.15.45626`, despite a `before:2026-08-01` filter. The result was not opened or used, and its mathematical assertions are excluded. This exposition undertook no source browsing and relies on none of that snippet's content.

## 9. Separate finite, non-Lean computational evidence

`nl/code-executor/report.md`, with `finite_certify.py`, `evidence.json`, `run.log`, and `run.json`, records an exact CPython 3.9.6 audit: 1,260 assertions, zero failed assertions or exceptions, and parent and worker exits 0. It is **finite program evidence, not Lean verification or a universal proof**, and it was not rerun for this exposition.

Its stated scope includes all 255 counting-identity instances N=2,…,256, using actual ordered-pair counts, with no symmetry reduction. For example at N=10 it records L(9)=−1, C(10)=9, R(10)=5, counting `(2,8),(3,7),(5,5),(7,3),(8,2)`.

The additional explicit tests include the failed positive pairs `(1,73),(4,70),(6,68)` at q=37, together with the successful `74=9+65`; and the square-template test at m=1304, where k=1,…,6 fail but k=7 yields the negative pair `2608=98+2510`. These finite failures concern selected templates, not the existence target.

The audit cross-checks 271 used Liouville arguments; its sieve bound 2608 is **not** a claimed target-verification range. Its **PB-label mapping remains unresolved**: the report verifies its explicit three formulas but records that correspondence to the dispatched named “PB three-test” was not established. No label-level certification is inferred here, even though the explicit examples can be read separately. None of this computational evidence is needed by the integrated universal identity or the other Lean lemmas.

## 10. What was actually checked in Lean

The preserved integration records identify Lean **v4.32.2**, commit `f3b06c705e6c85f5314019d5d3baab0fec5b580c`, Lake `5.0.0-src+f3b06c7`, and Mathlib commit `905b95818eb32af7874a58b427f50c1711a5e96c`. All nine dependency revisions are listed in `REPRODUCE.md:17–29`. The integration report (§6) records exact-SHA public availability witnesses no later than **2026-07-31**, including 2026-07-28 for Lean and Mathlib, and checks the installed revisions against those records. The later local checking date is not a later external source version. This exposition did not fetch sources or change any pin.

The following are **recorded completed commands**, run with working directory `P/lean`; they were not newly executed by this writer:

| Command | Recorded exit | Evidence under `formal/integration/` |
|---|---:|---|
| `lake build` | 0 | `v1-04-default-build.{json,stdout,stderr}` |
| `lake build Statement.Partial` | 0 | `v1-05-partial-build.*` |
| `lake env lean Statement/Partial.lean` | 0 | `v1-06-partial-direct.*` |
| `lake env lean -t 0 Statement/Partial.lean` | 0 | `v1-07-partial-trust-zero.*` |
| `lake env lean --stdin < ../formal/integration/v1-08-root-import-check.stdin.lean` | 0 | `v1-08-root-import-check.*` |
| `lake env lean --stdin < ../formal/integration/v1-09-absent-endpoints.stdin.lean` | 1, expected | `v1-09-absent-endpoints.*` |

The default build explicitly built `Statement.Partial` and root `Statement`, completing 925 jobs. The direct and trust-zero checks covered the actual integrated file. The root check imported `Statement`, checked all 50 added declarations (42 theorems and eight definitions), and repeated the axiom queries. The expected exit 1 in the last row consists of the two `Unknown identifier` diagnostics for `pointwise_keystone` and `liouville_goldbach`; it is evidence of **absence**, not an admitted proof.

All 42 partial theorems and 11 local/base definitions have the recorded transitive axiom set `{propext, Classical.choice, Quot.sound}`. The 29 queried upstream declarations use subsets of that set. The recorded closure check reports no `sorry`, `admit`, `sorryAx`, unsupported custom axiom, or native-evaluation assumption. Four unused-variable lints remain at `Partial` lines 51, 171, 187 and 291; the guarded statements were retained. The direct axiom output is `v1-06-partial-direct.stdout:21–102`, with matching maps recorded for the trust-zero and root checks in `audit-v1.json`.

The trust boundary includes the pinned Lean implementation/kernel, these foundational axioms, and the installed pinned dependency artifacts. This is not a fresh from-source rebuild of every upstream library or an independently implemented kernel check. The pre-existing `UnfinishedScaffold` only requires a `Target` proof as a field; no inhabitant is supplied, and `Partial` neither imports nor uses it. A definition named `Target`, or an axiom report on that definition, is not a proof of its proposition. [Mechanical evidence: integration report §§2–6; `REPRODUCE.md:43–157`.]

### Key prose-to-declaration map

All line ranges below refer to the same integrated `Partial.lean` hash in §11. The full 42-theorem inventory and upstream source map are in `formal/integration/source-proof-map-v1.txt`; this table identifies the load-bearing steps of this exposition.

| Prose source in `proof-v2.md` | Actual declaration(s) | Lines |
|---|---|---:|
| C01.2, C01.1: unit and sign | `omega_one`, `lambda_one`, `lambda_sign` | 43–55 |
| E01.1: multiplicity and multiplication | `omega_mul`, `lambda_mul` | 57–64 |
| E01.2: primes and small signs | `lambda_prime`, `lambda_two`, `lambda_three`, `lambda_four`, `lambda_five` | 66–86 |
| E01.2: doubling and squares | `lambda_two_mul`, `lambda_square` | 88–96 |
| E03: exact scaling | `hasSignedRepresentation_mul`, `representation_scaled_sign` | 102–122 |
| E02: diagonal | `representation_double`, `representation_diagonal` | 124–137 |
| E04, E05.8: two-sign seed and all 8m | `representation_two_sign_seed`, `eight_two_sign_seed`, `representation_multiple_eight` | 139–159 |
| C02: interval and casts | `mem_I_iff`, `interval_eq_Icc`, `interval_bounds`, `interval_card_cast` | 161–180 |
| C02: reflection | `reflection_mem`, `reflection_involutive`, `reflection_bijection` | 182–198 |
| C03: direct and reflected sums | `sum_lambda_interval`, `sum_lambda_reflection` | 200–213 |
| C04: ordered-pair/count bridge | `mem_orderedRepresentations`, `orderedRepresentations_eq_image`, `representation_count_eq_card_indices` | 215–250 |
| C05–C06: indicator and its sum | `two_sign_indicator`, `representation_count_eq_indicator_sum` | 252–266 |
| C07: integer identity | `four_mul_representation_count` | 268–289 |
| C08–C09: existence, strict bound, margin | `representation_count_pos_iff`, `count_pos_iff_keystone`, `keystone_ge_four_iff` | 291–308 |
| A01: universal equivalences | `target_iff_forall_hasRepresentation`; `target_iff_count_pos`, `target_iff_pointwise_keystone` | 98–100; 310–327 |
| PC00: two prime occurrences | `exists_prime_pair_factor_of_lambda_one` | 329–360 |
| PC01: Target iff all 2pq | `target_iff_prime_product_core` | 362–386 |

The PB/LS premises, their additional prose-only route deductions, the O-M5 rejection, the paper's analytic results, and the finite Python audit are not additional declarations in this table or hidden proof dependencies.

## 11. Exact artifact identity and source coverage

The following SHA-256 digests were recomputed locally during preparation with `shasum -a 256`; the three assigned mathematical snapshot hashes matched exactly.

| Input path relative to P | SHA-256 |
|---|---|
| `request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `nl/generator/proof-v2.md` | `bdcf57b670ed1e1410bacad5a2f9182c565add056714ef85e0155f939a6b7735` |
| `lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` |
| `formal/integration/integration-report-v1.txt` | `0f008c380573638e8b52796e8252eda83ee5e1eb79fd7a0caed6ef58a81984f7` |
| `formal/integration/source-proof-map-v1.txt` | `98fe3ef1958403c629e55d0a97fff50f5b2270c3e157e0e8f08664675888e977` |
| `formal/integration/audit-v1.json` | `4d32b5248d82c827edcb958ecd63ea62d68504bedf9fb396aa56edbcc7ca4db3` |
| `REPRODUCE.md` | `cb982a4687549930a398cec4b3d81449ebec7cd0bb2eb9ed8fc75f8d30e301c0` |
| `lean/.lake/packages/mathlib/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `nl/searcher/extraction-v2.md` | `787e83caae80656c7874f2a1e133f57e88dfcbde60a88b3d3b2e78653a954a6f` |
| `knowledge/mangerel-v2/paper.pdf` | `ae26a659220985c55576a18d05a84d5a56988024f8781ae4ccbe04847ac16505` |
| `sources.md` | `a8230ab9eb2e6e43d4c860fa1d35ecc74380995361973122500f750cd474b18a` |
| `nl/code-executor/report.md` | `9df3e8eef714c3e16ebaa76e336b726eca1d36c15c63257869da9696e32e4ba4` |
| `nl/code-executor/finite_certify.py` | `00a9d66bd81ca58e5cf0148fba6fa5b742c6a3285c82f46d5a1e3952aeab98f5` |
| `nl/code-executor/evidence.json` | `b42b9544e632431476c872b5696679d2908f05858737f6718f7d8c5a626fd72e` |

Coverage is separated by function: v2 and the integrated code support §§1–7; the factor-list source supports multiplicity and multiplicativity; the integration records support §10's compiler and dependency facts; only the eligible Mangerel v2 extraction and PDF pages 1–3 support §8's literature discussion; the explicitly finite audit supports §9. No paper theorem is a dependency of the integrated partial proof.

This document reorganizes existing arguments and statuses; it proposes no mathematical repair or replacement assertion. Only `FINAL_ARGUMENT.md` was written. No Lean source, protected definition, proof body, dependency, source ledger, or shared record was changed. No Lean or Python proof check was newly run by this writer. The deliverable is Markdown; no LaTeX compilation or new PDF generation was attempted or claimed.

## 12. Restart state

- **Problem:** all even N>2 must have positive witnesses with both Liouville values −1, including the possibility a=b.
- **Established partial content:** explicit diagonal and all-8m constructions; the exact ordered identity and reflection/count bridges; `Target` equivalent to the strict pointwise bound and to representations of all 2pq. The precise integrated version and its successful compiler/axiom evidence are identified above.
- **Concrete blocker:** neither of the universal goals in §6 has a proof. There is no complete large-N-plus-finite-remainder substitute.
- **Failed or limited routes:** O-M5 is refuted at q=5; the three fixed PB tests fail at q=59; finite templates do not supply uniform PB or LS. The separate finite audit retains its unresolved PB-label mapping.
- **Remaining directions:** a uniform prime-core witness construction or the strict pointwise counting bound would finish the existing reductions. PB and LS are only sufficient-route proposals with missing premises. The eligible paper supplies context and a different eventual correlation theorem, not either missing proof.

**Final status: the partial development compiles; Target remains UNRESOLVED.**
