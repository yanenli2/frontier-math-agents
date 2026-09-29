import Statement.Partial
import Mathlib.NumberTheory.LegendreSymbol.Basic

set_option autoImplicit false
set_option pp.universes false

#check @ArithmeticStatement.lambda_sign
#check @ArithmeticStatement.lambda_mul
#check @ArithmeticStatement.lambda_prime
#check @ArithmeticStatement.lambda_three
#check @ZMod.val_pos
#check @ZMod.val_lt
#check @ZMod.val_natCast_of_lt
#check @ZMod.natCast_zmod_val
#check @ZMod.neg_val
#check @ZMod.natCast_eq_zero_iff
#check @ZMod.intCast_zmod_eq_zero_iff_dvd
#check @ZMod.natCast_injOn_lt
#check @ZMod.natCast_eq_natCast_iff
#check @ZMod.exists_sq_eq_neg_one_iff
#check @isSquare_iff_exists_sq
#check @Finset.exists_ne_map_eq_of_card_lt_of_maps_to
#check @Finset.card_range
#check @Nat.Prime.eq_one_or_self_of_dvd
#check @Nat.Prime.dvd_iff_eq
#check @Nat.Prime.eq_two_or_odd
#check @Nat.odd_mod_four_iff
#check @Nat.exists_prime_and_dvd
#check @Nat.le_of_dvd
#check @Nat.mul_div_le
#check @Nat.div_lt_iff_lt_mul
#check @Nat.div_mul_le_self
#check @Nat.lt_mul_div_succ
#check @Nat.mul_div_cancel'
#check @Nat.div_mul_cancel
#check @Int.natAbs_coe_sub_coe_lt_of_lt
#check @Int.natAbs_neg
#check @Int.natCast_natAbs
#check @Int.natAbs_ofNat
#check @Nat.strong_induction_on
#print axioms ZMod.exists_sq_eq_neg_one_iff
#print axioms Finset.exists_ne_map_eq_of_card_lt_of_maps_to
