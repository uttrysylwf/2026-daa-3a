from typing import Tuple

from code05_proyek1.algorithms import (
    IterativeKMP,
    RecursiveKMP,
    NaiveMatcher,
    IterativeMergeSort,
    RecursiveMergeSort,
)
from code05_proyek1.core.counter import OperationCounter
from code05_proyek1.services.anomaly_detector import AnomalyDetector
from code05_proyek1.services.line_scanner import IterativeLineScanner, RecursiveLineScanner

MODES = ("iterative", "recursive", "naive")


def build_detector(mode: str) -> Tuple[AnomalyDetector, OperationCounter]:
    """Rakit detektor lengkap untuk satu mode. Mengembalikan (detektor, counter)."""
    counter = OperationCounter()
    if mode == "iterative":
        matcher = IterativeKMP(counter)
        return AnomalyDetector(matcher, IterativeLineScanner(matcher), IterativeMergeSort(counter)), counter
    if mode == "recursive":
        matcher = RecursiveKMP(counter)
        return AnomalyDetector(matcher, RecursiveLineScanner(matcher), RecursiveMergeSort(counter)), counter
    if mode == "naive":
        matcher = NaiveMatcher(counter)
        return AnomalyDetector(matcher, IterativeLineScanner(matcher), IterativeMergeSort(counter)), counter
    raise ValueError(f"Mode tidak dikenal: {mode!r}. Pilihan: {MODES}")
