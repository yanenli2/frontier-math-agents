import Mathlib.NumberTheory.LegendreSymbol.QuadraticReciprocity
import Mathlib.Tactic.Ring

set_option autoImplicit false

namespace ArithmeticStatement
namespace FourWork

theorem prime_dvd_quarter_isSquare {p r : ℕ}
    (hp : Nat.Prime p) (hLower : 7 ≤ p) (hMod : p % 4 = 3)
    (hr : Nat.Prime r) (hdiv : r ∣ (p + 1) / 4) :
    IsSquare (r : ZMod p) := by
  letI : Fact p.Prime := ⟨hp⟩
  letI : Fact r.Prime := ⟨hr⟩
  have hquarter : 4 * ((p + 1) / 4) = p + 1 := by omega
  have htpos : 0 < (p + 1) / 4 := by omega
  have htlt : (p + 1) / 4 < p := by omega
  have hrle : r ≤ (p + 1) / 4 := Nat.le_of_dvd htpos hdiv
  have hrlt : r < p := lt_of_le_of_lt hrle htlt
  have hp2 : p ≠ 2 := by omega
  obtain ⟨s, hs⟩ := hdiv
  have hpident : p + 1 = 4 * (r * s) := by rw [← hs]; exact hquarter.symm
  rcases hr.eq_two_or_odd with hr2 | hrodd
  · subst r
    apply (ZMod.exists_sq_eq_two_iff hp2).mpr
    right
    omega
  · have hdivp : r ∣ p + 1 := by
      refine ⟨4 * s, ?_⟩
      rw [hpident]
      ring
    have hcast : (p : ZMod r) + 1 = 0 := by
      simpa only [Nat.cast_add, Nat.cast_one] using
        (ZMod.natCast_eq_zero_iff (p + 1) r).mpr hdivp
    have hneg : (p : ZMod r) = -1 := by
      calc
        (p : ZMod r) = ((p : ZMod r) + 1) - 1 := by ring
        _ = -1 := by rw [hcast]; simp
    rcases Nat.odd_mod_four_iff.mp hrodd with hr1 | hr3
    · apply (ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_one
        (p := r) (q := p) hr1 hp2).mp
      rw [hneg]
      exact ZMod.exists_sq_eq_neg_one_iff.mpr (by omega)
    · apply (ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_three
        (p := p) (q := r) hMod hr3 (by omega)).mpr
      rw [hneg]
      intro hsquare
      exact (ZMod.exists_sq_eq_neg_one_iff.mp hsquare) hr3

theorem exists_small_prime_isSquare {p : ℕ}
    (hp : Nat.Prime p) (hLower : 7 ≤ p) (hMod : p % 4 = 3) :
    ∃ r : ℕ, Nat.Prime r ∧ r ∣ (p + 1) / 4 ∧
      r ≤ (p + 1) / 4 ∧ r < p ∧ IsSquare (r : ZMod p) := by
  have htwo : 2 ≤ (p + 1) / 4 := by omega
  have htlt : (p + 1) / 4 < p := by omega
  obtain ⟨r, hr, hdiv⟩ := Nat.exists_prime_and_dvd (show (p + 1) / 4 ≠ 1 by omega)
  have hrle : r ≤ (p + 1) / 4 := Nat.le_of_dvd (by omega) hdiv
  exact ⟨r, hr, hdiv, hrle, lt_of_le_of_lt hrle htlt,
    prime_dvd_quarter_isSquare hp hLower hMod hr hdiv⟩

end FourWork
end ArithmeticStatement

#print axioms ArithmeticStatement.FourWork.prime_dvd_quarter_isSquare
#print axioms ArithmeticStatement.FourWork.exists_small_prime_isSquare
#print axioms ZMod.exists_sq_eq_neg_one_iff
#print axioms ZMod.exists_sq_eq_two_iff
#print axioms ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_one
#print axioms ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_three
#print axioms ZMod.natCast_eq_zero_iff
#print axioms Nat.exists_prime_and_dvd
#print axioms Nat.le_of_dvd
#print axioms Nat.Prime.eq_two_or_odd
#print axioms Nat.odd_mod_four_iff
