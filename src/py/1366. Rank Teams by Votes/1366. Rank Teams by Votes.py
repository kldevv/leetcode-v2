class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        weights = [[0] * n for i in range(26)]
        
        for vote in votes:
            for i, c in enumerate(vote):
                j = ord(c) - ord('A')
                weights[j][i] += 1
        weights = sorted([(weight, -i) for i, weight in enumerate(weights) if any(weight)])
        
        return "".join(chr(int(l[-1]) * -1 + ord('A')) for l in weights[::-1])

