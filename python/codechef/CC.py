for _ in range(int(input())):
    # n=input()
    n,k=map(int,input().split())
    s=input()
    if n<2*k:
        print(s)
    else:
        c1=0
        c0=0
        for i in range(n):
            if s[i]=='0':
                c0+=1
            else:
                c1+=1
        
        if c1==c0:
            ans=""
            count1=0
            count=0
            if n%2==0:
                for i in range(n):
                    if i==0 or i==n-1:
                        ans+="1"
                    elif count<k:
                        ans+='0'
                        count+=1
                        count1=0
                    elif count1<k:
                        ans+='1'
                        count1+=1
                        if count1==k:
                            count=0
            else:
                for i in range(n):
                    if i==0 :
                        ans+="1"
                    elif count<k:
                        ans+='0'
                        count+=1
                        count1=0
                    elif count1<k:
                        ans+='1'
                        count1+=1
                        if count1==k:
                            count=0


            # for i in range(1,n):
            #     if i==1 or i%2==0:
            #         ans+="1"
            #     else:
            #         ans+="00"
            
            print(ans)

        else:
            print("IMPOSSIBLE")
