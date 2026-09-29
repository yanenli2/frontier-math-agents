Mode: DISCOVERY — conjectural; no proof weight.

# Compact source-search trace

Run date from local RUN.md: 2026-09-24. Source cutoff: 2026-07-31 inclusive.

Budget used: **5 / 5 WebSearch calls**. Each query included `before:2026-08-01`. Full-page retrieval: **0** (no WebFetch). Completed citation hops: **0**; one hop reserved for the AIM workshop question after primary inspection. No mathematical source admitted. Search snippets have no proof weight.

## Local setup

Read:

- `.clawcodex/skills/math-team/references/protocol.md`
- `.clawcodex/skills/math-team/references/knowledge.md`
- `P/request.md`
- `P/RUN.md`
- `P/sources.md`

Globs: problem-root files and `**/*index*` under `.clawcodex`. The latter returned no matching files. No local mathematical reference/wiki index was supplied. No other mathematical literature was assumed from memory.

An initial `SendMessage` asked the leader for missing local indexes and announced the browsing handoff; it failed with `Only active team members can send team messages`. No task-board changes were made. Durable browsing requests are in the companion package.

## Queries and outcomes

### 1. Exact named problem family

Query:

`"Liouville" "Goldbach" "even" before:2026-08-01`

Promising results:

- Publisher *On a Goldbach-Type Problem for the Liouville Function*: https://academic.oup.com/imrn/article/2024/16/11865/7704606
- PDF title `arXiv:2404.12117v2 [math.NT] 2 May 2024`: https://arxiv.org/pdf/2404.12117
- Contextual parity-obstruction blog: https://terrytao.wordpress.com/2014/07/09/the-parity-problem-obstruction-for-the-binary-goldbach-problem-with-bounded-error
- Lower-priority uninspected *Linear equations in primes*: https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf

Other results were unrelated/low-priority or lacked eligible version evidence and were not pursued. No theorem was extracted.

**Cutoff contamination:** a MathOverflow result at https://mathoverflow.net/questions/427499/does-asymptotic-goldbach-imply-grh displayed `rev 2026.9.15.45626` despite the date filter. Entire result excluded; not opened or used. The footer proves the displayed page revision is later than the cutoff, not that its underlying older mathematical assertions are individually later. We do not rely on any of them.

### 2. Exact primary title

Query:

`"On a Goldbach-type problem for the Liouville function" before:2026-08-01`

Domain filter: `arxiv.org`, `academic.oup.com`.

Result: https://arxiv.org/abs/2404.12117 . Snippet mentions “sufficiently large integers” and a question at the 2018 AIM workshop. This identified the exact arXiv record; no metadata/body was fetched.

### 3. Theorem/strength discovery within the identified paper

Query:

`"2404.12117" "Theorem" before:2026-08-01`

Results:

- https://arxiv.org/pdf/2404.12117 : snippet names **Remark 1**, **Theorem 1.2**, and reliance on Siegel's lower bound for L(1,chi) for quadratic Dirichlet characters.
- https://arxiv.org/abs/2404.12117 : snippet says “for all sufficiently large integers N, the (non-trivial) convolution sum bound”. The bound itself is absent.

Interpretation limited to retrieval planning: prioritize exact theorem and effectiveness discussion. Neither the bound nor effectiveness has been established. Do not convert this into a claim that the universal target is proved, disproved, or open.

### 4. Version-specific discovery

Query:

`"2404.12117v2" before:2026-08-01`

Results: same unversioned arXiv PDF and abstract URLs. The PDF's indexed title again states v2, 2 May 2024. Abstract snippet refers to “version, v2”.

Outcome: standard pinned forms `https://arxiv.org/abs/2404.12117v2` and `https://arxiv.org/pdf/2404.12117v2` are the requested inspection URLs. Their existence, actual version-selection behavior, and version availability date were **not directly verified**. No date claim is admitted solely from the search title.

### 5. Synonym family / original question lead

Query:

`"Goldbach" ("Liouville" OR "odd number of prime factors") "Sarnak" before:2026-08-01`

Outcome: no results returned. This only records a failed narrowly phrased query. It does not establish absence of the workshop problem or relevant literature. The precise workshop citation should be recovered from the eligible primary paper instead of guessing a URL.

## Scope limits and handoff

- Searched exact title/problem, parity-of-Omega synonym, theorem locator, and version notation families.
- Did not perform a comprehensive later-citing-paper search, MathSciNet/Zentralblatt audit, effective-threshold search, or source-body bibliography inspection.
- Did not inspect any primary theorem beyond its abstract/snippet; leader `/browse` access is the next dependency.
- Core full-text request: verify metadata at https://arxiv.org/abs/2404.12117v2, then inspect https://arxiv.org/pdf/2404.12117v2, especially introductory theorem statements, **Theorem 1.2**, **Remark 1**, hypotheses, exact convolution bound, effectiveness, and original AIM citation. Full B1/B2/B3 instructions are in `source-package-v1.md`.
- All promising leads remain **UNVERIFIED**, stored only in the assigned problem-local searcher directory. No external wiki or shared index promotion occurred.
- Artifact production is complete; exact source/theorem extraction and mathematical acceptance remain incomplete. No task board was touched, per assignment.

## Sources (discovery only)

- [arXiv abstract record](https://arxiv.org/abs/2404.12117)
- [Indexed arXiv PDF](https://arxiv.org/pdf/2404.12117)
- [Publisher record](https://academic.oup.com/imrn/article/2024/16/11865/7704606)
- [Parity-obstruction contextual lead](https://terrytao.wordpress.com/2014/07/09/the-parity-problem-obstruction-for-the-binary-goldbach-problem-with-bounded-error/)
- [Uninspected Linear equations in primes lead](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf)
