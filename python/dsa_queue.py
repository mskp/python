class Queue:
    def __init__(self) -> None:
        self.data = [0]*10
        self.front, self.rear = -1, -1
    
    def is_full(self):
        return self.rear == len(self.data) - 1

    def is_empty(self):
        return self.rear == self.front

    def insert(self, value):
        if self.is_full():
            return False

        self.rear += 1
        self.data[self.rear] = value
        
        return True

    def delete(self):
        if self.is_empty():
            return False

        self.front += 1
        deleted = self.data[self.front]
        return deleted
    
    def display(self):
        if self.is_empty():
            return False            

        for i in range(self.front+1, self.rear+1):
            print(self.data[i], end=' ')

if __name__ == '__main__':
    queue = Queue()
    queue.insert(45)
    queue.insert(263)
    queue.insert(62)
    queue.delete()
    queue.delete()
    queue.display()

    
    




