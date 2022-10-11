class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        diff_idx = []
        for i, (c1, c2) in enumerate(zip(s, goal)):
            if c1 != c2:
                diff_idx.append(i)
            if len(diff_idx) > 2:
                return False
        
        if len(diff_idx) == 2:
            return s[diff_idx[0]] == goal[diff_idx[1]] and s[diff_idx[1]] == goal[diff_idx[0]]
        if len(diff_idx) == 0:
            return len(s) - len(set(s))
        return False

