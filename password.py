from random import randint 
print("Welcome to the random password generator program")
char = ["3", "5", "s", "6", "M", "S", "1", "a", "b", "c"]
password = ""
for i in range (10):
    key = randint(1, len(char))
    password = password + char[key-1]
print(password )
print("Password maked.")
#vv = input("Enter password:")
#if vv == password:
#    print("Welcome Owenr of mobile. ")
#else:
 #   print("ERORR A113.")
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