from math import log2
from typing import Optional, Sequence

from code03_complexity.core.experiment import AlgorithmExperiment


class GrowthRateExperiment(AlgorithmExperiment):
    def __init__(self) -> None:
        super().__init__(
            "MODUL 4 — GROWTH RATE & SCALABILITY",
            "Perbandingan O(1), O(log n), O(n), O(n log n), dan O(n^2).",
        )

    def run(self, data: Optional[Sequence[int]] = None) -> None:
        self.print_header()

        sizes = [10, 100, 1_000, 10_000, 100_000]

        print(
            f"{'n':>10}{'1':>10}{'log2(n)':>14}"
            f"{'n':>14}{'n log n':>18}{'n^2':>20}"
        )

        for n in sizes:
            print(
                f"{n:>10}{1:>10}{log2(n):>14.2f}"
                f"{n:>14}{n * log2(n):>18.2f}{n*n:>20}"
            )

        print("\nAnalisis:")
        print("- Growth rate menjelaskan perubahan biaya saat n membesar.")
        print("- O(n^2) lebih cepat kehilangan skalabilitas dibanding O(n).")
