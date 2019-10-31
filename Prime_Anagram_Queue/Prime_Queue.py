# 14. Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Queue using
# the Linked List and Print the Anagrams from the Queue. Note no Collection Library
# can be used.

class Prime_Anagramqueue:
    def Prime_Anagram_Queue(self,N):
        primenumber = []
        anagram = []
        flag = 0
        for number in range(1, N):
            # it finds the prime number between 0 to 100
            if number > 1:
                for number1 in range(2, number):
                    # Prime number starts with 2
                    # if number ids divided by other number then set flag to 1
                    if number % number1 == 0:
                        flag = 1
                        break
                    else:
                        flag = 0
            if flag == 0:
                if number not in primenumber:
                    primenumber.append(str(number))

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
                                print(primenumber[iterating_Number], "is the anagram of",
                                      primenumber[iterating_Number1])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
