from stack import Stack


def infix_to_prefix(infix_exp):

    # creatig the mirror image of the given infix expression.
    mirror_image_infix_exp = "".join([")" if char == "(" else "(" if char == ")" else char for char in infix_exp[::-1] ])

    # now use the same logic as the postfix conversion to make postfix of created mirror image.

    oprater = Stack()
    intermediary_result = []
    precedence = {"^": 3 , "*": 2 , "/": 2, "+": 1, "-": 1}

    for x in mirror_image_infix_exp:

        if x.isalnum():
            intermediary_result.append(x)
        
        elif  x == ")":
            oprater.push(x)
        
        elif x == "(":
            while not oprater.is_empty() and oprater.peek() != ")":
                intermediary_result.append(oprater.pop())
            
            oprater.pop()
        
        else:
            while not oprater.is_empty() and oprater.peek() != ")" and precedence.get(x, 0) <= precedence.get(oprater.peek(), 0):
                intermediary_result.append(oprater.pop())
            
            oprater.push(x)

        # handling the remaining operators in the stack.
    while not oprater.is_empty():
        intermediary_result.append(oprater.pop())

    
    # now convert the proccessed mirror image into orignal flow by reversing it again.
    final_result = "".join(intermediary_result[::-1])


    return final_result


#---------------------------#
# prefix to infix conversion

def prefix_to_infix(prefix_exp):
    oprands = Stack()
    for char in prefix_exp[::-1]:
        if char.isalnum():
            oprands.push(char)
        else:
            first = oprands.pop()
            second = oprands.pop()
            resultant_exp = f"({first}{char}{second})"
            oprands.push(resultant_exp)

    return oprands.pop()



#---------------------------------------------------#
if __name__ == "__main__":

    user_input = input("enter the infix expression ( eg. A+B*C ) : \n")

    result  = infix_to_prefix(user_input.replace(" ", ""))

    result_r = prefix_to_infix(result)

    print(f"your given infix_expression ( { user_input } ) is converted into prefix_expression : \n {result}")

    print(f"\n see that whether your logic works or not : {result_r}")