class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lo, hi = 0, 0
        curr_len = 0
        curr_sum = 0
        ans = 0
        while hi < n:
            num = nums[hi]
            curr_sum += num
            curr_len += 1

            while (curr_sum * curr_len) >= k:
               curr_sum -= nums[lo]
               curr_len -= 1
               lo += 1
            
            ans += hi - lo + 1
            hi += 1
        return ans
        