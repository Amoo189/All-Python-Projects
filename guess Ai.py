a = 1
b = int(input("Enter your range:"))
print("if your guess < my guess 2,  if your guess > my guess 1, if your guess == my guess 3")
print('-----------—————-----------')
guess = 0
while b >= a:
    m = (a+b) // 2
    print(f"I guess the {m} ")
    guess += 1
    x = int(input(""))
    if x == 2:
        a = m +1
    elif x == 1:
        b = m-1
    else :
        print(f"I won :) in {guess} guess")
        break 
        