print("Welcome to the bank interest calculation program according to interest percentage and year")
balance = int(input('Enter your balance: ')) 
bank_interest = int(input('Enter your bank interest: ')) 
year = int(input('How many years? ')) 
for i in range(year):
    balance = balance + bank_interest/100 * balance
#print(balance)
print(f"{balance:,}")
print ("Thank you for choose we're app!")
print("Please rateing us! from (1star)to(5star)")
b = int(input("Enter your rateing:"))
while b > 5 or b < 0 or b == 0:
     if b == 0:
         print("Erorr!.the number is out of range. ")
         b = int(input("Enter your rateing:"))
     if b < 0:
         print("Erorr!.the number is out of range. ")
         b = int(input("Enter your rateing:"))   
     if b > 5:
         print("Erorr.the number is out of range. !")
         b = int(input("Enter your rateing:"))
if b == 5:
    print("😁THANK YOU😁")
if b == 4:
    print("😎not bad😎")
if b == 3:
    print("🙂not good🙂")
if b == 2:
    print("😑bad,not matter 😑")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem.")
if b == 1:
    print("😔too bad😔")
    v = input("Why don't you like our program?:")
    print("We will definitely follow up on this problem.")
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