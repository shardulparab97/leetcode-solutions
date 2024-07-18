class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        n = len(digits)
        mp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
                
        ans = []

        def backtrack(idx, curr_str):
            if idx == n:
                ans.append(''.join(curr_str))
                return
            
            for ch in mp[digits[idx]]:
                curr_str.append(ch)
                backtrack(idx+1, curr_str)
                curr_str.pop()

        backtrack(0, [])

        return ans

        