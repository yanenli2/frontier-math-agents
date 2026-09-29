Mode: DISCOVERY — conjectural; no proof weight.

# Counterexamples and scoped obstructions, attempt v1

## Result and scope

- **No counterexample to the original target, uniform PB, or uniform LS-square was found.** No universal conclusion follows from the searches below.
- **Smaller obstruction to the proposed three-test PB construction:** the first prime is **q=37**, not just the example 59 in the supplied candidates. All three tests fail, but PB itself holds: `74=9+65` is positive-positive.
- **An actual Liouville obstruction to a universal strict correlation bound:** at **N=10**, `C(10)=9=N-1`. The target nevertheless holds, with five ordered negative-negative pairs. Thus a proposed bound `|C(N)|<N-1` for every admissible N is false; its sufficiency without control of L is a separate failure explained below.
- The obstruction to **fixed finite divisor seeds with common scaling, even with the diagonal added**, has a direct proof. It does not refute the target. The smallest uncovered targets for the two supplied seed menus are 44 and 116, respectively, and both have elementary target witnesses.
- A six-square shift menu already fails at **m=1304**. The full LS-square assertion survives there with `t=49`. No LS-square failure was found for eligible `2<=m<=10000`.
- **Surviving concrete branch:** prime-product-core reduction plus a genuinely uniform PB proof, not enlargement of a fixed divisor table. A new candidate reduction for LS-square reduces its obstruction search to squarefree positive-sign inputs and odd prime squares; see Section 5. These deductions need fresh review.

There is no target-negative claim in this report. All mathematical arguments, reductions, and computational minimality claims below are candidates for regulator routing and fresh verification, not accepted results or Lean results.

## 1. Exact definitions, hypotheses, and conventions

The request and protected definition file specify:

- On positive integers, `Omega(n)` counts prime factors **with multiplicity**, and `Omega(1)=0`.
- `lambda(n)=(-1)^Omega(n)`, with signed integer codomain. Thus `lambda(1)=+1`.
- **Target:** every even integer `N>2` has positive integers `a,b` with `N=a+b` and `lambda(a)=lambda(b)=-1`. Equality of summands is allowed. No oddness, primality, coprimality, distinctness, or squarefreeness restriction is added.
- The protected Lean statement uses naturals for N,a,b and explicit positivity, with `omega n = n.primeFactorsList.length`. Every argument of lambda in this report is positive; no conclusion uses its totalized value at zero.

Write `P_s(n)` for a positive representation `n=a+b` with both lambda signs equal to `s`, where `s` is +1 or -1.

The auxiliary assertions under investigation are exactly:

- **PB:** for every prime `q>=5`, `P_+(2q)`.
- **LS-square:** for every integer `m>1` with `lambda(m)=+1`, there is a positive square `t=u^2<m`, with `u>=1`, such that `lambda(m-t)=+1` or `lambda(m+t)=-1`.

Local arithmetic used below follows directly from the definition: concatenating prime-factor occurrences gives `Omega(xy)=Omega(x)+Omega(y)` for positive x,y, hence complete multiplicativity. In particular, a prime has sign -1, a positive square has sign +1, and doubling reverses sign. Therefore scaling both terms of `P_s(n)` by a positive d gives `P_(lambda(d)s)(dn)`. This needs no coprimality. These elementary dependencies still require the project's fresh verification/formalization; the unaccepted input routes are not premises.

## 2. Inputs and provenance

Read the exact request, protocol, protected definitions, and both assigned unaccepted candidate routes. No external browsing, paper, imported theorem, or unsupported remembered analytic result was used. No later-source contamination was encountered. Only Python standard-library integer arithmetic was used for experiments; this is not a Lean certification or a dependency-version audit.

Let P be `.clawcodex/math-team/problems/liouville-goldbach-jul2026`.

| Input relative to P | SHA-256 at inspection |
|---|---|
| `request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| `formal/approved-v1/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` |
| `nl/explorer/attempt-v1.md` | `5143a167b3ac0e26116b33e934a3e33fff2bc6c44b5a7608e01c7f73d4cf94a2` |
| `nl/generator/proof-v1.md` | `eb6974f5493f7b77773ba5e685240e8d608f43e6fb2a1156d627d7a0dbca86f5` |

The protocol read was `.clawcodex/skills/math-team/references/protocol.md`. This report is the only written mathematical artifact from this assignment. Code and recorded outputs are in Section 7 of this same file; no evidence depends on an unsaved script.

## 3. PB: a smaller failed construction, not a failed bridge

### Candidate and hypothesis audit

The three proposed PB pairs are

`(1,2q-1)`, `(4,2(q-2))`, `(6,2(q-3))`.

For prime `q>=5`, every entry is positive and each pair sums to `2q`. Their first entries have positive lambda sign. A failed three-test construction is equivalent to the necessary sign conditions

`lambda(q-2)=+1`, `lambda(q-3)=+1`, `lambda(2q-1)=-1`.

At `q=37`, the original PB hypotheses hold: 37 is prime and at least 5. Exact trial division through its square root verifies primality. The signs are

- `35=5*7`, so `lambda(q-2)=+1`;
- `34=2*17`, so `lambda(q-3)=+1`;
- 73 is prime, so `lambda(2q-1)=-1`.

Consequently the three pairs at 74 are `(1,73)`, `(4,70)`, `(6,68)`, each with signs `(+1,-1)`: `70=2*5*7` and `68=2^2*17` have odd factor counts.

### Exact conclusion failure and surviving witnesses

This refutes only the claim that those three pairs cover every prime q. It **does not** refute PB:

`74=9+65`, with `9=3^2` and `65=5*13`, has two positive signs.

Even the stronger odd-prime negative-sum route survives: `37=5+32`, and both signs are negative. Doubling gives another PB pair `74=10+64`.

The original target at 74 is separately solved by `37+37`. Thus all original target hypotheses hold at N=74, but its conclusion does not fail.

### Smallest and boundary checks

The primes in `[5,37)` are `5,7,11,13,17,19,23,29,31`. Respectively, successful pairs from the three-test menu are

`(1,9), (4,10), (1,21), (1,25), (1,33), (4,34), (6,40), (1,57), (4,58)`.

Their entries factor with even multiplicity. Trial division independently enumerated these primes and found 37 as the only three-test miss through 37. Hence 37 is the smallest obstruction to this particular construction, subject to fresh checking of this finite audit.

The cutoff q>=5 matters. Extending PB to primes 2 or 3 would be false: the unordered positive splits of 4 and 6 have no positive-positive pair. Conversely q=5 works by `10=1+9`. These excluded primes do not refute the stated PB or the target.

### Bounded continuation

For every one of the **1227** primes `5<=q<=10000`, a PB pair was found, using only the first 128 positive-sign candidate first summands and stopping at the first success. There were only **2484** sign comparisons and no cap-exhausted primes. The largest least positive first summand was 24, attained at

`2426=24+2402` for q=1213, and `3574=24+3550` for q=1787.

The three-test menu failed at 156 primes in this scope, starting `37,59,97,137,163,331,337,353,367,379`. These are not PB failures.

**Unresolved:** uniform PB, or a contradiction using the full failure conditions, not just several shifts. A finite successful partner menu in this scope is not a uniform construction. A next computational scope, only if given a new symbolic objective, is primes `10000<q<=20000`, requiring lambda arguments through 40000; it was **not** searched here.

## 4. Finite divisor-seed obstruction

### Exact restricted method

Fix a finite set of positive seed sums S, and any chosen positive representations of each seed. A permitted output is obtained by multiplying **both summands by the same positive integer d**. Also permit the diagonal construction whenever `lambda(N/2)=-1`. This covers arbitrary seed signs and arbitrary multiplier signs; mixed-sign seed pairs cannot turn into a negative-negative pair under common scaling.

Let `K=max({2} union S)`, and choose a prime p>K. Such a prime exists by the elementary argument that a prime divisor of `K!+1` cannot be at most K. Put `N=2p^2`.

### Hypothesis audit and obstruction proof

- p is an odd prime, so N is an even integer greater than 2 and meets every original N-hypothesis.
- The divisors of `2p^2` are `1,2,p,2p,p^2,2p^2`.
- A seed sum s must divide N if a common dilation of a representation of s sums to N.
- Since s<=K<p, the only possible seed sums are 1 and 2.
- Sum 1 has no positive split. Sum 2 has only `(1,1)`; its scaling factor is p^2, of positive lambda sign, so its output is `(p^2,p^2)` with two positive signs.
- The separately allowed diagonal is exactly this same positive-positive pair.

Thus **this restricted method cannot produce a target witness at N**, regardless of how its finite seed representations were chosen. Iterating common scalings does not help: their product is still one common scaling. Nothing here excludes finite families of more general parameter-dependent formulas, independently scaled summands, or a variable prime-indexed seed.

### Concrete witnesses and non-failure of the target

For the supplied menu `S0={5,7,8,10,12,14,18}`, the smallest uncovered even N>2 after allowing the diagonal is **44**. For the expanded menu `S1={5,7,8,10,11,12,13,14,17,18,19,23}`, it is **116**. The bounded computation through 20000 returned 2137 and 1534 uncovered targets, respectively; these counts describe the method only.

Both smallest obstructions satisfy the target:

- `44=2+42`, with `42=2*3*7`;
- `116=2+114`, with `114=2*3*19`.

For a concrete member of the general obstruction family, all seed sums at most 23 fail at `N=2*29^2=1682`, even with the diagonal. Nevertheless

`1682=2+1680`, with `1680=2^4*3*5*7`,

is a target pair: the factor counts are 1 and 7. Thus the conclusion that fails is finite-method coverage, not existence of negative summands.

**Recommended routing:** fresh NL verification of the exact restricted-method proof, then retain it as a planning obstruction. Do not spend a global-proof budget only enlarging constant divisor seed lists.

## 5. LS-square: finite-menu failures and a surviving reduction

### Boundaries and finite-menu obstruction audit

The condition m>1 is essential: at m=1 the sign is positive, but no positive t<m exists. This is excluded, not a counterexample. m=2,3 have negative lambda sign and also do not test LS-square. The first admissible m is 4; t=1 works since `lambda(3)=lambda(5)=-1`.

Allowing t=0 would create an invalid shortcut (`lambda(m-0)=+1` with a zero constructed summand). Allowing t=m would likewise evaluate a forbidden zero difference. Neither is permitted here.

For the menu of the first k positive squares, the computed smallest failures are:

| k | Menu ends at | Smallest eligible failure |
|---|---:|---:|
| 1 | 1 | 9 |
| 2 | 4 | 21 |
| 3 | 9 | 84 |
| 4 | 16 | 84 |
| 5 | 25 | 1253 |
| 6 | 36 | 1304 |
| 7 | 49 | none in 2<=m<=10000 |

For the four-square menu, `84=2^2*3*7` has positive sign, and each allowed shift has the forbidden sign pattern `(-1,+1)`:

`(83,85), (80,88), (75,93), (68,100)`.

Here the composite factorizations are `85=5*17`, `80=2^4*5`, `88=2^3*11`, `75=3*5^2`, `93=3*31`, `68=2^2*17`, and `100=2^2*5^2`; 83 is prime. But the full assertion succeeds at t=25, giving the target pair `168=59+109`.

A larger new finite-menu obstruction is `m=1304=2^3*163`, again of positive sign:

| t | m-t, with factorization | m+t, with factorization | Signs |
|---:|---|---|---|
| 1 | 1303, prime | 1305=3^2*5*29 | (-,+) |
| 4 | 1300=2^2*5^2*13 | 1308=2^2*3*109 | (-,+) |
| 9 | 1295=5*7*37 | 1313=13*101 | (-,+) |
| 16 | 1288=2^3*7*23 | 1320=2^3*3*5*11 | (-,+) |
| 25 | 1279, prime | 1329=3*443 | (-,+) |
| 36 | 1268=2^2*317 | 1340=2^2*5*67 | (-,+) |
| 49 | 1255=5*251 | 1353=3*11*41 | (+,-) |

All primalities in these factorizations were checked by exact trial division in the second invocation, not inferred from a probabilistic primality routine. Each of the first six shifts is a positive square less than m but fails the desired disjunction. The seventh is a valid LS-square certificate. It constructs

`2608=98+2510`, where `98=2*7^2` and `2510=2*5*251`

are both negative-sign positive integers. Again this is not a target or LS-square counterexample.

For all **4952** eligible `2<=m<=10000`, complete square searches found a certificate. They used **6554** comparisons because of early stopping. The largest least u was 7, attained only at m=1304. Since a no-witness case would have examined every positive square below m, these were complete LS-square tests in the stated finite scope, not just seven-square tests. The extra nonsquare menu `{1,4,6,9,10,14,15,16}` also had no failure through m=10000; no general inference is made from that observation.

### New candidate reduction: square scaling and square-primitive inputs

This is a new deduction requiring fresh verification, not an accepted theorem.

**Square scaling.** If LS-square holds at m and d>0, it holds at `d^2*m`: from `t=u^2<m`, take `t'=(du)^2`. Both inequalities remain strict and positive. Also

`d^2*m +/- t' = d^2*(m +/- t)`,

so complete multiplicativity and `lambda(d^2)=+1` preserve both tested signs. The input sign remains positive too.

**Reduction.** To prove uniform LS-square, it suffices to prove it on:

1. squarefree `r>1` with `lambda(r)=+1` (hence an even, positive number of distinct prime factors); and
2. odd prime squares `p^2`.

Indeed, write any eligible m as `m=r*s^2`, with r squarefree and s positive, by removing even parts of its prime exponents. Then `lambda(r)=lambda(m)=+1`.

- If r>1, a certificate at r scales by s^2 to one at m.
- If r=1, then m=s^2 with s>=2. Choose any prime p dividing s and write `s=pk`. A certificate at p^2 scales by k^2 to one at m. For p=2, the needed base m=4 is already covered by t=1; only odd prime squares remain as new cases.

Conversely, global LS-square covers both displayed subclasses, so this is also an equivalence after the elementary m=4 case. Equivalently, any failure descends to a squarefree positive-sign input or an odd prime square, of size at most the original m. In particular every `m=4k^2` works explicitly via `t=k^2`, giving `(m-t,m+t)=(3k^2,5k^2)` with two negative signs.

**Important limitation:** arbitrary positive-sign scaling, used in the target's prime-product reduction, does not preserve a square shift. Multiplying t by a nonsquare can destroy the square condition. Thus this argument does not reduce LS-square to just all prime products.

**Next scope:** fresh review of this reduction, then a symbolic analysis of odd prime squares and squarefree positive-sign inputs. If a further bounded falsification test has a specific purpose, the next interval is `10000<m<=20000`, with lambda values required below 40000; that interval was not tested here. Neither the absence of a witness nor the failure of a fixed menu closes LS-square.

## 6. Why a non-extremal correlation does not force the negative color

### Exact count decomposition

For any sign word `x_1,...,x_(N-1)` with each x in `{+1,-1}`, define L, C, and R by the request's formulas, replacing lambda by x. Let H count the ordered positive-positive reflected pairs, and T the ordered mixed-sign pairs. Then, with M=N-1,

`M=R+H+T`, `C=R+H-T`, and `L=H-R`.

The last equality holds because the two orders of each mixed pair cancel in L. Therefore

`4R=M-2L+C`.

The bound `|C|<M` says only that there are both equal-sign and mixed-sign pairs. It does not say whether the equal-sign pairs are positive-positive or negative-negative. For even N, the center has pair-product +1 regardless of its color, so `C>=2-M>-M` already follows from the diagonal pair-product alone. This lower strict bound cannot select a negative center.

### Exact weakened-hypothesis countermodels

These are counterexamples to a sign-pattern proof step, **not to the Liouville target**. Every listed N is even and greater than 2, every word is two-valued, and x_1=+1. The positive indices and reflection sums have exactly the original counting domains.

| Model | N | Word on 1,...,N-1 | L | C | R |
|---|---:|---|---:|---:|---:|
| Arbitrary normalized word | 4 | `+,+,-` | 1 | -1 | 0 |
| `f(n)=(-1)^(v_2(n))` | 6 | `+,-,+,+,+` | 3 | 1 | 0 |
| `f(n)=(-1)^(v_2(n)+v_3(n)+v_5(n))` | 12 | `+,-,-,+,-,+,+,-,+,+,+` | 3 | -5 | 0 |

All satisfy `|C|<N-1` and have no negative-negative reflected pair. The first is the smallest even-N example under just sign normalization. It violates the Liouville value at 2. The second is globally completely multiplicative, has f(1)=1, f(2)=-1, positive squares, and the doubling sign rule, but violates the required prime sign at 3. The third additionally has the correct signs at primes 2,3,5, and still fails the claimed generic implication; it violates the required prime sign at 7 (and at larger primes outside that set).

Thus even some finite Liouville-like constraints plus multiplicativity do not justify the inference. **None satisfies every Liouville defining hypothesis**, so none is presented as an original-target witness. Requiring sign -1 at every prime fixes the actual Liouville function; any purported countermodel meeting that complete requirement must be checked as an actual target counterexample, not passed off as a free sign assignment.

An actual sufficient estimate would need `2L<M+C`. For example `L<=0` together with `C>-M` suffices, but a global bound on L has not been proved here. Average estimates cannot supply these pointwise inequalities without another argument.

### A separate actual-Liouville failure of the proposed universal bound

At N=10 the genuine sign word is

`+,-,-,+,-,+,-,-,+`.

Reflection preserves every sign, hence `C(10)=9`. Its sum is `L(9)=-1`, and R=5, from the ordered pairs

`(2,8),(3,7),(5,5),(7,3),(8,2)`.

Thus `|C(10)|<9` is false even though the target is true. For N=4,6,8 the exact triples `(L,C,R)` are `(-1,-1,1)`, `(-1,-3,1)`, `(-1,-1,2)`, so 10 is the smallest admissible failure of that universal strict bound. This does not rule out a separately justified eventual estimate or a different pointwise lower bound.

## 7. Computation: parameters, resource bounds, code, outputs

All three mathematical Bash invocations had a **30-second timeout**, completed successfully, and created no files. The interpreter identified itself as **Python 3.9.6**. The first full sieve/PB/LS/menu invocation reported about 0.0202 seconds. No timeout was used to close a mathematical branch.

The global value bound was **B=20000**, including every lambda argument. Accordingly PB was tested for q<=10000 and LS-square for m<=10000. The target construction was then checked for every even N<=20000. No lambda values above 20000 were searched.

- PB: at most 128 candidates per prime, at most `1227*128=157056` comparisons; actual 2484. Cap exhaustion would have meant **inconclusive**, not a PB counterexample. There was no cap exhaustion.
- LS-square: at most 99 candidates per eligible m, at most `4952*99=490248` comparisons; actual 6554. This is a bounded square search, not an all-pairs search.
- Divisor menus and target assembly: constant-size tests per target. The only unconstrained partner loops were for the two smallest uncovered seed examples, requiring at most 22 and 58 trials.
- Independent checks: trial-division factorization of the displayed small witnesses, all square shifts at `m=9,21,84,1253,1304`, and the stated constant nonsquare menu through m=10000. These are independent implementations of the sign evaluation, not independent mathematical review.

### Linear-size target assembly, and what it does not prove

For N=2m, a negative-sign m gives the diagonal. Otherwise remove two prime occurrences p,q from m and write `m=dpq`; their product has positive sign, so `lambda(d)=+1`. The PB pair at 2q, scaled by dp when q>=5, supplies a target pair. With the smallest-factor extraction below p<=q, the other cases are `(p,q)=(2,2),(2,3),(3,3)`, using negative core pairs `(3,5),(5,7),(5,13)` and scaling by d.

This is also a direct derivation of the conditional prime-product/PB assembly, rather than an assumption that the unaccepted candidates are true. Checking the final two signs and sum independently against the sieve produced:

```text
assembled targets 9999 range [4, 20000]
counts {'diagonal': 5047, 'small-core': 1881, 'PB-core': 3071}
largest PB q used 4999
```

It does **not** prove the uniform PB premise. The exact target's next untested interval begins at N=20002. Repeatedly enlarging a finite check does not supply the missing uniform proof or a Lean theorem.

### Reproduction code

This consolidates the three actual in-memory invocations; diagnostic formatting is shortened. It uses only integer sieving, bounded loops, trial division, and direct assertions. No all-pairs O(B^2) search is hidden in the target assembly.

```python
from math import isqrt
B, CAP = 20000, 128
spf = list(range(B+1))
for p in range(2, isqrt(B)+1):
    if spf[p] == p:
        for n in range(p*p, B+1, p):
            if spf[n] == n:
                spf[n] = p
f = [0]*(B+1)                 # index zero is never a lambda argument
f[1] = 1
for n in range(2, B+1):
    f[n] = -f[n//spf[n]]
primes = [p for p in range(2, B+1) if spf[p] == p]
A = [a for a in range(1, B+1) if f[a] == 1][:CAP]
pb, unresolved, checks = {}, [], 0
for q in primes:
    if not 5 <= q <= B//2:
        continue
    for a in A:
        if a > q:
            break
        checks += 1
        if f[2*q-a] == 1:
            pb[q] = (a, 2*q-a)
            break
    if q not in pb:
        unresolved.append(q)
print('PB', len(pb)+len(unresolved), checks, unresolved)
maxa = max(a for a,b in pb.values())
print('PB max first', maxa, [(q,*pair) for q,pair in pb.items()
                            if pair[0] == maxa])
three = [q for q in pb if f[q-2] == f[q-3] == 1 and f[2*q-1] == -1]
print('three tests', len(three), three[:10])
ls, failures, checks = {}, [], 0
for m in range(2, B//2+1):
    if f[m] != 1:
        continue
    for u in range(1, isqrt(m-1)+1):
        checks += 1
        if f[m-u*u] == 1 or f[m+u*u] == -1:
            ls[m] = u
            break
    if m not in ls:
        failures.append(m)
print('LS-square', len(ls)+len(failures), checks, failures)
for k in range(1,9):
    missed = [m for m,u in ls.items() if u > k] + failures
    print('square menu', k, len(missed), min(missed) if missed else None)
for S in ([5,7,8,10,12,14,18],
          [5,7,8,10,11,12,13,14,17,18,19,23]):
    missed = [N for N in range(4,B+1,2)
              if f[N//2] != -1 and not any(N%s == 0 for s in S)]
    N = missed[0]
    pair = next((a,N-a) for a in range(1,N//2+1)
                if f[a] == f[N-a] == -1)
    print('seed menu', len(missed), N, pair)
assert not unresolved, 'Capped PB search is inconclusive; do not assemble.'
small = {(2,2):(3,5), (2,3):(5,7), (3,3):(5,13)}
counts = {'diagonal':0, 'small-core':0, 'PB-core':0}
max_q = 0
for N in range(4,B+1,2):
    m = N//2
    if f[m] == -1:
        a = b = m
        counts['diagonal'] += 1
    else:
        p, q = spf[m], spf[m//spf[m]]
        d = m//(p*q)
        assert spf[p] == p and spf[q] == q and m == d*p*q and f[d] == 1
        if q >= 5:
            x,y = pb[q]
            a,b = d*p*x,d*p*y
            counts['PB-core'] += 1
            max_q = max(max_q,q)
        else:
            x,y = small[p,q]
            a,b = d*x,d*y
            counts['small-core'] += 1
    assert 0 < a < N and 0 < b < N and a+b == N and f[a] == f[b] == -1
print('assembled', sum(counts.values()), counts, max_q)

def factors(n):
    out, d = [], 2
    while d*d <= n:
        while n%d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out

def trial(n):
    assert n > 0
    return (-1)**len(factors(n))

def isprime(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))

bad = []
for q in range(5,38):
    if isprime(q):
        pairs = [(1,2*q-1),(4,2*(q-2)),(6,2*(q-3))]
        if not any(trial(a)==trial(b)==1 for a,b in pairs):
            bad.append(q)
print('independent three-test misses through 37', bad)
for m in (9,21,84,1253,1304):
    hit = next((u,trial(m-u*u),trial(m+u*u))
               for u in range(1,isqrt(m-1)+1)
               if trial(m-u*u)==1 or trial(m+u*u)==-1)
    print('trial square', m, factors(m), hit)
for u in range(1,8):
    lo,hi = 1304-u*u,1304+u*u
    print('m1304', u*u, factors(lo), trial(lo), factors(hi), trial(hi))
T = [1,4,6,9,10,14,15,16]
miss = next((m for m in range(2,10001) if trial(m)==1
             and not any(t<m and (trial(m-t)==1 or trial(m+t)==-1)
                         for t in T)), None)
print('constant nonsquare menu first failure through 10000', miss)

def stats(word):
    N = len(word)+1
    L = sum(word)
    C = sum(word[a-1]*word[N-a-1] for a in range(1,N))
    R = sum(word[a-1]==word[N-a-1]==-1 for a in range(1,N))
    assert 4*R == N-1-2*L+C
    return N,L,C,R
print('toy word', stats([1,1,-1]))
for N,S in ((6,{2}),(12,{2,3,5})):
    word = [(-1)**sum(p in S for p in factors(n)) for n in range(1,N)]
    print('multiplicative toy', sorted(S), stats(word))
for N in (4,6,8,10):
    print('actual lambda', stats([trial(n) for n in range(1,N)]))
for a,b in ((2,42),(2,114),(2,1680)):
    assert trial(a) == trial(b) == -1
    print('target witness', a+b, a, factors(a), b, factors(b))
```

Principal actual outputs, omitting the factor table already reproduced above:

```text
PB tested 1227 checks 2484 unresolved []
PB largest minimal first summand 24 attainers [(1213,24,2402),(1787,24,3550)]
three-test failures 156 first [37,59,97,137,163,331,337,353,367,379]
LS-square eligible 4952 checks 6554 failures []
LS-square largest minimal u 7 attainers [(1304,7,1,-1)]
square-menu counts for k=1,...,8: 1217,298,63,18,5,1,0,0
square-menu smallest failures: 9,21,84,84,1253,1304,None,None
S0 uncovered 2137 smallest 44 target witness (2,42)
S1 uncovered 1534 smallest 116 target witness (2,114)
independent trial-division three-test misses for primes [5,37]: [37]
trial square first (u,lower sign,upper sign):
  m=9: (2,-1,-1); m=21: (3,-1,-1); m=84: (5,-1,-1)
  m=1253: (6,-1,-1); m=1304: (7,1,-1)
constant nonsquare menu first failure through 10000: None
normalized toy stats (N,L,C,R): (4,1,-1,0)
multiplicative toy stats: (6,3,1,0), (12,3,-5,0)
actual Liouville stats: (4,-1,-1,1), (6,-1,-3,1), (8,-1,-1,2), (10,-1,9,5)
assembled targets 9999 counts {'diagonal':5047,'small-core':1881,'PB-core':3071}
largest PB q used 4999
```

## 8. Handoff, unresolved checks, and recommended owners

1. **team-lead / regulator routing:** classify q=37 and the square-menu examples as failures of restricted constructions; classify N=10 as a failure of the proposed universal strict absolute-correlation bound; classify artificial words only as failures of an inference from weakened hypotheses. None is an original-target counterexample.
2. **Fresh NL verifier:** verify exact definitions/domains, the finite divisor-seed obstruction, the q=37 minimality audit, the new LS-square square-scaling reduction, and the correlation decomposition/countermodels. The generator and explorer artifacts remain unaccepted inputs, not prior verdicts.
3. **Code executor or fresh arithmetic checker:** reproduce the bounded outputs, preferably with an independent factor-count implementation. The scripts provide evidence paths and finite scopes, not general theorems or formal proof certificates.
4. **Explorer/generator, after routing:** pursue uniform PB with an adaptive construction/full necessary constraints, or LS-square on squarefree positive-sign inputs and odd prime squares. PB's three tests are insufficient; arbitrary positive-sign scaling does not preserve LS-square; no contradiction from the full conditions has been established.
5. **Formal owner, only after review:** the elementary scaling/core interfaces and scoped reductions are potential partial lemmas. This assignment ran no Lean compilation and claims no accepted formal result.

Artifact production is complete. Mathematical acceptance and the original rigorous unconditional Lean proof remain separate, unfinished obligations.

## Delivery status

The required SendMessage handoff to `team-lead` was attempted after saving this report. The runtime rejected it with `Only active team members can send team messages`. No team was created and no retry/poll was made. The report remains saved at its assigned path; the caller must route it for the fresh reviews listed above.
