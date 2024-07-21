class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # catch is you need to use all the tickets once 
        g = collections.defaultdict(list)

        for u, v in tickets:
            g[u].append(v)
        
        for k in list(g.keys()):
            g[k].sort(reverse=True)

        vis = set()
        g2 = g.copy()
        print(g2)
        ans = []
        def dfs(node):
            # vis.add(node)

            # for nei in g[node]:
            #     nei = graph[node].pop()
            #         dfs(nei)

            while g[node]:
                # using pop is very important
                nei = g[node].pop()
                dfs(nei)
            
            ans.append(node)

        dfs("JFK")
        return ans[::-1]
