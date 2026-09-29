Mode: DISCOVERY — conjectural; no proof weight.

# Elementary route exploration, attempt v1

## Scope and provenance

- Exact target: for every even integer `N > 2`, there are positive integers `a,b` with `a+b=N` and `lambda(a)=lambda(b)=-1`. Equality `a=b` is allowed. Here `lambda(n)=(-1)^Omega(n)`, with prime factors counted with multiplicity and `Omega(1)=0`.
- Read the assigned `request.md` and math-team protocol. This is an explorer's candidate report, not the canonical decomposition, a review, or a Lean result.
- No external browsing, external theorem, or remembered literature result was used. The offered Mangerel PDF was not needed or read. Thus no external version enters these candidates. Arithmetic infrastructure still needs project-local justification and eligible Lean dependencies.
- **Every deduction and proposed lemma below is new, unreviewed material.** Arguments are supplied for review; none is marked accepted or verified.
- Four inexpensive Python invocations used only in-memory tables through 2000. Their bounded observations have no proof weight. No other artifact was written.

## Common definitions and elementary dependency

For `s` in `{+1,-1}`, write

`P_s(n) := there exist positive x,y with x+y=n and lambda(x)=lambda(y)=s`.

Write `B(n) := P_-(n) and P_+(n)` for a double-sign seed.

**Candidate arithmetic dependency M.** For positive `u,v`,

`Omega(uv)=Omega(u)+Omega(v)`, hence `lambda(uv)=lambda(u)lambda(v)`.

Local rationale: concatenate a prime-factor list for `u` and one for `v`. This is a prime-factor list for `uv`, and its length is the sum of their lengths. The definition by multiplicity makes its length `Omega(uv)`; well-definedness is the ordinary unique-factorization infrastructure underlying this definition. Then use `(-1)^(r+s)=(-1)^r(-1)^s`. The empty list gives `lambda(1)=1`; a prime has sign `-1`; a square has sign `+1`. No coprimality assumption belongs in M. In particular, `lambda(2u)=-lambda(u)`.

The Lean obligation is to connect the project's actual `Omega` definition to this factor-list or valuation argument, not silently substitute a count of distinct primes.

**Candidate scaling lemma S.** If `P_s(n)` and `d>0`, then `P_(lambda(d)s)(dn)`, witnessed by `dx,dy`. Both summands stay positive. This lemma needs M and no primality condition on `d`.

# Route 1 — sign-adaptive finite seeds and divisor covering

## Mechanism and concrete seeds

If `B(s)` and `N=ds` with `d>0`, choose the negative seed pair when `lambda(d)=+1`, and the positive seed pair when `lambda(d)=-1`. S then gives `P_-(N)`.

The following are explicit candidate double-sign seeds; checking their signs requires only M and the displayed small factorizations.

| Seed `s` | Negative pair | Positive pair |
|---|---|---|
| 5 | 2+3 | 1+4 |
| 7 | 2+5 | 1+6 |
| 8 | 3+5 | 4+4 |
| 10 | 5+5 | 1+9 |
| 12 | 5+7 | 6+6 |
| 14 | 3+11 | 4+10 |
| 18 | 5+13 | 9+9 |

For example, the proposed `N=8m` mechanism is exactly: use `3m+5m` when `lambda(m)=+1`, and `4m+4m` when `lambda(m)=-1`. The odd seeds 5 and 7 are useful additions: every even multiple of either is covered too. The target does not require seed summands, or final summands, to be odd or coprime.

## Exact limitation of a finite divisor-seed scheme

Consider any fixed finite list of positive integer seeds, with any fixed list of their positive representations. Allow arbitrary common scaling and either multiplier sign. This restricted method cannot cover all even targets, even after adding the diagonal construction below.

Choose a prime `p` larger than every seed and larger than 2. For `N=2p^2`, the only seed sizes at most that bound that can divide `N` are 1 and 2. Size 1 has no positive split. Size 2 has only `1+1`, with two positive signs; its multiplier is `p^2`, also of positive sign. Thus this representation cannot produce two negative signs. The diagonal `p^2+p^2` also has two positive signs. The same obstruction works for `2pq` with both primes beyond the seed bound.

This is a structural obstruction to **fixed seed size plus common scaling**, not a counterexample to the target and not a prohibition on finite families of more general parameter-dependent formulas. Arbitrarily large primes, if needed to make the limitation an infinite-family statement, have the elementary product-plus-one argument: a prime divisor of one plus the product of all primes up to a bound exceeds that bound.

### Important correction about `2p`

A finite list of double-sign seeds generally does leave the numbers `2p` with large prime `p` outside its divisor cover. But these are **not unresolved target cases**: `p+p` already has two negative signs. Equivalently, the positive seed `1+1=2`, scaled by the negative-sign multiplier `p`, works.

After that diagonal is allowed, `2p^2` and more generally `2pq`, not `2p`, are the natural surviving families.

## Dependencies, blocker, difference

- Dependencies: M, S, finite explicit sign checks, positivity.
- Contribution: unconditional-looking elementary coverage of many infinite divisibility classes, pending review/formalization.
- Global blocker: the finite divisor-cover obstruction above. Merely adding more constant seeds cannot eliminate it.
- Difference from the supplied seed: adds odd seeds, allows arbitrary seed signs, and identifies the precise failure of this entire restricted covering mechanism.

# Route 2 — minimal counterexamples and reduction to prime-product cores

## Candidate reduction C: exact prime-product core

The original target would be equivalent to the following smaller indexed family:

> For all primes `p,q`, including `p=q`, `P_-(2pq)`.

The forward direction simply instantiates the original target. Here is a candidate reverse argument.

Write an arbitrary admissible target as `N=2m`, where `m>1`.

1. If `lambda(m)=-1`, use `m+m`.
2. Otherwise `Omega(m)` is a positive even integer, hence at least 2. Select two prime-factor occurrences `p,q` from a factorization of `m`; they may be the same prime. Write `m=dpq`. The remaining number of prime factors is even, so `lambda(d)=+1`.
3. A negative representation of `2pq`, scaled by this positive-sign `d`, gives one of `2m`.

This does not impose squarefreeness or distinctness. Conversely, if `N` is a smallest counterexample, the same argument forces `N=2pq`: if more than two prime factors remained in `m`, then `d>1` and `2pq<N` would be a smaller even target. Thus the square-removal observations are subsumed by the sharper core reduction.

This is more than removing square factors: it also removes any even number of prime-factor occurrences. It does not prove the remaining prime-product family.

## Candidate bridge PB: a variable, prime-indexed positive seed

A sufficient new lemma is

> **PB.** For every prime `q>=5`, there exist positive `u,v` such that `u+v=2q` and `lambda(u)=lambda(v)=+1`.

Assembly idea: given a core `2pq`, if `q>=5`, scale PB's pair by the prime `p`, whose sign is negative. If only the other prime is at least 5, exchange their names. When both primes belong to `{2,3}`, the core is 8, 12, or 18, covered by the explicit negative seed pairs above.

PB is only a proposed sufficient lemma. It is **not** supplied by the original target at `2q`, since the target gives the opposite sign there. I have not established that PB is necessary for the original target.

An even more restrictive sufficient lemma would be

> For every prime `q>=5`, `P_-(q)`.

Doubling such a pair gives PB. This odd-prime lemma does not demand that either summand itself be prime, but it does add a new odd-target assertion. It should not be silently identified with the original problem.

## Exact necessary constraints on a failed core

If `P_-(2pq)` fails, scaling gives all of the following:

- `P_+(2p)` fails, since a positive pair at `2p` could be scaled by the negative-sign prime `q`.
- Likewise `P_+(2q)` fails.
- `P_-(p)` and `P_-(q)` fail: scaling by `2q` or `2p`, respectively, preserves a negative sign because those multipliers have positive sign.
- `P_+(pq)` fails, since doubling a positive pair would solve the core.

For a prime factor `r>=5`, three consequences are

`lambda(r-2)=+1`, `lambda(r-3)=+1`, and `lambda(2r-1)=-1`.

The first two follow from the missing negative representation of `r`, using the negative numbers 2 and 3. The third follows from the missing positive representation of `2r`, using `lambda(1)=+1`.

These three constraints alone do not contradict primality. For example, `r=59` satisfies them:

- `57=3*19` has positive sign;
- `56=2^3*7` has positive sign;
- `117=3^2*13` has negative sign.

Nevertheless `59=7+52` has two negative signs, and its doubled pair `118=14+104` has two positive signs. Thus reducing the failure conditions to just these first few shifts loses essential information.

## Dependencies, blocker, difference

- Dependencies: M/S, existence of a prime-factor list, parity of its length; no external analytic theorem.
- Contribution: a sharp candidate reduction of all even targets to `2pq`, and a concrete one-prime sufficient bridge.
- Global blocker: a uniform proof of PB or a different construction on every core. Bounded searches of PB cannot fill that obligation.
- Difference from Route 1: seed size is now variable and indexed by a prime; the factorization argument explains why such a variable family would suffice. It is not a larger finite divisor list.

# Route 3 — reflection/doubling and local sign certificates

This route does not start by factoring `N`. It studies the consequences of a hypothetical missing representation at `N=2m`.

## Forced signs under failure

If `P_-(2m)` fails, then:

1. `lambda(m)=+1`, because the center pair would otherwise solve the target.
2. `P_+(m)` fails, since doubling a positive pair gives a negative pair at `2m`.
3. For every `t` with `1<=t<m` and `lambda(t)=+1`, necessarily

   `lambda(m-t)=-1` and `lambda(m+t)=+1`.

For the first sign in (3), a positive `lambda(m-t)` would give a positive pair at `m`. For the second, the already negative `m-t` is reflected across `m` to `m+t`; these cannot both be negative.

These implications use exact domains: `m-t` must be positive; no value at zero or a negative integer is introduced. They are implications only. Failure does **not** mean all reflected pairs have opposite signs: positive-positive pairs are allowed, and the center is necessarily one.

## Candidate local-shift lemma LS

A sufficient new lemma is:

> For every `m>1` with `lambda(m)=+1`, there is a positive integer `t<m` such that `lambda(t)=+1` and at least one of
> `lambda(m-t)=+1` or `lambda(m+t)=-1` holds.

This yields explicit witnesses rather than just a contradiction:

- If `lambda(m-t)=+1`, use `2t+2(m-t)=2m`; both signs flip to negative.
- Otherwise `lambda(m-t)=-1`, and the alternative gives the negative pair `(m-t)+(m+t)=2m`.

A more restrictive construction-first candidate is **LS-square**: take `t=u^2`, with `u>=1` and `u^2<m`. Its exact required statement is

> For every `m>1` with `lambda(m)=+1`, some positive square `t<m` satisfies `lambda(m-t)=+1` or `lambda(m+t)=-1`.

Here `lambda(t)=+1` is automatic. This would restrict the witness shape: either one summand is twice a square, or the two summands have half-difference a square. It is an unproved sufficient condition, not a rephrasing known to be equivalent to the target.

A fixed tiny square menu already fails. For `m=84`, all of `t=1,4,9,16` have the forbidden pattern `(-,+)` at `(m-t,m+t)`:

- `(83,85)`, with `85=5*17`;
- `(80,88)`, with `80=2^4*5`, `88=2^3*11`;
- `(75,93)`, with `75=3*5^2`, `93=3*31`;
- `(68,100)`, with `68=2^2*17`, `100=2^2*5^2`.

But `t=25` gives `(59,109)`, a negative pair summing to 168. This refutes the four-square template, not LS-square.

## A possible certificate search, and its precise missing step

For fixed `m`, encode labels `x_n=lambda(n)` with values in `{+1,-1}`; impose multiplicative relations, known prime/square signs, and the hypothetical clauses excluding negative pairs at `2m`. One can seek a small inconsistent subsystem that produces an LS-type witness.

For a genuinely uniform proof, the subsystem must instead use integer expressions in `m`, verified positive on explicit ranges, together with symbolic product identities and an exhaustive collection of congruence/range cases. Factoring each individual number through a numerical bound gives only finite verification. It does not provide that uniform subsystem or an effective final coverage threshold.

A useful next search target is a product identity connecting several of `m-u^2` and `m+u^2` which makes the forced pattern `(-,+)` impossible. No such identity or exhaustive parameterization was found here. No average or individual sign assertion has been substituted for the simultaneous condition.

## Counting guardrail for sign-symmetry arguments

Let `L(x)=sum_{1<=n<=x} lambda(n)`. Absence of a negative pair at `2m` implies

`L(2m-1)>=1` and `L(m-1)<=0`.

For the first, reflection `a -> 2m-a` injects negative entries into positive entries, and the positive center leaves at least one extra positive. For the second, absence of a positive pair at `m` injects positive entries in `[1,m-1]` into negative entries there.

Consequently, a proof that `L(2m-1)<=0` for every `m>=2` would suffice, but no such assertion is proved or imported here. The short bounded experiment below cannot justify it. In particular, an average sign estimate, or the observation that negation swaps the two colors, does not supply a pointwise reflected-pair argument. This is a limitation check, not an attempt to repair the leader's correlation decomposition.

## Dependencies, blocker, difference

- Dependencies: only M's doubling case, exact two-valued signs, reflection, positivity.
- Contribution: explicit witness-producing local certificates and strong necessary constraints on any counterexample, independent of prime-core reduction.
- Global blocker: LS/LS-square requires simultaneous control of two shifted values for every positive-sign `m`. No uniform proof was obtained.
- Difference from Routes 1–2: additive shifts and reflected signs replace divisibility and a variable prime seed.

# Bounded experiments and actual falsifications

All runs used Python integer arithmetic and an `Omega` sieve through **2000**, followed by direct searches over `1<=a<=floor(n/2)`. They are exploratory observations, not certification of even their finite range.

1. For `2<=n<=2000`, the only missing negative representations found were `n=2,3`. The only missing positive representations found were `n=3,4,6,9`.
2. For every prime `5<=q<=1000`, a positive representation of `2q` was found. This tests PB only in that finite scope.
3. Using double-sign seeds
   `S={5,7,8,10,11,12,13,14,17,18,19,23}`
   and the diagonal criterion `lambda(N/2)=-1`, **147** even targets `4<=N<=2000` remained outside this construction. The first ten were
   `116,124,148,164,172,174,186,188,212,222`.
   Within this small range all 147 happened to be prime-product cores; this coincidence is not asserted globally. For example, `116=2*2*29` is nevertheless solved by `2+114`.
4. The fixed negative partner set `{2,3,5,7,8,11}` failed to furnish a pair at exactly these even targets in `14<=N<=2000`:
   `98,540,1210,1654,1856,1946,1964,1974`.
   The first is an explicit falsification of that proposed fixed-partner cover: the complements `96,95,93,91,90,87` all have positive sign. The actual pair `98=18+80` has two negative signs.
5. LS and LS-square had no failures for `2<=m<=1000` with `lambda(m)=+1`. The square menus `{1}`, `{1,4}`, `{1,4,9}`, `{1,4,9,16}` had respectively 120, 29, 8, and 2 failures in this same scope. The last two half-targets were 84 and 326. A larger nonsquare-inclusive menu `{1,4,6,9,10,14,15,16}` had no failures in this scope, which is not evidence of universal coverage beyond the finite check.
6. All odd prefixes `3<=x<=1999` had `L(x)<=-1` in the run. This is only a bounded observation; no global sign conclusion follows.

## Reproduction core

The four actual invocations used the same sieve and the following searches, split into separate small runs. This combined snippet reproduces the recorded scopes and counts without creating files:

```python
from math import isqrt
B = 2000
om = [0] * (B + 1)
primes = []
for p in range(2, B + 1):
    if om[p] == 0:
        primes.append(p)
        power = p
        while power <= B:
            for n in range(power, B + 1, power):
                om[n] += 1
            power *= p
f = [(-1) ** e for e in om]  # index 0 is unused

def rep(n, s):
    return next(((a, n-a) for a in range(1, n//2+1)
                 if f[a] == s and f[n-a] == s), None)

print('minus misses', [n for n in range(2, B+1) if rep(n, -1) is None])
print('plus misses', [n for n in range(2, B+1) if rep(n, 1) is None])
print('PB misses', [p for p in primes if 5 <= p <= 1000
                    and rep(2*p, 1) is None])
S = [5,7,8,10,11,12,13,14,17,18,19,23]
print('seed witnesses', [(s, rep(s,-1), rep(s,1)) for s in S])
def covered(n):
    return f[n//2] == -1 or any(n % s == 0 for s in S)
residual = [n for n in range(4, B+1, 2) if not covered(n)]
cores = sorted({2*p*q for i,p in enumerate(primes)
                for q in primes[i:] if 2*p*q <= B
                and not covered(2*p*q)})
print('residual', len(residual), residual[:40])
print('residual equals uncovered cores in scope', residual == cores)
K = [2,3,5,7,8,11]
print('fixed-partner misses', [n for n in range(14, B+1, 2)
      if not any(k < n and f[n-k] == -1 for k in K)])

def cert(m, t):
    return 1 <= t < m and f[t] == 1 and (f[m-t] == 1 or f[m+t] == -1)
ms = [m for m in range(2, 1001) if f[m] == 1]
print('LS misses', [m for m in ms if not any(cert(m,t) for t in range(1,m))])
print('LS-square misses', [m for m in ms if not any(cert(m,u*u)
                           for u in range(1,isqrt(m-1)+1))])
for T in ([1], [1,4], [1,4,9], [1,4,9,16], [1,4,6,9,10,14,15,16]):
    misses = [m for m in ms if not any(cert(m,t) for t in T)]
    print('menu', T, 'misses', len(misses), misses)
print('max odd-prefix L', max(sum(f[1:x+1]) for x in range(3,B,2)))
```

# Ranked next actions

1. **Highest feasibility; substantial partial contribution:** independently review and then formalize M, S, the explicit seeds, and candidate core reduction C. This yields usable infinite families and isolates an exact remaining family without asserting a solution. The finite divisor-cover obstruction should prevent spending the main budget merely enlarging a fixed seed table.
2. **Most focused proposed global bridge:** investigate PB for every prime `q>=5`, not just prime values in a table. Try explicit constructions or a uniform contradiction certificate for the simultaneous necessary constraints. The weaker three-shift test already survives at 59, so it is not sufficient. The odd-prime negative-sum assertion is a stronger alternative, not an established dependency.
3. **Genuinely different exploratory branch:** investigate LS-square via symbolic product identities or adaptive square shifts. The four-square template is concretely refuted, while the all-square statement remains an unproved candidate. Any substantial certificate search or wider computation should be assigned by the leader to the code executor with bounds and an explicit symbolic/generalization objective.

No route here closes the universal target. The remaining obligations are the stated global bridge/shift lemmas (or a different construction), independent mathematical review, eligible arithmetic infrastructure, and all required Lean checks. No assertion about the target's global literature status is made.
