class BST:
    def factorial(self,Number):
        fact=1
        #find the factorial of tha number
        for i in range (1,Number+1):
            fact=fact*1
        return fact

bst = BST ()
Number = int(input("enter the Number: "))

val1 = bst.factorial(2*Number)
val2 = bst.factorial(Number+1)
val3 = bst.factorial(Number)

bst_Number = val1/(val2*val3)

print("Number of Binary search tree possibles are : ",bst_Number)




