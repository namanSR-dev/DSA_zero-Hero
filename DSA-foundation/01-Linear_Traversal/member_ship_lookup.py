def two_sum(seq: list[int], target: int) -> tuple[int, int] | None:
    """Pattern: Looking back at what we've seen."""
    seen: set[int] = set()
    for x in seq:
        needed = target - x
        if needed in seen:
            return (needed, x)
        seen.add(x)
    return None