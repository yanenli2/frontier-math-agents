import Statement.Partial

set_option autoImplicit false

namespace ArithmeticStatement

theorem lambda_six :
  lambda 6 = (1 : ℤ)

theorem lambda_seven :
  lambda 7 = (-1 : ℤ)

theorem twelve_two_sign_seed :
  HasSignedRepresentation (-1 : ℤ) 12 ∧
    HasSignedRepresentation (1 : ℤ) 12

theorem representation_multiple_twelve (t : ℕ) (ht : 0 < t) :
  HasRepresentation (12 * t)

theorem representation_multiple_four_of_lambda_one {m : ℕ}
    (hm : 0 < m) (hSign : lambda m = (1 : ℤ)) :
  HasRepresentation (4 * m)

theorem representation_multiple_four_of_even {m : ℕ}
    (hm : 0 < m) (hEven : Even m) :
  HasRepresentation (4 * m)

theorem representation_multiple_four_of_three_dvd {m : ℕ}
    (hm : 0 < m) (hThree : 3 ∣ m) :
  HasRepresentation (4 * m)

theorem representation_multiple_four_of_sum_two_squares {m u v : ℕ}
    (hm : 0 < m) (hSum : m = u ^ 2 + v ^ 2) :
  HasRepresentation (4 * m)

theorem prime_one_mod_four_eq_sum_two_squares {p : ℕ}
    (hp : Nat.Prime p) (hMod : p % 4 = 1) :
  ∃ u v : ℕ, p = u ^ 2 + v ^ 2

theorem representation_four_prime_one_mod_four {p : ℕ}
    (hp : Nat.Prime p) (hMod : p % 4 = 1) :
  HasRepresentation (4 * p)

theorem prime_divisor_positive_sign_cofactor {m p : ℕ}
    (hm : 0 < m) (hSign : lambda m = (-1 : ℤ))
    (hp : Nat.Prime p) (hDiv : p ∣ m) :
  ∃ d : ℕ, 0 < d ∧ lambda d = (1 : ℤ) ∧ m = d * p

theorem exists_prime_factor_of_lambda_neg_one {m : ℕ}
    (hm : 0 < m) (hSign : lambda m = (-1 : ℤ)) :
  ∃ p d : ℕ,
    Nat.Prime p ∧ 0 < d ∧ lambda d = (1 : ℤ) ∧ m = d * p

theorem representation_multiple_four_of_prime_divisor {m p : ℕ}
    (hm : 0 < m) (hSign : lambda m = (-1 : ℤ))
    (hp : Nat.Prime p) (hDiv : p ∣ m)
    (hCore : HasRepresentation (4 * p)) :
  HasRepresentation (4 * m)

theorem representation_multiple_four_of_prime_one_mod_four_dvd {m p : ℕ}
    (hm : 0 < m) (hp : Nat.Prime p)
    (hDiv : p ∣ m) (hMod : p % 4 = 1) :
  HasRepresentation (4 * m)

theorem exists_prime_one_mod_four_of_lambda_neg_one {m : ℕ}
    (hm : 0 < m) (hMod : m % 4 = 1)
    (hSign : lambda m = (-1 : ℤ)) :
  ∃ p : ℕ, Nat.Prime p ∧ p ∣ m ∧ p % 4 = 1

theorem representation_multiple_four_of_mod_four_one {m : ℕ}
    (hm : 0 < m) (hMod : m % 4 = 1) :
  HasRepresentation (4 * m)

theorem representation_multiple_four_of_mod_four_ne_three {m : ℕ}
    (hm : 0 < m) (hMod : m % 4 ≠ 3) :
  HasRepresentation (4 * m)

theorem multiple_four_iff_odd_prime_core :
  (∀ m : ℕ, 0 < m → HasRepresentation (4 * m)) ↔
    ∀ p : ℕ, Nat.Prime p → p ≠ 2 → HasRepresentation (4 * p)

theorem multiple_four_iff_prime_three_mod_four_core :
  (∀ m : ℕ, 0 < m → HasRepresentation (4 * m)) ↔
    ∀ p : ℕ, Nat.Prime p → 7 ≤ p → p % 4 = 3 →
      HasRepresentation (4 * p)

end ArithmeticStatement
