from dataclasses import dataclass
from time import perf_counter
from typing import Any, Callable
import sys


@dataclass
class BenchmarkResult:
    result: Any
    elapsed_seconds: float


class Benchmark:
    @staticmethod
    def measure(func: Callable[..., Any], *args: Any, repeat: int = 1, **kwargs: Any) -> BenchmarkResult:
        best_time = float("inf")
        final_result = None

        for _ in range(repeat):
            start = perf_counter()
            final_result = func(*args, **kwargs)
            elapsed = perf_counter() - start
            best_time = min(best_time, elapsed)

        return BenchmarkResult(final_result, best_time)

    @staticmethod
    def shallow_size(obj: Any) -> int:
        return sys.getsizeof(obj)
