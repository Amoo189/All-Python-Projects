print("Welcome to calculate n mold fibonachi app. ")
n = int(input('Enter the n: '))
a = 1
b = 1
c = 0
i = 2
while i < n:
    c = a + b
    a = b
    b = c
    i = i + 1
print(c)
print ("Thank you for choose we're app!")
print("Please rateing us! from (1star)to(5 star)")
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
    print("😑bad😑")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem.")
if b == 1:
    print("😔too bad😔")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem")