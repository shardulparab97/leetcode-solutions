class Node:
    def __init__(self):
        self.children = {}
        self.sentences = collections.defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node()
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = Node()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)

    def add_to_trie(self, sentence, count):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            node.sentences[sentence] += count

    def input(self, c: str) -> List[str]:
        
        if c == "#":
            curr_sentence = "".join(self.curr_sentence)
            self.add_to_trie(curr_sentence, 1)
            self.curr_node = self.root
            self.curr_sentence = []
            return []
        
        self.curr_sentence.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []
        
        self.curr_node = self.curr_node.children[c]
        sentences = self.curr_node.sentences
        sorted_sentences = sorted(sentences.items(), key=lambda x: (-x[1], x[0]))
        ans = []
        for i in range(min(3, len(sorted_sentences))):
            ans.append(sorted_sentences[i][0])

        return ans

    
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)