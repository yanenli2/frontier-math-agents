import Mathlib.Data.Nat.Factors

namespace ArithmeticStatement

def omega (n : ℕ) : ℕ := n.primeFactorsList.length

def lambda (n : ℕ) : ℤ := (-1 : ℤ) ^ omega n

def HasSignedRepresentation (s : ℤ) (N : ℕ) : Prop :=
  ∃ a b : ℕ,
    0 < a ∧ 0 < b ∧ N = a + b ∧
      lambda a = s ∧ lambda b = s

def HasRepresentation (N : ℕ) : Prop :=
  HasSignedRepresentation (-1 : ℤ) N

theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :
  HasRepresentation (4 * m)

end ArithmeticStatement
