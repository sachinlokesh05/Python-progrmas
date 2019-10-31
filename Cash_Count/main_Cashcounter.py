from collections import deque
from DataStructure.Cash_Count.Cashcounter import Machine

print("Options : ""\n"
          "1--Withdraw\n"
          "2--Deposit")

mc=Machine()
try:
    P_count=int(input("enter the number of people availabale : "))
    g_pepole_queue = deque(mc.sorthing_Pepole(P_count))
    mc.Bank_operation(g_pepole_queue)
except:
    print("there are no one")
finally:
    print("thank you")

