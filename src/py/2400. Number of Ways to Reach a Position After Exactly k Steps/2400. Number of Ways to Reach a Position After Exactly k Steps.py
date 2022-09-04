class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # right - left = endPos - startPos
        # : right steps count should have diff equals to distance of start and end
        # left + right = k
        # : total steps count equals to k
        
        # > right = (endPos - startPos + k) // 2
        
        MOD = pow(10, 9) + 7
        if (endPos - startPos + k) % 2 != 0:
            return 0
        
        return math.comb(k, (endPos-startPos+k) // 2) % MOD

