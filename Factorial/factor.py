class Factorial:
    def fact(self,n):
        i=1
        result=1
        while i<=n:
            result=result*i
            print(i,"!=",result)
            i+=1