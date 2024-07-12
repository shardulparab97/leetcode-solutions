class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: (x[0], x[1]))
        n = len(events)
        idx = 0
        ans = 0

        pq = []
        curr_day = events[0][0]

        while idx<n:
            # push all items in heap with st == curr_day
            while idx <n and events[idx][0] == curr_day: 
                heapq.heappush(pq, events[idx][1])
                idx += 1
            
            # pop earliest ending event and increment curr_day
            heapq.heappop(pq)
            ans += 1
            curr_day += 1

            # pop out all events which have got over before curr_day
            while pq and pq[0] < curr_day:
                heapq.heappop(pq)

            # if heap is empty, make curr_day equal to the next starting eveny
            if idx<n and not pq:
                curr_day = events[idx][0]

        # for remaining items
        while pq:
            if heapq.heappop(pq) >= curr_day:
                ans += 1
                curr_day += 1
            
        return ans
