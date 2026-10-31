"""Implementasi SelectionSort untuk pembelajaran analisis algoritma."""
from ..base import SortAlgorithm

class SelectionSort(SortAlgorithm):
    def sort_in_place(self, data):
        for i in range(len(data) - 1):
            smallest = i
            for j in range(i + 1, len(data)):
                if data[j] < data[smallest]:
                    smallest = j
            data[i], data[smallest] = data[smallest], data[i]
