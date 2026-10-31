from time import perf_counter
from code06_typos.levenshtein import Levenshtein

class TypoValidator:
    """Memvalidasi kata dan mencari tiga kandidat koreksi."""
    def __init__(self, dictionary_manager):
        self.dictionary = dictionary_manager

    def validate(self, word, top_n=3):
        word = word.strip().lower()
        if not word:
            raise ValueError("Kata tidak boleh kosong.")
        start = perf_counter()
        valid = self.dictionary.binary_search(word)
        lookup_ms = (perf_counter() - start) * 1000
        if valid:
            return {"word": word, "valid": True, "lookup_ms": lookup_ms,
                    "suggestion_ms": 0.0, "candidates": []}

        start = perf_counter()
        scored = [(Levenshtein.distance(word, candidate), candidate)
                  for candidate in self.dictionary.words]
        scored.sort(key=lambda item: (item[0], item[1]))
        suggestion_ms = (perf_counter() - start) * 1000
        return {"word": word, "valid": False, "lookup_ms": lookup_ms,
                "suggestion_ms": suggestion_ms,
                "candidates": [{"word": w, "distance": d}
                               for d, w in scored[:top_n]]}
