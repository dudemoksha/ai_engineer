class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # height of leaf is 1

# Helper: Get height
def get_height(node):
    if not node:
        return 0
    return node.height

# Helper: Get balance factor
def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

# Right rotation (LL)
def rotate_right(z):
    y = z.left
    T3 = y.right

    # Rotation
    y.right = z
    z.left = T3

    # Update heights
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

# Left rotation (RR)
def rotate_left(z):
    y = z.right
    T2 = y.left

    # Rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

# AVL Insert
def insert(root, key):
    # 1. Normal BST insert
    if not root:
        return AVLNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # 2. Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # 3. Get balance factor
    balance = get_balance(root)

    # 4. Balance the tree

    # Case 1: Left Left
    if balance > 1 and key < root.left.key:
        return rotate_right(root)

    # Case 2: Right Right
    if balance < -1 and key > root.right.key:
        return rotate_left(root)

    # Case 3: Left Right
    if balance > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Case 4: Right Left
    if balance < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

# Preorder print for testing
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

# Test AVL insert
if __name__ == "__main__":
    root = None
    values = [10, 20, 30, 40, 50, 25]

    for v in values:
        root = insert(root, v)

    print("Preorder traversal of AVL tree:")
    preorder(root)
    print()
