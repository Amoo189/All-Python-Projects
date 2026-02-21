#POWERED BY||SALEH AMOO||THETA||θ 
print("Welcome to the program for determining whether a number is prime or composite")
while True:
    n = int(input("Enter the number:"))
    counter = 0
    i = 2
    while i < n:
        if n%i == 0:
            counter += 1
            break
        i += 1
    if counter == 0:
	    print("%d  is a prime number."%(n))
    else:
	    print("%d is not a prime number."%(n))
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