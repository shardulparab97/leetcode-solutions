class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        q = collections.deque()

        q.append((0, 0, k, 0))
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        vis = set()
        
        while q:
            x, y, k, dist = q.popleft()

            if (x, y) == (r-1, c-1):
                return dist

            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]

                if 0<=nx<r and 0<=ny<c:
                    new_k = k
                    if grid[nx][ny] == 1:
                        new_k -= 1
                    if new_k >= 0 and (nx, ny, new_k) not in vis:
                        q.append((nx, ny, new_k, dist+1))
                        vis.add((nx, ny, new_k))

        return -1 
