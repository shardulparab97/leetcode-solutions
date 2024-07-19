class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        r, c = len(board), len(board[0])
        q = collections.deque()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]

        vis = set()
        vis.add((x, y))
        q.append(click)

        while q:
            x, y = q.pop()
            num_mines = 0

            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]

                if 0<=nx<r and 0<=ny<c and board[nx][ny] == 'M':
                    num_mines += 1
                
            if num_mines > 0:
                board[x][y] = str(num_mines)
            
            else:
                board[x][y] = 'B'
                for dir in dirs:
                    nx = x + dir[0]
                    ny = y + dir[1]

                    if 0<=nx<r and 0<=ny<c and (nx, ny) not in vis:
                        vis.add((nx, ny))
                        q.append([nx, ny])

        return board


                
                

            
