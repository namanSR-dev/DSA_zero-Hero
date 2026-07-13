from tree_implement import TreeNode, Tree
def serialization(root: TreeNode) -> str:
    result = []
    
    def dfs(node):
        if not node:
            result.append("#")
            return
        
        # Append the value as a string to our mutable list
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
        
    dfs(root)
    # Join everything with a comma at the very end (O(N) time complexity)
    return ",".join(result)


def deserialization(serialized_str: str) -> TreeNode:
    # Split the string by the comma delimiter to get clean tokens
    tokens = serialized_str.split(",")
    
    # Pointer tracks the token index inside the list
    ptr = [0]

    def tree_builder():
        # When we reach the end of the tokens list
        if ptr[0] == len(tokens):
            return None
        
        # Read the current token and advance the pointer
        token = tokens[ptr[0]]
        ptr[0] += 1

        # Check for null character or an accidental empty string token
        if token == "#" or not token:
            return None
        
        # Create node - safely parsing multi-digit or negative numbers back to int
        node = TreeNode(int(token))

        # Recursive calls for left and right subtrees
        node.left = tree_builder()
        node.right = tree_builder()

        return node
    
    return tree_builder()


if __name__ == "__main__":

    my_tree = Tree()
    # Testing with multi-digit and negative numbers to prove it works!
    my_tree.create_tree([12, -5, None, 345, 4, None, 55])
    print("--- Original Tree Structure ---")
    my_tree.print_tree()

    my_serialized = serialization(my_tree.root)
    print(f"\nSerialized tree (With Delimiters): {my_serialized}")
    # Output format: 12,-5,345,#,#,4,#,55,#,#,#

    deserial_tree = deserialization(my_serialized)

    # Re-assigning to a fresh Tree instance to verify structural parity
    reconstructed_tree = Tree()
    reconstructed_tree.root = deserial_tree

    print("\n--- Deserialized Tree Structure ---")
    reconstructed_tree.print_tree()