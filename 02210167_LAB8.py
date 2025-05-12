# Red-Black Tree Implementation - Part 2
# Implemented by: Jigme Choden Ghalley
# Filename: 02210167_LAB 9.py

class Node:
    def __init__(self, data, color="red", left=None, right=None, parent=None):
        self.data = data
        self.color = color  # red or black
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color="black")  # Sentinel NIL node
        self.root = self.NIL

    def insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if not parent:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        node.color = "red"
        self.fix_insert(node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent and k.parent.color == "red":
            if k.parent == k.parent.parent.left:
                uncle = k.parent.parent.right
                if uncle.color == "red":
                    k.parent.color = "black"
                    uncle.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            else:
                uncle = k.parent.parent.left
                if uncle.color == "red":
                    k.parent.color = "black"
                    uncle.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)

        self.root.color = "black"

    def search(self, key):
        def _search(node, key):
            if node == self.NIL or key == node.data:
                return node
            if key < node.data:
                return _search(node.left, key)
            return _search(node.right, key)

        result = _search(self.root, key)
        return result != self.NIL

    def get_black_height(self):
        def _black_height(node):
            if node == self.NIL:
                return 1
            left_black_height = _black_height(node.left)
            if node.color == "black":
                return left_black_height + 1
            return left_black_height

        return _black_height(self.root)

    def delete(self, key):
        def _minimum(node):
            while node.left != self.NIL:
                node = node.left
            return node

        def _transplant(u, v):
            if not u.parent:
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            v.parent = u.parent

        node = self.root
        while node != self.NIL and node.data != key:
            node = node.left if key < node.data else node.right

        if node == self.NIL:
            print("Node not found!")
            return

        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            _transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            _transplant(node, node.left)
        else:
            y = _minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                _transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            _transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == "black":
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"


# Example Usage:
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    rb_tree.insert(10)
    rb_tree.insert(20)
    rb_tree.insert(30)
    rb_tree.insert(15)
    rb_tree.insert(25)
    rb_tree.insert(5)
    
    print("Search 25:", rb_tree.search(25))  # Should return True
    print("Black Height:", rb_tree.get_black_height())  # Should return appropriate black height

    rb_tree.delete(20)
    print("After Deletion of 20:")
    print("Search 20:", rb_tree.search(20))  # Should return False
    print("Black Height:", rb_tree.get_black_height())  # Should still return valid black height
