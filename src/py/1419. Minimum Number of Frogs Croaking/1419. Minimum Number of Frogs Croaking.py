class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frogs = [0] * 4
        out = 0
        for c in croakOfFrogs:
            if c == "c":
                frogs[0] += 1
            elif c == "r":
                if frogs[0] == 0:
                    return -1
                frogs[0] -= 1
                frogs[1] += 1
            elif c == "o":
                if frogs[1] == 0:
                    return -1
                frogs[1] -= 1
                frogs[2] += 1
            elif c == "a":
                if frogs[2] == 0:
                    return -1
                frogs[2] -= 1
                frogs[3] += 1
            elif c == "k":
                frogs[3] -= 1
            
            out = max(out, sum(frogs))
                
        return out if sum(frogs) == 0 else -1

