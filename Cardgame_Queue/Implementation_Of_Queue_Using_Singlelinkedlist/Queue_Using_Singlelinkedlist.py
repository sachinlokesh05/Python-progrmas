class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# A class to represent a queue

# The queue, front stores the front node
# of LL and rear stores the last node of LL
class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def EnQueue(self, item):
        n = Node(item)

        if self.rear == None:
            self.front = self.rear = n
            return
        self.rear.next = n
        self.rear = n

        # Method to remove an item from queue

    def DeQueue(self):

        if self.isEmpty():
            return
        n1 = self.front
        self.front = n1.next

        if (self.front == None):
            self.rear = None
        return str(n1.data)

    def Display(self):
        t=self.front
        while t!=None:
            print(t.data)
            t=t.next

    # Driver Code


if __name__ == '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)

    print("Dequeued item is " + q.DeQueue())
    q.Display()