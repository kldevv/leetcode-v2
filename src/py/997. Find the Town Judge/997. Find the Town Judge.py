class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if only of person in the town
        if not len(trust) and n == 1:
            return 1
        
        trust_counts = [0] * (n + 1)
        
        for a, b in trust:
            trust_counts[a] -= 1
            trust_counts[b] += 1
                
        for idx, tc in enumerate(trust_counts):
            if tc == n-1:
                return idx
            
        return -1
            