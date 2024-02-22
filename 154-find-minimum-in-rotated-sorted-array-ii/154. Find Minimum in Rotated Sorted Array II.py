class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n-1

        ans = float("inf")
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[lo] == nums[mid] == nums[hi]:
                ans = min(ans, nums[mid])
                lo += 1
                hi -= 1
                continue

            if nums[lo] <= nums[mid]:
                ans = min(ans, nums[lo])
                lo = mid+1
            else:
                ans = min(ans, nums[mid])
                hi = mid-1
        
        return ans
