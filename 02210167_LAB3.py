# Lab: Stack Implementation
# Pair Programming
# Part 1: Array-based Stack
# Implemented by: [Pema Checki]
# Part 2: Linked List-based Stack
# Implemented by: [Jigme Choden Ghalley]

class Node:
    """ Node class for representing stack elements. """
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Reference to the next node

class LinkedStack:
    """ Stack implementation using a linked list. """
    def __init__(self):
        self.top = None  # Reference to the top node (head of the list)
        self.size_counter = 0  # Track the number of elements
        print("Created new LinkedStack")

    def is_empty(self):
        """ Check if the stack is empty. """
        return self.top is None

    def push(self, element):
        """ Add an element to the top of the stack. """
        new_node = Node(element)  # Create a new node
        new_node.next = self.top  # Link it to the current top
        self.top = new_node  # Update top to the new node
        self.size_counter += 1  # Increase the size counter
        print(f"Pushed {element} to the stack")

    def pop(self):
        """ Remove and return the element at the top of the stack. """
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        popped_element = self.top.data  # Get data from top node
        self.top = self.top.next  # Move top to the next node
        self.size_counter -= 1  # Decrease the size counter
        print(f"Popped element: {popped_element}")
        return popped_element

    def peek(self):
        """ Return the element at the top without removing it. """
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data

    def size(self):
        """ Return the current number of elements in the stack. """
        print(f"Stack size: {self.size_counter}")
        return self.size_counter

    def display(self):
        """ Show all elements in the stack. """
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        stack_elements = []
        while current:
            stack_elements.append(current.data)
            current = current.next
        print(f"Display stack: {stack_elements}")

    def current_stack(self):
        """Show all elements in stack in the format: Current stack: 20-> 10-> null"""
        if self.is_empty():
            print("Current stack: null")
            return
        current = self.top
        stack_elements = []
        while current:
            stack_elements.append(str(current.data))
            current=current.next
        stack_str= "->".join(stack_elements) + "-> null"
        print("Current stack: ", stack_str)

# Example usage
stack = LinkedStack()
print("Stack is empty:", stack.is_empty())

stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.current_stack()

stack.peek()
stack.pop()
stack.display()
stack.size()