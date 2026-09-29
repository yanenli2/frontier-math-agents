# Finite computational certification report

Mode: CERTIFICATION / computational AUDIT, finite claims only.

## Verdict and qualification

**PASS for the explicit finite claims below:** 1,260 assertions; zero failed assertions; zero exceptions. Worker and parent exit statuses were both 0. This is exact computational evidence, not a formal proof or a global mathematical conclusion.

**PB-label fidelity remains unverified.** The dispatch says “PB three-test” but neither defines it nor supplies a definition file; `request.md` does not contain that term. This audit explicitly checks the three smallest positive-Liouville first-summand candidates `(1,73)`, `(4,70)`, `(6,68)` at `2q=74`. It does not silently certify that these are the intended named PB tests. A clarification notification to `team-lead` failed with `Only active team members can send team messages`. The leader must confirm the formula-to-label correspondence. The square-template formula is also stated explicitly below.

## Mathematical claims checked

Conventions: positive arguments only; `Omega` counts prime factors with multiplicity; `Omega(1)=0`; `lambda(1)=1`. Throughout, `++` and `--` refer to the two Liouville values, not to signs of the positive summands.

### q = 37

The independent exact factorization checks include primality of 37. The three explicit candidate pairs fail to be `++`:

| Pair | Relevant factorization | Liouville signs |
|---|---|---|
| 1 + 73 | 73 prime | (+1, -1) |
| 4 + 70 | 4 = 2^2; 70 = 2*5*7 | (+1, -1) |
| 6 + 68 | 6 = 2*3; 68 = 2^2*17 | (+1, -1) |

Equivalently, the computed values at `(2q-1,q-2,q-3)=(73,35,34)` are `(-1,+1,+1)`.

Nevertheless, **74 = 9 + 65 is `++`**, since `9=3^2` and `65=5*13`, both with `Omega=2`. Thus the three-candidate list misses a valid `++` decomposition at this q; its failure does not imply nonexistence of such a decomposition.

### q = 5

5 is prime. The inclusive sum is exactly

`L(4) = lambda(1)+lambda(2)+lambda(3)+lambda(4) = 1-1-1+1 = 0`.

### N = 10

`L(9)=-1`, `C(10)=9`, and the actual ordered `--` pairs are

`(2,8), (3,7), (5,5), (7,3), (8,2)`.

Thus `R(10)=5`, including the diagonal exactly once, and

`4R(10)=20=9-2*(-1)+9`.

### m = 1304

The checked square template is, for positive `k`,

`m = k^2 + (m-k^2)`, with corresponding target pair
`2m = 2k^2 + 2(m-k^2)`.

Only `k=1,...,7` is tested. All summands are positive. Each square has Liouville value `+1`; each doubled square has value `-1`.

| k | k^2 | 1304-k^2, fully factored | Omega of residual | lambda of residual | Target pair and signs |
|---|---|---|---|---|---|
| 1 | 1 | 1303, prime | 1 | -1 | 2 + 2606, (-1,+1) |
| 2 | 4 | 1300 = 2^2*5^2*13 | 5 | -1 | 8 + 2600, (-1,+1) |
| 3 | 9 | 1295 = 5*7*37 | 3 | -1 | 18 + 2590, (-1,+1) |
| 4 | 16 | 1288 = 2^3*7*23 | 5 | -1 | 32 + 2576, (-1,+1) |
| 5 | 25 | 1279, prime | 1 | -1 | 50 + 2558, (-1,+1) |
| 6 | 36 | 1268 = 2^2*317 | 3 | -1 | 72 + 2536, (-1,+1) |
| 7 | 49 | 1255 = 5*251 | 2 | +1 | 98 + 2510, (-1,-1) |

The target success is also factored directly, rather than inferred only from scaling: `98=2*7^2` and `2510=2*5*251`, each with `Omega=3`, and `98+2510=2608`. No claim that 1304 is a least exceptional `m` was checked or is made.

### Exhaustive counting-identity instances

For each integer `N=2,...,256`, including odd N, the script independently computes

- `R(N)`: number of actual ordered positive pairs `(a,N-a)` with both Liouville values `-1`;
- `L(N-1)`: inclusive sum over `1,...,N-1`;
- `C(N)`: signed integer sum of `lambda(a)*lambda(N-a)` over `a=1,...,N-1`.

Every one of the 255 exact comparisons passed:

`4R(N) = (N-1) - 2L(N-1) + C(N)`.

`R` is not obtained by rearranging this identity. Python signed integers are used throughout, without division of the right side or natural-number truncation.

Representative values, also rechecked by independent two-index enumeration and fresh trial factorization:

| N | L(N-1) | C(N) | R(N) | Both sides |
|---|---|---|---|---|
| 2 | 1 | 1 | 0 | 0 |
| 3 | 0 | -2 | 0 | 0 |
| 4 | -1 | -1 | 1 | 4 |
| 10 | -1 | 9 | 5 | 20 |
| 256 | -7 | 7 | 69 | 276 |

## Finite universe, coverage, and independence

The identity loop visits every `N` in the closed interval `[2,256]` exactly once and every `a` in `[1,N-1]`, totaling 32,640 ordered-pair positions. There is no symmetry reduction: both orders are retained, and `a=b` is allowed. The lower boundary `N=2` is tested even though it is outside the original target's `N>2` hypothesis. Zero summands and `lambda(0)` are never used. The square tests start at `k=1`, not the disallowed zero summand; residual positivity is explicitly checked.

The complete set of Liouville arguments used is the 271-element set

`{1,...,255} union {1255,1268,1279,1288,1295,1300,1303,1304,2510,2536,2558,2576,2590,2600,2606,2608}`.

For every argument in that set:

1. Trial division uses only exact remainder and integer quotient operations, testing divisors while `d*d <= remaining`.
2. Reconstructed products must equal the original integer.
3. The parity of the sum of prime exponents gives one Liouville value.
4. An independent Eratosthenes sieve finds primes, then flips each multiple's sign once for every prime power dividing it, giving a second value.
5. These two values must agree and belong to `{-1,+1}`.

All 271 comparisons and product reconstructions passed. For all 57 distinct prime factors, the output additionally supplies exact divisor/remainder certificates covering every integer divisor from 2 through the square-root boundary. Every remainder is nonzero, and sieve primality flags agree. The case 1 has empty factorization, reconstructed product 1, and Liouville value +1.

The sieve bound is 2608; the other 2,337 generated Liouville entries are not claimed as cross-checked evidence. No target or bridge search to 20,000 was run. This was one exhaustive identity-range run, with only five specified representative identity cases separately re-enumerated. No ratio/projection inference, sampling, fitted pattern, or extrapolation is involved. No computation was interrupted; the execution call had a 60-second timeout and completed normally.

## Reproduction and provenance

Run from any directory:

```sh
/Library/Developer/CommandLineTools/usr/bin/python3 -I -S ".clawcodex/math-team/problems/liouville-goldbach-jul2026/nl/code-executor/finite_certify.py"
```

The parent runs the same script with `--worker`, records its actual subprocess return code, captures stdout/stderr, and writes the evidence and manifest. The exact parent and worker commands are in `run.log` and `run.json`. This command regenerates the three output artifacts in the owned directory; it does not modify inputs or shared files.

Runtime: **CPython 3.9.6**, `default, Dec 2 2025, 07:27:58`, built with `Clang 17.0.0 (clang-1700.6.3.2)`. Both isolation and no-site flags were 1. The executable and directly imported standard-library module files are SHA-256 pinned in `run.json`. This runtime version/build predates the inclusive 2026-07-31 cutoff. Mathematical code was newly written here; no external mathematical sources, mathematical libraries, data tables, third-party packages, downloads, or later-source material were used. Standard-library code is used for execution, paths, JSON, hashing, and error reporting only. Seeds: none; no randomness. No floating-point arithmetic, probabilistic factoring, or numerical error bounds are involved in the mathematics.

Artifacts in this directory:

- `finite_certify.py`: complete new audit and packaging script.
- `evidence.json`: all 255 identity rows, every used factorization and sign, divisor certificates, named examples, representative ordered-pair lists, and the complete failure/exception arrays.
- `run.log`: commands, captured worker stdout/stderr, and actual worker/parent exit statuses.
- `run.json`: SHA-256 manifest and runtime provenance.
- `report.md`: this scoped interpretation and handoff.

SHA-256 identities:

| Artifact | SHA-256 |
|---|---|
| finite_certify.py | `00a9d66bd81ca58e5cf0148fba6fa5b742c6a3285c82f46d5a1e3952aeab98f5` |
| evidence.json | `b42b9544e632431476c872b5696679d2908f05858737f6718f7d8c5a626fd72e` |
| run.log | `656020dc378a129bf6f4800f153728e8fcbc8c4ca2b2b9348a917c6447a5da11` |
| run.json | `7ec4412954f806dffb7423c85b5f6a50d54dd1256998dc3bb407940107cf6593` |
| input request.md | `7c9d7dbba7deb2dba58671b320e1888a1e7770211a8964af0e6c12a3ab2abf0f` |
| input protocol.md | `e712830b3febe6e3fcaf0479c7aa9fc30f23aa4fcc5e1f45088f736f9c161f2b` |

A separate post-run standard-library JSON/hash check recomputed every artifact hash listed in `run.json`: `artifact_hash_mismatches=[]`, exit status 0. Its additional selected-factorization and boundary-row summaries agreed with the tables above; it did not rerun the range audit.

## Exit statuses and failures

- Initial preflight `ls -ld` of `nl` and `nl/code-executor`, chained to `python3 --version`: exit 1 because the owned output directory did not yet exist. `nl` existed; the chained version command did not execute. No mathematical code had run.
- After this parent-directory check, `mkdir` of the owned directory, `python3 --version`, and `command -v python3`: exit 0; frontend `/usr/bin/python3`, version 3.9.6.
- Isolated Python version/executable query: exit 0.
- Owned-directory check followed by the reproduction command: exit 0. Child actual exit 0; parent exit 0; stderr empty.
- Post-run hash verification and selected-output summarization: exit 0.
- Mathematical assertion failures: **none**, represented by `failed_assertions: []`.
- Unhandled audit exceptions: **none**, represented by `exceptions: []`.

The expected failures of candidate decompositions are mathematical outcomes asserted successfully, not failed program assertions. The unavailable team-message channel is a communication limitation, not a numerical failure.

## Remaining obligations / next owner

Leader: confirm whether the explicit three candidates coincide with the intended PB three-test definition; if not, supply the exact three formulas for a separate finite audit. The arithmetic here remains valid for the formulas actually recorded.

All universal proof obligations remain outside this deliverable: the counting identity for arbitrary N, positivity of R for every admissible even N, any uniform finite-template claim, and the faithful fully checked Lean theorem. This report certifies no universal theorem and gives **no global mathematical conclusion** about the original conjecture.
