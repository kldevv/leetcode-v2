class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = Counter(s[i:i+minSize] for i in range(0, len(s)-minSize+1))
        return max([v for k, v in cnt.items() if len(set(k)) <= maxLetters] or [0])

