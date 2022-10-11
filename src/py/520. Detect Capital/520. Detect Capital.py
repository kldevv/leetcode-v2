class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap_count = 0
        for c in word:
            cap_count += c.isupper()
        return cap_count == 0 or cap_count == len(word) or (cap_count == 1 and word[0].isupper())

