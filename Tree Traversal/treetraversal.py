class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node:
        print(node.value, end=', ')  # Visit the root node
        pre_order_traversal(node.left)  # Traverse the left subtree
        pre_order_traversal(node.right)  # Traverse the right subtree

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(8)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(10)
root.right.left.left = TreeNode(11)
root.right.left.right = TreeNode(12)

# Performing pre-order traversal
pre_order_traversal(root)  # Output: A B D E C F
