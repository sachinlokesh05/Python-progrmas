import datetime
import json
from Linkedlist import Singlelinkedlist

from Cardgame_Queue.Implementation_Of_Queue_Using_Singlelinkedlist.Queue_Using_Singlelinkedlist import Queue
from oops_utiliy.stock_utility import Stock, stock


def companyshares():
    global add, remove
    st = stock("stock_json")  # object is created for stock and linked list
    llist = Singlelinkedlist()
    stack = ()
    q = Queue()

    with open("stock_json") as f:  # json file is loaded
        data = json.load(f)

    try:  # try is used for the finding exception

        userinput = int(input("number of stocks you want to add or removed : "))

        for i in range(userinput):

            # input is taken from the user

            for i in range(len(st.onlystocks())):
                print("**", st.onlystocks()[i], end=" ")  # will display all the stocks in the portfolio

            user = int(input("\nenter 1 to add or enter 2 to delete or enter 3 to exit :"))

            if user == 1:

                added = st.add_stock()[1]
                stack.push(added)
                print()
                llist.add(stack.size()[0]["stock"])  # if user is given 1 we will ad the stock to the linked list
                now=datetime.datetime.now()
                q.addrear(now)

            elif user == 2:

                remove = st.deletestock()
                stack.push(data[remove])
                llist.add(stack.size()[0]["stock"])
                now1 = datetime.datetime.now()
                q.addrear(now1)

            else:
                print("bye bye")  # program will end here

        llist.print()       # final linked list is printed with the symbol which were added o removed
        print()
        q.printlist()  # final linked list is printed from queue function where time stamp of the add or remove is
        # updated

        st.dump("stock_json")  # this method is used for appending the data in JSON format

    except (ValueError,TypeError):
        print(" please check the  Error ")


if __name__ == '__main__':
    companyshares()