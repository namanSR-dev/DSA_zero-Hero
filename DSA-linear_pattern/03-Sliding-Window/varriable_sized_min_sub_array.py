def min_sub_array_with_target_sum (arr: list[int], S:int)->float|int:
    left:int = 0
    current_sum = 0
    best:float = float("inf")  # initializig it with the largest value possible because we have find the minimum.

    for right in range(len(arr)):

        # expanding the window
        current_sum += arr[right]

        # shrinking phase - here the window is minimal and valdi.
        while current_sum >= S:
            best = min(best, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return best if best != float("inf") else 0
    

if __name__ == "__main__":

    arr = list(map(int, input("enter the array of positive integer separate by spaces: ").split()))
    S = int(input("enter the Target value for the sub_array total sum: "))
    print(f"the size of minimal sub_array with target = {S} is: {min_sub_array_with_target_sum(arr,S)}")