import Statement.Partial

set_option autoImplicit false

namespace MultipleFourStatementInterface

def statement : Prop :=
  ∀ (m : ℕ) (hm : 0 < m), ArithmeticStatement.HasRepresentation (4 * m)

#print statement
#print axioms statement

#check fun (h : statement) (m : ℕ) (hm : 0 < m) =>
  (show ArithmeticStatement.HasRepresentation (4 * m) from h m hm)

#check fun (h : statement) (hm : (0 : ℕ) < 1) =>
  (show ArithmeticStatement.HasRepresentation 4 from h 1 hm)

end MultipleFourStatementInterface
