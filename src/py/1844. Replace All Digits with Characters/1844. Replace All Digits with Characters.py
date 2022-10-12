class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = chr(int(s[i]) + ord(s[i-1]))
        return "".join(s)

