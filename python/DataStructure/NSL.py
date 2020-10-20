class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()

    def is_empty(self):
        return self.items ==[] 
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def getStack(self):
        return self.items
    

for _ in range(int(input())):
    a=list(map(int,input().split()))
    v=list()
    s=Stack()
    i=0
    while i<len(a):
        if s.getStack()==[]:
            v.append(-1)
            s.push(a[i])
            i+=1
        elif a[i]>s.peek():
            v.append(s.peek())
            s.push(a[i])
            i+=1
        elif a[i]<s.peek():
            s.pop()
    
    print(v,end=" ")