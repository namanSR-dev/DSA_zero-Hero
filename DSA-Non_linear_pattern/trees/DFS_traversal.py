from tree_implement import Tree

# Pattern 1 - Traversal DFS
def preorder_traversal(root):
    if not root:
        return

    yield root.val
    yield from preorder_traversal(root.left)   # python 3.3 featrue : yield from prevent using for loop with yield
    yield from preorder_traversal(root.right)

# Usage:
# result = list(preorder_traversal(myTree.root))

def inorder_traversal(root):
    if not root:
        return

    yield from inorder_traversal(root.left)
    yield root.val  
    yield from inorder_traversal(root.right)


def postorder_traversal(root):
    if not root:
        return

    yield from postorder_traversal(root.left)  
    yield from postorder_traversal(root.right)
    yield root.val

if __name__ == "__main__":

    myTree = Tree()

    myTree.create_tree([1, 2, 3, 4, 5, 6, 7 , 8])

    myTree.print_tree()

    pre = list(preorder_traversal(myTree.root))

    output_string = " -> ".join(map(str, pre))

    print(f"\nPreorder Treversal: {output_string}")


    inr = list(inorder_traversal(myTree.root))

    output_string = " -> ".join(map(str, inr))

    print(f"\nInorder Treversal: {output_string}")


    post = list(postorder_traversal(myTree.root))

    output_string = " -> ".join(map(str, post))

    print(f"\nPostorder Treversal: {output_string}")