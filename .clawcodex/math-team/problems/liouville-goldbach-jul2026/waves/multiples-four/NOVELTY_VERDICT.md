# Novelty verdict: the multiples-of-four Liouville–Goldbach proof

Prepared 2026-09-28 for the accepted result `ArithmeticStatement.representation_multiple_four` (every positive multiple of four is a sum of two positive integers with Liouville value −1), as proved in [PROOF.md](PROOF.md).

## Summary

| Question | Verdict |
|---|---|
| Did the project depend on a library or repository that already contained this result? | **No.** No dependency found. |
| Is the theorem new? | **No.** CaptainSude's all-even theorem (public 2026-09-16) implies it. |
| Is the proof strategy new? | **No.** The rigidity endgame (antireflection ⇒ quadratic character ⇒ contradiction at a small prime quadratic residue) is Mangerel's, IMRN 2024. |
| Is any step new? | **Plausibly yes.** The bridge from a *missing Goldbach pair at 4p* to *full antireflection* (§§3–4) was not found in any source checked. The combinatorial multiplicativity argument (§5) is a new *method* for a known conclusion. |

The contribution is best described as an independent, fully elementary proof of the multiples-of-four case, with an apparently new bridge from the Goldbach-type hypothesis to Mangerel's rigidity setting. §2 must be credited to Mangerel (arXiv:2412.17199, §6.2) and §6 to Chowla–Cowles–Cowles (1980).

## 1. Dependency audit (no leakage found)

**Evidence.**

1. **No reference to the competing proof.** Outside the Lean build cache, a search of the problem directory for `CaptainSude` and `Astra` matches nothing except this verdict. The matches for `liouville-goldbach` are only the project's own directory name `liouville-goldbach-jul2026`. No file imports or cites CaptainSude's repository.
2. **Dependencies.** `lean/lakefile.toml` requires only Mathlib at `905b95818eb32af7874a58b427f50c1711a5e96c`. `lake-manifest.json` adds only Mathlib's standard companions: plausible, LeanSearchClient, importGraph, ProofWidgets4, aesop, Qq, batteries and Cli.
3. **Mathlib contains no Goldbach-type Liouville result.** In the checked-out pin, `grep -ril goldbach Mathlib` returns only `NumberTheory/Fermat.lean`. Its "Goldbach's theorem" is the unrelated fact that distinct Fermat numbers are coprime. `ArithmeticFunction.liouville` exists but is not used, because the project defines its own `lambda` from `primeFactorsList` in `Statement/Definitions.lean`.
4. **Timing.** The Mathlib pin was published 2026-07-28 (release workflow 30379912464), seven weeks before CaptainSude's 2026-09-16 release. CaptainSude builds on a later Mathlib (`de2ef682…`) and Lean v4.34.0-rc2. This project uses Lean v4.32.2.
5. **Mathlib results actually used** are general and long-standing: quadratic reciprocity and the supplement at 2, `ZMod.exists_sq_eq_neg_one_iff`, `Nat.Prime.sq_add_sq`, `ZMod` field structure, finite pigeonhole, and factorization lemmas. See [sources.md](sources.md) §§3–4 for line-level locators.
6. **Search hygiene.** `nl/searcher/search-trace.md` records one post-cutoff MathOverflow hit (revision 2026.9.15) that was excluded and not opened.

**Limits.** The provenance ledger was written by the agent team itself. This audit cannot inspect the base model's training data.

**Correction to an earlier informal claim.** The *written* proof of §6 avoids quadratic reciprocity (it uses a Gauss-lemma floor count). The *Lean* proof does not: `Character/ResiduePrime.lean` uses Mathlib's quadratic reciprocity, and the p ≡ 1 (mod 4) case uses `Nat.Prime.sq_add_sq`. The reciprocity-free argument is not formalized.

## 2. Sources compared

| Source | Date | Read by the team before this audit? |
|---|---|---|
| A. P. Mangerel, *On a Goldbach-type problem for the Liouville function*, arXiv:2404.12117v2 | 2024-05-02 | Yes, pages 1–4 and 14 (`nl/searcher/extraction-v2.md`) |
| A. P. Mangerel, same title, *IMRN* 2024(16):11865–11877, doi:10.1093/imrn/rnae149 (journal version, rewritten to be fully elementary) | 2024-07-03 | **No** |
| A. P. Mangerel, *On Shusterman's Goldbach-type problem for sign patterns of the Liouville function*, arXiv:2412.17199v1 | 2024-12-23 | No |
| S. Chowla, J. Cowles, M. Cowles, *The least prime quadratic residue and the class number*, J. Number Theory (cited as [2] in IMRN) | 1980 | No |
| CaptainSude, *Liouville-Goldbach* (GitHub, v1.0.0), attributed by the poster to "GPT-6 Astra" | 2026-09-15/16 | No (after the 2026-07-31 cutoff) |

## 3. Step-by-step comparison

| Proof step ([PROOF.md](PROOF.md)) | Prior occurrence | Verdict |
|---|---|---|
| §2 reduction: 2m + 2m when λ(m) = 1; 8 = 3 + 5 = 4 + 4 scaled for even m; scale a 4p pair by d with λ(d) = 1 | arXiv:2412.17199 §6.2, case (ii): "as 8 = 4 + 4 = 3 + 5 … a = b = 4N′ … a = 3N′, b = 5N′"; case (iii): a = b = N/2 | **Known**, except for the reduction to 4p for odd primes p |
| §3 rules (A), (B), (C), obtained by scaling pairs by 4 and by 2 | IMRN Lemma 2.2 derives similar local identities by splitting p = (p+m)/2 + (p−m)/2 and p = (2p+m)/3 + (p−m)/3, but *from* the constancy of λ(m)λ(p−m) | **Similar tools, different direction** |
| §4 ternary gap descent (x, y) → ((p+x)/3, (p+y)/3), giving **full antireflection** f(p−n) = −f(n) from a missing −1/−1 pair at 4p | Not found. In IMRN, antireflection (λ(m)λ(p−m) constant, eq. (3)) is the **hypothesis** \|L_λ(p)\| = p − 1, not a consequence. IMRN Remark 2 says the methods "appear to be far too rigid" for the Goldbach-type problem | **Plausibly new.** This is the bridge that the prior work lacked |
| §5 antireflection ⇒ multiplicativity on (ℤ/pℤ)^×, by least bad multiplier and circular gaps (nd < p) | Same conclusion as IMRN Lemma 2.3, Proposition 2.4 and Lemma 2.5, but reached with Fourier coefficients, Plancherel, an iterative j-descent (§3), a primitive root and Gauss sums | **Known conclusion, new elementary method.** Possible folklore not ruled out |
| §6 a prime r dividing (p+1)/4 is a nonzero square mod p (p ≡ 3 mod 4, p ≥ 7) | IMRN Proposition 2.6 cites Chowla–Cowles–Cowles for "a prime q ≤ (p+1)/4 < p such that χ_p(q) = +1". CaptainSude chooses the same prime and proves it by reciprocity | **Known.** The Gauss-lemma proof is a self-contained re-proof |
| §7 contradictions: F(−1) = −1 against −1 being a square (p ≡ 1 mod 4); λ(r) = −1 against r being a square (p ≡ 3 mod 4) | IMRN Proposition 2.6: "for each prime q < p we have χ_p(q) = −1", contradicted by a small prime residue | **Known** |

## 4. Relation to CaptainSude's proof

CaptainSude proves the stronger prime lemma "2p has a +1/+1 pair for every prime p > 3". Doubling that pair yields this project's 4p statement. Their argument also follows IMRN's structure: first make multiplication by 2 and 3 exact (their "commuting square", compare IMRN Lemma 2.3), then extend to all multipliers (their short-representative lemma, compare IMRN Proposition 2.4), and finish with the same (p+1)/4 prime. Their credit to "Mangerel's rigidity and commuting-defect arguments" is accurate.

The two proofs are independent and differ in the middle step. This project's §4 reaches **full** antireflection on (0, p), which the 4p hypothesis permits because scaling by 4 preserves signs. CaptainSude works only on (0, p/2) with an odd completion, because the weaker 2p hypothesis flips signs under scaling by 2.

## 5. Recommended attribution

- §2: Mangerel, arXiv:2412.17199, §6.2.
- §§5–7 overall strategy: Mangerel, IMRN 2024, §2 (rigidity via comparison with the Legendre symbol).
- §6: Chowla, Cowles and Cowles (1980), as cited in IMRN [2].
- Independence note: the team read only arXiv:2404.12117v2 (pages 1–4, 14). It did not read the IMRN version, 2412.17199 or Chowla–Cowles–Cowles, and nothing after the 2026-07-31 cutoff.

## 6. Open items

1. Search for folklore versions of the §5 argument ("multiplicative on short products implies a character") before claiming novelty of method.
2. Any novelty claim for §4 should be checked by a specialist, for example Mangerel.
3. Formalize the reciprocity-free proof of §6 if the "no reciprocity" claim is to be made for the Lean artifact.
