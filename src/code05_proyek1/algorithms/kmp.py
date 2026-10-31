import sys
from typing import List

from code05_proyek1.algorithms.base import StringMatcher


class IterativeKMP(StringMatcher):
    """KMP non-rekursif (while-loop). Waktu O(n + m), ruang O(m)."""

    def prepare(self, pattern: str) -> List[int]:
        self._validate(pattern)
        m = len(pattern)
        table = [0] * m
        length = 0   # panjang prefix-sufiks terpanjang sejauh ini
        i = 1
        while i < m:                                  # termination: 2i - length naik
            self.counter.compare()
            if pattern[i] == pattern[length]:
                length += 1
                table[i] = length
                i += 1
            elif length != 0:
                length = table[length - 1]            # fallback, i tidak maju
            else:
                table[i] = 0
                i += 1
        return table

    def first_match(self, text: str, pattern: str, table: List[int]) -> int:
        self._validate(pattern)
        n, m = len(text), len(pattern)
        i = 0   # indeks teks
        j = 0   # jumlah karakter pola yang sudah cocok
        while i < n:                                  # termination: 2i - j naik
            self.counter.compare()
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == m:
                    return i - m
            elif j != 0:
                j = table[j - 1]
            else:
                i += 1
        return -1


class RecursiveKMP(StringMatcher):
    """KMP rekursif (tail recursion). Waktu O(n + m), ruang O(n + m) karena stack."""

    @staticmethod
    def _ensure_recursion_limit(needed: int) -> None:
        if sys.getrecursionlimit() < needed:
            sys.setrecursionlimit(needed)

    def prepare(self, pattern: str) -> List[int]:
        self._validate(pattern)
        m = len(pattern)
        table = [0] * m
        self._ensure_recursion_limit(2 * m + 100)
        self._build(pattern, table, 1, 0, 1)
        return table

    def _build(self, pattern: str, table: List[int], i: int, length: int, depth: int) -> None:
        self.counter.note_depth(depth)
        if i >= len(pattern):                         # basis
            return
        self.counter.compare()
        if pattern[i] == pattern[length]:
            table[i] = length + 1
            self._build(pattern, table, i + 1, length + 1, depth + 1)
        elif length != 0:
            self._build(pattern, table, i, table[length - 1], depth + 1)
        else:
            table[i] = 0
            self._build(pattern, table, i + 1, 0, depth + 1)

    def first_match(self, text: str, pattern: str, table: List[int]) -> int:
        self._validate(pattern)
        self._ensure_recursion_limit(2 * len(text) + 100)
        return self._search(text, pattern, table, 0, 0, 1)

    def _search(self, text: str, pattern: str, table: List[int], i: int, j: int, depth: int) -> int:
        self.counter.note_depth(depth)
        if j == len(pattern):                         # basis 1: seluruh pola cocok
            return i - j
        if i >= len(text):                            # basis 2: teks habis
            return -1
        self.counter.compare()
        if text[i] == pattern[j]:
            return self._search(text, pattern, table, i + 1, j + 1, depth + 1)
        if j != 0:
            return self._search(text, pattern, table, i, table[j - 1], depth + 1)
        return self._search(text, pattern, table, i + 1, 0, depth + 1)
