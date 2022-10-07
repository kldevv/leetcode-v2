class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        
        s1_cnt = Counter(s1)
        s2_cnt = Counter()

        i = 0
        j = 0
        while i < len(s2):
            s2_cnt[s2[i]] += 1
            if i - j + 1 > n:
                s2_cnt[s2[j]] -= 1
                if s2_cnt[s2[j]] == 0:
                    del s2_cnt[s2[j]]
                j += 1
            if i >= n - 1 and s1_cnt == s2_cnt:
                return True
            i += 1
        return False

