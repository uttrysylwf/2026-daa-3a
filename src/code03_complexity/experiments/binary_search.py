from typing import Optional, Sequence, Tuple

from code03_complexity.core.experiment import AlgorithmExperiment
from code03_complexity.core.benchmark import Benchmark


class BinarySearchExperiment(AlgorithmExperiment):
    def __init__(self) -> None:
        super().__init__(
            "MODUL 2 — SORTING + BINARY SEARCH",
            "Preprocessing, O(n log n), O(log n), dan keuntungan pencarian berulang.",
        )

    def binary_search(self, data: Sequence[int], target: int) -> Tuple[int, int]:
        low = 0
        high = len(data) - 1
        comparisons = 0

        while low <= high:
            comparisons += 1
            mid = (low + high) // 2

            if data[mid] == target:
                return mid, comparisons
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1, comparisons

    def run(self, data: Optional[Sequence[int]] = None) -> None:
        self.print_header()

        if not data:
            print("Data tidak tersedia.")
            return

        target = data[len(data) // 2]

        sorting = Benchmark.measure(sorted, data, repeat=3)
        searching = Benchmark.measure(
            self.binary_search, sorting.result, target, repeat=3
        )

        index, comparisons = searching.result

        print(f"Ukuran input n       : {len(data)}")
        print(f"Waktu sorting         : {sorting.elapsed_seconds:.8f}s")
        print(f"Waktu binary search   : {searching.elapsed_seconds:.8f}s")
        print(f"Comparisons            : {comparisons}")
        print(f"Index                  : {index}")

        print("\nAnalisis:")
        print("- Sorting: O(n log n) worst-case")
        print("- Binary Search: O(log n)")
        print("- Iterative Binary Search: auxiliary space O(1)")
        print("- Preprocessing dapat menguntungkan untuk pencarian berulang.")
