class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        lower_bound = len(b) // len(a) + int(len(b) % len(a) != 0)
        
        if b in a * lower_bound:
            return lower_bound
        if b in a * (lower_bound + 1):
            return lower_bound + 1
        return -1