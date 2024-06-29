"""
#video 81
#Hybrid and Hierarchical Inheritance in Python

class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

class Car:
    pass

class TwoWheeler:
    pass

#parent child are in hierarchical inheritance 
#if we have more than 1 type of inheritance than it give us hybrid inheritance


#video 80
#Multilevel Inheritance in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_detail(self):
        print(f"{self.name}\n{self.age}")

class Employee(Person):
    def __init__(self, name, age, qualification):
        super().__init__(name, age)
        self.qualification = qualification
    
    def show_detail(self):
        super().show_detail()
        print(f"{self.qualification}")

class Programmer(Employee):
    def __init__(self, name, age, qualification, lang):
        super().__init__(name, age, qualification)
        self.lang = lang
    
    def show_detail(self):
        super().show_detail()
        print(f"{self.lang}")

me = Programmer("Muhammad Umar", 19, "Undergrad", ["C++", "python", "java"])
me.show_detail()


#video 79
#Multiple Inheritance in Python

class Employee:
    def __init__(self):
        print("Employee")
        
class Dancer:
    def __init__(self):
        print("Dancer")

class DancerEmployee(Employee, Dancer):
    def __init__(self):
        super().__init__()

de = DancerEmployee()
print(DancerEmployee.mro())


#video 78
#Single Inheritance in Python

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Bhaow Bhaow")
        
class Cat(Animal):
    def meow(self):
        print("Meow Meow")

class Lion(Animal):
    def roar(self):
        print("grraaaauuuu")

doggy  = Dog('doggy')
kitty  = Cat('kitty')
king  = Lion('king')

doggy.bark()
kitty.meow()
king.roar()


#video 77
#Operator Overloading in Python

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f"{self.a}+{self.b}i"

    def __add__(self, vec):
        return Complex(self.a + vec.a, self.b + vec.b)

    def __sub__(self, vec):
        return Complex(self.a - vec.a, self.b - vec.b)

    def __mul__(self, vec):
        return Complex(self.a * vec.a, self.b * vec.b)

    def __truediv__(self, vec):
        a = round(self.a / vec.a)
        b = round(self.b / vec.b)
        return Complex(a, b)
    
    def __eq__(self, vec):
        return self.a == vec.a and self.b == vec.b 

    def __ne__(self, vec):
        return self.a != vec.a or self.b != vec.b 

    def __le__(self, vec):
        return self.a <= vec.a and self.b <= vec.b 

    def __ge__(self, vec):
        return self.a >= vec.a and self.b >= vec.b 

    def __invert__(self):
        return Complex(self.b, self.a)

comp1 = Complex(2, 5)
comp2 = Complex(6, 5)

print(comp1 + comp2)
print(comp1 - comp2)
print(comp1 * comp2)
print(comp1 / comp2)
print(comp1 == comp2)
print(comp1 != comp2)
print(comp1 <= comp2)
print(comp1 >= comp2)
print(~comp1)


#video 76
#Exercise 8 - Merge the PDF
from pypdf import PdfWriter

merger = PdfWriter()
for pdf in ["pdfs/1.pdf", "pdfs/2.pdf"]:
    merger.append(pdf)
merger.write("pdfs/merged.pdf")
merger.close()

#video 75
#Exercise 7 - Clear the Clutter - Solution 
import os

def clearClutter(ext):    
    clutter_files = os.listdir('clutter')
    index = 0 #logic chagen ends with used
    for file in clutter_files:
        if file.endswith(ext):
            os.rename(f'clutter/{file}', f'clutter/{index}{ext}' )
            index = index + 1

clearClutter('.mp3')
clearClutter('.png')


#video 74
#Method Overriding in Python

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

rec = Shape(5, 8)
print(rec.area())
crc = Circle(7)
print(crc.area())

#video 73
#Magic/Dunder Methods in Python

from typing import Any


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __len__(self): #return length of object
        return len(self.name) + self.age
    
    def __str__(self):
        return "instant vars: name<string>, age<int>, methods: no methods"
    
    def __repr__(self):
        return f"Representation Person('{self.name}', {self.age})"
    
    def __call__(self, name, age):
        self.name = name
        self.age = age
        return self

p = Person("Muhammad Umar", 19)
print(len(p))
print(p)
p("You", 20)
print(p.name)
print(p.age)

#video 72
#Super Keyword in Python

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def info(self):
        print(self.name)
        print(self.id)

class Programmer(Employee):
    def __init__(self, name, id, lang):
        self.lang = lang
        super().__init__(name, id)
    def info(self):
        super().info()
        print(self.lang)

you = Employee('You', 1122)
me = Programmer('Umar', 7831, 'Python')
you.info()
me.info()

#video 71
#dir, __dict__ and help method in Python

x = [1, 2, 3]
# print(dir(x))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobby = 'religious content creation'

p = Person('Muhammad Umar', 19)
print(p.__dict__)
print(help(Person))
print(help(p))

#video 70
#Class Methods as Alternative Constructors in Python
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def dashStrConstructor(self, dashStr):
        return self(dashStr.split('-')[0], dashStr.split('-')[1])

a = Employee("emp1", 19)
b = Employee.dashStrConstructor("emp2-34")
c = Employee.dashStrConstructor("emp3-28")
print(a.name, a.age)
print(b.name, b.age)
print(c.name, c.age)


#video 69
#Class Methods in Python

class Employee:
    company = "Apple"
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"Name: {self.name}\nCompany: {self.company}")
    @classmethod
    def changeCo(self, co):
        self.company = co

a = Employee("Employee 1")
a.show()
a.changeCo("Tesla")
a.show()
print(Employee.company)

#video 68
#Exercise 7 - Clear the Clutter
import os

def clearClutter(ext):    
    clutter_files = os.listdir('clutter')
    index = 0
    for file in clutter_files:
        split_name = os.path.splitext(file)
        if ext == split_name[1]:
            os.rename(f'clutter/{file}', f'clutter/{index}{split_name[1]}' )
            index = index + 1

clearClutter('.mp3')

#video 67
#shouts and solution of exercise 6

#video 66
#Instance variables vs Class variables in Python

class Employee:
    company_name = 'BICE'
    no_employees = 0
    def __init__(self, name):
        self.name = name
        Employee.no_employees += 1
    
    def info(self):
        print(f"Compnay: {self.company_name}\n#Employees {Employee.no_employees}\nName: {self.name}")

a = Employee('Umar')
b = Employee('Ali')
a.company_name = "LAVI"
a.info()
b.info()

#cideo 65
#Static Methods in Python
class Math:
    def __init__(self, num):
        self.num = num
    
    def addToNum(self, val):
        self.num = self.num + val
    
    @staticmethod
    def sum(a, b):
        return a + b
    
a = Math(5)
a.addToNum(5)
print(a.num)
print(a.sum(1, 2))


#video 64
#Exercise 6

class Library:
    def __init__(self, books):
        self.books = books
        self.no_books = len(books)
    
    def showBooks(self):
        for book in self.books:
            print(book)
    
    def checkValidNOBooks(self):
        return len(self.books) == self.no_books

a = Library(["Book1", "Book2", "Book3", "Book4"])
a.no_books = 5
a.showBooks()
print(a.checkValidNOBooks())

#video 63
#shoutouts + exercise 5 solution


#video 62
#Access Method in Python

class Employee:
    def __init__(self, name, id):
        self.__name = name
        self.id = id

a = Employee("Muhammad Umar", 7831)
print(a.id)# by default public
# print(a.__name) #will give error because __name is made private here and can't be access directly
print(a._Employee__name) #but can be accessed indirectly
#_varname convention for protected but python do not enforce access modifire it only do mangling on __ thing

#video 61
#Inheritance in Python

class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name
    def showDetails(self):
        print(f"ID: {self.id}\nName: {self.name}")

class Programmer(Employee):
    def __init__(self, name, id, lang):
        Employee.__init__(self, name, id)
        self.lang = lang
    def showDetails(self):
        Employee.showDetails(self)
        print(f"Language: {self.lang}")


a = Programmer("Muhammad Umar", 7831, "C++")
a.showDetails()

b = Employee("Shaheerah Khaild", 5231)
b.showDetails()

#video 60
#Getters and Setters in Python

class MyClass:
    def __init__(self, value):
        self.value = value
    @property
    def ten_x_value(self):
        return self.value * 10
    @ten_x_value.setter
    def ten_x_value(self, value):
        self.value = value / 10
    def info(self):
        print(f"Value is {self.value}")


a = MyClass(10)
a.info()
a.ten_x_value = 10
print(a.ten_x_value)
print(a.value)

#video 59
#Decorators in Python

def tryCatch(fx):
    def mfx(*args, **kwargs):
        try:
            fx(*args, **kwargs)
        except:
            print('Something went wrong')
    return mfx

def greet(fx):
    def mfx(*args, **kwargs):
        print('Decorator Start!')
        fx(*args, **kwargs)
        print('Decorator End')
    return mfx

@greet
def hello():
    print('Hello World')

@tryCatch
@greet
def add(a, b):
    print(a + b)

hello()
add(1, 3)

#video 58
#Constructors in Python
class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    def info(self):
        return f"Name: {self.name}\nOccupation: {self.occupation}"
    
a = Person("Muhammad Umar", "Software Developer")
b = Person("Shaheerah Khaild", "HR")

print(a.info())
print(b.info())

#video 57
#Classes and Objects in Python
class Person:
    name = 'Harry'
    occupation = 'Software Developer'
    netWorth = 10000000
    def info(self):
        return f"Name: {self.name}\nOccupation: {self.occupation}\nNet Worth= {self.netWorth}"
    
a = Person()
a.name = 'Harry Bhai'
print(a.info())

#video 56
#Introduction to OOPs in Python 
#theory

#video 55
#Rock Paper Scissor
import random
import os

judge = {
    'r': 'p',
    'p': 's',
    's': 'r'
}
score = 0
timeLine = []

def clear_console():
    # Clear console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    choice = input('Press:\nr for rock🪨\np for paper📝\ns for scissor✂️\nanyother key to exit\nEnter your choice\n')
    computerChoice = random.choice(['r', 'p', 's'])
    if choice == computerChoice:
        print(f"you: {choice} | python: {computerChoice}")
        timeLine.append({'Draw', 0})
        print('Draw')
    elif choice == 'r' or choice == 'p' or choice == 's':
        print(f"you: {choice} | python: {computerChoice}")
        if judge[choice] == computerChoice:
            timeLine.append({'Lose', -1})
            print('Lose')
            score = score - 1
        else:
            timeLine.append({'Win', 1})
            print('Win')
            score = score + 1
    else:
        clear_console()
        break
    input("Press Enter to continue...")
    clear_console()

print(f"Total Score: {score}")
print(f"History: {timeLine}")


#video 54
#'is' vs '==' in Python

a = "4"
b = 4
#is compare exact memory
#== compare value 
print(a is b)#False
print(a == b)#Fasle

a = 1
b = 1
print(a is b)#True beacuse the constant is immutable and python store both of them at same memory location same for all immutable datatypes like tuples, string
print(a == b)#True beacuse the constant is immutable and python store both of them at same memory location same for all immutable datatypes like tuples, string

a = [1,2,3]
b = [1,2,3]
print(a is b)#False
print(a == b)#True list not immutable so a and b are copy of each other at different memory locations

#video 53
#Map, Filter and Reduce in Python
from functools import reduce

l = [1,2,3,4,5]
cube = lambda x: x*x*x
cubedL = map(cube, l)
print(list(cubedL))

qualifier = lambda x: True if x % 2 == 1 else False

oddL = filter(qualifier, l)
print(list(oddL))

reducedL = reduce(lambda x, y: x + y, l)
print(reducedL)


#video 52
#Lambda functions in Python

cal = lambda fn, val: fn(val)

avg = lambda a,b,c: (a + b + c) / 2
square = lambda x: x*x
cube = lambda x: x*x*x

print(cal(cube,2))
print(cal(square,2))
print(avg(1,2,3))


#video 51
#seek(), tell() and other functions
with open('marks.txt', 'r') as f:
    f.seek(10)
    print(f.tell())
    print(f.read(8))

with open('marks.txt', 'a') as f:
    f.write("57,23,34\n27,75,13\n49,87,83\n42,32,83")
    f.truncate(28)


#video 50
#read(), readlines() and other methods
def showMarks():
    with open('marks.txt', 'r') as f:
        i = 1
        while True:
            line = f.readline()
            if not line:
                break
            else:
                marks = line.split(",")
                m1 = int(marks[0])
                m2 = int(marks[1])
                m3 = int(marks[2])
                print(f"Student {i} SST Marks: {m1}/110 ({round(m1/100 * 110)}%)")
                print(f"Student {i} Math Marks: {m2}/110 ({round(m1/100 * 110)}%)")
                print(f"Student {i} Science Marks: {m3}/110 ({round(m1/100 * 110)}%)")
                print("\n")
            i+=1

def addMarks(marks):
    with open('marks.txt', 'a') as f:
        f.writelines(f"\n{marks[0]},{marks[1]},{marks[2]}")

# marks= [42, 32, 83]
# addMarks(marks)
showMarks()


#vid 49
#File IO in Python
f = open('wellcome.py')
text = f.read()
print(text)
f.close()

with open('wellcome.py', 'a') as append:
    append.write("#text from tutorial 49")

#vid 48
#local vs global variables
x = 10
def func():
    global x
    x = 5
print(f"global x before function call {x}")
func()
print(f"global x after function call {x}")

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