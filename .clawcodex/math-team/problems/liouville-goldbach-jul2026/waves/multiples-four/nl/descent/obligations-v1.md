# Obligation ledger: ternary gap descent and character rigidity

Mode: CERTIFICATION — candidate production; independent acceptance pending.

## 1. Deliverable, exact claim, and status

Candidate: `W/nl/descent/proof-attempt-v1.md`, where

    W=.clawcodex/math-team/problems/liouville-goldbach-jul2026/waves/multiples-four

Candidate SHA-256:

    23fc6ad19d1c45dd432945aa84756b190700b8c15394b1554ebb3ecaff82235e

Assigned claim: for every prime p>=7 with p=3 modulo 4, positive a,b exist with a+b=4p and lambda(a)=lambda(b)=-1. The candidate supplies FSPD as an intermediate corollary and also gives the full elementary bridge to `HasRepresentation (4*m)` for every m>0.

**Deliverable status:** a complete candidate argument is present, with no intentionally open mathematical step. This is the author's obligation accounting, not an acceptance or a fresh verification. No Lean source was edited or compiled. Mathematical acceptance and subsequent formalization remain leader-owned.

## 2. Input and dependency ledger

| Input | Treatment |
|---|---|
| `W/request.md` | Exact target and witness conventions; unchanged. |
| `W/nl/generator/proof-attempt-v1.md` | Context and prime-core reduction proposal. Its new two-squares proof is not imported. The final scaling bridge is rederived. |
| `W/nl/explorer/residual-v1.md` | Exact FSPD statement and first-split-prime idea. Real-norm and discriminant -24 routes are not dependencies. The proposed small-residue-prime bound is proved locally by a new finite count. |
| `W/nl/ce-hunter/fspd-v1.md` | Exact proposed local identities (R,T). Both are rederived in candidate §2. Neither the finite certificates nor absence of countermodels is a proof premise. |
| `W/nl/ce-hunter/fspd_exact.py` | Inspected only as discovery context. Not executed, certified, or used as a theorem. |
| `P/lean/Statement/Definitions.lean` | The actual lambda and Omega conventions, with Omega counting prime-factor occurrences. |
| `P/lean/Statement/Partial.lean` | Exact `HasRepresentation` interface; `lambda_one`, `lambda_sign`, `lambda_mul`, `lambda_prime`. Positive arguments and primality guards are checked in the candidate. |

All input hashes are recorded in candidate §9. No prior review or verdict was read. No task board, master, shared record, or Lean file was edited. No agents were spawned.

### Load-bearing theorem provenance

1. **Liouville signs and complete multiplicativity.** Exact accepted declarations are quoted with line references in candidate §0. The only required guards are positivity of inputs and primality when using the prime value. Every constructed witness and multiplier is positive. No coprimality guard is needed for complete multiplicativity.
2. **Prime arithmetic.** Prime cancellation comes from prime factorization; existence of a prime divisor is additionally justified by the least-divisor argument. Finite nonzero-residue inverses are derived by the injective-permutation argument. These are not Liouville representation assertions.
3. **Full reflection.** New local derivation in candidate §3. Its preconditions are p odd, 3 not dividing p, f completely multiplicative into signs, f(2)=f(p)=-1, and absence of the target pair. Primality of the assigned p gives the first two requirements; f(3)=-1 is forced rather than assumed.
4. **Character rigidity.** New local proof in candidate §4, using only p odd prime, complete multiplicativity, and full reflection for all 0<n<p. Neither FSPD nor partial character agreement is used. The finite cyclic-gap counting argument is included.
5. **Small quadratic-residue prime.** New local proof in candidate §6, for p>=7 prime and p=3 modulo 4. The exact count gives a square root of every prime divisor of (p+1)/4. Quadratic reciprocity and Euler's criterion are not imported.
6. **The p=1 modulo 4 assembly case.** A finite inverse-pair factorial argument is derived in candidate §8.1. No two-squares theorem or external Wilson theorem is assumed.

There are no external literature theorem applications. The source cutoff <=2026-07-31 therefore introduces no new source eligibility obligation: the argument uses the supplied elementary baseline plus finite mathematics derived in the candidate. No unsupported remembered result is treated as a dependency.

## 3. Mathematical obligation ledger

Every entry marked “supplied” means only that an explicit argument appears at the location stated; it does not mean independently accepted.

| ID | Obligation | Candidate location and status |
|---|---|---|
| O1 | Force f(3)=-1 even when q=2 and negativity at 3 is not initially prescribed. | §1: p+3p=4p; supplied. |
| O2 | Derive (A), (C), and (B) with positive arguments and the correct scaling signs. | §1: scaling by 4 preserves signs, scaling by 2 reverses them; supplied. |
| O3 | Verify f(p+3x)=-f(x) and f(p-x)=-f(x) for 0<3x<p, without assuming full reflection. | §2: two sign cases and the complementary pair 3(p-x),p+3x; supplied. |
| O4 | Under a positive-positive defect x+y=p, exclude 3 dividing either member. | §3.1: if x=3u, the pair 3p-x,p+x has two negative signs; supplied. |
| O5 | Justify the exact divisions (p+x)/3 and (p+y)/3. | §3.2: x,y both nonzero modulo 3 and p nonzero modulo 3 force x=y modulo 3; supplied. |
| O6 | Preserve positivity, total p, and both positive signs under the defect transformation. | §3.2: (C) gives negative numerators and f(3)=-1 changes the quotient signs to positive; supplied. |
| O7 | Exhibit a strictly decreasing positive integer parameter, not an unbounded reflection chain. | §3.3: delta=y-x, ordered with x<y; the new gap is delta/3. Odd p excludes zero initial or new gap; supplied. |
| O8 | Obtain full reflection, including the formerly unresolved middle third. | §§1,3: negative-negative pairs are excluded by (A), positive-positive pairs by O4–O7; supplied. |
| O9 | Define F on nonzero residue classes without presuming periodicity of f. | §4.1: unique representatives 1,...,p-1; full reflection gives oddness; supplied. |
| O10 | Prove closure of good multipliers and goodness of -1. | §4.1: explicit identities from the definition and reflection; supplied. |
| O11 | For the least bad representative n and arbitrary nonzero z, find a smaller signed multiplier k and a small positive residue d. | §4.2: n cyclic gaps among 0,z,...,(n-1)z; 0<abs(k)<n, kz=d mod p, 1<=d<p/n; supplied. |
| O12 | Avoid using unproved multiplicativity of F at a product that crosses p. | §4.3: ordinary f multiplicativity is used only on nd<p. All remaining multiplications are by the already-good k; supplied. |
| O13 | Deduce full multiplicativity and identify the nonzero squares precisely as the positive values. | §§4.3–4.4: least-bad contradiction, then square count and oddness count; supplied. |
| O14 | Produce a prime quadratic residue strictly below p uniformly, not from a finite test. | §6: choose a prime divisor r of t=(p+1)/4 and prove r is a square modulo p; supplied. |
| O15 | Prove the least-absolute-residue product identity and compute its negative count parity. | §6: absolute values permute 1,...,h; E has parity of an explicitly evaluated floor sum; supplied. |
| O16 | Convert the congruence r^h=1 to an actual nonzero square root of r. | §6: A=r^t and 2t=h+1 yield A^2=r modulo p; supplied. No separate square-test theorem is used. |
| O17 | Establish existence and bound for the globally least split prime q. | §6: a finite nonempty qualifying set contains r<=t; its minimum is globally least and q<=t<p; supplied. |
| O18 | Check every FSPD assumption and derive its conclusion without treating FSPD as a premise. | §7: q>=2 gives f(2)=-1; q<p and chi(q)=1 contradict f(q)=-1 under missing-pair rigidity; supplied. |
| O19 | Substitute lambda under exactly the accepted assumptions. | §7 and baseline declarations in §0; supplied. |
| O20 | Finish the optional all-m T4 bridge without importing unreviewed norm or two-squares claims. | §8: p=3 seed, p=1 mod 4 inverse-pair argument, sign cases and prime-divisor scaling; supplied. |

## 4. Exact descent domains and division audit

### First descent: defect gap

Input: a defect with x,y positive, x+y=p, f(x)=f(y)=1. The prime p is odd and different from 3.

- Orientation and parameter: exchange the entries so x<y; delta=y-x is a positive integer.
- Divisibility exclusion: 3 dividing either entry produces an actual forbidden pair of total 4p, not a formal sign contradiction outside the permitted interval.
- Divisions: after the exclusion, x,y have the same nonzero residue modulo 3. This proves both 3 divides p+x and 3 divides p+y before quotients are used.
- New arguments: x'=(p+x)/3 and y'=(p+y)/3 are positive integers; their sum is p, so each is less than p.
- New signs: (C) at y and x, respectively, gives f(p+x)=f(p+y)=-1; division by 3 is justified through complete multiplicativity and f(3)=-1.
- Strict descent: y'-x'=delta/3 is a positive integer smaller than delta. No positivity, integrality, or endpoint condition is deferred.

### Second minimum argument: least bad residue multiplier

Input: full reflection on every 1,...,p-1, with p odd prime.

- Parameter: the least representative n in {1,...,p-1} that is not good. Since 1 is good, 2<=n<p.
- Smaller objects: every signed integer k with 0<abs(k)<n is good, using the already-proved closure with -1.
- Counting domain: precisely n distinct residues 0,z,...,(n-1)z. Circular gaps are positive integers and sum to p.
- Strict size bound: p/n is not an integer since p is prime and 1<n<p. A minimum gap d satisfies 1<=d<p/n.
- Index difference: ordinary and wrapping gaps both have d=kz modulo p for nonzero k with abs(k)<n.
- Critical ordinary product: 0<nd<p, so f(nd)=f(n)f(d) translates to F without any periodicity assumption.
- Cancellation: F(k) is a sign and hence nonzero; its cancellation shows that n is good for arbitrary z.

This is a global compatibility argument on all nonzero residues. It does not assert agreement merely on a pair of windows, and does not posit that a reflection or division automatically reduces q.

## 5. Relation to the proposed FSPD route

The literal attempt to push the discrepancy at q directly through one-sided reflections is replaced by two justified finite steps:

1. remove the only possible obstruction to exact reflection by descending the gap of a positive-positive pair;
2. extend exact reflection and ordinary multiplicativity to multiplicativity modulo p by a least-bad-multiplier argument.

Once those steps hold, any negative-valued quadratic residue below p is forbidden. The first split prime supplies just such a residue. No negativity assumption at primes between 2 and q is used in §§1–5; those extra FSPD hypotheses are harmless and ensure in particular the required negativity at q. No countermodel search result is needed.

Thus this candidate does not abandon FSPD as too strong and does not infer impossibility from a failed route. It claims a local proof of a stronger missing-pair classification, with FSPD as a consequence. This claim is pending fresh review.

## 6. Unresolved issues, review focus, and next action

### Mathematical gap accounting

No unresolved mathematical step is knowingly retained in the candidate. All constructions, quotient integrality checks, strict bounds, sign case splits, and assembly bridges are explicitly supplied. This accounting is not a guarantee that a fresh verifier will find no error.

### Acceptance and formalization still outstanding

- Independent review of the new full-reflection descent, particularly the forced signs of 3p-x and p+x in §3.1.
- Independent review of the residue-multiplier minimum argument, particularly the wrapping cyclic gap and the fact that nd<p is the only use of local f multiplicativity in §4.3.
- Independent review of the floor-count parity and explicit square root in §6.
- Independent confirmation of FSPD and lambda substitution and the optional T4 assembly.
- No new Lean implementation, pinned compilation, or kernel/axiom check has been attempted. Those are separate future tasks, not silently counted as completed.

**Next action:** team-lead should dispatch this candidate and ledger to a fresh mathematical verifier, without treating the author's “supplied” labels as acceptance. If the three critical bridges pass, route the exact candidate statements for formalization. If a break point is found, preserve this v1 and request a new repair artifact identifying that precise point.
