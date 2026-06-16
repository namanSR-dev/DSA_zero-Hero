from collections import deque
from .tree_printer import visual_print

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    

    def create_tree(self, elements) -> TreeNode:
        """Builds a level-order tree, respecting None as empty branches."""
    
        if not elements or elements[0] is None:
            self.root = None
            return None
    
        iterator = iter(elements)
        self.root = TreeNode(next(iterator))
        queue = deque([self.root])
    
        while queue:
            current_node = queue.popleft()
    
            for child_side in ("left", "right"):
                try:
                    value = next(iterator)
                    if value is not None:
                        node_child = TreeNode(value)
                        setattr(current_node, child_side, node_child)
                        queue.append(node_child)
                    else:
                        # Explicitly leave the attribute as None (empty branch)
                        setattr(current_node, child_side, None)
                except StopIteration:
                    return self.root
        return self.root




     # --- EXTENSION BINDS HERE ---
    # We import and bind the function as a method dynamically
    def print_tree(self):
        """Prints a pretty visual layout of the current tree."""
        visual_print(self.root)



if __name__ == "__main__":

    my_tree = Tree()

    elements = ["A", "B", "C", "D", "E", "F", "G" , "H", "I"]

    my_tree.create_tree(elements)

    my_tree.print_tree()

            






