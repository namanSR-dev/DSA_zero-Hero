from tree_implement.tree_base import Tree


# Pattern 3 - selection in DFS
def tree_max_path(node):
    """return the max path sum of the tree"""

    if not node:
        return 0
    
    left_best = tree_max_path(node.left)
    right_best = tree_max_path(node.right)

    return node.val + max(left_best, right_best)


if __name__ == "__main__":

    mytree  = Tree()

    mytree.create_tree([1,2,3,4,5,6,7])

    mytree.print_tree()

    print(f"\n \n Tree max path : {tree_max_path(mytree.root)}")