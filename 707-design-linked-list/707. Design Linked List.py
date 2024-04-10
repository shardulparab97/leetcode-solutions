class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
    
class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # self.head_dummy = None
        self.len = 0
    
    def print_nodes(self):
        node = self.tail.prev
        while node is not None:
            print(node.val)
            node = node.prev


        

    def get(self, index: int) -> int:
        if index<0 or index>=self.len:
            return -1

        # self.print_nodes()
        
        if index+1 < self.len - index:
            node = self.head
            for _ in range(index+1):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.len - index):
                node = node.prev

        return node.val
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        prev, succ = self.head, self.head.next
        node.prev = prev
        node.next = succ
        prev.next = node
        succ.prev = node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        prev, succ = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = succ
        succ.prev = node
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.len:
            return
        elif index<0:
            index = 0
        
        if index < self.len - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            succ = prev.next
        else:
            succ = self.tail
            for _ in range(self.len - index):
                succ = succ.prev
            prev = succ.prev
        
        node = Node(val)
        node.prev = prev
        prev.next = node
        node.next = succ
        succ.prev = node
        self.len += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if 0<=index<self.len:
            if index < self.len - index:
                prev = self.head
                for _ in range(index):
                    prev = prev.next
                succ = prev.next.next
            else:
                succ = self.tail
                for _ in range(self.len - index - 1):
                    succ = succ.prev
                prev = succ.prev.prev

            prev.next = succ
            succ.prev = prev
            self.len -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)