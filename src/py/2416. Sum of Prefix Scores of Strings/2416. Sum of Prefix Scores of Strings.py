class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.counts = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tt = Trie()
        base = ord('a')
        
        for word in words:
            node = tt
            for c in word:
                idx = ord(c) - base
                if node.children[idx] is None:
                    node.children[idx] = Trie()
                node = node.children[idx]
                node.counts += 1
        
        out = []
        for word in words:
            node = tt
            score = 0
            for c in word:
                idx = ord(c) - base
                if node.children[idx] is not None:
                    node = node.children[idx]
                    score += node.counts
            out.append(score)
            
        return out