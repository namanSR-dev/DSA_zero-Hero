def two_sum_sorted ( seq: list[int], target: int) -> tuple[int, int] | None:
    """Patern: Two pointers in opposite direction."""
    left = 0
    right = len(seq)-1
    while left < right:
        current_sum = seq[left] + seq[right]
        if current_sum == target:
            return ( seq[left], seq[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

if __name__ == "__main__":
    print(two_sum_sorted([1,2,3,4,6,8,9], 14))
    print(two_sum_sorted([1,2,3,4,6,8,9], 7))
    print(two_sum_sorted([1,2,3,4,6,8,9], 20))