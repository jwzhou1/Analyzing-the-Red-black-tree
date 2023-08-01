import csv


class RBNode:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = RBNode(None, "BLACK")
        self.root = self.NIL_LEAF

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL_LEAF:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right != self.NIL_LEAF:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert_fixup(self, z):
        while z.parent and z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right

                if y and y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left

                if y and y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)

        self.root.color = "BLACK"

    def insert(self, key):
        new_node = RBNode(key, "RED", self.NIL_LEAF, self.NIL_LEAF, None)

        y = None
        x = self.root

        while x != self.NIL_LEAF:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y

        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        self.insert_fixup(new_node)

    def count_black_nodes(self, node):
        if node == self.NIL_LEAF:
            return 0

        left_count = self.count_black_nodes(node.left)
        right_count = self.count_black_nodes(node.right)

        if node.color == "BLACK":
            return left_count + right_count + 1
        else:
            return left_count + right_count

    def count_black_nodes_in_range(self, n):
        data = []
        for i in range(1, n + 1):
            self.insert(i)
            black_nodes = self.count_black_nodes(self.root)
            data.append([i, black_nodes])

        with open("CountBlackNodes.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Number of total Nodes", "Black Nodes"])
            writer.writerows(data)

if __name__ == "__main__":
    rb_tree = RedBlackTree()
    rb_tree.count_black_nodes_in_range(30000)
