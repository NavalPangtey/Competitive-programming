def calculateMex(Set): 
    Mex = 0
  
    while (Mex in Set): 
        Mex += 1
  
    return (Mex) 
  
# A function to Compute Grundy Number of 'n' 
# Only this function varies according to the game 
def calculateGrundy( n, dp): 
    if (n == 0): 
        return (0) 
    
    if dp[n]!=-1:
        return dp[n]
    
    Set = set() # A Hash Table 

    for i in range(n): 
       
        Set.add(calculateGrundy(i,dp)); 
    
    dp[n]=calculateMex(Set)
    return (dp[n])
  
# Driver program to test above functions 
n = 5; 
dp=[-1]*(n+1)
print(calculateGrundy(n,dp)) 
print(dp)