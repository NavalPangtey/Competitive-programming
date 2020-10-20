#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self,TreeNode):

        if not TreeNode:
            return TreeNode
        # q = []
        # q.append(TreeNode)
        # height = 0
        # while(True):
        #     nodeCount = len(q)
        #     if nodeCount == 0 :
        #         h=height

        #     height += 1
        #     while(nodeCount > 0):
        #         node = q[0]
        #         q.pop(0)
        #         if node.left is not None:
        #             q.append(node.left)
        #         if node.right is not None:
        #             q.append(node.right)

        #         nodeCount -= 1

        items = []
        queue = [TreeNode]

        count =1
        temp=[]
        ans=[]
        k=0
        flag1=0
        while queue:
            copy = queue[:]
            queue = []

            for item in copy:
                if item is None:
                    items.append(None)
                    queue.append(None)
                    queue.append(None)
                #     flag1+=1
                # if item.left is None:
                #     items.append(None)
                #     queue.append(None)
                #     queue.append(None)
                #     flag2+=1
                else:
                    items.append(item.val)

                    queue.append(item.left)

                    queue.append(item.right)



            if all((x is None for x in queue)):
                break


        # if (flag2==2**(h+1)-1):
        #     items= list(filter(None, items))
        #     for i in range(len(items)):
        #         temp.append(items[i])
        #         ans.append(temp)
        #         temp=[]
        #     return ans

        l= len(items)
        for i in range(l):
            if i==0:
                temp.append(items[i])
                ans.append(temp)
                temp=[]
                count+=1
            elif(i<=k+2**(count-1)):
                if items[i]==None:
                    if i==l-1:
                        ans.append(temp)
                else:
                    temp.append(items[i])
                    if i==l-1  :
                        ans.append(temp)

            else:
                ans.append(temp)
                temp=[]
                count+=1
                k=i-1
                if items[i]==None:
                    if i==l-1:
                        ans.append(temp)
                else:
                    temp.append(items[i])
                    if i==l-1  :
                        ans.append(temp)

        ans.reverse()
        return ans

    # def treeHeight(self,TreeNode):


    #     if TreeNode is None:
    #         return 0
    #     q = []
    #     q.append(TreeNode)
    #     height = 0
    #     while(True):
    #         nodeCount = len(q)
    #         if nodeCount == 0 :
    #             return height

    #         height += 1
    #         while(nodeCount > 0):
    #             node = q[0]
    #             q.pop(0)
    #             if node.left is not None:
    #                 q.append(node.left)
    #             if node.right is not None:
    #                 q.append(node.right)

    #             nodeCount -= 1





#*****************************************************************************15ms*********************************************************************************
                                                                            #Solution

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node,level):

            if len(levels)==level:
                levels.append([])

            levels[level].append(node.val)

            if node.left: helper(node.left, level+1)
            if node.right: helper(node.right, level+1)

        helper(root,0)
        return levels[::-1]
