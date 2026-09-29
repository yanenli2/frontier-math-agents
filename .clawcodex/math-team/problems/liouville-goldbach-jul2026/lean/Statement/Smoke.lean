import Statement.Scaffold

open ArithmeticStatement

#eval (1 : ℕ).primeFactorsList
#eval (12 : ℕ).primeFactorsList
#eval [1, 2, 4, 8, 12, 18].map (fun n => (n, omega n, lambda n))

#eval do
  unless (1 : ℕ).primeFactorsList == [] do
    throw (IO.userError "factor list at one failed")
  unless (12 : ℕ).primeFactorsList == [2, 2, 3] do
    throw (IO.userError "factor multiplicity smoke test failed")
  unless omega 1 == 0 && lambda 1 == (1 : ℤ) do
    throw (IO.userError "normalization at one failed")
  unless omega 4 == 2 && lambda 4 == (1 : ℤ) do
    throw (IO.userError "prime-square multiplicity smoke test failed")
  unless omega 8 == 3 && lambda 8 == (-1 : ℤ) do
    throw (IO.userError "prime-cube multiplicity smoke test failed")
  IO.println "definition smoke checks passed"

#check (Target : Prop)
#print ArithmeticStatement.omega
#print ArithmeticStatement.lambda
#print ArithmeticStatement.Target
#print ArithmeticStatement.UnfinishedScaffold
#print axioms ArithmeticStatement.omega
#print axioms ArithmeticStatement.lambda
#print axioms ArithmeticStatement.Target
#print axioms ArithmeticStatement.UnfinishedScaffold.mk
#print Even
#print Nat.primeFactorsList
#check Nat.primeFactorsList_zero
#check Nat.primeFactorsList_one
#check Nat.prime_of_mem_primeFactorsList
#check Nat.prod_primeFactorsList
#check Nat.primeFactorsList_unique
#check Nat.Prime.primeFactorsList_pow
#check Nat.perm_primeFactorsList_mul
#print axioms Nat.primeFactorsList
#print axioms Nat.primeFactorsList_one
#print axioms Nat.prime_of_mem_primeFactorsList
#print axioms Nat.prod_primeFactorsList
#print axioms Nat.Prime.primeFactorsList_pow
