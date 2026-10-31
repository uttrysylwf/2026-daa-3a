import argparse
from pathlib import Path
from typing import List, Optional

from code05_proyek1.experiments import ScalabilityExperiment
from code05_proyek1.services import LogReader, ReportFormatter, build_detector

DATASET = Path(__file__).resolve().parent / "dataset" / "case5_server_access.txt"

PRESETS = {
    # pola persis seperti contoh pada lembar asesmen
    "docx": [
        "POST /healthcheck",
        "X11; Linux x86_64; rv:130.0",
        "340.213.18.221:2816",
    ],
    # signature serangan yang memang ada pada dataset
    "attack": [
        "UNION%20SELECT",
        "<script>alert('XSS')</script>",
        "../../../../etc/passwd",
        "340.213.18.221:2816",
    ],
}


class AnomalyApplication:
    def __init__(self) -> None:
        self._formatter = ReportFormatter()

    @staticmethod
    def _parser() -> argparse.ArgumentParser:
        p = argparse.ArgumentParser(description="Kasus E - Deduplikasi Log Server & Anomali Siber (KMP + Merge Sort)")
        p.add_argument("--mode", choices=["iterative", "recursive", "both"], default="both",
                       help="pendekatan yang dijalankan (default: both)")
        p.add_argument("--preset", choices=list(PRESETS), default="docx", help="kumpulan pola bawaan")
        p.add_argument("--patterns", nargs="+", help="pola sendiri (menggantikan preset)")
        p.add_argument("--file", type=Path, default=DATASET, help="berkas log (default: dataset kasus 5)")
        p.add_argument("--experiment", action="store_true", help="jalankan eksperimen skenario terbaik/terburuk")
        return p

    def _detect(self, mode: str, lines: List[str], patterns: List[str]) -> None:
        detector, counter = build_detector(mode)
        results = detector.detect(lines, patterns)
        print(f"##### MODE: {mode.upper()} #####")
        print(self._formatter.format(results, counter.comparisons))
        print(f"- Perbandingan elemen saat Merge Sort: {detector.sorter.element_comparisons}")
        print(f"- Kedalaman rekursi maksimum: {counter.max_depth}")
        print()

    def run(self, argv: Optional[List[str]] = None) -> None:
        args = self._parser().parse_args(argv)

        if args.experiment:
            print("=== EKSPERIMEN KOMPLEKSITAS (pola k=1, panjang baris 200, panjang pola 20) ===")
            experiment = ScalabilityExperiment()
            print(experiment.format(experiment.run([250, 500, 1000, 2000])))
            return

        lines = LogReader.read_lines(args.file)
        patterns = args.patterns if args.patterns else PRESETS[args.preset]
        print(f"Berkas: {args.file.name} | jumlah baris log: {len(lines)} | jumlah pola k = {len(patterns)}\n")

        modes = ["iterative", "recursive"] if args.mode == "both" else [args.mode]
        for mode in modes:
            self._detect(mode, lines, patterns)
