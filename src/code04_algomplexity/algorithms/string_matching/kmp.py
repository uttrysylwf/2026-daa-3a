"""Implementasi KMP untuk pembelajaran analisis algoritma."""
from ..base import StringMatcher

class KMP(StringMatcher):
    def find_all(self, text, pattern):
        if not pattern:
            return list(range(len(text) + 1))
        lps = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        positions, j = [], 0
        for i, char in enumerate(text):
            while j and char != pattern[j]:
                j = lps[j - 1]
            if char == pattern[j]:
                j += 1
            if j == len(pattern):
                positions.append(i - j + 1)
                j = lps[j - 1]
        return positions
