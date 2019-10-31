class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class Singlelinkedlist:

    def __init__(self):
        self.head=None

#to add the data at the end
    def add(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
        else:
            t=self.head
            while t.next is not None:
                t=t.next
            t.next=n
        return

#To print the data in the singlelinkedlist Nodes
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data)
            t=t.next
#To reverse the data of the node
    def reverse(self,head):

#To insert the data in the middle
     def insertion_middle(self,n,data,position):
         p=Node(data)
         t=n
         while( position > 1):
             t=t.next
             position -= 1
         p.next=t.next
         t.next =p

#To insert the data at the first
    def insertion_first(self,n,data,position):
        p=Node(data)
        t=n
        if(position==0):
            n.next = t.next
            t.next = n
        return n

#To insert the data at last
    def insertion_last(self,h,data):
        n = Node(data)
        t = h
        while(t.next is not None):
            t=t.next
        n.next=t.next
        t.next=n

#To delet the data at first
    def delet_first(self):
        t=self.head
        if(t is not None):
            self.head=t.next
        else:
            print("head is empty")
        return

#To delete the data in the middle
    def delete_mid(self,n,position):
        t=n
        fast=t.next.next
        while position > 1:
            t=t.next
            position-=1
        t=fast

#To delete the data at last
    def delete_last(self,n):
        t=n
        while t.next.next is not None:
            t=t.next
        t.next=None

#To search given element in the list
    def search(self,data):
        t=self.head
        count=0
        while t.data!=data:
            count += 1
            t=t.next
        print(count)


    def treverse(self,n):
        t=n
        count=0
        while t!=None:
            count+=1
            t=t.next
        return(count)


sl=Singlelinkedlist()
print(sl.treverse(sl.head))
# sl.add(50)
# sl.add(20)
# sl.add(55)
# sl.add(("sachin"))
# sl.display()
# # sl.insertion_middle(sl.head,22,2)
# # print("")
# # sl.display()
# # sl.insertion_first(sl.head,10,0)
# # print("\n")
# # sl.display()
# # sl.insertion_last(sl.head,88)
# # print("\n")
# # sl.display()
# # sl.delet_first()
# # sl.delete_mid(sl.head,1)
# # sl.delete_last(sl.head)
# # sl.display()
# sl.search("sachin")