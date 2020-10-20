
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start , traversal):
        """ root -> left-> right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


def minHeight(root):
        if root == None:
            return 0
        L = minHeight(root.left)
        R = minHeight(root.right)
        return 1 + (min(L, R) or max(L, R))


#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7

# Set up tree:
# tree.root = BinaryTree(1)
root= Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left=Node(8)
# print(tree.print_tree("preorder"))

print(minHeight(root))
