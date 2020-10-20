# cook your dish here
t=int(input())
for i in range(t):
    c=0
    a=input()
    p=input()
    if a==1:
        c=1
    elif a>=p:
        q=a//p
        c+=q
        r=a%p
        if r>0:
           if r%2==0:
               c+=1
           elif r==1:
               c+=1
           else:
               c+=2
    else:
       if a%2==0:
           c+=1
       else:
           c+=2

    print(c)


################################################ SEcond Solution

n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    if l[0]%2==0:
        c=0
        c=c+(l[0]//l[1])
        if l[0]%l[1]==0:
            print(c)
        else:
            print(c+1)
    else:
        c=1
        l[0]=l[0]-1
        c=c+(l[0]//l[1])
        if l[0]%l[1]==0:
            print(c)
        else:
            print(c+1)
