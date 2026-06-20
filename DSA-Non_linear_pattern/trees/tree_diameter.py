from tree_implement.tree_base import Tree

# Pattern 5 : Multiple Information + Global Aggregation
def tree_diameter(node):
    """return the diameter: max number of edges between two leaf nodes"""
    if not node:
        return 0,0
    
    left_height, left_diameter = tree_diameter(node.left)  
    right_height, right_diameter = tree_diameter(node.right)

    
    current_height = max(left_height, right_height) + 1

    # This pattern check 3 cases : 

    # 1. Either - diameter is inside the left subtree
    # 3. OR - diammeter is pass through the current node 
    # 2. OR - diameter is inside the right subtree
    current_diameter = max(left_height + right_height, max(left_diameter, right_diameter))

    return current_height, current_diameter

if __name__ == "__main__":

    mytree  = Tree()

    mytree.create_tree([1, 2, None, 5, 6,  None, 7])

    mytree.print_tree()

    print(f"\n \n Tree diameter : {tree_diameter(mytree.root)[1]}")