## function practice

def last_char(name):
    return name[-1]
print(last_char("Anoop"))# this is for printing last character of a string

###

def odd_even(num):
    if num%2==0:
        return "even"
    return "odd"
print(odd_even(9))

##
def is_ever(num):
    if num%2==0:
        return  True

print(is_ever(10))
def is_even1(num):
    return num%2==0

print(is_even1(10))

def song():
    return  "Happy birthday song"
print(song())


## function for which number is greater


def greater_than(a, b):
    if a>b:
        return a
    return b
num1= int(input("please enter a number"))
num2 =int(input("please enter a diff number"))

bigger = greater_than(num1, num2)
print(f"{bigger} is greater")



## function for threr numbers, which one is greater

def greater_than(a, b, c):
    if a>b and a>c:
        return a
    elif b>c and b >a:
        return b
    else:
        return c
num1= int(input("please enter a number"))
num2 =int(input("please enter a diff number"))
num3 =int(input("please enter a diff number"))

bigger = greater_than(num1, num2, num3)
print(f"{bigger} is greater")


## how to call a function in a function



def greater_than(a, b):
    if a>b:
        return a
    return b
num1= int(input("please enter a number"))
num2 =int(input("please enter a diff number"))
num3 =int(input("please enter a diff number"))


bigger = greater_than(num1, num2)
print(f"{bigger} is greater")
print(greater_than(bigger, num3))


## function for is_palindrome

def is_reverse(name):
    reversed_name = name[::-1]
    if name == reversed_name:
        return True
    else:
        return False
print(is_reverse("naman"))











