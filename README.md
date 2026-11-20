# The normalized number of zero signed sums ±1±2±…±n increases from n=16

Let S_n = ε_1 + 2ε_2 + … + nε_n with independent fair signs, and Q_n = 1² + … + n². Along n ≡ 0, 3 (mod 4) the
sequence √Q_n P(S_n = 0) tends to √(2/π) (Sullivan, 2013). The paper proves that it increases strictly from n = 16,
with decreases only at 3→4, 8→11 and 15→16, and gives the same classification when each summand is repeated m times
(four decreases for m = 2, one for m = 3, none for m ≥ 4).

Files:

- `main.tex`, `main.pdf`: the paper.
- `check_polynomial.py`: decides the 1268 comparisons with mn < 320 by multiplying out the generating polynomial,
  checks the rational identities and the numerical inequality used in the proof, and prints the values in the
  closing remark. Output in `check_polynomial.out`.
- `check_signed_walk.py`: decides the same comparisons by counting signed sums. Output in `check_signed_walk.out`.

Both programs use only the Python standard library: `python check_polynomial.py` and `python check_signed_walk.py`.

License: CC BY 4.0.
