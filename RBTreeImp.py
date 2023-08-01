import sys

# Node creation
class Node():
    # The Node class represents a single node in the Red-Black Tree.
    # Each node contains an item, pointers to its parent, left child, right child,
    # and a color (0 for black and 1 for red).
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1 # Initializing the color as red (1).


class RedBlackTree():
    # The RedBlackTree class is used to represent the Red-Black Tree.
    # It contains methods for insertion, deletion, and various tree traversals.

    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0  # Color of the sentinel node is black (0).
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # Pre-order traversal
    def pre_order_helper(self, node):
        if node != TNULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # In-order traversal
    def in_order_helper(self, node):
        if node != TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.item + " ")
            self.in_order_helper(node.right)

    # Post-order traversal
    def post_order_helper(self, node):
        if node != TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(node.item + " ")

    # Search the tree
    def search_tree_helper(self, node, key):
        if node == TNULL or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Fix the tree after deleting a node
    # This method fixes the Red-Black Tree properties after a node is deleted from the tree.
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    # Private helper method: __rb_transplant
    # This method is used for node deletion in the tree.
    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion helper method
    # This method deletes a node with a given key from the tree.
    # It uses the __rb_transplant method and also calls delete_fix for fixing the tree.
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    # Fix the tree after inserting a node
    # This method fixes the Red-Black Tree properties after a node is inserted into the tree.
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # Printing the tree helper method
    # This method prints the tree in a tree-like format with indentations.
    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    # Method to find the inorder successor of a given node x in the Red-Black Tree.
    # The inorder successor of a node is the node with the smallest value greater than the given node's value.
    # If the right subtree of the node is not empty, the successor is the minimum node in the right subtree.
    # Otherwise, it climbs up the tree towards the root, until it finds a parent where the given node is in the left subtree.
    # The parent in this case is the successor.
    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    # Method to find the inorder predecessor of a given node x in the Red-Black Tree.
    # The inorder predecessor of a node is the node with the largest value smaller than the given node's value.
    # If the left subtree of the node is not empty, the predecessor is the maximum node in the left subtree.
    # Otherwise, it climbs up the tree towards the root, until it finds a parent where the given node is in the right subtree.
    # The parent in this case is the predecessor.
    def predecessor(self, x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    # Method to perform a left rotation around the given node x in the Red-Black Tree.
    # A left rotation is a tree operation that preserves the binary search tree property
    # and the Red-Black Tree properties while rotating a node and its right child to the left.
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Method to perform a right rotation around the given node x in the Red-Black Tree.
    # A right rotation is a tree operation that preserves the binary search tree property
    # and the Red-Black Tree properties while rotating a node and its left child to the right.
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Method to insert a new node with a given key (value) into the Red-Black Tree.
    # The insertion process starts at the root of the tree and follows the standard binary search tree insertion.
    # After inserting the node, the Red-Black Tree properties might be violated, so the fix_insert() method is called
    # to ensure that the properties are maintained and the tree remains balanced.
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node
        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, item):
        self.delete_node_helper(self.root, item)

    def print_tree(self):
        self.__print_helper(self.root, "", True)


if __name__ == "__main__":
    # This block of code is executed when the script is run as the main program.
    # It demonstrates the usage of the Red-Black Tree class by inserting nodes with keys,
    # printing the tree structure, and then deleting a node with a specific key.

    bst = RedBlackTree() # Creating an instance of the RedBlackTree class.

    # Inserting elements into the Red-Black Tree.
    bst.insert(10)
    bst.insert(18)
    bst.insert(7)
    bst.insert(15)
    bst.insert(16)
    bst.insert(30)
    bst.insert(25)
    bst.insert(40)
    bst.insert(60)

    bst.print_tree()
    print("\nAfter deleting an element")
    # Deleting a node with a specific key from the Red-Black Tree.
    bst.delete_node(40)
    bst.print_tree()
