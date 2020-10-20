# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         for i, j in enumerate(nums):
#             s_ele = target - j
#             if s_ele in nums and nums.index(s_ele) != i:
#                 return [i, nums.index(s_ele)]
#         return []


#!/bin/python3



# import os
# import sys
# import array as arr
# #
# # Complete the simpleArraySum function below.

# def simpleArraySum(ar):
#    sum=0
#    for y in range(len(ar)):
#        sum = sum + ar[y]

#    return sum



# n=int(input())
# ar=arr.array('i',[])
# i=0
# for i in range(n):

#    # k=int(input())
#    ar.insert(i,int(input()))

# print(simpleArraySum(ar))


import os
import sys
import array as arr
#
# Complete the simpleArraySum function below.

def simpleArraySum(ar):
   sum=0
   for y in range(len(ar)):
       sum = sum + ar[y]

   return sum



n=int(input())

lists=list(map(int,input().rstrip().split()))

# lists=[]
# i=0
# for i in range(n):

#    # k=int(input())
#     lists.insert(i,int(input()))
#     #lists[i]= int(input())

ar=arr.array('i',lists)

print(simpleArraySum(ar))



