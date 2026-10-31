from pathlib import Path
from code04_algomplexity.algorithms.searching import LinearSearch, BinarySearch, HashTableSearch
from code04_algomplexity.algorithms.sorting import BubbleSort, SelectionSort, InsertionSort, MergeSort, QuickSort, HeapSort
from code04_algomplexity.algorithms.string_matching import NaiveStringMatching, KMP, RabinKarp, BoyerMoore

def main():
    data = [9, 3, 7, 3, 1]
    print('SORTING:', data)
    for algorithm in (BubbleSort(), SelectionSort(), InsertionSort(), MergeSort(), QuickSort(), HeapSort()):
        print(type(algorithm).__name__, algorithm.sort(data))
    print('SEARCHING (indeks mulai 0):')
    for algorithm in (LinearSearch(), BinarySearch(), HashTableSearch()):
        source = sorted(data) if isinstance(algorithm, BinarySearch) else data
        print(type(algorithm).__name__, source, 'target=3:', algorithm.search(source, 3))
    index = HashTableSearch().build_index(data)
    print('Indeks hash digunakan ulang:', [index.search(x) for x in (3, 7, 42)])
    story_path = Path(__file__).resolve().parent / 'data' / '01_kelinci_dan_kebun_wortel.txt'
    text = story_path.read_text(encoding='utf-8')
    pattern = 'kelinci'
    print(f'STRING MATCHING: sumber={story_path.name}, pattern={pattern!r}')
    print(f'Panjang teks: {len(text)} karakter')
    for algorithm in (NaiveStringMatching(), KMP(), RabinKarp(), BoyerMoore()):
        print(type(algorithm).__name__, algorithm.find_all(text, pattern))

if __name__ == '__main__':
    main()
