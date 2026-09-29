import Statement.Partial
import Mathlib.NumberTheory.SumTwoSquares

set_option autoImplicit false

namespace ArithmeticStatement

theorem lambda_six :
  lambda 6 = (1 : ℤ) := by
  calc
    lambda 6 = lambda 2 * lambda 3 := lambda_mul (u := 2) (v := 3) (by decide) (by decide)
    _ = 1 := by rw [lambda_two, lambda_three]; decide

theorem lambda_seven :
  lambda 7 = (-1 : ℤ) :=
  lambda_prime Nat.prime_seven

theorem twelve_two_sign_seed :
  HasSignedRepresentation (-1 : ℤ) 12 ∧
    HasSignedRepresentation (1 : ℤ) 12 := by
  constructor
  · exact ⟨5, 7, by decide, by decide, rfl, lambda_five, lambda_seven⟩
  · exact ⟨6, 6, by decide, by decide, rfl, lambda_six, lambda_six⟩

theorem representation_multiple_twelve (t : ℕ) (ht : 0 < t) :
  HasRepresentation (12 * t) :=
  representation_two_sign_seed twelve_two_sign_seed.1 twelve_two_sign_seed.2 t ht

theorem representation_multiple_four_of_lambda_one {m : ℕ}
    (hm : 0 < m) (hSign : lambda m = (1 : ℤ)) :
  HasRepresentation (4 * m) := by
  have hneg : lambda (2 * m) = (-1 : ℤ) := by rw [lambda_two_mul hm, hSign]
  have hfactor : 4 * m = 2 * (2 * m) := by ring
  rw [hfactor]
  exact representation_double (Nat.mul_pos (by decide) hm) hneg

theorem representation_multiple_four_of_even {m : ℕ}
    (hm : 0 < m) (hEven : Even m) :
  HasRepresentation (4 * m) := by
  obtain ⟨k, hk⟩ := hEven
  have hkpos : 0 < k := by omega
  have hfactor : 4 * m = 8 * k := by rw [hk]; ring
  rw [hfactor]
  exact representation_multiple_eight k hkpos

theorem representation_multiple_four_of_three_dvd {m : ℕ}
    (hm : 0 < m) (hThree : 3 ∣ m) :
  HasRepresentation (4 * m) := by
  obtain ⟨t, ht⟩ := hThree
  have htpos : 0 < t := by omega
  have hfactor : 4 * m = 12 * t := by rw [ht]; ring
  rw [hfactor]
  exact representation_multiple_twelve t htpos

theorem representation_multiple_four_of_sum_two_squares {m u v : ℕ}
    (hm : 0 < m) (hSum : m = u ^ 2 + v ^ 2) :
  HasRepresentation (4 * m) := by
  have hordered : ∀ a b : ℕ, b < a → m = a ^ 2 + b ^ 2 → HasRepresentation (4 * m) := by
    intro a b hab hsum
    obtain ⟨w, rfl⟩ := Nat.exists_eq_add_of_le (Nat.le_of_lt hab)
    have hw : 0 < w := by omega
    have hroot : 0 < b + w + b := by omega
    have hwsq : 0 < w ^ 2 := by simpa only [pow_two] using Nat.mul_pos hw hw
    have hrootsq : 0 < (b + w + b) ^ 2 := by
      simpa only [pow_two] using Nat.mul_pos hroot hroot
    refine ⟨2 * (b + w + b) ^ 2, 2 * w ^ 2,
      Nat.mul_pos (by decide) hrootsq, Nat.mul_pos (by decide) hwsq, ?_, ?_, ?_⟩
    · rw [hsum]
      ring
    · rw [lambda_two_mul hrootsq, lambda_square hroot]
    · rw [lambda_two_mul hwsq, lambda_square hw]
  rcases lt_trichotomy u v with hlt | heq | hgt
  · exact hordered v u hlt (by simpa only [add_comm] using hSum)
  · subst v
    have hsquare : 0 < u ^ 2 := by omega
    have hfactor : 4 * m = 8 * (u ^ 2) := by rw [hSum]; ring
    rw [hfactor]
    exact representation_multiple_eight (u ^ 2) hsquare
  · exact hordered u v hgt hSum

theorem prime_one_mod_four_eq_sum_two_squares {p : ℕ}
    (hp : Nat.Prime p) (hMod : p % 4 = 1) :
  ∃ u v : ℕ, p = u ^ 2 + v ^ 2 := by
  letI : Fact p.Prime := ⟨hp⟩
  obtain ⟨u, v, hsum⟩ := Nat.Prime.sq_add_sq (p := p) (by omega)
  exact ⟨u, v, hsum.symm⟩

theorem representation_four_prime_one_mod_four {p : ℕ}
    (hp : Nat.Prime p) (hMod : p % 4 = 1) :
  HasRepresentation (4 * p) := by
  obtain ⟨u, v, hsum⟩ := prime_one_mod_four_eq_sum_two_squares hp hMod
  exact representation_multiple_four_of_sum_two_squares hp.pos hsum

theorem prime_divisor_positive_sign_cofactor {m p : ℕ}
    (hm : 0 < m) (hSign : lambda m = (-1 : ℤ))
    (hp : Nat.Prime p) (hDiv : p ∣ m) :
  ∃ d : ℕ, 0 < d ∧ lambda d = (1 : ℤ) ∧ m = d * p := by
  obtain ⟨d, hd⟩ := hDiv
  have hdpos : 0 < d := by
    by_contra! hnot
    have hz : d = 0 := by omega
    rw [hz, mul_zero] at hd
    omega
  have hdSign : lambda d = (1 : ℤ) := by
    rw [hd, lambda_mul hp.pos hdpos, lambda_prime hp] at hSign
    omega
  exact ⟨d, hdpos, hdSign, by simpa only [mul_comm] using hd⟩

theorem exists_prime_factor_of_lambda_neg_one {m : ℕ}
    (hm : 0 < m) (hSign : lambda m = (-1 : ℤ)) :
  ∃ p d : ℕ,
    Nat.Prime p ∧ 0 < d ∧ lambda d = (1 : ℤ) ∧ m = d * p := by
  have hmne : m ≠ 1 := by
    intro heq
    rw [heq, lambda_one] at hSign
    contradiction
  obtain ⟨p, hp, hDiv⟩ := Nat.exists_prime_and_dvd hmne
  obtain ⟨d, hd, hdSign, hfactor⟩ := prime_divisor_positive_sign_cofactor hm hSign hp hDiv
  exact ⟨p, d, hp, hd, hdSign, hfactor⟩

theorem representation_multiple_four_of_prime_divisor {m p : ℕ}
    (hm : 0 < m) (hSign : lambda m = (-1 : ℤ))
    (hp : Nat.Prime p) (hDiv : p ∣ m)
    (hCore : HasRepresentation (4 * p)) :
  HasRepresentation (4 * m) := by
  obtain ⟨d, hd, hdSign, hfactor⟩ := prime_divisor_positive_sign_cofactor hm hSign hp hDiv
  have scaled := hasSignedRepresentation_mul hd hCore
  have hscale : d * (4 * p) = 4 * m := by rw [hfactor]; ring
  simpa [HasRepresentation, hdSign, hscale] using scaled

theorem representation_multiple_four_of_prime_one_mod_four_dvd {m p : ℕ}
    (hm : 0 < m) (hp : Nat.Prime p)
    (hDiv : p ∣ m) (hMod : p % 4 = 1) :
  HasRepresentation (4 * m) := by
  rcases lambda_sign hm with hplus | hminus
  · exact representation_multiple_four_of_lambda_one hm hplus
  · exact representation_multiple_four_of_prime_divisor hm hminus hp hDiv
      (representation_four_prime_one_mod_four hp hMod)

theorem multiple_four_iff_odd_prime_core :
  (∀ m : ℕ, 0 < m → HasRepresentation (4 * m)) ↔
    ∀ p : ℕ, Nat.Prime p → p ≠ 2 → HasRepresentation (4 * p) := by
  constructor
  · intro h p hp hpne
    exact h p hp.pos
  · intro h m hm
    by_cases hEven : Even m
    · exact representation_multiple_four_of_even hm hEven
    · rcases lambda_sign hm with hplus | hminus
      · exact representation_multiple_four_of_lambda_one hm hplus
      · obtain ⟨p, d, hp, hd, hdSign, hfactor⟩ := exists_prime_factor_of_lambda_neg_one hm hminus
        have hpne : p ≠ 2 := by
          intro heq
          apply hEven
          exact ⟨d, by rw [hfactor, heq]; ring⟩
        have hDiv : p ∣ m := ⟨d, by rw [hfactor]; ring⟩
        exact representation_multiple_four_of_prime_divisor hm hminus hp hDiv (h p hp hpne)

end ArithmeticStatement

#check Nat.Prime.sq_add_sq
#print axioms Nat.Prime.sq_add_sq
#print axioms ArithmeticStatement.prime_one_mod_four_eq_sum_two_squares
#print axioms ArithmeticStatement.representation_four_prime_one_mod_four
#print axioms ArithmeticStatement.prime_divisor_positive_sign_cofactor
#print axioms ArithmeticStatement.exists_prime_factor_of_lambda_neg_one
#print axioms ArithmeticStatement.representation_multiple_four_of_prime_divisor
#print axioms ArithmeticStatement.representation_multiple_four_of_prime_one_mod_four_dvd
#print axioms ArithmeticStatement.multiple_four_iff_odd_prime_core
#print axioms ArithmeticStatement.lambda_six
#print axioms ArithmeticStatement.lambda_seven
#print axioms ArithmeticStatement.twelve_two_sign_seed
#print axioms ArithmeticStatement.representation_multiple_twelve
#print axioms ArithmeticStatement.representation_multiple_four_of_lambda_one
#print axioms ArithmeticStatement.representation_multiple_four_of_even
#print axioms ArithmeticStatement.representation_multiple_four_of_three_dvd
#print axioms ArithmeticStatement.representation_multiple_four_of_sum_two_squares
