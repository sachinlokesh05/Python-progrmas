# 13. Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Stack using
# the Linked List and Print the Anagrams in the Reverse Order. Note no Collection
# Library can be used.

from DataStructure.Linkedlist_Utility.Linkedlist_Utility import Singlelinkedlist


class Prime:
    def prime(self,N):
        primenumber = []
        flag = 0
        for i in range(1, N):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        flag = 0
                        break
                    else:
                        flag = 1

            if flag == 1:
                if i not in primenumber:
                    primenumber.append(str(i))
                    sl.add(i)
        sl.display()

        count = sl.treverse(sl.head)
        for i in range(count):
            for j in range(count):
                if len(primenumber[i]) == len((primenumber[j])):
                    if len(primenumber[i]) > 1:
                        if len(primenumber[j]) > 1:
                            queue_1 = (list(primenumber[i]))
                            queue_2 = (list(primenumber[j]))

                            queue_1.sort()
                            queue_2.sort()

                            if queue_1 == queue_2:
                                    print(primenumber[i], "is anagram of", primenumber[j])
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

sl=Singlelinkedlist()