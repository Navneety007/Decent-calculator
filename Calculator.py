import math

print("""
Calculator
Type : 
    '+' or 'add' to sum
    '-' or 'sub' to subtract
    'x' or '*' to multiply
    '/' or '%' to divide
    'sq' to square 
    'sqrt' to square root""")

def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)
def square(a):
    print(a*a)
def square_root(a):
    print(math.sqrt(a))

def calculate():
    take = input("Enter the operation type : ")
    if take == '+' or take == 'add':
        no1 = int(input("Enter the first no. : "))
        no2 = int(input("Enter the second no. : "))
        add(no1,no2)
    elif take == '-' or take == 'sub':
        no1 = int(input("Enter the first no. : "))
        no2 = int(input("Enter the second no. : "))
        subtract(no1,no2)
    elif take == 'x' or take == '*':
        no1 = int(input("Enter the first no. : "))
        no2 = int(input("Enter the second no. : "))
        multiply(no1,no2)
    elif take == '/' or take == '%':
        no1 = int(input("Enter the first no. : "))
        no2 = int(input("Enter the second no. : "))
        divide(no1,no2)
    elif take == 'sq':
        no1 = int(input("Enter the no. : "))
        square(no1)
    elif take == 'sqrt' :
        no1 = int(input("Enter the no. : "))
        square_root(no1)
    else:
        print("Invalid Input !!")
    
    take_ = input("Press Enter to Calculate again :- ")
    if take_ == "":
        calculate()
    else:
        exit()
calculate()