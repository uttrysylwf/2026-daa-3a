from pathlib import Path
from code06_typos.dictionary_manager import DictionaryManager
from code06_typos.typo_validator import TypoValidator
from code06_typos.performance import PerformanceAnalyzer

def main():
    path = Path(__file__).resolve().parent / "dataset/dictionary.txt"
    dictionary = DictionaryManager(path)
    try:
        words = dictionary.load()
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return
    validator = TypoValidator(dictionary)
    analyzer = PerformanceAnalyzer(dictionary)
    print("=" * 54)
    print("VALIDATOR TYPO BAHASA INDONESIA — OOP")
    print(f"Jumlah kata unik: {len(words)}")
    print("=" * 54)
    while True:
        print("\n1. Validasi kata dan tampilkan 3 saran")
        print("2. Benchmark Linear Search vs Binary Search")
        print("0. Keluar")
        choice = input("Pilih menu: ").strip()
        if choice == "1":
            try:
                result = validator.validate(input("Masukkan kata: "))
            except ValueError as error:
                print(error)
                continue
            if result["valid"]:
                print(f"✓ {result['word']!r} ditemukan di kamus.")
                print(f"Waktu pencarian: {result['lookup_ms']:.4f} ms")
            else:
                print(f"✗ {result['word']!r} tidak ditemukan di kamus.")
                print("Kandidat koreksi terbaik:")
                for i, item in enumerate(result["candidates"], 1):
                    print(f"{i}. {item['word']} (jarak: {item['distance']})")
                print(f"Waktu pencarian: {result['lookup_ms']:.4f} ms")
                print(f"Waktu membuat saran: {result['suggestion_ms']:.2f} ms")
        elif choice == "2":
            target = input("Kata untuk diuji: ").strip()
            if not target:
                print("Kata tidak boleh kosong.")
                continue
            try:
                repetitions = int(input("Pengulangan [1000]: ").strip() or "1000")
                if repetitions < 1:
                    raise ValueError
            except ValueError:
                print("Masukkan bilangan bulat positif.")
                continue
            analyzer.compare(target, repetitions)
        elif choice == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
