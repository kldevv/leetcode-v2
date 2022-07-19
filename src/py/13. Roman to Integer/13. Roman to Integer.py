class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        If the roman followed is larger, the current should be subtracted, otherwise added.
        
        e.g. IV -1 + 5
        e.g. VI +5 + 1
        '''
        
        conversion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        num = 0
        for i in range(0, len(s) - 1):
            currNum = conversion[s[i]]
            nextNum = conversion[s[i+1]]
            
            num += (-1 if currNum < nextNum else 1) * currNum
        num += conversion[s[-1]]
        
        return num