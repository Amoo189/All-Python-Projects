from math import *
print('____________________________')
print('This program can calculate pi number, e number, fabs of  number,floor of  number,ceil of  number,factorial,cos,sin,log of two numbers, pow of two number,sqrt of number,hypot of two numbers,radians,degrees,gcd,lcm.')
print('____________________________')
print('Note:Writing with keyboard and do not use than keyboard shortcuts')
print('____________________________')
print('Note:This program if you write number and word,remove number')
print('____________________________')
print('Note:you can write number or word not both')
print('____________________________')
while True:
    """print('This program can calculate pi number, e number, fabs of  number floor of  number,ceil of  number,factorial,cos,sin,log of twonumbers, pow of twonumber,sqrt of number,hypot of two numbers,radians,degrees.')"""
    o = input("Now,What do you want?:")
    if o == 'pi':
        print(f"The answer:{pi}")
        print('____________________________')
    if o == 'e':
        print(f"The answer:{e}")
        print('____________________________')
    if o == 'fabs':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{fabs(fa)}")
        print('____________________________')
    if o == 'floor':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{floor(fa)}")
        print('____________________________')
    if o == 'ceil':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{ceil(fa)}")
        print('____________________________')
    if o == 'factorial':
        fa = int(input("Enter your number:"))
        print(f"The answer is:{factorial(fa)}")
        print('____________________________')
    if o == 'cos':
        fa = int(input("Enter your number:"))
        print(f"The answer is:{cos(fa)}")
        print('____________________________')
    if o == 'sin':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{sin(fa)}")
        print('____________________________')
    if o == 'log':
        fa = float(input("Enter your first number:"))
        fas = float(input("Enter your second number:"))
        print(f"The answer is:{log(fa,fas)}")
        print('____________________________')
    if o == 'pow':
        fa = float(input("Enter your first number:"))
        fas = float(input("Enter your second number:"))
        print(f"The answer is:{pow(fa,fabs)}")
        print('____________________________')
    if o == 'sqrt':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{sqrt(fa)}")
        print('____________________________')
    if o == 'hypot':
        fa = float(input("Enter your first number:"))
        fas = float(input("Enter your second number:"))
        print(f"The answer is:{hypot(fa, fas)}")
        print('____________________________')
    if o == 'radians':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{radians(fa)}")
        print('____________________________')
    if o == 'degrees':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{degrees(fa)}")
        print('____________________________')
    if o == 'gcd':
        fa = int(input("Enter your first number:"))
        fas = int(input("Enter your second number:"))
        print(f"The answer is:{gcd(fa,fas)}")
        print('____________________________')
    if o == 'lcm':
        fa = int(input("Enter your first number:"))
        fas = int(input("Enter your second number:"))
        print(f"The answer is:{lcm(fa,fas)}")
        print('____________________________')