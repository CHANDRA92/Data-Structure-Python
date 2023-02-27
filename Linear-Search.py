import array as arr
pos = -1
def Linear_search(list,n):
    for i in range(len(list)):
        if list[i] == n :
            globals() ['pos'] = i
            return True
    return False

# list = [10,20,30,40]
# found = 30

l = int(input('Enter the lenth of the array ::'))
a = arr.array('i',[0]*l)
for i in range(l):
    a[i]=int(input('Enter the element ::'))
found = int(input('Enter the element to search ::'))
if Linear_search(a,found):
    print('Element found',pos+1)
else:
    print('Element not found')