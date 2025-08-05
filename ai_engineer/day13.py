class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
def insert(root,value):
    if root is None:
        return Node(value)
    if value<root.value:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root
def search(root,key):
    if root is None:
        return False
    if key==root.value:
        return True
    elif key<root.value:
        return search(root.left,key)
    else:
        return search(root.right,key)
def delete(root,key):
    if root is None:
        return root
    if key<root.value:
        root.left=delete(root.left,key)
    elif key>root.value:
        root.right=delete(root.right,key)
    else:
        if root.left is None and root.right is None:
            return None
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        minimum=mini(root.right)
        root.value=minimum
        root.right=delete(root.right,minimum)
    return root
def mini(node):
    while node.left:
        node=node.left
    return node.value
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,"->",end=" ")
        inorder(root.right)
a=[10,19,28,17,38,90,13,2,14]
root=None
for i in a:
    root=insert(root,i)
print("Inorder Traversal:")
inorder(root)
print("\nSearch for 19:", search(root, 19))
print("Search for 100:", search(root, 100))
root=delete(root,13)
print("Inorder Traversal after deleting 13:")
inorder(root)
        
        
        
        
        
