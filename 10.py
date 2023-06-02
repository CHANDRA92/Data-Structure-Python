# Write a program to insert and delete a node (any position) at/from the given linear list 17-21-25-27-33-35.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linklist(Node):
    def __init__(self, data):
        self.head = Node(data)
    def insert(self, data):
        # insert data position index

        if self.head == None:
            self.head = Node(data)
            return self.head
            

        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)
        return self.head

    def delete(self, data):
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            return self.head
        while temp.next.data != data:
            temp = temp.next
        temp.next = temp.next.next
        return self.head