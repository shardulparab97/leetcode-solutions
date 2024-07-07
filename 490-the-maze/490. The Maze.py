import collections
class Solution:
    # TC: Very simple O(m.n.(m+n)) --> because we need 
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # simple just keep on doing! Also since we are not interested in distance we just need a simple visited
        # set and not the one with distance
        m, n = len(maze), len(maze[0])

        if start == destination and maze[start[0]][start[1]] != 1:
            return True

        vis = set()

        # only when we have to worry about distance we need to also add the distance param
        vis.add((start[0], start[1]))
        print(start)

        # use deque because O(1) append and popleft/pop
        q = collections.deque()
        q.append(start)

        while q:
            
            x, y = q.popleft()
            

            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                # this is for the direction 
                nx, ny = x, y
                while 0 <= nx + dx < m and 0 <= ny + dy < n and  maze[nx+dx][ny + dy] != 1:
                    nx += dx
                    ny += dy
                
                if (nx, ny) not in vis: 
                    q.append([nx, ny])
                    vis.add((nx, ny))
            
                if [nx, ny] == destination:
                    return True

        return False

            
        