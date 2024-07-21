class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # form the graph
        rank = {}
        g = collections.defaultdict(list)
        conn_dict = {}

        for i in range(n):
            rank[i] = None

        for edge in connections:
            u, v = edge[0], edge[1]
            g[u].append(v)
            g[v].append(u)
            conn_dict[(min(u, v), max(u, v))] = 1

        def dfs(node, discovery_rank):
            if rank[node]:
                return rank[node]
            
            rank[node] = discovery_rank
            
            # min_rank tells the smallest rank that can be reached from it 
            min_rank = discovery_rank + 1 # doing plus one because the smallest will be its neighbour
            
            for nei in g[node]:
                if rank[nei] and rank[nei] == discovery_rank - 1:
                    continue
                
                recursive_rank = dfs(nei, discovery_rank + 1)

                if recursive_rank <= discovery_rank:
                    del conn_dict[(min(node, nei), max(node, nei))]
                
                
                min_rank = min(min_rank, recursive_rank)

            return min_rank

        dfs(0, 0)
        res = []
        for u, v in conn_dict:
            res.append([u, v])

        return res

                



        
