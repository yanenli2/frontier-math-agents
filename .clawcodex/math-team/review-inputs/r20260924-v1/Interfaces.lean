import Statement.Definitions
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Algebra.BigOperators.Ring.Finset

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
  omega 1 = 0

theorem lambda_one :
  lambda 1 = (1 : ℤ)

theorem lambda_sign {n : ℕ} (hn : 0 < n) :
  lambda n = (1 : ℤ) ∨ lambda n = (-1 : ℤ)

theorem omega_mul {u v : ℕ} (hu : 0 < u) (hv : 0 < v) :
  omega (u * v) = omega u + omega v

theorem lambda_mul {u v : ℕ} (hu : 0 < u) (hv : 0 < v) :
  lambda (u * v) = lambda u * lambda v

theorem lambda_prime {p : ℕ} (hp : Nat.Prime p) :
  lambda p = (-1 : ℤ)

theorem lambda_two :
  lambda 2 = (-1 : ℤ)

theorem lambda_three :
  lambda 3 = (-1 : ℤ)

theorem lambda_four :
  lambda 4 = (1 : ℤ)

theorem lambda_five :
  lambda 5 = (-1 : ℤ)

theorem lambda_two_mul {m : ℕ} (hm : 0 < m) :
  lambda (2 * m) = -lambda m

theorem lambda_square {t : ℕ} (ht : 0 < t) :
  lambda (t ^ 2) = (1 : ℤ)

theorem target_iff_forall_hasRepresentation :
  Target ↔ ∀ N : ℕ, Even N → 2 < N → HasRepresentation N

theorem hasSignedRepresentation_mul {s : ℤ} {N d : ℕ}
    (hd : 0 < d) (h : HasSignedRepresentation s N) :
  HasSignedRepresentation (lambda d * s) (d * N)

theorem representation_scaled_sign {u v m : ℕ} {s : ℤ}
    (hu : 0 < u) (hv : 0 < v) (hm : 0 < m)
    (hs : s = (1 : ℤ) ∨ s = (-1 : ℤ))
    (huSign : lambda u = s) (hvSign : lambda v = s)
    (hmSign : lambda m = -s) :
  HasRepresentation (m * (u + v))

theorem representation_double {m : ℕ}
    (hm : 0 < m) (hSign : lambda m = (-1 : ℤ)) :
  HasRepresentation (2 * m)

theorem representation_diagonal {N : ℕ}
    (hEven : Even N) (hN : 2 < N) (hSign : lambda N = (1 : ℤ)) :
  HasRepresentation N

theorem representation_two_sign_seed {d : ℕ}
    (hminus : HasSignedRepresentation (-1 : ℤ) d)
    (hplus : HasSignedRepresentation (1 : ℤ) d)
    (m : ℕ) (hm : 0 < m) :
  HasRepresentation (d * m)

theorem eight_two_sign_seed :
  HasSignedRepresentation (-1 : ℤ) 8 ∧
    HasSignedRepresentation (1 : ℤ) 8

theorem representation_multiple_eight (m : ℕ) (hm : 0 < m) :
  HasRepresentation (8 * m)

theorem mem_I_iff {N a : ℕ} :
  a ∈ I N ↔ 0 < a ∧ a < N

theorem interval_eq_Icc {N : ℕ} (hN : 2 ≤ N) :
  I N = Finset.Icc 1 (N - 1)

theorem interval_bounds {N a : ℕ} (hN : 2 ≤ N) (ha : a ∈ I N) :
  0 < a ∧ a < N ∧ 0 < N - a ∧ N - a < N

theorem interval_card_cast {N : ℕ} (hN : 2 ≤ N) :
  ((I N).card : ℤ) = (N : ℤ) - 1

theorem reflection_mem {N a : ℕ} (hN : 2 ≤ N) (ha : a ∈ I N) :
  N - a ∈ I N

theorem reflection_involutive {N a : ℕ}
    (hN : 2 ≤ N) (ha : a ∈ I N) :
  N - (N - a) = a

theorem reflection_bijection {N : ℕ} (hN : 2 ≤ N) :
  Set.BijOn (fun a : ℕ => N - a) (I N : Set ℕ) (I N : Set ℕ)

theorem sum_lambda_interval {N : ℕ} (hN : 2 ≤ N) :
  (∑ a ∈ I N, lambda a) = L (N - 1)

theorem sum_lambda_reflection {N : ℕ} (hN : 2 ≤ N) :
  (∑ a ∈ I N, lambda (N - a)) = L (N - 1)

theorem mem_orderedRepresentations {N a b : ℕ} :
  (a, b) ∈ orderedRepresentations N ↔
    0 < a ∧ 0 < b ∧ N = a + b ∧
      lambda a = (-1 : ℤ) ∧ lambda b = (-1 : ℤ)

theorem orderedRepresentations_eq_image {N : ℕ} (hN : 2 ≤ N) :
  orderedRepresentations N =
    (representationIndices N).image (fun a : ℕ => (a, N - a))

theorem representation_count_eq_card_indices {N : ℕ} (hN : 2 ≤ N) :
  R N = (representationIndices N).card

theorem two_sign_indicator {a b : ℕ} (ha : 0 < a) (hb : 0 < b) :
  (4 : ℤ) *
      (if lambda a = (-1 : ℤ) ∧ lambda b = (-1 : ℤ) then (1 : ℤ) else 0) =
    (1 - lambda a) * (1 - lambda b)

theorem representation_count_eq_indicator_sum {N : ℕ} (hN : 2 ≤ N) :
  (R N : ℤ) =
    ∑ a ∈ I N,
      if lambda a = (-1 : ℤ) ∧ lambda (N - a) = (-1 : ℤ)
      then (1 : ℤ) else 0

theorem four_mul_representation_count {N : ℕ} (hN : 2 ≤ N) :
  4 * (R N : ℤ) = ((N : ℤ) - 1) - 2 * L (N - 1) + C N

theorem representation_count_pos_iff {N : ℕ} (hN : 2 ≤ N) :
  0 < R N ↔ HasRepresentation N

theorem count_pos_iff_keystone {N : ℕ} (hN : 2 ≤ N) :
  0 < R N ↔ 2 * L (N - 1) - ((N : ℤ) - 1) < C N

theorem keystone_ge_four_iff {N : ℕ} (hN : 2 ≤ N) :
  0 < R N ↔ 4 ≤ ((N : ℤ) - 1) - 2 * L (N - 1) + C N

theorem target_iff_count_pos :
  Target ↔ ∀ N : ℕ, Even N → 2 < N → 0 < R N

theorem target_iff_pointwise_keystone :
  Target ↔ ∀ N : ℕ, Even N → 2 < N →
    2 * L (N - 1) - ((N : ℤ) - 1) < C N

theorem exists_prime_pair_factor_of_lambda_one {m : ℕ}
    (hm : 1 < m) (hSign : lambda m = (1 : ℤ)) :
  ∃ p q d : ℕ,
    Nat.Prime p ∧ Nat.Prime q ∧ 0 < d ∧
      lambda d = (1 : ℤ) ∧ m = d * (p * q)

theorem target_iff_prime_product_core :
  Target ↔ ∀ p q : ℕ,
    Nat.Prime p → Nat.Prime q → HasRepresentation (2 * p * q)

theorem pointwise_keystone (N : ℕ) (hEven : Even N) (hN : 2 < N) :
  2 * L (N - 1) - ((N : ℤ) - 1) < C N

theorem liouville_goldbach :
  Target

end ArithmeticStatement
