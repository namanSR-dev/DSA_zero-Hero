import sys
import os

# Add the 'trees' directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
trees_dir = os.path.abspath(os.path.join(current_dir, ".."))
if trees_dir not in sys.path:
    sys.path.append(trees_dir)

from tree_implement import Tree, TreeNode

def create_binary_search_tree(sequence):
    """Helper function for BST class to create the BST"""
    if not sequence or sequence[0] is None:
        return None
    
    root = TreeNode(sequence[0])  # making the first element - a root value

    for value in sequence[1:]:

        # ignoring the null values in the sequence
        if value is None:
            continue

        # for every value - we start with Top
        current_node = root

        # Keep going downward until we find the correct position of the value in the BST
        while True:

            # for smaller values - we go left
            if value < current_node.val:
                if current_node.left is None:
                    current_node.left = TreeNode(value)
                    break
                else:
                    current_node = current_node.left

            # for larger values - we go right
            elif value > current_node.val:
                if current_node.right is None:
                    current_node.right = TreeNode(value)
                    break
                else:
                    current_node = current_node.right
            else:
                break
        
    return root


def bst_deletion( node:TreeNode, value:str )->TreeNode:
    """
    performs the deletion of node in Binary search tree
    """
    # 0. Base case - empty tree or empty branch
    if not node:
        return None

    # 1. search the nade with given value
    if value < node.val:
        node.left = bst_deletion(node.left, value)

    elif value > node.val :
        node.right = bst_deletion(node.right, value)
    
    # 2. once value is found - deletion begin
    else:
        
        # case-1: no child - just delete the node
        if node.left is None and node.right is None:
            return None

        # case-2: only one branch either left or right
        elif not(node.left and node.right):
            return node.left if node.left else node.right

        # case-3: when node as both the childs
        else:
            inorder_successor = node.right
            while inorder_successor.left :
                inorder_successor = inorder_successor.left
            node.val = inorder_successor.val
            node.right = bst_deletion(node.right, inorder_successor.val)

    return node

#---------------New BST Class----------------#

class BST:
    def __init__(self):
        # Composition approach for reusing the methods from standard "Tree" class.
        self._tree = Tree()

    def create_BST(self, sequence):
        """Creates the BST for the given sequence"""
        # Call the helper with the sequence.
        # SAVE the returned top node into your base tree's root attribute!
        self._tree.root = create_binary_search_tree(sequence)
        
        return self._tree.root
    
    def print_BST(self):
        """Prints the corresponding BST"""
        # Method to print the BST as usual level order printing method from the base "Tree" class
        self._tree.print_tree()

    def delete_node(self, value):
        """Deletes a node with the given value"""
        self._tree.root = bst_deletion(self._tree.root, value)
        return self._tree.root




if __name__ == "__main__":
    # A sequence combining symbols and alphabets.
    # Python orders these by ASCII: '#' (35) < 'M' (77) < 'a' (97) < 'z' (122)
    test_sequence = ["0", "M", "F", "a", "#", "A", "k", "$"]
    
    print(f"1. Input Sequence: {test_sequence}\n")
    
    # Initialize your BST class
    my_bst = BST()
    
    # Create the tree structure and fetch the root node reference
    root_node = my_bst.create_BST(test_sequence)
    
    print("2. Visualizing Generated Tree Structure:")
    # Print using your base Tree class method
    my_bst.print_BST() 


    print("Check the delete function:")
    v = input(f"enter the any value from list-{test_sequence} to delete: ")

    root = my_bst.delete_node(v)
    print("The updated Tree is - ")
    my_bst.print_BST()
