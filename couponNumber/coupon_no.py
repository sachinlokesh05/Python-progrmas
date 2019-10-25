import random
from array import array
from numpy11 import *

class coupon:
    def CouponNumbres(self, distinctCoupons):
        coupon = 0
        flag = 0
        array1 =array([])
        dist_count = 0;
        count = 0;
        random_no = 0;
        random_no_count = 0;
        flag = 0;

        while (coupon < distinctCoupons):
            randomNumber = random.randint(1,50)
            random_no_count += 1
            for i in range(distinctCoupons):
                if array1[i] != random_no and random_no > 0:
                    flag = 1
            if flag == 1:
                flag = 0
                count = count + 1
                array1[count] = random_no
                dist_count += 1
        print('"Total random numbers generated :', random_no_count)
        print('Distinct coupons are :')
        for i in range(distinctCoupons):
            print(array1[i])