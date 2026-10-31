"""Implementasi LinearSearch untuk pembelajaran analisis algoritma."""
from ..base import SearchAlgorithm

class LinearSearch(SearchAlgorithm):
    def search(self, data, target):
        for i, value in enumerate(data):
            if value == target:
                return i
        return -1
