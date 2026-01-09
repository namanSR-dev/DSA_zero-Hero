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

    print(dict)

# frequency_count( [4,6,2,4,32,4,6] )




# linear-traversal + Conditional-check

def two_sum ( seq: list[int], target:int ) -> set[int] | None:
    seen = set() # set is used to check member ship, dictionary can also be used both has O(1) lookup but dict. has memory overhead
                # [note:- {} will create the empty dictionary not set.]
    for x in seq:
      needed = target - x
      if needed in seen:
         return (needed, x)
      seen.add(x)
    return None

# seq = [5, 7, 9, 35, 8, 2, 57, 45]
# target = 64

# print(two_sum(seq, target))
      



# linear-traversal + Min/Max tracking

def min_max(seq:list[int]) -> int :
   if not seq: return None, None  # early exit for empty sequence - GOOD PRACTICE

   min = max = seq[0]  # this ensure that min and max both hold some value even if any one condition never match

   for x in seq[1:] :
      if x > max:
         max = x
      elif x < min:
         min = x
   
   return min, max     # this line returns the tuple since ", " creates the tuple not "()" but
                       # for creating empty tuple use this ---> empty_tuple = () <---
                       # while tuple = 5, will create the tuple alone no need of "()" and same for tuple = 1,5,2,4 --> (1,5,2,4)

# seq = [4,7,2,9,32,65,35,1]
# print(min_max(seq))
