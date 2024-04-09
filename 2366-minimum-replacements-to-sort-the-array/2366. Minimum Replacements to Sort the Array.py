class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        maxMinVal = nums[n-1]
        ans = 0

        for i in range(n-2, -1, -1):
            parts = math.ceil(nums[i]/maxMinVal)
            ans += (parts - 1)
            maxMinVal = nums[i]//parts
        
        return ans

