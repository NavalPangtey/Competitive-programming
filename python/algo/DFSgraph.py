#((((((((((DFS GRAPH TRAVERSAL FOR DIRECTED GRAPH))))))))))

# from collections import defaultdict 
# class Graph: 
  
#     def __init__(self): 
#         self.graph = defaultdict(list)

#     def addEdge(self, u, v): 
#         self.graph[u].append(v) 
  
   
#     def DFSUtil(self, v, visited): 
#         visited[v] = True
#         print(v, end = ' ') 
#         for i in self.graph[v]: 
#             if visited[i] == False: 
#                 self.DFSUtil(i, visited) 

#     def DFS(self): 
#         V=len(self.graph)
#         visited = [False] *V 
#         for i in range(V):
#             if visited[i]==False:
#                 self.DFSUtil(i, visited)  

# g = Graph() 
# g.addEdge(0, 1) 
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)


# print("Following is DFS ") 
# g.DFS() 

# *********************************************************************

#((((((((((FOR UNDIRECTED GRAPH))))))))))


# (((((((((((COUNTONG CONNECT COMPONENTS)))))))))))

# from collections import defaultdict 
# arr=defaultdict(list)

# def dfs(node):
#     v[node]=True
#     for i in arr[node]:
#         if v[i]==False:
#             dfs(i)

# n,e=map(int,input().split())

# for i in range(e):
#     a,b=map(int,input().split())
#     arr[a].append(b)
#     arr[b].append(a)
# cc=0
# v = [False]*(n+1)
# for i in range(1,n+1):
#     if v[i]==False:
#         dfs(i)
#         cc+=1

# print(cc)

# *********************************************************************


# Bishu and his Girlfriend (((((SINGLE SOURCE SHORTEST PATH ON TREE)))))

# from collections import defaultdict
# import math
# arr=defaultdict(list)

# def dfs(node,d):
#     visited[node]=1
#     distance[node]=d
#     for i in arr[node]:
#         if visited[i]==0:
#             dfs(i,distance[node]+1)

# n=int(input())
# visited=[0]*(n+1)
# distance=[0]*(n+1)
# for i in range(n-1):
#     u,v=map(int,input().split())
#     arr[u].append(v)
#     arr[v].append(u)
# dfs(1,0)
# q=int(input())
# mimimum=math.inf
# ans=-1
# for i in range(q):
#     gg=int(input())
#     if distance[gg]<mimimum:
#         mimimum=distance[gg]
#         ans=gg
#     elif distance[gg]==mimimum and gg<ans:
#         ans=gg
# print(ans)


# *********************************************************************
#(((((((((((((((Tree or not check)))))))))))))))

# from collections import defaultdict
# arr=defaultdict(list)

# def dfs(node):
#     visited[node]=True
#     for i in arr[node]:
#         if visited[i]==False:
#             dfs(i)

# n,m=map(int,input().split())
# for i in range(m):
#     u,v=map(int,input().split())
#     arr[u].append(v)
#     arr[v].append(u)
# visited=[False]*(n+1)

# cc=0
# for i in range(1,n+1):
#     if visited[i]==False:
#         dfs(i)
#         cc+=1

# if cc==1 and m==n-1:
#     print('YES')
# else:
#     print("NO")




# *********************************************************************
#(((((((((((((((BIlpartite graph problem)))))))))))))))

from collections import defaultdict
def dfs(node,c):
    visited[node]=True
    color[node]=c
    for i in arr[node]:
        if visited[i]==False:
            res=dfs(i,c^1)
            if res==False:
                return False
        elif color[node]==color[i]:
            return False
    return True

for j in range(int(input())):
    arr=defaultdict(list)
    n,m=map(int,input().split())
    for i in range(m):
        u,v=map(int,input().split())
        arr[v].append(u)
        arr[u].append(v)
    
    visited=[False]*(n+1)
    color=[-1]*(n+1)
    flag=True
    for i in range(1,n+1):
        if visited[i]==False:
            res=dfs(i,0)
            if res==False:
                flag=False
                break

    print('Scenario #{}:'.format(j+1))
    if flag: 
        print('No suspicious bugs found!')
    else:
        print('Suspicious bugs found!')

        
   