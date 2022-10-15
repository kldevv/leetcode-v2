class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26
        j = 0
        out = 0
        for i, c in enumerate(s):
            c_ord = ord(c) - ord('A')
            cnt[c_ord] += 1
            while j < i and i - j + 1 - max(cnt) > k:
                cnt[ord(s[j]) - ord('A')] -= 1
                j += 1
            out = max(out, i - j + 1)
        return out