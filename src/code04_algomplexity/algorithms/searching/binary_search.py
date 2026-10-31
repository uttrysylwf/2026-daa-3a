"""Implementasi BinarySearch untuk pembelajaran analisis algoritma."""
from ..base import SearchAlgorithm

class BinarySearch(SearchAlgorithm):
    def search(self, data, target):
        # Prasyarat: data sudah terurut menaik. Cari batas kiri target.
        low, high = 0, len(data)
        while low < high:
            mid = (low + high) // 2
            if data[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low if low < len(data) and data[low] == target else -1
