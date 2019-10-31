from collections import deque

class Machine:
    # Ask a person whether he wants to deposit or withdraw thw money and save them in queue
    def sorthing_Pepole(self,P_count):
        g_count=deque([])

        for iterating in range(P_count):
            try:
                p_choice=int(input("enter the your choice : "))
            except:
                print("enter the valid choice")
            if p_choice==1:
                g_count.append(1)
            elif p_choice==2:
                g_count.append(2)
            else:
                print("invalid choice")

        return g_count

    def Bank_operation(self,g_pepole_queue):
            f_people_queue=g_pepole_queue
            f_total_cash=100
            iterating_element=0
            while iterating_element<=len(f_people_queue):
                if f_people_queue is not None:
                    # If peron chooses to withdraw money
                    # then deduct the amount and pop him
                    if f_people_queue[iterating_element] == 1:
                        g_amount = int(input("enter the amount You want to withdraw : "))
                        f_total_cash = f_total_cash - g_amount
                        f_people_queue.popleft()
                        print("remaining amount is : ", f_total_cash)
                        print(f_people_queue)
                        iterating_element+=1

                    elif f_people_queue[iterating_element] == 2:
                        # If person chooses to deposit money
                        # then add the amount and pop him
                        g_amount = int(input("enter the amount You want to deposit : "))
                        f_total_cash = f_total_cash + g_amount
                        f_people_queue.popleft()
                        print("remaining amount : ", f_total_cash)
                        print(f_people_queue)
                        iterating_element+=1











