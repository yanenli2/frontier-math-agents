# Multiple-of-four attempt v1: inputs, obligations, and handoff

Mode: CERTIFICATION — candidate production, not self-acceptance.

**Deliverable status: candidate files produced. Mathematical status: requested theorem unresolved.** No task-board action, Lean edit, nested agent, or external-source retrieval was performed. No fresh compiler/kernel verification is claimed.

## 1. Exact assignment and artifact ownership

Project root: `.`.

P: `.clawcodex/math-team/problems/liouville-goldbach-jul2026` under that root.

W: `P/waves/multiples-four`.

Target: for every m∈ℕ with m>0, there exist a,b∈ℕ with a>0, b>0, 4m=a+b, and λ(a)=λ(b)=-1. The definitions are Ω(n)=length(n.primeFactorsList) and λ(n)=(-1)^Ω(n) in ℤ. Multiplicity counts; a=b is allowed; no further witness or input condition is imposed.

Owned output files only:

- `W/nl/generator/proof-attempt-v1.md`;
- this file, `W/nl/generator/obligations-v1.md`.

The target and all mathematical input hashes are recorded in proof-attempt-v1.md §0. The assignment and both protocol files were read before doing the mathematics. All earlier artifacts were preserved.

## 2. Dependency inventory and source discipline

| ID | Exact usable content | Source and guards | Use |
|---|---|---|---|
| D0 | Approved target and sign/representation definitions | `W/request.md`; `W/formal/approved-v1/Declaration.lean`; positive witnesses | Contract; no weakening |
| D1 | λ(n)∈{1,-1} for n>0; λ(1)=1 | `P/lean/Statement/Partial.lean:43–55` | Every sign case split |
| D2 | λ(uv)=λ(u)λ(v) for u,v>0, with no coprimality requirement | `Partial.lean:57–64` | All scaling and factor signs |
| D3 | λ(q)=-1 for prime q; λ(2)=-1; λ(4)=1; λ(t²)=1 for t>0; λ(2t)=-λ(t) | `Partial.lean:66–96` | Diagonal, square, seed, and doubled constructions |
| D4 | P_s(N) implies P_{λ(d)s}(dN) for d>0 | `Partial.lean:102–109`; explicitly reconstructed by multiplying witnesses | Prime-core assembly |
| D5 | G(8t) for every t>0 | `Partial.lean:150–159` | Even m and equal square coordinates |
| D6 | Positive integer prime factor lists consist of primes, have product n, and multiply by concatenation up to permutation | Accepted factor-list input documented in `FINAL_ARGUMENT.md` §2 and `sources.md`, pinned Mathlib `Data/Nat/Factors.lean` | Choosing prime divisors; elementary prime cancellation |
| L1 | Inverse pairing gives (p-1)!=-1 modulo p; then a root of -1 when p=1 modulo 4 | Full local proof in attempt §3.2, using only D6, finite permutation, and prime p≥5 | Two-squares construction; not a named external theorem assumption |
| L2 | More than p pairs map to p residues; a bounded congruence vector has norm p | Full finite counting and inequalities in attempt §3.2 | Two-squares construction; no lattice theorem imported |

The original all-even `Target`, the original prime-product-core assertion, and C3/S/Q defined in this attempt are **not** accepted inputs. The old all-even target was not invoked. `FINAL_ARGUMENT.md` was used for its self-contained mathematics and boundary descriptions, not as evidence from historical reviewers.

No analytic theorem or paper theorem is used. All externally supplied mathematical input is within the previously accepted definitions/partial module and the pinned factor-list source. Wilson's factorial congruence and the prime two-squares result are derived locally rather than imported from memory. Their local arguments require fresh review like all other new work. The source cutoff remains 2026-07-31 inclusive.

## 3. Obligation ledger

“Argument supplied” means the candidate contains a proof; it does not mean an independent verifier has accepted it.

| ID | Obligation | Location/evidence | Current status |
|---|---|---|---|
| O00 | Preserve the exact target, positive domains, multiplicity convention, and equality-allowed witnesses | Attempt §0, matching approved declaration | Contract recorded |
| O01 | Close m=1 and every λ(m)=1 case | (2m,2m), signs from D3 | Argument supplied, §2.1 |
| O02 | Close every even m without dividing inappropriate witnesses | m=2t, t>0, use G(8t) | Argument supplied, §2.1 |
| O03 | For an unresolved odd m, select a prime p dividing m and prove λ(m/p)=1 | λ(m)=-1, λ(p)=-1, m=pd>0, D2 | Argument supplied, §2.1 |
| O04 | Assemble arbitrary m from odd prime cores; justify least-counterexample primality | Positive scaling by d with λ(d)=1; p<m only in the composite case | Argument supplied, §2.2 |
| O05 | Check rather than assume a positive seed at total 4 | Exhaustion 1+3,2+2,3+1 | Seed premise refuted, §2.3; target not refuted |
| O06 | Prove the additional uniform family G(12t) | Seeds (5,7) negative and (6,6) positive; exact sign cases | Argument supplied, §2.3 |
| O07 | Make every square-construction witness positive, including equal-coordinate and zero-coordinate edge cases | Unequal coordinates give 2(u+v)²,2|u-v|²; equal nonzero coordinates use G(8u²) | Argument supplied, §3.1 |
| O08 | Produce a root of -1 modulo each prime 1 modulo 4, without importing an unproved theorem | Nonzero residue permutation, inverse pairs, self-inverses ±1, even (p-1)/2 | Argument supplied, §3.2 |
| O09 | Produce an integer square-sum exactly p rather than an unspecified multiple | (s+1)²>p residue inputs; nonzero norm ≤2s²<2p; p divides norm | Argument supplied, §3.2 |
| O10 | Exhaust prime classes and justify both directions of T4 iff C3 | p=3, p=1 modulo 4, or p≥7 and p=3 modulo 4; converse scales with correct sign | Argument supplied, §4 |
| O11 | Derive all m=1 modulo 4, not only prime inputs | If λ(m)=-1 and all prime factors are 3 modulo 4, m=3 modulo 4, contradiction | Argument supplied, §4 |
| O12 | Justify each reflection/doubling implication with range and sign guards | No -- at 4p, no ++ at 2p, no -- at p | Argument supplied, §5.1 |
| O13 | Turn a supplied shift witness into an actual pair | Two cases for λ(2p-t), explicit positive pairs | Argument supplied, §5.2; S(p) itself not established |
| O14 | Supply a uniform elementary contradiction to the forced shift pattern (**) for residual primes | No such contradiction obtained | OPEN |
| O15 | Check the five-pair mechanism and distinguish its failure from target failure | Prime p=163; exact factorizations; actual successful pair (50,602) | Proposed finite cover refuted, §5.3 |
| O16 | Check whether the two-twice-squares form can cover residual primes | 2p=6 modulo 8, impossible as sum of two squares modulo 8 | Template extension ruled out, §5.4; target not refuted |
| O17 | Prove all residual prime cores C3 | ∀ prime p≥7, p=3 modulo 4 ⇒ G(4p) | OPEN: the universal load-bearing endpoint |
| O18 | Alternative adaptive square-shift Q(p) | ∃k≥1, k²<2p and λ(2p-k²)=1; explicit doubling bridge proved | OPEN sufficient route, §6 |
| O19 | Replace bounded diagnostics by a uniform argument, if used for the endpoint | No large-p theorem or finite-to-infinite step is available | OPEN; no proof claim based on experiments |
| O20 | Independently verify the local partial deductions and exact reduction | Fresh verifier required; generator does not accept its own output | Pending leader routing |
| O21 | Formalize any newly accepted partial deductions | No Lean changes or compiler checks in this assignment | Not performed or claimed |

## 4. Strongest partial conclusion and exact missing claim

The strongest uniform core equivalence for which this attempt supplies a complete argument is:

T4 ↔ [for every prime p≥7 congruent to 3 modulo 4, G(4p)].

Beyond the previous all-8t family, the attempt supplies:

- G(4m) for every positive m that is a sum of two squares;
- in particular G(4p) for every prime p congruent to 1 modulo 4, with a self-contained proof and explicit twice-square witnesses;
- G(12t) for every t>0;
- G(4m) whenever m has a prime divisor congruent to 1 modulo 4;
- G(4m) for every positive m not congruent to 3 modulo 4.

These are unreviewed deductions with proofs in the candidate, not accepted extensions of the baseline. The universal claim for the remaining primes is still exactly:

∀p∈ℕ, Prime(p) ∧ p≥7 ∧ p≡3 (mod 4) ⇒
∃a,b∈ℕ, a>0 ∧ b>0 ∧ 4p=a+b ∧ λ(a)=λ(b)=-1.

No sign, size, or congruence premise was added to T4. The displayed restriction is the output of a proved reduction: all other inputs were separately handled, and the restricted universal assertion is explicitly unresolved.

## 5. Failed routes and experiment boundaries

1. **Uniform scaling/minimal-counterexample mechanism:** correctly reduces a least counterexample to a prime. It cannot descend past a prime using a sign-preserving proper divisor. The absent positive-positive seed at 4 is an exact obstruction to that fixed-seed method.
2. **Uniform additive reflection/doubling mechanism:** failure at 4p implies the sign pattern (**) for every positive-sign t<2p. The implications are rigorous; a contradiction from them is missing. An enlarged list of five explicit pairs fails at the genuine residual prime p=163. This is not a counterexample to T4.
3. **Two-square construction:** resolves primes 1 modulo 4 but cannot itself solve primes 3 modulo 4, since any pair of twice-squares would contradict the square residues modulo 8.
4. **Finite diagnostics:** first run used a smallest-prime-factor sieve through 200000. The five-formula search had a prime cap of 50000 but stopped after its fifth failure, at p=1531; the failures were 163,367,827,907,1531. A separate diagnostic scanned all odd primes below 50000 but did not establish any uniform theorem. The adaptive-square run used a sieve through 400000 and residual primes below 200000, with no Q(p) failures in that range; the largest observed least k was 14 at p=170243. These finite observations are recorded only to diagnose routes. No source file, data file, Lean artifact, or third output file was created.

Both requested substantively different uniform elementary mechanisms were attempted, with their exact points of failure preserved. The extra two-square mechanism supplies new uniform progress but not the endpoint.

## 6. Concrete next action

First send the local two-squares proof, the positivity checks, and the equivalence T4 iff C3 to a fresh mathematical verifier. The leader may route accepted partial content to the independently working Lean generator; this author does not claim acceptance or edit Lean.

For further mathematics, one specific alternative is to attack the adaptive assertion Q(p): for every residual prime p, find k with 0<k²<2p and λ(2p-k²)=1. Its constructive bridge is already proved. It must allow a nonsquare positive-sign complement, because a square complement is impossible in this residue class. Either a uniform proof or an exact counterexample to Q(p) is needed; more finite successful tests alone would not discharge O17 or O18.

**Final handoff: incomplete proof attempt with new candidate partial reductions; C3 remains open. Only a fresh verifier can accept any new mathematical content.**
