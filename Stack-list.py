maxstack = int(input("Enter the stack size :"))
stk = []*maxstack
top = -1
def push (item):
    if (globals() ['top'] == maxstack-1):
        print ("Stack is Overflowed")
    else :
        for i in stk:
            stk[i]=item
        globals() ['top']+=1
        print(globals() ['top'])
        # stk.insert([globals() ['top']],item)
        # stk.append(item)
        print(item,"is Push in stack")
def pop ():
    if (globals() ['top']==-1):
        # globals() ['top'] == None
        print('Underflow')
    else:
        print('Pop :',stk[globals() ['top']])
        globals() ['top']-=1
def display():
  if(globals() ['top']==-1):
    print('Stack is empty!')
  else:
    # globals() ['top']=len(stk)-1
    print(stk[globals() ['top']])
    print(stk[globals() ['top']],'<---top')
    for i in range(globals() ['top']-1,-1,-1):
      print(stk[i])
while True:
    print("""Enter the operation
    1.Push
    2.Pop
    3.Display
    4.quit
    """)
    choice = int (input(":->"))
    if choice == 1:
        
        item = int (input("Enter item you want to push :"))
        push(item)
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the incorrect choice")