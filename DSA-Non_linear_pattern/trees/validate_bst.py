from bst_implement import BST

# for root node the range of left and right would be negative to positive infinity
def validate_BST(node, left_bound = float("-inf"), right_bound = float("inf")):
    """validate the BST"""

    # any empty node is default valid
    if not node:
        return True
    
    # check for the current node first
    if not (left_bound < node.val < right_bound):
        return False
     
    # now checking for the right and left sub_trees

    # left sub-tree can't have value greater then the current node value
    is_left_valid = validate_BST(node.left, left_bound, node.val)

    # right sub-tree can't have value smaller then the current node value
    is_right_valid = validate_BST(node.right, node.val, right_bound)

    # since current node is valid bst node we go to check if its left and right sub-tree both are valid or not
    return is_left_valid and is_right_valid


# ---------------- Test Execution ---------------- #

if __name__ == "__main__":
    # A sequence combining symbols and alphabets.
    test_sequence = [4,1,6,5,8]
    
    print(f"1. Input Sequence: {test_sequence}\n")
    
    # Initialize your BST class
    my_bst = BST()
    
    # Create the tree structure and fetch the root node reference
    root_node = my_bst.create_BST(test_sequence)
    
    print("2. Visualizing Generated Tree Structure:")
    # Print using your base Tree class method
    my_bst.print_BST() 
    print()
    
    # Validate the generated tree
    is_valid = validate_BST(root_node)
    
    print(f"3. Validation Result: Is this a valid BST? -> {is_valid}")