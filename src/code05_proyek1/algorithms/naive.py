from typing import List

from code05_proyek1.algorithms.base import StringMatcher


class NaiveMatcher(StringMatcher):
    """Brute-force (solusi 'kurang tepat'); hanya dipakai sebagai pembanding eksperimen.
    Waktu O(n*m), ruang O(1)."""

    def prepare(self, pattern: str) -> List[int]:
        self._validate(pattern)
        return []

    def first_match(self, text: str, pattern: str, table: List[int]) -> int:
        self._validate(pattern)
        n, m = len(text), len(pattern)
        start = 0
        while start + m <= n:
            j = 0
            while j < m:
                self.counter.compare()
                if text[start + j] != pattern[j]:
                    break
                j += 1
            if j == m:
                return start
            start += 1
        return -1
