# Role catalog and source mapping

The 26 definitions below are adapted from the user's
`~/workspace/MechMath-agent-team` checkout: each component's
`.codex/agents/*.toml`, matching `prompts/*.md`, and orchestration rules.
The source checkout is provenance, not a runtime dependency.

Use the full `math-*` value as `Agent.subagent_type`. For a persistent member,
choose a short unique name such as `nl-generator`; type and teammate name are
different fields. Use a new unique name when several instances of a role are
needed. All definitions inherit the session's model.

Only the main session is team-lead. This adaptation has no extra supervisor
agent: routing stays in the skill and mathematical content stays with specialists.

## Natural-language proof solving

| Definition | Purpose | Lifetime | Original prompt |
|---|---|---|---|
| [math-nl-auditor](../../../agents/math-nl-auditor.md) | Resolve ambiguous mathematical notation, definitions, named families, and boundary conventions before proof or counterexample work. | Named teammate as needed | `nl-prover/prompts/auditor.md` |
| [math-nl-ce-hunter](../../../agents/math-nl-ce-hunter.md) | Search for counterexamples, degenerate cases, and scoped obstructions to a mathematical statement or proof route. | Named teammate as needed | `nl-prover/prompts/ce-hunter.md` |
| [math-nl-code-executor](../../../agents/math-nl-code-executor.md) | Run bounded mathematical experiments or audit exact finite computations, exhaustive enumeration, and computational certificates. | Named teammate as needed | `nl-prover/prompts/code_executor.md` |
| [math-nl-explorer](../../../agents/math-nl-explorer.md) | Propose diverse conjectural proof routes, constructions, and inexpensive experiments for a difficult mathematical problem. | Named teammate as needed | `nl-prover/prompts/explorer.md` |
| [math-nl-generator](../../../agents/math-nl-generator.md) | Construct or repair a detailed natural-language proof of one assigned lemma or the final assembly, preserving the original hypotheses. | Named teammate as needed | `nl-prover/prompts/generator.md` |
| [math-nl-kb-manager](../../../agents/math-nl-kb-manager.md) | Answer a focused proof-solving query from an existing local mathematical wiki without modifying the knowledge base. | Named teammate as needed | `nl-prover/prompts/kb-manager.md` |
| [math-nl-refiner](../../../agents/math-nl-refiner.md) | Simplify an existing mathematical proof plan or an already accepted proof while retaining the accepted version as fallback. | Named teammate as needed | `nl-prover/prompts/refiner.md` |
| [math-nl-regulator](../../../agents/math-nl-regulator.md) | Diagnose failed or stalled proof attempts and recommend the smallest concrete next task, owner, and alternate routes. | Named teammate as needed | `nl-prover/prompts/regulator.md` |
| [math-nl-searcher](../../../agents/math-nl-searcher.md) | Find mathematical source theorems and literature, preserving exact statements, locators, preconditions, and honest provenance. | Named teammate as needed | `nl-prover/prompts/searcher.md` |
| [math-nl-sketcher](../../../agents/math-nl-sketcher.md) | Turn an exact mathematical problem into a target contract, dependency-ordered lemma plan, and explicit proof obligations. | Named teammate as needed | `nl-prover/prompts/sketcher.md` |
| [math-nl-synthesizer](../../../agents/math-nl-synthesizer.md) | Compare candidate mathematical approaches and produce a ranked branch queue based on feasibility and contribution to the target. | Named teammate as needed | `nl-prover/prompts/synthesizer.md` |
| [math-nl-verifier](../../../agents/math-nl-verifier.md) | Independently check a mathematical proof, plan, refinement, or counterexample from a fresh context and an exact artifact snapshot. | Fresh one-shot review | `nl-prover/prompts/verifier.md` |
| [math-nl-writer](../../../agents/math-nl-writer.md) | Write mathematical exposition or progress notes from verified or explicitly qualified artifacts without inventing or repairing mathematics. | Named teammate as needed | `nl-prover/prompts/writer.md` |

## Lean formalization

| Definition | Purpose | Lifetime | Original prompt |
|---|---|---|---|
| [math-fl-blueprinter](../../../agents/math-fl-blueprinter.md) | Decompose a difficult Lean formalization target into source-aligned helper declarations and a dependency-ordered proof plan. | Named teammate as needed | `fl-prover/prompts/blueprinter.md` |
| [math-fl-f-generator](../../../agents/math-fl-f-generator.md) | Prove one approved Lean theorem or helper in an assigned scratch area without changing its protected statement. | Named teammate as needed | `fl-prover/prompts/f_generator.md` |
| [math-fl-f-reviewer](../../../agents/math-fl-f-reviewer.md) | Independently review whether a Lean declaration faithfully expresses its source theorem before proof search or after a statement change. | Fresh one-shot review | `fl-prover/prompts/f_reviewer.md` |
| [math-fl-formalizer](../../../agents/math-fl-formalizer.md) | Translate a mathematical source statement into a faithful Lean declaration scaffold for independent statement review. | Named teammate as needed | `fl-prover/prompts/formalizer.md` |
| [math-fl-golfer](../../../agents/math-fl-golfer.md) | Conservatively simplify an already verified Lean proof while preserving its statement, accepted axioms, and proof behavior. | Named teammate as needed | `fl-prover/prompts/golfer.md` |
| [math-fl-integrator](../../../agents/math-fl-integrator.md) | Merge independently reviewed and compiler-checked Lean artifacts into the designated master development, then recheck the integrated result. | Named teammate as needed | `fl-prover/prompts/integrator.md` |
| [math-fl-regulator](../../../agents/math-fl-regulator.md) | Audit a Lean proof wave for statement drift, vacuity, missing premises, integration gaps, and the next actionable owner. | Named teammate as needed | `fl-prover/prompts/regulator.md` |
| [math-fl-statement-readback](../../../agents/math-fl-statement-readback.md) | Read a Lean declaration literally in a fresh context without its intended theorem, detecting quantifier, bound, constant, and vacuity surprises. | Fresh one-shot review | `fl-prover/prompts/statement_readback.md` |

## Knowledge-base work

| Definition | Purpose | Lifetime | Original prompt |
|---|---|---|---|
| [math-kb-archivist](../../../agents/math-kb-archivist.md) | Organize Lean proof artifacts into a persistent mathematical archive with declaration maps, provenance, and accurate proof-status cards. | Named teammate as needed | `kb-manager/prompts/archivist.md` |
| [math-kb-ingester](../../../agents/math-kb-ingester.md) | Distill registered mathematical sources or research artifacts into linked wiki pages while preserving provenance and verification status. | Named teammate as needed | `kb-manager/prompts/ingester.md` |
| [math-kb-maintainer](../../../agents/math-kb-maintainer.md) | Inspect and repair a mathematical wiki's links, indexes, metadata, duplication, and evidence relationships within an authorized scope. | Named teammate as needed | `kb-manager/prompts/maintainer.md` |
| [math-kb-registrar](../../../agents/math-kb-registrar.md) | Register supplied mathematical references as immutable hash-addressed sources and maintain their manifest or manual-download queue. | Named teammate as needed | `kb-manager/prompts/registrar.md` |
| [math-kb-researcher](../../../agents/math-kb-researcher.md) | Answer mathematical research questions from a local compiled wiki with exact page citations, inferences, gaps, and optional authorized notes. | Named teammate as needed | `kb-manager/prompts/researcher.md` |

## Adaptation decisions

- ClawCodex native TeamCreate, Agent, SendMessage, and task tools replace the
  source harness's dispatch wrappers. Durable files remain the mathematical
  evidence; messages carry handoffs through team-lead.
- Original specialist separation, exact-statement discipline, fresh NL review,
  formal fidelity/readback, Lean compiler/axiom checks, and immutable source
  provenance are retained.
- The source project's separate Python facades, platform-specific hooks,
  external model services, and hundreds of skill references are not copied or
  assumed installed. Their relevant contracts are represented in the local
  [protocol](protocol.md) and mode-specific workflows.
- Fresh reviewers use explicit custom definitions and synchronous one-shot calls
  without teammate names. They do not reuse persistent worker conversations.
  Blind Lean readback receives code-only inputs with no shared project
  instructions in its dispatch; its source-fidelity comparison belongs to a
  different reviewer.
- Persistent roles are launched on demand within current ClawCodex admission
  limits. The MechMath six-worker setting and model-specific preferences are
  not copied into global settings.
- The current session owns its live team. Definitions and problem artifacts
  survive shutdown; restarting from artifacts creates fresh workers and tasks.
- The definitions are project-local. The surrounding repository currently
  ignores `.clawcodex/` in Git, so these files persist on this machine without
  automatically becoming a repository commit.
