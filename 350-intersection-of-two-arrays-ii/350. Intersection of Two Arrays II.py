class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        mp = collections.defaultdict(int)

        for n1 in nums1:
            mp[n1] += 1
        
        k = 0
        for n2 in nums2:
            if mp[n2] > 0:
                mp[n2] -= 1
                nums1[k] = n2
                k += 1

        return nums1[:k]