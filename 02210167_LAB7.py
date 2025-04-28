class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        print("Created new Binary Tree")
        print(f"Root: {self.root.value if self.root else 'None'}")

    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_height = self.height(node.left) if node.left else 0
        right_height = self.height(node.right) if node.right else 0
        return 1 + max(left_height, right_height)

    def size(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_size = self.size(node.left) if node.left else 0
        right_size = self.size(node.right) if node.right else 0
        return 1 + left_size + right_size

    def count_leaves(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        left_leaves = self.count_leaves(node.left) if node.left else 0
        right_leaves = self.count_leaves(node.right) if node.right else 0
        return left_leaves + right_leaves

    def is_full_binary_tree(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return True
        if (node.left is None and node.right is None):
            return True
        if (node.left is not None and node.right is not None):
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    def is_complete_binary_tree(self):
        if self.root is None:
            return True

        queue = [self.root]
        found_none = False

        while queue:
            current = queue.pop(0)
            if current:
                if found_none:
                    return False
                queue.append(current.left)
                queue.append(current.right)
            else:
                found_none = True
        return True

# Example usage:
if __name__ == "__main__":
    # Create an empty Binary Tree
    tree = BinaryTree()

    # Now manually assign nodes
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Tree Height:", tree.height())
    print("Total Nodes:", tree.size())
    print("Leaf Nodes Count:", tree.count_leaves())
    print("Is Full Binary Tree:", tree.is_full_binary_tree())
    print("Is Complete Binary Tree:", tree.is_complete_binary_tree())