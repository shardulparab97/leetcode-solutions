class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for st, en, p in zip(startTime, endTime, profit):
            jobs.append((st, en, p))

        jobs.sort()

        n = len(jobs)
        pq = []
        maxProfit = 0
        for i in range(n):
            st, en, p = jobs[i]

            while pq and st >= pq[0][0]:
                maxProfit = max(maxProfit, pq[0][1])
                heapq.heappop(pq)

            heapq.heappush(pq, (en, p + maxProfit))

        ans = -1
        while pq:
            ans = max(ans, pq[0][1])
            heapq.heappop(pq)

        return ans


