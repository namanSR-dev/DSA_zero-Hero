from tree_implement import Tree, TreeNode


def iterative_dfs_preorder(root:TreeNode):
    """
    Genearates the DFS Preorder traversal by using iterative approach with the help of stack.
    """
    # Early exit
    if not root:
        return []
    
    stack = [root]
    traversal = []

    # until stack is empty - no node left to visit.
    while stack:
        
        curr_node = stack.pop()
        traversal.append( curr_node.val )

        # Appending the right node first so that Left node get proccessed first ( LIFO )
        if curr_node.right:
            stack.append(curr_node.right)
        
        if curr_node.left:
            stack.append(curr_node.left)

    
    return traversal


def iterative_dfs_postorder(root:TreeNode):

    """
    Genearates the DFS Postorder traversal by using iterative approach with the help of stack.
    """

    # Early exit
    if not root:
        return []

    stack = [root]
    traversal = []

    while stack:
        curr_node = stack.pop()
        traversal.append(curr_node.val)

        # Appending left node first so that right node get proccessed first ( LIFO )
        if curr_node.left: 
            stack.append(curr_node.left)
        if curr_node.right:
            stack.append(curr_node.right)

    return traversal[::-1]


def iterative_dfs_inorder(root:TreeNode):

    """
    Genearates the DFS Inorder traversal by using iterative approach with the help of stack.
    """

    if not root:
        return []

    stack = []
    traversal = []

    curr_node = root

    while curr_node or stack:

        # keep going down from the left side.
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        
        # Can't go down - mark recent node visited

        curr_node = stack.pop()
        traversal.append(curr_node.val)

        # now it's Right sub-tree turn
        curr_node = curr_node.right
    

    return traversal



if __name__ == "__main__":

    my_tree = Tree()

    my_tree.create_tree([1,2,3,4,5,6,7,8,9])

    my_tree.print_tree()

    print("inorder - ",iterative_dfs_inorder(my_tree.root))
    print("preorder - ",iterative_dfs_preorder(my_tree.root))
    print("postorder -",iterative_dfs_postorder(my_tree.root))



