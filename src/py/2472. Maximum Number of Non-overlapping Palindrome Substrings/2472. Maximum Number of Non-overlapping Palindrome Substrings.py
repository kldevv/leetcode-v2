class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def is_pal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        n = len(s)
        tl = -1
        out = 0
        for i in range(n):
            if i <= tl:
                continue
            # we need to consider odd and even length
            # if there is a valid case with the length of k+2, 
            if i+k-1 < n and is_pal(i, i+k-1):
                out += 1
                tl = i + k - 1
            elif i+k < n and is_pal(i, i+k):
                out += 1
                tl = i + k
        
        return out
# k = 3
# odd:
#     abcba
#     abba

# k = 4
# odd:
#     acbbca
# even:
#     abba
#     abcba