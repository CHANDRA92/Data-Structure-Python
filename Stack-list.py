stack = []
def push_stack():
    element = input("Enter the element : ")
    stack.append(element)
    print(stack)
def pop_stack():
    if not stack:
        print("No elements is available ")
    else:
        e =stack.pop()
        print("Remove element :",e)
        print(stack)
while True:
    print("""Enter the operation
    1.Push
    2.Pop
    3.quit
    """)
    choice = int (input(":->"))
    if choice == 1:
        push_stack()
    elif choice == 2:
        pop_stack()
    elif choice == 3:
        break
    else:
        print("Enter the incorrect choice")