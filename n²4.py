#n = int(input("Enter the number:"))
#sum = 0**2
#a = 1**2
#while a < n+1:
#    sum = sum + a**2
#    a = a + 1
#print(sum)

#n = int(input("Enter the number:"))
#sum = 0**3
#a = 1**3
#while a < n+1**3:
#    sum = sum + a**3
#    a = a + 1
#print(sum)

'''n = int(input("Enter the number:"))
sum = 0
#a = 1
#while a < n+1:
for a in range(1, n+1, 1):
    sum = sum + a
    #a = a + 1
print(sum)'''

'''n = int(input("Enter the number:"))
sum = 0**0
a = 1**1
while a < n+1**n:
    sum = sum + a**a
    a = a + 1
print(f"{sum-1:,}")'''


'''print ("Thank you for choose we're app!")
                print("Please rateing us! from (1star)to(5 star)")
                b = int(input("Enter your rateing:"))
                while b > 5 or b < 0 or b == 0:
                    if b == 0:
                        print("Erorr!.the number is out of range. ")
                        b = int(input("Enter your rateing:"))
                    if b < 0:
                        print("Erorr!.the number is out of range. ")
                        b = int(input("Enter your rateing:"))  
                    if b > 5:
                        print("Erorr!.the number is out of range. ")
                        b = int(input("Enter your rateing:"))

    if b < 0:'''


a = []
for i in range(7):
    n = int(input('enter your number:'))
    a.append(n)
#print(sorted(a))
a.sort(reverse=True)
print(a)

