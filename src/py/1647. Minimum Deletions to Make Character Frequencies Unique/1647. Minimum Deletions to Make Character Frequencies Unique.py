class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = sorted(list(Counter(s).values()), reverse=True)
        
        out = 0
        for i in range(1, len(cnt)):
            max_next_cnt = max(cnt[i-1] - 1, 0)
            # see how many count have exceeded max_next_cnt
            out += max(cnt[i] - max_next_cnt, 0)
            cnt[i] = min(cnt[i], max_next_cnt)
            
        return out

