from Algorithum.utility.utility import Utility

u=Utility()
P=int(input("enter the principal amount"))
Y=int(input("enter the time"))
R=float(input("enter the rate of Intreset"))
u.monthlyPayment(P,Y,R)