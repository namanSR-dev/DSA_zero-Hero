from tree_implement import Tree, TreeNode

def createTree_from_Traversal(inorder: list|str, preorder: list|str = None, postorder: list|str = None) -> TreeNode:
    # value-index map for inorder sequence for O(1) time
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    # Initialize pointers (only the used one needs to be valid, but both declared for nonlocal)
    pre_idx = 0
    pst_idx = len(postorder) - 1 if postorder else -1

    def helper(in_start: int, in_end: int) -> TreeNode:
        # Declare nonlocals flat at the top of the inner function
        nonlocal pre_idx, pst_idx

        # Base condition
        if in_start > in_end:
            return None

        # Determine root value based on available traversal
        if preorder is not None:
            root_val = preorder[pre_idx]
            pre_idx += 1
        elif postorder is not None:
            root_val = postorder[pst_idx]
            pst_idx -= 1
        else:
            raise ValueError("Either preorder or postorder must be provided.")

        root_idx = inorder_map[root_val]
        root = TreeNode(root_val)

        # CRITICAL: Build right child first for postorder, left child first for preorder
        if preorder is not None:
            root.left = helper(in_start, root_idx - 1)
            root.right = helper(root_idx + 1, in_end)
        else:
            root.right = helper(root_idx + 1, in_end)
            root.left = helper(in_start, root_idx - 1)

        return root

    return helper(0, len(inorder) - 1)



if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    
    root = createTree_from_Traversal(inorder, postorder=postorder)
    my_tree = Tree()

    my_tree.root = root

    my_tree.print_tree()