class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        pq = []
        dist = [float("inf")] * n

        dist[k-1] = 0
        heapq.heappush(pq, (0, k-1))

        for t in times:
            u, v, w = t
            g[u-1].append((v-1, w))

        while len(pq) > 0:
            d, idx = heapq.heappop(pq)

            for nei in g[idx]:
                nei_idx, nei_dist = nei
                if (d + nei_dist) < dist[nei_idx]:
                    dist[nei_idx] = d + nei_dist
                    heapq.heappush(pq, (dist[nei_idx], nei_idx))
        
        if dist.count(float("inf")) > 0:
            return -1
        return max(dist)

        