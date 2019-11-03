class Stack:
    def __init__(self):
        self.stk=[]

    def push(self,data):
        self.stk.append(data)

    def pop(self):
        if self.stk==[]:
            return  -1
        else:
            return self.stk.pop()

    def peek(self):
        n=len(self.stk)
        return self.stk[n-1]

    def display(self):
         return self.stk


st=Stack()
while(1):
    print("1.push()")
    print("2.pop()")
    print("3.peek()")
    print("4.display()")
    print("5.exit()")
    ch = int(input("enter the choice value"))
    if ch == 1:
        num = int(input("enter the value of num"))
        st.push(num)

    elif ch == 2:
        N = st.pop()
        if N == -1:
            print("stack is empty")

        else:
            print("popped element is : ", N)

    elif ch == 3:
        print("the top element is : ", st.peek())

    elif ch == 4:
        print(st.display())

    else:
        break;


