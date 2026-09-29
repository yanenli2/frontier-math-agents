import Statement.FourWork.Character.ResidueValue
import Statement.FourWork.Descent.Cyclic

set_option autoImplicit false

namespace ArithmeticStatement
namespace FourWork

theorem goodMultiplier_natCast_step {p n : ℕ} (hp : Nat.Prime p)
    (hanti : ∀ j : ℕ, 0 < j → j < p → lambda (p - j) = -lambda j)
    (hn : 0 < n) (hnp : n < p)
    (hsmall : ∀ j : ℕ, 0 < j → j < n → GoodMultiplier p (j : ZMod p)) :
    GoodMultiplier p (n : ZMod p) := by
  letI : Fact p.Prime := ⟨hp⟩
  by_cases hn1 : n = 1
  · subst n
    simpa only [Nat.cast_one] using goodMultiplier_one hp
  have hn2 : 2 ≤ n := by omega
  have hn0 : (n : ZMod p) ≠ 0 := by
    apply ZMod.val_pos.mp
    rwa [ZMod.val_natCast_of_lt hnp]
  refine ⟨hn0, ?_⟩
  intro z hz
  obtain ⟨k, d, hk0, hkn, hd, hnd, hkz⟩ := cyclic_short_multiple hp hn2 hnp z hz
  have hkabs : GoodMultiplier p (k.natAbs : ZMod p) :=
    hsmall k.natAbs (Int.natAbs_pos.mpr hk0) hkn
  have hkgood : GoodMultiplier p (k : ZMod p) := by
    rcases Int.natAbs_eq k with hk | hk
    · have hcast : (k : ZMod p) = (k.natAbs : ZMod p) := by
        simpa only [Int.cast_natCast] using congrArg (fun j : ℤ => (j : ZMod p)) hk
      rw [hcast]
      exact hkabs
    · have hcast : (k : ZMod p) = -(k.natAbs : ZMod p) := by
        simpa only [Int.cast_neg, Int.cast_natCast] using
          congrArg (fun j : ℤ => (j : ZMod p)) hk
      rw [hcast]
      exact goodMultiplier_neg hp hanti hkabs
  have hdlt : d < p := by nlinarith
  have hbridge : residueLambda p ((n : ZMod p) * (d : ZMod p)) =
      residueLambda p (n : ZMod p) * residueLambda p (d : ZMod p) := by
    rw [← Nat.cast_mul, residueLambda_natCast hnd,
      residueLambda_natCast hnp, residueLambda_natCast hdlt]
    exact lambda_mul hn hd
  have hknz : (k : ZMod p) * ((n : ZMod p) * z) =
      (n : ZMod p) * (d : ZMod p) := by
    rw [← hkz]
    ring
  have hprod := hkgood.2 ((n : ZMod p) * z) (mul_ne_zero hn0 hz)
  rw [hknz, hbridge, ← hkz, hkgood.2 z hz] at hprod
  have hnonzero : residueLambda p (k : ZMod p) ≠ 0 := by
    rcases residueLambda_sign hkgood.1 with h | h <;> rw [h] <;> decide
  apply mul_left_cancel₀ hnonzero
  calc
    residueLambda p (k : ZMod p) * residueLambda p ((n : ZMod p) * z) =
        residueLambda p (n : ZMod p) *
          (residueLambda p (k : ZMod p) * residueLambda p z) := hprod.symm
    _ = residueLambda p (k : ZMod p) *
        (residueLambda p (n : ZMod p) * residueLambda p z) := by ring

theorem residueLambda_mul {p : ℕ} (hp : Nat.Prime p)
    (hanti : ∀ n : ℕ, 0 < n → n < p → lambda (p - n) = -lambda n)
    {a b : ZMod p} (ha : a ≠ 0) (hb : b ≠ 0) :
    residueLambda p (a * b) = residueLambda p a * residueLambda p b := by
  letI : Fact p.Prime := ⟨hp⟩
  have hgood : ∀ n : ℕ, 0 < n → n < p → GoodMultiplier p (n : ZMod p) := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro hn hnp
      exact goodMultiplier_natCast_step hp hanti hn hnp
        (fun j hj hjn => ih j hjn hj (lt_trans hjn hnp))
  have hagood := hgood a.val (ZMod.val_pos.mpr ha) (ZMod.val_lt a)
  rw [ZMod.natCast_zmod_val] at hagood
  exact hagood.2 b hb

theorem lambda_eq_one_of_isSquare {p n : ℕ} (hp : Nat.Prime p)
    (hanti : ∀ j : ℕ, 0 < j → j < p → lambda (p - j) = -lambda j)
    (hn : 0 < n) (hnp : n < p) (hsquare : IsSquare (n : ZMod p)) :
    lambda n = (1 : ℤ) := by
  letI : Fact p.Prime := ⟨hp⟩
  have hn0 : (n : ZMod p) ≠ 0 := by
    apply ZMod.val_pos.mp
    rwa [ZMod.val_natCast_of_lt hnp]
  obtain ⟨x, hx⟩ := hsquare
  have hx0 : x ≠ 0 := by
    intro hzero
    rw [hzero, zero_mul] at hx
    exact hn0 hx
  have hmul := residueLambda_mul hp hanti hx0 hx0
  rw [← hx, residueLambda_natCast hnp] at hmul
  rcases residueLambda_sign hx0 with hsign | hsign <;> simpa [hsign] using hmul

end FourWork
end ArithmeticStatement

#print axioms ArithmeticStatement.FourWork.goodMultiplier_natCast_step
#print axioms ArithmeticStatement.FourWork.residueLambda_mul
#print axioms ArithmeticStatement.FourWork.lambda_eq_one_of_isSquare
#print axioms ArithmeticStatement.FourWork.cyclic_short_multiple
#print axioms ArithmeticStatement.lambda_mul
#print axioms Int.natAbs_pos
#print axioms Int.natAbs_eq
#print axioms Nat.strong_induction_on
#print axioms ZMod.natCast_zmod_val
#print axioms mul_left_cancel₀
