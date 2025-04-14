# Part 2: Linked List-based Queue Implementation
# Implemented by: Pema cheki
# Pair Programming Partner: Jigme Choden galley implemented  Array-based Queue

# Task 3: Implement the Node and LinkedQueue Class Structure
class Node:
    def __init__(self, data):  # Node class with data and next reference
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):  # Initializing front, rear, and size counter
        self.front = None
        self.rear = None
        self.size_counter = 0
        print("Created new LinkedQueue")

    # Task 4: Implement Linked List-based Queue Operations
    def is_empty(self):  # Check if queue is empty
        return self.size_counter == 0

    def enqueue(self, element):  # Add an element to the rear
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size_counter += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):  # Remove and return the front element
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size_counter -= 1
        print(f"Dequeued element: {removed_data}")
        self.display_current()
        return removed_data

    def peek(self):  # Return the front element without removing it
        if self.is_empty():
            print("Queue is empty, no front element")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data

    def size(self):  # Return the current number of elements
        print(f"Queue size: {self.size_counter}")
        return self.size_counter

    def display(self):  # Show all elements in the queue in [x,y,z] format
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"Display queue:[{','.join(elements)}]")

    def display_current(self):  # Show all elements in the queue in x -> y -> z -> null format
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Current queue: " + " -> ".join(elements) + " -> null")

# Example usage
queue = LinkedQueue()
print("Queue is empty:", queue.is_empty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.peek()
queue.dequeue()
queue.size()
