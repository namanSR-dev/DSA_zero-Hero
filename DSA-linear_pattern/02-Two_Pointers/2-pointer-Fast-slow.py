def remove_duplicates( nums: list[int]) -> int:
    """Pattern: Fast and Slow Pointers."""
    if not nums:
        return 0
    
    slow = 1 # Pointer for the position of the last unique element or the next insertion point.
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:  # found an unique element so update the anchor
            nums[slow] = nums[fast]
            slow += 1
    return slow

if __name__ == "__main__":
    nums1 = [1, 1, 2]
    k1 = remove_duplicates(nums1)
    print(f"After removing duplicates: {nums1[:k1]}, New length: {k1}")

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = remove_duplicates(nums2)
    print(f"After removing duplicates: {nums2[:k2]}, New length: {k2}")