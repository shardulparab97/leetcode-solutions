class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # get max time to visit the node and its children
        # if len(relations) == 0:
        #     return time[0]
        g = {i: [] for i in range(1, n+1)}
        for u, v in relations:
            g[u].append(v)

        vis = {}

        def dfs(node):
            if node in vis:
                return vis[node]
        
            max_time = time[node-1]
            for nei in g[node]:
                nei_time = dfs(nei)
                max_time = max(max_time, nei_time + time[node-1])

            vis[node] = max_time
            return vis[node]


        ans = -1
        for i in range(1, n+1):
            if i not in vis:
                res = dfs(i)
                ans = max(ans, res)

        return ans

