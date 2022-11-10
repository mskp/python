class LinkedList:
    
    class Node:

        def __init__(self, value: any) -> None:
            self.data = value
            self.next = None
            
    def __init__(self) -> None:
        self.size = 0
        self.head: self.Node = None

    def insert_at_first(self, value: any) -> Node:
        node: self.Node = self.Node(value)

        self.size += 1
        if self.head is None:
            head = node
            return head

        node.next = head
        head = node
        
        return head

    def insert_at_index(self, index: int, value: any) -> None:
        self.size += 1

        if index == 0: 
            return self.insert_at_first(value)

        elif index == self.size: 
            return self.insert_at_last(value)

        node: self.Node = self.Node(value)
        temp = self.head

        for i in range(1, index):
            temp = temp.next

        node.next = temp.next
        temp.next = node

    def insert_at_last(self, value: any):
        node: self.Node = self.Node(value)
        temp = self.head

        self.size += 1
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        
        print('END')

if __name__ == '__main__': 
   list = LinkedList()
   list.head = list.insert_at_first('s')
   list.insert_at_last('u')
   list.insert_at_last('s')
   list.display()
