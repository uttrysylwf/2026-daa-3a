class OperationCounter:
    """Pencatat operasi dasar untuk pengukuran empiris.

    comparisons : jumlah perbandingan karakter (operasi dasar KMP / Naive)
    max_depth   : kedalaman rekursi terbesar yang pernah dicapai
    """

    def __init__(self) -> None:
        self.comparisons = 0
        self.max_depth = 0

    def reset(self) -> None:
        self.comparisons = 0
        self.max_depth = 0

    def compare(self) -> None:
        self.comparisons += 1

    def note_depth(self, depth: int) -> None:
        if depth > self.max_depth:
            self.max_depth = depth
