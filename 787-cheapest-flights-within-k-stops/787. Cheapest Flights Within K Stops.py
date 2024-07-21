class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[] for _ in range(n)]

        for u, v, w in flights:
            g[u].append((v, w))
            # g[v].append((u, w))
        k += 1
        vis = set()
        pq = []
        heapq.heappush(pq, (0, src, k))
        min_dist = float("inf")

        while pq:
            dist, node, k_ = heapq.heappop(pq)

            if (node, k_) in vis:
                continue

            if node == dst:
                return dist
                # min_dist = min(min_dist, dist)
                # continue
            
            vis.add((node, k_))

            for nei, w in g[node]:
                if k_ > 0 and (nei, k_ - 1) not in vis:
                    heapq.heappush(pq, (dist+w, nei, k_ - 1))

        return -1