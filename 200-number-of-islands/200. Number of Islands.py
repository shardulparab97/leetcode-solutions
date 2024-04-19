class Solution:
    

    def run_dfs(self, x, y):

        for i in range(4):
            nx = x + self.dir[i][0]
            ny = y + self.dir[i][1]

            if 0 <= nx < self.m and 0 <= ny < self.n and self.grid[nx][ny] == "1":
                self.grid[nx][ny] = "2"
                self.run_dfs(nx, ny)

        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        # similar to connected components
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        ans = 0

        # using dfs after this and play around with the grid itself
        # for i in range(self.m):
        #     for j in range(self.n):
        #         if self.grid[i][j] == "1":
        #             ans += 1
        #             self.grid[i][j] = "2"
        #             self.run_dfs(i, j)

        
        # for running bfs
        q = collections.deque()
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == "1":
                    q.clear()
                    ans += 1
                    self.grid[i][j] = "2"
                    q.append([i, j])
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx = x + self.dir[k][0]
                            ny = y + self.dir[k][1]

                            if 0 <= nx < self.m and 0 <= ny < self.n and self.grid[nx][ny] == "1":
                                self.grid[nx][ny] = "2"
                                q.append([nx, ny])

        return ans
                                


        return ans
        