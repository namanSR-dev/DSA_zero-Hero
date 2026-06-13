from collections import deque
from tree_printer import visual_print

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    

    def create_tree(self, elements) -> TreeNode:
        """Builds the Level ordered complete Binary Tree"""

        iterator = iter(elements)

        # base case: setting the root first
        try:
            self.root = TreeNode(next(iterator))
        except StopIteration:
            self.root = None
            return self.root
        
        
        queue = deque([self.root])    # waiting order queue for level order insertion
        
        while queue:
            current_node = queue.popleft()
            # setting the right and left nodes
            for child_side in ("left", "right"):
                
                try:
                    value = next(iterator)
                    node_child = TreeNode(value)

                    # Dynamically setting the attribut of the node object
                    setattr(current_node, child_side, node_child)

                    queue.append(node_child)

                except StopIteration:
                    queue.clear()  # clearing the queue once task done
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

            






