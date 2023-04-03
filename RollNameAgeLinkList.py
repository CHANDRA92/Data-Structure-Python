#     6. Write a program to create a linear linked list, node will contain the fields Roll,
#  Name & age.
class Node:
    def __init__(self, roll=None,name=None,age=None):
        self.roll = roll
        self.name = name
        self.age = age
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,roll,name,age):
        new_node = Node(roll,name,age)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def Display(self):
        current = self.head
        if current is None:
            print ('Empty List')
        else:
            print("Roll\tName\tAge")
            while current:
                print(f"{current.roll}\t{current.name}\t{current.age}")
                current = current.next

s=LinkedList()
while True:
    print("""
    1. Enter Details of Student
    2. Display
    3. Exit
    """)
    choice = int(input("Emter choice :"))
    if choice == 1:
        Roll = int(input("Enter Student Roll :: "))
        Name = input("Enter Name :: ")
        Age = int(input("Enter Age :: "))
        s.append(Roll, Name,Age)
    elif choice == 2:
        s.Display()
    elif choice == 3:
        print("Exit!!!!")
        break
    else:
        print("invalid option!!!")
