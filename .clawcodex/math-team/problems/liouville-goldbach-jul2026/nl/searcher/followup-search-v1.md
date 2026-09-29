Mode: DISCOVERY — conjectural; no proof weight.

# Bounded follow-up search v1

## Result and limits

Completed exactly three WebSearch calls, each with `after:2024-05-01 before:2026-08-01`. No WebFetch, remote page opening, task-board operation, or nested agent was used. No new relevant follow-up or eligible-version candidate was identified. There were 23 returned URLs: 10 from Q1, none from Q2, and 13 from Q3. All are recorded below.

**This is not evidence that the target remained open through the cutoff.** Q1 and Q3 produced overwhelmingly off-topic results, and Q1 even returned non-arXiv domains despite its `site:` term. The returned material therefore supports only a report about these particular tool responses, not a reliable survey of the literature. No search snippet was used mathematically.

## Inputs and local primary-source anchor

Read the assigned protocol, `request.md`, the local `sources.md` ledger, and PDF pages 1–4 of `knowledge/mangerel-v2/paper.pdf`. No separate wiki index was supplied. Work is confined to this report; no shared ledger, knowledge file, or external wiki was changed.

Exact target: every even integer N > 2 has positive integers a,b with N=a+b and λ(a)=λ(b)=−1, where λ(n)=(−1)^Ω(n), including λ(1)=1; a=b is allowed.

**Supplied eligible source; extraction unverified by an independent reviewer:** Alexander P. Mangerel, *On a Goldbach-type problem for the Liouville function*, arXiv:2404.12117v2, 2024-05-02. The local ledger records the v2 timestamp as 2024-05-02 14:48:54 UTC; this pass did not independently recheck the remote metadata.

- Versioned record: <https://arxiv.org/abs/2404.12117v2>
- Versioned PDF: <https://arxiv.org/pdf/2404.12117v2>
- Inspected local file: `knowledge/mangerel-v2/paper.pdf`, PDF/printed pp. 1–4.
- Theorem 1.2, p. 1: with ℒλ(N)=Σ_{1≤n<N} λ(n)λ(N−n), there exists N₀∈ℕ such that N≥N₀ implies |ℒλ(N)|<N−1.
- Remark 1, p. 2: the proof uses Siegel's theorem, and N₀ is ineffective. The remark points to Remark 3 for effective information, up to a possible unique exception, when N is prime. Remark 3 was not inspected in this pass.
- Remark 2, p. 3: explicitly asks whether every even N≥4 has 1≤a,b≤N with a+b=N and λ(a)=λ(b)=−1. This is the original target, not an established theorem in that remark. The remark discusses stronger convolution savings and states an intention to return to the problem in a future paper.
- Relationship to this search: the explicit future-paper statement motivated searching for subsequent work, without assuming whether that work exists. Theorem 1.2 alone is not the all-even negative-negative representation theorem, and its stated threshold is not effective. Its exact admissibility and any new bridge remain for a fresh verifier.

Additional discovery families: uniform (+,+) representations of 2p for prime p, with the precise prime range and exceptions to be inspected in any actual source; explicit/effective quantitative thresholds. No equivalence between such an auxiliary statement and the original target is asserted here.

## Search trace and exact returned URLs

Titles below are discovery metadata only, transcribed from the returned results (some were truncated by the tool). No title, URL date component, arXiv identifier, or search date filter verifies a source version's availability date.

### Q1 — broad primary-source follow-up search

Exact query:

```text
site:arxiv.org Liouville Goldbach after:2024-05-01 before:2026-08-01
```

No separate domain-filter parameter. Returned results:

1. “Liouville quantum gravity: from random planar maps to conformal ...” — <https://arxiv.org/abs/2510.16431>
2. “Not the Liouville's we wished for but the Liouville's we deserved.” — <https://www.reddit.com/r/mathmemes/comments/1pww54e/not_the_liouvilles_we_wished_for_but_the>
3. “[2510.19770] $\mathcal{N}=1$ super complex Liouville string - arXiv” — <https://arxiv.org/abs/2510.19770>
4. “[2409.18759] The complex Liouville string: the worldsheet - arXiv” — <https://arxiv.org/abs/2409.18759>
5. “Timelike Liouville theory and AdS$_3$ gravity at finite cutoff - arXiv” — <https://arxiv.org/abs/2508.03236>
6. “Trying to understand Liouville's theorem [closed]” — <https://math.stackexchange.com/questions/4981992/trying-to-understand-liouvilles-theorem>
7. “[2604.25463] Liouville Blocks from Spectral Networks - arXiv” — <https://arxiv.org/abs/2604.25463>
8. “Pedro Schmied – Deforming the Double Liouville String - YouTube” — <https://www.youtube.com/watch?v=YQuPJLkFftg>
9. “[2412.18411] Deforming the Double Liouville String - arXiv” — <https://arxiv.org/abs/2412.18411>
10. “Sturm–Liouville Operators, Their Spectral Theory, and Some ...” — <https://bookstore.ams.org/COLL/67>

Assessment: no target-specific lead apparent from returned titles. Quantum/string, analytic-function, and spectral-theory homonyms dominated. The six arXiv URLs are unversioned and are not eligible-version identifications. None merits full inspection for this obligation on the returned evidence.

### Q2 — arithmetic disambiguation and named-author follow-up

Exact query:

```text
"Liouville function" "Goldbach" "Mangerel" after:2024-05-01 before:2026-08-01
```

Tool parameter: `allowed_domains: ["arxiv.org"]`.

Response: “No results found.” No URLs returned.

Assessment: this more constrained query did not even return the supplied relevant v2. The reason is unknown; publication-date indexing or matching limitations are possible, not established. An empty response cannot establish absence of later work.

### Q3 — sign/prime-indexed and effective-threshold families

Exact query:

```text
"Liouville" "Goldbach" ("2p" OR "twice a prime" OR "positive" OR "effective" OR "explicit threshold") after:2024-05-01 before:2026-08-01
```

No separate domain filter, allowing non-arXiv follow-up leads. Returned results:

1. “Mathematics | Igor Pak's blog” — <https://igorpak.wordpress.com/category/mathematics>
2. “PRIME - ArchWiki” — <https://wiki.archlinux.org/title/PRIME>
3. “4 Ways to Strengthen Positive Thinking | Psychology Today” — <https://www.psychologytoday.com/us/blog/common-wisdom-insights/202509/4-ways-to-strengthen-positive-thinking>
4. “Karl Weierstrass (1815 - 1897) was a German mathematician who ...” — <https://www.facebook.com/probal.chakraborty.121/posts/karl-weierstrass-1815-1897-was-a-german-mathematician-who-specialized-in-analysi/1925778014820124>
5. “M.D. Artykbayev's work on Riemann Hypothesis and Dynamic ...” — <https://www.facebook.com/groups/1056119238855297/posts/1767526574381223>
6. “Home - EFFECTIVE” — <https://effective-euproject.eu>
7. “GSBA 582 - PRIME | USC Marshall” — <https://students.marshall.usc.edu/current-students/marshall-global-programs-and-partnerships/gsba-582-prime>
8. “Prime membership not showing in Google play - Google Play Community” — <https://support.google.com/googleplay/thread/322541268/prime-membership-not-showing-in-google-play?hl=en>
9. “Quartus Prime Standard Edition Design Software Version 25.1 for Windows | Altera” — <https://www.altera.com/downloads/fpga-development-tools/quartus-prime-standard-edition-design-software-version-25-1-windows>
10. “Instagram” — <https://www.instagram.com/p/DY6hCpdGoxr?hl=en>
11. “The Prime Rib Rules Every Home Cook Should Know - YouTube” — <https://www.youtube.com/watch?v=XufciNPDsv8>
12. “Metroid Prime - Samus Varia Suit | LEGO® Ideas” — <https://ideas.lego.com/product-ideas/e4860eea-dd0f-42c8-a1d2-18a03476ab95>
13. “De-Escalation of Nodal Surgery in Clinically Node-Positive Breast ...” — <https://pubmed.ncbi.nlm.nih.gov/39745737>

Assessment: no identifiable target-specific primary source. General Goldbach commentary and unrelated matches for “prime,” “positive,” or “effective” do not identify a result about the requested Liouville sign representations. No mathematical claim from these snippets was retained.

## Eligibility, contamination, and inspection queue

- **New eligible-version leads:** none established.
- **New source worthy of full primary inspection:** none identified by this bounded search.
- **UNVERIFIED candidate inbox:** empty; there is no new reusable theorem candidate to preserve. The supplied version-specific anchor above remains available for source review, not promotion as a solution.
- No explicit publication/revision date after 2026-07-31 was displayed in these returned results. This does not verify their eligibility: all new unversioned/live URLs and all their mathematical assertions are excluded from proof use. None was opened or downloaded.
- The local ledger already records prior accidental exposure to a MathOverflow footer `rev 2026.9.15.45626` at <https://mathoverflow.net/questions/427499/does-asymptotic-goldbach-imply-grh>. That prior later-revision exposure is explicitly excluded here; this pass did not revisit its page or use its content.
- The already supplied Mangerel v2, not any current unversioned revision, was the only external mathematical body inspected in this pass.

## Unsearched scope and concrete next direction

Budget exhausted at three queries. No citation-index traversal, author bibliography inspection, arXiv version-history inspection, journal issue search, dated MathOverflow snapshot inspection, alternate search service, or remote full-primary-source inspection was performed. The broad OR query does not exhaust alternative formulations such as even Ω, sign-pattern representation counts, binary additive convolutions, or uniformity over primes. No citation hops were followed.

If the leader authorizes a further pass, use `/browse` to inspect version histories of actual citing papers or the author's bibliography starting from arXiv:2404.12117v2, pinning every candidate to a publicly available version on or before 2026-07-31. For the effective-bound branch, complete local primary inspection of the v2 Remark 3 and its cited source, while checking whether any exceptional prime, ineffectivity, sign mismatch, or missing finite range prevents the exact target. Neither direction is a claim that a solution exists or does not exist.

## Sources

- [Supplied Mangerel v2 record](https://arxiv.org/abs/2404.12117v2)
- [Supplied Mangerel v2 PDF](https://arxiv.org/pdf/2404.12117v2)
- All returned search URLs are preserved above as excluded/unverified discovery metadata, not mathematical evidence.
