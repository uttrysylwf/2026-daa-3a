# Proyek Algoritma Python OOP — Pertemuan 5

Implementasi 13 algoritma searching, sorting, dan string matching untuk mata kuliah Desain dan Analisis Algoritma. Python >= 3.10, tanpa dependensi runtime eksternal.

## Menjalankan

Ekstrak ZIP, masuk ke folder `algoritma_oop`, lalu:

```bash
python main.py
python -m unittest discover -s tests -v
```

Opsional instal paket dengan `python -m pip install -e .` (memerlukan setuptools).

## Struktur

```text
algoritma_oop/
    README.md
    pyproject.toml
    main.py
    algorithms/
        __init__.py
        base.py
        searching/
            __init__.py
            linear_search.py
            binary_search.py
            hash_table_search.py
        sorting/
            __init__.py
            bubble_sort.py
            selection_sort.py
            insertion_sort.py
            merge_sort.py
            quick_sort.py
            heap_sort.py
        string_matching/
            __init__.py
            naive.py
            kmp.py
            rabin_karp.py
            boyer_moore.py
    tests/
        __init__.py
        test_algorithms.py
```

## Konsep OOP

- **Abstraksi:** `SearchAlgorithm`, `SortAlgorithm`, dan `StringMatcher` mendefinisikan kontrak melalui ABC dan abstractmethod.
- **Inheritance:** setiap implementasi mewarisi kelas abstrak sesuai kategorinya.
- **Polimorfisme:** contoh `main.py` memanggil metode yang sama pada beberapa implementasi.
- **Enkapsulasi:** `HashTableIndex` menyimpan tabel posisi dalam `_positions` dan menyediakan metode `search()`.
- `SortAlgorithm.sort()` menggunakan kembali metode `sort_in_place()` dari subclass dan menyalin input agar data pemanggil tetap utuh.

## API dan contoh

```python
from algorithms.searching import BinarySearch, HashTableSearch
from algorithms.sorting import MergeSort
from algorithms.string_matching import KMP

result = MergeSort().sort([5, 1, 3, 1])  # [1, 1, 3, 5]
position = BinarySearch().search(result, 3)  # 2
index = HashTableSearch().build_index([5, 1, 3, 1])
print(index.search(1))  # 1
print(index.search(99))  # -1
print(KMP().find_all('ABABABA', 'ABA'))  # [0, 2, 4]
```

Searching mengembalikan indeks pertama (mulai 0), atau -1 jika tidak ditemukan. Binary Search mensyaratkan urutan menaik; validasi urutan sengaja tidak dilakukan karena membutuhkan O(n). Biaya pengurutan data harus dihitung terpisah. Hash Table memerlukan elemen dan target yang hashable dengan kontrak hash/equality yang konsisten. Indeks yang dibuat merepresentasikan data saat pembangunan; perubahan sumber memerlukan pembangunan ulang.

Sorting menerima elemen yang dapat dibandingkan secara konsisten. `sort(data)` mengembalikan list baru; `sort_in_place(list)` mengubah list asli dan mengembalikan None. Bubble, Insertion, dan Merge Sort stabil pada implementasi ini; Selection, Quick, dan Heap Sort tidak dijamin stabil.

String matching mengembalikan semua posisi, termasuk overlap. Pattern kosong cocok di setiap batas: `[0, ..., len(text)]`. Panjang dan posisi dihitung berdasarkan code point Python, bukan byte atau grapheme tampilan. Kesetaraan Unicode mengikuti string Python, tanpa normalisasi otomatis.

## Kompleksitas untuk implementasi ini

`n` adalah jumlah elemen/panjang teks, `m` panjang pattern, `k` jumlah hasil. Ruang berikut adalah **ruang tambahan**, tanpa input dan daftar hasil string O(k). Kolom sorting berlaku untuk `sort_in_place`; `sort` menambah salinan O(n). Analisis mengasumsikan operasi perbandingan/hash elemen berbiaya konstan; untuk objek/string besar biaya ini perlu diperhitungkan.

| Algoritma | Best time | Average/expected time | Worst time | Ruang tambahan |
|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Binary Search (batas kiri) | O(log n) | O(log n) | O(log n) | O(1) |
| Hash lookup sesudah build | O(1) | O(1) expected | O(n) | O(n) indeks |
| Bubble Sort (early exit) | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort (pivot terakhir) | O(n log n) | O(n log n)* | O(n²) | O(log n) batas stack |
| Heap Sort | O(n)** | O(n log n)* | O(n log n) | O(1) |
| Naive String Matching | O(n)*** | Bergantung input | O((n-m+1)m) | O(1) |
| KMP | O(n+m) | O(n+m) | O(n+m) | O(m) |
| Rabin–Karp | O(n+m) | O(n+m) expected**** | O(nm+m) | O(1) |
| Boyer–Moore bad-character | Bergantung input | Bergantung input | O(nm+m) | O(min(m, jumlah karakter berbeda)) |

Batas dinyatakan dengan Big-O; gunakan Theta ketika ingin menyatakan batas ketat untuk model/kasus yang ditetapkan. Formula string terburuk mengasumsikan 1 <= m <= n; pattern lebih panjang langsung menghasilkan kosong, dan pattern kosong membutuhkan O(n) untuk membuat output.

Binary Search menggunakan lower bound untuk menjamin indeks duplikasi pertama; karena itu tidak berhenti segera saat menemukan target di tengah. Best case O(1) pada versi Binary Search biasa tidak berlaku umum pada versi ini.

Hash: build expected O(n), worst O(n²) jika banyak collision. `HashTableSearch.search(data, target)` membangun indeks setiap pemanggilan, sehingga expected O(n), worst O(n²). Gunakan `build_index()` satu kali untuk banyak query; lookup saja expected O(1). Dictionary Python digunakan sebagai struktur hash dasar.

* Average Quick Sort mengasumsikan permutasi acak dengan elemen berbeda. Data terurut atau semua sama dapat menghasilkan O(n²), tetapi rekursi hanya pada partisi lebih kecil menjaga stack O(log n) bahkan pada kasus buruk. Tidak menggunakan slicing partisi.

** Heap Sort ini dapat O(n) untuk semua nilai sama karena sift langsung berhenti. O(n log n) tetap batas atas semua kasus; best case tidak selalu Theta(n log n).

*** Naive dapat menolak setiap alignment pada karakter pertama, dengan O(n-m+1) perbandingan. Untuk m tetap dan teks besar ini O(n). Waktu bergantung hubungan n dan m.

**** Rabin–Karp menggunakan rolling hash modular dan verifikasi karakter. Expected linear memerlukan asumsi collision jarang dan jumlah/verifikasi kecocokan tidak mendominasi; banyak kecocokan nyata dapat membuatnya O(nm). Modulus tetap tidak menjamin bebas collision. Model ruang O(1) mengasumsikan integer hash berukuran tetap.

Boyer–Moore di sini adalah varian **bad-character saja**, tanpa good-suffix/Galil. Tabel dibuat O(m); jumlah alignment bisa kecil pada input tertentu, tetapi tidak ada jaminan worst-case linear.

## Aktivitas analisis Pertemuan 5

1. Tentukan input size dan operasi dasar: equality untuk searching, perbandingan/pertukaran untuk sorting, perbandingan karakter untuk string matching.
2. Hitung Linear Search pada target pertama, terakhir, dan tidak ada.
3. Bandingkan Bubble/Insertion pada data terurut, terbalik, dan acak. Early exit mengubah best case Bubble.
4. Bandingkan Merge Sort dengan sorting in-place: waktu O(n log n) dan biaya buffer O(n).
5. Bandingkan pencarian linear berulang dengan satu build indeks hash dan banyak lookup. Sertakan waktu pembangunan.
6. Bandingkan Naive dan KMP untuk teks banyak karakter berulang; diskusikan tabel LPS O(m).
7. Uji Quick Sort pada input terurut untuk membedakan average dan worst case.
8. Untuk eksperimen waktu, gunakan `time.perf_counter()`, ukuran input bertahap, seed tetap, dan beberapa pengulangan. Siapkan input di luar waktu pengukuran; catat jika biaya salinan `sort()` ikut dihitung. Hasil eksperimen tidak membuktikan batas asimtotik.

Pengujian menggunakan unittest dan oracle `sorted`, `list.index`, serta `str.startswith`: data kosong, singleton, duplikasi, negatif, input acak deterministik, overlap, Unicode, hash collision, dan enumerasi semua teks biner sampai panjang 6/pattern sampai panjang 4. Rabin–Karp juga diuji dengan modulus kecil untuk memaksa collision.
