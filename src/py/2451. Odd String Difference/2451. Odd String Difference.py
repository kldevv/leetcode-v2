class Solution:
    def oddString(self, words: List[str]) -> str:
        cnt = defaultdict(list)
        for word in words:
            diff = []
            for i in range(len(word)-1):
                diff.append(ord(word[i+1])-ord(word[i]))
            cnt[str(diff)].append(word)
        
        for s in cnt.values():
            if len(s) == 1:
                return s[0]