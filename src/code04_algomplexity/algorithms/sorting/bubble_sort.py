"""Implementasi BubbleSort untuk pembelajaran analisis algoritma."""
from ..base import SortAlgorithm

class BubbleSort(SortAlgorithm):
    def sort_in_place(self, data):
        for end in range(len(data) - 1, 0, -1):
            swapped = False
            for j in range(end):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
            if not swapped:
                break
