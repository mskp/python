class Node:

    def __init__(self, value: any) -> None:
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.size = 0
        self.head: Node = None

    def insert_at_first(self, value: any) -> Node:
        node: Node = Node(value)

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

        node: Node = Node(value)
        temp = self.head

        for i in range(1, index):
            temp = temp.next

        node.next = temp.next
        temp.next = node

    def insert_at_last(self, value: any):
        node: Node = Node(value)
        temp = self.head

        self.size += 1
        while temp.next is not None:
            temp = temp.next

        temp.next = node

    def display(self):
        temp: Node = self.head

        while temp is not None:
            # print(f'{temp.data} -> ', end = "")
            print(temp.data, end=" -> ")
            temp = temp.next
        
        print('END')

if __name__ == '__main__': 

    myList = LinkedList()
    myList.head = myList.insert_at_first(34)
    myList.insert_at_last(45343)
    myList.insert_at_index(3, 26427)
    myList.display()