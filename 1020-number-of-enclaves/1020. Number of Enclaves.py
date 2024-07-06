class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # do reverse traverse from shore to entry point 
        # check which are used and which not 

        r, c = len(grid), len(grid[0])

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            grid[x][y] = 0 
            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]

                if 0<=nx<r and 0<=ny<c and grid[nx][ny] == 1:
                    dfs(nx, ny)

        
 
        for i in range(r):
            for j in range(c):
                if 1 not in grid[i]:
                    break
                else:
                    if (i==0 or i==r-1 or j==0 or j==c-1) and grid[i][j] == 1:
                        dfs(i, j)

        ans = 0
        print(grid)
        for i in range(r):
            ans += sum(grid[i])

        return ans

        