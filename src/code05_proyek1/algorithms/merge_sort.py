import sys
from abc import ABC, abstractmethod
from typing import Callable, List, Sequence, TypeVar

from code05_proyek1.core.counter import OperationCounter

T = TypeVar("T")
Precedes = Callable[[T, T], bool]   # precedes(a, b) True bila a harus SEBELUM b (ketat)


class MergeSort(ABC):
    """Merge Sort stabil. Waktu Θ(n log n), ruang O(n) (+ O(log n) stack pada versi rekursif).
    Tidak memakai sorted() / list.sort()."""

    def __init__(self, counter: OperationCounter) -> None:
        self.counter = counter
        self.element_comparisons = 0

    @abstractmethod
    def sort(self, items: Sequence[T], precedes: Precedes) -> List[T]:
        ...

    def _merge(self, src: List[T], dst: List[T], lo: int, mid: int, hi: int, precedes: Precedes) -> None:
        """Gabungkan src[lo:mid] dan src[mid:hi] (masing-masing terurut) ke dst[lo:hi]."""
        i, j, k = lo, mid, lo
        while i < mid and j < hi:
            self.element_comparisons += 1
            if precedes(src[j], src[i]):      # kanan hanya diambil bila STRICT lebih dulu -> stabil
                dst[k] = src[j]
                j += 1
            else:
                dst[k] = src[i]
                i += 1
            k += 1
        while i < mid:
            dst[k] = src[i]
            i += 1
            k += 1
        while j < hi:
            dst[k] = src[j]
            j += 1
            k += 1


class IterativeMergeSort(MergeSort):
    """Bottom-up: lebar blok 1, 2, 4, ... sampai >= n."""

    def sort(self, items: Sequence[T], precedes: Precedes) -> List[T]:
        n = len(items)
        src: List[T] = list(items)
        dst: List[T] = list(items)
        width = 1
        while width < n:                              # termination: width berlipat dua
            lo = 0
            while lo < n:
                mid = min(lo + width, n)
                hi = min(lo + 2 * width, n)
                self._merge(src, dst, lo, mid, hi, precedes)
                lo += 2 * width
            src, dst = dst, src
            width *= 2
        return src


class RecursiveMergeSort(MergeSort):
    """Top-down: bagi dua, urutkan tiap bagian secara rekursif, lalu gabungkan."""

    def sort(self, items: Sequence[T], precedes: Precedes) -> List[T]:
        data: List[T] = list(items)
        buffer: List[T] = list(items)
        needed = 4 * len(items).bit_length() + 100
        if sys.getrecursionlimit() < needed:
            sys.setrecursionlimit(needed)
        self._sort(data, buffer, 0, len(data), precedes, 1)
        return data

    def _sort(self, data: List[T], buffer: List[T], lo: int, hi: int, precedes: Precedes, depth: int) -> None:
        self.counter.note_depth(depth)
        if hi - lo < 2:                               # basis
            return
        mid = (lo + hi) // 2
        self._sort(data, buffer, lo, mid, precedes, depth + 1)
        self._sort(data, buffer, mid, hi, precedes, depth + 1)
        self._merge(data, buffer, lo, mid, hi, precedes)
        for t in range(lo, hi):
            data[t] = buffer[t]
