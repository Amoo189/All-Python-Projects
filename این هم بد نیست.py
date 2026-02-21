import random
rand = random.randint(1, 100)
guess = int(input("Enter your guess:"))
while rand != guess:
    if rand > guess:
        print('Try a larger number.')
    else:
        print('Try a smaller number.')
    guess = int(input('Enter another guess:'))
print('Good job!')
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