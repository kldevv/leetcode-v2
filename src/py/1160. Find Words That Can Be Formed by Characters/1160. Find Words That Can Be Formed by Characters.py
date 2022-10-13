class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_cnt = Counter(chars)
        out = 0
        for word in words:
            word_cnt = Counter(word)
            if (word_cnt & char_cnt) == word_cnt:
                out += len(word)
        return out

