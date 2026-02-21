a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your third number:"))
d = int(input("Enter your fourth number:"))
e = int(input("Enter your fifth number:"))
g = int(input("Enter your sixth number:"))
f = int(input("Enter your seventh number:"))
h = int(input("Enter your eighth number:"))
data = [a, b, c, d, e, f, g, h]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0
        print(data)