
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Head node of the list
        self.tail = None  # Tail node 
        self.size = 0  # Counter for number of elements
        print("Created new LinkedList")
        print(f"Current size: {self.size}")
        print("Head: None")

    def append(self, element):
        """Add an element to the end of the list"""
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        """Retrieve an element at a specific index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        print(f"Element at index {index}: {current.data}")
        return current.data

    def set(self, index, element):
        """Replace an element at a specific index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} to {element}")

    def size_of_list(self):
        """Return the current number of elements"""
        print(f"Current size: {self.size}")
        return self.size

    def prepend(self, element):
        """Add an element at the beginning of the list"""
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        print(f"Prepended {element} to the list")

    def print_list(self):
        """Print the linked list elements"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Print Linked list: [" + " ".join(elements) + "]")

# Example usage:
linked_list = LinkedList()
linked_list.append(5)
linked_list.get(0)
linked_list.set(0, 10)
linked_list.get(0)
linked_list.size_of_list()
linked_list.prepend(10)
linked_list.prepend(11)
linked_list.get(0)
linked_list.print_list()
