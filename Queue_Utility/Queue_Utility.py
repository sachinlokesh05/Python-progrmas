class Queue:
    def __init__(self):
        self.items=[]

    def Enqueue(self,item):
        self.items.append(item)

    def Dequeue(self):
        self.items.pop(0)

    def display(self):
        return self.items

qu=Queue()



while(1):
    print("1.enqueue")
    print("2.dequeue")
    ch = int(input("choice : "))
    if ch==1:
        num=int(input("enter the value add : "))
        qu.Enqueue(num)

    elif ch==2:
        qu.Dequeue()

    elif ch==3:
        print(qu.display())

    else:
        break