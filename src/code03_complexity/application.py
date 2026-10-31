from typing import Dict

from code03_complexity.core.experiment import AlgorithmExperiment
from code03_complexity.services.data_service import DataService
from code03_complexity.experiments import (
    LinearSearchExperiment,
    BinarySearchExperiment,
    DuplicateDetectionExperiment,
    GrowthRateExperiment,
    SpaceComplexityExperiment,
)


class ComplexityLabApplication:
    def __init__(self) -> None:
        self._data_service = DataService(seed=42)
        self._data = []

        self._experiments: Dict[str, AlgorithmExperiment] = {
            "1": LinearSearchExperiment(),
            "2": BinarySearchExperiment(),
            "3": DuplicateDetectionExperiment(),
            "4": GrowthRateExperiment(),
            "5": SpaceComplexityExperiment(),
        }

    def _read_input_size(self) -> int:
        raw = input("Masukkan ukuran input n [default 10000]: ").strip()

        if raw == "":
            return 10_000

        try:
            n = int(raw)
            if n <= 0:
                raise ValueError
            return n
        except ValueError:
            print("Input tidak valid. Digunakan n = 10000.")
            return 10_000

    def _prepare_data(self) -> None:
        n = self._read_input_size()
        self._data = self._data_service.generate_unique_numbers(n)
        print(f"Dataset dibuat: n = {n}")

    def _print_menu(self) -> None:
        print("\n" + "=" * 78)
        print("ALGORITHM COMPLEXITY LAB — OOP")
        print("=" * 78)

        for key, experiment in self._experiments.items():
            print(f"{key}. {experiment.name}")

        print("6. Ganti ukuran dataset")
        print("0. Keluar")

    def run(self) -> None:
        self._prepare_data()

        while True:
            self._print_menu()
            choice = input("Pilih modul: ").strip()

            if choice == "0":
                print("Program selesai.")
                break

            if choice == "6":
                self._prepare_data()
                continue

            experiment = self._experiments.get(choice)

            if experiment is None:
                print("Pilihan tidak valid.")
                continue

            experiment.run(self._data)
