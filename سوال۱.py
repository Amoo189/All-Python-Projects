import random

def generate_password(name, ational_code):
    last_digit = int(ational_code[-1])
    lg = int(max(ational_code))
    password = ""
    char2 = []
    char4 = []
    char5 = []
    for char in name:
        char2.append(char)
    for char3 in ational_code:
        char4.append(char3)
    char5.append(char3)
    char5.append(char4)

    if last_digit % 2 == 0:
        password += ''.join(filter(str.isalpha, name))
        password += ''.join(random.choices(char2, k=2*lg+4))
    else:
        password += str(last_digit)
        password += ''.join(random.choices(char2, k=2*lg+4))
    
    return password

name = input("Enter name:")
ational_code = input("Enter ational_code:")

password = generate_password(name, ational_code)
print("Rnadom password:", password)