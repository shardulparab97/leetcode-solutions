class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.ans = 0
        sx, sy, ex, ey = 0, 0, 0, 0
        remaining = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 2:
                    ex, ey = i, j
                elif grid[i][j] != -1:
                    remaining += 1
        vis = set()
        vis.add((sx, sy))
        remaining += 1

        # print(sx, sy, ex, ey)
        def solve(x, y, cnt, vis, remaining):
            # print(x, y)
            if (x, y) == (ex, ey) and remaining == 0:
                # print(ans)
                self.ans += 1
                return
            
            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]

                if 0<=nx<m and 0<=ny<n and grid[nx][ny] != -1:
                    if (nx, ny) not in vis :
                        remaining -= 1
                        vis.add((nx, ny))
                        solve(nx, ny, cnt, vis, remaining)
                        vis.remove((nx, ny))
                        remaining += 1


        solve(sx, sy, 0, vis, remaining)
        return self.ans
                
            

            
       