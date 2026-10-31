from typing import Optional, Sequence, Tuple

from code03_complexity.core.experiment import AlgorithmExperiment
from code03_complexity.core.benchmark import Benchmark


class LinearSearchExperiment(AlgorithmExperiment):
    def __init__(self) -> None:
        super().__init__(
            "MODUL 1 — LINEAR SEARCH",
            "Best/average/worst case, basic operation, time O(1)-O(n), space O(1).",
        )

    def search(self, data: Sequence[int], target: int) -> Tuple[int, int]:
        comparisons = 0

        for index, value in enumerate(data):
            comparisons += 1
            if value == target:
                return index, comparisons

        return -1, comparisons

    def run(self, data: Optional[Sequence[int]] = None) -> None:
        self.print_header()

        if not data:
            print("Data tidak tersedia.")
            return

        cases = [
            ("Best case", data[0]),
            ("Approx. average case", data[len(data) // 2]),
            ("Worst case / not found", -999_999_999),
        ]

        print(f"Ukuran input n = {len(data)}\n")

        for label, target in cases:
            result = Benchmark.measure(self.search, data, target, repeat=3)
            index, comparisons = result.result

            print(
                f"{label:26} target={target:<12} index={index:<8} "
                f"comparisons={comparisons:<8} time={result.elapsed_seconds:.8f}s"
            )

        print("\nAnalisis:")
        print("- Basic operation: value == target")
        print("- Best case: O(1)")
        print("- Average case: O(n)")
        print("- Worst case: O(n)")
        print("- Auxiliary space: O(1)")
