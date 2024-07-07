class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque()

        wset = set()
        for w in wordList:
            wset.add(w)

        q.append([beginWord, 1])
        vis = set()
        vis.add(beginWord)
        while q: 
            w, cnt = q.popleft()

            if w == endWord:
                return cnt

            for i in range(len(w)):
                for c in range(0, 26):
                    if chr(97+c) != w[i]:
                        new_word = w[:i] + chr(97 + c) + w[i+1:]
                        if new_word in wset and new_word not in vis:
                            q.append([new_word, cnt+1])
                            vis.add(new_word)

        return 0
