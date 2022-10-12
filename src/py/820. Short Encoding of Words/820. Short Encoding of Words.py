class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        
        
        Trie = lambda : collections.defaultdict(Trie)
        root = Trie()
        
        nodes = [reduce(dict.__getitem__, reversed(word), root) for word in words]
        
        return sum([len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0])

