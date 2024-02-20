class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # we do know it is going to be in this range
        n = len(nums)
        nums.sort() 
        
        lo, hi = 0, nums[-1] - nums[0]
        ans = -1

        # [1, 1, 2, 5, 7, 9, 10]

        # [1, 1, 2, 5]

        # 0 to 4
        # [0, 1, 4, 0, 1, 4, 1, 1, 3, 4, 4, 3]

        # [0, 0, 1, 1, 1, 1, 3, 3, 4, 4, 4 ,4]
        # k = 3
        # 0 to 9
        # 4, mid = 2
        def check(dist):
            i, j, cnt = 0, 0, 0
            for i in range(n):
                while j < n and nums[j]-nums[i] <= dist:
                    cnt += j-i
                    j += 1
            return cnt >= k

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else: 
                lo = mid + 1
        
        return ans

        # 0, 2, 2
        
        # [0, 10] --> 5, k = 4 --> <=8 

        # 0, 5, 6, 9, 10
        # n^2 pairs
        # n^2 log n^2

        # 0, 5, 5
