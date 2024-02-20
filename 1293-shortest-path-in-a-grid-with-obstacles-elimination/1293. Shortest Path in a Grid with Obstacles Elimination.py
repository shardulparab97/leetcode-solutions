class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()

        q.append((0, 0, 0, 0)) # x, y, k, steps
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        vis = set()

        while q:
            x, y, k_, steps = q.popleft()
            
            if (x, y) == (m-1, n-1):
                return steps
            
            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]
                

                if 0<=nx<m and 0<=ny<n:
                    k_used = k_
                    if grid[nx][ny] == 1:
                        k_used += 1
                    if k_used<= k and (nx, ny, k_used) not in vis:
                        q.append((nx, ny, k_used, steps+1))
                        vis.add((nx, ny, k_used))
                        

        return -1
            

