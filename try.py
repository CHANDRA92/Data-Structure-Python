# 
# a = set(['L','M','N','O'])
# a.update(['P','Q'])
# a.discard('M')
# print(a)
# a1 = set(['X','Y','Z'])
# a2 = set([6,8,10])
# a2.add(12)
# a1.add(5)
# a2.add('L')
# a1.add(a2)
# print(a1)
# print(a2)

# def myFunca(a,b,c):
#     return (a*b)/c
# x = myFunca(318,485,2)
# print(x)

# import re
# s = "Nina is 12 years old and she goes to school and she also attends dance clases"
# s1 =  re.findall("she",s)
# print(s1)

# import numpy as n
# n1 = n.arange(8)
# n2 = n1[::4]
# print(n.shares_memory(n1,n2))
# print(n1)
# print(n2)

# import numpy as n
# import pandas as p
# a = [5,6,7,8,9,10]
# b = [1,2,3,4,5,6]
# c= list(range(6))

# num = [5,3,6,2,4,10]
# res = map(lambda a,b:a*b,num)
# print(res)

num = [11,12,13,14,15,16]
res = list(filter(lambda x:x%3,num))
print(res)
