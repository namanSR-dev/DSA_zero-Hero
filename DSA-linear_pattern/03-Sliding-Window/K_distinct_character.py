def sub_string_with_k_distinct_char (s:str, k:int)->int:
    left:int = 0
    best:int = 0
    freq:dict[str,int] = {}

    # expanding phase
    for right in range(len(s)):
        ch = s[right]
        freq[ch] = freq.get(ch, 0) + 1

        # shrinking phase
        while len(freq) > k:
            left_char = s[left]
            freq[left_char] -= 1
            
            # deleting the char when it goes out of window
            if freq[left_char] == 0:
                del freq[left_char]
            
            left += 1
        
        # valid window here
        best = max(best, right - left + 1)

    return best



if __name__ == "__main__":
    s = input("enter the string of your choice: ")
    k = int(input("enter the window size: "))

    print(f"The size of sub_string with {k} distinct characters is: {sub_string_with_k_distinct_char(s,k)}")