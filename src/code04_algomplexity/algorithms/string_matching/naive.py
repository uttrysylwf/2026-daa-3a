"""Implementasi NaiveStringMatching untuk pembelajaran analisis algoritma."""
from ..base import StringMatcher

class NaiveStringMatching(StringMatcher):
    def find_all(self, text, pattern):
        n, m = len(text), len(pattern)
        positions = []
        for i in range(n - m + 1):
            j = 0
            while j < m and text[i + j] == pattern[j]:
                j += 1
            if j == m:
                positions.append(i)
        return positions
