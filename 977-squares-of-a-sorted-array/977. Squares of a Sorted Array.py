class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lo = 0
        hi = n-1
        result = [None] * n

        for i in range(n-1, -1, -1):
            if abs(nums[lo]) < abs(nums[hi]):
                val = nums[hi]
                hi -= 1
            else:
                val = nums[lo]
                lo += 1
            result[i] = val * val
        
        return result
        