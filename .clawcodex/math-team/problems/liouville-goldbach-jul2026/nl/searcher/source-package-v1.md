Mode: DISCOVERY — conjectural; no proof weight.

# Source package v1: Liouville–Goldbach

Status: **UNVERIFIED SOURCE INBOX / discovery only. No mathematical source admitted.**

## Assignment and target

- Request: `../../request.md`, especially lines 7–14 and 16–27.
- Exact target: for every even integer N > 2, there are positive integers a,b with N = a+b and lambda(a) = lambda(b) = -1, where lambda(n) = (-1)^Omega(n), prime factors are counted with multiplicity, and Omega(1) = 0. Equality a=b is allowed.
- Cutoff: source version demonstrably public by 2026-07-31 inclusive. Search filters are not date verification.
- Scope: five focused WebSearch queries; at most one citation hop per promising result. No WebFetch and no full-page web retrieval by this worker. Full inspection must use the leader's `/browse` driver.
- Read local protocol, knowledge workflow, request, RUN, and sources ledger. No local reference/wiki index was supplied; the index-name scan under `.clawcodex` returned no matches. The local ledger says no mathematical literature has yet been admitted.
- Ownership restricts this worker to `P/nl/searcher/`; this file is the problem-local unverified intake package. No shared ledger, external wiki, or task board was edited.

## Executive result

A highly relevant primary-source lead was discovered:

**On a Goldbach-type problem for the Liouville function**, arXiv **2404.12117**.

The search index identifies **v2, 2 May 2024**, and returns a publisher record in *International Mathematics Research Notices*. However, neither version history nor the paper body has been inspected. These are discovery metadata, not independently verified publication facts.

Search snippets advertise a nontrivial convolution-sum bound “for all sufficiently large integers N.” Another snippet mentions **Theorem 1.2, Remark 1**, and use of Siegel's lower bound for L(1,chi) for quadratic Dirichlet characters. This is an unusually close lead, but it does **not** yet supply an audited exact theorem, a universal all-N proof, or an effective threshold. In particular, no inference of ineffectivity is certified merely from the Siegel-theorem snippet.

**Current blocker:** the required beyond-abstract primary-source inspection has not occurred. `SendMessage(to="team-lead", ...)` failed with `Only active team members can send team messages`, so the browsing request could not be delivered through that channel. Exact requests are recorded below for the leader. No open-status conclusion is drawn.

## SP1 — UNVERIFIED primary lead (highest priority)

### Provenance

- Indexed title: *On a Goldbach-type problem for the Liouville function*.
- Authors: **not established by inspected evidence**; obtain from the pinned source.
- Identifier: arXiv:2404.12117.
- Discovery URLs actually returned by search:
  - https://arxiv.org/abs/2404.12117
  - https://arxiv.org/pdf/2404.12117
  - https://academic.oup.com/imrn/article/2024/16/11865/7704606
- The PDF result's indexed title is `arXiv:2404.12117v2 [math.NT] 2 May 2024`.
- Proposed exact-version requests, constructed using arXiv's versioned URL form; **not fetched or independently existence/date checked by this worker**:
  - https://arxiv.org/abs/2404.12117v2
  - https://arxiv.org/pdf/2404.12117v2
- Candidate availability: 2024-05-02 for v2, from the search-result title only. This is before the cutoff but **eligibility remains unverified** until primary submission metadata is checked.
- Publisher publication date, DOI, authors, final pagination, corrections, and version equivalence: not checked. Do not treat a current publisher page as an eligible frozen mathematical source merely because its URL contains `2024`.

### Exact usable theorem and locator

**None extracted yet.** No theorem body or PDF page was inspected. Do not cite this package as evidence for a mathematical statement.

Locator leads only:

1. Abstract snippet: “for all sufficiently large integers N, the (non-trivial) convolution sum bound”. The displayed snippet omits the bound itself.
2. PDF snippet: “Remark 1. The proof of Theorem 1.2 relies on Siegel's theorem on lower bounds for L(1,chi), where chi is a quadratic Dirichlet character.”
3. Abstract snippet refers to a question posed at the **2018 AIM workshop on Sarnak's conjecture**.

Hypotheses, sign choices, parity/domain restrictions, constants, uniformity, proof dependencies, and theorem/page numbering beyond these snippet locators are all **uninspected**.

### Relationship to the obligation

- The title is an exact subject match.
- The “for all sufficiently large” phrase suggests a **pointwise-in-N, asymptotic-range** result, rather than merely an almost-all/density result. This is a provisional classification of the snippet, not an audited theorem classification.
- A pointwise theorem for all sufficiently large N still does not by itself give the requested **every even N > 2** theorem. Exact threshold effectiveness and rigorous finite coverage would have to be resolved.
- A convolution estimate may be useful for the representation-count identity in request.md, lines 76–85. Neither the estimate nor its strength is available here, so no such application is asserted.
- Density, averaged, or log-averaged substitutes do not discharge the target. No such substitute was audited during this search.
- Mathematical admissibility and non-circularity remain for a fresh verifier after exact extraction.

### Required leader `/browse` requests

Perform these in order, without displaying a newer revision's mathematical text:

**B1 — version metadata**

URL: https://arxiv.org/abs/2404.12117v2

Request: inspect only bibliographic/version metadata first. Return title, complete authors, identifier, selected version, exact v2 submission/public-availability timestamp, history needed to verify that version, and any withdrawal/correction metadata relevant to the selected bytes. Confirm the selected version is v2 and was public by 2026-07-31. If the page redirects to an unversioned/latest page, do not read its mathematical body; re-pin or report the redirect. If v2 eligibility is not verifiable, stop before mathematical inspection.

**B2 — eligible primary text beyond abstract**

URL: https://arxiv.org/pdf/2404.12117v2

Prerequisite: B1 confirms eligibility and identity. Download/save immutable bytes and compute a hash if supported by the leader's workflow. Inspect the opening theorem/remark section (initially PDF pages 1–4, expanding within the same source if the relevant text lies elsewhere), not just the abstract. Return:

- definition/domain of lambda and whether Omega counts multiplicity;
- exact Goldbach-type question/conjecture as stated;
- every introductory theorem/corollary bearing on lambda(n)=lambda(N-n)=-1 or the convolution sum;
- especially the complete **Theorem 1.2** and **Remark 1**, with all hypotheses, quantifiers, constants, exceptional sets, and PDF/printed page locators;
- whether the result is unconditional, whether N is arbitrary/even, whether the conclusion is all-N/sufficiently-large/almost-all/averaged/log-averaged, and exactly what it says about threshold effectiveness and computed small cases;
- enough of the proof/dependency discussion to distinguish a direct result from an assumption of the present target;
- the exact bibliography entry/URL for the 2018 AIM workshop question.

Rendered formula/page inspection is needed when PDF extraction obscures notation. Please save the resulting evidence in a leader-authorized source path and return that path rather than promoting it to accepted mathematics.

**B3 — conditional one-hop follow-up**

The allowed hop is reserved for the **2018 AIM workshop question** cited in SP1. First obtain its exact citation from B2. Then inspect one dated eligible original problem document/snapshot, with its exact question number and quantifiers. Do not guess the URL or follow references recursively. If the citation is unavailable, leave this lead unresolved. A fifth search attempting to locate this item returned no results; that is not evidence of absence.

**Optional metadata cross-check, not needed for the mathematical theorem if arXiv v2 suffices:** https://academic.oup.com/imrn/article/2024/16/11865/7704606 . Only publication metadata should be inspected until the exact publisher version's eligibility is established.

## SP2 — UNVERIFIED contextual near miss; not a target theorem

- Indexed title: *The parity problem obstruction for the binary Goldbach problem with bounded error*.
- URL: https://terrytao.wordpress.com/2014/07/09/the-parity-problem-obstruction-for-the-binary-goldbach-problem-with-bounded-error/
- Author/byline: not independently inspected.
- Date: URL encodes 2014-07-09; this does not certify the age of current page text or comments.
- Search snippet discusses Liouville weights and the parity obstruction for prime-pair arguments. Its language includes an expectation of orthogonality, so this is **not** a discovered unconditional representation theorem.
- Potential use: warning against conflating a heuristic correlation estimate with a theorem; no mathematical dependency is taken from it.
- Exact lemma/hypotheses/page locator: none inspected.
- Eligibility: would require a demonstrably eligible dated snapshot or original version before reading as mathematical evidence.
- Priority: low. No citation hop taken; do not divert the B1/B2 budget to this mutable page.

## Other uninspected lead

Search 1 also returned *Linear equations in primes* at https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf . The snippet discusses finite versus infinite complexity and binary problems. Authors, date/version, exact statement and applicability were not verified. This is not an admitted source or a claimed solution; it is preserved only as a lower-priority direction if the main lead does not suffice. No citation hop was taken.

## Cutoff exposure log

Despite `before:2026-08-01`, search 1 included a MathOverflow snippet with the explicit footer `rev 2026.9.15.45626`:

https://mathoverflow.net/questions/427499/does-asymptotic-goldbach-imply-grh

That is an **accidental post-cutoff webpage-revision exposure**. The result and all of its mathematical assertions are excluded. It was not opened, pursued, or used. The earlier-date query did not guarantee a historical page version. Other unversioned results are also unadmitted. No mathematical source body was intentionally opened after the cutoff, and no WebFetch call was made.

## What is and is not delivered

Delivered: bounded discovery, one especially close primary-source/version lead, explicit unknowns, cutoff/exposure tracking, and exact metadata/full-text inspection requests.

Not delivered: audited author/version metadata; exact theorem extraction; primary proof inspection; theorem admissibility/non-circularity; an effective universal representation theorem; a source-certified open-status statement. The source-search scope is five queries documented in `search-trace.md`, not the whole literature.

Next owner: leader `/browse` retrieval for B1/B2, followed by source extraction and fresh mathematical verification. If SP1 is insufficient, a new search allocation should target its bibliography and subsequent **eligible** exact-strength results, especially effective thresholds/universal small-case completion, rather than silently substituting almost-all or averaged claims.

## Sources (discovery only)

- [arXiv abstract record: 2404.12117](https://arxiv.org/abs/2404.12117)
- [Indexed arXiv PDF lead](https://arxiv.org/pdf/2404.12117)
- [Publisher record: On a Goldbach-Type Problem for the Liouville Function](https://academic.oup.com/imrn/article/2024/16/11865/7704606)
- [Parity-problem contextual lead](https://terrytao.wordpress.com/2014/07/09/the-parity-problem-obstruction-for-the-binary-goldbach-problem-with-bounded-error/)
- [Uninspected Linear equations in primes lead](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf)
