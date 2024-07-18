class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.isWord = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode('')
        wordDict = set(wordDict)
        for word in wordDict:
            curr = root
            for w in word:
                if w not in curr.children:
                    node = TrieNode(w)
                    curr.children[w] = node
                curr = curr.children[w]

            curr.isWord = True
        
        n = len(s)
        dp = [False] * n
        i = 0

        for i in range(n):
            if i == 0 or dp[i-1] == True:
                curr = root
                for j in range(i, n):
                    if s[j] in curr.children:
                        curr = curr.children[s[j]]
                        if curr.isWord:
                            dp[j] = True
                            if j == n - 1:
                                return True
                    else:
                        break

        return dp[-1]