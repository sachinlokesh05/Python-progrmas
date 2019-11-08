import json

from Linkedlist import Singlelinkedlist
from oops_utiliy.stock_utility import stock, Stock

"""
company shares function is created to read file from the JSON file and we can add or remove
"""

st = Stock("stock_json")  # object is created for stock and linked list
llist = Singlelinkedlist()


def companyshares():
    while 1:
        print("1.to add the stock")
        print("2.to delete the stocks ")
        print("3. to show stock report")
        choice =int(input("enter your choice "))
        if choice==1:
            with open("stock_json") as f:  # json file is loaded
                data = json.load(f)
            for items in data:  # json file is converted in linked list
                llist.add(items)
        elif choice == 3:

                # try is used for the finding exception
                for i in range(len(st.only_stocks())):  # will display all the stocks in the portfolio
                    print("**",st.only_stocks()[i],end=" ")

                    print("\nchoose from above stocks to delete stocks ")


                llist.add(st.show_report()[1])  # if user is given 1 we will ad the stock to the linked list

        elif choice == 3:
            for i in range(len(st.only_stocks())):  # will display all the stocks in the portfolio
                print("**", st.only_stocks()[i], end=" ")

                print("\nchoose from above stocks to delete stocks ")

                g = st.delete_stock()  # if user is given 2 we will call stock class to delete the data
                llist.remove(data[g])  # here data is removed

        else:
            print("bye bye")  # program will end here

        st.dump("stock_json")

    

"""
main  function is created and function is called 
"""

if __name__ == '__main__':
    companyshares()