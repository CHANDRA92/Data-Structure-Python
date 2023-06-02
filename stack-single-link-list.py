# Write a program to implementing the STACK operations using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def Push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def Pop(self):
        if self.head == None:
            print("Stack is empty")
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

    def Display(self):
        if self.head == None:
            print("Stack is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
            
s= Stack()

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

        if val!=None:

            print("Popped element is:",val)

    elif option=="3":

        s.Display()

    elif option=="4":

        print("Exit!!!!")

        break

    else:

        print("invalid option!!!")