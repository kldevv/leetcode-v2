class Leaderboard:

    def __init__(self):
        self.scores = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        out = []
        for score in self.scores.values():
            heapq.heappush(out, score)
            if len(out) > K:
                heapq.heappop(out)
        return sum(out)

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)