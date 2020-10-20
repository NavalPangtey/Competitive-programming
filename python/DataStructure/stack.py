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

s= Stack()
print(s.is_empty())
s.push('a')
s.push('b')
s.push('c')
s.push('d')
s.pop()
print(s.peek())