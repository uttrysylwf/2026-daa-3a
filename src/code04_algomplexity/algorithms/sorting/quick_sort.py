"""Implementasi QuickSort untuk pembelajaran analisis algoritma."""
from ..base import SortAlgorithm

class QuickSort(SortAlgorithm):
    def sort_in_place(self, data):
        # Lomuto: pivot terakhir. Rekursi hanya pada partisi lebih kecil.
        def quick(lo, hi):
            while lo < hi:
                pivot, boundary = data[hi], lo
                for j in range(lo, hi):
                    if data[j] <= pivot:
                        data[boundary], data[j] = data[j], data[boundary]
                        boundary += 1
                data[boundary], data[hi] = data[hi], data[boundary]
                if boundary - lo < hi - boundary:
                    quick(lo, boundary - 1)
                    lo = boundary + 1
                else:
                    quick(boundary + 1, hi)
                    hi = boundary - 1
        quick(0, len(data) - 1)
