a = 0
b = 0
print("Welcome to the p number accuracy app!")
print("Increase the accuracy of the number from 1 to... (the desired number)")
n = int(input("Enter p number accuracy:"))
for i in range(1, n, 4):
	a = a + 1 / i
for j in range(3, n, 4):
	b = b + 1 / j
print(4*(a-b))
print ("Thank you for choose we're app!")
print("Please rateing us! from 1..5star")
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
    print("😔too bad 😔")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem")