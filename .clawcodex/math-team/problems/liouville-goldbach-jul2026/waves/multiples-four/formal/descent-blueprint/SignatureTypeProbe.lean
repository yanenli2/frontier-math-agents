import Statement.Partial
import Mathlib.Data.ZMod.Basic

set_option autoImplicit false

namespace ArithmeticStatement.FourWork

def residueLambda (p : ℕ) (z : ZMod p) : ℤ :=
  lambda z.val

def GoodMultiplier (p : ℕ) (a : ZMod p) : Prop :=
  a ≠ 0 ∧ ∀ z : ZMod p, z ≠ 0 →
    residueLambda p (a * z) = residueLambda p a * residueLambda p z

#check ∀ {p n : ℕ}
    (hno : ¬ HasRepresentation (4 * p))
    (hn : 0 < n) (hnp : n < p) (hs : lambda n = (-1 : ℤ)),
    lambda (p - n) = (1 : ℤ)

#check ∀ {p n : ℕ}
    (hno : ¬ HasRepresentation (4 * p))
    (hn : 0 < n) (hnp : n < 2 * p) (hs : lambda n = (1 : ℤ)),
    lambda (2 * p - n) = (-1 : ℤ)

#check ∀ {p x y : ℕ}
    (hno : ¬ HasRepresentation (4 * p))
    (hx : 0 < x) (hy : 0 < y) (hsum : x + y = p)
    (hxsign : lambda x = (1 : ℤ)) (hysign : lambda y = (1 : ℤ)),
    ¬ 3 ∣ x

#check ∀ {p x y : ℕ}
    (hp : Nat.Prime p) (hp3 : p ≠ 3)
    (hno : ¬ HasRepresentation (4 * p))
    (hx : 0 < x) (hxy : x < y) (hsum : x + y = p)
    (hxsign : lambda x = (1 : ℤ)) (hysign : lambda y = (1 : ℤ)),
    ∃ u v : ℕ, 0 < u ∧ u < v ∧ u + v = p ∧
      lambda u = (1 : ℤ) ∧ lambda v = (1 : ℤ) ∧ v - u < y - x

#check ∀ {p : ℕ}
    (hp : Nat.Prime p) (hp2 : p ≠ 2) (hp3 : p ≠ 3)
    (hno : ¬ HasRepresentation (4 * p))
    {x y : ℕ} (hx : 0 < x) (hy : 0 < y) (hsum : x + y = p),
    ¬ (lambda x = (1 : ℤ) ∧ lambda y = (1 : ℤ))

#check ∀ {p : ℕ}
    (hp : Nat.Prime p) (hp2 : p ≠ 2) (hp3 : p ≠ 3)
    (hno : ¬ HasRepresentation (4 * p)),
    ∀ n : ℕ, 0 < n → n < p → lambda (p - n) = -lambda n

#check ∀ {p n : ℕ}
    (hp : Nat.Prime p) (hn : 2 ≤ n) (hnp : n < p)
    (z : ZMod p) (hz : z ≠ 0),
    ∃ k : ℤ, ∃ d : ℕ, k ≠ 0 ∧ k.natAbs < n ∧
      0 < d ∧ n * d < p ∧ (k : ZMod p) * z = (d : ZMod p)

#check ∀ {p n : ℕ} (hnp : n < p),
    residueLambda p (n : ZMod p) = lambda n

#check ∀ {p : ℕ} {z : ZMod p} (hz : z ≠ 0),
    residueLambda p z = (1 : ℤ) ∨ residueLambda p z = (-1 : ℤ)

#check ∀ {p : ℕ} (hp : Nat.Prime p)
    (hanti : ∀ n : ℕ, 0 < n → n < p → lambda (p - n) = -lambda n)
    {z : ZMod p} (hz : z ≠ 0),
    residueLambda p (-z) = -residueLambda p z

#check ∀ {p : ℕ} (hp : Nat.Prime p),
    GoodMultiplier p (1 : ZMod p)

#check ∀ {p : ℕ} (hp : Nat.Prime p)
    (hanti : ∀ n : ℕ, 0 < n → n < p → lambda (p - n) = -lambda n)
    {a : ZMod p} (ha : GoodMultiplier p a),
    GoodMultiplier p (-a)

#check ∀ {p n : ℕ} (hp : Nat.Prime p)
    (hanti : ∀ j : ℕ, 0 < j → j < p → lambda (p - j) = -lambda j)
    (hn : 0 < n) (hnp : n < p)
    (hsmall : ∀ j : ℕ, 0 < j → j < n → GoodMultiplier p (j : ZMod p)),
    GoodMultiplier p (n : ZMod p)

#check ∀ {p : ℕ} (hp : Nat.Prime p)
    (hanti : ∀ n : ℕ, 0 < n → n < p → lambda (p - n) = -lambda n)
    {a b : ZMod p} (ha : a ≠ 0) (hb : b ≠ 0),
    residueLambda p (a * b) = residueLambda p a * residueLambda p b

#check ∀ {p n : ℕ} (hp : Nat.Prime p)
    (hanti : ∀ j : ℕ, 0 < j → j < p → lambda (p - j) = -lambda j)
    (hn : 0 < n) (hnp : n < p) (hsquare : IsSquare (n : ZMod p)),
    lambda n = (1 : ℤ)

#check ∀ {p r : ℕ}
    (hp : Nat.Prime p) (hLower : 7 ≤ p) (hMod : p % 4 = 3)
    (hr : Nat.Prime r) (hdiv : r ∣ (p + 1) / 4),
    IsSquare (r : ZMod p)

#check ∀ {p : ℕ}
    (hp : Nat.Prime p) (hLower : 7 ≤ p) (hMod : p % 4 = 3),
    ∃ r : ℕ, Nat.Prime r ∧ r ∣ (p + 1) / 4 ∧
      r ≤ (p + 1) / 4 ∧ r < p ∧ IsSquare (r : ZMod p)

end ArithmeticStatement.FourWork

namespace ArithmeticStatement

#check ∀ {p : ℕ}
    (hp : Nat.Prime p) (hLower : 7 ≤ p) (hMod : p % 4 = 3),
    HasRepresentation (4 * p)

#check ∀ (m : ℕ) (hm : 0 < m),
    HasRepresentation (4 * m)

end ArithmeticStatement
