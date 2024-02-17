class Node:
    def __init__(self):
        self.isWord = False
        self.children = dict()

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        root = Node()

        # 0(mk) time complexity 
        # making the trie
        for word in wordDict:
            node = root
            for w in word:
                if w not in node.children:
                    node.children[w] = Node()
                node = node.children[w]
            node.isWord = True

        len_s = len(s)
        dp = [False] * len_s

        for i in range(len_s):
            if i == 0 or dp[i-1] == True:
                curr = root # means we have found a word here
                for j in range(i, len_s):
                        ch = s[j]
                        if ch in curr.children:
                            curr = curr.children[ch]
                            if curr.isWord == True:
                                dp[j] = True 
                                if j == len_s - 1:
                                    return True
                        else:
                            break

        return dp[-1]
                    

        