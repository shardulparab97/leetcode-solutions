class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = float("-inf")
        st = collections.deque()

        for num in preorder:
            while st and st[-1] < num:
                min_limit = st.pop()
            
            if num <= min_limit:
                return False
            
            st.append(num)
        
        return True