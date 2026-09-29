import Statement.FourPartial
import Statement.FourWork.Descent.Ternary
import Statement.FourWork.Character.Rigidity
import Statement.FourWork.Character.ResiduePrime

set_option autoImplicit false

namespace ArithmeticStatement

theorem representation_four_prime_three_mod_four {p : ℕ}
    (hp : Nat.Prime p) (hLower : 7 ≤ p) (hMod : p % 4 = 3) :
    HasRepresentation (4 * p) := by
  by_contra hno
  have hanti := FourWork.lambda_antireflection_of_no_representation
    hp (by omega) (by omega) hno
  obtain ⟨r, hr, _, _, hrp, hsquare⟩ := FourWork.exists_small_prime_isSquare hp hLower hMod
  have hpositive := FourWork.lambda_eq_one_of_isSquare hp hanti hr.pos hrp hsquare
  have hnegative := lambda_prime hr
  omega

theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :
    HasRepresentation (4 * m) := by
  exact (multiple_four_iff_prime_three_mod_four_core.mpr
    (fun p hp hLower hMod => representation_four_prime_three_mod_four hp hLower hMod)) m hm

end ArithmeticStatement

#check ArithmeticStatement.representation_four_prime_three_mod_four
#check ArithmeticStatement.representation_multiple_four
#print axioms ArithmeticStatement.representation_four_prime_three_mod_four
#print axioms ArithmeticStatement.representation_multiple_four
#print axioms ArithmeticStatement.FourWork.lambda_reflection_eq_one_of_neg
#print axioms ArithmeticStatement.FourWork.lambda_double_reflection_eq_neg_one_of_pos
#print axioms ArithmeticStatement.FourWork.three_not_dvd_of_positive_pair
#print axioms ArithmeticStatement.FourWork.positive_pair_gap_step
#print axioms ArithmeticStatement.FourWork.no_positive_pair
#print axioms ArithmeticStatement.FourWork.lambda_antireflection_of_no_representation
#print axioms ArithmeticStatement.FourWork.cyclic_short_multiple
#print axioms ArithmeticStatement.FourWork.residueLambda
#print axioms ArithmeticStatement.FourWork.GoodMultiplier
#print axioms ArithmeticStatement.FourWork.residueLambda_natCast
#print axioms ArithmeticStatement.FourWork.residueLambda_sign
#print axioms ArithmeticStatement.FourWork.residueLambda_neg
#print axioms ArithmeticStatement.FourWork.goodMultiplier_one
#print axioms ArithmeticStatement.FourWork.goodMultiplier_neg
#print axioms ArithmeticStatement.FourWork.goodMultiplier_natCast_step
#print axioms ArithmeticStatement.FourWork.residueLambda_mul
#print axioms ArithmeticStatement.FourWork.lambda_eq_one_of_isSquare
#print axioms ArithmeticStatement.FourWork.prime_dvd_quarter_isSquare
#print axioms ArithmeticStatement.FourWork.exists_small_prime_isSquare
#print axioms ArithmeticStatement.lambda_six
#print axioms ArithmeticStatement.lambda_seven
#print axioms ArithmeticStatement.twelve_two_sign_seed
#print axioms ArithmeticStatement.representation_multiple_twelve
#print axioms ArithmeticStatement.representation_multiple_four_of_lambda_one
#print axioms ArithmeticStatement.representation_multiple_four_of_even
#print axioms ArithmeticStatement.representation_multiple_four_of_three_dvd
#print axioms ArithmeticStatement.representation_multiple_four_of_sum_two_squares
#print axioms ArithmeticStatement.prime_one_mod_four_eq_sum_two_squares
#print axioms ArithmeticStatement.representation_four_prime_one_mod_four
#print axioms ArithmeticStatement.prime_divisor_positive_sign_cofactor
#print axioms ArithmeticStatement.exists_prime_factor_of_lambda_neg_one
#print axioms ArithmeticStatement.representation_multiple_four_of_prime_divisor
#print axioms ArithmeticStatement.representation_multiple_four_of_prime_one_mod_four_dvd
#print axioms ArithmeticStatement.exists_prime_one_mod_four_of_lambda_neg_one
#print axioms ArithmeticStatement.representation_multiple_four_of_mod_four_one
#print axioms ArithmeticStatement.representation_multiple_four_of_mod_four_ne_three
#print axioms ArithmeticStatement.multiple_four_iff_odd_prime_core
#print axioms ArithmeticStatement.multiple_four_iff_prime_three_mod_four_core
#print axioms ArithmeticStatement.omega
#print axioms ArithmeticStatement.lambda
#print axioms ArithmeticStatement.HasSignedRepresentation
#print axioms ArithmeticStatement.HasRepresentation
#print axioms ArithmeticStatement.lambda_one
#print axioms ArithmeticStatement.lambda_sign
#print axioms ArithmeticStatement.lambda_mul
#print axioms ArithmeticStatement.lambda_prime
#print axioms ArithmeticStatement.lambda_two
#print axioms ArithmeticStatement.lambda_three
#print axioms ArithmeticStatement.lambda_four
#print axioms ArithmeticStatement.lambda_five
#print axioms ArithmeticStatement.lambda_two_mul
#print axioms ArithmeticStatement.lambda_square
#print axioms ArithmeticStatement.hasSignedRepresentation_mul
#print axioms ArithmeticStatement.representation_double
#print axioms ArithmeticStatement.representation_two_sign_seed
#print axioms ArithmeticStatement.representation_multiple_eight
#print axioms ArithmeticStatement.omega_mul
#print axioms Nat.perm_primeFactorsList_mul
#print axioms Nat.prod_primeFactorsList
#print axioms Nat.Prime.sq_add_sq
#print axioms ZMod.exists_sq_eq_neg_one_iff
#print axioms ZMod.exists_sq_eq_two_iff
#print axioms ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_one
#print axioms ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_three
#print axioms Finset.exists_ne_map_eq_of_card_lt_of_maps_to
#print axioms ZMod.instField
#print axioms Nat.strong_induction_on
