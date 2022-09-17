class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
            else:
                stk.append([c, 1])
            while stk and stk[-1][1] >= k:
                stk[-1][1] -= k
                if stk[-1][1] == 0:
                    stk.pop()
                    if len(stk) > 1 and stk[-2][0] == stk[-1][0]:
                        stk[-2][1] += stk[-1][1]
                        stk.pop()
        
        out = ""
        for c, count in stk:
            out += c * count
        return out

