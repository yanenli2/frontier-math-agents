import Statement.Partial
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Linarith

set_option autoImplicit false

namespace ArithmeticStatement
namespace FourWork

theorem cyclic_short_multiple {p n : ℕ}
    (hp : Nat.Prime p) (hn : 2 ≤ n) (hnp : n < p)
    (z : ZMod p) (hz : z ≠ 0) :
    ∃ k : ℤ, ∃ d : ℕ, k ≠ 0 ∧ k.natAbs < n ∧
      0 < d ∧ n * d < p ∧ (k : ZMod p) * z = (d : ZMod p) := by
  letI : Fact p.Prime := ⟨hp⟩
  let r : ℕ → ℕ := fun i => ((i : ZMod p) * z).val
  let b : ℕ → ℕ := fun i => n * r i / p
  have hrlt : ∀ i : ℕ, r i < p := fun i => ZMod.val_lt _
  have hrcast : ∀ i : ℕ, (r i : ZMod p) = (i : ZMod p) * z :=
    fun i => ZMod.natCast_zmod_val _
  have hblt : ∀ i : ℕ, b i < n := by
    intro i
    apply (Nat.div_lt_iff_lt_mul hp.pos).mpr
    exact Nat.mul_lt_mul_of_pos_left (hrlt i) (by omega)
  have hrinj : ∀ i : ℕ, i < n → ∀ j : ℕ, j < n → r i = r j → i = j := by
    intro i hi j hj hrij
    have hcast : (i : ZMod p) * z = (j : ZMod p) * z := by
      simpa only [hrcast] using congrArg (fun a : ℕ => (a : ZMod p)) hrij
    have hij : (i : ZMod p) = (j : ZMod p) := mul_right_cancel₀ hz hcast
    have hval := congrArg ZMod.val hij
    simpa only [ZMod.val_natCast_of_lt (lt_trans hi hnp),
      ZMod.val_natCast_of_lt (lt_trans hj hnp)] using hval
  by_cases hwrap : ∃ i : ℕ, i < n ∧ b i = n - 1
  · obtain ⟨i, hi, hbin⟩ := hwrap
    have hi0 : i ≠ 0 := by
      intro heq
      subst i
      have hbzero : b 0 = 0 := by simp [b, r]
      rw [hbzero] at hbin
      omega
    have hdpos : 0 < p - r i := Nat.sub_pos_of_lt (hrlt i)
    have hlower : (n - 1) * p ≤ n * r i := by
      have h := Nat.div_mul_le_self (n * r i) p
      change b i * p ≤ n * r i at h
      simpa only [hbin] using h
    have hprod : (n - 1) * p + p = n * p := by
      calc
        _ = (n - 1 + 1) * p := by ring
        _ = n * p := by rw [Nat.sub_add_cancel (by omega : 1 ≤ n)]
    have hgap : n * (p - r i) + n * r i = n * p := by
      rw [← Nat.mul_add, Nat.sub_add_cancel (Nat.le_of_lt (hrlt i))]
    have hle : n * (p - r i) ≤ p := by omega
    have hnotdvd : ¬ n ∣ p := by
      intro hdiv
      rcases hp.eq_one_or_self_of_dvd n hdiv with heq | heq <;> omega
    have hne : n * (p - r i) ≠ p := by
      intro heq
      exact hnotdvd ⟨p - r i, heq.symm⟩
    refine ⟨-(i : ℤ), p - r i, by omega, ?_, hdpos, by omega, ?_⟩
    · simpa only [Int.natAbs_neg, Int.natAbs_natCast] using hi
    · rw [Int.cast_neg, Int.cast_natCast, Nat.cast_sub (Nat.le_of_lt (hrlt i)),
        ZMod.natCast_self, zero_sub, hrcast]
      ring
  · have hmaps : Set.MapsTo b (Finset.range n) (Finset.range (n - 1)) := by
      intro i hi
      have hin : i < n := Finset.mem_range.mp hi
      have hbine : b i ≠ n - 1 := fun h => hwrap ⟨i, hin, h⟩
      exact Finset.mem_range.mpr (by have h := hblt i; omega)
    have hcard : (Finset.range (n - 1)).card < (Finset.range n).card := by
      simp only [Finset.card_range]
      omega
    obtain ⟨i, hi, j, hj, hij, hbin⟩ :=
      Finset.exists_ne_map_eq_of_card_lt_of_maps_to hcard hmaps
    have hin : i < n := Finset.mem_range.mp hi
    have hjn : j < n := Finset.mem_range.mp hj
    have hrij : r i ≠ r j := fun h => hij (hrinj i hin j hjn h)
    have hshort : ∀ i j : ℕ, i < n → j < n → i ≠ j → b i = b j → r i < r j →
        ∃ k : ℤ, ∃ d : ℕ, k ≠ 0 ∧ k.natAbs < n ∧
          0 < d ∧ n * d < p ∧ (k : ZMod p) * z = (d : ZMod p) := by
      intro i j hi hj hij hbin hrij
      have hlower : b i * p ≤ n * r i := Nat.div_mul_le_self (n * r i) p
      have hupper : n * r j < p * (b i + 1) := by
        have h := Nat.lt_mul_div_succ (n * r j) hp.pos
        change n * r j < p * (b j + 1) at h
        simpa only [← hbin] using h
      have hgap : n * (r j - r i) + n * r i = n * r j := by
        rw [← Nat.mul_add, Nat.sub_add_cancel (Nat.le_of_lt hrij)]
      have hsmall : n * (r j - r i) < p := by nlinarith
      have hkabs : ((j : ℤ) - (i : ℤ)).natAbs < n := by
        apply Int.ofNat_lt.mp
        rw [Int.natCast_natAbs]
        exact abs_lt.mpr ⟨by omega, by omega⟩
      refine ⟨(j : ℤ) - (i : ℤ), r j - r i, by omega, hkabs,
        Nat.sub_pos_of_lt hrij, hsmall, ?_⟩
      rw [Int.cast_sub, Int.cast_natCast, Int.cast_natCast,
        Nat.cast_sub (Nat.le_of_lt hrij), hrcast, hrcast]
      ring
    rcases lt_or_gt_of_ne hrij with hlt | hgt
    · exact hshort i j hin hjn hij hbin hlt
    · exact hshort j i hjn hin hij.symm hbin.symm hgt

end FourWork
end ArithmeticStatement

#print axioms ArithmeticStatement.FourWork.cyclic_short_multiple
#print axioms Finset.exists_ne_map_eq_of_card_lt_of_maps_to
#print axioms ZMod.val_lt
#print axioms ZMod.natCast_zmod_val
#print axioms ZMod.val_natCast_of_lt
#print axioms Nat.Prime.eq_one_or_self_of_dvd
