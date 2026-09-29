import Statement
set_option autoImplicit false
#check @ArithmeticStatement.omega
#check @ArithmeticStatement.lambda
#check @ArithmeticStatement.HasSignedRepresentation
#check @ArithmeticStatement.HasRepresentation
#check @ArithmeticStatement.FourWork.residueLambda
#check @ArithmeticStatement.FourWork.GoodMultiplier
#check @ArithmeticStatement.FourWork.lambda_reflection_eq_one_of_neg
#check @ArithmeticStatement.FourWork.lambda_double_reflection_eq_neg_one_of_pos
#check @ArithmeticStatement.FourWork.three_not_dvd_of_positive_pair
#check @ArithmeticStatement.FourWork.positive_pair_gap_step
#check @ArithmeticStatement.FourWork.no_positive_pair
#check @ArithmeticStatement.FourWork.lambda_antireflection_of_no_representation
#check @ArithmeticStatement.FourWork.cyclic_short_multiple
#check @ArithmeticStatement.FourWork.residueLambda_natCast
#check @ArithmeticStatement.FourWork.residueLambda_sign
#check @ArithmeticStatement.FourWork.residueLambda_neg
#check @ArithmeticStatement.FourWork.goodMultiplier_one
#check @ArithmeticStatement.FourWork.goodMultiplier_neg
#check @ArithmeticStatement.FourWork.goodMultiplier_natCast_step
#check @ArithmeticStatement.FourWork.residueLambda_mul
#check @ArithmeticStatement.FourWork.lambda_eq_one_of_isSquare
#check @ArithmeticStatement.FourWork.prime_dvd_quarter_isSquare
#check @ArithmeticStatement.FourWork.exists_small_prime_isSquare
#check @ArithmeticStatement.representation_four_prime_three_mod_four
#check @ArithmeticStatement.representation_multiple_four
#check @ArithmeticStatement.lambda_six
#check @ArithmeticStatement.lambda_seven
#check @ArithmeticStatement.twelve_two_sign_seed
#check @ArithmeticStatement.representation_multiple_twelve
#check @ArithmeticStatement.representation_multiple_four_of_lambda_one
#check @ArithmeticStatement.representation_multiple_four_of_even
#check @ArithmeticStatement.representation_multiple_four_of_three_dvd
#check @ArithmeticStatement.representation_multiple_four_of_sum_two_squares
#check @ArithmeticStatement.prime_one_mod_four_eq_sum_two_squares
#check @ArithmeticStatement.representation_four_prime_one_mod_four
#check @ArithmeticStatement.prime_divisor_positive_sign_cofactor
#check @ArithmeticStatement.exists_prime_factor_of_lambda_neg_one
#check @ArithmeticStatement.representation_multiple_four_of_prime_divisor
#check @ArithmeticStatement.representation_multiple_four_of_prime_one_mod_four_dvd
#check @ArithmeticStatement.exists_prime_one_mod_four_of_lambda_neg_one
#check @ArithmeticStatement.representation_multiple_four_of_mod_four_one
#check @ArithmeticStatement.representation_multiple_four_of_mod_four_ne_three
#check @ArithmeticStatement.multiple_four_iff_odd_prime_core
#check @ArithmeticStatement.multiple_four_iff_prime_three_mod_four_core
#check (ArithmeticStatement.representation_multiple_four :
  ∀ m : ℕ, 0 < m → ∃ a b : ℕ,
    0 < a ∧ 0 < b ∧ 4 * m = a + b ∧
    (-1 : ℤ) ^ a.primeFactorsList.length = (-1 : ℤ) ∧
    (-1 : ℤ) ^ b.primeFactorsList.length = (-1 : ℤ))
#print ArithmeticStatement.omega
#print ArithmeticStatement.lambda
#print ArithmeticStatement.HasSignedRepresentation
#print ArithmeticStatement.HasRepresentation
#print ArithmeticStatement.FourWork.residueLambda
#print ArithmeticStatement.FourWork.GoodMultiplier
#print ArithmeticStatement.Target
#print ArithmeticStatement.UnfinishedScaffold
#print axioms ArithmeticStatement.C
#print axioms ArithmeticStatement.FourWork.GoodMultiplier
#print axioms ArithmeticStatement.FourWork.cyclic_short_multiple
#print axioms ArithmeticStatement.FourWork.exists_small_prime_isSquare
#print axioms ArithmeticStatement.FourWork.goodMultiplier_natCast_step
#print axioms ArithmeticStatement.FourWork.goodMultiplier_neg
#print axioms ArithmeticStatement.FourWork.goodMultiplier_one
#print axioms ArithmeticStatement.FourWork.lambda_antireflection_of_no_representation
#print axioms ArithmeticStatement.FourWork.lambda_double_reflection_eq_neg_one_of_pos
#print axioms ArithmeticStatement.FourWork.lambda_eq_one_of_isSquare
#print axioms ArithmeticStatement.FourWork.lambda_reflection_eq_one_of_neg
#print axioms ArithmeticStatement.FourWork.no_positive_pair
#print axioms ArithmeticStatement.FourWork.positive_pair_gap_step
#print axioms ArithmeticStatement.FourWork.prime_dvd_quarter_isSquare
#print axioms ArithmeticStatement.FourWork.residueLambda
#print axioms ArithmeticStatement.FourWork.residueLambda_mul
#print axioms ArithmeticStatement.FourWork.residueLambda_natCast
#print axioms ArithmeticStatement.FourWork.residueLambda_neg
#print axioms ArithmeticStatement.FourWork.residueLambda_sign
#print axioms ArithmeticStatement.FourWork.three_not_dvd_of_positive_pair
#print axioms ArithmeticStatement.HasRepresentation
#print axioms ArithmeticStatement.HasSignedRepresentation
#print axioms ArithmeticStatement.I
#print axioms ArithmeticStatement.L
#print axioms ArithmeticStatement.R
#print axioms ArithmeticStatement.Target
#print axioms ArithmeticStatement.UnfinishedScaffold.mk
#print axioms ArithmeticStatement.count_pos_iff_keystone
#print axioms ArithmeticStatement.eight_two_sign_seed
#print axioms ArithmeticStatement.exists_prime_factor_of_lambda_neg_one
#print axioms ArithmeticStatement.exists_prime_one_mod_four_of_lambda_neg_one
#print axioms ArithmeticStatement.exists_prime_pair_factor_of_lambda_one
#print axioms ArithmeticStatement.four_mul_representation_count
#print axioms ArithmeticStatement.hasSignedRepresentation_mul
#print axioms ArithmeticStatement.interval_bounds
#print axioms ArithmeticStatement.interval_card_cast
#print axioms ArithmeticStatement.interval_eq_Icc
#print axioms ArithmeticStatement.keystone_ge_four_iff
#print axioms ArithmeticStatement.lambda
#print axioms ArithmeticStatement.lambda_five
#print axioms ArithmeticStatement.lambda_four
#print axioms ArithmeticStatement.lambda_mul
#print axioms ArithmeticStatement.lambda_one
#print axioms ArithmeticStatement.lambda_prime
#print axioms ArithmeticStatement.lambda_seven
#print axioms ArithmeticStatement.lambda_sign
#print axioms ArithmeticStatement.lambda_six
#print axioms ArithmeticStatement.lambda_square
#print axioms ArithmeticStatement.lambda_three
#print axioms ArithmeticStatement.lambda_two
#print axioms ArithmeticStatement.lambda_two_mul
#print axioms ArithmeticStatement.mem_I_iff
#print axioms ArithmeticStatement.mem_orderedRepresentations
#print axioms ArithmeticStatement.multiple_four_iff_odd_prime_core
#print axioms ArithmeticStatement.multiple_four_iff_prime_three_mod_four_core
#print axioms ArithmeticStatement.omega
#print axioms ArithmeticStatement.omega_mul
#print axioms ArithmeticStatement.omega_one
#print axioms ArithmeticStatement.orderedRepresentations
#print axioms ArithmeticStatement.orderedRepresentations_eq_image
#print axioms ArithmeticStatement.prime_divisor_positive_sign_cofactor
#print axioms ArithmeticStatement.prime_one_mod_four_eq_sum_two_squares
#print axioms ArithmeticStatement.reflection_bijection
#print axioms ArithmeticStatement.reflection_involutive
#print axioms ArithmeticStatement.reflection_mem
#print axioms ArithmeticStatement.representationIndices
#print axioms ArithmeticStatement.representation_count_eq_card_indices
#print axioms ArithmeticStatement.representation_count_eq_indicator_sum
#print axioms ArithmeticStatement.representation_count_pos_iff
#print axioms ArithmeticStatement.representation_diagonal
#print axioms ArithmeticStatement.representation_double
#print axioms ArithmeticStatement.representation_four_prime_one_mod_four
#print axioms ArithmeticStatement.representation_four_prime_three_mod_four
#print axioms ArithmeticStatement.representation_multiple_eight
#print axioms ArithmeticStatement.representation_multiple_four
#print axioms ArithmeticStatement.representation_multiple_four_of_even
#print axioms ArithmeticStatement.representation_multiple_four_of_lambda_one
#print axioms ArithmeticStatement.representation_multiple_four_of_mod_four_ne_three
#print axioms ArithmeticStatement.representation_multiple_four_of_mod_four_one
#print axioms ArithmeticStatement.representation_multiple_four_of_prime_divisor
#print axioms ArithmeticStatement.representation_multiple_four_of_prime_one_mod_four_dvd
#print axioms ArithmeticStatement.representation_multiple_four_of_sum_two_squares
#print axioms ArithmeticStatement.representation_multiple_four_of_three_dvd
#print axioms ArithmeticStatement.representation_multiple_twelve
#print axioms ArithmeticStatement.representation_scaled_sign
#print axioms ArithmeticStatement.representation_two_sign_seed
#print axioms ArithmeticStatement.sum_lambda_interval
#print axioms ArithmeticStatement.sum_lambda_reflection
#print axioms ArithmeticStatement.target_iff_count_pos
#print axioms ArithmeticStatement.target_iff_forall_hasRepresentation
#print axioms ArithmeticStatement.target_iff_pointwise_keystone
#print axioms ArithmeticStatement.target_iff_prime_product_core
#print axioms ArithmeticStatement.twelve_two_sign_seed
#print axioms ArithmeticStatement.two_sign_indicator
#print axioms Finset.card_image_of_injective
#print axioms Finset.card_pos
#print axioms Finset.exists_ne_map_eq_of_card_lt_of_maps_to
#print axioms Finset.mem_filter
#print axioms Finset.mem_image
#print axioms Finset.mem_product
#print axioms Finset.mul_sum
#print axioms Finset.product_eq_sprod
#print axioms Finset.sum_add_distrib
#print axioms Finset.sum_const
#print axioms Finset.sum_filter
#print axioms Finset.sum_nbij'
#print axioms Finset.sum_sub_distrib
#print axioms GaussianInt.prime_iff_mod_four_eq_three_of_nat_prime
#print axioms GaussianInt.sq_add_sq_of_nat_prime_of_not_irreducible
#print axioms Int.cast_pow
#print axioms Int.natAbs_eq
#print axioms Int.natAbs_pos
#print axioms List.Perm.length_eq
#print axioms List.length_append
#print axioms List.prod_cons
#print axioms Nat.Prime.eq_one_or_self_of_dvd
#print axioms Nat.Prime.eq_two_or_odd
#print axioms Nat.Prime.primeFactorsList_pow
#print axioms Nat.Prime.sq_add_sq
#print axioms Nat.card_Ico
#print axioms Nat.cast_sub
#print axioms Nat.dvd_of_mem_primeFactorsList
#print axioms Nat.exists_eq_add_of_le
#print axioms Nat.exists_prime_and_dvd
#print axioms Nat.le_of_dvd
#print axioms Nat.not_even_iff_odd
#print axioms Nat.odd_iff
#print axioms Nat.odd_mod_four_iff
#print axioms Nat.perm_primeFactorsList_mul
#print axioms Nat.primeFactorsList
#print axioms Nat.primeFactorsList_one
#print axioms Nat.primeFactorsList_prime
#print axioms Nat.prime_five
#print axioms Nat.prime_of_mem_primeFactorsList
#print axioms Nat.prime_seven
#print axioms Nat.prime_three
#print axioms Nat.prime_two
#print axioms Nat.prod_primeFactorsList
#print axioms Nat.strong_induction_on
#print axioms Nat.sub_sub_self
#print axioms ZMod.exists_sq_eq_neg_one_iff
#print axioms ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_one
#print axioms ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_three
#print axioms ZMod.exists_sq_eq_two_iff
#print axioms ZMod.instField
#print axioms ZMod.natCast_eq_zero_iff
#print axioms ZMod.natCast_mod
#print axioms ZMod.natCast_zmod_val
#print axioms ZMod.neg_val
#print axioms ZMod.val_lt
#print axioms ZMod.val_natCast_of_lt
#print axioms ZMod.val_pos
#print axioms mul_left_cancel₀
#print axioms mul_ne_zero
#print axioms neg_one_pow_eq_ite
#print axioms pow_add
