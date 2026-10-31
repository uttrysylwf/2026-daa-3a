from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class PatternResult:
    """Hasil pemindaian satu pola anomali pada seluruh log.

    line_numbers berisi nomor baris (mulai dari 1) yang memuat pola.
    Frekuensi = jumlah baris log yang memuat pola (satu baris dihitung sekali).
    """

    pattern: str
    line_numbers: List[int] = field(default_factory=list)

    @property
    def frequency(self) -> int:
        return len(self.line_numbers)

    @property
    def first_line(self) -> Optional[int]:
        if not self.line_numbers:
            return None
        return self.line_numbers[0]
