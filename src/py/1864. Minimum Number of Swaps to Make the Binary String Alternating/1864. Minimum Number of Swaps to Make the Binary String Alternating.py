class Solution:
    def minSwaps(self, s: str) -> int:
        one = 0
        zero = 0
        for c in s:
            one += (c == "1")
            zero += (c == "0")
        
        if abs(one-zero) > 1:
            return -1
        
        cnt = 0
        for i, c in enumerate(s):
            cnt += (int(c) != (i + (one > zero)) % 2)
        
        if one == zero:
            cnt = min(len(s)-cnt, cnt)
        
        return cnt // 2

