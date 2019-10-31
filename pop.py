from DataStructure.Linkedlist_Utility.Linkedlist_Utility import Singlelinkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def reverse(self, ):
        previous = None
        current_node = self.head
        while current_node != None:
            temp_to_store_next = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = temp_to_store_next
        self.head = previous

    def stack_pop(self):
        sl.reverse()
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        print(current_node.data)
        current_node = None
        print(current_node.data)

sl = Singlelinkedlist()
st = Stack()
st.sl.add(50)
st.stack_pop()