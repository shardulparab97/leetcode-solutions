class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        q = collections.deque()

        g = [[] for _ in range(n)]

        for f in flights:
            g[f[0]].append((f[1], f[2]))
            # g[f[1]].append((f[0], f[2]))

        # k, node, distance
        q.append((0, src, 0))
        dist[src] = 0

        while q:
            stops, node, distance = q.popleft()

            for n in g[node]:
                if stops > k: 
                    continue
                next_node = n[0]
                edge_weight = n[1]
                if (dist[next_node] > distance + edge_weight) and stops<=k : # important because last node stop is not counted
                    dist[next_node] = distance + edge_weight
                    q.append((stops+1, next_node, dist[next_node]))
        
        return dist[dst] if dist[dst] != float("inf") else -1
                



