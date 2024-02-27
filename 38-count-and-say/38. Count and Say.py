class Solution:
    def create_string(self, val) -> str:
      
      res = ""
      n = len(val)-1
      lo, hi = 0, 0

      while hi <= n:
          while hi <= n and (val[lo] == val[hi]):
            hi += 1
          
          res += f"{hi-lo}{val[lo]}"
          lo = hi

      return res

    def countAndSay(self, n: int) -> str:
      if n == 1:
        return "1"

      val = "1"
      ctr = 2

      while ctr <= n:
        val = self.create_string(val)
        ctr += 1

      return val


        