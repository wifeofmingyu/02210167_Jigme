# Lab: Stack Implementation
# Pair Programming
# Part 1: Array-based Stack
# Implemented by: Pema cheki 02210180
# Part 2: Linked List-based Stack
# Implemented by: Jigme Choden Galley 02210167


class ArrayStack:
    def __init__(self, capacity=10):
        """
        Constructor to initialize the stack with a default capacity.
        """
        self.capacity = capacity  # Set the maximum size of the stack
        self.stack = [None] * self.capacity  # Create an array of fixed size
        self.top = -1  # Initialize top pointer to -1, indicating an empty stack
        print(f"Created new ArrayStack with capacity: {self.capacity}")

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return self.top == -1

    def push(self, element):
        """
        Add an element to the top of the stack.
        """
        if self.top == self.capacity - 1:
            print("Stack Overflow! Cannot push element.")
            return
        self.top += 1  # Move the top pointer up
        self.stack[self.top] = element  # Store the element at the new top position
        print(f"Pushed {element} to the stack")

    def pop(self):
        """
        Remove and return the element at the top of the stack.
        """
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        popped_element = self.stack[self.top]  # Get the top element
        self.stack[self.top] = None  # Remove reference for garbage collection
        self.top -= 1  # Move the top pointer down
        print(f"Popped element: {popped_element}")
        return popped_element

    def peek(self):
        """
        Return the element at the top without removing it.
        """
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        print(f"Top element: {self.stack[self.top]}")
        return self.stack[self.top]

    def size(self):
        """
        Return the current number of elements in the stack.
        """
        print(f"Stack size: {self.top + 1}")
        return self.top + 1

    def display(self):
        """
        Show all elements in the stack.
        """
        if self.is_empty():
            print("Stack is empty!")
        else:
            print(f"Display stack: {self.stack[:self.top + 1]}")

# Example usage:
stack = ArrayStack()  # Create a stack with default capacity 10
print("Stack is empty:", stack.is_empty())  # Check if the stack is empty

stack.push(10)  # Push 10
stack.display()
stack.push(20)  # Push 20
stack.display()
stack.push(30)  # Push 30
stack.display()

stack.peek()  # Peek top element
stack.pop()   # Pop top element
stack.size()  # Get stack size
stack.display()
