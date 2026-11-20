"""Second, independent computation of the finite comparisons: count the sign patterns of
S_{m,n} = sum_j j (eps_{j1} + ... + eps_{jm}) step by step on the integers, then compare
Q_a C_a^2 with 4^{m(a-n)} Q_n C_n^2 for consecutive admissible n < a with m n < 320. Standard library only."""


def Q(n):
    return n * (n + 1) * (2 * n + 1) // 6


def zero_counts(m, nmax):
    off = m * nmax * (nmax + 1) // 2
    dist = [0] * (2 * off + 1)
    dist[off] = 1
    lo = hi = off
    for n in range(1, nmax + 1):
        for _ in range(m):
            new = [0] * (2 * off + 1)
            for s in range(lo, hi + 1):
                c = dist[s]
                if c:
                    new[s - n] += c
                    new[s + n] += c
            dist = new
            lo -= n
            hi += n
        if (m * n * (n + 1) // 2) % 2 == 0:
            yield n, dist[off]


tested, exceptions = 0, []
for m in range(1, 320):
    rows = list(zero_counts(m, 319 // m + 3))
    for (a, ca), (b, cb) in zip(rows, rows[1:]):
        if m * a < 320:
            gap = Q(b) * cb * cb - Q(a) * ca * ca * 4 ** (m * (b - a))
            tested += 1
            if gap <= 0:
                exceptions.append((m, a, b, 'decrease' if gap < 0 else 'tie'))
print('comparisons with mn < 320:', tested)
print('non-increasing steps (m, n, a):', exceptions)
