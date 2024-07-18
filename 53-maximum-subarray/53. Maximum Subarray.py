class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        curr_sum = 0
        pos_flag = False
        for n in nums:
            if n >= 0:
                pos_flag = True
            curr_sum += n
            if curr_sum < 0:
                curr_sum = 0
            ans = max(ans, curr_sum)
        return ans if pos_flag else max(nums)

        