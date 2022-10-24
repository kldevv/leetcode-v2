class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [0] * n
        
        end = 0
        for i in range(n):
            for word in words:
                if s.startswith(word, i):
                    end = max(end, i + len(word))
            
            bold[i] = end > i
        
        
        out = []
        i = 0
        while i < n:
            if not bold[i]:
                out.append(s[i])
                i += 1
            else:
                j = i
                while j < n and bold[j]:
                    j += 1
                out.append(f"<b>{s[i:j]}</b>")
                i = j

        return "".join(out)

