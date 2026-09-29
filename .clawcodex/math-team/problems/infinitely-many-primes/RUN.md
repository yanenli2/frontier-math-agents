# RUN — infinitely-many-primes

- **Problem ID:** `infinitely-many-primes`
- **Team name:** `math-team`
- **Mode:** natural-language (NL) proof workflow
- **Project root:** `.`
- **Problem dir:** `.clawcodex/math-team/problems/infinitely-many-primes`
- **Protocol:** `.clawcodex/skills/math-team/references/protocol.md`
- **NL workflow:** `.clawcodex/skills/math-team/references/natural-language.md`
- **Roles catalog:** `.clawcodex/skills/math-team/references/roles.md`

## Budget / resource limits

- No token or wall-clock budget was set by the user. Default skill guidance applies:
  at most two long-lived team members, fresh one-shot verifiers, no model-driven polling loop.
- Roles selected for this target (deliberately minimal — elementary proof):
  `math-nl-sketcher` (target contract + lemma plan), `math-nl-generator` (proof),
  fresh `math-nl-verifier` (independent acceptance). No explorer/synthesizer/searcher:
  the route is a standard elementary one and role sprawl is explicitly discouraged
  for a short elementary proof.

## Toolchain

- No external toolchain required. Optional mechanical check available: a bounded
  primality/enumeration script via `Bash` + `python3` if a worker wants a sanity check.
  Toolchain success is never mathematical acceptance.

## Pre-flight note (non-mathematical blocker, resolved)

`TeamCreate` initially failed: `.clawcodex/team.json` held a dead roster named
`team-demo` (README-summary demo team, mtime 2026-09-23 23:42). `TeamRuntime.__init__`
(`src/services/swarm/team_runtime.py:105-113`) reserves that path with an atomic
`open("x")` and has no liveness check, so the stale file blocked creation.

Evidence it was dead: `lsof` showed no process holding `team.json`, the team-demo
task board, or its mailboxes; the only live ClawCodex CLI session was this one
(started 01:10); `TaskList` showed no live board; both demo tasks were already
`completed`.

Per the skill's rule against deleting a roster merely to make startup pass, the user
was asked explicitly and authorized removal. Backup preserved at
`/tmp/team-demo-roster-backup-20260924.json`. Only `team.json` was removed; the
demo's mailbox and task-board files were left untouched.
