class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # words = list(set(words))
        g = {c: set() for word in words for c in word}

        for w_idx in range(len(words) - 1):
            w1 = words[w_idx]
            w2 = words[w_idx + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            else:
                for i in range(min_len):
                    if w1[i] != w2[i]:
                        g[w1[i]].add(w2[i])
                        break

        


        ans = collections.deque()
        vis = set()
        inCycle = set()

        def dfs(node):
            # print(node)
            vis.add(node)
            inCycle.add(node)

            # check for cycles
            for nei in g[node]:
                if nei not in vis:
                    if dfs(nei) == False:
                        return False
                elif nei in inCycle:
                    return False

            inCycle.remove(node)
            ans.appendleft(node)
            return True
        # print(g)
        # for node, _ in g.items():
        #     print(node)
        for node in list(g.keys()):
            # print(node)
            if node not in vis:
                if dfs(node) == False:
                    return ""

        return ''.join(list(ans))
