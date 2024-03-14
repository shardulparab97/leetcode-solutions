class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key= lambda x: (x[0], x[1]))
        pq = []
        ans = 0
        i =0
        n = len(events)

        curr_day = events[0][0]

        while i<n:
            while i<n and events[i][0] == curr_day:
                heapq.heappush(pq, events[i][1])
                i += 1
            
            # attend the earliest event 
            heapq.heappop(pq)
            ans += 1
            curr_day += 1



            # events have ended and can't do anything
            while pq and pq[0]<curr_day:
                heapq.heappop(pq)
            
            if i<n and not pq:
                curr_day = events[i][0]

            
        while pq:
            if heapq.heappop(pq) >= curr_day:
                curr_day += 1
                ans += 1
        
        return ans