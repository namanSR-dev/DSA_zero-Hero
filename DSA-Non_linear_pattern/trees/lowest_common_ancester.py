from bst_implement import BST


def lowest_comman_ancester(node, p, q):
    """return the lowest common ancester of the given p and q node"""

    # Base Case: for leaf nodes
    if not node:
        return None
    
    # when we actually find one of the targets
    if node.val == p or node.val == q:
        return node
    
    # if not then keep exploring the left and right sub-trees
    left_search = lowest_comman_ancester(node.left, p, q)
    right_search = lowest_comman_ancester(node.right, p, q)

    # when we reach the Actual LCA node
    if left_search and right_search:
        return node
    
    # finally propagating the LCA to the top
    return left_search or right_search


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
    lca = lowest_comman_ancester(root_node, 5, 8)
    
    print(f"3. Validation Result: Is this a valid BST? -> {lca}")