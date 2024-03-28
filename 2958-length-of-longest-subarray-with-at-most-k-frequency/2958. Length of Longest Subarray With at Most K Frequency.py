class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        lo, hi = 0, 0
        freq = collections.defaultdict(int)

        ans = float("-inf")

        while hi < n:
            val = nums[hi]
            freq[val] += 1
        
            if freq[val] > k:
                while freq[val] > k:
                    freq[nums[lo]] -= 1
                    lo += 1
                
            else:
                ans = max(ans, hi-lo+1)
            
            hi += 1
        
        return ans


