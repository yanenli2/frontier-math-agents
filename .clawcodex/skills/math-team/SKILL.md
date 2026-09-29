---
name: math-team
description: Create and coordinate a named mathematical problem-solving team with MechMath-inspired proof, independent review, Lean formalization, and knowledge-base specialists. Use for collaborative math solving, formal proof work, or managing this math team.
---

# Math team

Act as the main session's `team-lead`. Use the project agents in
`.clawcodex/agents/math-*.md`; route mathematical work to the appropriate
specialist and keep the authoritative status. You may copy supplied statements
verbatim, maintain records, run mechanical checks, and assemble accepted files.
Do not fill a specialist's mathematical gap yourself.

Request: $ARGUMENTS

## Choose the operation

These are arguments to this skill, interpreted in the conversation, not shell commands:

- `start`: create a named team ready for work; start a named NL sketcher and
  generator with a brief standby assignment. Do not invent a math problem.
- A problem statement or source path: start/reuse the team and solve in
  natural-language mode.
- `formal <statement or Lean path>`: use the Lean workflow.
- `knowledge <request>`: use the local knowledge-base workflow.
- `continue <problem-id>`: read the saved problem artifacts and resume from
  their evidence. After a process restart, create fresh workers and task IDs.
- `status`: report recorded members, live state when available, task progress,
  accepted results, blockers, and artifact paths.
- `stop`: checkpoint the problem and shut down this team.

Default team name: `math-team`. Honor an explicit `team=<name>` in the request.
Use a filesystem-safe name containing letters, digits, hyphens, or underscores.
Keep the selected team name in every team call. A bare invocation means `start`,
even if the Request line still contains an unexpanded template placeholder.
`status` and `stop` never create a team or launch workers. If there is no owned
live runtime, report the saved state and any stale roster instead.

## Read the relevant instructions

Read [protocol.md](references/protocol.md) and [roles.md](references/roles.md).
For solving, read only the matching workflow:
[natural-language.md](references/natural-language.md),
[lean.md](references/lean.md), or [knowledge.md](references/knowledge.md).
The blind statement-readback agent is deliberately exempt from shared problem
context; follow its restricted dispatch in the Lean workflow.

## Establish the team

1. Resolve the project root containing this skill, the requested team name, and
   the session's workspace. Discover `TeamCreate`/`TeamDelete` with `ToolSearch`
   if their schemas are deferred. Verify the needed `math-*` definitions are
   available before dispatch.
2. Reuse a matching team only if this session actually owns its live runtime.
   A roster on disk does not restore a runtime. ClawCodex allows one active team
   per workspace. If another team exists, report its name and owner; do not
   overwrite it or stop it as a side effect of starting this one.
   If a roster is stale, explain that it needs separate recovery after the old
   process is confirmed stopped. Never delete a roster merely to make startup pass.
3. If needed, call `TeamCreate` with the selected name and a math-workflow description.
4. For each persistent member use an explicit registered definition, a unique
   teammate name, the actual team name, and `model: "inherit"`. For example:

   ```json
   {
     "description": "Plan the mathematical proof",
     "subagent_type": "math-nl-sketcher",
     "name": "nl-sketcher",
     "team_name": "math-team",
     "model": "inherit",
     "prompt": "Use the supplied task packet. Write only its assigned artifacts, report to team-lead with SendMessage, and remain available."
   }
   ```

   Replace the example prompt with a complete packet from the protocol. Adapt
   the example team name if the user chose another.
   For `start` without a problem, supply the root, protocol, role, and team/member
   names only; state that no problem is assigned and the worker should stand by.
   Do not invent a task, problem directory, or mathematical artifact.
5. Start only the needed specialists. Keep at most two long-lived members by
   default, honor the actual runtime admission limits, and leave capacity for
   fresh review. Idle teammates still occupy live-worker slots. Retire an idle
   member through approved shutdown when another specialty needs its slot.
   Never spawn all 26 roles at once or change global limits.
6. Independent NL verifiers, formal-statement reviewers, and blind readback
   agents run as fresh synchronous `Agent` calls: explicit `subagent_type`,
   `model: "inherit"`, `run_in_background: false`, and **omit** both `name`
   and `team_name`. Supply only the review packet, not prior conversation,
   reviewer verdicts, or author confidence. Do not turn these roles into
   persistent reviewers. They appear as delegated runs, not long-lived roster members.

Use `SendMessage` for subsequent assignments to a live named specialist; do not
spawn the same live name again. Team members report through `team-lead`.
Keep the team available after reporting the outcome unless the user requested
shutdown. End idle turns normally; do not run a model-driven polling loop.

## Store work and coordinate assignments

Use `<workspace>/.clawcodex/math-team/problems/<problem-id>/` for durable problem
artifacts unless the user chooses another location. Select a short safe slug;
if it already exists, confirm from its request whether this is the same problem
before reusing it. Do not overwrite an unrelated run. Record the exact original
request in `request.md` and the team name, mode, paths, and configured budget in
`RUN.md`. Pass **absolute** input/output/protocol paths to workers.

Use `TaskCreate`, `TaskUpdate`, `TaskGet`, and `TaskList` for shared tracking.
Task descriptions identify the problem ID, intended role, inputs, output path,
dependencies, and acceptance condition. Set ownership explicitly; keep review
and publication tasks assigned to `team-lead`. With idle workers, newly created
unowned tasks can be auto-claimed: follow the protocol's role/owner checks and
re-read the actual task after assignment. Do not treat a task-completed flag as
a proof verdict.

For a dependency-gated task, an ownership notification is not a release to work:
check that every `blockedBy` task is complete and the required artifacts exist.
Send only actionable assignments. Record actual returned task and agent IDs,
not invented IDs.

Keep `STATUS.md` and `HANDOFF.md` current: accepted artifact versions and review
paths, unresolved obligations, branch queue, current owners, failed attempts
and their scope, next action, and resource limits. Preserve proof attempts and
review packets rather than rewriting accepted evidence. A continued problem
recreates only unfinished tasks from these records; it does not recover live
workers or their old conversation histories.

## Finish or stop

Report the original target, result status, evidence paths, remaining gaps, and
which members are standing by. Claim a proof only under the relevant workflow's
acceptance conditions. Respect explicit user budgets; do not infer exhaustion
from one failed attempt. If a required tool or specialist is unavailable, save
a concrete blocker and recovery handoff.

On `stop`, save task/role status and incomplete work in the durable problem
directory. Send each live member:

```json
{"to":"nl-generator","message":{"type":"shutdown_request","reason":"The user requested math-team shutdown."}}
```

Use the actual names. Wait for matching approvals and terminal worker state.
For an unresponsive worker after a bounded wait, use `TaskStop` with its recorded
ID as needed to honor the stop request; retain its unfinished work in the handoff.
Call `TeamDelete` only after all teammates exit. It removes the live roster,
mailboxes, and task board, not the saved definitions, this skill, or problem
artifacts. Never delete those durable files during team cleanup.

## Examples

```text
/math-team start
/math-team Prove that every finite subgroup of the multiplicative group of a field is cyclic.
/math-team formal Check the theorem in my-project/Main.lean against the supplied statement.
/math-team knowledge Find relevant results in the local math wiki.
/math-team continue finite-subgroups
/math-team status
/math-team stop
```
