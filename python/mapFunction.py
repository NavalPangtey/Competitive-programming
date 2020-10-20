l=[1,23,5,2,3,4,]
l2=[3,4,2,4,1,4]

result= map(lambda x: x+x , l)

print(result)

def addition(l):
    return l+l

result= map(addition,l)

print(result)


num1=[1,2,3,4,5,6]
num2=[1,2,3,4,5,6]

result=map(lambda x,y:x*y,num1,num2)
print(result)


exampleString=['naval','nalini','papa','mom']
result=map(list,exampleString)
print(result)
