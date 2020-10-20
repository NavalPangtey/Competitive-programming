
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric( root):

    if not root :
        return None

    check=False
    queue=[]
    queue.append(root)
    currentlvl=list()
    while len(queue)>0:
        size=len(queue)
        currentlvl=list()
        for i in range(size):
            node=queue.pop(0)
            currentlvl.append(node)
            if node!=-1:
                if node.left is not None:
                    queue.append(node.left)
                else:
                    queue.append(-1)
                if node.right is not None:
                    queue.append(node.right)
                else:
                    queue.append(-1)
        for i in range(len(currentlvl)):
            if currentlvl[i]!=-1:
                currentlvl[i]=currentlvl[i].val
        for i in range(len(currentlvl)):
            print(currentlvl[i],end="")
        print()
        if len(currentlvl)==1:
            check=True
        else:
            n=len(currentlvl)-1
            for i in range(len(currentlvl)):
                if currentlvl[i]!=currentlvl[n-i]:
                    return False
                if (len(currentlvl)//2)-1==i:
                    break
    
    return check
        

root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
# root.left.left = Node(3) 
root.left.right = Node(3) 
# root.right.left=Node(2)       
root.right.right=Node(3)
            
print(isSymmetric(root))