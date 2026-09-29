import Statement.Partial

set_option autoImplicit false

namespace ArithmeticStatement

-- Incomplete exact-target attempt. The residual branch intentionally fails to close.
-- This file is not an accepted theorem module and must not be integrated.
theorem representation_multiple_four (m : ℕ) (hm : 0 < m) :
  HasRepresentation (4 * m) := by
  by_cases hEven : Even m
  · obtain ⟨k, hk⟩ := hEven
    have hkpos : 0 < k := by omega
    have hfactor : 4 * m = 8 * k := by rw [hk]; ring
    rw [hfactor]
    exact representation_multiple_eight k hkpos
  · rcases lambda_sign hm with hplus | hminus
    · apply representation_diagonal
      · exact ⟨2 * m, by ring⟩
      · omega
      · rw [lambda_mul (by decide) hm, lambda_four, hplus]
        rfl
    · have hmne : m ≠ 1 := by
        intro heq
        rw [heq, lambda_one] at hminus
        contradiction
      have hmgt : 1 < m := by omega
      done

end ArithmeticStatement
