class Node:
    def __init__(self,val):
        self.next=None
        self.val=val

class MyLinkedList:

    def __init__(self):
        self.head= None
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        temp=self.head
        for i in range(index):
            if i == index:
                return temp.val
            temp=temp.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
    
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp:
                if temp.next==None:
                    temp.next=new_node
                temp=temp.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node=Node(val)
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
            
        if index==count-1:
            temp.next=new_node
        elif index>count:
            return
        else:        
            gg=self.head
            for i in range(index-1):
                gg=gg.next
            new_node=gg.next
            gg.next=new_node
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        temp=self.head
        for i in range(index-1):
            temp=temp.next
            if temp is None:
                return
        
        temp.next=temp.next.next
        
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)