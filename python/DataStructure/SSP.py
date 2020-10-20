class Stack():
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
    
    def is_empty(self):
        return self.items==[]
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def getStack(self):
        return self.items

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    v=list()
    temp=list()
    tk=0
    s=Stack()
    flag=False
    i=0
    count=1
    comp=0
    while i<len(a):
        if s.getStack()==[]:
            v.append(count)
                    
            count=1
            if flag==True:
                j=tk-1
                while j>=0:
                    s.push(temp[j])
                    j-=1   
                temp=[]
                tk=0
                flag=False
            s.push(a[i]) 
            i+=1
        elif a[i]>=s.peek():
            flag=True
            comp=s.peek()
            while a[i] >= comp:
                count+=1
                temp.append(s.peek())
                s.pop()
                tk+=1
                comp=s.peek()
                if s.getStack()==[]:
                    break
                
            
           
                   
        elif a[i]<s.peek():
            v.append(count)
            if flag==True:
                j=tk-1
                while j>=0:
                    s.push(temp[j])
                    j-=1   
                temp=[]
                tk=0
                flag=False
            s.push(a[i])
            count=1
            i+=1

            

    print(" ".join(str(x) for x in v))