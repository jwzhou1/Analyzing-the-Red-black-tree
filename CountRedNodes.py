import csv


class Node:
    def __init__(self, data):
        self.data = data
        self.color = 'RED'
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None)
        self.NIL_LEAF.color = 'BLACK'
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

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        new_node.parent = None
        new_node.data = data
        new_node.color = 'RED'

        y = None
        x = self.root

        while x != self.NIL_LEAF:
            y = x
            if new_node.data < x.data:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent is None:
            new_node.color = 'BLACK'
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent.color == 'RED':
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left  # Uncle
                if u.color == 'RED':
                    u.color = 'BLACK'
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right  # Uncle

                if u.color == 'RED':
                    u.color = 'BLACK'
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 'BLACK'

    def count_red_nodes(self, node):
        if node == self.NIL_LEAF:
            return 0
        red_nodes_left = self.count_red_nodes(node.left)
        red_nodes_right = self.count_red_nodes(node.right)
        if node.color == 'RED':
            return 1 + red_nodes_left + red_nodes_right
        else:
            return red_nodes_left + red_nodes_right

if __name__ == "__main__":
    tree = RedBlackTree()

    data_list = []

    for i in range(1, 30001):
        tree.insert(i)
        total_nodes = i
        red_nodes = tree.count_red_nodes(tree.root)
        data_list.append([total_nodes, red_nodes])

    with open("CountRedNodes.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Total Nodes", "Red Nodes"])
        writer.writerows(data_list)






