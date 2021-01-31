from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass


# return the operand stack of the input_string 
# str -> stack
def toStack(input_str):
    input_array = input_str.split(" ")
    stack = Stack(len(input_array))
    i = 0
    while(i < len(input_array)):
        stack.push(input_array[i])
        i += 1
    return stack



def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''

    

    
    



def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    pass


