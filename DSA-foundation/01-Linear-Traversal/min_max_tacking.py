def min_max(seq:list[int]) -> tuple[int, int] | tuple[None, None] :
   '''Linear-traversal + min/max finding'''
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
