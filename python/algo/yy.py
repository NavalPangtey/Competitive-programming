# Python program for KMP Algorithm 
def KMPSearch(pat, txt, lps):
    M = len(pat)
    N = len(txt)
    count_arr=[0 for x in range(N)]
    # # create lps[] that will hold the longest prefix suffix
    # # values for pattern
    # lps = [0] * M
    j = 0  # index for pat[]

    # # Preprocess the pattern (calculate lps[] array)
    # computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    while i < N:
        # print(i)
        count_arr[i]=count_arr[i-1]
        print(count_arr)
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            # print(i)
            count_arr[i-1]+=1
            j = lps[j - 1]

            # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return count_arr


def computeLPSArray(pat, M):
    lps=[0 for x in range(M)]
    len = 0  # length of the previous longest prefix suffix
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    return lps


txt=input()
pat=input()
lps=computeLPSArray(pat,len(pat))
# print(lps)
count1=KMPSearch(pat,txt,lps)[-1]
count_arr=KMPSearch(pat,txt+txt,lps)
count2=count_arr[-1]
count3=count2-(2*count1)
# print(count1)
# print(count2)
# print(count3)
q=int(input())
for _ in range(q):
    n=int(input())
    val=n//len(txt)
    if val:
        ans=val*count1 + (val-1)*count3
        extra = n % len(txt)
        ans+= count_arr[len(txt)-1+extra]-count_arr[len(txt)-1]
    else:
        extra=n%len(txt)
        ans=count_arr[extra-1]
    print(ans)