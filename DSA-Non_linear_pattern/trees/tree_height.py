from tree_implement import Tree

# Pattern 3 - selection in DFS
def tree_height(node):
    """returns the Height of the Tree"""
    if not node:
        return 0
    
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)

    return 1+max(left_height, right_height)



if __name__ == "__main__":

    mytree  = Tree()

    mytree.create_tree("ABCDEFGHI")

    mytree.print_tree()

    print(f"\n \n Tree Height : {tree_height(mytree.root)}")