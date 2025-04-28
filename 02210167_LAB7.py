#Task 1: Implement the Node and Binary Tree Class Structure

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        if root is None:
            print("Created new Binary Tree")
            print("Root: None")
        else:
            print(f"Created new Binary Tree\nRoot: {self.root.value}")

#Task 2: Implement Tree Information Methods
from collections import deque

class BinaryTree(BinaryTree):  # Extending the previous BinaryTree class

    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def size(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def count_leaves(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def is_full_binary_tree(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return True
        if (node.left is None and node.right is None):
            return True
        if (node.left is not None) and (node.right is not None):
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    def is_complete_binary_tree(self):
        if self.root is None:
            return True
        queue = deque()
        queue.append(self.root)
        end = False
        while queue:
            node = queue.popleft()
            if node:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            else:
                end = True
        return True

