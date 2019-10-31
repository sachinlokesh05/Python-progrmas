# 11. Take a range of 0 - 1000 Numbers and find the Prime numbers in that range. Store
# the prime numbers in a 2D Array, the first dimension represents the range 0-100,
# 100-200, and so on. While the second dimension represents the prime numbers in
# that range

class Prime_TwoD:
    def array(self,N):
        list0 = []
        list1 = []
        array = [[], [[]]]
        flag = 0

        for i in range(0, N):
            min = i * 100
            max = (i + 1) * 100
            for number in range(min, max + 1):
                if number > 1:
                    for number1 in range(2, number):
                        if number % number1 == 0:
                            flag = 1
                            break
                        else:
                            flag = 0

                    if flag == 0:
                        if number not in list1:
                            list1.append(number)

            list0.append(min)
            list0.append(max)
            array[0] = list0
            array[1][0] = list1
            print(array)
            list0.clear()
            list1.clear()
