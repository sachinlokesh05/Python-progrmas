class GuseeGame:
    def guessing(self,number):
        if number<=100:
            low=0
            high=100
            mid=0
            while low<=high:
                mid=(low+high)//2
                c=int(input("enter 1 if number b/w "+str(low)+"--"+str(mid)+"enter 2 if number b/w "+str(mid+1)+"--"+str(high)))
                if c==1:
                    high=mid
                    return high
                else:
                    low = mid + 1
                    return low
                return low,high
        else:
            return 0



g=GuseeGame()

number=(int(input("enter the number b/w 1 to 100")))
number1=g.guessing(number)
if number1==0:
    print("enter the correct number")
else:
    print("you =r number is:",number1)

