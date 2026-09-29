# Original user request

/math-team formal Develop a rigorous, unconditional proof of the following conjecture, using both natural-language reasoning agents and Lean formalization agents. Success requires a faithful, fully checked Lean theorem.

TARGET

Define λ(n) = (-1)^Ω(n), where Ω(n) counts prime factors with multiplicity and Ω(1) = 0.

Prove:
For every even integer N > 2, there exist positive integers a,b such that
    N = a + b,
    λ(a) = λ(b) = -1.

Allow a = b. Preserve the exact quantifiers and hypotheses. Do not add primality, oddness, coprimality, or other restrictions.

SOURCE CUTOFF — JULY 31, 2026, INCLUSIVE

Every agent must use only external source versions demonstrably publicly available on or before this date.

- Exclude later publications, revisions, solutions, and unverifiably dated material.
- Select eligible arXiv versions and dated snapshots of changing webpages. An older initial publication date does not authorize a newer revision.
- Use search date filters, then verify source dates. Search snippets are not mathematical evidence.
- Apply the restriction to cached material, downloaded documents, imported proofs, and mathematical library code.
- Pin Mathlib and mathematical dependencies to eligible versions with a compatible Lean toolchain. Do not silently fetch their current main branches.
- Record titles, authors, URLs, versions, availability dates, and theorem/page references in sources.md.
- Support remembered external theorems with eligible sources or prove them within this project.
- Ignore later material encountered accidentally and disclose any contamination.

New mathematical deductions developed during this run must be justified and reviewed.

ORCHESTRATION

Use the installed math-team skill, including both its natural-language and Lean workflows. The main session is team-lead.

Launch specialists as needed. Respect configured limits, keep at most two persistent workers by default, and preserve capacity for fresh reviewers. Give each worker explicit inputs, output ownership, and acceptance conditions.

Maintain a shared map connecting each informal lemma to its Lean declaration, proof status, dependencies, source provenance, and review evidence.

1. VERIFY THE LEAN ENVIRONMENT

Inspect the available Lean tools, lean-toolchain, Lake configuration, and dependency versions. Verify that the selected project actually compiles.

Use configured Lean diagnostics and goal-inspection tools when available to the assigned agent. Otherwise, invoke Lean/Lake through Bash. Record actual commands and results.

If the environment is unavailable, record the exact setup blocker and continue feasible informal work. Formal verification remains a required unfinished obligation.

2. FORMALIZE AND REVIEW THE STATEMENT FIRST

Assign math-fl-formalizer to encode the Liouville function and exact target.

Audit:
- Prime factors are counted with multiplicity.
- λ(1) = 1.
- The codomain represents -1 correctly, for example ℤ.
- a and b are explicitly positive.
- The theorem covers every even N > 2.
- Definitions and hypotheses do not introduce vacuity.

Run a fresh math-fl-statement-readback with only isolated declaration signatures and the transitive definitions used by their types. Do not send this overall prompt, the intended theorem, proof bodies, source-intent comments, plans, or previous verdicts to that agent.

Have a fresh math-fl-f-reviewer compare the literal readback and Lean statement against the original mathematical target.

After approval, snapshot the statement and definitions. Any semantic change requires new readback and fidelity review.

3. DEVELOP INFORMAL AND FORMAL ARGUMENTS TOGETHER

Use:
- math-nl-sketcher and math-fl-blueprinter for matching informal and formal dependency plans.
- math-nl-searcher for eligible literature and exact theorem statements.
- math-nl-explorer and math-nl-generator for new approaches and detailed arguments.
- math-nl-ce-hunter and math-nl-code-executor for bounded experiments and attempts to falsify proposed lemmas.
- math-fl-f-generator for proving approved lemmas in Lean.

Formalize useful intermediate results early. Feed formalization failures back to the responsible mathematical specialist. Distinguish missing library infrastructure from actual mathematical gaps.

As one possible route, derive and verify:

    4R(N) = (N-1) - 2L(N-1) + C(N),

where
    R(N) counts ordered positive pairs a+b=N with λ(a)=λ(b)=-1,
    L(x) = Σ_{1≤n≤x} λ(n),
    C(N) = Σ_{a=1}^{N-1} λ(a)λ(N-a).

Formalize the identity with explicit casts and signed arithmetic. Avoid unintended natural-number subtraction or division. The goal is R(N)>0 for every admissible N.

Explore other approaches when useful.

4. VERIFY EVERY ACCEPTED RESULT

math-fl-f-generator must compile candidates using the pinned environment after meaningful changes.

For each accepted theorem:
- Check its exact statement against the approved snapshot.
- Compile the actual file containing it.
- Eliminate all sorry/admit placeholders from its proof and dependencies.
- Run #print axioms on the declaration and inspect its transitive assumptions.
- Reject sorryAx, unsupported custom axioms, circular dependencies, and assumptions that encode the desired conclusion.
- Record standard foundational axioms and any additional trusted mechanisms explicitly.
- Preserve file hashes, commands, exit statuses, and diagnostics.

Draft scaffolds may contain clearly recorded unfinished obligations; they never count as established results.

Use fresh math-nl-verifier reviews to audit the mathematics and exposition. Obtain two separate fresh reviews of the final argument.

NL verifiers, formal reviewers, and blind readers run as fresh synchronous Agent calls with explicit subagent_type, run_in_background=false, and no name or team_name. Do not reuse reviewer conversations.

5. INTEGRATE AND RECHECK

Only math-fl-integrator merges accepted candidates into the designated master development.

Rebuild the integrated project and explicitly compile the final theorem module. Confirm that the build includes that module. Repeat statement, admitted-obligation, dependency, and axiom checks.

Use math-fl-regulator to audit the final evidence for statement drift, vacuity, missing cases, and stale reviews. Use math-fl-golfer only after acceptance, preserving the verified baseline.

SUCCESS CONDITIONS

Declare success only when:
- The Lean statement faithfully expresses the original conjecture.
- The complete proof and all required dependencies pass the actual Lean checks.
- No mathematical obligation or prohibited assumption remains.
- Source provenance satisfies the cutoff.
- Final reviews cover the exact integrated version.

An averaged result, an almost-all result, or a conditional theorem leaves the original target unresolved. A sufficiently-large-N argument requires an effective threshold and rigorous coverage of every remaining case.

Computational experiments and successful compilation of an unfinished scaffold do not establish the conjecture.

PERSISTENCE AND REPORTING

Save work under:
.clawcodex/math-team/problems/liouville-goldbach-jul2026/

Maintain request.md, RUN.md, STATUS.md, HANDOFF.md, sources.md, informal attempts, Lean files, statement snapshots, review reports, and build/axiom logs.

Provide REPRODUCE.md with the exact toolchain, dependency revisions, final theorem name, and commands needed to check the result.

Work autonomously within configured resource limits. Replan after failed approaches.

If the proof remains incomplete, report verified partial results, exact unresolved Lean goals, mathematical gaps, rejected approaches, and concrete next steps. Never manufacture a proof or silently weaken the target.
