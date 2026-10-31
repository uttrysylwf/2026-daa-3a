import random
from pathlib import Path

import pytest

from code05_proyek1.algorithms import (
    IterativeKMP, RecursiveKMP, NaiveMatcher, IterativeMergeSort, RecursiveMergeSort,
)
from code05_proyek1.core.counter import OperationCounter
from code05_proyek1.models import PatternResult
from code05_proyek1.services import LogReader, build_detector, rarest_first

DATASET = Path(__file__).resolve().parent.parent / "dataset" / "case5_server_access.txt"
MATCHERS = [IterativeKMP, RecursiveKMP, NaiveMatcher]


def _rand_text(rng, n, alphabet="AB"):
    return "".join(rng.choice(alphabet) for _ in range(n))


# ---------- Proses 1: tabel failure ----------
@pytest.mark.parametrize("cls", [IterativeKMP, RecursiveKMP])
def test_failure_table_known_values(cls):
    m = cls(OperationCounter())
    assert m.prepare("ABABCABAB") == [0, 0, 1, 2, 0, 1, 2, 3, 4]
    assert m.prepare("AAAA") == [0, 1, 2, 3]
    assert m.prepare("X") == [0]


@pytest.mark.parametrize("cls", MATCHERS)
def test_empty_pattern_rejected(cls):
    with pytest.raises(ValueError):
        cls(OperationCounter()).prepare("")


# ---------- Proses 2: pencocokan pada satu baris ----------
@pytest.mark.parametrize("cls", MATCHERS)
def test_first_match_equals_builtin(cls):
    rng = random.Random(7)
    m = cls(OperationCounter())
    for _ in range(300):
        text = _rand_text(rng, rng.randint(0, 40))
        pattern = _rand_text(rng, rng.randint(1, 6))
        assert m.first_match(text, pattern, m.prepare(pattern)) == text.find(pattern)


@pytest.mark.parametrize("cls", [IterativeKMP, RecursiveKMP])
def test_kmp_comparison_bounds(cls):
    """Terbaik = n perbandingan; terburuk <= 2n (batas atas KMP)."""
    n, m = 300, 10
    c = OperationCounter()
    kmp = cls(c)
    kmp.first_match("B" * n, "A" * m, kmp.prepare("A" * m))
    best = c.comparisons - (m - 1)               # kurangi biaya membangun tabel
    assert best == n

    c.reset()
    pat = "A" * (m - 1) + "B"
    kmp.first_match("A" * n, pat, kmp.prepare(pat))
    assert c.comparisons <= 2 * n + 2 * m


def test_recursive_depth_is_linear_in_line_length():
    c = OperationCounter()
    kmp = RecursiveKMP(c)
    kmp.first_match("B" * 400, "A", kmp.prepare("A"))
    assert c.max_depth >= 400


# ---------- Proses 4: merge sort ----------
@pytest.mark.parametrize("cls", [IterativeMergeSort, RecursiveMergeSort])
def test_merge_sort_matches_builtin_and_is_stable(cls):
    rng = random.Random(3)
    for _ in range(100):
        data = [(rng.randint(0, 5), i) for i in range(rng.randint(0, 40))]
        out = cls(OperationCounter()).sort(data, lambda a, b: a[0] < b[0])
        assert out == sorted(data, key=lambda t: t[0])   # sorted() stabil -> sama persis
        assert len(data) == len(out)


@pytest.mark.parametrize("cls", [IterativeMergeSort, RecursiveMergeSort])
def test_merge_sort_does_not_mutate_input(cls):
    data = [3, 1, 2]
    cls(OperationCounter()).sort(data, lambda a, b: a < b)
    assert data == [3, 1, 2]


def test_rarest_first_order():
    a = PatternResult("a", [1, 2, 3])
    b = PatternResult("b", [9])
    z = PatternResult("z", [])
    s = IterativeMergeSort(OperationCounter()).sort([z, a, b], rarest_first)
    assert [r.pattern for r in s] == ["b", "a", "z"]


# ---------- Pipeline ----------
LINES = [
    "GET /index OK",
    "POST /healthcheck 200",
    "GET /index OK",
    "UNION SELECT x",
    "POST /healthcheck 200",
    "POST /healthcheck 200",
]


@pytest.mark.parametrize("mode", ["iterative", "recursive", "naive"])
def test_detector_small(mode):
    detector, _ = build_detector(mode)
    res = detector.detect(LINES, ["POST /healthcheck", "UNION SELECT", "nope"])
    assert [(r.pattern, r.line_numbers) for r in res] == [
        ("UNION SELECT", [4]),
        ("POST /healthcheck", [2, 5, 6]),
        ("nope", []),
    ]


def test_modes_give_identical_results_and_operations():
    lines = LogReader.read_lines(DATASET)
    pats = ["POST /healthcheck", "X11; Linux x86_64; rv:130.0", "340.213.18.221:2816"]
    outs = []
    for mode in ("iterative", "recursive"):
        det, c = build_detector(mode)
        r = det.detect(lines, pats)
        outs.append(([(x.pattern, x.line_numbers) for x in r], c.comparisons))
    assert outs[0] == outs[1]


def test_dataset_against_reference():
    lines = LogReader.read_lines(DATASET)
    assert len(lines) == 3459
    pats = ["POST /healthcheck", "X11; Linux x86_64; rv:130.0", "340.213.18.221:2816"]
    det, _ = build_detector("iterative")
    for r in det.detect(lines, pats):
        expected = [i + 1 for i, l in enumerate(lines) if r.pattern in l]   # referensi (boleh pakai builtin di test)
        assert r.line_numbers == expected
