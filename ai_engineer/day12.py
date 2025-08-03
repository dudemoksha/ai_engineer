from collections import deque

# ✅ Class name should start with uppercase by convention
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# ✅ Insert function for Binary Search Tree
def insert(root, value):
    if root is None:
        return Node(value)  # ✅ Node not node (capital N)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# ✅ Inorder Traversal (recursive)
def inorder(node):
    if node:  # ✅ Needed to avoid AttributeError if node is None
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

# ✅ Level Order Traversal (BFS using queue)
def level_order(root):
    if root is None:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.value, end=' ')  # ✅ Keep it on same line
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# ✅ Build the tree from list
values = [1, 3, 4, 2, 4, 5, 23, 3]
root = None
for val in values:
    root = insert(root, val)

# ✅ Run traversals
print("Inorder Traversal:")
inorder(root)

print("\nLevel Order Traversal:")
level_order(root)
