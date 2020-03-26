#I/O files
myfile=open('Test.txt')
print(myfile.read())
with open('test.txt') as my_new_file:
    contents=my_new_file.read()
with open('test.txt',mode='r')as myfile:
    contents=myfile.read()
with open('teehee.txt',mode='w')as f:
    f.write('hello')
#Comparison Operators
print(2==2)
#if/elif/else
if True:
    print('TRUE')
else:
    print('False')
#for loops
newlist=[1,2,3,4,5,6]
for num in newlist:
    print(num)
list_sum=0
for sum in newlist:
    list_sum=list_sum+num
print(list_sum)
mylist=[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in mylist:
    print(a+b+c)
d={'k1':1,'k2':2,'k3':3}
for value in d.values():
    print(value)
#while loops
x=0
while x<5:
    print(f'The Current Value of X is {x}')
    x=x+1
else:
    print('x is greater than 5')
for num in newlist:
    if num=='4'
    print(num)
mystring='hello'
mylist=[]
for letter in mystring:
    mylist.append(letter)
mylist=[x for x in 'word']
mylist=[num**2 for num in range(0,11)]
mylist=[x for x in range(0,11) if x%2==0]
