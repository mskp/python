class Stack:

    def __init__(self) -> None:
        self.data = [0 for i in range(50)]
        self.top_of_stack = -1
    
    def is_full(self):
        return self.top_of_stack == len(self.data) - 1

    def is_empty(self):
        return self.top_of_stack == -1
    
    def push(self, value):
        if self.is_full():
            return False
        
        self.top_of_stack += 1
        self.data[self.top_of_stack] = value
    
    def pop(self):
        if self.is_empty():
            return False
        
        deleted = self.data[self.top_of_stack]
        self.top_of_stack -= 1
        return deleted

    def display(self):
        if self.is_empty():
            return False

        for i in range(self.top_of_stack, -1, -1):
            print(str(self.data[i]) + ' ')

if __name__ == 'stack_ds':
# if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(23)
    my_stack.push(45)
    # my_stack.pop()
    # my_stack.pop()
    my_stack.display()
    print(__name__)
