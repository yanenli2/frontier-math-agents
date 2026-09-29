Mode: DISCOVERY — conjectural; no proof weight.

# FSPD countermodel analysis: bounded exclusion and partial exact rigidity

## 1. Accepted definitions, hypotheses, and scope

The original target in `../../request.md` is representation of every positive multiple of four as a sum of two positive integers of Liouville value -1. Here lambda(n)=(-1)^Omega(n), with prime factors counted with multiplicity. Equal summands are allowed. This report investigates only the stronger, unproved FSPD in `../explorer/residual-v1.md`, section 3; it neither changes nor certifies the original target.

**FSPD, exactly as investigated.**

1. p is a prime, p>=7, and p=3 modulo 4.
2. For integers not divisible by p, chi_p(n) is +1 for a nonzero quadratic residue modulo p, and -1 otherwise. At multiples of p the Legendre symbol is 0.
3. q is the least prime r with chi_p(r)=+1; in particular q is not p.
4. f maps the positive integers to {+1,-1} and is completely multiplicative: f(ab)=f(a)f(b) for all positive a,b.
5. f(p)=-1 and f(r)=-1 for every prime r<=q. Every other prime sign is unrestricted.
6. The asserted conclusion is existence of positive a,b with a+b=4p and f(a)=f(b)=-1.

Consequences used below: f(1)=+1, f(t^2)=+1, and f(2)=-1 because q>=2. No value at zero is used. A countermodel would have to avoid every pair a,4p-a for 1<=a<=2p, including the equal pair. Assigning all prime signs through 4p suffices: signs at larger primes can be chosen arbitrarily and extended by prime factorization.

**Outcome.** No FSPD countermodel was found. Exact constraint propagation reported inconsistency for every prime p=19 modulo 24 below 500 (eleven primes, listed below). More usefully, a new candidate local derivation gives two exact identities under the missing-pair assumption:

    f(p-x) = -f(x),
    f(p+3x) = -f(x) = f(3x),       0 < 3x < p.             (R,T)

These are partial rigidity statements, not full reflection rigidity and not a proof of FSPD. They have derivations below and require fresh mathematical verification. No genuinely fatal gap to applying FSPD to lambda was identified.

## 2. Structural candidate: exact outer-third reflection and ternary translation

This derivation does not use primality, congruences, or quadratic reciprocity. Its initial hypotheses are a positive integer p, complete multiplicativity into {+1,-1}, f(2)=f(p)=-1, and absence of a negative-negative pair summing to 4p. Thus all its hypotheses follow from a hypothetical FSPD countermodel.

### 2.1 Necessary preliminary signs and reflections

The pair p+3p=4p forces f(3p)=+1 because f(p)=-1. Hence f(3)=-1. This also covers FSPD's q=2 case, where negativity at 3 is not initially prescribed.

For 0<u<p, the pair 4u+4(p-u)=4p gives

    f(u)=-1  ==>  f(p-u)=+1.                              (A)

For 0<v<2p, the pair 2v+2(2p-v)=4p gives

    f(v)=+1  ==>  f(2p-v)=-1.                             (C)

Combining (A) with (C), using v=p-u, gives the supplied one-sided implication

    f(u)=-1  ==>  f(p+u)=-1,       0<u<p.                 (B)

Every argument in these applications is strictly positive and each displayed pair has total 4p.

### 2.2 Exact ternary translation

Fix an integer x with 0<3x<p.

* If f(x)=-1, (A) gives f(p-x)=+1. Consequently f(3(p-x))=-1. Its complementary summand p+3x must be positive-sign, since

      3(p-x)+(p+3x)=4p.

  Thus f(p+3x)=+1=-f(x).

* If f(x)=+1, then f(3x)=-1. Apply (B) with u=3x, whose required range is exactly 0<3x<p. It gives f(p+3x)=-1=-f(x).

Therefore (T) holds, with no assumption about an exact reflection law.

### 2.3 Exact outer-third reflection

Negative-negative signs at x,p-x are excluded by (A). If instead both signs were positive, (T) would give f(p+3x)=-1, while complete multiplicativity would give f(3(p-x))=-1. The preceding complementary pair would contradict the missing-pair assumption. The only remaining sign patterns are opposite signs, proving the candidate identity (R).

By symmetry, (R) also holds when 0<p-x<p/3. At a possible integral boundary 3x=p, it holds directly because p-x=2x and f(2)=-1. This boundary does not occur for the FSPD primes p>=7. Thus any still-possible positive-positive pair at total p must have both entries strictly inside (p/3,2p/3).

**What this changes.** Section 3.2 correctly warns that absence alone does not immediately give a full reflection-product identity. The derivation above supplies that identity on the outer thirds, and the additional exact translation (T), using the forced sign f(3)=-1. It does not justify importing an argument requiring reflection on all of 1,...,p-1.

**Possible next descent interface, not a completed descent.** Using the explorer's bound q<=(p+1)/4 gives 3q<p for p>3. Consequently a hypothetical FSPD countermodel must satisfy

    f(p-q)=+1,   f(p+3q)=+1.

For n<q, every prime factor is below q, so f(n)=chi_p(n). Identity (R) then also supplies character agreement at p-n, for 1<=n<q, because chi_p(-1)=-1. The small initial agreement window therefore has a reflected agreement window; the discrepancy at q forces discrepancies at specific translates. No integer descent from these windows is supplied. This paragraph uses the explorer's general bound and elementary character facts; the derivations of (R,T) themselves do not depend on that bound or any external source.

## 3. Bounded exact search: scope and exhaustiveness

No Liouville or Q(p) sample was run. Each prime r<=4p has a Boolean variable e_r, representing f(r)=(-1)^e_r. For n<=4p, let V(n) contain the prime-exponent parities from exact trial factorization. Then

    f(n)=(-1)^(V(n) dot e).

Each pair contributes precisely the clause

    NOT((V(a) dot e)=1 AND (V(4p-a) dot e)=1).

The solver maintains linear equations over F_2 and reduces the two endpoint forms. A known negative endpoint forces its partner positive. Identical reduced endpoints force that common sign positive; opposite endpoints make the clause automatic. Repeated propagation either produces a contradiction or leaves clauses for an exhaustive binary split A=0 versus A=1,B=0. Each actual FSPD run contradicted at its initial node, so **no branching, sampling, or free-variable default was used to infer inconsistency**. A contradiction under the fixed equations eliminates every assignment of the remaining prime bits, conditional on the implementation's correctness.

Primality uses trial division through the integer square root. Quadratic residues are obtained by the finite set of modular squares, not reciprocity. The q values below are tested against every smaller prime. All eleven listed p are precisely the primes in the requested congruence class below 500.

| p | q | Initially unrestricted prime signs <=4p | Result | Search nodes |
|---:|---:|---:|---|---:|
| 19 | 5 | 17 | inconsistent | 1 |
| 43 | 11 | 33 | inconsistent | 1 |
| 67 | 17 | 48 | inconsistent | 1 |
| 139 | 5 | 97 | inconsistent | 1 |
| 163 | 41 | 104 | inconsistent | 1 |
| 211 | 5 | 142 | inconsistent | 1 |
| 283 | 7 | 184 | inconsistent | 1 |
| 307 | 7 | 195 | inconsistent | 1 |
| 331 | 5 | 212 | inconsistent | 1 |
| 379 | 5 | 236 | inconsistent | 1 |
| 499 | 5 | 297 | inconsistent | 1 |

The two invocations recorded approximately 0.0061 and 0.0525 seconds, respectively. Each had an 80-second global deadline and a 30,000-node per-run cap; all loops have explicit finite bounds. Actual computation was far below the two-minute aggregate allowance. No cap was reached. The largest system had 301 prime variables.

The script also ran a small decoder/control test at p=19, with only f(2)=f(19)=-1 prescribed; the second invocation repeated this control. It returned a missing-pair assignment with f(5)=+1. This is explicitly **not an FSPD witness**, since q=5. The finite negative-prime set in that control is {2,3,13,19,29,31,37}, with all other primes <=76 positive. Multiplication of the prime signs independently checks every complementary pair. Its only relevance is distinguishing a genuine arbitrary-sign model from the stronger FSPD constraints; no conclusion about lambda follows.

**Limit of inference.** This is bounded computational evidence, not a uniform proof. No model was found for the stated eleven primes; nothing was searched above 499 or outside this residual class, apart from the control at 19. If another bounded countermodel run is authorized, the next numerical scope is 500<p<=1000, p=19 modulo 24, with a fresh aggregate cap. Mathematical review of (R,T) is the preferred next action instead of merely enlarging the sample.

## 4. Hand-checkable certificates for the first four requested cases

These local certificates are independent of the Gaussian elimination code and use only signs forced by the relevant FSPD hypotheses. They do not require signs at larger primes to equal Liouville signs.

The q values are 5,11,17,5 for p=19,43,67,139. Square roots of q modulo p are respectively 9,21,33,12. Direct modular squaring in the script verifies that all preceding primes are nonresidues. Primality of each p and q is tested by trial division.

* **p=19, q=5.** If f(7)=+1, use 76=20+56: 20=4*5 and 56=8*7 are both negative-sign. If f(7)=-1, use 76=28+48: 28=4*7 and 48=16*3 are both negative-sign. This exhausts the unrestricted sign at 7.

* **p=43, q=11.** Use 172=44+128. Here 44=4*11 and 128=2^7 both have sign -1.

* **p=67, q=17.** Use 268=68+200. Here 68=4*17 and 200=2^3*5^2 both have sign -1.

* **p=139, q=5.** The following is an exhaustive decision tree:
  1. If f(17)=+1, use 556=12+544, with 12=4*3 and 544=2^5*17.
  2. Otherwise f(17)=-1. If f(11)=-1, use 556=17+539, with 539=7^2*11.
  3. Otherwise f(11)=+1. If f(7)=-1, use 556=28+528, with 28=4*7 and 528=2^4*3*11.
  4. Otherwise f(7)=+1. Use 556=56+500, with 56=2^3*7 and 500=2^2*5^3.

Every displayed summand is positive, every sum is exactly 4p, and each terminal branch has both signs negative. These examples are finite certificates, not a claim that their particular constructions extend uniformly.

## 5. Applicability audit, obstruction status, and unresolved checks

* **No candidate FSPD countermodel:** there is no witness satisfying all original hypotheses and failing its conclusion in this report. The control assignment fails f(q)=-1 and must not be routed as a refutation.
* **No fatal application gap identified:** lambda on positive integers is completely multiplicative, takes values in {+1,-1}, and equals -1 at every prime. Consequently, if FSPD is proved, substituting lambda satisfies all of its sign hypotheses. A countermodel to FSPD, if later found, would concern the stronger route, not T4 or actual lambda.
* **Conventions:** complete multiplicativity is essential, not just multiplicativity on coprime inputs. The Legendre-symbol argument order is (r/p). No summand may be zero. Equal summands are included; here f(2p)=f(2)f(p)=+1, so the equal pair cannot itself witness the conclusion.
* **Unresolved:** uniform FSPD; a descent using the first-split condition; full reflection on the middle third; independent verification of the new local derivations and implementation. No timeout, failed proof route, or absence of a witness closes any of these obligations.
* **Recommended next owner:** team-lead should route (R,T) to a fresh mathematical verifier/regulator first, and then return accepted identities, if any, to the descent explorer. A separate code reviewer can check the finite propagation traces. This author assigns no mathematical acceptance status.

## 6. Evidence paths, reproduction, and identities

Owned artifacts, all under the assigned `W/nl/ce-hunter/`:

* `fspd-v1.md` — this report.
* `fspd_exact.py` — the only durable script, newly written Python 3 standard-library code.
* `fspd_raw.jsonl` — the only raw-output artifact, containing both invocations and their complete root propagation traces.

From this artifact directory, the two diagnostic invocations are reproducible as:

```sh
python3 fspd_exact.py
python3 -c 'import runpy; d=runpy.run_path("fspd_exact.py"); d["main"].__globals__["CASES"]=(163,211,283,307,331,379,499); d["main"]()'
```

The interpreter was Python 3.9.6. No mathematical package, current source, web source, or remembered reciprocity calculation was used. The cutoff 2026-07-31 is respected by using only the supplied packet and local derivations/computation. No prior review or shared task/team state was read.

SHA-256 snapshots (paths relative to W):

```text
request.md
  a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f
nl/explorer/residual-v1.md
  4725c57ed85ddeb6591e2b59e7fb4952ea0e0a8aee5fbb19f5c7669ef1002fa4
nl/ce-hunter/fspd_exact.py
  9af5932c7ab2e5466ea48f4b8a490aaf048baf9696032e4ab7e89def3a5f9d3a
nl/ce-hunter/fspd_raw.jsonl
  59d669a04bc5156d649b338b42add9954170ce393c81834b3497943a352087a9
```
