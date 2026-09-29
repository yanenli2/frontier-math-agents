# Fresh independent review of partial proof attempt v1

Mode: CERTIFICATION.

**Requested T4 verdict: UNRESOLVED.** The exact candidate does not prove representation for every positive multiple of four. Its remaining universal obligation is C3, stated below. This is not a finding that T4 is false.

**Scoped mathematical verdicts:** the supplied local proofs and equivalences listed in §4 pass this natural-language audit under the supplied baseline. In particular, the two-squares argument and the conclusion for every positive m not congruent to 3 modulo 4 pass. These local PASS results are not a PASS for T4, S(p), or Q(p) universally.

No repair of the candidate was made. No substantive gap was found in its claimed completed local deductions. No new Lean theorem was compiled or kernel-checked in this review. An LLM mathematical review is not Lean kernel verification.

## 1. Artifact identity and review boundary

Path aliases:

- R = `.`
- P = `R/.clawcodex/math-team/problems/liouville-goldbach-jul2026`
- W = `P/waves/multiples-four`
- M = `P/lean/.lake/packages/mathlib`
- This report = `W/nl/reviews/partial-review-v1.md`

SHA-256 values were computed directly with `shasum -a 256`. The candidate, obligation ledger, and two baseline Lean files were hashed again immediately before writing this report; their identities were unchanged.

| Input | SHA-256 | Read scope |
|---|---|---|
| `R/.clawcodex/skills/math-team/references/protocol.md` | `e712830b3febe6e3fcaf0479c7aa9fc30f23aa4fcc5e1f45088f736f9c161f2b` | Full |
| `W/request.md` | `a812fb01fe4e29e0c6e0fc4737fb3e98a730091f35e32f08ceba740bc30ec96f` | Full; exact assigned target |
| `W/nl/generator/proof-attempt-v1.md` | `1730e39b6ef4eb33bc4621e26642d63b4c775415a4cdeec7de00ccff71fa89ef` | Full, lines 1–286 |
| `W/nl/generator/obligations-v1.md` | `03d84b25c0a632aa73a794588f71a4768109ca6706f077c6bbc7eb48f0c452a7` | Full, lines 1–107 |
| `P/lean/Statement/Definitions.lean` | `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d` | Full |
| `P/lean/Statement/Partial.lean` | `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0` | Full; relevant dependencies identified below |
| `W/formal/approved-v1/Declaration.lean` | `bdfb30bcfade7b9df33e48f280125d10a40dd76f365cf5b87047183475fee7ed` | Full; signature comparison, not a proof |
| `P/request.md` | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` | Full; original target and source constraints |
| `P/sources.md` | `9df552348f03fd84ffe0e203f1340f26e6a902f8424f924068fe6fb86c1a7dbb` | Full; provenance ledger, not literature evidence |
| `P/lean/lean-toolchain` | `2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273` | Full |
| `P/lean/lake-manifest.json` | `de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03` | Full |
| `M/Mathlib/Data/Nat/Factors.lean` | `3e64e2c8ba907c05209966a7bba8754cf2ab33f328a3010667ffe58c95e0bca3` | Lines 1–220; hash covers entire file |
| `M/Mathlib/Data/Nat/Prime/Defs.lean` | `617c1a2a927a2a282092f11c8d254036454e7ffa2eab12f8dd16880cf83d0d61` | Lines 1–100; hash covers entire file |

The baseline hashes match the supplied identities. The other checked identities quoted in candidate §0 also match. `P/FINAL_ARGUMENT.md`, cited by the author, was not opened or relied on: the needed statements were checked directly against the supplied baseline and pinned factorization source. No historical review, author-confidence artifact, task board, or team state was inspected. No agents were spawned. Only this report was written.

## 2. Exact target and convention audit — PASS

The target remains

`∀ m : ℕ, 0 < m → ArithmeticStatement.HasRepresentation (4 * m)`.

Unfolding `HasRepresentation` and `HasSignedRepresentation` gives positive natural a,b, equality `4*m = a+b`, and both lambda values equal to -1 in ℤ. `omega` is the length of `primeFactorsList`, including multiplicities. Lambda at 1 is +1. Equal summands are allowed. The isolated declaration matches these definitions and the request exactly.

The candidate's G(N) is precisely this representation predicate. Its P_s(N) matches the signed version. All final witnesses are positive natural numbers. Integer coordinates in the modular argument are replaced by absolute values before applying lambda; no value of lambda at a negative integer is required. No lambda(0) convention is used.

The cases m=1, repeated prime factors, equal witnesses, even m, and primes 2 and 3 are not discarded. No primality, oddness, coprimality, or distinctness condition is imposed on the original target. C3 is an equivalent residual assertion after separately proving the complementary cases, not an added premise in a purported proof of T4.

The original all-even target is broader than T4 and is not proved here either.

## 3. Dependency and source audit

| Dependency | Exact usable content and guards | Audit |
|---|---|---|
| D1 | `Partial.lean:43–55`: lambda(1)=1; for n>0, lambda(n) is +1 or -1 | Every sign split concerns a positive input. |
| D2 | `Partial.lean:57–64`: omega(uv)=omega(u)+omega(v), hence lambda(uv)=lambda(u)lambda(v), for u,v>0 | No coprimality condition. The list-product permutation counts repetitions, so repeated factors cause no exception. |
| D3 | `Partial.lean:66–96`: prime sign -1, signs at 2,3,4,5, doubling changes sign, and lambda(t²)=1 for t>0 | All prime and positivity guards are satisfied in the claimed constructions. |
| D4 | `Partial.lean:102–109`: P_s(N) implies P_{lambda(d)s}(dN) for d>0 | Witnesses are multiplied by d. No converse scaling or division of witnesses is used. |
| D5 | `Partial.lean:139–159`: opposite-sign seeds at a total give its positive multiples; in particular G(8t) for every t>0 | Seeds 3+5 and 4+4 are valid. The equal positive-sign seed is permitted. |
| D6 | Pinned `Factors.lean:55–88,143–156,196–202`: list entries prime, product n for n≠0, singleton for a prime, prime membership/divisibility for n≠0, and product-list concatenation for nonzero factors | Supports existence of a prime divisor of n>1 and ordinary prime cancellation. This is independent of any representation theorem. |

The candidate's use of prime cancellation is legitimate: the factor-list product facts supply Euclid's divisibility property. In modular arithmetic this has its usual integer meaning; zero cases are immediate and signs do not affect divisibility. The proof does not assume a field theorem whose proof would depend on the desired two-squares result.

`git -C M rev-parse HEAD` returned `905b95818eb32af7874a58b427f50c1711a5e96c`. Comparing both inspected Mathlib source files with that commit using `git diff --exit-code` returned exit 0 and no difference. The manifest pins the same revision; `lean-toolchain` specifies `leanprover/lean4:v4.32.2`.

The supplied provenance ledger records exact-version public availability on 2026-07-28, within the inclusive 2026-07-31 cutoff, and the transitive package revisions. This review used the user-supplied pinned baseline, not a later checkout. Public-availability metadata was not independently re-fetched. No external source was retrieved and no paper theorem was used. Wilson's congruence and the needed prime two-squares result have local proofs audited below. The original Target, `target_iff_prime_product_core`, C3, S, and Q are not imported assumptions.

This is a source/guard audit of the new argument against the specified baseline, not a fresh transitive compilation or environment-provenance certification.

## 4. Step-by-step mathematical checks

### 4.1 Diagonal, even m, and prime-divisor scaling — PASS

Candidate §2.1, lines 64–79; ledger O01–O03.

- If lambda(m)=1, the witnesses (2m,2m) are positive, have total 4m, and each has sign -1. At m=1 this is 4=2+2.
- If m is even and positive, m=2t with t>0, so the exact baseline G(8t) applies.
- Otherwise m is odd, lambda(m)=-1, and m>1. For any prime divisor p, the factorization m=pd has p odd and d>0. Multiplicativity yields -1=-lambda(d), hence lambda(d)=1. Multiplying a representation of 4p by d gives one of 4m with both negative signs preserved.

This works for any chosen prime occurrence, including when p divides m repeatedly. No unjustified inference from a representation of a composite number to one of a divisor appears.

### 4.2 Exact odd-prime core and least counterexample — PASS

Candidate §2.2, lines 81–91; O04.

The forward direction of T4 iff G(4p) for every odd prime is specialization to m=p. Conversely, the sign/even split above exhausts positive m, and the remaining inputs have a prime divisor to which the stated core applies.

For a least counterexample, compositeness would give a prime divisor p<m; minimality gives G(4p), and the sign-preserving scaling contradicts failure. At a prime there is no such smaller divisor argument. The candidate does not incorrectly use minimality to close that last case.

### 4.3 Total-four obstruction and all-12t seed — PASS

Candidate §2.3, lines 93–105; O05–O06.

The positive ordered decompositions of 4 are exactly 1+3, 2+2, 3+1. Their signs are respectively (+,-), (-,-), (-,+); no positive-positive seed exists at total 4. This refutes only the suggested two-sign seed at 4.

At total 12, 5+7 has two negative signs and 6+6 has two positive signs. The primality/sign checks are elementary and valid. If lambda(t)=1, scale 5+7; if lambda(t)=-1, scale 6+6. In either case t>0 gives positive witnesses and total 12t. Thus G(12t) holds for every positive t, and 3 dividing m is covered. In particular p=3 is settled by 12=5+7; it is not left in the residual core.

### 4.4 Sum-of-two-squares construction, including all boundary cases — PASS

Candidate §3.1, lines 111–123; O07.

For m=u²+v²>0 with u,v nonnegative and u≠v, both u+v and |u-v| are positive. The proposed witnesses have sign -1 by the square and doubling laws, and the integer identity

`2(u+v)² + 2(u-v)² = 4(u²+v²)`

gives the required total. If exactly one coordinate is zero, the witnesses are equal positive numbers; this is allowed. If u=v, positivity of m implies u>0, and the separate G(8u²) branch applies. The zero-zero pair is excluded by m>0. No zero witness is ever admitted.

### 4.5 Root of -1 by inverse pairing — PASS

Candidate §3.2, lines 127–139; O08.

For prime p≡1 mod 4, p≥5. Prime cancellation makes multiplication by each nonzero residue an injective self-map of the finite nonzero residue set, hence a permutation, so inverses exist. The self-inverse residues solve (a-1)(a+1)=0 and are exactly the two distinct residues ±1. Every other residue belongs to a two-element inverse pair with product 1. Therefore the product of all nonzero residues is -1.

For h=(p-1)/2, the pairs j and p-j exhaust those residues. Their product is (-1)^h(h!)²; h is even. Thus t=h! satisfies t²≡-1 mod p. There is no unproved appeal to Wilson's theorem or to the two-squares theorem in this derivation.

### 4.6 Pigeonhole vector and strict norm bound — PASS

Candidate §3.2, lines 141–157; O09.

A prime is not a square, so s=floor(sqrt(p)) satisfies the two strict inequalities s²<p<(s+1)². The inclusive square grid 0≤i,j≤s has exactly (s+1)²>p points. Mapping it to the p residues by i+tj forces a collision of distinct pairs. Their integer difference (x,y) is nonzero and has |x|,|y|≤s.

From x≡-ty and t²≡-1, p divides x²+y². Nonzeroness gives positive norm, and the supplied upper bound is genuinely strict:

`0 < x²+y² ≤ 2s² < 2p`.

It therefore equals p, rather than 0, 2p, or an unspecified multiple of p. Taking absolute values gives natural u,v. Since p is odd, u=v is impossible. This verifies every load-bearing counting, divisibility, and size step and closes G(4p) for all primes p≡1 mod 4 by §4.4.

### 4.7 Sharper exact equivalence and unconditional residue classes — PASS

Candidate §4, lines 159–179; O10–O11.

The residual assertion is exactly

`C3: ∀ p : ℕ, Prime(p) → 7 ≤ p → p ≡ 3 (mod 4) → G(4p)`.

T4 implies C3 by restriction. In the reverse direction, after the diagonal and even cases, m is odd with sign -1 and any prime divisor p has sign-positive cofactor. Such an odd prime is exactly one of:

1. p=3, covered by the total-12 seed;
2. p≡1 mod 4, covered by the local two-squares proof;
3. p≡3 mod 4 and p≠3, hence p≥7, covered by the explicitly assumed C3.

Each resulting representation is scaled by a positive cofactor of sign +1. Prime 2 was already removed by the even-m case. Both directions and every boundary case are valid.

The extension to m having a prime divisor 1 mod 4 is also correct without assuming m odd: the sign-positive case is diagonal, and in the sign-negative case the cofactor again has sign +1.

For m≡1 mod 4, m is odd. If its sign were -1 and no prime divisor were 1 mod 4, all prime occurrences would be 3 mod 4. Their product modulo 4 would be (-1)^Omega(m)=-1, contradicting m≡1. Multiplicity is essential here and is counted correctly. The m=1 case is separately covered. Together with even m, this proves G(4m) for every positive m not congruent to 3 mod 4. For positive N divisible by 4, the only residue class not uniformly settled by these arguments is N≡12 mod 16; this does not assert failure anywhere in that class.

Consequently any least counterexample must be a prime p≥7 congruent to 3 modulo 4. This is a restriction on a hypothetical counterexample, not an existence claim.

### 4.8 Reflection/doubling under failure — PASS, conditional only

Candidate §5.1, lines 181–199; O12.

Assume failure of G(4p) as stated. Each forbidden-sign implication is valid:

- For 0<x<4p, two negative signs at x and 4p-x would directly be forbidden witnesses, so a negative sign at x forces a positive sign at its reflection.
- For 0<x<2p, two positive signs at x and 2p-x would become two negative signs after doubling; thus a positive sign at x forces a negative one at 2p-x.
- For 0<x<p, two negative signs at x and p-x would remain negative after multiplication by 4 and have total 4p.

Every difference is positive, so sign dichotomy and multiplicativity apply. To combine the first two rules, 0<t<2p ensures 0<2p-t<4p; its reflection is exactly 2p+t. Hence failure imposes both signs in (**), with the stated universal scope over positive-sign t. No contradiction follows in the candidate, and none is certified here.

### 4.9 S(p) construction — PASS for S(p) ⇒ G(4p), not existence

Candidate §5.2, lines 201–217; O13.

For an S-witness t, if lambda(2p-t)=1, the pair (2t,2(2p-t)) has positive entries, total 4p, and both signs -1. If only lambda(2p+t)=-1 is known, dichotomy at the positive integer 2p-t either returns that first construction or yields the negative-negative pair (2p-t,2p+t). The two cases exhaust the possibilities.

The candidate neither proves S(p) for the residual primes nor asserts G(4p) ⇒ S(p). No equivalence is certified.

### 4.10 Five fixed pairs and p=163 — PASS for the stated template failure

Candidate §5.3, lines 219–246; O15.

All five pairs are positive for p≥7 and sum to 4p. Their sign tests follow respectively by factoring the relevant entries as 2(2p-1), 4(p-2), 4(p-3), 2(p±1), and the displayed 2p±1 themselves.

For p=163, 163≡3 mod 4 and 12²<163<13². Trial division by the complete prime list 2,3,5,7,11 gives nonzero remainders 1,1,3,2,9. Thus it is a genuine residual prime. The displayed factorizations and exponent sums independently verify:

| Pair | Omega values | Signs |
|---|---|---|
| (2,650), with 650=2·5²·13 | (1,4) | (-,+) |
| (8,644), with 644=2²·7·23 | (3,4) | (-,+) |
| (12,640), with 640=2⁷·5 | (3,8) | (-,+) |
| (324,328), with 324=2²·3⁴ and 328=2³·41 | (6,4) | (+,+) |
| (325,327), with 325=5²·13 and 327=3·109 | (3,2) | (-,+) |

The factors used are prime by complete trial division up to their square roots; for 109 the required list is 2,3,5,7. Thus this is a rigorously checked failure of this particular five-pair cover, not merely a search observation.

It is not a counterexample to T4: 50=2·5² and 602=2·7·43 each have three prime factors with multiplicity, 43 is prime, and 50+602=652=4·163. The finite example refutes only the specified list; it does not prove that every possible larger finite list must fail.

### 4.11 Twice-square obstruction — PASS for that template only

Candidate §5.4, lines 248–250; O16.

For p≡3 mod 4, a representation 4p=2u²+2v² would give u²+v²=2p≡6 mod 8. Integer squares modulo 8 are exactly among 0,1,4; pairwise sums give only 0,1,2,4,5. The obstruction is valid even allowing zero, negative, or equal coordinates. It says nothing against general Liouville-negative witnesses.

### 4.12 Q(p) bridge — PASS for Q(p) ⇒ G(4p), not the proposed universal assertion

Candidate §6, lines 252–260; O18 bridge.

For k≥1 and k²<2p with lambda(2p-k²)=1, the pair (2k²,2(2p-k²)) is positive and sums to 4p. Both signs are -1. The positive square k² has sign +1, so this is indeed S(p)'s first alternative with t=k².

At p=163, k=5 gives the positive-sign complement 301=7·43 and recovers (50,602). This checks the example, not a universal quantifier. Q is only a proposed sufficient route. A counterexample to Q would not, by itself, refute C3 or T4.

## 5. Bounded diagnostics: reproduced observations, no universal proof weight

The candidate preserves its bounds and does not use a finite-to-infinite inference. I independently reran these diagnostics in memory using Python 3.9.6, without creating a script or data file. The common sieve bound was 400000 inclusive, sufficient for every accessed value in both original tests.

Reproduction method: initialize spf(n)=n; for each sieve prime q≤floor(sqrt(400000)), mark the previously unmarked multiples starting at q²; set lambda(1)=1 and successively lambda(n)=-lambda(n/spf(n)). Primality tests in the scans were spf(p)=p. Test the actual five pairs, scan a=1,...,floor(p/2) for G(p), and scan k=1,...,floor(sqrt(2p-1)) for Q. All arithmetic and square-root bounds used integers.

Observed output, exit 0:

- Five-pair scan over primes 7≤p<50000, p≡3 mod 4, stopping after five failures: **163, 367, 827, 907, 1531**.
- All 5132 odd primes 3≤p<50000 tested for G(p): only **p=3** lacked such a representation.
- All 9005 primes 7≤p<200000, p≡3 mod 4, tested for Q(p): **no failures**.
- Largest least successful k: **14**, attained at **p=170243** only in that scan.
- Least k at p=7,163,367: **2,5,4**, respectively.

These agree with the candidate's numerical observations. They certify no universal G(p), C3, S, or Q claim. In particular, the G(3) diagnostic does not conflict with the proved G(12) boundary case. The p=163 template refutation in §4.10 has a separate elementary certificate and does not depend on this computation.

## 6. Remaining obligations, ledger disposition, and next action

### Required endpoint still absent

The exact open mathematical obligation is

`∀ p : ℕ, Prime(p) → 7 ≤ p → p ≡ 3 (mod 4) →`
`  ∃ a b : ℕ, 0<a ∧ 0<b ∧ 4*p=a+b ∧ lambda(a)=-1 ∧ lambda(b)=-1`.

This is ledger O17/C3. By the checked equivalence it is necessary and sufficient to finish T4 within the established reduction. The precise break occurs after candidate §4: a residual prime is not reduced to a smaller input; §5 obtains only necessary sign restrictions under failure; §6 supplies only a conditional construction. Neither produces witnesses for every such prime.

Ledger disposition:

- O00–O13: the stated target checks and local arguments pass within their specified scopes; O13 does not establish existence of an S-witness.
- O15–O16: the specific template failures/obstructions pass; neither refutes T4.
- O14: no contradiction from (**) has been supplied.
- O17: open, and load-bearing for T4.
- O18: its constructive implication passes, but the universal existence assertion Q remains open.
- O19: the bounded observations have been reproduced, but supply no unbounded argument. No numerical exhaustion is accepted as proving the endpoint.
- O20: this report supplies one fresh natural-language audit of this exact snapshot only.
- O21: new Lean formalization, pinned compilation, and axiom inspection remain unperformed here.

O14 and O18 are alternative research routes, not additional assumptions that may be attached to T4 and not both mandatory if C3 is proved by another method. No repair is needed to the completed local arguments found in this audit. The missing universal endpoint is a substantive unfinished proof, not a typographical issue and not a demonstrated false statement.

**Recommended next action:** the leader may route the locally passing deductions for separate formalization and exact pinned compiler/axiom checks while keeping `representation_multiple_four` unresolved. Route C3, or the expressly sufficient Q route, back for new mathematical work; require a uniform argument or an exact counterexample to the particular proposed auxiliary assertion. Re-review any changed candidate under new hashes. Do not publish this partial review as certification of T4 or of the original all-even theorem.
