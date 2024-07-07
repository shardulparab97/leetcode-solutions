class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        

        q = collections.deque()
        q.append([beginWord, 1])
        vis = set()
        
        wset = set()
        for w in wordList:
            wset.add(w)
        while q:
            w, cnt = q.popleft()

            if w == endWord:
                return cnt

            # iterate over all the possible options
            for i in range(len(w)):
                for j in range(0, 26):
                    if chr(97+j) != w[i]:
                        wc = w[:i] + chr(97+j) + w[i+1:]
                        # print(wc)
                        if wc in wset and wc not in vis:
                            q.append([wc, cnt+1])
                            vis.add(wc)

        return 0
        