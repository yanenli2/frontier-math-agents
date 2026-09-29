Mode: DISCOVERY — conjectural; no proof weight.

# Dependency-ordered decomposition, version 1

All edges describe a proposed proof plan, not accepted theorem dependencies. All statements are OPEN until separately justified and reviewed. A review of this plan would certify only the decomposition/assembly implication, not the missing lemma proofs.

## Artifact map

- `target-contract-v1.md`: exact target, domains, finite sums, casts, and success boundary.
- `lemmas/counting-v1.md`: C01-C09 and conditional assembly A01.
- `lemmas/keystone-v1.md`: K01, optional estimate/tail criteria K02-K03, and partial-sum criterion K04.
- `lemmas/elementary-families-v1.md`: E01-E06, exact constructions and signs.
- `lemmas/residual-v1.md`: residual target ER01 and conditional assembly A02.
- `source-scope-v1.md`: supplied Mangerel v2 pages 1-4 and its precise insufficiency for K01.
- `obligation-ledger-v1.md`: load-bearing obligations, statuses, and next owners.
- `branch-queue-v1.md`: ranked independent work and precise source/computation requests.
- `formal-handoff-v1.md`: statement-preserving formalization targets and audit gates.

## Main acyclic graph

D denotes only the exact definitions/domain contract, not a theorem.

    D -> C01 sign dichotomy
    D -> C02 finite interval, cardinality, reflection
    C02 -> C03 reflected sum reindexing
    C02 -> C04 ordered-pair bijection
    C01 -> C05 signed indicator expansion
    C02 -> C06 cardinality/indicator sum
    (C02,C03,C05,C06) -> C07 exact counting identity
    C04 -> C08 count/existence bridge
    C07 -> C09 exact positivity equivalences

    D -> K01 universal pointwise keystone [NO PROOF SUPPLIED]
    (C08,C09,K01) -> A01 exact original target

No edge points from A01 or the target back to K01. K01 cannot be proved by assuming the existence conclusion. The exact identity does not close K01.

## Optional estimate branch

    D + ordered arithmetic -> K02 sufficient margin implication
    genuinely proved uniform estimates + K02 -> explicit tail positivity
    (explicit tail positivity, rigorous finite coverage,C09) -> K03
    K03 -> K01 -> A01

The phrase “genuinely proved uniform estimates” denotes missing mathematical/source obligations, not a hidden hypothesis declared true. All constants, strict inequalities, quantifiers and thresholds must be supplied.

Independently:

    (C01,C02,finite-set cardinality bounds) -> K04
    K04 + L(N-1)<0 -> R(N)>0 for that N

No universal sign assertion about L is included. The stronger universal-negative-partial-sum route requires its own proof or falsification work.

## Elementary construction branch

    D -> E01 multiplicativity, squares, primes, finite signs
    (C01,E01) -> E02 diagonal family
    E01 -> E03 sign-controlled scaling
    (C01,E03) -> E04 two-sign seed transfer
    (E01,E04,finite seed sums) -> E05 all multiples of 8,10,12,14,18
    (E01,E03,integer exponent parity) -> E06 square families/powers of two

    D -> ER01 residual family [NO PROOF SUPPLIED]
    (C01,E02,E05,ER01,positive quotient from divisibility) -> A02 original target

This graph also has no target-to-residual feedback. E05 is unconditional as a proposed mathematical statement, but its present status is unproved/unreviewed; it is not an accepted partial theorem merely because its construction is explicit.

## Checked dependency preconditions

| Edge/application | Required input | Why it is available in the planned application |
|---|---|---|
| C01 inside C05 | a,b positive | C05 states this; for b=N-a, C02 supplies it |
| C02-C09 at a target N | N>=2 | target has N>2 |
| C03 reindexing | finite common domain and bijection | C02 explicitly supplies I_N and its reflection involution |
| C04 pair parametrization | positive witnesses bounded by N-1 | comes from a+b=N and the other witness being at least 1; this is part of C04's obligation |
| C05-C07 arithmetic | lambda in Z; indicator in Z | definitions and explicit casts, not natural subtraction |
| C06/C07 count convention | ordered pairs, diagonal once | R is indexed by every a in I_N; C04 establishes the pair interpretation |
| C09 strict positivity | K=4R and natural-to-integer order bridge | C07 plus O-C09; K>=0 alone is insufficient |
| K02 margin | M=N-1>0, alpha,beta>=0, 2alpha+beta<1 | N>=2; constants and bounds must be supplied by the prospective estimate theorem |
| K03 finite/tail split | known N0, tail includes N0, finite branch excludes it | explicit statement; finite coverage is a separate obligation |
| E01 multiplication | both factors positive | every family parameter and every coefficient is positive |
| E02 halving | N even and positive | original domain; a separate formal halving/coercion check remains |
| E03 scaling | SAME positive m for both summands; opposite factor sign | explicitly in the statement, checked per selected branch |
| E04 sign split | lambda(m) is +/-1 | m>=1 and C01 |
| E05 application | positive seed coefficients and exact seed signs/sums | finite checks assigned to E01/E05, not assumed from display |
| E06 exponent cases | k>=2 and exhaustive parity/divisibility split | stated; construction of integer square exponents is an obligation |
| A02 divisibility case | quotient m>=1 | N>0, d>0, d divides N; positive quotient bridge assigned explicitly |
| A02 residual case | every seed nondivides N and lambda(N)=-1 | complements of the preceding exhaustive cases; not an added hypothesis on T0 |

The table checks that the proposed statements contain enough hypotheses. It does not claim that their proofs have been completed.

## Independent frontier and blockers

Can be assigned immediately and in parallel by the leader, subject to worker limits:

1. C01: elementary signed exponent dichotomy and lambda(1).
2. C02/C04: finite integer interval reflection and ordered-pair parametrization.
3. E01: positive multiplicativity and exact small signs, independently of the counting route.
4. Formal statement/domain fidelity and eligible toolchain/library audit, independently of all proof search.
5. Source review of a genuinely stronger pointwise theorem, or bounded experiments against stronger candidate premises, independently of local lemma proofs.

Once C01/C02 are available, C03/C05/C06 form the next cheap frontier. Once E01 is available, the explicit multiple-of-8 construction is a small, useful unconditional-family proof target.

**Counting keystone blocker:** K01, a strict pointwise inequality equivalent to the target after the identity.

**Elementary-coverage blocker:** ER01 or a replacement theorem covering every residual N. Explicit families do not resolve this global bridge.

**Formal blocker outside this worker's scope:** the approved statement snapshot and actually verified eligible environment were not supplied to this worker. The handoff therefore proposes interfaces without asserting any compilation or library eligibility result.

## Conditional terminal assembly

Route A: an admissible N satisfies N>=2; K01 gives strict positivity of K(N); C09 gives R(N)>0; C08 produces positive a,b with the required sum and signs. This reaches the exact target without restricting the witnesses. Every use remains conditional on the unproved K01 and local lemmas.

Route B: split by lambda(N). The positive-sign case is assigned to E02. In the negative-sign case, divisibility by a seed in D is assigned to E05 after producing a positive quotient; the complementary cases are exactly ER01. C01 ensures there is no third sign. This also reaches the exact target only conditionally on ER01 and the local family lemmas.

No combination of branch diagrams, small-case data, the counting identity, or the supplied convolution nonconstancy theorem is itself a full proof.
