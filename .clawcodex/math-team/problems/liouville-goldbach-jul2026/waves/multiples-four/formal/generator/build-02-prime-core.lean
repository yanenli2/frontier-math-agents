import Statement.Partial

set_option autoImplicit false

namespace ArithmeticStatement

-- Incomplete exact-target attempt. The prime-core obligation is not assumed.
-- The final `done` fails; this file must not be integrated as a proved module.
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
    · have hprod := Nat.prod_primeFactorsList (Nat.ne_of_gt hm)
      cases hlist : m.primeFactorsList with
      | nil =>
          have hsign : lambda m = (1 : ℤ) := by simp [lambda, omega, hlist]
          omega
      | cons p t =>
          have hp : Nat.Prime p :=
            Nat.prime_of_mem_primeFactorsList (n := m) (by simp [hlist])
          have hd : 0 < t.prod := by
            by_contra! hnot
            have hz : t.prod = 0 := by omega
            simp [hlist, hz] at hprod
            omega
          have hfactor : m = t.prod * p := by
            calc
              m = p * t.prod := by simpa only [hlist, List.prod_cons] using hprod.symm
              _ = t.prod * p := Nat.mul_comm p t.prod
          have hdSign : lambda t.prod = (1 : ℤ) := by
            rw [hfactor, lambda_mul hd hp.pos, lambda_prime hp] at hminus
            omega
          have hpne : p ≠ 2 := by
            intro heq
            apply hEven
            exact ⟨t.prod, by rw [hfactor, heq]; ring⟩
          suffices hcore : HasRepresentation (4 * p) by
            have scaled := hasSignedRepresentation_mul hd hcore
            have hscale : t.prod * (4 * p) = 4 * m := by rw [hfactor]; ring
            simpa [HasRepresentation, hdSign, hscale] using scaled
          done

end ArithmeticStatement
