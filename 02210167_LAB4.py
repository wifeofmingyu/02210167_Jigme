# Lab: Queue Implementation
# Pair Programming
# Part 1: Array-based Queue
# Implemented by: [Jigme Choden Ghalley]
# Part 2: Linked List-based Queue
# Implemented by: [Pema Checki]

class ArrayQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0
        print(f"Created new Queue with capacity: {capacity}")
        print(f"Queue is empty: {self.is_empty()}")

    def enqueue(self, element):
        if self.is_full():
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        self.count += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
        if self.is_empty():
            return None
        element = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"Dequeued element: {element}")
        self.display()
        return element

    def peek(self):
        if self.is_empty():
            return None
        element = self.queue[self.front]
        print(f"Front element: {element}")
        return element

    def size(self):
        print(f"Queue size: {self.count}")
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def display(self):
        elements = []
        for i in range(self.count):
            index = (self.front + i) % self.capacity
            elements.append(str(self.queue[index]))
        print(f"Display current queue: [{','.join(elements)}]")


# Example usage to produce the exact requested output
queue = ArrayQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.peek()
queue.dequeue()
queue.size()