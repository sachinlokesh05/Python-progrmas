import random
def Gambler():
    noOfbets=int(input("enter the number time you want to play"))
    money=int(input("enter the money you want"))
    goal=int(input("enter the goal money"))
    win=0
    lose=0
    count=0

    for i in range(noOfbets):
        randomNumber=random.random()
        count+=1
        if randomNumber>0.5:
            win+=1
            money+=1
        else:
            lose+=1
            money-=1
        if money==goal:
            print("you have achived your goal")
            break
        elif money==0:
            print("you have exhausted your money")
            break
        perWin=(win*100)/count
        perLose=100-(perWin)
    print("money i made",money)
    print("no of wins",win)
    print("no of loses",lose)
    print("per of wins",perWin)
    print("per of lose",perLose)



