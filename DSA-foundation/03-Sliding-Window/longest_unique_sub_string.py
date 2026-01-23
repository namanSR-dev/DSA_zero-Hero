def longest_unique_sub_string (Str: str) -> int:
    left: int = 0
    freq: dict[str, int] = {}
    best: int = 0

    for right in range(len(Str)):
        #expanding phase
        ch:str = Str[right]
        freq[ch] = freq.get(ch, 0) + 1

        while freq[ch] > 1: # shrinking phase
            remove_left:str = Str[left]
            freq[remove_left] -= 1
            left += 1

        # sub_string is valid here so udate the best
        best = max(best, right - left + 1) 

    return best


if __name__ == "__main__":
    Str:str = input("Enter any string of your choice: ")
    print(f"The longest unique sub_string in your given string - {Str} is: {longest_unique_sub_string(Str)}")