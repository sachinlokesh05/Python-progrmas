import json
import random
import re

from oops_utiliy.time import a


class Stock:
    def __init__(self,filename):
        with open(filename) as f:
            self.data=json.load(f)
            # print(self.data)


    def add_stocks(self):
        z=[]
        try:
            stock=input("enter the stock you which to add : ")
            total_number=int(input("enter the number of stocks you want add : "))
            share_price=random.randint(100,200)
            Ttime=a.time()
        except ValueError:
            print("enter the correct value")

        dict1={"stock": stock, "total_share" :total_number,"share_price":share_price,"time":Ttime}

        z=self.data
        z.append(dict1)
        return dict1,z

    def show_report(self):
        share=0
        share_price=0
        total_share=0

        for i in range(len(self.data)):
            share+=1
            total_share=total_share+self.data[i]["total_share"]
            share_price=share_price+self.data[i]["share_price"]

        return share,total_share,share_price

    def only_stocks(self):
        stocks=[]
        for i in self.data:
            stocks.append(i["stock"])
        return stocks

    def dump(self,filename):
        with open(filename) as f:
            dump1=json.dump(self.data,f,indent=2)
        print(dump1)

    def delete_stock(self):
        user=input("enter : ")
        q=-1
        for i in self.data:
            if i["stock"] == user:
                q+=1
                del self.data[q]
        return q


filename="fdattaa.json"
stock = Stock(filename)


# a,b=stock.add_stocks()
# print(a)
m,n,p=stock.show_report()
# # print(m)
# # print(n)
# # print(p)
# # stock.dump(filename)
# # print(stock.only_stocks())
# # stock.delete_stock()
# # stock.show_report()
# # print(stock.only_stocks())
# print(stock.show_report()[0])
# print(stock.show_report()[1])
# print(stock.show_report()[2])
# # print(stock.show_report()[3])