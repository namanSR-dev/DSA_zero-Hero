from tree_implement.tree_base import Tree
from collections import deque

# Pattern 6 : BFS traversal
def bfs_traversal(node):
    """returns the level order treaversal of given tree"""
    if not node:
        return []

    q = deque()

    q.append(node)

    bfs_levels = []

    while q:

        level_length = len(q)

        current_level = []

        for _ in range(level_length):
            current_node = q.popleft()

            if current_node.left:
                    q.append(current_node.left)
            
            if current_node.right:
                    q.append(current_node.right)

            current_level.append(current_node.val)

        bfs_levels.append(current_level)

    return bfs_levels


if __name__ == "__main__":

    mytree  = Tree()

    root = mytree.create_tree([1, 2, None, 5, 6,  None, 7])

    mytree.print_tree()

    print(f"\n \n Tree level order traversal : {bfs_traversal(root)}")
        