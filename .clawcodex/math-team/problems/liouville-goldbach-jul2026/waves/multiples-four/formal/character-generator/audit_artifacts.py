#!/usr/bin/env python3
"""Compare literal approved statements and record exact pinned-source provenance."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

OUT = Path(__file__).resolve().parent
P = OUT.parents[3]
LEAN = P / "lean"
W = P / "waves/multiples-four"
M = LEAN / ".lake/packages/mathlib"
APPROVED = W / "formal/descent-blueprint/Readback.lean.txt"
SHA = lambda data: hashlib.sha256(data).hexdigest()
expected_approved = "372c3a6b8acfc112331707944bfef543c12ea03049ce5bb95eae7e34f9591763"
assert SHA(APPROVED.read_bytes()) == expected_approved
text = APPROVED.read_text()
lines = text.splitlines(keepends=True)

specs = {
    "ResidueValue": [("residueLambda", 23, 24, "def"), ("GoodMultiplier", 26, 28, "def"),
        ("residueLambda_natCast", 71, 72, "theorem"), ("residueLambda_sign", 74, 75, "theorem"),
        ("residueLambda_neg", 77, 80, "theorem"), ("goodMultiplier_one", 82, 83, "theorem"),
        ("goodMultiplier_neg", 85, 88, "theorem")],
    "Rigidity": [("goodMultiplier_natCast_step", 90, 94, "theorem"),
        ("residueLambda_mul", 96, 99, "theorem"), ("lambda_eq_one_of_isSquare", 101, 104, "theorem")],
    "ResiduePrime": [("prime_dvd_quarter_isSquare", 106, 109, "theorem"),
        ("exists_small_prime_isSquare", 111, 114, "theorem")],
}
comparison = {"approved_snapshot": str(APPROVED), "approved_sha256": expected_approved,
    "comparison_rule": "Exact UTF-8 internal text, including whitespace and final LF; only the theorem body separator ' := by' and proof are excluded. Definition bodies are included.",
    "declarations": {}, "sources": {}, "prohibited_tokens": {}}
actual_interfaces = []
for module, specs_for_module in specs.items():
    path = LEAN / f"Statement/FourWork/Character/{module}.lean"
    source = path.read_text()
    comparison["sources"][str(path)] = SHA(path.read_bytes())
    banned = re.findall(r"\b(?:sorry|admit|axiom|unsafe|native_decide|sorryAx)\b", source)
    comparison["prohibited_tokens"][str(path)] = banned
    assert not banned, (path, banned)
    names = re.findall(r"^(?:theorem|lemma|def|axiom)\s+(\w+)", source, re.M)
    assert names == [s[0] for s in specs_for_module], (path, names)
    for name, start, end, kind in specs_for_module:
        approved = "".join(lines[start - 1:end])
        pattern = rf"^{kind} {name}\b[\s\S]*?" + (r"(?= := by)" if kind == "theorem" else r"(?=\n\n)")
        candidate = re.search(pattern, source, re.M).group() + "\n"
        record = {"source": str(path), "approved_lines": [start, end],
            "approved_sha256": SHA(approved.encode()), "candidate_sha256": SHA(candidate.encode()),
            "exact_equal": candidate == approved, "text": candidate}
        comparison["declarations"][name] = record
        assert candidate == approved, name
        actual_interfaces.append(candidate)

fixed_expected = {
    "Statement/Definitions.lean": "79e976007c612f99c2023e675ca81337145dc25dd762e1ad17b967d0ac7cde6d",
    "Statement/Partial.lean": "9f0f46d5b9cc6442e76b73148e94c8c84766136acabebb7e709e398cfab4c8f0",
    "Statement/FourPartial.lean": "4b5e430fcfc8f766475ce4d0483f129642b0eaffc2af34e78a42d9bf10581325",
    "lean-toolchain": "2bdc48adfa58d0017e538a0ad117c5d73d35deec879978f909406a80c8037273",
    "lakefile.toml": "0ccf5fbb075e3de589067cac832ecde230db77c411efaa495b5578ad69cddaa4",
    "lake-manifest.json": "de9173316a8421f7f5572cf43fc93768e3bffe6de99141c2de2ccf17dc40ef03",
}
comparison["fixed_files"] = {}
for rel, expected in fixed_expected.items():
    actual = SHA((LEAN / rel).read_bytes())
    comparison["fixed_files"][str(LEAN / rel)] = {"expected": expected, "actual": actual, "unchanged": actual == expected}
    assert actual == expected, rel
comparison["all_comparisons_pass"] = True
(OUT / "statement-comparison-v1.json").write_text(json.dumps(comparison, indent=2, ensure_ascii=False) + "\n")
(OUT / "approved-statements-v1.lean.txt").write_bytes(APPROVED.read_bytes())
neutral = "".join(lines[:21]) + "\n" + "\n".join(actual_interfaces) + "\nend FourWork\nend ArithmeticStatement\n"
(OUT / "CharacterInterfaces-v1.lean.txt").write_text(neutral)

commands = [
    ["git", "-C", str(M), "rev-parse", "HEAD"],
    ["git", "-C", str(M), "show", "-s", "--format=%H%n%cI", "HEAD"],
    ["git", "-C", str(M), "status", "--porcelain"],
    ["lake", "env", "lean", "--version"],
]
provenance = {"cwd": str(LEAN), "commands": [], "source_hashes": {},
    "cache_command_log": str(OUT / "reciprocity-cache.log"),
    "source_cutoff": "2026-07-31 inclusive", "no_lake_update": True}
for argv in commands:
    proc = subprocess.run(argv, cwd=LEAN, text=True, capture_output=True)
    provenance["commands"].append({"argv": argv, "exit_status": proc.returncode,
        "stdout": proc.stdout, "stderr": proc.stderr})
    assert proc.returncode == 0
assert provenance["commands"][0]["stdout"].strip() == "905b95818eb32af7874a58b427f50c1711a5e96c"
assert not provenance["commands"][2]["stdout"]
paths = [
    M / "Mathlib/NumberTheory/LegendreSymbol/Basic.lean",
    M / "Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean",
    M / "Mathlib/Algebra/Field/ZMod.lean",
    M / "Mathlib/Data/ZMod/Basic.lean",
    M / "Mathlib/Algebra/Group/Even.lean",
    M / "Mathlib/Data/Nat/Prime/Defs.lean",
    M / "Mathlib/Data/Nat/Prime/Basic.lean",
    M / "Mathlib/Data/Nat/ModEq.lean",
    M / "Mathlib/Data/Nat/Init.lean",
    M / "Mathlib/Algebra/GroupWithZero/Defs.lean",
    M / "Mathlib/Algebra/GroupWithZero/Basic.lean",
    LEAN / "Statement/FourWork/Descent/Cyclic.lean",
    W / "formal/reviews/descent-fidelity-v1.md",
    W / "nl/descent/proof-attempt-v1.md",
    W / "request.md",
    Path.home() / ".elan/toolchains/leanprover--lean4---v4.32.2/src/lean/Init/Data/Int/Order.lean",
    Path.home() / ".elan/toolchains/leanprover--lean4---v4.32.2/src/lean/Init/Data/Nat/Dvd.lean",
]
for path in paths:
    provenance["source_hashes"][str(path)] = SHA(path.read_bytes())
cyclic = LEAN / "Statement/FourWork/Descent/Cyclic.lean"
assert provenance["source_hashes"][str(cyclic)] == "09fbee47a60bf7db94d65e871fc49f5d07d60838c8b01cfbfdecb53033471290"
(OUT / "Cyclic-dependency-v1.lean.txt").write_bytes(cyclic.read_bytes())
api_ranges = {
    "Mathlib/NumberTheory/LegendreSymbol/Basic.lean": [(282, 286)],
    "Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean": [(45, 45), (73, 77), (99, 99), (153, 167)],
    "Mathlib/Algebra/Field/ZMod.lean": [(17, 39)],
}
provenance["reciprocity_api_source_and_field_instance"] = {}
for rel, ranges in api_ranges.items():
    slines = (M / rel).read_text().splitlines(keepends=True)
    provenance["reciprocity_api_source_and_field_instance"][rel] = [
        {"lines": [start, end], "text": "".join(slines[start-1:end])} for start, end in ranges]
(OUT / "provenance-v1.json").write_text(json.dumps(provenance, indent=2, ensure_ascii=False) + "\n")
print("All 10 theorem statements and 2 definitions exactly match approved snapshot.")
print("Baseline definitions, old masters, and pins match approved hashes; no prohibited proof tokens.")
for path, digest in comparison["sources"].items():
    print(digest, path)
print("Pinned source provenance and frozen compiled Cyclic dependency recorded.")
