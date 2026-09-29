# Reproduce the pinned statement scaffold

**Status: no target proof exists.** `ArithmeticStatement.Target` is a definition
of the intended proposition, not a proved theorem. `UnfinishedScaffold` has an
unprovided `result : Target` field. These instructions reproduce statement and
environment checks only, not the user's final success condition.

## Exact environment

Project directory:

```text
.clawcodex/math-team/problems/liouville-goldbach-jul2026/lean
```

- Lean toolchain: `leanprover/lean4:v4.32.2`.
- Lean source/binary commit: `f3b06c705e6c85f5314019d5d3baab0fec5b580c`.
- Mathlib: `905b95818eb32af7874a58b427f50c1711a5e96c` (dated release `v4.32.2`).
- Preserve `lean-toolchain`, `lakefile.toml`, and `lake-manifest.json` exactly.
- All eight transitive exact revisions are in `lake-manifest.json` and
  `environment-report.txt`; metadata/date witnesses are alongside this file.
- Do not run an unpinned update or replace a pin with `main`/`master`.

## Actual checks

Run from the project directory:

```sh
lake env lean --version
lake build Statement.Definitions Statement.Scaffold Statement.Smoke Statement
lake env lean Statement/Scaffold.lean
lake env lean Statement/Smoke.lean
lake env lean .clawcodex/math-team/review-inputs/r20260924-v1/Declaration.lean
```

All these commands exited 0 in this run. `Statement` is also the default Lake
target and imports the definitions, scaffold, and smoke modules explicitly.
`Statement.Smoke` prints the exact declaration types and transitive axiom sets,
and runs finite definition tests. Expected factor list at 12 is `[2, 2, 3]`;
expected `(n, omega n, lambda n)` values include `(1, 0, 1)`, `(4, 2, 1)`, and
`(8, 3, -1)`. The reported axiom set for the definitions is
`[propext, Classical.choice, Quot.sound]`, without `sorryAx`.

The supplemental neutral `Dependencies.lean` and `ListOperations.lean` files
are **signature/definition excerpts with proof bodies erased**, not standalone
compilation modules. Only `Declaration.lean` is an independent compiling copy.

## Re-fetch the bounded cache if needed

From the same project directory, with the pinned source checkouts present:

```sh
MATHLIB_NO_CACHE_ON_UPDATE=1 \
MATHLIB_CACHE_DIR=.clawcodex/math-team/problems/liouville-goldbach-jul2026/formal/environment/cache \
lake exe cache get Mathlib.Data.Nat.Factors Mathlib.Algebra.Group.Even
```

The initial fetch retrieved 664 module artifacts, not the whole Mathlib cache.
No global cache or toolchain change is required. The cache tool itself is built
from the pinned Mathlib source.

For a fresh source checkout, reproduce each package's saved `*-git-init`,
`*-git-remote`, `*-git-fetch`, and `*-git-checkout` command using the exact SHA
in the preserved manifest. The initial checkout procedure was:

```sh
git init <project-local-package-directory>
git -C <project-local-package-directory> remote add origin <audited-repository-url>
git -C <project-local-package-directory> fetch --depth 1 --no-tags origin <audited-full-sha>
git -C <project-local-package-directory> checkout --detach <audited-full-sha>
```

Do not resolve a moving branch before auditing its version. `setup_pinned.py`
records how the original root manifest and checkouts were initialized; it
refuses to overwrite an existing root manifest, preserving this snapshot.
Do not delete existing accepted artifacts merely to rerun it.

## Evidence and replay

For every recorded command, `<label>.json` records argv, cwd, environment,
timeout, exit status and SHA-256 of `<label>.stdout` and `<label>.stderr`.
Relevant labels: `lake-env-version`, `cache-factors`, `build-statement-v1`,
`lean-scaffold-v1`, `lean-smoke-v1`, `lean-review-declaration-v1`.
The recorder `run.py` can capture a replay using a **new** label; it refuses to
overwrite previous evidence. `statement-hashes-v1.stdout` and
`../formalizer/snapshot-v1.json` identify the production statement artifacts.

Fresh blind readback, source-fidelity approval, all target proof development,
master integration, and final theorem verification remain separate obligations.
