from typing import List, Optional, Sequence, Tuple

from code03_complexity.core.experiment import AlgorithmExperiment
from code03_complexity.core.benchmark import Benchmark


class SpaceComplexityExperiment(AlgorithmExperiment):
    def __init__(self) -> None:
        super().__init__(
            "MODUL 5 — SPACE COMPLEXITY",
            "Time complexity sama, auxiliary space berbeda.",
        )

    def sum_in_place(self, data: Sequence[int]) -> int:
        total = 0
        for value in data:
            total += value
        return total

    def sum_with_copy(self, data: Sequence[int]) -> Tuple[int, List[int]]:
        copied = list(data)
        total = 0
        for value in copied:
            total += value
        return total, copied

    def run(self, data: Optional[Sequence[int]] = None) -> None:
        self.print_header()

        if not data:
            print("Data tidak tersedia.")
            return

        in_place = Benchmark.measure(self.sum_in_place, data, repeat=3)
        copied_version = Benchmark.measure(self.sum_with_copy, data, repeat=3)

        total_copy, copied = copied_version.result

        print(f"Ukuran input n        : {len(data)}")

        print("\nIn-place")
        print(f"Total                  : {in_place.result}")
        print(f"Runtime                : {in_place.elapsed_seconds:.8f}s")
        print("Time                    : O(n)")
        print("Auxiliary space         : O(1)")

        print("\nDengan Copy")
        print(f"Total                  : {total_copy}")
        print(f"Runtime                : {copied_version.elapsed_seconds:.8f}s")
        print("Time                    : O(n)")
        print("Auxiliary space         : O(n)")
        print(f"Shallow copy size       : {Benchmark.shallow_size(copied)} bytes")
