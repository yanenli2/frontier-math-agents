universe u

variable {α : Type u}

@[implicit_reducible] def List.length : List α → Nat
  | nil => 0
  | cons _ as => HAdd.hAdd (length as) 1

namespace List

def replicate : (n : Nat) → (a : α) → List α
  | 0, _ => []
  | n + 1, a => a :: replicate n a

theorem length_nil : length ([] : List α) = 0

theorem length_cons {a : α} {as : List α} :
  (cons a as).length = as.length + 1

end List
