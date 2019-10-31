#Number Binary tree

class Node:

    def __init__(self,data):
        self.left_child = None
        self.right_child = None
        self.data = data

    #To insert the data into the tree in order
    def insertion(self,data):
        #if the data in not None get into tree
        if self.data == None:
            #creating Node with the present data
            self.data = Node(data)

        #if the current data is less then head data goes to left
        elif data < self.data:
            if self.left_child == None :
                self.left_child = Node(data)
            else:
                self.left_child.insertion(data)

        # if the current data is greater then head data goes to right
        elif data > self.data:
            if self.right_child == None:
                self.right_child = Node(data)
            else:
                self.right_child.insertion(data)
        else:

            #it there are no data in the head make the present data as head data
            self.data = data

    #To print the sorted tree
    def PrintTree(self):
        if self.left_child:
            self.left_child.PrintTree()
        print(self.data)
        if self.right_child:
            self.right_child.PrintTree()

