class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n = len(board)
        m = len(board[0])
        
        while True:
            # mark
            to_crush = set()
            for i in range(n):
                for j in range(m):
                    if board[i][j]:
                        if i < n-2 and board[i][j] == board[i+1][j] == board[i+2][j]:
                            to_crush |= {(i, j), (i+1, j), (i+2, j)}
                        if j < m-2 and board[i][j] == board[i][j+1] == board[i][j+2]:
                            to_crush |= {(i, j), (i, j+1), (i, j+2)}
                        
            if not to_crush:
                break
            
            # crush
            for i, j in to_crush:
                board[i][j] = 0
            
            # drop
            for j in range(m):
                t = n-1
                for i in range(n-1, -1, -1):
                    if board[i][j]:
                        board[t][j] = board[i][j]
                        t -= 1
                while t >= 0:
                    board[t][j] = 0
                    t -= 1
        return board    
    