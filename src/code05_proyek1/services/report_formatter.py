from typing import List

from code05_proyek1.models.pattern_result import PatternResult


class ReportFormatter:
    """Menyusun laporan teks sesuai format pada lembar asesmen."""

    TITLE = "=== LAPORAN ANOMALI LOG SERVER (TERURUT DARI PALING LANGKA) ==="

    def format(self, results: List[PatternResult], operations: int) -> str:
        out: List[str] = [self.TITLE, ""]
        for rank, item in enumerate(results, start=1):
            first = "-" if item.first_line is None else str(item.first_line)
            out.append(f'{rank}. Pola: "{item.pattern}"')
            out.append(f"   Indeks Pertama: {first}")
            out.append(f"   Frekuensi: {item.frequency}")
            out.append("")
        out.append("Metrik Eksekusi:")
        out.append(f"- Total Operasi Dasar (Perbandingan Karakter): {operations} operasi")
        return "\n".join(out)
