# A class that represents the individual node in a BST.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None

# Function to insert a new node with the given key
def insert(root, new_key):
    if root is None:
        root = TreeNode(new_key)
        return root
    if new_key < root.key:
        root.l = insert(root.l, new_key)
    else:
        root.r = insert(root.r, new_key)
    return root

# Function to find the specific key in the tree recursively
def find(self, find_key):
    if self.key == find_key:
        print("Key exists in tree")
        return
    if self.key > find_key:
        if self.l:
            find(self.l, find_key)
        else:
            print("Key does not exist in tree")
    else:
        if self.r:
            find(self.r, find_key)
        else:
            print("Key does not exist in tree")

# Function to display the output of the tree
def display(root):
    if root:
        display(root.l)
        print(root.key)
        display(root.r)


r = TreeNode(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

display(r)

find(r, 30)
