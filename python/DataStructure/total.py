
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, sum):
   
    def dfs(root,s):
        if not root:
            return False
        elif root.left is None and root.right is None and s-root.val==0:
            return True
        else:
            return dfs(root.left,s-root.val) or dfs(root.right,s-root.val)
               
    return dfs(root,sum)
    


root = Node(5) 
root.left = Node(4) 
root.right = Node(8) 
root.left.left = Node(11) 
root.left.left.left = Node(7) 
root.left.left.right = Node(2) 
root.right.left=Node(13)       
root.right.right=Node(4)
root.right.right.right=Node(1)
            
print(hasPathSum(root,22))