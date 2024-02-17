class Node: 
    def __init__(self):
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        len_s = len(s)
        root = Node()
        wordDict = set(wordDict)

        for word in wordDict:
            curr = root
            for w in word:
                if w not in curr.children:
                    curr.children[w] = Node()
                curr = curr.children[w]
            curr.children["END"] = word

        # now using backtracking
        path = []
        ans = []
        curr = root
        def solve(idx, curr, path):
            if idx == len(s):
                ans.append(" ".join(path))
            for i in range(idx, len_s):
                ch = s[i]
                if ch in curr.children:
                    curr = curr.children[ch]
                
                    if "END" in curr.children:
                        path.append(curr.children["END"])
                        solve(i+1, root, path)
                        path.pop()
                else:
                    break
        
        solve(0, root, [])
        return ans


        
        

