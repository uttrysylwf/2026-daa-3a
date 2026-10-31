from typing import List, Sequence

from code05_proyek1.algorithms.base import StringMatcher
from code05_proyek1.algorithms.merge_sort import MergeSort
from code05_proyek1.models.pattern_result import PatternResult
from code05_proyek1.services.line_scanner import LineScanner


def rarest_first(a: PatternResult, b: PatternResult) -> bool:
    """True bila a harus tampil SEBELUM b.

    Urutan: frekuensi terkecil di atas (anomali paling langka); pola yang tidak
    ditemukan (frekuensi 0) ditaruh paling bawah; seri dipecah oleh baris pertama.
    """
    a_zero = a.frequency == 0
    b_zero = b.frequency == 0
    if a_zero != b_zero:
        return b_zero
    if a_zero:
        return False
    if a.frequency != b.frequency:
        return a.frequency < b.frequency
    return a.line_numbers[0] < b.line_numbers[0]


class AnomalyDetector:
    """Orkestrasi: prepare pola -> pindai log -> kelompokkan -> urutkan."""

    def __init__(self, matcher: StringMatcher, scanner: LineScanner, sorter: MergeSort) -> None:
        self.matcher = matcher
        self.scanner = scanner
        self.sorter = sorter

    def detect(self, lines: List[str], patterns: Sequence[str]) -> List[PatternResult]:
        results: List[PatternResult] = []
        for pattern in patterns:
            table = self.matcher.prepare(pattern)                    # Proses 1
            numbers = self.scanner.scan(lines, pattern, table)       # Proses 2 + 3
            results.append(PatternResult(pattern=pattern, line_numbers=numbers))
        return self.sorter.sort(results, rarest_first)               # Proses 4
