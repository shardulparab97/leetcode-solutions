class Solution:
    def maxScore(self, nums: List[int]) -> int:
        l1 = [num for num in nums if num>=0]
        ans = len(l1)
        l1_sum = sum(l1)
        if l1_sum <= 0:
            return 0
        
        l2 = [num for num in nums if num<0]
        l2.sort(reverse=True)

        i = 0
        while i < len(l2):
            if l1_sum + l2[i] > 0:
                l1_sum += l2[i]
                i += 1
            else:
                break

        return ans + i 
        