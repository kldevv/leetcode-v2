class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            maps = {}
            for x, y in zip(word, pattern):
                if maps.setdefault(x, y) != y:
                    return False
            # x => y, y can only match to x
            return len(set(maps.values())) == len(maps.values())
            
        return filter(match, words)

