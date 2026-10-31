from typing import Optional, Sequence, Set, Tuple

from code03_complexity.core.experiment import AlgorithmExperiment
from code03_complexity.core.benchmark import Benchmark


class DuplicateDetectionExperiment(AlgorithmExperiment):
    def __init__(self) -> None:
        super().__init__(
            "MODUL 3 — DUPLICATE DETECTION",
            "Perbandingan O(n^2) vs expected O(n) untuk time-space trade-off.",
        )

    def has_duplicate_nested(self, data: Sequence[int]) -> Tuple[bool, int]:
        comparisons = 0

        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                comparisons += 1
                if data[i] == data[j]:
                    return True, comparisons

        return False, comparisons

    def has_duplicate_set(self, data: Sequence[int]) -> Tuple[bool, int, Set[int]]:
        seen: Set[int] = set()
        checks = 0

        for value in data:
            checks += 1
            if value in seen:
                return True, checks, seen
            seen.add(value)

        return False, checks, seen

    def run(self, data: Optional[Sequence[int]] = None) -> None:
        self.print_header()

        if not data:
            print("Data tidak tersedia.")
            return

        sample = list(data[:min(len(data), 4000)])

        if len(sample) >= 2:
            sample[-1] = sample[0]

        nested = Benchmark.measure(self.has_duplicate_nested, sample)
        using_set = Benchmark.measure(self.has_duplicate_set, sample, repeat=3)

        nested_found, nested_cmp = nested.result
        set_found, set_checks, seen = using_set.result

        print(f"Ukuran input uji      : {len(sample)}")

        print("\nNested Loop")
        print(f"Duplicate              : {nested_found}")
        print(f"Comparisons             : {nested_cmp}")
        print(f"Runtime                 : {nested.elapsed_seconds:.8f}s")
        print("Time                    : O(n^2)")
        print("Auxiliary space         : O(1)")

        print("\nSet")
        print(f"Duplicate              : {set_found}")
        print(f"Checks                  : {set_checks}")
        print(f"Runtime                 : {using_set.elapsed_seconds:.8f}s")
        print("Expected time           : O(n)")
        print("Auxiliary space         : O(n)")
        print(f"Shallow set size        : {Benchmark.shallow_size(seen)} bytes")

        print("\nInti konsep: tambahan memori dapat digunakan untuk mengurangi waktu eksekusi.")
