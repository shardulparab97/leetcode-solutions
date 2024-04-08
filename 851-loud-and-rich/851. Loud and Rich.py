class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        ans = [None] * n

        for u, v in richer:
            g[v].append(u)

        def dfs(node):
            if ans[node] == None:
                ans[node] = node
                for nei in g[node]:
                    cand = dfs(nei)
                    if (quiet[cand] < quiet[ans[node]]):
                        ans[node] = cand
            return ans[node]

        for i in range(n):
            dfs(i)
        
        return ans

    