class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, node, new_val):
        if node.value > new_val:
            if node.left:
                self.insert_helper(node.left, new_val)
            else:
                node.left = Node(new_val)
        else:
            if node.right:
                self.insert_helper(node.right, new_val)
            else:
                node.right = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)
        
    
    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
