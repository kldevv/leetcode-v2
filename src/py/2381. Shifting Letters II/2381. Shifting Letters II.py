class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        moves = [0] * (n+1)
        
        for start, end, direc in shifts:
            d = 1 if direc else -1
            moves[start] += d
            moves[end+1] -= d
        
        for i in range(1, n+1):
            moves[i] += moves[i-1]
        
        s = list(s)
        for i, (c, m) in enumerate(zip(s, moves)):
            s[i] = chr((ord(c)-ord('a')+m) % 26 + ord('a'))
        
        return "".join(s)
                    