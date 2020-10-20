class Stack():
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def is_empty(self):
        return self.items ==[]

    def peek(self):
        if not self.is_empty():  
            return self.items[-1]  #-1 is the last element of the list in python
    def get_stak(self):
        return self.items

def is_paren_balanced(paren_srting):
    s=Stack()
    is_balanced = True
    index=0
