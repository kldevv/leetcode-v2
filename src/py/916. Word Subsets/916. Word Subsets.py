class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        b_cnt = Counter()
        for word in words2:
            b_cnt |= Counter(word)
            
        out = []
        for word in words1:
            a_word_cnt = Counter(word)
            if a_word_cnt & b_cnt == b_cnt:
                out.append(word)
                
        return out