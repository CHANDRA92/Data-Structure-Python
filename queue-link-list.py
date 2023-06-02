    # 17. Write a program to implementing the QUEUE operations using linked list. 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        dequeued_data = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

        return dequeued_data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.front
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()


# Example usage
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Queue elements:")
queue.display()

dequeued_element = queue.dequeue()
print("Dequeued element:", dequeued_element)

print("Updated queue:")
queue.display()
