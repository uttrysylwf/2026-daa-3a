"""Indeks hash yang bisa dipakai ulang untuk beberapa pencarian."""
from ..base import SearchAlgorithm

class HashTableIndex:
    def __init__(self, data):
        self._positions = {}
        for i, value in enumerate(data):
            self._positions.setdefault(value, i)

    def search(self, target):
        return self._positions.get(target, -1)

class HashTableSearch(SearchAlgorithm):
    def build_index(self, data):
        return HashTableIndex(data)

    def search(self, data, target):
        # One-shot mencakup biaya pembangunan O(n).
        return self.build_index(data).search(target)
