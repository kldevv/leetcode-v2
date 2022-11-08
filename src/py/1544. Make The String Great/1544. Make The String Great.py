class Solution:
    def makeGood(self, s: str) -> str:
        def is_good(c1, c2):
            if c1.isupper() == c2.isupper():
                return False
            
            a = ord(c1) - ord('A' if c1.isupper() else 'a')
            b = ord(c2) - ord('A' if c2.isupper() else 'a') 
                
            return a == b
        
        # empty string is also good
        if not s:
            return s
        
        out = []
        for c in s:
            if out and is_good(out[-1], c):
                out.pop()
            else:
                out.append(c)
        return "".join(out)
        