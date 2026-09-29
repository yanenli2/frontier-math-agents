import Statement.Partial

set_option autoImplicit false

#print ArithmeticStatement.omega
#print ArithmeticStatement.lambda
#print ArithmeticStatement.HasSignedRepresentation
#print ArithmeticStatement.HasRepresentation
#print axioms ArithmeticStatement.omega
#print axioms ArithmeticStatement.lambda
#print axioms ArithmeticStatement.HasSignedRepresentation
#print axioms ArithmeticStatement.HasRepresentation

#check fun (N : ℕ) (h : ArithmeticStatement.HasRepresentation N) =>
  (show ∃ a b : ℕ,
    0 < a ∧ 0 < b ∧ N = a + b ∧
      ArithmeticStatement.lambda a = (-1 : ℤ) ∧
      ArithmeticStatement.lambda b = (-1 : ℤ) from h)

#check fun (N : ℕ)
    (h : ∃ a b : ℕ,
      0 < a ∧ 0 < b ∧ N = a + b ∧
        ArithmeticStatement.lambda a = (-1 : ℤ) ∧
        ArithmeticStatement.lambda b = (-1 : ℤ)) =>
  (show ArithmeticStatement.HasRepresentation N from h)

#check fun (a : ℕ) (ha : 0 < a)
    (hSign : ArithmeticStatement.lambda a = (-1 : ℤ)) =>
  (show ArithmeticStatement.HasRepresentation (a + a) from
    ⟨a, a, ha, ha, rfl, hSign, hSign⟩)

#eval Nat.primeFactorsList 1
#eval ArithmeticStatement.omega 1
#eval ArithmeticStatement.lambda 1
#eval Nat.primeFactorsList 2
#eval ArithmeticStatement.lambda 2
#eval Nat.primeFactorsList 4
#eval ArithmeticStatement.omega 4
#eval ArithmeticStatement.lambda 4
#eval decide ((0 : ℕ) < 1)
#eval decide ((0 : ℕ) < 0)
#eval decide ((0 : ℕ) < 2 ∧ 0 < (2 : ℕ) ∧ 4 * (1 : ℕ) = 2 + 2 ∧
  ArithmeticStatement.lambda 2 = (-1 : ℤ) ∧
  ArithmeticStatement.lambda 2 = (-1 : ℤ))
