class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def find_max_cnt(cnt):
            return max((c, i) for i, c in enumerate(cnt))[0]
        
        cnt = [0] * 26
        j = 0
        out = 0
        for i, c in enumerate(s):
            c_ord = ord(c) - ord('A')
            cnt[c_ord] += 1
            while j < i and i - j + 1 - find_max_cnt(cnt) > k:
                cnt[ord(s[j]) - ord('A')] -= 1
                j += 1
            out = max(out, i - j + 1)
        return out