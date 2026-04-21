def logest_sub_array_with_sum_k (arr:list[int], k:int)->int:
    prefix_sum:int = 0
    initial_index:dict[int,int] = {}
    best:int = 0

    for i,x in enumerate(arr):

        prefix_sum += x

        if prefix_sum == k:  # handling key 0 in hashmap
            best = max(best, i+1)

        if prefix_sum - k in initial_index:  # handling keys other than 0
            best = max(best, i - initial_index[prefix_sum - k])

        if prefix_sum - k not in initial_index: # first occurence - store it
            initial_index[prefix_sum - k] = i
    
    return best
