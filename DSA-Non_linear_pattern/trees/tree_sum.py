from tree_implement.tree_base import Tree


# pattern 2 : Aggregation in Tree
def tree_sum(node):
    """returns the sum of values of each node of the Tree"""
    
    if not node:
        return 0
    
    left_sum = tree_sum(node.left)
    right_sum = tree_sum(node.right)

    return node.val + left_sum + right_sum


if __name__ == "__main__":

    mytree  = Tree()

    mytree.create_tree([1,2,3,4,5,6,7])

    mytree.print_tree()

    print(f"\n \n Tree Sum : {tree_sum(mytree.root)}")