class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        freq = [0] * (n + mx + 1)

        ans = 0

        for num in nums:
            freq[num] += 1

        for idx, f in enumerate(freq):
            if f <= 1:
                continue
            ans += f-1
            freq[idx+1] += f-1

        return ans




