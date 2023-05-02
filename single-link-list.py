class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        if current is None:
            print ('Empty List')
        else:
            while current:
                print(current.data,'-->',end= ' ')
                current = current.next
    def rev_list(self):
        prevnode = None
        currentnode =nextnode = self.head
        while nextnode != None:
            nextnode = nextnode.next
            currentnode.next = prevnode
            prevnode = currentnode
            currentnode = nextnode
        self.head = prevnode
    def delete_node(self, value):
        current = self.head
        previous = None
        while current:
            if current.data == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                del current
                return
            previous = current
            current = current.next
    def sort(self):
            #sort link list using bubble sort
            #1. create two pointer current and nextnode
            #2. while nextnode is not null

            current = self.head
            while current:
                nextnode = current.next
                while nextnode:
                    if current.data > nextnode.data:
                        current.data, nextnode.data = nextnode.data, current.data
                    nextnode = nextnode.next
                current = current.next


            

l = LinkedList()
while True:
    print("""
    1. Create Node
    2. Display
    3. Reverse Node
    4. Delete Node using Value
    5. Sorting link list
    6. Exit
    """)
    choice = int(input("Emter choice :"))
    if choice == 1:
        info = int(input("Enter value in node :: "))
        l.append(info)
    elif choice == 2:
        l.print_list()
    elif choice == 3:
        l.rev_list()
    elif choice == 4:
        info = int(input("Enter value in node :: "))
        l.delete_node(info)
    elif choice == 5:
        print("Values sort by asending order")
        l.sort()
    elif choice == 6:
        print("Exit!!!!")
        break
    else:
        print("invalid option!!!")