class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x: (x[0], -x[1]))
        idx = {}
        out = []
        for id_, score in items:
            if id_ not in idx:
                idx[id_] = [len(out), 0]
                out.append([id_, 0])
            if idx[id_][1] < 5:
                out[idx[id_][0]][1] += score
                idx[id_][1] += 1
        
        return [[x, y // 5] for x, y in out]
