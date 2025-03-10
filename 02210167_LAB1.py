

class CustomList:

    def __init__(self, capacity=10):
        """Initialize the list with the given capacity."""
        self._array = [None] * capacity  #underlying array for storage
        self._capacity = capacity  # Maximum size of the list
        self._size = 0  #current no of elements in the list
        print(f"Created new custom list with capacity: {self._capacity}")
        print(f"Current size of the list is: {self._size}")

    def append(self, element):
        """Add an element to the end of the list."""
        if self._size == self._capacity:
            self._resize()
        self._array[self._size] = element
        self._size += 1
        print(f"Appended element: {element} to the list")

    def get(self, index):
        """Get the element at the specific index."""
        if 0 <= index < self._size:
            return self._array[index]
        #raise IndexError("Index out of range")
        else:
            raise IndexError("Index out of range")

    def set(self, index, element):
        """Replace the element at the specific index."""
        if 0 <= index < self._size:
            self._array[index] = element
            print(f"Set element at index {index}: {element}")
        else:
            raise IndexError("Index out of range")

    def size(self):
        """Return the current number of elements in the list."""
        return self._size

    def _resize(self):
        """Resize the array when it reaches full capacity."""
        new_capacity = self._capacity * 2
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
        print(f"Resized the list to capacity: {self._capacity}")


if __name__ == "__main__":
    my_list = CustomList()
    my_list.append(30)
    my_list.append(3)
    print(f"Element at index 0: {my_list.get(0)}")
    my_list.append(0)
    print(f"Element at index 1: {my_list.get(1)}")
    print(f"Current size of the list: {my_list.size()}")
