# Exact continuation request

> for the next step, I would suggest you try to prove: "The required representation for every positive multiple of 4". Please use the team to do the prove of this Lemma.

## Target interface

Using the existing approved definitions, the requested lemma is:

```lean
theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :
  ArithmeticStatement.HasRepresentation (4 * m)
```

`HasRepresentation N` means there exist a,b : ℕ with 0<a, 0<b, N=a+b and lambda(a)=lambda(b)=-1. `lambda(n)=(-1)^omega(n)` in ℤ and `omega(n)=n.primeFactorsList.length`, counting multiplicity. All m>0, including m=1, are included. Equal summands are allowed. No sign, parity, prime, or coprimality restriction may be added to m or witnesses.

The original problem request at ../../request.md and its source cutoff 2026-07-31 inclusive remain in force. This is a new partial target, not authorization to weaken the original all-even conjecture. Freeze the earlier proof/definition/source snapshots. Only the integrator may extend the master after fresh statement fidelity, mathematical review, actual pinned compilation, and axiom checks. Failure to prove the new lemma must be reported as unresolved, not inferred from examples.
