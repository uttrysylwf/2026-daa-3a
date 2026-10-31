# Typo Validator Bahasa Indonesia — Python OOP

Program terminal untuk mengecek ejaan berdasarkan `dictionary.txt`, menyarankan tiga kata terdekat dengan Levenshtein Distance, dan membandingkan Linear Search dengan Binary Search.

## Menjalankan
1. Pastikan Python 3.10+ tersedia.
2. Pastikan `dictionary.txt` ada di folder ini.
3. Jalankan `python main.py`.

Tidak memerlukan library eksternal.

## Struktur OOP
- `DictionaryManager`: membaca kamus dan menjalankan Linear/Binary Search.
- `Levenshtein`: menghitung jarak edit dengan Dynamic Programming.
- `TypoValidator`: memvalidasi kata dan memilih kandidat koreksi.
- `PerformanceAnalyzer`: menampilkan hasil benchmark.
- `main.py`: antarmuka menu CLI.

## Kompleksitas
- Linear Search: O(n) waktu, O(1) ruang tambahan.
- Binary Search: O(log n) waktu, O(1) ruang tambahan, dengan prasyarat kamus terurut.
- Levenshtein Distance: O(mk) waktu dan O(min(m,k)) ruang untuk panjang kata m dan k.
- Pencarian saran menghitung jarak ke seluruh kata kamus; waktu total bergantung pada jumlah dan panjang kata.

Benchmark hanya mengukur pencarian berulang setelah kamus dimuat. Waktu pemuatan dan pengurutan tidak termasuk. Hasil waktu dipengaruhi perangkat dan input.

Catatan: validitas kata mengikuti isi kamus, bukan verifikasi konteks atau makna. Kualitas saran bergantung pada kelengkapan kamus.
