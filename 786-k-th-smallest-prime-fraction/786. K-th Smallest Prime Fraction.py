class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        pq = []
        for i in range(n-1, -1, -1):
            for j in range(0, i):
                heapq.heappush(pq, (-arr[j]/arr[i], j, i))
                if len(pq) > k:
                    heapq.heappop(pq)
        
        _, id1, id2 = heapq.heappop(pq)
        return [arr[id1], arr[id2]]

        


