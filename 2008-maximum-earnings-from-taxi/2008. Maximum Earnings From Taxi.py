class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        
        pq = []
        n = len(rides)
        maxProfit = 0

        for i in range(n):
            st, en, tip = rides[i]

            while pq and st >= pq[0][0]:
                maxProfit = max(maxProfit, pq[0][1])
                heapq.heappop(pq)
            
            heapq.heappush(pq, (en, en-st+tip + maxProfit))

        ans = -1
        while pq:
            ans = max(ans, pq[0][1])
            heapq.heappop(pq)

        return ans
        

        