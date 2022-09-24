class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        not_cross = collections.defaultdict(int)
        for i in range(len(wall)):
            width = 0
            for incre_width in wall[i][:-1]:
                width += incre_width
                not_cross[width] += 1
        
        if not len(not_cross):
            return len(wall)
        
        return len(wall) - max(count for count in not_cross.values())
        