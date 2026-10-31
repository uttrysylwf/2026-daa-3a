"""Implementasi MergeSort untuk pembelajaran analisis algoritma."""
from ..base import SortAlgorithm

class MergeSort(SortAlgorithm):
    def sort_in_place(self, data):
        buffer = [None] * len(data)
        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return
            mid = (lo + hi) // 2
            merge_sort(lo, mid)
            merge_sort(mid, hi)
            i, j = lo, mid
            for k in range(lo, hi):
                if i < mid and (j >= hi or data[i] <= data[j]):
                    buffer[k] = data[i]
                    i += 1
                else:
                    buffer[k] = data[j]
                    j += 1
            for k in range(lo, hi):
                data[k] = buffer[k]
        merge_sort(0, len(data))
