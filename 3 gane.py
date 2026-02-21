print("Welcome to calculate area of cylinder and girth of circle and area of circle.")
a = int(input("Please choose your want calculate.for calculate area of cylinder click number(1)and for calculate grith of circle click number(2)and for calculate area of circle click number(3):"))
while a > 3:
    if a > 3:
        print("The number is out of range.please try again.")
        a = int(input("Please choose your want calculate.for calculate area of cylinder click number(1)and for calculate grith of circle click number(2)and for calculate area of circle click number(3):"))
if a == 1:
    n = int(input("Enter Ray:"))
    c = int(input("Enter High:"))
    V = 'V=S.H'
    x = ((n**2)*3.14)*c
    print(x)
if a == 2:
    d = int(input("Enter Diagonal:"))
    p = d*3.14
    print(p)
if a == 3:
    k = int(input("Enter Ray:"))
    f = (k**2)*3.14
    print(f)
print ("Thank you for choose we're app!")
print("Please rateing us! from (1star)to(5star)")
b = int(input("Enter your rateing:"))
while b > 5:    
     if b > 5:
         print("Erorr!.the number is out of range. ")
         b = int(input("Enter your rateing:"))
if b == 5:
    print("😁THANK YOU😁")
if b == 4:
    print("😎not bad😎")
if b == 3:
    print("🙂not good🙂")
if b == 2:
    print("😑bad,not matter😑")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem.")
if b == 1:
    print("😔too bad😔")
    v = input("Why don't you like our program?.what's wrong?:")
    print( "We will definitely follow up on this problem")