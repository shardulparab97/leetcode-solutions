class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg = set()
        
        for n in nums:
            if n<0:
                neg.add(n)

        ans = -1
        for n in nums:
            if n>ans and -n in neg:
                ans = n

        return ans
