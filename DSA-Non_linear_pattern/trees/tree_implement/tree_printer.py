from collections import deque

def visual_print(root):
    """Isolated printing function that generates the structural layout."""
    if not root:
        print("[Empty Tree]")
        return

    def get_height(node):
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    height = get_height(root)
    max_width = (2 ** height) * 3
    grid = [[" " for _ in range(max_width)] for _ in range(height * 2 - 1)]

    root_col = max_width // 2
    queue = deque([(root, 0, root_col)])

    while queue:
        node, row, col = queue.popleft()
        if not node:
            continue

        grid[row][col] = str(node.val)
        gap = 2 ** (height - (row // 2) - 2)

        if node.left:
            grid[row + 1][col - gap] = "/"
            queue.append((node.left, row + 2, col - gap * 2))

        if node.right:
            grid[row + 1][col + gap] = "\\"
            queue.append((node.right, row + 2, col + gap * 2))

    for line in grid:
        row_str = "".join(line).rstrip()
        if row_str:
            print(row_str)
