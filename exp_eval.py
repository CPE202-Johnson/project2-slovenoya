from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass


# void
# process operator to calculate the result
def process_operator(str, stack):
    try:
        stack.push(float(str))
    except ValueError:
        if "+-*/**".__contains__(str):
            operate(str, stack)
        else:
            raise PostfixFormatException("Invalid token")


# void
# process a single calculation
def operate(str, stack):
    try:
        a = float(stack.pop())
        b = float(stack.pop())
        if str == "+":
            stack.push(b + a)
        elif str == "-":
            stack.push(b - a)
        elif str == "*":
            stack.push(b * a)
        elif str == "/":
            if a == 0:
                raise ValueError
            stack.push(b / a)
        else:
            stack.push(b ** a)
    except IndexError:
        raise PostfixFormatException("Insufficient operands")


def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    input_array = input_str.split(" ")
    operation_len = len(input_array)
    stack = Stack(operation_len)
    i = 0
    while(i < operation_len):
        operation = input_array[i]
        process_operator(operation, stack)
        i += 1
    if stack.item_num == 1:
        return stack.pop()
    else:
        raise PostfixFormatException("Too many operands")




def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    input_array = input_str.split(" ")
    operation_len = len(input_array)
    stack = Stack(operation_len)
    i = operation_len
    while i > 0:
        i -= 1
        string = input_array[i]
        if "+-*/**<<>>".__contains__(string):
            a = str(stack.pop())
            b = str(stack.pop())
            stack.push(a + " " + b + " " + string)
        else:
            stack.push(string)
    return stack.pop()