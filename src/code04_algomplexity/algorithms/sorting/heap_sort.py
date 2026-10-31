"""Implementasi HeapSort untuk pembelajaran analisis algoritma."""
from ..base import SortAlgorithm

class HeapSort(SortAlgorithm):
    def sort_in_place(self, data):
        def sift(root, size):
            while 2 * root + 1 < size:
                child = 2 * root + 1
                if child + 1 < size and data[child] < data[child + 1]:
                    child += 1
                if data[root] >= data[child]:
                    break
                data[root], data[child] = data[child], data[root]
                root = child
        for root in range(len(data) // 2 - 1, -1, -1):
            sift(root, len(data))
        for end in range(len(data) - 1, 0, -1):
            data[0], data[end] = data[end], data[0]
            sift(0, end)
