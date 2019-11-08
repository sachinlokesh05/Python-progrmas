# Generators:-
# Difference between yeild  and return using in function

def Sqrt():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

values=Sqrt()
print(values.__next__())

for i in values:
    print(i)
print("\n")

def Sqrt():
    n=1
    while n<=10:
        sq=n*n
        n += 1
        return sq



values=Sqrt()
print(values)