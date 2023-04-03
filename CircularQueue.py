import array as arr 


class Queue:
    def __init__(self):
        self.front= -1
        self.rear = -1
        self.maxstk=int(input("enter size of queue:"))
        self.queue=arr.array('i',[0]*self.maxstk)

    def Push(self,n):
        # self.n=n
        if ((self.rear + 1)%self.maxstk) == self.front:
            print("stack overflow")
        elif (self.front == -1 and self.rear == -1):
            self.front =self.rear =0
            self.queue[self.rear] = n
        else:
            self.rear = (self.rear+1)%self.maxstk 
            self.queue[self.rear] = n
    
    def Pop(self):
        if self.front == -1 and self.rear == -1:
            print("Stack Underflow")
        elif (self.front == self.rear):
            print("Pop item is ",self.queue[self.front])
            self.front = self.rear = -1
        else:
            print("Pop item is ",self.queue[self.front])
            self.front = (self.front + 1)%self.maxstk 
    def Display(self):
        i = self.front
        if self.front == -1 and self.rear == -1:
            print("Stack Underflow")
        else:
            while (i!=self.rear):
                print(self.queue[i],'<-->',end= "")
                i = (i+1)%self.maxstk
            print(self.queue[self.rear],end="")
            print()
               
s=Queue()

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

        # if val!=-1:

        #     print("Popped element is:",val)

    elif option=="3":

        s.Display()

    elif option=="4":

        print("Exit!!!!")

        break

    else:

        print("invalid option!!!")