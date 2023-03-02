s=[]

top=None

def isEmpty(stk):

  if stk==[]:

    return True

  else:

    return False  

def push(stk,item):

  s.append(item)

  top=len(stk)-1

def spop(stk):

  if(isEmpty(stk)):

    return('UnderFlow!')

  else:

     i = stk.pop()

     if(len(stk) ==0):

       top=None

     else:

       top=top-1

  return i

def peek(stk):

  if isEmpty(stk):

    return('underflow')

  else:

    top=len(stk)-1

    return(stk[top])

def display(stk):

  if(isEmpty(stk)):

    print('Stack is empty!')

  else:

    top=len(stk)-1

    print(stk[top],'<---top')

    for i in range(top-1,-1,-1):

      print(stk[i])

while True:      

  print('''STACK IMPLEMENTATION

1.PUSH

2.POP

3.PEEK

4.DISPLAY

5.EXIT''')

  ch=int(input('Enter your choice(1-5)'))

  if ch==1:

    item=int(input("enter item you wan to push"))

    push(s,item)

    print('%d added sussessfully'%item)

    input('enter any key to continue')



  elif ch==2:

    item=spop(s)

    if item=='underflow':

      print('stack is empty')

    else:

      print('%d is popped'%item)

    input('enter any key to continue')   

  elif ch==3:

    item=peek(s)

    if item=='underflow':

      print('stack is empty')

    else:

      print('%d is popped'%item)

    input('enter any key to continue')  

  elif ch==4:

    display(s)

    input('enter any key to continue')

  elif ch==5:

    break

  else:

    print('wrong input')  

    input('press any key to continue')

  print('\n\n\n')