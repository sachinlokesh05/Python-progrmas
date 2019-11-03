from collections import deque

from Cash_Count.Cashcounter import Machine

print("Options : ""\n"
          "1--Withdraw\n"
          "2--Deposit")
mc=Machine()
P_count=int(input("enter the number of people availabale : "))
g_pepole_queue = deque(mc.sorthing_Pepole(P_count))
mc.Bank_operation(g_pepole_queue)


