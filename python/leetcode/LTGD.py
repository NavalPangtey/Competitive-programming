class Solution:
    def largestTimeFromDigits(self, A):
        hh=0
        mm=0
        
        for num in reversed(range(0,24)):
            B=list()
            B=A[:]
            a=num//10
            b=abs((a*10)-num)
            f1=False
            f2=False
            for i in range(len(A)):
                if A[i]==a and f1 ==False:
                    f1=True
                elif A[i]==b and f2==False:
                    f2=True
                
                if f1 and f2:
                    hh=(a*10)+b
                    B.remove(a)
                    B.remove(b)
            #         break
            # print(hh)
            # if f1 and f2:
                    for min in reversed(range(0,60)):
                        c=min//10
                        d=abs((c*10)-min)
                        f3=False
                        f4=False
                        for i in range(len(B)):
                            if B[i]==c and f3==False:
                                f3=True
                            elif B[i]==d and f4==False:
                                f4=True
                            
                            if f3 and f4:
                                mm=(c*10)+d
                                # B.remove(c)
                                # B.remove(d)
                        #         break
                        # if f3 and f4:
                                if hh<10:
                                    hh=str(hh)
                                    hh='0'+hh
                                if mm<10:
                                    mm=str(mm)
                                    mm='0'+mm

                                    print(hh)
                                    print(mm)
                                    print(A)
                                    
                                    return f'{hh}:{mm}'
                                
        return("ho")
        





A=[2,0,6,6]
p=Solution()
print(p.largestTimeFromDigits(A))