class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # greedy
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and n:
                adjacent_cnt = flowerbed[i-1] == 1 if i > 0 else 0
                adjacent_cnt += flowerbed[i+1] == 1 if i < len(flowerbed)-1 else 0
                if adjacent_cnt == 0:
                    n -= 1
                    flowerbed[i] = 1
        return n == 0