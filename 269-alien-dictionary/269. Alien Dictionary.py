class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #TOPOLOGICAL SORT AND POST ORDER DFS
        adj ={ c: set() for word in words for c in word}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = {} #True = visited and path , False = visited
        path = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return ""
            visited[c] = False
            path.append(c)
        for c in adj:
            if dfs(c):
                return ""
        path.reverse()
        return "".join(path)
