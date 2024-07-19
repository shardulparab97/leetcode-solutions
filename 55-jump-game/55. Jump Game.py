class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return True

        midx = -1
        goal = n-1

        # we have to just check till where can it do max index
        for i in range(n-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
        