def subarrays_sum_equal_to_k (arr:list[int], k:int)->int:
    prefix_sum:int = 0
    freq:dict[int,int] = {0:1}
    count:int = 0

    for x in arr:
        prefix_sum += x

        if prefix_sum - k in freq:
            print(f"{prefix_sum-k} : {freq[prefix_sum - k]}")
            count += freq[prefix_sum - k]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    print(freq)
    return count


if __name__ == "__main__":

    arr = list(map(int, input("enter any integer list separated by space").split()))
    k = int(input("enter the sum for sub_array: "))

    print(f"The no. of sub_arrays with sum equal to {k} is: {subarrays_sum_equal_to_k(arr, k)}")
