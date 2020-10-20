try :
    for i in range(int(input())):
        n = int(input())
        c=(n-1)//2
        a=list(map(int,input().split()))
        b=[]
        count1=0
        count2=0
        count3=0
        for i in range(n):
            if(a[i+1]-a[i]==0):
                count3+=1
            elif(a[i+1]-a[i]>=0):
                count1+=1
            else:
                count2+=1

        print(count3)
        if count3==n-1:
            print(a)
        else:
            if count2==count1:
                print(a)
            # else:

except Exception:
    pass
