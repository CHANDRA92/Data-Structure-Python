import array as arr 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularQLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
    def Push(self,data): #enqueue
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else :
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
    
    def Pop(self): #dequeue
        if self.front == None and self.rear == None or self.front ==0 and self.rear == 0:
            print("Queue is empty or Underflow")
        elif self.front==self.rear :
            print("Pop item is ",self.front.data)
            self.front = self.rear = 0
        else :
            print("Pop item is ",self.front.data)
            self.front = self.front.next
            self.rear.next = self.front
    
    def Display(self):
        self.temp = self.front
        
        if self.front == None and self.rear == None or self.front ==0 and self.rear == 0:
            print("Queue is empty or Underflow")
        else:
            while (self.temp.next != self.front):
                print(self.temp.data,'<-->',end="")
                self.temp = self.temp.next
            print(self.temp.data,'<-->',end="")
            print()

s = CircularQLinkedList()

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
