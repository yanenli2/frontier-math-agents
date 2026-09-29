import Statement.Partial

set_option autoImplicit false

namespace ArithmeticStatement
namespace FourWork

theorem lambda_reflection_eq_one_of_neg {p n : ℕ}
    (hno : ¬ HasRepresentation (4 * p))
    (hn : 0 < n) (hnp : n < p) (hs : lambda n = (-1 : ℤ)) :
    lambda (p - n) = (1 : ℤ) := by
  have hc : 0 < p - n := by omega
  rcases lambda_sign hc with hplus | hminus
  · exact hplus
  · exfalso
    apply hno
    refine ⟨4 * n, 4 * (p - n), Nat.mul_pos (by decide) hn,
      Nat.mul_pos (by decide) hc, by omega, ?_, ?_⟩
    · rw [lambda_mul (by decide) hn, lambda_four, hs, one_mul]
    · rw [lambda_mul (by decide) hc, lambda_four, hminus, one_mul]

theorem lambda_double_reflection_eq_neg_one_of_pos {p n : ℕ}
    (hno : ¬ HasRepresentation (4 * p))
    (hn : 0 < n) (hnp : n < 2 * p) (hs : lambda n = (1 : ℤ)) :
    lambda (2 * p - n) = (-1 : ℤ) := by
  have hc : 0 < 2 * p - n := by omega
  rcases lambda_sign hc with hplus | hminus
  · exfalso
    apply hno
    refine ⟨2 * n, 2 * (2 * p - n), Nat.mul_pos (by decide) hn,
      Nat.mul_pos (by decide) hc, by omega, ?_, ?_⟩
    · rw [lambda_two_mul hn, hs]
    · rw [lambda_two_mul hc, hplus]
  · exact hminus

theorem three_not_dvd_of_positive_pair {p x y : ℕ}
    (hno : ¬ HasRepresentation (4 * p))
    (hx : 0 < x) (hy : 0 < y) (hsum : x + y = p)
    (hxsign : lambda x = (1 : ℤ)) (hysign : lambda y = (1 : ℤ)) :
    ¬ 3 ∣ x := by
  rintro ⟨u, hxu⟩
  have hu : 0 < u := by omega
  have hup : u < p := by omega
  have husign : lambda u = (-1 : ℤ) := by
    rw [hxu, lambda_mul (by decide) hu, lambda_three] at hxsign
    omega
  have hcomp := lambda_reflection_eq_one_of_neg hno hu hup husign
  have hcomppos : 0 < p - u := by omega
  have hsecond := lambda_double_reflection_eq_neg_one_of_pos hno hy (by omega) hysign
  have hsecondpos : 0 < 2 * p - y := by omega
  apply hno
  refine ⟨3 * (p - u), 2 * p - y, Nat.mul_pos (by decide) hcomppos,
    hsecondpos, by omega, ?_, hsecond⟩
  rw [lambda_mul (by decide) hcomppos, lambda_three, hcomp, mul_one]

theorem positive_pair_gap_step {p x y : ℕ}
    (hp : Nat.Prime p) (hp3 : p ≠ 3)
    (hno : ¬ HasRepresentation (4 * p))
    (hx : 0 < x) (hxy : x < y) (hsum : x + y = p)
    (hxsign : lambda x = (1 : ℤ)) (hysign : lambda y = (1 : ℤ)) :
    ∃ u v : ℕ, 0 < u ∧ u < v ∧ u + v = p ∧
      lambda u = (1 : ℤ) ∧ lambda v = (1 : ℤ) ∧ v - u < y - x := by
  have hy : 0 < y := by omega
  have hxThree := three_not_dvd_of_positive_pair hno hx hy hsum hxsign hysign
  have hyThree := three_not_dvd_of_positive_pair hno hy hx (by omega) hysign hxsign
  have hpThree : ¬ 3 ∣ p := by
    intro hdiv
    rcases hp.eq_one_or_self_of_dvd 3 hdiv with heq | heq <;> omega
  have hxmod : x % 3 ≠ 0 := fun h => hxThree (Nat.dvd_of_mod_eq_zero h)
  have hymod : y % 3 ≠ 0 := fun h => hyThree (Nat.dvd_of_mod_eq_zero h)
  have hpmod : p % 3 ≠ 0 := fun h => hpThree (Nat.dvd_of_mod_eq_zero h)
  have hxres : x % 3 = 1 ∨ x % 3 = 2 := by omega
  have hyres : y % 3 = 1 ∨ y % 3 = 2 := by omega
  have hpModSum : p % 3 = (x % 3 + y % 3) % 3 := by rw [← hsum, Nat.add_mod]
  have hremainders : (p + x) % 3 = 0 ∧ (p + y) % 3 = 0 := by
    rw [Nat.add_mod p x 3, Nat.add_mod p y 3]
    rcases hxres with hxres | hxres <;> rcases hyres with hyres | hyres <;>
      simp_all
  have hdivx : 3 ∣ p + x := Nat.dvd_of_mod_eq_zero hremainders.1
  have hdivy : 3 ∣ p + y := Nat.dvd_of_mod_eq_zero hremainders.2
  let u := (p + x) / 3
  let v := (p + y) / 3
  have hueq : 3 * u = p + x := Nat.mul_div_cancel' hdivx
  have hveq : 3 * v = p + y := Nat.mul_div_cancel' hdivy
  have hu : 0 < u := by omega
  have hv : 0 < v := by omega
  have hpx : lambda (p + x) = (-1 : ℤ) := by
    have h := lambda_double_reflection_eq_neg_one_of_pos hno hy (by omega) hysign
    have heq : 2 * p - y = p + x := by omega
    simpa only [heq] using h
  have hpy : lambda (p + y) = (-1 : ℤ) := by
    have h := lambda_double_reflection_eq_neg_one_of_pos hno hx (by omega) hxsign
    have heq : 2 * p - x = p + y := by omega
    simpa only [heq] using h
  have husign : lambda u = (1 : ℤ) := by
    rw [← hueq, lambda_mul (by decide) hu, lambda_three] at hpx
    omega
  have hvsign : lambda v = (1 : ℤ) := by
    rw [← hveq, lambda_mul (by decide) hv, lambda_three] at hpy
    omega
  exact ⟨u, v, hu, by omega, by omega, husign, hvsign, by omega⟩

theorem no_positive_pair {p : ℕ}
    (hp : Nat.Prime p) (hp2 : p ≠ 2) (hp3 : p ≠ 3)
    (hno : ¬ HasRepresentation (4 * p))
    {x y : ℕ} (hx : 0 < x) (hy : 0 < y) (hsum : x + y = p) :
    ¬ (lambda x = (1 : ℤ) ∧ lambda y = (1 : ℤ)) := by
  have hordered : ∀ d : ℕ, ∀ a b : ℕ, b - a = d → 0 < a → a < b → a + b = p →
      lambda a = (1 : ℤ) → lambda b = (1 : ℤ) → False := by
    intro d
    induction d using Nat.strong_induction_on with
    | h d ih =>
        intro a b hgap ha hab habsum hasign hbsign
        obtain ⟨u, v, hu, huv, huvsum, husign, hvsign, hless⟩ :=
          positive_pair_gap_step hp hp3 hno ha hab habsum hasign hbsign
        exact ih (v - u) (by omega) u v rfl hu huv huvsum husign hvsign
  rintro ⟨hxsign, hysign⟩
  rcases lt_trichotomy x y with hxy | heq | hyx
  · exact hordered (y - x) x y rfl hx hxy hsum hxsign hysign
  · have hodd : p % 2 = 1 := hp.eq_two_or_odd.resolve_left hp2
    omega
  · exact hordered (x - y) y x rfl hy hyx (by omega) hysign hxsign

theorem lambda_antireflection_of_no_representation {p : ℕ}
    (hp : Nat.Prime p) (hp2 : p ≠ 2) (hp3 : p ≠ 3)
    (hno : ¬ HasRepresentation (4 * p)) :
    ∀ n : ℕ, 0 < n → n < p → lambda (p - n) = -lambda n := by
  intro n hn hnp
  have hc : 0 < p - n := by omega
  rcases lambda_sign hn with hplus | hminus
  · have hneg : lambda (p - n) = (-1 : ℤ) := by
      rcases lambda_sign hc with hcplus | hcminus
      · exact False.elim ((no_positive_pair hp hp2 hp3 hno hn hc (by omega)) ⟨hplus, hcplus⟩)
      · exact hcminus
    rw [hneg, hplus]
  · rw [lambda_reflection_eq_one_of_neg hno hn hnp hminus, hminus]
    rfl

end FourWork
end ArithmeticStatement

#print axioms ArithmeticStatement.FourWork.lambda_reflection_eq_one_of_neg
#print axioms ArithmeticStatement.FourWork.lambda_double_reflection_eq_neg_one_of_pos
#print axioms ArithmeticStatement.FourWork.three_not_dvd_of_positive_pair
#print axioms ArithmeticStatement.FourWork.positive_pair_gap_step
#print axioms ArithmeticStatement.FourWork.no_positive_pair
#print axioms ArithmeticStatement.FourWork.lambda_antireflection_of_no_representation
#print axioms ArithmeticStatement.lambda_sign
#print axioms ArithmeticStatement.lambda_mul
#print axioms ArithmeticStatement.lambda_three
#print axioms ArithmeticStatement.lambda_four
#print axioms ArithmeticStatement.lambda_two_mul
#print axioms Nat.strong_induction_on
