universe u

def Even {α : Type u} [Add α] (a : α) : Prop := ∃ r, a = r + r

namespace Nat

def minFacAux (n : ℕ) : ℕ → ℕ
  | k =>
    if n < k * k then n
    else
      if k ∣ n then k
      else
        minFacAux n (k + 2)

def minFac (n : ℕ) : ℕ :=
  if 2 ∣ n then 2 else minFacAux n 3

def primeFactorsList : ℕ → List ℕ
  | 0 => []
  | 1 => []
  | k + 2 =>
    let m := minFac (k + 2)
    m :: primeFactorsList ((k + 2) / m)

theorem prime_def_lt {p : ℕ} :
  Prime p ↔ 2 ≤ p ∧ ∀ m < p, m ∣ p → m = 1

theorem minFac_dvd (n : ℕ) : minFac n ∣ n

theorem minFac_prime {n : ℕ} (n1 : n ≠ 1) : Prime (minFac n)

theorem minFac_le_of_dvd {n : ℕ} :
  ∀ {m : ℕ}, 2 ≤ m → m ∣ n → minFac n ≤ m

theorem primeFactorsList_zero : primeFactorsList 0 = []

theorem primeFactorsList_one : primeFactorsList 1 = []

theorem primeFactorsList_two : primeFactorsList 2 = [2]

theorem primeFactorsList_add_two (n : ℕ) :
  primeFactorsList (n + 2) = minFac (n + 2) :: primeFactorsList ((n + 2) / minFac (n + 2))

theorem prime_of_mem_primeFactorsList {n : ℕ} :
  ∀ {p : ℕ}, p ∈ primeFactorsList n → Prime p

theorem prod_primeFactorsList :
  ∀ {n}, n ≠ 0 → List.prod (primeFactorsList n) = n

theorem Prime.primeFactorsList_pow {p : ℕ} (hp : p.Prime) (n : ℕ) :
  (p ^ n).primeFactorsList = List.replicate n p

end Nat
