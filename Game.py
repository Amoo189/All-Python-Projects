import random
a = random.randint(1, 100)
print('Welcome to guess the number game!')
print('Guess the number from 1 to 100')
guess = 0
while guess != a:
	guess = int(input("Enter your guess:"))
	if guess > a:
		print("The number is big!,Make it smaller")
	if guess < a:
		print("The number is small! Make it bigger")
	if guess == a:
		print("◇☆☆GOOD JOB, YOU WON!☆☆◇")
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
    print("😑bad😑")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem.")
if b == 1:
    print("😔too bad😔")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem")