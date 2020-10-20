# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val =x
        self.next = None

class  LinkedList(object):
    """docstring for  LinkedList"""
    def __init__(self):
        self.head=None




class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p1=l1
        p2=l2

        currentcarry=0

        head = cur = ListNode(0)

        while p1 or p2 or currentcarry:

            currentvalue=currentcarry
            currentvalue +=0 if p1 is None else p1.val
            currentvalue +=0 if p2 is None else p2.val
            if currentvalue>=10:
                currentvalue-=10
                currentcarry=1
            else:
                currentcarry=0

            cur.next= ListNode(currentvalue)
            cur = cur.next

            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2=p2.next
            elif p2 is None:
                p1=p1.next
            else:
                p1=p1.next
                p2=p2.next

        return head.next




l1= LinkedList()

l1.head=ListNode(int(input()))
pp=ListNode(int(input()))
l1.head.next=pp
while pp:
    pp=ListNode(int(input()))
    pp.next=pp
    if pp==None:
        break



l2= LinkedList()

l2.head=ListNode(int(input()))
pp=ListNode(int(input()))
l2.head.next=pp
while pp:
    pp=ListNode(int(input()))
    pp.next=pp

    if pp==None:
        break







# l2size = int(input())

# for i in range(l2size):
#     if i==0:
#         l2= ListNode(input())
#     else:
#         l2.next=ListNode(input())

#     next=next.next



# Recursively print linked list
def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)


s = Solution()
l3 = s.addTwoNumbers(l1, l2)
print(linked_list_str(l3))
