from abc import ABC, abstractmethod
from typing import Optional, Sequence


class AlgorithmExperiment(ABC):
    def __init__(self, name: str, description: str) -> None:
        self._name = name
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @abstractmethod
    def run(self, data: Optional[Sequence[int]] = None) -> None:
        raise NotImplementedError

    def print_header(self) -> None:
        print("\n" + "=" * 78)
        print(self.name)
        print(self.description)
        print("=" * 78)
