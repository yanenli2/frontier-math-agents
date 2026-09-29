Mode: DISCOVERY — conjectural; no proof weight.

# Mangerel v2: source extraction and target-gap report

**Status: UNVERIFIED source package / literature context only.** The statements below were read in the specified PDF, not independently proved or formally imported. Eligibility/provenance, a source's mathematical claim, project acceptance, and Lean verification are distinct. No proof of the user's conjecture is offered here.

## 1. Source identity and eligibility

- **Author:** Alexander P. Mangerel.
- **Title:** *On a Goldbach-type problem for the Liouville function*.
- **Pinned version:** arXiv:2404.12117v2, 14 pages.
- **Version URLs:** https://arxiv.org/abs/2404.12117v2 ; https://arxiv.org/pdf/2404.12117v2 . These identify the source; neither was fetched in this invocation.
- **Local PDF:** `.clawcodex/math-team/problems/liouville-goldbach-jul2026/knowledge/mangerel-v2/paper.pdf`.
- **Supplied SHA-256:** `ae26a659220985c55576a18d05a84d5a56988024f8781ae4ccbe04847ac16505`. This digest was supplied by the assignment, not recomputed here.
- **Local metadata:** same directory, `arxiv-metadata.txt`; lines 7, 31, and 35–38 identify v2 and give its submission time as **2024-05-02 14:48:54 UTC**. The assignment reports independent leader `/browse` verification. The PDF's first-page margin independently reads `arXiv:2404.12117v2 [math.NT] 2 May 2024`.
- **Cutoff:** 2026-07-31 inclusive. The specified v2 predates it. The unversioned DOI in the metadata is not used to authorize another version.
- **Inspected:** PDF/printed pages 1–4 and the bibliography on page 14. Page 3 was read a second time to check the displayed inequalities. No other mathematical source was opened.

Transcriptions below normalize line wrapping and mathematical typography, but retain mathematical signs, constants, and quantifiers. Bracketed reference numbers belong to this paper.

## 2. Definitions and notation in the inspected source

**Page 1, Problem 1.1:**

\[
\mathcal L_\lambda(N):=\sum_{1\le n<N}\lambda(n)\lambda(N-n).
\]

The problem asks that, for every \(N\ge3\), this satisfy \(|\mathcal L_\lambda(N)|<N-1\). Its footnote 1 says no range for \(N\) was actually given in the cited problem, and that \(N\ge3\) is the author's presumed intended range. **Problem 1.1 is a posed problem, not a proved all-\(N\) theorem.**

The source calls \(\lambda\) the Liouville function. The inspected pages do **not** explicitly define it as \((-1)^{\Omega(n)}\), define \(\Omega\), or state an \(\Omega(1)\) convention. They use the usual sign-valued and multiplicative properties: page 4 explicitly says each summand is \(\pm1\), and displays reductions using \(\lambda(1)=1\) and multiplicativity. The project's definition must still be taken from `request.md` and independently matched to any formal implementation.

**Important notation distinction:** the paper's \(\mathcal L_\lambda(N)\) is the request's **\(C(N)\)**, not its summatory function \(L(N-1)\). The paper writes the latter sum explicitly as \(\sum_{n<N}\lambda(n)\). Its \(L(1,\chi)\) in Remark 1 is a Dirichlet \(L\)-value, a third object. The shorthand \(\sum_{n<N}\) in these displays has the positive-integer range specified in the definition above.

## 3. Exact extracted theorem: Theorem 1.2

**Locator:** page 1, last main-text statement.

> **Theorem 1.2.** There exists \(N_0\in\mathbb N\) such that if \(N\ge N_0\) then \(|\mathcal L_\lambda(N)|<N-1\).

**Hypotheses/scope:** integer \(N\) in the positive-integer setting of the introduction; sufficiently large; no evenness, primality, or coprimality hypothesis. The source states an unconditional result. It neither supplies a numerical \(N_0\) here nor asserts the inequality for every \(N\ge3\).

**Relationship to the obligation:** this is a sufficiently-large-\(N\), strict correlation bound, not the assertion that every even \(N>2\) has a decomposition with both Liouville signs negative. It is also not an almost-all statement: its stated eventual range covers every integer above its threshold, but for a different conclusion.

## 4. Exact extracted effectiveness statement: Remark 1

**Locator:** page 2, opening paragraph.

> **Remark 1.** The proof of Theorem 1.2 relies on Siegel's theorem on lower bounds for \(L(1,\chi)\), where \(\chi\) is a quadratic Dirichlet character. Thus, the lower bound \(N_0\) is ineffective. See Remark 3 below for an indication of what sorts of effective results (up to a possible unique exception) may be proved, in the case of \(N\) prime, using the Siegel-Tatuzawa theorem [9].

The source's word “ineffective” is explicit; this is not merely a missing numerical computation in the extraction. The reference to possible effective results retains **both** qualifications: prime \(N\) and a possible unique exception. It is not a claim of an effective all-even-\(N\) theorem. Remark 3 itself was outside this extraction's inspected pages and is not reconstructed here.

**Further source context, not independently verified:** the proof-strategy discussion on page 2 cites Siegel's theorem as `[6, Thm. 5.28(2)]` and identifies it as the source of ineffectivity. Page 3 cites Linnik's theorem as `[6, Thm. 18.1]`, with an effectively computable constant, but still concludes only that \(N\) is bounded by some \(N_0\). The effective ingredient does not cancel the stated ineffectivity of Theorem 1.2.

## 5. Exact target discussion and displays: Remark 2

**Locator:** page 3, Remark 2 in full, including numbered display (2).

> **Remark 2.** One may also ask another natural Goldbach-type problem regarding the Liouville function: given an even integer \(N\ge4\), must there exist \(1\le a,b\le N\) with \(a+b=N\), such that \(\lambda(a)=\lambda(b)=-1\)? This is obviously implied by the binary Goldbach conjecture, and therefore a weakening of it.
>
> The methods of this paper appear to be far too rigid to address this problem directly. Note, however, that even a result of the form

\[
\tag{2}
\left|\sum_{n<N}\lambda(n)\lambda(N-n)\right|<N-g(N),
\]

> where \(g:\mathbb R\to\mathbb R\) is a (sufficiently quickly) increasing function satisfying \(g(x)=o(x)\), would suffice to prove the existence of such a pair \((a,b)\).
>
> Indeed, suppose otherwise. Then for any \(1\le n<N\), \((1-\lambda(n))(1-\lambda(N-n))=0\). It follows that

\[
0=\sum_{1\le n<N}(1-\lambda(n))(1-\lambda(N-n))
 =N-1-2\sum_{n<N}\lambda(n)+\sum_{n<N}\lambda(n)\lambda(N-n).
\]

> We deduce from this and the prime number theorem that, e.g.,

\[
\left|\sum_{n<N}\lambda(n)\lambda(N-n)\right|
>N-2\left|\sum_{n<N}\lambda(n)\right|
\ge N-CNe^{-\sqrt{\log N}},
\]

> for some absolute constant \(C>0\) and all \(N\ge3\). Thus, the choice \(g(x)=Cxe^{-\sqrt{\log x}}\) would suffice to this end.
>
> It is natural to ask to what extent the techniques in this paper may be perturbed in order to prove a bound like (2). We plan to return to this problem in a future paper.

**Footnote 2, page 3:** credits Mark Shusterman for pointing out this problem and identifies his MathOverflow post:
`http://mathoverflow.net/questions/307479/goldbachs-conjecture-for-the-liouville-function`.
This is a reference copied from the eligible PDF, not a visited or independently date-verified webpage.

### Reading safeguards for Remark 2

1. **Same target, posed rather than solved.** For integers, even \(N\ge4\) matches even \(N>2\). The source's \(1\le a,b\le N\) adds no effective restriction beyond positive integers with \(a+b=N\); positivity forces each summand below \(N\). No distinctness, primality, oddness, or coprimality requirement appears. Thus the remark really does discuss the user's target, but as a question.
2. **Hypothetical estimate, not another theorem.** Display (2) is proposed as a sufficient kind of bound; it is not asserted proved in this paper. “Sufficiently quickly” is part of the source wording, not a precise rate condition supplied by Theorem 1.2. The displayed example of \(g\) gives the intended analytic scale. The promised future paper is not evidence that such a paper or result exists.
3. **The zero is conditional.** The exact identity displayed here has left side zero only under the supposition that no required pair exists. The paper does not introduce the request's ordered-pair count \(R(N)\). Its expansion corresponds to the expression on the right of the request's proposed general identity \(4R(N)=(N-1)-2L(N-1)+C(N)\); this extraction does not certify that identity in Lean.
4. **Apparent display defect; do not silently repair it.** The subsequent display really prints **\(>N-2|\sum_{n<N}\lambda(n)|\)**, whereas the preceding exact identity contains **\(N-1\)**. This creates an apparent off-by-one/strictness mismatch. A fresh verifier must audit the deduction and constants before using any sufficient-condition formulation. The printed inequality has been preserved, not promoted to an accepted lemma or quietly corrected.
5. **PNT remains an external dependency.** The prime number theorem is invoked by name in this remark, without a numbered citation or proof of the displayed quantitative summatory estimate here. Its quantitative form, constants, valid range, and any adjustment for the preceding display issue need separate eligible evidence or a project proof. Neither PNT nor Siegel is project-proved by virtue of this extraction.

## 6. Mathematical gaps to the universal target

- **Conclusion gap:** Theorem 1.2 excludes extremal correlation \(\pm(N-1)\). Having both signs among the products \(\lambda(n)\lambda(N-n)\) does not by itself identify a pair with both values \(-1\); a positive product may instead come from two \(+1\) values. The request requires positivity of its exact counting expression, not merely non-extremality of \(C(N)\).
- **Quantitative gap:** the paper expressly proposes a stronger saving \(g(N)\) on an analytic scale relevant to the summatory Liouville function. Its proved saving relative to the trivial bound is not that estimate. One cannot substitute Theorem 1.2 for (2).
- **Uniformity/effectivity gap:** the theorem has an ineffective eventual threshold, and the hypothetical strengthened estimate is not supplied. An eventual target proof would still need an effective threshold and rigorous coverage of every remaining admissible even integer, as `request.md` requires. No such coverage is contained in this evidence bundle.
- **Dependency/verification gap:** the definition bridge, finite counting identity, any analytic theorem actually used, range/constant bookkeeping, and every formal dependency remain separate obligations. No Lean file, import, compilation, axiom inspection, or proof acceptance was performed here.
- **Literature-status limitation:** the source treats the exact target as a further problem in May 2024. This is not a claim that the target remained open at the July 2026 cutoff, nor a proof that an effective result does not exist elsewhere.

## 7. Bibliographic citations copied from page 14

These are **secondary citation leads only**. Their own texts, version provenance, and theorem hypotheses were not audited or imported.

- **[6]** H. Iwaniec and E. Kowalski. *Analytic number theory*, volume 53 of *American Mathematical Society Colloquium Publications*. American Mathematical Society, Providence, RI, 2004. Source locators: `[6, Thm. 5.28(2)]` for Siegel on page 2; `[6, Thm. 18.1]` for Linnik on page 3. No exact usable statement from the book is claimed here.
- **[8]** American Institute of Mathematics. *AIM problem list: Sarnak's conjecture*, 2018. `http://aimpl.org/sarnakconjecture/5/`. Page 1 calls the cited item “Problem 5.1 of [8]”; the author explicitly qualifies its presumed range in footnote 1. The webpage was not opened.
- **[9]** T. Tatuzawa. *On a theorem of Siegel*. *Japan. J. Math.*, 21:163–178, 1951. This is the reference attached to the Siegel-Tatuzawa discussion in Remark 1. Its text was not opened.

## 8. Reusable candidates, all UNVERIFIED

Stored here only, respecting the single-file ownership assignment; no external wiki or separate knowledge inbox was modified.

| Candidate | Source locator | Reuse boundary |
|---|---|---|
| Eventual strict correlation bound | Theorem 1.2, p. 1 | Exact literature statement; ineffective threshold; does not assert the target. |
| Explicit effectiveness limitation | Remark 1, p. 2 | Source disclosure; prime-only qualified follow-on mention is not an effective all-even result. |
| Exact-target formulation and conditional zero identity | Remark 2, p. 3 | Useful statement/notation reference; identity and definition bridge need project verification. |
| Stronger-saving/PNT route | Remark 2, p. 3, (2) and following display | Proposed sufficient route only; unproved saving, external PNT, and apparent display defect remain obligations. |

## 9. Compact search trace and exposure log

1. Read the assigned protocol and `request.md`; retained the all-even, positive-summand target and cutoff.
2. Read supplied `arxiv-metadata.txt`; checked v2/date against the PDF margin and the assignment's leader-verified timestamp.
3. Read PDF pages 1–4 beyond the abstract; extracted Problem 1.1's definition, Theorem 1.2, Remarks 1–2, and the effectiveness citations in the proof-strategy paragraphs.
4. Read page 14 to identify references [6], [8], [9]. The same rendered page also showed the end of a proof; it supplied no additional extracted candidate.
5. Re-read page 3 to preserve the exact conditional identity and subsequent inequality signs. Detected the apparent off-by-one/strictness issue and left it flagged for independent audit.
6. Checked the assigned output path before writing; no prior file existed. Wrote this artifact only.

**Search scope:** the supplied pinned source and metadata only; zero WebSearch/WebFetch calls. No follow-up literature search was undertaken. No supplied general reference/wiki index was part of this narrow input packet, and none was opened. Citation tracing stopped at the bibliography; no cited work or mutable webpage was fetched.

**Exposure log for this invocation:** no later-version, post-cutoff, or unversioned mathematical source was accessed. All rendered mathematical pages belonged to the assigned v2 PDF. URLs embedded in the source were copied as citation data only. No prior exposure log was supplied to this invocation or modified.

**Next direction, not performed:** a separately authorized, date-filtered search for follow-ups between 2024-05-02 and 2026-07-31 that explicitly prove the exact all-even-\(N\) target or an effective sufficiently-large version; verify each promising version's availability date and full theorem. This extraction makes no negative existence claim about that unsearched scope.
