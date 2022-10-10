class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        
        def get_smallest(cnt):
            # return lexi smallest and yet still visited element
            for i, count in enumerate(cnt):
                if count != 0:
                    return chr(i + ord('a'))
        
        t = []
        out = []
        for c in s:
            # if top of stack is smaller than all the following elements, record the top
            while t and t[-1] <= get_smallest(cnt):
                out.append(t[-1]) 
                t.pop()
            t.append(c)
            cnt[ord(c) - ord('a')] -= 1
        # pop off rest of the elements
        out += reversed(t)
        
        return "".join(out)

