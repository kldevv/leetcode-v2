class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]
        
        s = list(s)
        for i, (c, k) in enumerate(zip(s, shifts)):
            s[i] = chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        
        return "".join(s)
    