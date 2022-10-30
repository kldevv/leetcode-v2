class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        ori_n = n
        base = 1
        while sum(map(int, str(n))) > target:
            n = n // 10 + 1
            base *= 10
        return base * n - ori_n

