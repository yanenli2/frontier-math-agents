Mode: DISCOVERY — conjectural; no proof weight.

# Residual branch and coverage assembly, version 1

These are unproved statements, not a claim that the elementary family list covers the original target.

For positive n let lambda(n)=(-1)^(Omega(n)) in Z, with multiplicity-counted Omega and Omega(1)=0. Write G(N) for the existence of positive integers a,b with N=a+b and lambda(a)=lambda(b)=-1. Let D={8,10,12,14,18}.

## ER01 — Exact remaining elementary-family branch (OPEN)

Statement: For every integer N such that

    N is even, N>2, lambda(N)=-1,
    and d does not divide N for every d in D,

G(N) holds.

No proof or candidate universal construction is supplied. The nondivisibility assumptions describe only the residual subproblem after the fixed families are accepted; they must not be added to or substituted for the original target.

## A02 — Conditional assembly from families plus the residual branch

Statement: Assume all three of the following statements:

1. For every even integer N>2 with lambda(N)=+1, G(N) holds.
2. For every d in D and every integer m>=1, G(dm) holds.
3. ER01 holds.

Then for every even integer N>2, G(N) holds.

Dependencies: E02 supplies statement 1, E05 supplies statement 2, ER01 supplies statement 3, and C01 supplies the exhaustive sign dichotomy at the positive input N. A divisibility case d|N must produce a positive integer quotient m with N=dm, using N>0 and d>0; this positivity bridge is mandatory.

Named obligation: O-G01. This assembly is acyclic: ER01 is a new independent proof task, not something deduced from the desired universal conclusion. Until ER01 (or a different coverage theorem) is proved, E02/E05 remain partial results only.
