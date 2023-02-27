import array as arr
pos = -1
def binary_search(list,n):
    low = 0
    up = len(list) - 1
    while low <= up:
        mid = (low + up) //2
        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n :
                low = mid + 1
            else:
                up = mid + 1
    return False
# In BinarySearch list is sorted
# list = [10,12,14,15,16,17,18,19,20,21,22,45]
# found = 12

l = int(input('Enter the lenth of the array ::'))
a = arr.array('i',[0]*l)
for i in range(l):
    a[i]=int(input('Enter the element ::'))
found = int(input('Enter the element to search ::'))

if binary_search(a,found):
    print ("Element found at ",pos+1)
else:
    print ("Element not found")

