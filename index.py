"""
#vid 47
#vid40/Exercise 4 inhancement
import random
import string

def encode(_str):
    if type(_str) == str:
        size = len(_str)
        if size < 3:
            return _str[::-1]
        else:
            random_prefix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            random_suffix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            result = random_prefix +  _str[1::] + _str[0]  + random_suffix
            return result
    else:
        print('Please Provide string data')

def decode(_str):
    if type(_str) == str:
        size = len(_str)
        return _str[::-1] if size < 3 else _str[-4] + _str[3:-4]
    else:
        print('Please Provide string data')

def enCodeStr(_str):
    words = _str.split(" ")
    enCodedStr = []
    for word in words:
        rtn = encode(word)
        enCodedStr.append(rtn)
    return " ".join(enCodedStr)

def deCodeStr(_str):
    words = _str.split(" ")
    deCodedStr = []
    for word in words:
        rtn = decode(word)
        deCodedStr.append(rtn)
    return " ".join(deCodedStr)
    

_str = input("Enter your string:\n  ")
a = enCodeStr(_str)
b = deCodeStr(a)
print(f"encoded: {a}")
print(f"decoded: {b}")



#video 46
#os module
import os

print(os.__file__)

#video 45
#__name__
from wellcome import wellcome

wellcome()

#video 44
# How import works in Python
from pandas import __version__
from math import sqrt, __name__ as name


print(__version__)
print(sqrt(9))
print(name)


#video 41
#enumerate function
def table(_num):
    natural_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, num in enumerate(natural_numbers):
        print( f'{_num} x {natural_numbers[index]}  = {_num * num }')

table(14)

#video 41
#short hand if else
a = 90
b = 90
c = 10 if a == b else 9
print(c)

print("a > b") if a > b else print("a == b") if a == b else print("b > a")

#video40
import random
import string

def encode(_str):
    if type(_str) == str:
        size = len(_str)
        if size < 3:
            return _str[::-1]
        else:
            random_prefix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            random_suffix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            result = random_prefix +  _str[1::] + _str[0]  + random_suffix
            return result
    else:
        print('Please Provide string data')

def decode(_str):
    if type(_str) == str:
        size = len(_str)
        return _str[::-1] if size < 3 else _str[-4] + _str[3:-4]
    else:
        print('Please Provide string data')

print(decode(encode("Harry")))
print(decode(encode("no")))

#video39
score = 0

questions = ["Question1?", "Question2?", "Question3?", "Question4?"]
options = [['option1', 'option2', 'option3', 'option4'], 
           ['option1', 'option2', 'option3', 'option4'], 
           ['option1', 'option2', 'option3', 'option4'], 
           ['option1', 'option2', 'option3', 'option4']]
correctOptions = ['option1', 'option2', 'option3', 'option4']

for i in range(len(questions)):
    print(questions[i])
    for j in range(len(options[i])):
        print(f"{j + 1}. {options[i][j]}")
    ans = int(input('Your Answer? (1/2/3/4) => ')) - 1
    if correctOptions[i] == options[i][ans]:
        score += 2

print(f"Your final score is: {score}")

#video38
a = input("Enter any value between 5 and 9 => ")
if (a == 'quit'):
    exit()
else:
    a = int(a)
    if (a < 5 or a > 9):
        raise ValueError("Value should be between 5 and 9")
    else:
        print(a, ' is your number.')

#video37
try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))

    print(l[i])
except:
    print("some error occured")
finally:
    print("end of program")

# video36
a = input("Enter any number: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("invalid input")
# except Exception as e:
    # print(e)

# video 35
for i in range(5):
    print(i)
else:
    print("sorry no i for")

i=0
while i in range(5):
    print(i)
    i = i+1
else:
    print("sorry no i while")


#video 34
ep1= {122:45, 123:89, 124: 69, 125: 69}
ep2= {126: 67, 127: 90}

ep1.update(ep2)
# ep1.pop(125)
# ep1.popitem()
del ep1[122]
print(ep1)
# del ep1
# ep1.clear()

#Video33
dic={
    "name": "umar",
    "age": 19
}
print(dic.get("address"))
# print(dic["address"])

for key in dic.keys():
    print(key, ":", dic[key])

# print(dic.items())

for key, value in dic.items():
    print(key, ":", value)
    
    
# Video 32
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
s3 = {2, 1, 6, 5}
print(s1.union(s2))
print(s2.union(s1))
print(s1 == s3)
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
s1.update(s2)
print(s1)


# Video 31
s = {1,2,2,3}
print(s)
s.add('number')
print(s)
print(type(s))
s = {}
print(type(s))
s = set()
print(type(s))


# Video 30
def multiply(n, m):
    if (m == 0):
        return 0
    return  n + multiply(n, m-1)

def factorial(n):
    if(type(n) != int or n < 0):
        return "Aik to ye subah subah aa jata he dimagh khrab krne"
    if (n == 0):
        return 1
    return n * factorial(n-1)

def fibonaci(n):
    if (n == 0 or n == 1):
        return n
    return fibonaci(n-1) + fibonaci(n-2)

print(multiply(6, 7))
print(factorial(6))
print(factorial("6"))
print(factorial(-1))
print(fibonaci(8))


Video 29
import this => zen of python pep8
def square(n):
    '''This function square the number. This is a doc string'''
    print(n**2)

square(5)
print(square.__doc__)

Video 28
string = "Hey my name is {} and I am from {}"
name = "Muhammad Umar"
country= "Pakistan"
print(string.format(name, country))

fstring = f"Hey my name is {name} and I am from {country}"
print(fstring)

string = "Only for price {price:.2f}"
print(string.format(price = 49.853256234))

price = 49.853256234
fstring = f"Only for price {price:.3f}"
print(fstring)

asItIsFString = f"Hey my name is {{name}} and I am from {{country}}"
print(asItIsFString)


Video 27 KBC
questions= ["What is the capital of Pakistan?", "Which acid is called king of acids?", "Which word is used for 'swear' in shariah?", "When did the WW2 stated?"]
options=[("Multan", "Islamabad", "Karachi", "Lahore"), ("Nitric Acid", "Hydrochloric Acid", "Sulphuric Acid", "Oxalic Acid"), ("yameen", "jashae", "nzadhar", "altawadue"), ("1944", "1938", "1940", "1939")]
answers=('b', 'c', 'a', 'd')

qNum = 1
score = 0
for question in questions:
    print("\nQ", qNum, ' ', question)
    opt = ['a', 'b', 'c', 'd']
    optNum = 0
    for option in options[qNum - 1]:
        print(opt[optNum], '.', option, end='\t')
        optNum += 1
    answer = 'q'
    while (answer != 'a' and answer != 'b' and answer != 'c' and answer != 'd'):
        answer = str(input())
    if (answer == answers[qNum - 1]):
        print("right")
        score+=1
    else:
        print("wrong")
    qNum += 1
else:
    print("Your score is ", score)
    print("Your winning amount is ", score * 10000000)


Video 25
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
temp = list(tup)
temp.append(10)
tup = tuple(temp)
print(tup)


Video 24
tuple = (1, 5, 6, "tuple", True, ["list1", 123], ("anotherone", 2)) #unchangeable
print(type(tuple), tuple)
print(len(tuple))
print(len(tuple[5]), tuple[-1])
if ("anotherone", 2) in tuple:
    print("Yes (\"anotherone\", 2) is present ")


Video 23
l = [6, 2, 3, 4, 5, 1]
print(l)
l.append(7)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
print(l.index(6))
print(l.count(1))
m=l
m[0]=0
print(l)
m=l.copy()
m[0] = 9
print(l, m)
m.insert(0, 199)
print(m)
n=[900, 1000, 1100]
m.extend(n)
print(m)
k = m +l
print(k)


Video 21
def sum(a,b=0,c=0):
    print("a b c => ", a, b, c)
    return(a+b+c)
    
print(sum(a=5))
print(sum(c=1, b=5, a=5))

Video 20
def average (a, b, c):
    return (a + b + c)/3
def greater (a, b):
    if (a>b):
        return "a is greater"
    elif(a<b):
        return "b is greater"
    else:
        return "a and b are equal"
def lesser (a, b):
    # pass
    if (a<b):
        return "a is lesser"
    elif(a>b):
        return "b is lesser"
    else:
        return "a and b are equal"


print(average(1.1, 2.1, 3.1))
print(greater(4, 5))
print(lesser(4, 5))
    

Video 19
for i in range(1, 120):
    if(i >= 11):
        continue
    print("5 x ", i, " = ", 5 * i)
else:
    print("Loop is over")

Video 18
condition = True
while(condition):
    i = int(input("Enter i: "))
    print(i)
    condition = i<38
else:
    print("i is greater than 38")

Video 17
name=["Muhammad Umar", "Muhammad Daniyal Waseem", "Muhammad Khizar", "Muhammad Rayyan Asghar"]
for i in name:
    print(i,end=', ')
for k in range(90, 100, 2):
    print(k, end=" ")

Video 16
x=4
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case _ if x!=5:
        print("x is not 1,2,3,4,5")
    case _:
        print("x is 5")

Video 15
import time
currentTime=time.localtime()
currentHour = currentTime.tm_hour

if (currentHour < 5):
    print("Go sleep you psycho")
elif (currentHour < 10):
    print("Good morning")
elif(currentHour < 17):
    print("Good afternoon")
elif(currentHour < 19):
    print("Good evening")
else:
    print("Good night")

Video 14
age=int(input("Enter your age "))

if(age < 15):
    print("What are you doing here go study. You can't drive.")
elif(age < 18):
    print("You are underage. You can't drive.")
    print("Age threshold is 18.")
else:
    print("You can drive.")
    print("You can drive since age 18.")
print("i am outside coditional")

Video 13
a="i am a lower case string!!!!!!!!!"
b="i am an upper case string"
print(a.upper())
print(b.lower())
print(a.rstrip("!"))
print(b.replace("an upper case", "a simple"))
print(a.split(" "))
print(b.capitalize())
print(a.center(50))
print(b.count("a"))
print(a.endswith("!"))
print(b.find("a"))
print(a.index("a"))
print(b.isalpha())
print(a.isalnum())
print(b.islower())
print(a.isprintable())
print(b.isspace())
print(a.istitle())
"""