import random
class flip:
    def flip_Coin(self):
        heads=0
        tails=0
        n=int(input("enter the number times you want to flip "))
        for i in range (1,n+1):
            result=random.random()
            if result>0.5:
                heads+=1
            elif result==0.5:
                n-=1
            else:
                tails += 1
        print("number of heads:",int(heads))
        print("number of tails:",int(tails))
        perHeads=(heads*100)/n
        perTails=100-perHeads
        print("percentage of heads:",int(perHeads),"%")
        print("percentage of tails",int(perTails),"%")



