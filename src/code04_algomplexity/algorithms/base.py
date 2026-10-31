"""Kontrak OOP untuk tiga keluarga algoritma."""
from abc import ABC, abstractmethod
from typing import Sequence, TypeVar
T = TypeVar('T')

class SearchAlgorithm(ABC):
    @abstractmethod
    def search(self, data: Sequence[T], target: T) -> int:
        """Kembalikan indeks kemunculan pertama, atau -1."""

class SortAlgorithm(ABC):
    def sort(self, data: Sequence[T]) -> list[T]:
        """Salin input agar data pemanggil tidak berubah."""
        result = list(data)
        self.sort_in_place(result)
        return result

    @abstractmethod
    def sort_in_place(self, data: list[T]) -> None:
        """Urutkan list secara menaik dengan operator perbandingan."""

class StringMatcher(ABC):
    @abstractmethod
    def find_all(self, text: str, pattern: str) -> list[int]:
        """Temukan semua posisi termasuk overlap; pattern kosong cocok di setiap batas."""
