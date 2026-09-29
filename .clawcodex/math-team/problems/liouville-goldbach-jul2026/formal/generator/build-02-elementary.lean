import Statement.Definitions
import Mathlib.Algebra.Ring.Parity

set_option autoImplicit false

namespace ArithmeticStatement

def HasSignedRepresentation (s : ℤ) (N : ℕ) : Prop :=
  ∃ a b : ℕ,
    0 < a ∧ 0 < b ∧ N = a + b ∧
      lambda a = s ∧ lambda b = s

def HasRepresentation (N : ℕ) : Prop :=
  HasSignedRepresentation (-1 : ℤ) N

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

end ArithmeticStatement

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
