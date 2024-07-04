class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        idx = 0

        curr_char = ''
        cnt_char = 0
        i = 0

        while i < n:
            if cnt_char == 0:
                curr_char = chars[i]

            if chars[i] == curr_char:
                cnt_char += 1
            else:
                if cnt_char == 1:
                    chars[idx] = curr_char
                    idx += 1
                else:
                    chars[idx] = curr_char
                    idx += 1
                    cnt_char = list(str(cnt_char))
                    for cnt in cnt_char:    
                        chars[idx] = cnt
                        idx += 1

                i -= 1
                cnt_char = 0
            i += 1
            # now only for the last case
        if cnt_char == 1:
                chars[idx] = curr_char
                idx += 1
        else:
                chars[idx] = curr_char
                idx += 1
                cnt_char = list(str(cnt_char))
                for cnt in cnt_char:    
                        chars[idx] = cnt
                        idx += 1

                
        return idx
                

