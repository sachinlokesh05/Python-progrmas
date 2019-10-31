import math
import time
class Utility:
# print("constractor")
    def __init__(self):
        pass

#program for convert fahrehnit to celsius
    def toCelsius(self,fahrehnit):
        print(((fahrehnit-32)*5)/9,"celsius")

#program for convert celsius to fahrehnit
    def toFahrehnit(self,celsius):
        print((celsius*(9/5))+32,"Fahrehnit")

#program to check the two strings are anagram or not
    def checkAnagram(self,s1,s2):
        if(sorted(s1)==sorted(s2)):
            print("the strings are anagram")
        else:
            print("the strings are not anagram")

#program to reverse the given string
    def reverse(self, s):
        return s[::-1]

#program to check the given string is palidrome or not
    def isPalidrome_str(self,s):
        rev=Utility.reverse(self,s)
        if (s==rev):
            print("this is palidrome")
            return True
        print("this is not palidrome")
        return False
#program to check the given number is palidrome or not
    def isPalidrome_int(self,n):
        temp=n
        rev=0
        while (temp>0):
            r=n%10;
            rev=rev*10+r
            temp=temp//10;
        if (n==rev):
            print("the number is palidrome ")
            return True
        else:
            print("the number is not palidrome")
            return  False

#program for power given number
    def power(self,number,exponent):
        sum=1
        while exponent>0:
            sum=sum*number
            exponent-=1
        return sum

#program for Newton's sqrt
    def sqrt(self,c):
        t=0
        t=c
        epsilon=1e-15;
        while (abs(t - (c/t)) > epsilon*t):
            t = ((c/t)+t)/12
        return t
#Bubble sort program to sort the character array
    def Bubblesort_char(self,ch):
        s=[]
        for i in range(len(ch)):
            for j in range(len(ch)-1):
                if(ch[j]>ch[j+1]):
                    temp=ch[j+1]
                    ch[j+1]=ch[j]
                    ch[j]=temp
        for i in range (len(ch)):
                s.append(ch[i])
        return s
#Bubblesort program for sort the integer array
    def Bubblesort_int(self,num):
        for i in range(len(num)):
            for j in range(len(num)-1):
                if(num[j]>num[j+1]):
                    temp=num[j+1]
                    num[j+1]=num[j]
                    num[j]=temp
        return num
#insertionsort program to sort the character array
    def Insertionsort_char(self,ch):
        for i in range(1,len(ch)):
            temp=ch[i]
            j=i
            while(j>0 and ch[j-1]>temp):
                ch[j]=ch[j-1]
                j-=1
            ch[j]=temp

        return  ch
#insertionsort program to sort the integer array
    def Insertionsort_num(self,num):
        for i in range(1,len(num)):
            temp=num[i]
            j=i
            while(j>0 and num[j-1]>temp):
                num[j]=num[j-1]
                j-=1
            num[j]=temp
        return num

#monthlyPayment calculation
    def monthlyPayment(self,P,Y,R):
        n=12*Y
        r=R/(12*100)
        payment=P*r/(1-((1+r)**(-n)))
        print(math.ceil(payment),"rupees")
#program to convert decimal to binary
    def toBinary(self,dec):
        sum=""
        while( dec>0 ):
            r=dec%2
            sum=str(r)+sum
            dec=dec//2
        return sum

#swapping of nibbles and again converting it into decimal
    def swapNibbles(self,x):
        return ((x & 0x0F) << 4 | (x& 0xF0)>>4)

#prime number from 1 to 1000
    def primeNumner(self,n):
        count = 0
        for i in range (1,n):
            if i>1:
                for j in range (2,i):
                    if i%j==0:
                        break
                else:
                    count+=1
                    print(i,end=" ")
#program for print the prime palidrome
    def primePalidrome(self,n):
        count = 0
        for i in range (1,n):
            if i>1:
                for j in range (2,i):
                    if i%j==0:
                        break
                else:
                    p=str(i)
                    q=Utility.reverse(self,str(i))
                    if(p==q):
                        print(p,"--",q,"=that is palidrome")


    def primeAnagram(self,n):
        count = 0
        z=[]
        for i in range (1,n):
            if i>1:
                for j in range (2,i):
                    if i%j==0:
                        break
                else:
                    z.append(i)
        print(z)
        for i in  z:
            for j in z:
                if sorted(str(i)) == sorted(str(j)):
                    print(i)

#Iterator method for bubble sort
    def Binarysearch_itr(self,list,start,end,key):
        while start<=end:
            mid=(end-start)+start//2
            if key==list[mid]:
                return mid
            elif key>list[mid]:
                start=mid+1
            else:
                end=mid-1
        return -1

#recursive method for buble
    def Binarysearch_rec(self,list, start, end, key):
        if start<=end:
            mid=(end-start)+start//2
            if key==list[mid]:
                return mid
            elif key>list[mid]:
                return Utility.Binarysearch_rec(list,start,mid+1,key)
            else:
                return Utility.Binarysearch_rec(list,mid-1,end,key)
        return -1
#program for mergesort

    def merge(self,left,right):
        sorted_list=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if right[j]>=left[i]:
                sorted_list.append(left[i])
                i+=1
            else:
                sorted_list.append(right[j])
                j+=1

            sorted_list+=left[:i]
            sorted_list+=right[j:]

        return  sorted_list

    def mergesort(self,list):
        if len(list)==0 or len(list)==1:
            return list
        else:
            middle=(len(list)-1)//2
            left=u.mergesort(list[:middle])
            right=u.mergesort(list[middle:])
            return u.merge(left,right)
        return com

u=Utility()
print(u.primeAnagram(50))


