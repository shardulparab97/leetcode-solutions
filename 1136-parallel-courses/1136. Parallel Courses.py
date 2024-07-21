class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g = {i : [] for i in range(1, n+1)}

        for u,v in relations:
            g[u].append(v)

        vis = {}
        ans = -1

        def dfs(node):
            if node in vis:
                return vis[node]
            else:
                vis[node] = -1
            ans = 1
            for nei in g[node]:
                child_len = dfs(nei)
                if child_len == -1:
                    return -1 
                ans = max(ans, child_len+1)

            vis[node] = ans
            return vis[node]


        for i in range(1, n+1):
            if i not in vis:
                res = dfs(i)
                if res == -1:
                    return -1 
                ans = max(ans, res)

        return ans