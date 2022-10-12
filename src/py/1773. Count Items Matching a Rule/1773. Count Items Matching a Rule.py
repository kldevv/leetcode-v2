class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i = 0
        if ruleKey == "color":
            i = 1
        elif ruleKey == "name":
            i = 2
        
        out = 0
        for item in items:
            out += int(item[i] == ruleValue)
        return out

