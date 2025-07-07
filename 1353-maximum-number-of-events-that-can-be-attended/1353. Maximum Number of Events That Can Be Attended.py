class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key = lambda x: (x[0], x[1]))

        pq = []
        ans = 0
        curr_day = events[0][0]
        idx = 0

        while idx<n: 
            
            # push all events starting before curr_day
            while idx<n and events[idx][0] == curr_day:
                heapq.heappush(pq, events[idx][1])
                idx += 1

            # complete 1 event
            heapq.heappop(pq)
            ans += 1
            curr_day += 1

            # remove all events ending before curr day
            while pq and pq[0] < curr_day:
                heapq.heappop(pq)

            # if pq is empty, move curr_day to next starting item 
            if idx < n and not pq:
                curr_day = events[idx][0]

        # if the heap is still not empty
        while pq:
            if heapq.heappop(pq) >= curr_day:
                ans += 1
                curr_day += 1

        return ans

            
            

            
