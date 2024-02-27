class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # we will use bfs but use two more details
        # i.e. max_min and curr_sum

        # over here BFS will not work due to memory limit
        r, c = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * c for _ in range(r)]

        def get_min_health(currCell, nr, nc):
            if nr>=r or nc >= c:
                return float("inf")

            nextCell = dp[nr][nc]

            return max(1, nextCell - currCell)

        for row in reversed(range(r)):
            for col in reversed(range(c)):
                currCell = dungeon[row][col]

                rh = get_min_health(currCell, row, col+1)
                dh = get_min_health(currCell, row+1, col)
                nextHealth = min(rh, dh)

                if nextHealth != float("inf"):
                    min_health = nextHealth
                else:
                    min_health = 1 if currCell >= 0 else 1 - currCell
                
                dp[row][col] = min_health

        return dp[0][0]





        