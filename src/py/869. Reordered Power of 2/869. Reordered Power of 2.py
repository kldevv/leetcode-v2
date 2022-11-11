class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_cnt = Counter(str(n))
        for i in range(32):
            if n_cnt == Counter(str(1 << i)):
                return True
        return False
