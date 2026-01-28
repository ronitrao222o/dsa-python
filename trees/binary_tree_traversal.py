class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
