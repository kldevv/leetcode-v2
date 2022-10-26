class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stk = []
        part = list(part)
        for c in s:
            stk.append(c)
            if stk[-len(part):] == part:
                stk = stk[:-len(part)]
        return "".join(stk)