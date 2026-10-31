import random
import unittest
from itertools import product
from code04_algomplexity.algorithms.searching import LinearSearch, BinarySearch, HashTableSearch
from code04_algomplexity.algorithms.sorting import BubbleSort, SelectionSort, InsertionSort, MergeSort, QuickSort, HeapSort
from code04_algomplexity.algorithms.string_matching import NaiveStringMatching, KMP, RabinKarp, BoyerMoore

class AlgorithmTests(unittest.TestCase):
    def test_sorting(self):
        rng = random.Random(42)
        cases = [[], [1], [2, 2], list(range(30)), list(range(30, -1, -1))]
        cases += [[rng.randrange(-10, 11) for _ in range(rng.randrange(50))] for _ in range(80)]
        for cls in (BubbleSort, SelectionSort, InsertionSort, MergeSort, QuickSort, HeapSort):
            for values in cases:
                with self.subTest(algorithm=cls.__name__, values=values):
                    original = values.copy()
                    self.assertEqual(cls().sort(values), sorted(values))
                    self.assertEqual(values, original)
                    inplace = values.copy()
                    self.assertIsNone(cls().sort_in_place(inplace))
                    self.assertEqual(inplace, sorted(values))

    def test_searching(self):
        for values in ([], [1], [3, 1, 3, 2], [0] * 20):
            for cls in (LinearSearch, BinarySearch, HashTableSearch):
                data = sorted(values) if cls is BinarySearch else values
                for target in (-1, 0, 1, 2, 3, 99):
                    expected = data.index(target) if target in data else -1
                    self.assertEqual(cls().search(data, target), expected)
                if cls is HashTableSearch:
                    index = cls().build_index(data)
                    for target in (-1, 0, 1, 3):
                        self.assertEqual(index.search(target), data.index(target) if target in data else -1)

    def test_matching_exhaustive(self):
        strings = [''.join(chars) for n in range(7) for chars in product('ab', repeat=n)]
        patterns = [''.join(chars) for n in range(5) for chars in product('ab', repeat=n)]
        matchers = [NaiveStringMatching(), KMP(), RabinKarp(), RabinKarp(modulus=2), BoyerMoore()]
        for text in strings + ['😊a😊a', 'ééé', '中文中文']:
            for pattern in patterns + ['😊', 'éé', '中文']:
                expected = [i for i in range(len(text) - len(pattern) + 1) if text.startswith(pattern, i)]
                for matcher in matchers:
                    with self.subTest(algorithm=type(matcher).__name__, text=text, pattern=pattern):
                        self.assertEqual(matcher.find_all(text, pattern), expected)

    def test_hash_collision(self):
        class Key:
            def __init__(self, value): self.value = value
            def __hash__(self): return 1
            def __eq__(self, other): return isinstance(other, Key) and self.value == other.value
        values = [Key(i) for i in range(10)]
        index = HashTableSearch().build_index(values)
        self.assertEqual(index.search(Key(7)), 7)
        self.assertEqual(index.search(Key(20)), -1)

    def test_rabin_karp_validation(self):
        for kwargs in ({'base': 0}, {'modulus': 1}, {'base': 1.5}):
            with self.assertRaises(ValueError): RabinKarp(**kwargs)

if __name__ == '__main__':
    unittest.main()
