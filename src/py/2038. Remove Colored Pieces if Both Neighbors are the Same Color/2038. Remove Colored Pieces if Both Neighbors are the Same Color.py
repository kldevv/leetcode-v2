class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A_cnt = 0
        B_cnt = 0
        for i in range(1, len(colors)-1):
            if colors[i] == colors[i-1] == colors[i+1]:
                if colors[i] == "A":
                    A_cnt += 1
                else:
                    B_cnt += 1
        
        return A_cnt > B_cnt