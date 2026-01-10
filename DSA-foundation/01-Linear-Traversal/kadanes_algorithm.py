def max_sub_array(arr: list[int]) -> int | None:
    """Pattern: Resetting state when it becomes a liability (current < 0)."""
    if not arr: return None

    best = arr[0]
    current = 0
    for x in arr:
        current += x
        if current > best:
            best = current
        if current < 0:
            current = 0
    return best