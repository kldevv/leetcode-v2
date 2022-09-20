class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        others = {}
        for x, y in pairs:
            others[x] = y
            others[y] = x
        
        pref = collections.defaultdict(lambda : [0] * n)
        for x, friends in enumerate(preferences):
            for i, friend in enumerate(friends):
                pref[x][friend] = i
        
        out = 0
        for x, y in pairs:
            for u in preferences[x]:
                if pref[u][x] < pref[u][others[u]]:
                    out += 1
                    break
                if u == y:
                    break
            for u in preferences[y]:
                if pref[u][y] < pref[u][others[u]]:
                    out += 1
                    break
                if u == x:
                    break
        return out