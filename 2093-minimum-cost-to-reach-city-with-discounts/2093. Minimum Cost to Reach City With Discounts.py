class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        g = [[] for _ in range(n)]

        for h in highways:
            g[h[0]].append((h[1], h[2]))
            g[h[1]].append((h[0], h[2]))

        pq = []
        dist = [float("inf")] * n
        dist[0] = 0
        # very important use of vis set 
        vis = set()
        heapq.heappush(pq, (0, 0, discounts))
        
        while pq:
            dist, node, discount = heapq.heappop(pq)
            if (node, discount) in vis:
                continue
            vis.add((node, discount))
            if node == n-1:
                return dist

            for nei, w in g[node]:
                if (nei, discount) not in vis:
                    heapq.heappush(pq, (dist + w, nei, discount))
                if discount>0 and (nei, discount-1) not in vis:
                    heapq.heappush(pq, (dist + w//2, nei, discount-1))

        return -1

            
