class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for kk in range(0, len(s), 2*k):
            i = kk
            j = min(kk + k, len(s)) - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return "".join(s)
                