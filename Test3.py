#Functions
def name_function():
    '''
    '''
    print('Hello')
def say_hello(name='name'):
    return'hello'+ name
result=say_hello('Jose')
print(result)

def add(n1,n2):
    return n1+n2
result = add(20,30)
print(result)

def dog_check(mystring):
    return 'dog' in mystring.lower()
#Pig Latin
def pig_latin(word):
    if word[0]in'aeiou':
        return(word+'ay')
    else:
        return(word[1:]+word[0]+'ay')

example=pig_latin('elephant')
print(example)
#*args and **kargs
def myfunc(*args):
    return sum(args)*2
def myfunc(*args,**kwargs):
    print(f'I would like {args[0],kwargs['food']}')
myfunc(10,20,30,fruit='orange',food='eggs','animal':'dog')

def myfunc(word):
    result=''
    for letter in range(len(word)):
        if letter%2 is 0:
            result+=word[letter].lower()
        else:
            result+=word[letter].upper()
    return result
print(myfunc('test'))

def myfunc(sentence):
    words=sentence.split()
    words.reverse()
    end_sentence=' '.join(words)
    return end_sentence
print(myfunc('How are you today'))

def prime(nums):
    y=0
    for i in range(2,nums+1):
        for x in range(2,i-1):
            if i%x == 0:
                break
        else:
            y+=1
    return y
print(prime(5))
