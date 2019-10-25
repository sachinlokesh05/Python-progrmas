def Nthharmonic():
    n=int(input("enter the nth value"))
    result=0
    for i in range(1,n+1):
        print("1/",i,end="=")
        result=result+(1/i)
        print(result)
