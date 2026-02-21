from math import *
from fraction import *
print('____________________________')
print('This program can calculate pi number, e number, fabs of  number,floor of  number,ceil of  number,factorial,cos,sin,log of  numbers, pow of two number,sqrt of number,hypot of two numbers,radians,degrees,tan,ک.م.م ,ب.م..م‌ هم اضافه کردم.')
print('____________________________')
print('Note:Writing with keyboard and do not use than keyboard shortcuts')
print('____________________________')
print('Note:This program if you write number and word,remove number')
print('____________________________')
#print('Note:you can write number or word not both of them.')
print('____________________________')
while True:
    """print('This program can calculate pi number, e number, fabs of  number floor of  number,ceil of  number,factorial,cos,sin,log of twonumbers, pow of twonumber,sqrt of number,hypot of two numbers,radians,degrees.')"""
    print('Help:pi for pi,e for e,f for fabs,fl for floor,c for ceil,! for factorial, cos for cos,sin for sin,l  for log,po for pow, sq for sqrt,hy for hypot,radi for radians, degr for degrees ب.م.م برای ب.م.م ک.م.م برای ک.م.م.')
    print('____________________________')
    o = input("Now,What do you want?:")
    '''print('Help:p for pi,e for e,f for fabs,fl for floor,c for ceil,fa for factorial, cos for cos,sin for sin,l  for log,po for pow, sq for sqrt,hy for hypot,radi for radians, degr for degrees.')
    
    print('Help:p for pi,e for e,f for fabs,fl for floor,c for ceil,fa for factorial, cos for cos,sin for sin,l  for log,po for pow, sq for sqrt,hy for hypot,radi for radians, degr for degrees.')'''
    
    if o == 'pi':
        print(f"The answer:{pi}")
        print('____________________________')
    if o == 'e':
        print(f"The answer:{e}")
        print('____________________________')
    if o == 'f':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{fabs(fa)}")
        print('____________________________')
    if o == 'fl':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{floor(fa)}")
        print('____________________________')
    if o == 'c':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{ceil(fa)}")
        print('____________________________')
    if o == '!':
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
    if o == 'l':
        fa = float(input("Enter your number:"))
       # fas = float(input("Enter your second number:"))
        print(f"The answer is:{log(fa)}")
        print('____________________________')
    if o == 'po':
        fa = float(input("Enter your first number:"))
        fas = float(input("Enter your second number:"))
        print(f"The answer is:{pow(fa,fas)}")
        print('____________________________')
    if o == 'sq':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{sqrt(fa)}")
        print('____________________________')
    if o == 'hy':
        fa = float(input("Enter your first number:"))
        fas = float(input("Enter your second number:"))
        print(f"The answer is:{hypot(fa, fas)}")
        print('____________________________')
    if o == 'radi':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{radians(fa)}")
        print('____________________________')
    if o == 'degr':
        fa = float(input("Enter your number:"))
        print(f"The answer is:{degrees(fa)}")
        print('____________________________')
    if o == 'tan':
        fa = int(input('Enter your number:'))
        print(f"The answer is:{tan(fa)}")
        print('____________________________')
    if o == "ب.م.م":
       fos = int(input("Enter your first number:"))
       fos2 = int(input("Enter your second number:"))
       I = Fraction(fos, fos2)
       print(f"The answer is {I}")
    if o == "ک.م.م":
       fos = int(input("Enter your first number:"))
       fos2 = int(input("Enter your second number:"))
       print(f"The answer is{gcd(fos, fos2)}")