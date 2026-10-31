from pathlib import Path
from time import perf_counter

class DictionaryManager:
    """Membaca kamus dan menyediakan algoritma pencarian."""
    def __init__(self, path):
        self.path = Path(path)
        self.words = []

    def load(self):
        if not self.path.exists():
            raise FileNotFoundError(f"File kamus tidak ditemukan: {self.path}")
        with self.path.open(encoding="utf-8") as f:
            self.words = sorted({line.strip().lower() for line in f if line.strip()})
        if not self.words:
            raise ValueError("Kamus kosong.")
        return self.words

    def linear_search(self, target):
        target = target.lower()
        for word in self.words:
            if word == target:
                return True
        return False

    def binary_search(self, target):
        target = target.lower()
        left, right = 0, len(self.words) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.words[mid] == target:
                return True
            if self.words[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def benchmark(self, target, repetitions=1000):
        results = {}
        for name, method in (("Linear Search", self.linear_search),
                             ("Binary Search", self.binary_search)):
            start = perf_counter()
            for _ in range(repetitions):
                method(target)
            elapsed = perf_counter() - start
            results[name] = (elapsed * 1000, elapsed * 1000 / repetitions)
        return results
