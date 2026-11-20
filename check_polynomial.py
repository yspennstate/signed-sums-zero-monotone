"""Finite comparisons of the note by multiplying out prod_j (1+x^j)^m, plus the rational identities and the
numerical inequality used for mn >= 320. Standard library only."""
from fractions import Fraction
from math import pi


def variance(n):
    return n * (n + 1) * (2 * n + 1) // 6


def central_counts(m, last):
    # Coefficients are packed in base 2^width; every coefficient is below 2^(m*last), so no carries occur.
    width = m * last + 1
    mask = (1 << width) - 1
    polynomial = 1
    for n in range(1, last + 1):
        for _ in range(m):
            polynomial += polynomial << (width * n)
        total = m * n * (n + 1) // 2
        if total % 2 == 0:
            yield n, (polynomial >> (width * (total // 2))) & mask


tested, exceptions = 0, []
for m in range(1, 320):
    prev = None
    for n, c in central_counts(m, 319 // m + 3):
        if prev:
            a, old = prev
            if m * a < 320:
                gap = variance(n) * c ** 2 - (variance(a) * old ** 2 << (2 * m * (n - a)))
                tested += 1
                if gap <= 0:
                    exceptions.append((m, a, n, 'decrease' if gap < 0 else 'tie'))
        prev = n, c
        if m == 1 and n in (16, 100, 300):
            r = 6 * (3 * n * n + 3 * n - 1) / (5 * n * (n + 1) * (2 * n + 1))
            print(f'A_(1,{n}) = {variance(n) ** 0.5 * c / 2 ** n:.6f}; two-term value {(2 / pi) ** 0.5 * (1 - r / 4):.6f}')
print('comparisons with mn < 320:', tested)
print('non-increasing steps (m, n, a):', exceptions)

for n in range(1, 301):
    def r(k):
        return Fraction(sum(i ** 4 for i in range(1, k + 1)), variance(k) ** 2)
    assert r(n) == Fraction(6 * (3 * n * n + 3 * n - 1), 5 * n * (n + 1) * (2 * n + 1))
    gap = r(n) - r(n + 1)
    assert gap == Fraction(36 * (n * n + 2 * n - 1), 5 * n * (n + 2) * (2 * n + 1) * (2 * n + 3))
    assert gap > Fraction(1, 4 * n * n)
print('identities for r_n and r_n - r_(n+1) > 1/(4n^2): checked for n <= 300 (rational functions of bounded degree)')
lhs = 216 * 4 * 81 * 320 ** 4
assert lhs < 74 * 10 ** 13 and Fraction(8, 3) ** 40 > 10 ** 17
print('216*4*81*320^4 =', lhs, '< 7.4e14; (8/3)^40 > 1e17')
