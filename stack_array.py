class Stack:

    '''
        stack class inplemented by array
    '''

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.item_num = 0
    
    # return whether the stack is full
    # self -> boolean
    def is_full(self):
        return self.item_num == self.capacity
    

    # return if the stack is empty
    # self -> boolean
    def is_empty(self):
        return self.item_num == 0
    

    # add an item to the top of the stack
    # void
    def push(self, item):
        if(self.is_full()):
            raise IndexError
        self.items[self.item_num] = item
        self.item_num += 1
    
    # pop an item from the top of the stack
    # self -> item
    def pop(self):
        if(self.is_empty()):
            raise IndexError
        self.item_num -= 1
        return self.items[self.item_num]
    


    # return the top item in the stack without poping it
    # self -> item
    def peek(self):
        if(self.is_empty()):
            raise IndexError
        return self.items[self.item_num - 1]
