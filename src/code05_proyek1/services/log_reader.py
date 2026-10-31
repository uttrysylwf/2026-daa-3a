from pathlib import Path
from typing import List


class LogReader:
    """Membaca berkas log dan memecahnya menjadi baris (pemisah: karakter newline)."""

    @staticmethod
    def read_lines(path: Path) -> List[str]:
        text = Path(path).read_text(encoding="utf-8")
        lines = text.split("\n")
        if len(lines) > 0 and lines[-1] == "":        # newline penutup bukan baris log
            lines.pop()
        return [line.rstrip("\r") for line in lines]
