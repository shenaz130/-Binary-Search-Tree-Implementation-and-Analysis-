class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:  # Corrected from root.value to root.data
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
            
    def pre_order(self, node):
        if not node:
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)
        
    def height(self, node):
        # Base case: If the node is None, return -1 for height
        if node is None:
            return -1
        # Recursively calculate the height of left and right subtrees
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        # Height of the current node is max of left and right subtree heights + 1
        if right_height > left_height:
            return left_height + 1
        else: 
            return right_height + 1


# Create an instance of BinaryTree
bt = BinaryTree()
bt.root = bt.insert(None, 15)  # Start with the root node
bt.insert(bt.root, 5)  # Insert additional nodes
bt.insert(bt.root, 10)
bt.insert(bt.root, 20)
bt.insert(bt.root, 30)
bt.insert(bt.root, 40)
# Print the tree in pre-order traversal
bt.pre_order(bt.root)
print("Height of the tree:", bt.height(bt.root))
