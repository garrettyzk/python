#formatting
a='Hello My Name is{}'
print(a.format(' Garrett'))
result=100/777
print('The result was {r:1.5f}'.format(r=result))
print(f'The result was {result:1.5f}')
#lists
list=[1,2,3]
list.append(4)
list.pop(2)
numlist=[2,25,56,4,8,136,47]
numlist.sort()
numlist.reverse()
print(numlist)
print(list)
#dictionary
dictionary={'Key':'StanLoona','Key2':'Stray Kidz'}
dictionary['Key3']='skz'
print(dictionary)
print(dictionary['Key'])
#tuple
tuple=('1','1','1','1','2','3')
print(tuple.count('1'))
#set
print(set(tuple))

b=None #prevent error message from unknown variable
