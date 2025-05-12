# 02210180_LAB9.py
# AVL Tree Implementation - Part 1 by Pema cheki

class AVLNode:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def _init_(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def search(self, value):
        return self._search(self.root, value)

    def get_height(self):
        return self._get_height(self.root)

    def is_balanced(self):
        return self._is_balanced(self.root)

    def print_tree(self):
        self._print_tree(self.root, "", True)

    # Internal helper methods

    def _insert(self, node, value):
        if not node:
            return AVLNode(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # Duplicate value not inserted

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        return self._balance(node)

    def _delete(self, node, value):
        if not node:
            return node
        elif value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node with two children
            min_larger_node = self._get_min_value_node(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        return self._balance(node)

    def _search(self, node, value):
        if not node:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _is_balanced(self, node):
        if not node:
            return True
        balance = self._get_balance(node)
        return abs(balance) <= 1 and self._is_balanced(node.left) and self._is_balanced(node.right)

    def _balance(self, node):
        balance = self._get_balance(node)

        # Left heavy
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right heavy
        if balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left),
                           self._get_height(x.right))
        return x

    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

    def _print_tree(self, node, indent="", last=True):
        if node:
            print(indent, "`- " if last else "|- ", node.value, sep="")
            indent += "   " if last else "|  "
            self._print_tree(node.left, indent, False)
            self._print_tree(node.right, indent, True)

if __name__== "__main__":
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)

    print("Is balanced?", avl_tree.is_balanced())  # True
    print("Tree height:", avl_tree.get_height())   # 2 or 3 depending on balancing
    print("Tree structure:")
    avl_tree.print_tree()