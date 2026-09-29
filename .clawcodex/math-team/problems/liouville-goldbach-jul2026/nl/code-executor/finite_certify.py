#!/usr/bin/env python3
"""Exact, bounded Liouville arithmetic audit; not a universal theorem prover.

Run with Python's -I -S flags. No third-party imports, randomness, floating-point
arithmetic, probabilistic primality tests, or mathematical source imports.
The parent process records the actual worker exit status and artifact hashes.
"""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import traceback

SCRIPT = Path(__file__).resolve()
OUT = SCRIPT.parent
PROBLEM = OUT.parent.parent
ROOT = PROBLEM.parents[3]
INPUTS = {
    "request": PROBLEM / "request.md",
    "protocol": ROOT / ".clawcodex/skills/math-team/references/protocol.md",
}
BOUND = 2608
IDENTITY_MIN = 2
IDENTITY_MAX = 256
REPRESENTATIVES = (2, 3, 4, 10, 256)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")


def runtime_record():
    modules = {}
    for name, module in (("hashlib", hashlib), ("json", json),
                         ("pathlib", sys.modules["pathlib"]),
                         ("subprocess", subprocess), ("traceback", traceback)):
        path = Path(module.__file__).resolve()
        modules[name] = {"path": str(path), "sha256": sha256(path)}
    executable = Path(sys.executable).resolve()
    return {
        "implementation": sys.implementation.name,
        "version": sys.version,
        "version_info": list(sys.version_info),
        "executable": str(executable),
        "executable_sha256": sha256(executable),
        "isolated": sys.flags.isolated,
        "no_site": sys.flags.no_site,
        "direct_stdlib_module_files": modules,
    }


def trial_factor(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("trial_factor requires a positive integer")
    remaining = n
    factors = []
    divisor = 2
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors.append([divisor, exponent])
        divisor += 1
    if remaining > 1:
        factors.append([remaining, 1])
    return factors


def trial_lambda(n):
    omega = sum(exponent for _, exponent in trial_factor(n))
    return 1 if omega % 2 == 0 else -1


def prime_divisor_certificate(p):
    divisors = []
    remainders = []
    divisor = 2
    while divisor * divisor <= p:
        divisors.append(divisor)
        remainders.append(p % divisor)
        divisor += 1
    return {
        "p": p,
        "tested_divisors": divisors,
        "remainders": remainders,
        "is_prime": p >= 2 and all(r != 0 for r in remainders),
        "first_divisor_beyond_sqrt": divisor,
    }


def liouville_sieve(bound):
    # Independent of trial_factor: Eratosthenes, then one sign flip per p^j.
    prime = [True] * (bound + 1)
    prime[0] = False
    prime[1] = False
    divisor = 2
    while divisor * divisor <= bound:
        if prime[divisor]:
            for multiple in range(divisor * divisor, bound + 1, divisor):
                prime[multiple] = False
        divisor += 1
    values = [None] + [1] * bound  # lambda(0) is intentionally undefined.
    for p in range(2, bound + 1):
        if prime[p]:
            power = p
            while power <= bound:
                for multiple in range(power, bound + 1, power):
                    values[multiple] = -values[multiple]
                power *= p
    return values, prime


class Checks:
    def __init__(self):
        self.count = 0
        self.counts_by_category = {}
        self.failures = []

    def equal(self, category, label, actual, expected):
        self.count += 1
        self.counts_by_category[category] = (
            self.counts_by_category.get(category, 0) + 1)
        if actual != expected:
            self.failures.append({"category": category, "label": label,
                                  "actual": actual, "expected": expected})


def audit(result, checks):
    values, prime_flags = liouville_sieve(BOUND)
    used = {}

    def lam(n, context):
        if not 1 <= n <= BOUND:
            raise ValueError("lambda argument outside declared finite universe")
        used.setdefault(n, set()).add(context)
        return values[n]

    def pair(a, b, context):
        la, lb = lam(a, context), lam(b, context)
        return {"a": a, "b": b, "sum": a + b,
                "lambda_a": la, "lambda_b": lb,
                "both_positive_lambda": la == 1 and lb == 1,
                "both_negative_lambda": la == -1 and lb == -1}

    # The formulas below are explicit; the supplied PB label was not defined
    # in request.md, so its fidelity to these three tests is not asserted.
    q37 = {"q": 37, "twice_q": 74,
           "three_tests": [pair(a, 74 - a, "q37") for a in (1, 4, 6)],
           "successful_plus_pair": pair(9, 65, "q37")}
    checks.equal("example", "q37 prime", trial_factor(37), [[37, 1]])
    checks.equal("example", "q37 first three positive-lambda first summands",
                 [n for n in range(1, 9) if lam(n, "q37") == 1], [1, 4, 6])
    for row in q37["three_tests"]:
        checks.equal("example", "q37 failed candidate sum a=" + str(row["a"]),
                     row["sum"], 74)
        checks.equal("example", "q37 failed candidate signs a=" + str(row["a"]),
                     [row["lambda_a"], row["lambda_b"]], [1, -1])
    checks.equal("example", "q37 9+65 sum", q37["successful_plus_pair"]["sum"], 74)
    checks.equal("example", "q37 9+65 signs",
                 [q37["successful_plus_pair"]["lambda_a"],
                  q37["successful_plus_pair"]["lambda_b"]], [1, 1])
    q37["reduced_three_test_arguments"] = [
        {"n": n, "lambda": lam(n, "q37")} for n in (73, 35, 34)]
    checks.equal("example", "q37 reduced three-test signs",
                 [row["lambda"] for row in q37["reduced_three_test_arguments"]],
                 [-1, 1, 1])
    for n in (37, 74):
        lam(n, "q37")
    result["q37"] = q37

    q5 = {"q": 5, "terms": [lam(n, "q5_L4") for n in range(1, 5)]}
    q5["L_inclusive_4"] = sum(q5["terms"])
    checks.equal("example", "q5 prime", trial_factor(5), [[5, 1]])
    checks.equal("example", "L4 terms", q5["terms"], [1, -1, -1, 1])
    checks.equal("example", "L4 equals zero", q5["L_inclusive_4"], 0)
    lam(5, "q5_L4")
    result["q5"] = q5

    identities = []
    for n in range(IDENTITY_MIN, IDENTITY_MAX + 1):
        l_sum = sum(lam(a, "identity") for a in range(1, n))
        c_sum = sum(lam(a, "identity") * lam(n - a, "identity")
                    for a in range(1, n))
        pairs = [(a, n - a) for a in range(1, n)
                 if lam(a, "identity") == -1 and lam(n - a, "identity") == -1]
        r_count = len(pairs)  # Actual ordered positive pairs, not rearranged RHS.
        lhs = 4 * r_count
        rhs = (n - 1) - 2 * l_sum + c_sum
        checks.equal("identity", "N=" + str(n), lhs, rhs)
        row = {"N": n, "L_inclusive_N_minus_1": l_sum,
               "C_signed": c_sum, "R_ordered_positive_pairs": r_count,
               "lhs": lhs, "rhs": rhs}
        identities.append(row)
        if n == 10:
            result["N10"] = dict(row, ordered_negative_pairs=[list(p) for p in pairs])
    checks.equal("example", "N10 C", result["N10"]["C_signed"], 9)
    checks.equal("example", "N10 R", result["N10"]["R_ordered_positive_pairs"], 5)
    checks.equal("example", "N10 ordered pairs", result["N10"]["ordered_negative_pairs"],
                 [[2, 8], [3, 7], [5, 5], [7, 3], [8, 2]])
    checks.equal("coverage", "identity N sequence", [r["N"] for r in identities],
                 list(range(2, 257)))
    result["identity_rows"] = identities

    # Representative independent loop: two indices, fresh trial factorizations,
    # and no sieve access. In particular, neither count is inferred from identity.
    representatives = []
    for n in REPRESENTATIVES:
        direct_pairs = []
        c_sum = 0
        for a in range(1, n):
            for b in range(1, n):
                if a + b == n:
                    la, lb = trial_lambda(a), trial_lambda(b)
                    c_sum += la * lb
                    if la == -1 and lb == -1:
                        direct_pairs.append([a, b])
        l_sum = sum(trial_lambda(a) for a in range(1, n))
        baseline = identities[n - IDENTITY_MIN]
        checks.equal("independent_representative", "R N=" + str(n), len(direct_pairs),
                     baseline["R_ordered_positive_pairs"])
        checks.equal("independent_representative", "C N=" + str(n), c_sum,
                     baseline["C_signed"])
        checks.equal("independent_representative", "L N=" + str(n), l_sum,
                     baseline["L_inclusive_N_minus_1"])
        representatives.append({"N": n, "R": len(direct_pairs), "C": c_sum,
                                "L": l_sum, "ordered_negative_pairs": direct_pairs})
    result["independent_representatives"] = representatives

    square_rows = []
    m = 1304
    for k in range(1, 8):
        square = k * k
        residual = m - square
        reduced = pair(square, residual, "square_template")
        target = pair(2 * square, 2 * residual, "square_template")
        row = {"k": k, "square": square, "m_minus_square": residual,
               "reduced_pair": reduced, "target_pair": target}
        expected_reduced = [1, -1] if k <= 6 else [1, 1]
        expected_target = [-1, 1] if k <= 6 else [-1, -1]
        checks.equal("square", "reduced signs k=" + str(k),
                     [reduced["lambda_a"], reduced["lambda_b"]], expected_reduced)
        checks.equal("square", "target signs k=" + str(k),
                     [target["lambda_a"], target["lambda_b"]], expected_target)
        checks.equal("square", "reduced positive k=" + str(k),
                     reduced["a"] > 0 and reduced["b"] > 0, True)
        checks.equal("square", "target positive k=" + str(k),
                     target["a"] > 0 and target["b"] > 0, True)
        checks.equal("square", "reduced sum k=" + str(k), reduced["sum"], 1304)
        checks.equal("square", "target sum k=" + str(k), target["sum"], 2608)
        square_rows.append(row)
    checks.equal("square", "six failures then one success",
                 [row["target_pair"]["both_negative_lambda"] for row in square_rows],
                 [False] * 6 + [True])
    checks.equal("square", "k7 pair is 98+2510",
                 [square_rows[-1]["target_pair"]["a"],
                  square_rows[-1]["target_pair"]["b"]], [98, 2510])
    lam(1304, "square_template")
    lam(2608, "square_template")
    result["m1304"] = {"m": m, "N": 2 * m, "square_tests": square_rows}

    factor_rows = []
    unique_primes = set()
    for n in sorted(used):
        factors = trial_factor(n)
        omega = sum(exponent for _, exponent in factors)
        trial_sign = 1 if omega % 2 == 0 else -1
        reconstruction = 1
        for p, exponent in factors:
            reconstruction *= p ** exponent
            unique_primes.add(p)
        checks.equal("factor_product", "n=" + str(n), reconstruction, n)
        checks.equal("lambda_cross_check", "n=" + str(n), trial_sign, values[n])
        checks.equal("lambda_sign_range", "n=" + str(n), values[n] in (-1, 1), True)
        factor_rows.append({"n": n, "prime_powers": factors, "Omega": omega,
                            "lambda_trial": trial_sign, "lambda_sieve": values[n],
                            "reconstructed_product": reconstruction,
                            "contexts": sorted(used[n])})
    prime_certificates = []
    for p in sorted(unique_primes):
        certificate = prime_divisor_certificate(p)
        checks.equal("prime_certificate", "factor p=" + str(p), certificate["is_prime"], True)
        checks.equal("prime_sieve_cross_check", "factor p=" + str(p), prime_flags[p], True)
        prime_certificates.append(certificate)
    checks.equal("coverage", "all identity lambda arguments present",
                 all(n in used for n in range(1, 256)), True)
    result["lambda_entries_used"] = factor_rows
    result["prime_divisor_certificates"] = prime_certificates
    result["coverage"] = {
        "identity_N_count": len(identities),
        "identity_N_min": IDENTITY_MIN,
        "identity_N_max": IDENTITY_MAX,
        "identity_ordered_pair_positions_examined": sum(n - 1 for n in range(2, 257)),
        "used_lambda_argument_count": len(used),
        "used_lambda_argument_min": min(used),
        "used_lambda_argument_max": max(used),
        "all_used_lambda_entries_cross_checked": True,
        "sieve_bound": BOUND,
        "sieve_entries_not_used_in_claims": BOUND - len(used),
        "independently_rechecked_N": list(REPRESENTATIVES),
        "symmetry_reduction": "none; both (a,b) and (b,a), and diagonal a=b, retained",
        "scope_excludes": ["broad target search", "broad bridge search",
                           "N outside 2..256 except specified examples",
                           "universal counting-identity proof", "global target proof"],
    }


def worker():
    checks = Checks()
    result = {
        "mode": "CERTIFICATION / finite computational AUDIT",
        "claim": "Only the explicit finite arithmetic claims and identity instances recorded here",
        "global_mathematical_conclusion": "none",
        "source_policy": {
            "cutoff_inclusive": "2026-07-31",
            "external_mathematical_inputs": [],
            "third_party_dependencies": [],
            "code": "newly written for this bounded audit",
            "seed": None,
            "arithmetic": "Python arbitrary-precision integers only; no rounding error",
        },
        "definitions": {
            "lambda": "(-1)^Omega(n), positive integer n, Omega(1)=0",
            "L": "inclusive sum lambda(a) for a=1,...,N-1",
            "C": "signed sum lambda(a)*lambda(N-a) for a=1,...,N-1",
            "R": "actual ordered positive pairs (a,b), a+b=N, both lambda=-1; a=b permitted",
            "identity": "4*R(N)=(N-1)-2*L(N-1)+C(N)",
            "explicit_three_tests": "(1,2q-1),(4,2q-4),(6,2q-6) at q=37",
            "square_test": "k=1,...,7; (k^2,m-k^2), then (2k^2,2(m-k^2)), m=1304",
        },
        "template_label_limitation": (
            "PB three-test is not defined in the supplied request.md. The explicit "
            "three-smallest-positive-lambda-first-summand tests are checked, but "
            "their fidelity to the undefined PB label is not certified. "
            "The square-template formulas are recorded explicitly as well."),
        "unresolved_obligations": [
            "Leader must confirm that the explicit three tests match the intended PB definition.",
            "No claim for every N, nor a formal proof of the counting identity, is supplied.",
            "No Lean execution, universal positivity argument, or final theorem certification is supplied.",
        ],
        "runtime": runtime_record(),
        "input_artifacts": {name: {"path": str(path), "sha256": sha256(path)}
                            for name, path in INPUTS.items()},
        "script": {"path": str(SCRIPT), "sha256": sha256(SCRIPT)},
        "exceptions": [],
    }
    try:
        audit(result, checks)
    except Exception:
        result["exceptions"].append(traceback.format_exc())
    result["assertion_count"] = checks.count
    result["assertion_counts_by_category"] = checks.counts_by_category
    result["failed_assertions"] = checks.failures
    exit_status = 2 if result["exceptions"] else (1 if checks.failures else 0)
    result["worker_intended_exit_status"] = exit_status
    result["verdict"] = ("PASS_EXPLICIT_FINITE_CLAIMS_ONLY" if exit_status == 0
                         else "FAIL_OR_INCOMPLETE")
    write_json(OUT / "evidence.json", result)
    print("verdict=" + result["verdict"])
    print("assertions=" + str(checks.count))
    print("failed_assertions=" + str(len(checks.failures)))
    for failure in checks.failures:
        print("FAILED_ASSERTION " + json.dumps(failure, sort_keys=True))
    for exception in result["exceptions"]:
        print("EXCEPTION " + exception)
    if "coverage" in result:
        print("coverage=" + json.dumps(result["coverage"], sort_keys=True))
    print("PB_label_fidelity=UNVERIFIED; explicit formulas recorded")
    print("worker_intended_exit_status=" + str(exit_status))
    return exit_status


def package():
    parent_command = [sys.executable, "-I", "-S", str(SCRIPT)]
    worker_command = parent_command + ["--worker"]
    completed = subprocess.run(worker_command, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True, check=False)
    log = ("mode=CERTIFICATION, finite scope only\n"
           + "parent_command=" + json.dumps(parent_command) + "\n"
           + "worker_command=" + json.dumps(worker_command) + "\n"
           + "--- worker stdout ---\n" + completed.stdout
           + "--- worker stderr ---\n" + completed.stderr
           + "worker_actual_exit_status=" + str(completed.returncode) + "\n"
           + "parent_exit_status=" + str(completed.returncode) + "\n")
    (OUT / "run.log").write_text(log, encoding="utf-8")
    paths = {"script": SCRIPT, "evidence": OUT / "evidence.json",
             "log": OUT / "run.log", **INPUTS}
    manifest = {
        "parent_command": parent_command,
        "worker_command": worker_command,
        "working_directory_constraint": "none; all paths absolute",
        "worker_actual_exit_status": completed.returncode,
        "parent_exit_status": completed.returncode,
        "runtime": runtime_record(),
        "artifacts": {name: {"path": str(path), "sha256": sha256(path)}
                      for name, path in paths.items() if path.exists()},
    }
    write_json(OUT / "run.json", manifest)
    print(log, end="")
    return completed.returncode


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(package())
    if sys.argv[1:] == ["--worker"]:
        sys.exit(worker())
    print("usage: python3 -I -S " + str(SCRIPT), file=sys.stderr)
    sys.exit(2)
