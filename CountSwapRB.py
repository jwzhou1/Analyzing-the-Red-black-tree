import csv

class Node:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, 'BLACK')
        self.root = self.nil
        self.swap_count = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == self.nil:
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

        if x.right != self.nil:
            x.right.parent = y

        x.parent = y.parent

        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert_fixup(self, z):
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'BLACK'

    def insert(self, key):
        z = Node(key, 'RED', self.nil, self.nil, self.nil)
        y = self.nil
        x = self.root

        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        self.insert_fixup(z)

    def count_swaps(self):
        return self.swap_count

    def _count_swaps_recursive(self, node):
        if node == self.nil:
            return 0

        left_swaps = self._count_swaps_recursive(node.left)
        right_swaps = self._count_swaps_recursive(node.right)

        swaps = left_swaps + right_swaps

        if node.color == 'RED':
            swaps += 1

        return swaps

    def count_swaps_in_tree(self):
        return self._count_swaps_recursive(self.root)


def main():
    red_black_tree = RedBlackTree()
    results = []

    for i in range(1, 30001, 1):
        red_black_tree.insert(i)
        swaps = red_black_tree.count_swaps_in_tree()
        results.append((i, swaps))

    # Write the results to a CSV file
    with open("CountSwapRB.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Nodes Added", "Swaps"])
        for result in results:
            csv_writer.writerow(result)

if __name__ == "__main__":
    main()