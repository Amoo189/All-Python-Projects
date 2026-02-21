#POWERED BY||SALEH AMOO||BETA||β
#┄┄┄┅┅❅✾❅┅┅┄┄┄
n = int(input("Enter the number:"))
i = 1
while i < n+1:
#	print(f"i: {i}")
	if n%i==0:
		print(i)
	i += 1
#n = int(input('Enter the number: '))
#i = 2
#counter = 0
#whi'le i <= n:
#    if n%i==0:
#        counter = counter + 1
#    i = i + 1
#print(counter)
print ("Thank you for choose we're app!")
print("Please rateing! from (1star)to(5star)")
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