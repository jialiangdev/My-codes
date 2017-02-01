# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:51:42 2016

@author: Jialiang Yu
"""


list1=[1,2,3,4]
list2=['a','b','c','d']
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print dict(zip(list1,list2))

"""
print dict(map(None, list1, list2))
print dict(map(lambda *row: row,*(list1,list2)))


L=[list1,list2]
leng=len(list1)
lis=sum(L,[])

print {L[0][i]: L[1][i] for i in range(leng)}
print {lis[i]: lis[i+leng] for i in range(leng)}
print dict([j[i] for j in L] for i in range(leng))
print dict([L[j][i] for j in (0,1)] for i in range(leng))
"""