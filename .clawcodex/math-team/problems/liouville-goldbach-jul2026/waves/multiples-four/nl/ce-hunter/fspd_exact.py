#!/usr/bin/env python3
"""Bounded exact FSPD diagnostics; Python standard library only.

Run this file directly. No Liouville/Q(p) search. Each prime sign is a bit,
where 1 means -1. Complete multiplicativity is exponent-parity XOR.
The no-pair clause is NOT(bit(a) = bit(4*p-a) = 1).
All factoring and residue tests are direct integer operations.
"""
import json
import platform
import time
from math import isqrt

CASES = (19, 43, 67, 139)
TOTAL_SECONDS = 80.0
MAX_NODES_PER_RUN = 30000
START = time.monotonic()
DEADLINE = START + TOTAL_SECONDS


def emit(x):
    print(json.dumps(x, sort_keys=True), flush=True)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def factors(n):
    out = {}
    rest = n
    for d in range(2, isqrt(n) + 1):
        # At most bit_length(n) divisions for every trial divisor.
        for _ in range(n.bit_length()):
            if rest % d:
                break
            out[d] = out.get(d, 0) + 1
            rest //= d
        if rest == 1:
            break
    if rest > 1:
        out[rest] = out.get(rest, 0) + 1
    assert all(prime(r) for r in out)
    z = 1
    for r, k in out.items():
        z *= r ** k
    assert z == n
    return out


def solve(p, extra_negative, name):
    assert prime(p) and p >= 7 and p % 4 == 3
    primes = [r for r in range(2, 4*p + 1) if prime(r)]
    index = {r: i for i, r in enumerate(primes)}
    residues = {x*x % p for x in range(1, p)}
    q = next(r for r in primes if r % p in residues)
    count = len(primes)
    masks = [0] * (4*p + 1)
    fac = [{}] * (4*p + 1)
    for n in range(1, 4*p + 1):
        fac[n] = factors(n)
        for r, k in fac[n].items():
            if k % 2:
                masks[n] ^= 1 << index[r]
    pairs = [(a, 4*p-a) for a in range(1, 2*p + 1)]
    fixed = sorted(set([2, p] + list(extra_negative(q, primes))))
    nodes = 0
    conflicts = 0
    root_log = []
    root_rows = {}
    result_rows = None

    def reduce(mask, rows, value=0):
        remaining = 0
        for _ in range(count):
            if not mask:
                break
            bit = mask.bit_length() - 1
            if bit in rows:
                rm, rc = rows[bit]
                mask ^= rm
                value ^= rc
            else:
                remaining |= 1 << bit
                mask ^= 1 << bit
        assert not mask
        return remaining, value

    def add(rows, mask, value):
        m, c = reduce(mask, rows, value)
        if not m:
            return (c == 0), False
        rows[m.bit_length() - 1] = (m, c)
        return True, True

    initial = {}
    for r in fixed:
        ok, new = add(initial, 1 << index[r], 1)
        assert ok and new

    def propagate(rows, log):
        for sweep in range(count + 1):
            if time.monotonic() >= DEADLINE:
                return 'LIMIT', []
            changed = False
            active = []
            for a, b in pairs:
                am, ac = reduce(masks[a], rows)
                bm, bc = reduce(masks[b], rows)
                if (not am and ac == 0) or (not bm and bc == 0):
                    continue
                if am == bm and ac != bc:
                    continue
                forcing = None
                reason = None
                if not am and ac == 1:
                    forcing, reason = b, 'left_negative'
                elif not bm and bc == 1:
                    forcing, reason = a, 'right_negative'
                elif am == bm and ac == bc:
                    forcing, reason = a, 'equal_reduced_signs'
                if forcing is not None:
                    ok, new = add(rows, masks[forcing], 0)
                    if not ok:
                        log.append({'pair': [a, b], 'reason': reason,
                                    'conflict': True})
                        return 'CONFLICT', []
                    if new:
                        changed = True
                        log.append({'pair': [a, b], 'reason': reason,
                                    'forced_positive': forcing,
                                    'factors': fac[forcing]})
                else:
                    active.append((a, b, am, bm))
            if not changed:
                return 'STABLE', active
        raise AssertionError('Propagation exceeded rank bound')

    # Iterative depth-first search: at most the stated node budget.
    stack = [(initial, [])]
    status = 'LIMIT'
    for _ in range(MAX_NODES_PER_RUN):
        if not stack:
            status = 'UNSAT'
            break
        if time.monotonic() >= DEADLINE:
            break
        rows, log = stack.pop()
        nodes += 1
        state, active = propagate(rows, log)
        if nodes == 1:
            root_log = list(log)
            root_rows = dict(rows)
        if state == 'LIMIT':
            break
        if state == 'CONFLICT':
            conflicts += 1
            continue
        if not active:
            status = 'SAT'
            result_rows = rows
            break
        a, b, am, bm = min(
            active,
            key=lambda t: (min(bin(t[2]).count('1'), bin(t[3]).count('1')),
                           max(t[2].bit_length(), t[3].bit_length()), t[0]))
        if bin(am).count('1') > bin(bm).count('1'):
            a, b = b, a
        # Clause splits exhaustively into A=0 OR (A=1 AND B=0).
        second = dict(rows)
        ok1, _new1 = add(second, masks[a], 1)
        ok2, _new2 = add(second, masks[b], 0)
        if ok1 and ok2:
            stack.append((second, []))
        first = dict(rows)
        ok, _new = add(first, masks[a], 0)
        if ok:
            stack.append((first, []))
    else:
        if not stack:
            status = 'UNSAT'
    record = {'p': p, 'q': q, 'name': name, 'status': status,
              'primes_le_4p': count, 'initial_free_prime_bits': count-len(fixed),
              'fixed_negative_primes': fixed, 'nodes': nodes,
              'conflicting_leaves': conflicts, 'root_rank': len(root_rows),
              'root_log': root_log}
    if result_rows is not None:
        bits = [0] * count
        for bit in sorted(result_rows):
            mask, rhs = result_rows[bit]
            other = mask ^ (1 << bit)
            for j in range(bit):
                if other & (1 << j):
                    rhs ^= bits[j]
            bits[bit] = rhs
        signs = {r: (-1 if bits[i] else 1) for i, r in enumerate(primes)}
        # Independent evaluation: multiply prime signs with full exponents.
        vals = [1] * (4*p + 1)
        for n in range(1, 4*p + 1):
            for r, k in factors(n).items():
                vals[n] *= signs[r] ** k
        assert all(signs[r] == -1 for r in fixed)
        bad = [a for a, b in pairs if vals[a] == vals[b] == -1]
        assert not bad
        record['negative_primes_le_4p'] = [r for r in primes if signs[r] == -1]
        record['positive_primes_le_4p'] = [r for r in primes if signs[r] == 1]
        record['negative_negative_pairs'] = bad
        record['low_character_discrepancies'] = [
            n for n in range(1, p) if vals[n] != (1 if n in residues else -1)]
        record['low_positive_positive_reflections'] = [
            n for n in range(1, (p+1)//2)
            if vals[n] == vals[p-n] == 1]
        record['q_sign'] = signs[q]
    if status != 'LIMIT':
        root_fixed_prime_signs = {}
        for r in primes:
            m, c = reduce(1 << index[r], root_rows)
            if not m:
                root_fixed_prime_signs[r] = -1 if c else 1
        record['root_fixed_prime_signs'] = root_fixed_prime_signs
    emit(record)
    return status


def main():
    emit({'purpose': 'FSPD arbitrary-sign models, NOT lambda/Q(p)',
          'cases': CASES, 'total_seconds_cap': TOTAL_SECONDS,
          'nodes_cap_per_run': MAX_NODES_PER_RUN,
          'python': platform.python_version(),
          'no_external_sources_or_packages': True})
    for p in CASES:
        if time.monotonic() >= DEADLINE:
            emit({'not_started': p, 'reason': 'global_time_cap'})
            continue
        result = solve(p, lambda q, ps: [r for r in ps if r <= q], 'FSPD')
        if result == 'SAT':
            break
    # Diagnostic for the precise one-sided-to-rigidity gap, not a target search.
    # The character model is allowed here: only f(2)=f(p)=-1 is fixed.
    if time.monotonic() < DEADLINE:
        solve(19, lambda q, ps: [], 'weaker_only_2_and_p_negative')
    emit({'total_elapsed_seconds': time.monotonic()-START})


if __name__ == '__main__':
    main()
