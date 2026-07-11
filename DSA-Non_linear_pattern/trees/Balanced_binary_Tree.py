from tree_implement import Tree

#Pattern 4:  Multi-state return
def check_balance(node):

    if not node:
        return 0, True
    
    left_height, is_left_balanced = check_balance(node.left)
    right_height, is_right_balanced = check_balance(node.right)

    return 1 + max(left_height, right_height),  is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1



if __name__ == "__main__":

    mytree  = Tree()

    mytree.create_tree([1, 2, 3, 4, None, None, 5, 6, None, None, 7])

    mytree.print_tree()

    print(f"\n \n Tree Balanced : {check_balance(mytree.root)[1]}")