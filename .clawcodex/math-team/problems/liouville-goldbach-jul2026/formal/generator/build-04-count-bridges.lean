import Statement.Definitions
import Mathlib.Algebra.Ring.Parity
import Mathlib.Algebra.Ring.Int.Defs
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

set_option autoImplicit false

open scoped BigOperators

namespace ArithmeticStatement

def HasSignedRepresentation (s : ℤ) (N : ℕ) : Prop :=
  ∃ a b : ℕ,
    0 < a ∧ 0 < b ∧ N = a + b ∧
      lambda a = s ∧ lambda b = s

def HasRepresentation (N : ℕ) : Prop :=
  HasSignedRepresentation (-1 : ℤ) N

def I (N : ℕ) : Finset ℕ :=
  Finset.Ico 1 N

def representationIndices (N : ℕ) : Finset ℕ :=
  (I N).filter (fun a =>
    lambda a = (-1 : ℤ) ∧ lambda (N - a) = (-1 : ℤ))

def orderedRepresentations (N : ℕ) : Finset (ℕ × ℕ) :=
  ((I N).product (I N)).filter (fun ab =>
    N = ab.1 + ab.2 ∧
      lambda ab.1 = (-1 : ℤ) ∧ lambda ab.2 = (-1 : ℤ))

def R (N : ℕ) : ℕ :=
  (orderedRepresentations N).card

def L (x : ℕ) : ℤ :=
  ∑ a ∈ Finset.Icc 1 x, lambda a

def C (N : ℕ) : ℤ :=
  ∑ a ∈ I N, lambda a * lambda (N - a)

theorem omega_one :
  omega 1 = 0 := by
  simp [omega]

theorem lambda_one :
  lambda 1 = (1 : ℤ) := by
  simp [lambda, omega_one]

theorem lambda_sign {n : ℕ} (hn : 0 < n) :
  lambda n = (1 : ℤ) ∨ lambda n = (-1 : ℤ) := by
  unfold lambda
  rw [neg_one_pow_eq_ite (R := ℤ) (n := omega n)]
  split <;> simp

theorem omega_mul {u v : ℕ} (hu : 0 < u) (hv : 0 < v) :
  omega (u * v) = omega u + omega v := by
  simpa [omega] using
    (Nat.perm_primeFactorsList_mul (Nat.ne_of_gt hu) (Nat.ne_of_gt hv)).length_eq

theorem lambda_mul {u v : ℕ} (hu : 0 < u) (hv : 0 < v) :
  lambda (u * v) = lambda u * lambda v := by
  simp only [lambda, omega_mul hu hv, pow_add]

theorem lambda_prime {p : ℕ} (hp : Nat.Prime p) :
  lambda p = (-1 : ℤ) := by
  simp [lambda, omega, Nat.primeFactorsList_prime hp]

theorem lambda_two :
  lambda 2 = (-1 : ℤ) :=
  lambda_prime Nat.prime_two

theorem lambda_three :
  lambda 3 = (-1 : ℤ) :=
  lambda_prime Nat.prime_three

theorem lambda_four :
  lambda 4 = (1 : ℤ) := by
  calc
    lambda 4 = lambda 2 * lambda 2 := lambda_mul (u := 2) (v := 2) (by decide) (by decide)
    _ = 1 := by rw [lambda_two]; decide

theorem lambda_five :
  lambda 5 = (-1 : ℤ) :=
  lambda_prime Nat.prime_five

theorem lambda_two_mul {m : ℕ} (hm : 0 < m) :
  lambda (2 * m) = -lambda m := by
  rw [lambda_mul (by decide) hm, lambda_two]
  exact neg_one_mul (lambda m)

theorem lambda_square {t : ℕ} (ht : 0 < t) :
  lambda (t ^ 2) = (1 : ℤ) := by
  rw [pow_two, lambda_mul ht ht]
  rcases lambda_sign ht with h | h <;> rw [h] <;> decide

theorem target_iff_forall_hasRepresentation :
  Target ↔ ∀ N : ℕ, Even N → 2 < N → HasRepresentation N :=
  Iff.rfl

theorem hasSignedRepresentation_mul {s : ℤ} {N d : ℕ}
    (hd : 0 < d) (h : HasSignedRepresentation s N) :
  HasSignedRepresentation (lambda d * s) (d * N) := by
  obtain ⟨a, b, ha, hb, hN, hsa, hsb⟩ := h
  refine ⟨d * a, d * b, Nat.mul_pos hd ha, Nat.mul_pos hd hb, ?_, ?_, ?_⟩
  · rw [hN, Nat.mul_add]
  · rw [lambda_mul hd ha, hsa]
  · rw [lambda_mul hd hb, hsb]

theorem representation_scaled_sign {u v m : ℕ} {s : ℤ}
    (hu : 0 < u) (hv : 0 < v) (hm : 0 < m)
    (hs : s = (1 : ℤ) ∨ s = (-1 : ℤ))
    (huSign : lambda u = s) (hvSign : lambda v = s)
    (hmSign : lambda m = -s) :
  HasRepresentation (m * (u + v)) := by
  have h : HasSignedRepresentation s (u + v) :=
    ⟨u, v, hu, hv, rfl, huSign, hvSign⟩
  have scaled := hasSignedRepresentation_mul hm h
  rcases hs with hs | hs
  · simpa [HasRepresentation, hmSign, hs] using scaled
  · simpa [HasRepresentation, hmSign, hs] using scaled

theorem representation_double {m : ℕ}
    (hm : 0 < m) (hSign : lambda m = (-1 : ℤ)) :
  HasRepresentation (2 * m) := by
  exact ⟨m, m, hm, hm, two_mul m, hSign, hSign⟩

theorem representation_diagonal {N : ℕ}
    (hEven : Even N) (hN : 2 < N) (hSign : lambda N = (1 : ℤ)) :
  HasRepresentation N := by
  obtain ⟨m, rfl⟩ := hEven
  have hm : 0 < m := by omega
  have hsign : lambda m = (-1 : ℤ) := by
    rw [← two_mul, lambda_two_mul hm] at hSign
    omega
  simpa only [two_mul] using representation_double hm hsign

theorem representation_two_sign_seed {d : ℕ}
    (hminus : HasSignedRepresentation (-1 : ℤ) d)
    (hplus : HasSignedRepresentation (1 : ℤ) d)
    (m : ℕ) (hm : 0 < m) :
  HasRepresentation (d * m) := by
  rcases lambda_sign hm with h | h
  · simpa [HasRepresentation, h, Nat.mul_comm] using
      hasSignedRepresentation_mul hm hminus
  · simpa [HasRepresentation, h, Nat.mul_comm] using
      hasSignedRepresentation_mul hm hplus

theorem eight_two_sign_seed :
  HasSignedRepresentation (-1 : ℤ) 8 ∧
    HasSignedRepresentation (1 : ℤ) 8 := by
  constructor
  · exact ⟨3, 5, by decide, by decide, rfl, lambda_three, lambda_five⟩
  · exact ⟨4, 4, by decide, by decide, rfl, lambda_four, lambda_four⟩

theorem representation_multiple_eight (m : ℕ) (hm : 0 < m) :
  HasRepresentation (8 * m) :=
  representation_two_sign_seed eight_two_sign_seed.1 eight_two_sign_seed.2 m hm

theorem mem_I_iff {N a : ℕ} :
  a ∈ I N ↔ 0 < a ∧ a < N := by
  simp [I, Nat.succ_le_iff]

theorem interval_eq_Icc {N : ℕ} (hN : 2 ≤ N) :
  I N = Finset.Icc 1 (N - 1) := by
  ext a
  simp only [mem_I_iff, Finset.mem_Icc]
  omega

theorem interval_bounds {N a : ℕ} (hN : 2 ≤ N) (ha : a ∈ I N) :
  0 < a ∧ a < N ∧ 0 < N - a ∧ N - a < N := by
  obtain ⟨hapos, halt⟩ := mem_I_iff.mp ha
  omega

theorem interval_card_cast {N : ℕ} (hN : 2 ≤ N) :
  ((I N).card : ℤ) = (N : ℤ) - 1 := by
  simp only [I, Nat.card_Ico]
  rw [Nat.cast_sub (by omega : 1 ≤ N)]
  rfl

theorem reflection_mem {N a : ℕ} (hN : 2 ≤ N) (ha : a ∈ I N) :
  N - a ∈ I N :=
  mem_I_iff.mpr (interval_bounds hN ha).2.2

theorem reflection_involutive {N a : ℕ}
    (hN : 2 ≤ N) (ha : a ∈ I N) :
  N - (N - a) = a :=
  Nat.sub_sub_self (Nat.le_of_lt (mem_I_iff.mp ha).2)

theorem reflection_bijection {N : ℕ} (hN : 2 ≤ N) :
  Set.BijOn (fun a : ℕ => N - a) (I N : Set ℕ) (I N : Set ℕ) := by
  refine ⟨fun a ha => reflection_mem hN ha, ?_, ?_⟩
  · intro a ha b hb hab
    have h := congrArg (fun x : ℕ => N - x) hab
    simpa only [reflection_involutive hN ha, reflection_involutive hN hb] using h
  · intro b hb
    exact ⟨N - b, reflection_mem hN hb, reflection_involutive hN hb⟩

theorem sum_lambda_interval {N : ℕ} (hN : 2 ≤ N) :
  (∑ a ∈ I N, lambda a) = L (N - 1) := by
  rw [interval_eq_Icc hN]
  rfl

theorem sum_lambda_reflection {N : ℕ} (hN : 2 ≤ N) :
  (∑ a ∈ I N, lambda (N - a)) = L (N - 1) := by
  calc
    (∑ a ∈ I N, lambda (N - a)) = ∑ a ∈ I N, lambda a :=
      Finset.sum_nbij' (fun a : ℕ => N - a) (fun a : ℕ => N - a)
        (fun a ha => reflection_mem hN ha) (fun a ha => reflection_mem hN ha)
        (fun a ha => reflection_involutive hN ha)
        (fun a ha => reflection_involutive hN ha) (fun a ha => rfl)
    _ = L (N - 1) := sum_lambda_interval hN

theorem mem_orderedRepresentations {N a b : ℕ} :
  (a, b) ∈ orderedRepresentations N ↔
    0 < a ∧ 0 < b ∧ N = a + b ∧
      lambda a = (-1 : ℤ) ∧ lambda b = (-1 : ℤ) := by
  simp only [orderedRepresentations, Finset.mem_filter, Finset.mem_product,
    mem_I_iff]
  constructor
  · rintro ⟨⟨⟨ha, _⟩, ⟨hb, _⟩⟩, hN, hsa, hsb⟩
    exact ⟨ha, hb, hN, hsa, hsb⟩
  · rintro ⟨ha, hb, hN, hsa, hsb⟩
    exact ⟨⟨⟨ha, by omega⟩, ⟨hb, by omega⟩⟩, hN, hsa, hsb⟩

theorem orderedRepresentations_eq_image {N : ℕ} (hN : 2 ≤ N) :
  orderedRepresentations N =
    (representationIndices N).image (fun a : ℕ => (a, N - a)) := by
  ext ⟨a, b⟩
  rw [mem_orderedRepresentations, Finset.mem_image]
  constructor
  · rintro ⟨ha, hb, hab, hsa, hsb⟩
    have hba : N - a = b := by omega
    refine ⟨a, ?_, by simp only [hba]⟩
    exact Finset.mem_filter.mpr
      ⟨mem_I_iff.mpr ⟨ha, by omega⟩, hsa, by simpa only [hba] using hsb⟩
  · rintro ⟨x, hx, hpair⟩
    obtain ⟨hxI, hxa, hxb⟩ := Finset.mem_filter.mp hx
    have hxa' : x = a := congrArg Prod.fst hpair
    have hxb' : N - x = b := congrArg Prod.snd hpair
    subst a
    subst b
    have hbds := interval_bounds hN hxI
    exact ⟨hbds.1, hbds.2.2.1, by omega, hxa, hxb⟩

theorem representation_count_eq_card_indices {N : ℕ} (hN : 2 ≤ N) :
  R N = (representationIndices N).card := by
  rw [R, orderedRepresentations_eq_image hN]
  exact Finset.card_image_of_injective _ (fun a b h => congrArg Prod.fst h)

theorem representation_count_pos_iff {N : ℕ} (hN : 2 ≤ N) :
  0 < R N ↔ HasRepresentation N := by
  rw [R, Finset.card_pos]
  constructor
  · rintro ⟨⟨a, b⟩, hab⟩
    exact ⟨a, b, mem_orderedRepresentations.mp hab⟩
  · rintro ⟨a, b, hab⟩
    exact ⟨(a, b), mem_orderedRepresentations.mpr hab⟩

end ArithmeticStatement

#print axioms ArithmeticStatement.mem_I_iff
#print axioms ArithmeticStatement.interval_eq_Icc
#print axioms ArithmeticStatement.interval_bounds
#print axioms ArithmeticStatement.interval_card_cast
#print axioms ArithmeticStatement.reflection_mem
#print axioms ArithmeticStatement.reflection_involutive
#print axioms ArithmeticStatement.reflection_bijection
#print axioms ArithmeticStatement.sum_lambda_interval
#print axioms ArithmeticStatement.sum_lambda_reflection
#print axioms ArithmeticStatement.mem_orderedRepresentations
#print axioms ArithmeticStatement.orderedRepresentations_eq_image
#print axioms ArithmeticStatement.representation_count_eq_card_indices
#print axioms ArithmeticStatement.representation_count_pos_iff
#print axioms ArithmeticStatement.omega_one
#print axioms ArithmeticStatement.lambda_one
#print axioms ArithmeticStatement.lambda_sign
#print axioms ArithmeticStatement.omega_mul
#print axioms ArithmeticStatement.lambda_mul
#print axioms ArithmeticStatement.lambda_prime
#print axioms ArithmeticStatement.lambda_two
#print axioms ArithmeticStatement.lambda_three
#print axioms ArithmeticStatement.lambda_four
#print axioms ArithmeticStatement.lambda_five
#print axioms ArithmeticStatement.lambda_two_mul
#print axioms ArithmeticStatement.lambda_square
#print axioms ArithmeticStatement.target_iff_forall_hasRepresentation
#print axioms ArithmeticStatement.hasSignedRepresentation_mul
#print axioms ArithmeticStatement.representation_scaled_sign
#print axioms ArithmeticStatement.representation_double
#print axioms ArithmeticStatement.representation_diagonal
#print axioms ArithmeticStatement.representation_two_sign_seed
#print axioms ArithmeticStatement.eight_two_sign_seed
#print axioms ArithmeticStatement.representation_multiple_eight
