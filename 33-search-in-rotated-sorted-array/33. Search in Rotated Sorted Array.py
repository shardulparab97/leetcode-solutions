class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo]<=target<=nums[mid]:
                    hi -= 1
                else:
                    lo += 1
            else:
                if nums[mid]<=target<=nums[hi]:
                    lo += 1
                else:
                    hi -= 1
        return -1