class Node:
    def __init__(self, key):
        """Initialize a node with the given key."""
        self.left = None
        self.right = None
        self.value = key
class BST:
    def __init__(self):
        """Initialize an empty Binary Search Tree."""
        self.root = None
    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)
    def _insert_rec(self, node, key):
        """Helper method to insert a new key recursively."""
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)
    def search(self, key):
        """Search for a key in the BST and return True if found, else False."""
        return self._search_rec(self.root, key)
    def _search_rec(self, node, key):
        """Helper method to search for a key recursively."""
        if node is None:
            return False
        if node.value == key:
            return True
        elif key < node.value:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)
    def inorder_traversal(self):
        """Return a list of values in the BST in inorder."""
        return self._inorder_rec(self.root)
    def _inorder_rec(self, node):
        """Helper method for inorder traversal."""
        return (self._inorder_rec(node.left) if node.left else []) + \
               [node.value] + \
               (self._inorder_rec(node.right) if node.right else [])
# Testing the BST implementation
if __name__ == "__main__":
    bst = BST()
    numbers = [7, 3, 9, 1, 5, 8, 10]  
    for number in numbers:
        bst.insert(number)
    print("Inorder Traversal:", bst.inorder_traversal())
    print("Search for 5:", bst.search(5))  # Should return True
    print("Search for 6:", bst.search(6))  # Should return False