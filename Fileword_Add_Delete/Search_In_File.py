# 1. UnOrdered List
# a. Desc -> Read the Text from a file, split it into words and arrange it as Linked List.
# Take a user input to search a Word in the List. If the Word is not found then add it
# to the list, and if it found then remove the word from the List. In the end save the
# list into a file
# b. I/P -> Read from file the list of Words and take user input to search a Text
# c. Logic -> Create a Unordered Linked List. The Basic Building Block is the Node
# Object. Each node object must hold at least two pieces of information. One ref to
# the data field and second the ref to the next node object.
# d. O/P -> The List of Words to a File.
from DataStructure.Linkedlist_Utility.Linkedlist_Utility import Singlelinkedlist
sl=Singlelinkedlist()
f = open("Data_File", "r")
sl.add(f.read().split(" "))
sl.display()
if sl.search("python") is True:
    print("yes")
else:
    print("no")
f.close()
# print(sl)
# flag = 0
# for i in range(len(data)):
#     s = "madduri"
#     if data[i] == s:
#         flag = 0
#
#     if flag == 0:
#         f.write(s)
#
# g.close()

