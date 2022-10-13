class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        queue = [list(s)]
        i = 0
        while i < len(s):
            while i < len(s) and not s[i].isalpha():
                i += 1
            if i < len(s):
                new_queue = queue.copy()
                for cand in queue:
                    new_queue.append(cand[:i] + [cand[i].swapcase()] + cand[i+1:])
                queue = new_queue
            i += 1
        return map(lambda x : "".join(x), queue)