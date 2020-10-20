#range
for i in range(1,10):
     print(i)
print("/////////////")
#for loop
a=[1,2,3,4,8,6,4,3]
for i in a:
     print(i)
print("/////////////")

#for usingrange(start, stop, step)

for i in range(0,15,3):
     print(i)
print("/////////////")
# step argument to iterate backwards

for i in range(100,0,-10):
     print(i)

print("/////////////")
#For Loops using Sequential Data Types
sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']
for ch in sharks:
     print(ch)

print("/////////////")

#usnig range to add items to list 
sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']

for ch in range(len(sharks)):
     sharks.append('nav')
print(sharks)
print("/////////////")
#creating a list
a=[]
for x in range(20):
     a.append(x)

print(a)

print("/////////////")
#itrating trough string
s='Naval'
for l in s:
     print(l)



print("/////////////")
#itrating through a dictionary
sammy_shark = {'name':'sam','animl':'shark','color':"blue","location":'ocean'}
for k in sammy_shark:
     print(k+':'+ sammy_shark[k])
#When using dictionaries with for loops, the iterating variable
#  corresponds to the keys of the dictionary, 
# and dictionary_variable[iterating_variable] corresponds to the values.
#  In the case above, the iterating variable key was used to stand for key, 
# and sammy_shark[key] was used to stand for the values.

print("/////////////")

#nested for loops

num_list = [1,2,3]
alpha_list = ['a','b','c']
for num in num_list:
     print(num)
     for letter in alpha_list:
          print(letter)
print("/////////////")

#eg

list_of_list = [['naval','kabir','nell'],[0,1,2,3],[2.3,2.4,7.4]]
for list in list_of_list:
     print (list)

for list in list_of_list:
     for item in list:
          print(item)

print("/////////////")

