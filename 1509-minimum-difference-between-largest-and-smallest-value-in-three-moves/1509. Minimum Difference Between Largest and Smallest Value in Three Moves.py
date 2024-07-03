class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()

        minDiff = float("inf")

        for lo in range(4):
            hi = n - 4 + lo
            minDiff = min(minDiff, nums[hi] - nums[lo])

        return minDiff