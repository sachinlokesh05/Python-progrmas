from Algorithum.utility.utility import Utility

u=Utility()
arr=list(map(int,input("enter the list of numbers").split(" ")))
print(u.Binarysearch_rec(arr,0,len(list)-1,5))
