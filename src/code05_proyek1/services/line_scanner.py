from abc import ABC, abstractmethod
from typing import List

from code05_proyek1.algorithms.base import StringMatcher


class LineScanner(ABC):
    """Memindai seluruh baris log untuk satu pola; mengembalikan nomor baris (mulai 1)
    yang memuat pola, terurut naik."""

    def __init__(self, matcher: StringMatcher) -> None:
        self.matcher = matcher

    @abstractmethod
    def scan(self, lines: List[str], pattern: str, table: List[int]) -> List[int]:
        ...


class IterativeLineScanner(LineScanner):
    """Satu kali jalan dengan for-loop. Waktu O(N·L) (N baris, L panjang rata-rata), ruang O(hasil)."""

    def scan(self, lines: List[str], pattern: str, table: List[int]) -> List[int]:
        found: List[int] = []
        for number, line in enumerate(lines, start=1):
            if self.matcher.first_match(line, pattern, table) != -1:
                found.append(number)
        return found


class RecursiveLineScanner(LineScanner):
    """Divide & conquer: pindai separuh kiri, separuh kanan, lalu gabungkan.
    Waktu O(N·L), ruang stack O(log N) + O(hasil)."""

    def scan(self, lines: List[str], pattern: str, table: List[int]) -> List[int]:
        return self._scan(lines, pattern, table, 0, len(lines), 1)

    def _scan(self, lines: List[str], pattern: str, table: List[int], lo: int, hi: int, depth: int) -> List[int]:
        self.matcher.counter.note_depth(depth)
        if hi - lo == 0:
            return []
        if hi - lo == 1:                              # basis: satu baris
            if self.matcher.first_match(lines[lo], pattern, table) != -1:
                return [lo + 1]
            return []
        mid = (lo + hi) // 2
        left = self._scan(lines, pattern, table, lo, mid, depth + 1)
        right = self._scan(lines, pattern, table, mid, hi, depth + 1)
        return left + right
