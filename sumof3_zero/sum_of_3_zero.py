def zeroof3(arr):
    for i in range (0,len(arr)):
        for j in range (i+1,len(arr)):
            for k in range (j+1,len(arr)):
                if arr[i]+arr[j]+arr[k]==0:
                    print (arr[i],arr[j],arr[k])


