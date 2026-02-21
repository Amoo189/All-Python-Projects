m = int(input("Enter width:"))
n = int(input("Enter along:"))
s = ""
for i in range(n):
	s = s + "$"
#s =  "#" * n
for j in range(m):
	s = s + "$"
	print(s)
print ("Thank you for choose we're app!")
print("Please rateing us! from (1star)to(5 sta)")
b = int(input("Enter your rateing:"))
while b > 5or b < 0 or b == 0:
     if b == 0:
         print("Erorr!.the number is out of range. ")
         b = int(input("Enter your rateing:"))
     if b < 0:
         print("Erorr!.the number is out of range. ")
         b = int(input("Enter your rateing:"))
          
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
'''while b < 0:
    if b < 0:
        print("Erorr!.the number is out of range. ")
        b = int(input("Enter your rateing:"))
if b == 5:
    print("😁THANK YOU😁")
if b == 4:
    print("😎not bad😎")
if b == 3:
    print("🙂not good🙂")
if b == 2:
    print("😑bad,not matter.😑")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem.")
if b == 1:
    print("😔too bad😔")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem")'''