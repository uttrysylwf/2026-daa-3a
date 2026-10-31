"""Implementasi RabinKarp untuk pembelajaran analisis algoritma."""
from ..base import StringMatcher

class RabinKarp(StringMatcher):
    def __init__(self, base=256, modulus=1_000_000_007):
        if not isinstance(base, int) or base < 1:
            raise ValueError('base harus bilangan bulat positif')
        if not isinstance(modulus, int) or modulus < 2:
            raise ValueError('modulus harus bilangan bulat >= 2')
        self.base, self.modulus = base, modulus

    def find_all(self, text, pattern):
        n, m = len(text), len(pattern)
        if m == 0:
            return list(range(n + 1))
        if m > n:
            return []
        base, mod = self.base, self.modulus
        high = pow(base, m - 1, mod)
        ph = th = 0
        for j in range(m):
            ph = (ph * base + ord(pattern[j])) % mod
            th = (th * base + ord(text[j])) % mod
        positions = []
        for i in range(n - m + 1):
            if ph == th:
                # Verifikasi karakter: hash collision tidak menghasilkan false positive.
                j = 0
                while j < m and text[i + j] == pattern[j]:
                    j += 1
                if j == m:
                    positions.append(i)
            if i < n - m:
                th = ((th - ord(text[i]) * high) * base + ord(text[i + m])) % mod
        return positions
