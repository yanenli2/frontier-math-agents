# Lean formalization workflow

Use the registered `math-fl-*` roles. This mode requires a supplied source
statement and a configured Lean project. Inspect the actual lean-toolchain,
lakefile, library dependencies, and available commands. Do not infer that Lean
or Mathlib is installed, install a toolchain silently, or substitute an LLM
verdict when the compiler is unavailable. Save a setup blocker if necessary.

## Statement fidelity before proof

The formalizer translates the source definitions and theorem into a scratch
scaffold. Record source locators and interpretation decisions. A scaffold may
temporarily use sorry if it is explicitly tracked as unfinished.

A fresh math-fl-f-reviewer compares the source and encoded statement. Require
approval of the exact declaration, referenced definitions, and hypotheses
before proof work. Snapshot the approved statement and relevant definitions.
No generator, integrator, or golfer may change that snapshot to make a target
easier. A statement repair goes through formalization and fresh review again.

A compiler proves the proposition it sees; it does not establish that the
proposition faithfully expresses the user's mathematics.

## Blind statement readback

Before accepting a declaration or using it as an accepted dependency, invoke a
fresh math-fl-statement-readback **without name or team_name**, with explicit
subagent_type and run_in_background false. Use the role's own prompt, not a
parent-context fork. Do not add shared CLAWCODEX.md or other project instructions
to its packet. This role has no team/task tools; its omission frontmatter is not
a substitute for a clean dispatch and restricted reads.

Give it only:
- Neutral paths to the exact declaration and transitive definitions its type uses.
- A private report output path.

Use code-only review inputs with source-intent comments removed when practical.
Do not include the problem title, brief, intended statement, blueprint, prose
proof, prior verdicts, or author explanations. Do not prepend the ordinary
team dispatch packet or ask it to read the shared protocol. If information
about intent leaks into the packet, make a new clean dispatch.

The output states the literal quantifier order, pointwise/aggregate meaning,
constant restrictions, and vacuity risks. It cannot determine correspondence
to an unseen source. Send its literal account to the separate formal reviewer
for comparison with the original source. A statement or defining dependency
change invalidates both readback and fidelity evidence.

## Proof work and integration

A blueprinter can propose source-aligned helper declarations when a target
needs decomposition. The f-generator proves one approved target in an assigned
scratch area. Choose scratch locations that actually use the configured Lean
project/import environment; record their absolute paths. Preserve the accepted
master while experimenting.

Check the exact candidate using the pinned project toolchain, for example
`lake env lean path/to/Candidate.lean` when that command matches the project.
Retain commands, working directory, exit status, diagnostics, and file hashes.
Use all of these acceptance checks:

1. Relevant Lean compilation/build succeeds.
2. No admitted obligations remain in the accepted target or required helpers.
   Inspect code for sorry/admit and inspect compiler diagnostics; a text search
   alone is not a complete proof-status check.
3. Inspect `#print axioms <declaration>` for the target and dependencies. Record
   the transitive axiom set and compare it with the explicitly accepted base;
   never accept sorryAx or newly introduced unsupported axioms. Conditional
   theorems using external assumptions must say exactly which assumptions.
4. Compare the statement and defining dependencies with the approved snapshots.
5. Source-fidelity review and blind readback cover this exact version.

Only math-fl-integrator may merge the checked candidate into the assigned
master development. It resolves imports/namespaces mechanically and reruns the
relevant build and checks on the integrated result. Any mathematical repair
returns to the responsible specialist. A passing scratch file is not enough.

A golfer may propose a separate cleanup of an accepted proof. Keep the baseline
unless all checks pass on the replacement. The regulator audits the final wave
for stale evidence, statement drift, vacuity, unproved dependencies, and
integration omissions.

## Completion

Report the original source target, final Lean declaration and files, toolchain,
successful commands, admitted-obligation/axiom results, exact fidelity/readback
reports, and remaining assumptions. Do not claim a proof for a compiling
scaffold, a weakened target, or a file whose checker was never run. Preserve
failed attempts, blockers, and the next owner for later continuation.
