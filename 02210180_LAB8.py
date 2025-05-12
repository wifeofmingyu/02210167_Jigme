# 02210180_LAB9.py
# AVL Tree Implementation - Part 1 by Pema cheki

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    # Public insert method
    def insert(self, value):
        self.root = self._insert(self.root, value)

    # Internal recursive insert method
    def _insert(self, node, value):
        if not node:
            return AVLNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # Duplicate values not allowed

        # Update height and rebalance
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._rebalance(node)

    # Public delete method
    def delete(self, value):
        self.root = self._delete(self.root, value)

    # Internal recursive delete method
    def _delete(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._rebalance(node)

    # Search method
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    # Return height of tree
    def get_height(self):
        return self._get_height(self.root)

    # Check if the tree is balanced
    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if not node:
            return True
        balance = self._get_balance(node)
        return abs(balance) <= 1 and self._is_balanced(node.left) and self._is_balanced(node.right)

    # Helper methods

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _rebalance(self, node):
        balance = self._get_balance(node)

        # Left Heavy
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._right_rotate(node)         # Left-Left case
            else:
                node.left = self._left_rotate(node.left)  # Left-Right case
                return self._right_rotate(node)

        # Right Heavy
        if balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._left_rotate(node)          # Right-Right case
            else:
                node.right = self._right_rotate(node.right)  # Right-Left case
                return self._left_rotate(node)

        return node

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# Example usage
if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    print(avl_tree.is_balanced())  # Should return True
    print(avl_tree.get_height())   # Should return appropriate height
