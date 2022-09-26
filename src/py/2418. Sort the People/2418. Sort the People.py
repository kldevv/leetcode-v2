class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        out = sorted([(height, name) for name, height in zip(names, heights)], reverse=True)
        return [n for h, n in out]

