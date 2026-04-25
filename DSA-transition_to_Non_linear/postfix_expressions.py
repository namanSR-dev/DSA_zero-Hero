from stack import Stack

def infix_to_postfix ( infix_exp ) :
    precedence = {"+":1, "-": 1, "*": 2, "/": 2, "^": 3}
    output = []
    operator = Stack()

    for char in infix_exp:

        # if char is oprand
        if char.isalnum():
            output.append(char)

        # if char is "("
        elif char == "(":
            operator.push(char)

        # if char is ")" then we stark poping out the operators
        elif char == ")":
            while (not operator.is_empty() and operator.peek() != "("):
                output.append(operator.pop())
            operator.pop() # removeing the "(".
        
        # if char is operator then
        else:
            # if higher precedence operator than <char> present in waiting stack we will take it out and add to our output
            while (not operator.is_empty() and operator.peek() != "(" and precedence.get(char, 0) <= precedence.get(operator.peek(), 0)):
                output.append(operator.pop())
            
            # finally add the operator to waiting stack
            operator.push(char)
    
    # finally pop out the remaining operators and add it to the output.
    while not operator.is_empty():
        output.append(operator.pop())
    
    return "".join(output)





#---------------------------#
# postfix to infix conversion

def postfix_to_infix(postfix_exp):
    oprands = Stack()
    for char in postfix_exp:
        if char.isalnum():
            oprands.push(char)
        else:
            first = oprands.pop()
            second = oprands.pop()
            resultant_exp = f"({second}{char}{first})"
            oprands.push(resultant_exp)

    return oprands.pop()





#---------------------------------------------------#
if __name__ == "__main__":

    user_input = input("enter the infix expression ( eg. A+B*C ) : \n")

    result  = infix_to_postfix(user_input.replace(" ", ""))

    result_r = postfix_to_infix(result)

    print(f"your given infix_expression ( { user_input } ) is converted into postfix_expression : \n {result}")

    print(f"\n see that whether your logic works or not : {result_r}")
        
            
            

    