class Solution:
    def minOperations(self, n: int) -> int:
        target = sum(2 * i + 1 for i in range(n)) // n
        return sum(abs((i * 2 + 1) - target) for i in range(n)) // 2