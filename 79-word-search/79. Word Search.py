class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtrack with checks and simply replace the value with something else till the backtrack happens
        r, c = len(board), len(board[0])
        pos = []
        n = len(word)
        wordStart = word[0]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(r):
            for j in range(c):
                if board[i][j] == wordStart:
                    pos.append((i, j))

        def check_if_exists(x, y, idx):
            if idx == n:
                return True

            temp = board[x][y]
            board[x][y] = "#"

            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                if 0<=nx<r and 0<=ny<c and board[nx][ny] == word[idx]:
                    if check_if_exists(nx, ny, idx+1) == True:
                        return True
            
            board[x][y] = temp
            return False


        # now backtrack and check here
        for p in pos:
            x, y = p
            if check_if_exists(x, y, 1) == True:
                return True
        
        return False
        
       