class Solution:
    def frequencySort(self, s: str) -> str:
        s_l = list(s)
        counts = collections.Counter(s_l)
        return "".join(sorted(s_l, key=lambda x : (counts[x], x), reverse=True))

