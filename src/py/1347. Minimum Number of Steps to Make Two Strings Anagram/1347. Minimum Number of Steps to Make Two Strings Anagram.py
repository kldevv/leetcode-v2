class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts_s = collections.Counter(s)
        counts_t = collections.Counter(t)
        
        total_diff = 0
        for k in set(counts_s.keys()) | set(counts_t.keys()):
            total_diff += abs(counts_s[k] - counts_t[k])
        return total_diff // 2

