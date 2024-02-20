class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # use bfs with state machine and solve
        # TC = O(N*K)
        q = collections.deque()

        r, c = len(grid), len(grid[0]) 
        
        vis = set()
        state = (0, 0, 0)
        vis.add(state)

        q.append((state, 0))
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        while q:
            state, dist = q.popleft()

            x, y, k_used = state

            if x == r-1 and y == c-1:
                return dist

            for i in range(4):
                nx = x + dirs[i][0]
                ny = y + dirs[i][1]
                if 0<=nx<r and 0<=ny<c:
                    k_new = k_used
                    if grid[nx][ny] == 1:
                        k_new += 1  # very important do not repeat any variables

                    new_state = (nx, ny, k_new)
                    if k_new <= k and new_state not in vis:
                        vis.add(new_state)
                        q.append((new_state, dist+1))
        
        return -1