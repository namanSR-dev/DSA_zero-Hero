"""
Docstring for foundation.linear-traversal-And-operations

-- this file teach you the how linarly traver through the sequence and perform different opertion
-- this file become the foundation for most DSA questions.

"""


#linear-traversal + Store Pattern

def frequency_count (seq:list[int]) -> None :

    dict = {}     # dictionary is used for fast lookup and saves

    for x in seq:
       if x in dict:
        dict[x] = dict[x] + 1
    else:
        dict[x] = 1

    print(dict.items())