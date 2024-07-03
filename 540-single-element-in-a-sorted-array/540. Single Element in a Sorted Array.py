class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        lo, hi = 0, n-1
        ans = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            halves_even = (hi - mid) % 2  == 0
            if mid+1 < n and nums[mid] == nums[mid+1]:
                if halves_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif mid -1 >= 0 and nums[mid] == nums[mid-1]:
                if halves_even:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                ans = nums[mid]
                break
        return ans
            