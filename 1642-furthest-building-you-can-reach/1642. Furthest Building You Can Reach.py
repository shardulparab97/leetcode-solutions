class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # using DP will cause MLE

        # MIN HEAP is to take the shortest jump 
        # n = len(heights)

        # pq = []
        # for i in range(0, n-1):
        #     # now simply check on the difference and ladders, bricks
        #     dist = heights[i+1] - heights[i]

        #     if dist <= 0:
        #         continue

        #     # else now check on ladders
        #     if ladders > 0:
        #         heapq.heappush(pq, dist)
        #         ladders -= 1
        #     else:
        #         if pq:
        #             dist = heapq.heappop(pq)
        #         bricks -= dist
        #             # ladders += 1
        #         if bricks < 0:
        #             return i
               
        
        # return n-1

        ladder_allocations = [] # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocations) <= ladders:
                continue
            # Otherwise, we will need to take a climb out of ladder_allocations
            bricks -= heapq.heappop(ladder_allocations)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i
        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1
