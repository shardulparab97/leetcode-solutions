class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ans = 0

        s_ptr, t_ptr = 0, 0
        s_len, t_len = len(source), len(target)
        old_t_ptr = 0

        while t_ptr < t_len:
            if source[s_ptr] == target[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                s_ptr += 1

            if s_ptr == s_len:
                if t_ptr == old_t_ptr:
                    return -1
                else:
                    old_t_ptr = t_ptr
                ans += 1
                if t_ptr != t_len:
                    s_ptr = 0

        return ans+1 if s_ptr < s_len else ans
    
            

        