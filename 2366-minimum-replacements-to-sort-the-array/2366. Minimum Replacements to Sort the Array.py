class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        maxMinVal = nums[n-1]
        ans = 0
        
        '''
        For case:
        maxMinVal = 4
        nums[i] = 13
        parts = math.ceil(nums[i] / maxMinVal) = 4
        ans += 4-1 i.e. 3 different ooperations of splitting
        
        now we can split it as 4+4+4+1 or 4+3+3+3 
        but we want to maintain the maxMinVal as high as possible
        that's why we pick 4+3+3+3 
        then we have our new maxMinVal = num[i]//parts = 3
        '''
        
        for i in range(n-2, -1, -1):
            parts = math.ceil(nums[i]/maxMinVal)
            ans += (parts - 1)
            maxMinVal = nums[i]//parts
        
        return ans

