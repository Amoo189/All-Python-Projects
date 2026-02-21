print("Welcome to calculate sum many number program.")
print("Help:1=Enter your first number and for write next number only click the speac button,2=you can write many number don't worry.thanks!")
numbers = map(int, input("Enter your numbers:").split())
print(f"Sum of the numbes:{sum(numbers)}")
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