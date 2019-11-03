from Binary_Search_Tree.Number_Bst import Node
tree=Node(3)

#input list
list = [5, 3, 4, 5, 6, 8, 6]
for i in range(len(list)):
    tree.insertion(list[i])
#calling the printtree method to print
tree.PrintTree()