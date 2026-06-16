from tree_implement.tree_base import Tree
from tree_height import tree_height

# pattern 2 : Aggregation in Tree
def count_nodes(node):
    """return the number of nodes in the tree"""

    if not node:
        return 0
    
    left_count = count_nodes(node.left)
    right_count = count_nodes(node.right)

    return 1 + left_count + right_count


if __name__ == "__main__":

    mytree = Tree()

    mytree.create_tree("ABCDEFGHIJKLMNO")

    mytree.print_tree()

    print(f"\n\n Number of nodes in the Tree : {count_nodes(mytree.root)}")
    print(f"\n Tree Height : {tree_height(mytree.root)}")