class PerformanceAnalyzer:
    """Menampilkan perbandingan waktu Linear Search dan Binary Search."""
    def __init__(self, dictionary_manager):
        self.dictionary = dictionary_manager

    def compare(self, target, repetitions=1000):
        results = self.dictionary.benchmark(target, repetitions)
        print(f"\nBenchmark untuk {target!r} ({repetitions} pengulangan)")
        print(f"{'Algoritma':<18}{'Total (ms)':>14}{'Rata-rata (ms)':>20}")
        print("-" * 52)
        for name, (total, average) in results.items():
            print(f"{name:<18}{total:>14.4f}{average:>20.6f}")
        print("Catatan: waktu aktual dipengaruhi perangkat dan data uji.")
