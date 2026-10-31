"""Implementasi InsertionSort untuk pembelajaran analisis algoritma."""
from ..base import SortAlgorithm

class InsertionSort(SortAlgorithm):
    def sort_in_place(self, data):
        for i in range(1, len(data)):
            key, j = data[i], i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
