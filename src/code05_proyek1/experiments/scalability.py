import time
import tracemalloc
from dataclasses import dataclass
from typing import List, Tuple

from code05_proyek1.services.factory import build_detector


@dataclass
class Measurement:
    scenario: str
    mode: str
    lines: int
    total_chars: int
    comparisons: int
    seconds: float
    peak_kib: float
    max_depth: int

    @property
    def ratio(self) -> float:
        return self.comparisons / self.total_chars


class ScalabilityExperiment:
    """Eksperimen skenario terbaik / terburuk dengan skala input bervariasi.

    Terbaik  : karakter pertama pola TIDAK ada di log -> tiap karakter dibandingkan 1x.
               teks 'B'*L, pola 'A'*m
    Terburuk : teks 'A'*L, pola 'A'*(m-1)+'B' -> KMP ~2 perbandingan/karakter,
               Naive ~m perbandingan/karakter.
    """

    def __init__(self, line_length: int = 200, pattern_length: int = 20, repeats: int = 3) -> None:
        self.line_length = line_length
        self.pattern_length = pattern_length
        self.repeats = repeats

    def _dataset(self, scenario: str, n_lines: int) -> Tuple[List[str], str]:
        L, m = self.line_length, self.pattern_length
        if scenario == "terbaik":
            return ["B" * L] * n_lines, "A" * m
        return ["A" * L] * n_lines, "A" * (m - 1) + "B"

    def measure(self, scenario: str, mode: str, n_lines: int) -> Measurement:
        lines, pattern = self._dataset(scenario, n_lines)

        best = float("inf")
        comparisons = 0
        depth = 0
        for _ in range(self.repeats):                  # waktu: ambil yang tercepat
            detector, counter = build_detector(mode)
            start = time.perf_counter()
            detector.detect(lines, [pattern])
            elapsed = time.perf_counter() - start
            if elapsed < best:
                best = elapsed
            comparisons, depth = counter.comparisons, counter.max_depth

        detector, _ = build_detector(mode)             # memori: lari terpisah
        tracemalloc.start()
        detector.detect(lines, [pattern])
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return Measurement(scenario, mode, n_lines, n_lines * self.line_length,
                           comparisons, best, peak / 1024, depth)

    def run(self, sizes: List[int]) -> List[Measurement]:
        rows: List[Measurement] = []
        for scenario in ("terbaik", "terburuk"):
            for n_lines in sizes:
                for mode in ("iterative", "recursive", "naive"):
                    rows.append(self.measure(scenario, mode, n_lines))
        return rows

    @staticmethod
    def format(rows: List[Measurement]) -> str:
        head = (f"{'Skenario':<9} {'Mode':<10} {'Baris':>6} {'Karakter':>9} {'Perbandingan':>13} "
                f"{'Rasio':>6} {'Waktu(ms)':>10} {'Puncak(KiB)':>12} {'Depth':>6}")
        out = [head, "-" * len(head)]
        for r in rows:
            out.append(f"{r.scenario:<9} {r.mode:<10} {r.lines:>6} {r.total_chars:>9} {r.comparisons:>13} "
                       f"{r.ratio:>6.2f} {r.seconds * 1000:>10.2f} {r.peak_kib:>12.1f} {r.max_depth:>6}")
        return "\n".join(out)
