class Solution:
    def decodeString(self, s: str) -> str:
        st = collections.deque()
        ans = ""

        curr_num = 0
        curr_str = ""
        # very important in the case the size does not fit
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num*10 + int(ch)
            elif ch == '[':
                st.append((curr_str, curr_num))
                curr_num = 0
                curr_str = ''
            elif ch == ']':
                prev_str, multiplier = st.pop()
                curr_str = prev_str + curr_str * multiplier
            else:
                curr_str += ch
        
        return curr_str

        
                    
