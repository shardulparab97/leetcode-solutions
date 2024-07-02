class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        vis = [False] * n

        ans = float("-inf")
        def dfs(node):
            vis[node] = True
            pq = []
            res = float("-inf")
            for nei in g[node]:
                if vals[nei]>0:
                    heapq.heappush(pq, -1 * vals[nei])
                    if vis[nei] == False:
                        res = max(res, dfs(nei))
            
            sz = len(pq)
            ans = 0
            for i in range(min(k, sz)):
                ans += -1 * heapq.heappop(pq)
            ans += vals[node]
            return max(ans, res)


                


        for i in range(n):
            if not vis[i]:
                ans = max(ans, dfs(i))

        return ans


        


