import Mathlib.Data.Nat.Factors
import Mathlib.Algebra.Group.Even

namespace ArithmeticStatement

def omega (n : ℕ) : ℕ := n.primeFactorsList.length

def lambda (n : ℕ) : ℤ := (-1 : ℤ) ^ omega n

def Target : Prop :=
  ∀ N : ℕ, Even N → 2 < N →
    ∃ a b : ℕ,
      0 < a ∧ 0 < b ∧ N = a + b ∧
        lambda a = (-1 : ℤ) ∧ lambda b = (-1 : ℤ)

end ArithmeticStatement
