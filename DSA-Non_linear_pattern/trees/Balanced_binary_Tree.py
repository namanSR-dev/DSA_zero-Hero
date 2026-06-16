from tree_implement.tree_base import Tree

def check_balance(node):

    if not node:
        return 0, True
    
    left_height, is_left_balanced = check_balance(node.left)
    right_height, is_right_balanced = check_balance(node.right)

    return 1 + max(left_height, right_height), abs(left_height - right_height) <= 1



if __name__ == "__main__":

    mytree  = Tree()

    mytree.create_tree([1, 2, None, 4, 5])

    mytree.print_tree()

    print(f"\n \n Tree Balanced : {check_balance(mytree.root)[1]}")