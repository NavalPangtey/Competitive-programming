class Node:
    def __init__(self,data):
        self.data= data
        self.next= None


class linkedlist:

    def __init__(self):
        self.head= None
    
    def push(self,new_data):

        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    def insert(self, prev_node,new_data):
        if prev_node is None:
            print("there is no such previous node.")
            return
        new_node =Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node    
    
    def append(self,new_data):
        new_node=Node(new_data)

        if self.head is None:
            self.head= new_node
            return
        
        last = self.head
        while last.next:
            last=last.next
        
        last.next= new_node
        new_node.next=None
    
    def delete(self,key):

        temp= self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if (temp.data==key):
                break
            prev= temp
            temp = temp.next
        
        if temp is None:
            return
        
        prev.next = temp.next
        temp =None
    
    def deletePosition(self, position):
        if self.head is None:
            return
        
        temp= self.head

        if position==0:
            self.head = temp.next
            temp =None
            return
        for i in range(position-1):
            temp =temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next
    
    def lengthOfLinkList(self):
        temp = self.head

        count=0
        while temp:
            temp=temp.next
            count+=1
        
        return count
    
    def getCountRecu(self, node):
        if not node:
            return 0
        else:
            return 1+ self.getCountRecu(node.next)

    def lengthOfLinkListRecursively(self):
        return self.getCountRecu(self.head)

    def searchele(self,key):
        temp = self.head
        if temp is None:
            return False
        
        while temp:
            if temp.data==key:
                return True
            temp=temp.next
        
        return False

    def searchRecu(self,node,key):
        if not node:
            return False
        else:
            if node.data==key:
                return True
        
        return self.searchRecu(node.next, key)

    def swap(self,X,Y):
        
        if X==Y:
            return 
        
        prevx=None
        currx=self.head

        while currx  and currx.data!=X:
            prevx=currx
            currx=currx.next
        
        prevy=None
        curry=self.head

        while curry and curry.data!=Y:
            prevy=curry
            curry=curry.next
        
        if currx ==None or curry==None:
            return 
        
        if prevx :
            prevx.next=curry
        else:
            self.head=curry

        if prevy :
            prevy.next = currx
        else:
            self.head =currx

        temp= currx.next
        currx.next=curry.next
        curry.next=temp

    
    def printList(self):
        temp =self.head
        while temp:
            print(temp.data,end=" ")
            temp= temp.next

if __name__=='__main__': 
    llist = linkedlist()
    llist.append(10)
    llist.push(3)
    llist.push(5)
    llist.push(6)
    llist.push(1000)
    llist.append(22)
    llist.insert(llist.head.next.next,8)
    llist.delete(10)
    llist.deletePosition(3)
    llist.printList()
    print()
    # print(llist.lengthOfLinkList())
    print(llist.lengthOfLinkListRecursively())
    print(llist.searchele(1))
    print(llist.searchRecu(llist.head,22))
    llist.swap(1,13)
    llist.printList()

    