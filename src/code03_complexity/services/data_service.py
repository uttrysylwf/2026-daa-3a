import random
from typing import List


class DataService:
    def __init__(self, seed: int = 42) -> None:
        self._seed = seed

    def generate_unique_numbers(self, n: int) -> List[int]:
        rng = random.Random(self._seed)
        data = list(range(n))
        rng.shuffle(data)
        return data
