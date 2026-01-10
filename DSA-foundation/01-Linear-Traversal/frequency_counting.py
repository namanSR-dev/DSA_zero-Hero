
def frequency_count(seq: list[int]) -> dict[int, int]:
    """Pattern: Store and Increment."""
    freq: dict[int, int] = {} 
    for x in seq:
        freq[x] = freq.get(x, 0) + 1 # Pro tip: .get() simplifies the if/else logic
    return freq

if __name__ == "__main__":
    print(frequency_count([4, 6, 2, 4, 32, 4, 6]))