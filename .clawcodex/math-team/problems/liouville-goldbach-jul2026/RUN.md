# Run record

- Date: 2026-09-24. Source eligibility cutoff: 2026-07-31 inclusive (UTC at the boundary when applicable).
- Workspace: .
- Problem: liouville-goldbach-jul2026; mode: formal plus natural-language discovery/certification.
- Team: math-team. Main-session leader ID: tcp9ou0cy.
- Limits: at most two persistent specialists; fresh synchronous anonymous reviewers; no global limit changes, no explicit user total-time/token budget. Config(max_agents) returned null; runtime admission is authoritative.
- Protocol: .clawcodex/skills/math-team/references/protocol.md; workflows lean.md and natural-language.md.
- User approved archiving an inactive unrelated team. Old roster and completed task state preserved in .clawcodex/math-team/runtime-archive/20260924-before-liouville/. No existing mathematical artifacts removed.
- Initial tools: ~/.elan/bin/{lean,lake,elan}, /opt/homebrew/bin/gh, /usr/bin/python3.
- `elan toolchain list`: leanprover/lean4:v4.32.2. No initial lean-toolchain, lakefile, or manifest in this workspace.
- GitHub release metadata query: `gh api repos/leanprover/lean4/releases/tags/v4.32.2 --jq '{tag_name,published_at,target_commitish,html_url}'`; exit 0; published_at 2026-07-28T16:34:35Z. A compatible pinned mathematical library remains to be selected.
- Source protocol: metadata may establish dates; mathematical evidence requires an eligible immutable version. No later mathematical sources are authorized. Newly derived arguments are local contributions, not historical claims.
- Master development: `lean/Statement/Partial.lean`, imported by root `lean/Statement.lean`. Only math-fl-integrator performed its merge. The original target remains unproved.

## Actual specialists and task identities

Persistent workers were rotated with matching approved shutdowns, never exceeding two live members:
- fl-formalizer `txt8idic5`, task `ca76ab6f021e`: pinned setup, exact definition/scaffold, blind bundle; exited after approval.
- nl-sketcher `t7603z1wv`, task `058f7f3988b0`: exact contract/lemma plan; exited after approval.
- nl-generator `t3tshym2p`, task `987c8d91ddff`: partial proof and repaired optional-route ledger; exited after approval.
- fl-generator `tw05jhslm`, task `4da258fcd6e7`: 42 compiled exact helper theorems; standing by.
- fl-integrator `tp42r5gx3`, task `197f419f93e6`: first-wave master merge and checks; later retired during the multiples-of-four continuation. Current integration worker is fl-integrator-final `tdkudsui0`, idle after completion; the full continuation role/task chronology is in waves/multiples-four/RUN.md.
- Leader tasks `e885c3f26ed2` (statement review/snapshot) and `aa7d226b5a7e` (final partial-evidence review).

Runtime auto-offered several newly created tasks to idle authors before explicit assignment settled. Each wrong-role worker returned the task without performing it; leader re-read/reassigned and the intended worker confirmed actual ownership. These events did not authorize self-review or master edits by generators.

Anonymous synchronous specialist calls used math-nl-searcher (discovery, extraction, follow-up), math-nl-explorer, math-fl-blueprinter, math-nl-ce-hunter, math-nl-code-executor, and math-nl-writer. Reviews/readbacks used fresh synchronous `Agent` calls, explicit subagent_type/model inherit, run_in_background=false, and no name/team_name. No reviewer conversation was reused. No nested agents or external model processes were used.

## Final evidence identities

- Base definition/Target snapshot: `79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d`.
- Approved helper interfaces: `89080f705ec6f0ba690edbc4e7d3d97cea18a6f3d3c3cdcb31e30abefbb434bc`.
- Candidate and byte-identical integrated Partial: `9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0`.
- Final self-contained exposition: `1b93364b818b0eae95875d391ca6f944614f00b963a1e384ba1a0fe2533957a9`.
- Frozen source ledger: `9df552348f03fd84ffe0e203f1340f26e6a902f8424f924068fe6fb86c1a7dbb`.

The first final-review attempt detected source-ledger hash/citation drift and historical-verdict text in a cited proof artifact. It is retained, not counted as a clean final review. Leader preserved the old exposition and changed only its ledger hash and locator; no mathematics or Lean changed. Replacement packets constrained content to the self-contained exposition, actual code, raw checks and dated sources, excluding historical reviews/proof metadata. Two independent fresh final reports cover the final hashes: `nl/reviews/final-review-a-v2.md` and `final-review-b-v1.md`. Both find the stated partial results supported and the original Target unresolved.

## Actual checks and trust

Full commands, working directories, exit statuses and diagnostics: `formal/environment/`, `formal/generator/build-*`, `formal/reviews/candidate-audit-v1.{json,log}`, and `formal/integration/audit-v1.json`/`v1-*`. Default build, explicit Statement.Partial build, direct compile, trust-zero compile and root-import checks all exited 0. Both unproved endpoint names deliberately fail `#check`; expected exit 1 is not accepted as a proof. The standard axiom union is propext, Classical.choice, Quot.sound; no sorryAx, custom mathematical axiom, native-decide assumption, or circular conclusion premise. Source-hash caches and Lean's compiler/kernel/compiled artifacts remain disclosed trust mechanisms; no full upstream from-source rebuild was claimed.

One accidental post-cutoff search snippet was excluded and logged in sources.md. Literature is context only. Finite Python checks are separately recorded and never substituted for universal proof. Final-wave regulator `formal/reviews/final-regulator-v1.md` accepts the partial evidence and leaves Target unresolved; its JSON preserves exact mechanical checks. STATUS.md/HANDOFF.md annotate stale historical progress labels without altering frozen source/proof/review artifacts. No git commit or publication was requested or made. Source browsing completed with the eligible version saved, the owned browser tab closed, and no source uploads.
