def max_sub_array(arr: list[int], k:int)-> int:

    current_sum:int = 0
    # building the first window
    for i in range(0,k):
        current_sum += arr[i]

    best:int = current_sum

    # sliding the window
    for i in range(k, len(arr)):
        current_sum += arr[i]
        current_sum -= arr[i - k]

        if best < current_sum:
            best = current_sum

    return best

if __name__ == "__main__":
    seq:list[int] = list(map(int, input("Enter the List of integers seperated by the space: ").split()))
    print(f"input: {seq}")
    k:int = int(input("Now! Enter the size of sub_array: "))
    print(f"max_sub_array of size - {k}: \n => {max_sub_array(seq, k)}")