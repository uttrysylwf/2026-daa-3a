from abc import ABC, abstractmethod
from typing import List

from code05_proyek1.core.counter import OperationCounter


class StringMatcher(ABC):
    """Kontrak pencocok string: cari kemunculan PERTAMA pola pada satu teks.

    prepare()     -> praproses pola (mis. tabel failure KMP), dilakukan 1x per pola
    first_match() -> indeks kemunculan pertama, atau -1 bila tidak ada
    """

    def __init__(self, counter: OperationCounter) -> None:
        self.counter = counter

    @staticmethod
    def _validate(pattern: str) -> None:
        if len(pattern) == 0:
            raise ValueError("Pola tidak boleh kosong.")

    @abstractmethod
    def prepare(self, pattern: str) -> List[int]:
        ...

    @abstractmethod
    def first_match(self, text: str, pattern: str, table: List[int]) -> int:
        ...
