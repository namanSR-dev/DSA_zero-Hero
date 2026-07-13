from tree_implement.tree_base import Tree
from collections import deque

# Pattern 6 : BFS traversal
def bfs_traversal(node):
    """returns the level order treaversal of given tree"""
    if not node:
        return []

    q = deque()

    q.append(node)

    right_side_view = []

    while q:

        level_length = len(q)

        for i in range(level_length):
            current_node = q.popleft()

            if current_node.left:
                    q.append(current_node.left)
            
            if current_node.right:
                    q.append(current_node.right)

            if i == level_length - 1:
                right_side_view.append(current_node.val)

        

    return right_side_view


if __name__ == "__main__":

    mytree  = Tree()

    root = mytree.create_tree([1, 2, 3, 4, 5])

    mytree.print_tree()

    print(f"\n \n Tree level order traversal : {bfs_traversal(root)}")
        