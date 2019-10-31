# 12. Extend the Prime Number Program and store only the numbers in that range that are
# Anagrams. For e.g. 17 and 71 are both Prime and Anagrams in the 0 to 1000 range.
# Further store in a 2D Array the numbers that are Anagram and numbers that are not
# Anagram



primenumber=[]
array = [[] , [[]]]
flag=0
list1=[]
list2=[]
for number in range(1,20):
    if number > 1:
        for number1 in range(2, number):
            if number % number1 == 0:
                flag = 1
                break
            else:
                flag = 0

        if flag == 0:
            if number not in primenumber:
                primenumber.append(number)

        for iterating_Number in range(len(primenumber)):
            for iterating_Number1 in range(len(primenumber)):
                # check if length of the numbers are same or equal to 1 or equal to 0
                if len(primenumber[iterating_Number]) == len(primenumber[iterating_Number1]):
                    if len(primenumber[iterating_Number]) > 1:
                        if len(primenumber[iterating_Number1]) > 1:
                            # add the two numbers into queue
                            queue_1 = (list(primenumber[iterating_Number]))
                            queue_2 = (list(primenumber[iterating_Number1]))
                            # sort the queues
                            queue_1.sort()
                            queue_2.sort()
                            # print(list)
                            if queue_1 == queue_2:
                                list1.append(primenumber[iterating_Number])
                            else:
                                list2.append(primenumber[iterating_Number])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass


    array[0]=list1
    array[1][0]=list2
    print(array)
    list1.clear()
    list1.clear()