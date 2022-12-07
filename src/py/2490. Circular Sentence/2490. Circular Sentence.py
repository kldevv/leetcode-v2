class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")
        n = len(s)
        for i in range(n):
            # i+1 % n rolls back to 0
            if s[i][-1] != s[(i+1) % n][0]:
                return False
        return True
