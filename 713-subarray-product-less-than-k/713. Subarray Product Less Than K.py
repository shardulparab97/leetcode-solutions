class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        ans = 0
        lo, hi = 0, 0
        prod = 1

        while hi < n:
            val = nums[hi]
            prod *= val

            while prod >= k:
                prod = prod // nums[lo]
                lo += 1

            ans += hi - lo + 1
            hi += 1
        


        return ans

            
