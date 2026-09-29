Mode: CERTIFICATION — candidate production, not independent mathematical acceptance.

# Elementary lemmas, counting identity, and prime-core reduction — candidate v1

Author/owner: `nl-generator`, task `987c8d91ddff`.
Problem root P: `.clawcodex/math-team/problems/liouville-goldbach-jul2026`.

This artifact supplies proof candidates for the assigned elementary and counting results and an equivalence reduction. It does **not** supply a proof of the full conjecture. The remaining uniform prime-indexed bridge and the alternative shift bridge are explicitly open. No result in this file has been independently accepted, compiled as a Lean theorem, or integrated by this worker.

## 0. Exact inputs, definitions, and provenance

### 0.1 Protected target

The fixed definitions are `P/formal/approved-v1/Definitions.lean:6–14`:

- `omega n = n.primeFactorsList.length`, a natural number;
- `lambda n = (-1 : Z) ^ omega n`, an integer;
- `Target` is `forall N : Nat, Even N -> 2 < N -> exists a b : Nat, 0<a and 0<b and N=a+b and lambda a=-1 and lambda b=-1`.

Write Ω and λ for these exact definitions. For an integer s, abbreviate

`P_s(n) := exists a,b : Nat, 0<a, 0<b, n=a+b, lambda(a)=s, lambda(b)=s`,

and write `G(n) := P_(-1)(n)`. These abbreviations impose no parity, primality, coprimality, or distinctness on a,b.

All arguments of λ used below are proved positive. In particular, nothing uses the totalized value at zero. The ordinary-integer wording of the request and this natural-domain target have the following elementary transport: a positive integer has a unique natural representative, and this representation preserves addition, multiplication, order, and the prime-factor list of a positive input. If an integer N>2 is even, write N=2m in integers; then m>1, so N,m and any positive witnesses are natural representatives. Conversely, coercing natural positive witnesses gives integer witnesses. Thus using natural indices here does not remove any admissible integer target. The protected Lean statement itself is unchanged.

### 0.2 Candidate inputs, not assumed theorems

The plan inputs are:

- `P/nl/sketcher/formal-handoff-v1.md`, especially C01–C09 and E01–E05 in lines 51–80;
- `P/nl/sketcher/decomposition-v1.md`, the graphs at lines 19–66;
- `P/nl/explorer/attempt-v1.md`, M/S at lines 21–29, core reduction at lines 74–90, PB at lines 92–106, and shift route at lines 140–172.

Their assertions are not treated as established dependencies. The proofs below supply the required steps directly. No paper theorem or remembered analytic result is used.

### 0.3 Exact foundational factor-list source

Let F denote the local file

`P/lean/.lake/packages/mathlib/Mathlib/Data/Nat/Factors.lean`

at Mathlib commit `905b95818eb32af7874a58b427f50c1711a5e96c`. Its immutable source URL is

`https://github.com/leanprover-community/mathlib4/blob/905b95818eb32af7874a58b427f50c1711a5e96c/Mathlib/Data/Nat/Factors.lean`.

Title/module: *Prime numbers / prime factorization*, `Mathlib.Data.Nat.Factors`; file authors: Leonardo de Moura, Jeremy Avigad, Mario Carneiro (F:1–5). The supplied environment report `P/formal/environment/environment-report.txt:17–30,115–125` records public exact-SHA availability on 2026-07-28 and the matching Lean v4.32.2 environment. This is before the 2026-07-31 cutoff. This worker checked `git rev-parse HEAD` at the checkout: it returned the stated SHA; `git status --short -- Mathlib/Data/Nat/Factors.lean` returned no changes. This worker did not repeat the environment's external-publication audit.

The exact factor-list facts used are:

- **F1** (`Nat.primeFactorsList_one`, F:49–50): `primeFactorsList 1 = []`.
- **F2** (`Nat.prime_of_mem_primeFactorsList`, F:55–65): every entry of `primeFactorsList n` is prime.
- **F3** (`Nat.prod_primeFactorsList`, F:70–81): if `n != 0`, the product of `primeFactorsList n` is n.
- **F4** (`Nat.primeFactorsList_prime`, F:83–88): if p is prime, `primeFactorsList p = [p]`.
- **F5** (`Nat.primeFactorsList_unique`, F:167–179): if the product of a finite list l is n and every entry of l is prime, then l is a permutation of `primeFactorsList n`.
- **F6** (`Nat.perm_primeFactorsList_mul`, F:195–202): if `a != 0` and `b != 0`, then `primeFactorsList (a*b)` is a permutation of `primeFactorsList a ++ primeFactorsList b`.

F6 expressly has **no coprimality assumption**. F:198–202 derives it from F5, list-product concatenation, F3, and F2. Repeated prime occurrences remain repeated list entries. F5 is stated here also to expose the foundational unique-factorization dependency; the proofs below can use F6 directly. No statement equivalent to the additive target occurs in any of F1–F6.

All subsequent finite-list, finite-set, exponent, and ordered-ring manipulations are derived explicitly below. Their eventual Lean implementation must use the same pinned dependency closure; this artifact does not claim those formal proof scripts exist.

### 0.4 Input identities

SHA-256, computed before this candidate was written:

| Input relative to P | SHA-256 |
|---|---|
| `request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `formal/approved-v1/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `nl/sketcher/formal-handoff-v1.md` | `25ce7919c925c8a3d8ae3a6296a65aa92e93fec3fcdd18a4df41675fa0dbdfb7` |
| `nl/sketcher/decomposition-v1.md` | `042453780be12a3446e78255c7894d06cbf829271ec48a9c2619198b2510ca3a` |
| `nl/explorer/attempt-v1.md` | `5143a167b3ac0e26116b33e934a3e33fff2bc6c44b5a7608e01c7f73d4cf94a2` |
| `lean/.lake/packages/mathlib/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` |
| `formal/environment/environment-report.txt` | `05e10971b80acab2a04139ec6a0647e5f8fbd4a09bb516b1db205b084adac71a` |

## 1. Signed arithmetic and multiplicity

### C01.1 — exponent parity, sign dichotomy, and unit square

**Statement.** For k in Nat, `(-1)^k` is 1 if k is even and -1 if k is odd. Consequently for every n>0, `lambda(n)=1 or lambda(n)=-1`, and `lambda(n)^2=1`. More precisely, `lambda(n)=1` iff Ω(n) is even, and `lambda(n)=-1` iff Ω(n) is odd.

**Proof.** Every natural k has one of the forms 2r or 2r+1: induction starts with 0=2*0, and taking a successor switches these two forms. They cannot both occur: if r<=s then 2r<=2s<2s+1, while if s<r then r>=s+1 and 2r>=2s+2>2s+1. Both possibilities exclude 2r=2s+1.

By induction on r, `(-1)^(2r)=1`: the r=0 case is the definition of zeroth power; increasing r multiplies the preceding power by `(-1)^2=1`. Hence `(-1)^(2r+1)=1*(-1)=-1`. Substitution of k=Ω(n) gives the dichotomy. Since 1 and -1 are different integers, it also gives each asserted converse. In both possible sign cases the square is 1. The argument actually applies to the total definition at any natural n, but only positive n will be used. No factorization theorem is needed for this step.

### C01.2 — value at one

**Statement.** `Omega(1)=0` and `lambda(1)=1`.

**Proof.** F1 gives the empty factor list, whose length is 0. The definition of λ gives `(-1)^0=1`.

### E01.1 — complete multiplicativity on positive inputs

**Statement.** If u,v>0, then

`Omega(uv)=Omega(u)+Omega(v)` and `lambda(uv)=lambda(u)*lambda(v)`.

**Proof.** Positivity gives the two nonzero hypotheses of F6. A permutation of finite lists preserves length: each elementary transposition merely exchanges two positions; equivalently this follows by induction on the constructors of list permutation. Concatenation has length equal to the sum of lengths, as induction on its first list shows. Taking lengths in F6 therefore gives the stated Ω equality. Importantly, common prime factors are not discarded by concatenation.

For completeness, the exponent identity `z^(r+s)=z^r*z^s` for natural r,s follows by induction on s from the zeroth- and successor-power definitions and associativity of multiplication. Apply it with z=-1 in the integers and with r=Ω(u), s=Ω(v). This proves the λ equality. No coprimality, primality, or squarefreeness of u,v was assumed.

### E01.2 — primes, squares, doubling, and finite signs

**Statement.** If p is prime, `Omega(p)=1` and `lambda(p)=-1`. If t>0, `lambda(t^2)=1`. For x>0, `lambda(2x)=-lambda(x)`. In particular,

`lambda(2)=lambda(3)=lambda(5)=-1`, `lambda(4)=1`.

**Proof.** F4 identifies a prime's factor list with the singleton [p], whose length is 1. A prime is at least 2, so positivity is available in all later multiplicative uses. E01.1 and C01.1 give `lambda(t*t)=lambda(t)^2=1`. Since 2 is prime, E01.1 gives `lambda(2x)=(-1)*lambda(x)=-lambda(x)`. Taking t=2 gives λ(4)=1.

Here and later the small primality checks can be made without an external primality theorem as follows. If n>=2 is composite, write n=de with d,e>=2; one of d,e, say d, satisfies d<=e and hence d^2<=n. Thus to prove primality it suffices to exclude each integer d>=2 with d^2<=n. For 2,3 there is no such d; for 5,7 the only one is 2, which divides neither. For the other numbers used later the required nonzero remainder lists are:

| n | possible d>=2 with d^2<=n | remainders n mod d, in that order |
|---|---|---|
| 13 | 2,3 | 1,1 |
| 19 | 2,3,4 | 1,1,3 |
| 59 | 2,3,4,5,6,7 | 1,2,3,4,5,3 |

The underlying elementary characterization is that a nonprime n>=2 has a divisor other than 1 and itself; writing n as that divisor times its complementary divisor yields d,e>=2. The table is exact integer division, not a probabilistic test. These checks establish only the listed primes. They do not establish any infinite prime-indexed claim.

## 2. Scaling, diagonal, and every multiple of eight

### E03 — scaling with the exact multiplier sign

**Statement.** For any integer s, positive integer d, and `P_s(n)`, one has `P_(lambda(d)*s)(dn)`. In particular, if s is 1 or -1 and `lambda(d)=-s`, then `G(dn)`.

**Proof.** Let a,b be the positive witnesses for `P_s(n)`. The proposed witnesses are da,db. They are positive, and distributivity gives `dn=d(a+b)=da+db`. Every use of E01.1 has positive factors; it gives `lambda(da)=lambda(d)*s` and the identical formula for db. If λ(d)=-s, these two signs equal `(-s)*s=-s^2=-1`, since s^2=1. The same d multiplies both summands; no independently chosen multipliers have been introduced.

### E02 — diagonal construction

**Statement.** If N is even, N>2, and `lambda(N)=1`, then `G(N)` with a=b=N/2. Equivalently, whenever m>1 and `lambda(m)=-1`, `G(2m)` is witnessed by (m,m).

**Proof.** Evenness gives a natural m with N=m+m=2m. Since N>2, m>1. E01.2 applies to this positive m, giving `1=lambda(N)=-lambda(m)`, and therefore λ(m)=-1. The pair (m,m) has the required sum and signs. The equivalent direct criterion follows immediately from its displayed witnesses. Equality of the two witnesses is explicitly allowed by the target.

### E04 — two-sign seed transfer

**Statement.** If `P_(-1)(d)` and `P_1(d)`, then for every m>0, `G(dm)`.

**Proof.** By C01.1 exactly one of λ(m)=1 and λ(m)=-1 holds. In the first case, scale the negative seed pair by m using E03; in the second case scale the positive seed pair. Multiplication by 1 preserves the seed signs in the first case, and multiplication by -1 reverses the positive signs in the second. Commutativity identifies md with dm. The hypotheses contain actual positive seed witnesses in both cases.

### E05.8 — all `N=8m`, with no multiplier restriction beyond positivity

**Statement.** For every natural m>0, `G(8m)`; moreover 8m is even and greater than 2.

**Proof.** If λ(m)=1, choose a=3m, b=5m. These are positive; their sum is 8m; and E01.1 with the signs from E01.2 gives

`lambda(3m)=(-1)*1=-1`, `lambda(5m)=(-1)*1=-1`.

If λ(m)=-1, choose a=b=4m. Again both are positive and sum to 8m, while

`lambda(4m)=1*(-1)=-1`.

C01.1 exhausts the cases. Finally m>=1 gives 8m>=8>2, and 8m=2(4m) is even. This is an unconditional partial family; it does not cover all even N merely because m was arbitrary.

## 3. Counting conventions and the exact signed identity

These definitions agree with the proposed interfaces at `formal-handoff-v1.md:29–45`. They are definitions for this proof artifact, not edits to the protected Lean file.

For natural N and x, let

- `I_N = {a : Nat | 0<a and a<N}`;
- `J_x = {a : Nat | 0<a and a<=x}`;
- `F_N = {a in I_N | lambda(a)=-1 and lambda(N-a)=-1}`;
- `R(N) = |F_N|`, a natural number;
- `L(x) = sum_(a in J_x) lambda(a)`, an integer;
- `C(N) = sum_(a in I_N) lambda(a)*lambda(N-a)`, an integer.

All sets are finite: I_N is contained in the first N naturals and J_x in the first x+1. `N-a` inside λ is natural subtraction. It will only be evaluated with a in I_N, where it is the ordinary positive difference. Define also the integer

`K(N) = ((N:Z)-1) - 2*L(N-1) + C(N)`.

The `N-1` in the argument of L is a natural index. The subtraction in `(N:Z)-1`, in `K(N)`, and in every following sign/sum formula is integer subtraction. We impose N>=2 throughout C02–C09, although some preliminary facts hold more generally.

### C02 — interval, cardinality, and reflection

**Statement.** For N>=2:

1. `I_N = J_(N-1)` and `|I_N|=N-1` in naturals;
2. `(|I_N|:Z)=(N:Z)-1`;
3. for a in I_N, both a and b=N-a are positive and below N, a+b=N, and `N-b=a`;
4. `rho_N(a)=N-a` is a bijection from I_N to itself, with inverse itself.

**Proof.** For natural a, `a<N` is equivalent to `a<=N-1` when N>=1. One direction follows by subtracting 1 from the inequality a+1<=N; the reverse follows from a<=N-1<N. Thus I_N consists exactly of `1,2,...,N-1`. The map k↦k+1 from `0,1,...,N-2` to this list is bijective, so this interval has N-1 elements. Here N>=2 ensures N-1>=1 and gives the displayed endpoints without exceptional conventions. Casting the equality `(N-1)+1=N` into the integers gives `(N-1:Nat):Z = (N:Z)-1`, proving (2).

For (3), a<N gives a<=N, so natural subtraction is exact: `a+(N-a)=N`. It also gives `N-a>=1`. Since a>=1, the same equality gives `N-a<=N-1<N`. Now subtract b=N-a from a+b=N; the inequality b<=N ensures natural subtraction is exact and yields N-b=a. This proves that rho_N maps I_N into itself and its square is the identity. The latter property gives both injectivity (apply rho_N to an equality of images) and surjectivity (a is the image of rho_N(a)). No λ(0) value has entered.

### C03 — reflected sum

**Statement.** For N>=2,

`sum_(a in I_N) lambda(N-a) = L(N-1)`.

**Proof.** C02's bijection replaces the index a by b=N-a, with every b in I_N appearing exactly once. To see the finite-sum principle directly, enumerate the finite domain; applying a bijection permutes its list of elements, and commutativity and associativity of integer addition leave the sum unchanged. Therefore the left side is `sum_(b in I_N) lambda(b)`. C02 identifies I_N with J_(N-1), so this is L(N-1).

### C04 — explicit ordered-positive-pair correspondence

**Statement.** For N>=2, the function

`a -> (a,N-a)`

is a bijection between F_N and

`Q_N = {(a,b) : Nat*Nat | 0<a, 0<b, N=a+b, lambda(a)=-1, lambda(b)=-1}`.

Hence R(N) is exactly the number of ordered positive pairs in the request's count.

**Proof.** If a belongs to F_N, C02 gives positivity of a,N-a and their sum N; the definition of F_N gives the two negative signs. This proves the map lands in Q_N.

Conversely, suppose (a,b) belongs to Q_N. Since b>=1 and a+b=N, a<N; and since a>=1, b<N. Thus a belongs to I_N. Natural subtraction is exact because a<=N, and cancelling a from a+b=N gives b=N-a. The two signs therefore put a in F_N. This inverse sends (a,b) to its first coordinate. Composing either way recovers the original element, so the maps are inverse bijections. Q_N is finite because both coordinates lie in I_N.

If a!=b, the pairs (a,b) and (b,a) correspond to different first coordinates and are counted separately. If a=b, the single diagonal pair corresponds to one index and is counted once. There is no division by 2 and no prohibition on a=b.

### C05 — two-sign indicator identity

**Statement.** For positive a,b, define the integer indicator

`delta(a,b) = 1` if `lambda(a)=lambda(b)=-1`, and `delta(a,b)=0` otherwise.

Then

`4*delta(a,b) = (1-lambda(a))*(1-lambda(b))`.

**Proof.** C01.1 gives four exhaustive pairs of signs. If both are -1, the right side is `(1+1)*(1+1)=4`, equal to the left. In each other pair at least one sign is 1, giving a zero factor on the right; the indicator is then zero on the left. This uses the signed integer values, not natural subtraction.

### C06 — cardinality as the integer indicator sum

**Statement.** For N>=2,

`(R(N):Z) = sum_(a in I_N) delta(a,N-a)`.

**Proof.** All delta terms are defined at positive arguments by C02. Partition the finite set I_N into F_N and its complement. Each term on F_N is 1, and each term on the complement is 0. Thus the sum is the sum of |F_N| copies of 1, namely the integer cast of |F_N|. The elementary rule “the sum of k copies of 1 is k” follows by induction on k, starting with the empty sum 0 and adding 1 at each step. This is exactly the asserted cast of R(N).

### C07 — exact integer counting identity

**Statement.** For every N>=2,

`4*(R(N):Z) = ((N:Z)-1) - 2*L(N-1) + C(N)`.

**Proof.** Multiply C06 by the integer 4 and distribute multiplication over its finite sum. Apply C05 to each term; C02 has verified its positive-input hypotheses. Expanding every product in Z gives

`4*(R(N):Z)`
`= sum_(a in I_N) [1-lambda(a)-lambda(N-a)+lambda(a)*lambda(N-a)]`
`= (|I_N|:Z) - sum_(a in I_N) lambda(a)`
`  - sum_(a in I_N) lambda(N-a)`
`  + sum_(a in I_N) lambda(a)*lambda(N-a)`.

Distributing a finite sum across additions/subtractions follows by induction on an enumeration of I_N; it is only distributivity and associativity of integer addition. By C02, the constant sum is `(N:Z)-1`, and the first λ sum is L(N-1). C03 makes the reflected λ sum L(N-1), and the last sum is C(N) by definition. Combining the two identical subtracted sums proves the displayed identity. No division, truncation of a signed quantity, or unguarded cast of natural subtraction is used.

Evenness is **not** a hypothesis of C07. The bound N>=2 is the only N-hypothesis.

### C08 — count/existence bridge

**Statement.** For every N>=2,

`0<R(N) iff G(N)`.

**Proof.** A finite set has positive cardinality exactly when it is nonempty: an enumeration of the empty set has length zero, while an enumeration containing an element has length at least one; conversely, a list of positive length has a first element. Apply this to F_N. C04 carries its elements precisely to the ordered witnesses of G(N), in both directions. This supplies the exact existence bridge, including positivity and the original sum equation.

### C09 — strict-bound and integer-margin equivalences

**Statement.** For every N>=2, the following are equivalent:

1. `0<R(N)`;
2. `0<K(N)` in Z;
3. `2*L(N-1)-((N:Z)-1) < C(N)` in Z;
4. `4<=K(N)` in Z;
5. G(N).

**Proof.** Put r=(R(N):Z), a nonnegative integer. The natural-to-integer embedding preserves order: the cast of a natural k is the sum of k copies of 1, so k>=1 is equivalent to its cast being at least 1, and k=0 is equivalent to its cast being 0. Consequently `R(N)>0` is equivalent to r>=1 and to r>0.

C07 says K(N)=4r. Because 4 is strictly positive, 4r>0 iff r>0. Also, for integral r>=0, 4r>=4 iff r>=1: the forward direction excludes r=0, and the reverse multiplies r>=1 by 4. This proves equivalence of (1),(2),(4). Moving integer summands across the strict inequality

`0 < ((N:Z)-1)-2*L(N-1)+C(N)`

gives exactly (3). Finally C08 gives (1) iff (5).

The non-strict assertion K(N)>=0 is automatic from the identity and does **not** imply existence. Strict positivity, or the integer margin 4, is essential.

### A01 — conditional counting assembly, with its missing premise exposed

If one proves

`K01: forall N : Nat, Even N -> 2<N -> 2*L(N-1)-((N:Z)-1) < C(N)`,

then `Target` follows from C09 at each admissible N; N>2 supplies N>=2. Conversely, `Target` and C09 imply precisely this same pointwise K01. Thus the counting route has been reformulated exactly, not solved. There is no proof of K01 here, no average estimate substituted for it, and no unsupported axiom declaring it.

## 4. Exact prime-product-core reduction

### PC00 — selecting two prime occurrences with a positive-sign remainder

**Statement.** If m>1 and `lambda(m)=1`, there are primes p,q and a positive natural d such that

`m=d*p*q` and `lambda(d)=1`.

The primes may be equal. A remainder d=1 is allowed.

**Proof.** Let l be the actual list `primeFactorsList m`. Since m>1, m!=0, so F3 gives `prod(l)=m`. The list cannot be empty: the empty product is 1, contradicting m>1. Its length k=Ω(m) is even by C01.1. A positive even natural is at least 2: writing k=2r, positivity forces r>=1. Thus l has at least two positions. Write it as `p :: q :: t`.

F2 proves p,q and every entry of t are prime; it imposes no distinction between positions' values. Set d=prod(t). Every entry of t is at least 2, hence positive. Induction on t proves its product is positive, with the empty product d=1 as the base case. The list-product equality gives m=p*q*d=d*p*q.

Now E01.1 applies to the positive factors d,p,q, and E01.2 gives λ(p)=λ(q)=-1. Therefore

`1=lambda(m)=lambda(d)*lambda(p)*lambda(q)=lambda(d)*((-1)*(-1))=lambda(d)`.

This proves the required remainder sign. It also explains why removing two prime occurrences preserves even multiplicity; equivalently Ω(m)=Ω(d)+2 follows from E01.1. No squarefreeness or factor-divisibility shortcut has been assumed.

### PC01 — equivalence to all prime-product cores

Define

`Core := forall p,q : Nat, Prime p -> Prime q -> G(2*p*q)`.

**Statement.** `Target iff Core`.

**Proof, Target implies Core.** Fix arbitrary primes p,q. Each is at least 2, so `2*p*q>=8>2`. It is even because it equals 2(pq). Apply Target to obtain exactly G(2pq). This includes p=q and p=2 or q=2.

**Proof, Core implies Target.** Assume Core only for this implication, and let N be an arbitrary even natural with N>2. Write N=2m with m natural. Then m>1. By C01.1, either λ(m)=-1 or λ(m)=1.

- If λ(m)=-1, E02's direct diagonal criterion gives G(N), with (m,m).
- If λ(m)=1, apply PC00 to obtain primes p,q and positive d with m=dpq and λ(d)=1. Core gives positive witnesses a,b for G(2pq). E03 scales them by d. Their signs remain -1 because λ(d)=1, their sum is `d*(2pq)=2m=N`, and both remain positive. Hence G(N).

These are all possible signs. As N was arbitrary, Target follows. The assumption Core is discharged only into this implication and then the equivalence; it is **not** declared true.

**Counterexample consequence.** Any counterexample N would have λ(N/2)=1 by the diagonal argument. Applying PC00 to m=N/2 produces a core 2pq for which G(2pq) also fails, since otherwise scaling solves N. Moreover d>=1 gives 2pq<=N. In particular, a least counterexample, if one exists, must itself have N=2pq: if d>1 the failing core is smaller, while if d=1 the equality holds. This is only a conditional reduction and not an existence assertion about counterexamples.

## 5. Focused attempt at a uniform bridge: exact progress and failure

This section is part of the preserved attempt. It separates proved conditional implications from the unproved uniform statements. It does not promote numerical observations from the explorer into premises.

### PB00 — the proposed prime-indexed positive bridge would suffice

Define the unresolved statement

`PB: forall q : Nat, Prime q -> 5<=q -> P_1(2*q)`.

**Conditional assertion.** PB implies Core, hence Target by PC01.

**Proof of the conditional assertion.** Let p,q be arbitrary primes. If q>=5, PB supplies a positive-sign pair for 2q. Scale it by the positive prime p using E03: λ(p)=-1, so the resulting pair is negative-negative and sums to 2pq. If p>=5 instead, exchange the roles of p and q.

If neither prime is at least 5, each is 2 or 3. Indeed a prime is at least 2, and 4 is not prime because 4=2*2. The remaining unordered cores are 8,12,18. They have negative pairs (3,5), (5,7), and (5,13), respectively. Their sums are exact, all numbers are positive, and the necessary primalities were checked in E01.2. This exhausts the cases, including equal primes. The PB hypothesis remains an open premise of the conditional assertion.

PB is **not** identified with the original target at 2q: the latter has the negative diagonal (q,q), whereas PB requires two positive signs. No necessity of PB for Target is asserted.

### PB01 — exact even-summand route and the partial-sum obstruction

**Statement.** For each positive q, a positive-sign representation of 2q with both summands even exists iff `P_(-1)(q)`.

**Proof.** Given q=a+b with both signs -1, E01.2 changes the signs of 2a,2b to +1 and their sum is 2q. Conversely, from positive even u,v with u+v=2q, write u=2a,v=2b. Positivity implies a,b>0, cancellation of 2 gives a+b=q, and `1=lambda(2a)=-lambda(a)` gives λ(a)=-1, with the same calculation for b.

Thus a sufficient route to PB is the additional **odd-target** statement `P_(-1)(q)` for every prime q>=5. This is a new assertion, not supplied by Target's even-N quantifier.

A direct counting attempt gives the following rigorous obstruction under failure. Suppose `P_(-1)(q)` fails, with q>=2. Partition I_q into A={a:λ(a)=-1} and B={a:λ(a)=1}. They partition the interval by C01.1. Reflection a↦q-a injects A into B: the reflected input is positive by C02, it cannot have negative sign without giving a forbidden pair, and therefore has positive sign. The map is injective by C02. Hence |A|<=|B| and

`L(q-1) = (|B|:Z)-(|A|:Z) >= 0`.

The equality is a finite sum of +1 and -1 over that partition. Therefore `L(q-1)<0` would suffice to prove `P_(-1)(q)` and then PB at q.

**Precise stalled obligation in this subroute.** No proof has been obtained of `L(q-1)<0` for every prime q>=5, nor of the weaker required `P_(-1)(q)`. The primality of q specifies λ(q), not the sum over all smaller integers; the displayed injection supplies no opposite inequality. No general sign assertion about L is imported. The strict-negativity condition is only a stronger sufficient conjectural subroute, not a fact used elsewhere.

A representation in PB may also have two odd summands. Since a sum equal to 2q has same-parity summands, PB at a fixed q is exactly the disjunction of the even-summand route just analyzed and an odd-odd positive-sign representation. No argument here excludes or covers the second possibility uniformly.

### PB02 — shifted tests, exact primality example, and why the finite test stops

Suppose q>=5 is prime and PB fails at q. Then:

1. `P_(-1)(q)` fails, by PB01;
2. `lambda(q-2)=1`: otherwise (2,q-2) is a negative pair at q;
3. `lambda(q-3)=1`: otherwise (3,q-3) is a negative pair at q;
4. `lambda(2q-1)=-1`: otherwise (1,2q-1) is a positive pair at 2q.

All complements are positive under q>=5, and each “otherwise” uses the exhaustive dichotomy C01.1. These conditions suggest trying the following three PB pairs:

- `(1,2q-1)` works if `lambda(2q-1)=1`;
- `(4,2(q-2))` works if `lambda(q-2)=-1`, since λ(4)=1 and doubling reverses sign;
- `(6,2(q-3))` works if `lambda(q-3)=-1`, since λ(6)=λ(2)λ(3)=1.

This is a precise three-test construction, but it is not a cover of all primes. For the prime q=59, primality was proved by the exact remainder table in E01.2, and

`57=3*19`, `56=2^3*7`, `117=3^2*13`.

E01.1–E01.2 show, respectively,

`lambda(57)=1`, `lambda(56)=1`, `lambda(117)=-1`.

Consequently all three candidate pairs at 2q=118 have signs (+1,-1): their second entries are 117,114=2*57,112=2*56. This exactly falsifies the three-test cover, without falsifying PB. In fact

`118=14+104`, `14=2*7`, `104=2^3*13`

is a positive-positive pair, since both factor counts are even. Equivalently, `59=7+52`, with `52=2^2*13`, is a negative-negative pair. These equalities are local exact checks, not an enumeration argument.

A product-parity continuation of the failed tests still leaves an explicit missing sign. For example, the forced signs λ(q-2)=λ(q-3)=1 imply only

`lambda((q-2)(q-3))=1`.

Expanding the product as `q^2-5q+6` gives no second computable sign: multiplicativity does not assign λ to a sum or polynomial from λ(q). Reducing that expression modulo q also gives no λ equality. Similarly, factoring `q^2-1=(q-1)(q+1)` expresses an unknown sign in terms of two unknown signs, not in terms of λ(q)^2. There is no justified contradiction at this point.

**Exact failure scope.** The three local constraints alone are compatible with a genuine prime, as q=59 proves. This does not prove that the full set of failure constraints is consistent, and it does not refute PB. The missing step is a uniform choice of a positive pair at 2q, or a uniform contradiction using *all* necessary constraints, for every prime q>=5. No such choice or contradiction was found in this attempt. Enlarging a finite table would not by itself establish that quantified step.

### LS01 — alternative shift bridge retained as an open sufficient statement

For clarity, the explorer's other uniform option is

`LS: for every m>1 with lambda(m)=1, there exists t with 0<t<m, lambda(t)=1, and [lambda(m-t)=1 or lambda(m+t)=-1]`.

**Conditional assertion.** LS implies Target.

**Proof of the conditional assertion.** Write an admissible N as 2m. If λ(m)=-1, use (m,m). Otherwise λ(m)=1 by C01.1 and LS supplies t. If λ(m-t)=1, use (2t,2(m-t)); the signs are both -1 by doubling. If that sign is not 1, C01.1 gives λ(m-t)=-1, and LS supplies λ(m+t)=-1; use (m-t,m+t). In both cases the witnesses are positive because 0<t<m, and their sum is 2m. The cases are exhaustive.

Conversely, if G(2m) fails, λ(m)=1, and for every positive t<m with λ(t)=1 one necessarily has

`lambda(m-t)=-1` and `lambda(m+t)=1`.

The first follows because a positive sign at m-t would solve G(2m) by doubling; the second follows because, once m-t is negative, a negative sign at m+t would give a negative pair directly. These implications are rigorous, but no uniform contradiction to this forced pattern has been obtained. No equivalence between LS and Target is claimed, and LS is not assumed in any unconditional lemma above.

## 6. Final assembly boundary and next action

The candidate unconditional results supplied here are C01.1–C01.2, E01.1–E01.2, E02–E04, E05.8, C02–C09, PC00, and the equivalence PC01. PB00, PB01–PB02's stated necessary/sufficient implications, and LS01's conditional implication are also accompanied by proofs of their **stated conditional directions**, not proofs of their open premises.

After review, these would give:

1. an unconditional proof for every multiple of eight and for the diagonal sign family;
2. an exact integer count/existence/strict-bound interface for every N>=2;
3. an exact reduction of the full target to all `2pq`, including equal primes;
4. explicitly open uniform bridges PB, LS, or the equivalent counting keystone K01.

The target remains unresolved in this artifact. The next action is a fresh NL verification of this exact candidate and its source dependency, followed by statement-aligned Lean implementations of the accepted local lemmas. A mathematical search for Core/PB/LS or K01 is a separate task. See `obligation-ledger-v1.md` for the dependency map, proof preconditions, unresolved claims, and handoff owners.
