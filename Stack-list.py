import array as arr 





class stack:

    def __init__(self):

        self.top=-1

        self.maxstk=int(input("enter size of stack:"))

        self.arr=arr.array('i',[0]*self.maxstk)



    def Push(self,n):

        self.n=n

        if self.top == self.maxstk-1:

            print("stack overflow")

        else:

            self.top+=1

            self.arr[self.top]=self.n



    def Pop(self):

        if self.top==-1:

            print("stack underflow")

            return -1

        else :

            self.item = self.arr[self.top]

            self.top-=1

            return self.item



    def Display(self):

        if self.top == -1:

            print("stack is empty")

        else :

            for i in range(self.top,-1,-1):

                print(self.arr[i])
                
s=stack()

while True:



    print("*****main menu******")

    print("1. Push")

    print("2. Pop")

    print("3. Display")

    print("4. Exit")

    option=input("enter option:")

    if option == "1":

        item=int(input("enter number to push on stack:"))

        s.Push(item)

    elif option == "2":

        val = s.Pop()

        if val!=-1:

            print("Popped element is:",val)

    elif option=="3":

        s.Display()

    elif option=="4":

        print("Exit!!!!")

        break

    else:

        print("invalid option!!!")