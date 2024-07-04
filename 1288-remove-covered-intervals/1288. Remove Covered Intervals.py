class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        if n==1:
            return 1
        pq = []
        # for interval in intervals:
        #     heapq.heappush(pq, interval)

        heapq.heappush(pq, [intervals[0][0], intervals[0][1]])
        
        # curr_s, curr_en = heapq.heappop(pq)
        for i in range(1, n):
            vis = []
            s, en = intervals[i]
            unused_flag = True
            while pq:
                curr_s, curr_en = heapq.heappop(pq)
                if curr_s<=s and en<=curr_en: # reverse case does not exist, found overlap, breakpoint
                    heapq.heappush(pq, [curr_s, curr_en])
                    unused_flag = False
                    break
                else:
                    vis.append([curr_s, curr_en])
            if unused_flag:
                heapq.heappush(pq, [s, en])
            for v in vis:
                heapq.heappush(pq, v)

        return len(pq)




            


