class Solution:
    def removeStars(self, s: str) -> str:
        st = collections.deque()

        for ch in s:
            if ch == '*':
                if st:
                    st.pop()
            else:
                st.append(ch)

        return ''.join(list(st))