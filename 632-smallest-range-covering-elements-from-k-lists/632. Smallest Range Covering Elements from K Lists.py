class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        pq = []
        curr_max = float("-inf")
        for list_id, num in enumerate(nums):
            heapq.heappush(pq, (num[0], list_id, 0))
            curr_max = max(curr_max, num[0])

        # we have already save best values here
        best_min = pq[0][0]
        best_max = curr_max


        while len(pq) == k: # condition that len should be equal to k
            num, list_id, idx = heapq.heappop(pq)

            # over here continue option is much better 
            if idx + 1 <  len(nums[list_id]):
                heapq.heappush(pq, (nums[list_id][idx+1], list_id, idx+1))
                curr_min = pq[0][0]
                curr_max = max(curr_max, nums[list_id][idx+1])
                
                
                if curr_max - curr_min < best_max - best_min:
                    best_min = curr_min
                    best_max = curr_max

        return [best_min, best_max]


            
        
