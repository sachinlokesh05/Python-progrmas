from Algorithum.vending_machine.Note import Note

n=Note()
amount=int(input("enter the amount:"))
if amount<0:
    print("enter the correct amount")
else:
    n.getChange(amount)
