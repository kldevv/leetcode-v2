class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        
        for i in range(n):
            image[i].reverse()
        
        for i in range(n):
            for j in range(m):
                image[i][j] ^= 1
        
        return image