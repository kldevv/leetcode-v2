class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        factors = int(10 ** 9 + 7)
        powers = []
        while n:
            powers.append(n & (-n))
            n &= (n & (n-1))

        for i in range(1, len(powers)):
            powers[i] *= powers[i-1]

        out = []
        for start, end in queries:
            out.append((powers[end] // (powers[start-1] if start > 0 else 1)) % factors)
        return out