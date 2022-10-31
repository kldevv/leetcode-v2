class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        out = []
        for word in queries:
            for d in dictionary:
                mismatch = 0
                for c1, c2 in zip(word, d):
                    mismatch += int(c1 != c2)
                if mismatch <= 2:
                    out.append(word)
                    break
        return out
            
            
            