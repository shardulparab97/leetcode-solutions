class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"

        ctr = 2
        val = "1"

        def create_str(val):
            len_val = len(val)

            lo, hi = 0, 0
            new_val = ""
            while hi < len_val:
                while hi < len_val and val[lo] == val[hi]:
                    hi += 1

                new_val += f"{hi-lo}{val[lo]}"
                lo = hi
            
            return new_val



        while ctr <= n:
            val = create_str(val)
            ctr += 1

        return val