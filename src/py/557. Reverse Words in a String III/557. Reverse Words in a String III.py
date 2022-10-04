class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = 0
        while i < n:
            i_start = i
            while i < n and not s[i].isspace():
                i += 1
            i_end = i - 1
            
            while i_start < i_end:
                s[i_start], s[i_end] = s[i_end], s[i_start]
                i_start += 1
                i_end -= 1
            i += 1
        return "".join(s)
   