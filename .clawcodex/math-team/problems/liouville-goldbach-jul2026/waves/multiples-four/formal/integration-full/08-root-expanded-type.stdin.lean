import Statement
set_option autoImplicit false
#check (id (α := ∀ m : ℕ, 0 < m → ∃ a b : ℕ,
    0 < a ∧ 0 < b ∧ 4 * m = a + b ∧
    (-1 : ℤ) ^ a.primeFactorsList.length = (-1 : ℤ) ∧
    (-1 : ℤ) ^ b.primeFactorsList.length = (-1 : ℤ))
  ArithmeticStatement.representation_multiple_four)
#print axioms ArithmeticStatement.representation_multiple_four
