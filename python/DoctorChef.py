for i in range(int(input())):
        n,x=map(int,input().split())
        day=0
        a= list(map(int, input().split()))
        a.sort()
        for num in a:
            if x>=num:
                day+=1
                x=max(x,num*2)
            else:
                while x<num:
                    x*=2
                    day+=1
                day+=1
                x=num*2
        print(day)



