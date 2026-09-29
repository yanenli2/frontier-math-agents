# Natural-language proof workflow

Use the registered `math-nl-*` roles from [roles.md](roles.md). The leader chooses
the next specialist by the actual blocker; a short elementary proof does not
need every role or a long fixed pipeline.

## Start with an exact target

Copy the user's input to request.md. Have the sketcher record the target
contract: definitions, quantifiers, domains, hypotheses, conclusion directions,
accepted conventions, and any material ambiguity. Route unresolved terminology
to the auditor. If a relevant local wiki exists, obtain a focused query from
math-nl-kb-manager; do not make an absent KB a prerequisite for solving.

For a nontrivial target, obtain a lemma graph with exact statements, dependency
preconditions, an independent frontier, a keystone blocker, and an assembly
route. Sketches and plans remain proposals until reviewed. Generators may
attempt assembly against stated lemmas while their proofs are pending, but
label it conditional; final acceptance requires every used obligation closed.

## Search and prove

Use an explorer when genuine route diversity helps, then a synthesizer when
several routes need comparison. Rank by feasibility and contribution to the
original target. Give exploratory roles explicit DISCOVERY mode.

Use the smallest owner for missing information:
- Definitions/conventions: auditor.
- External theorem or literature: searcher.
- Existing local wiki: kb-manager.
- Finite computation or experiment: code-executor.
- Candidate counterexample: ce-hunter.
- Proof or assembly: generator.
- Failure diagnosis and next-owner recommendation: regulator.

Each generator owns one exact target and writes a versioned attempt plus its
obligations and dependencies. Dispatch independent targets within available
capacity. Do not mark an unproved statement as proved because the diagram
closes or the generator declares success.

## Independent acceptance

For each mathematical acceptance, call a fresh math-nl-verifier with explicit
subagent_type, no name/team_name, and run_in_background false. Supply the exact
statement, artifact, dependency/source evidence, output path, and CERTIFICATION
mode. Do not include author confidence or prior verifier conclusions. Check
that the report refers to the current artifact snapshot.

For a plan, PASS covers the stated decomposition and assembly implication, not
the as-yet unwritten lemma proofs. For a proof, PASS must cover all required
hypotheses, sources, dependencies, cases, and load-bearing obligations.
For a counterexample, require all original assumptions and the precise failure
of the original conclusion.

If the review reports a gap, route that gap to its owner. The leader must not
rewrite the mathematics. One failed attempt is not exhaustion. Track scoped
failures and keep viable branches open. If the user set a resource budget,
stop at it and preserve the exact remaining obligation.

## Refine and present

Keep the accepted proof as the baseline. A refiner may propose a simpler plan
or cleaner proof when useful; each mathematical change requires a fresh review
before replacing the baseline. Do not impose an unrelated optimization task
when the user asks for a small or time-limited result.

Use the writer for a substantial final exposition or requested article. Let
the leader mechanically publish an accepted artifact as proof.tex. Writing
which changes mathematical content needs review. Compile LaTeX/PDF only with
available tooling; typesetting success is not mathematical verification.

For an incomplete stop, preserve:
- The original target and the precise current blocker.
- Established results with their proofs and exact review paths.
- Attempts and the scope of each failure.
- Open routes, necessary sources, next owner, and acceptance condition.
- A concise human-readable summary and reusable lessons.

A final result must clearly say whether it is an independently reviewed proof,
a checked counterexample, a partial result, or unresolved. Do not present an
LLM-reviewed natural-language proof as a Lean-certified theorem.
