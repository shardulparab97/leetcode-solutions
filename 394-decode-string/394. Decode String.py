class Solution:
    def decodeString(self, s: str) -> str:
        st = collections.deque()
        ans = ""

        for ch in s:
            if ch != ']':
                st.append(ch)
            else:
                temp = []
                cnt = []
                while st and st[-1] != '[':
                    temp.append(st.pop())
                st.pop()
                temp = "".join(temp[::-1])
                # one main issue keep on popping till numbers are there
                while st and '0'<=st[-1]<='9':
                    cnt.append(st.pop())
                cnt = "".join(cnt[::-1])
                temp = temp * int(cnt)
                st.append(temp)
        # print(st)
        return "".join(st)
                    
