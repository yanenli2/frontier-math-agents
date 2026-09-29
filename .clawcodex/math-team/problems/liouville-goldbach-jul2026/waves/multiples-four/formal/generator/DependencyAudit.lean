import Statement.Partial

set_option autoImplicit false

open ArithmeticStatement

#check (∀ (m : ℕ) (hm : 0 < m), HasRepresentation (4 * m))
#check representation_multiple_eight
#check representation_diagonal
#check lambda_mul
#check hasSignedRepresentation_mul
#check Nat.prod_primeFactorsList
#check Nat.prime_of_mem_primeFactorsList
#check four_mul_representation_count
#check representation_count_pos_iff
#check count_pos_iff_keystone

#print axioms ArithmeticStatement.omega
#print axioms ArithmeticStatement.lambda
#print axioms ArithmeticStatement.HasSignedRepresentation
#print axioms ArithmeticStatement.HasRepresentation
#print axioms ArithmeticStatement.lambda_one
#print axioms ArithmeticStatement.lambda_sign
#print axioms ArithmeticStatement.lambda_mul
#print axioms ArithmeticStatement.lambda_prime
#print axioms ArithmeticStatement.lambda_four
#print axioms ArithmeticStatement.hasSignedRepresentation_mul
#print axioms ArithmeticStatement.representation_diagonal
#print axioms ArithmeticStatement.representation_multiple_eight
#print axioms ArithmeticStatement.four_mul_representation_count
#print axioms ArithmeticStatement.representation_count_pos_iff
#print axioms ArithmeticStatement.count_pos_iff_keystone
#print axioms Nat.prod_primeFactorsList
#print axioms Nat.prime_of_mem_primeFactorsList
