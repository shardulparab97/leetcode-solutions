class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = [[] for _ in range(n)]

        for r in relations:
            g[r[0]-1].append(r[1]-1)

        # will store distance
        vis = {}
        def dfs(node):
            if node in vis:
                return vis[node]
            
            max_len = float("-inf")

            for nei in g[node]:
                len = dfs(nei)
                max_len = max(max_len, len + time[node])
            vis[node] = max_len if max_len != float("-inf") else time[node]
            return vis[node]
                

        ans = float("-inf")
        for i in range(n):
            if i not in vis:
                curr_len = dfs(i)
                ans = max(ans, curr_len)

        return int(ans)