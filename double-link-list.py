class Node :
    def __init__(self,info):
        self.info=info
        self.next=None
        self.prev= None
class DLL:
    def __init__(self) :
        self.head=None
    def create (self,info):
        new = Node(info) 
        if self.head is None:
            self.head =new
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next=new
            new.prev= temp
            print(self.head)
    def show(self):
        if self.head is None:
            print('Link list is Empty')
        else:
            temp = self.head
            while temp:
                print(temp.info,"<-->",end=' ')
                temp= temp.next
            print()
    def insert_first(self,info):
        if self.head is None:
            print('First created the Node,after inseert')
        else:
            new = Node(info)
            new.next= self.head
            self.head.prev=new
            self.head=new
    def delete_last_node(self):
        if self.head is None:
            print("Empty list")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next = None
    def delete_first_node(self):
        if self.head is None:
            print("Empty list")
        else:
            temp = self.head
            self.head=temp.next
            temp.next=None
            self.head.prev = None

    def delt_pos(self):
        if self.head is None:
            print("Empty list")
        else:
            info = int(input('Enter the node to be deleted :: '))
            temp = self.head
            while temp.next is not None:
                if temp.info == info:
                    if temp == self.head :#first node
                        self.head = temp.next
                        temp.next.prev = None
                        # temp = None
                    else: #middle node
                        p = temp.prev
                        temp.prev.next=temp.next
                        temp.next.prev = p
                        # temp = None
                temp = temp.next
            if temp.prev == None  and temp.next == None and temp.info == info: # only one node 
                self.head = None
                # temp = None
            elif temp.next == None and temp.info == info:#last node
                temp.prev.next = None
                temp = None
    def insert_pos(self):
        pos = int(input("Enter postion to insert :: "))
        info = int(input("Enter value in node :: "))
        if pos == 1 :
            s.insert_first()
            # new = Node(info)
            # self.head.prev = new
            # new.next = self.head
            # self.head = new
        elif pos >1 :
            i=1
            temp = self.head
            while (i<pos-1):
                temp = temp.next
                i+=1
            # print(i)
            if i==pos-1 and temp.next is None:
                new=Node(info)
                new.prev = temp
                temp.next=new
                new.next = None
                print('H')
        
            elif (i<pos):    
                new=Node(info)
                new.prev =temp
                new.next = temp.next
                temp.next = new
                new.next.prev = new
            




s=DLL()
while True:
    print("""
********Main Mainu*********
    1. Create Node
    2. Display
    3. Insert value at Begining 
    4. Insert value at Position
    5. Delete last Node
    6. Delete first Node
    7. Delete node using Value 
    """)
    choice = int(input("Emter choice :"))
    if choice == 1:
        info = int(input("Enter value in node :: "))
        s.create(info)
    elif choice == 2:
        s.show()
    elif choice == 3:
        info = int(input("Enter value in node :: "))
        s.insert_first(info)
    elif choice == 4:
        s.insert_pos()
    elif choice == 5:
        s.delete_last_node()
    elif choice == 6:
        s.delete_first_node()
    elif choice == 7:
        s.delt_pos()
    else:
        break