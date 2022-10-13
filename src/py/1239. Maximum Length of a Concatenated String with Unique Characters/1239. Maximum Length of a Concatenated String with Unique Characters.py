class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def bit_mask(word):
            out = 0
            for c in word:
                out |= (1 << (ord(c) - ord('a')))
            return out
            
        arr = [(bit_mask(x), len(x)) for x in arr if len(set(x)) == len(x)]
        queue = [(0, 0)]
        
        out = 0
        for word_mask, word_len  in arr:
            old_queue = queue.copy()
            for subseq_len, subseq_mask in old_queue:
                if word_mask & subseq_mask == 0:
                    queue.append((subseq_len + word_len, word_mask | subseq_mask))
                    out = max(out, queue[-1][0])
        return out

            