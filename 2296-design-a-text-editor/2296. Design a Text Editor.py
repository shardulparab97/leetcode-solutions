class TextEditor:

    def __init__(self):
        self.prefix=[]
        self.suffix=[]
        # print(f"prefix:{"".join(self.prefix)}, suffix:{"".join(self.suffix)}")

        
    def addText(self, text: str) -> None:
        for ch in text:
            self.prefix.append(ch)
        # print(f"prefix:{"".join(self.prefix)}, suffix:{"".join(self.suffix)}")
        

    def deleteText(self, k: int) -> int:
        counter=0
        while len(self.prefix)>0 and counter<k:
            counter+=1
            self.prefix.pop()
        return counter

    def cursorLeft(self, k: int) -> str:
        counter=0
        while len(self.prefix)>0 and counter<k:
            self.suffix.append(self.prefix.pop())
            counter+=1
        mini=min(10,len(self.prefix))
        return "".join(self.prefix[len(self.prefix)-mini:])

    def cursorRight(self, k: int) -> str:
        counter=0
        while len(self.suffix)>0 and counter<k:
            self.prefix.append(self.suffix.pop())
            counter+=1
        mini=min(10,len(self.prefix))
        return "".join(self.prefix[len(self.prefix)-mini:])

        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)