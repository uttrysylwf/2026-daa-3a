"""Implementasi BoyerMoore untuk pembelajaran analisis algoritma."""
from ..base import StringMatcher

class BoyerMoore(StringMatcher):
    def find_all(self, text, pattern):
        # Varian dasar bad-character, tanpa good-suffix/Galil.
        n, m = len(text), len(pattern)
        if not m:
            return list(range(n + 1))
        last = {char: i for i, char in enumerate(pattern)}
        positions, shift = [], 0
        while shift <= n - m:
            j = m - 1
            while j >= 0 and pattern[j] == text[shift + j]:
                j -= 1
            if j < 0:
                positions.append(shift)
                shift += (m - last.get(text[shift + m], -1)
                          if shift + m < n else 1)
            else:
                shift += max(1, j - last.get(text[shift + j], -1))
        return positions
