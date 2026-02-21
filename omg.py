while True:
    text = input("Enter your words:")

    import re 
    a = [m[0] for m in re.finditer(r"(.)\1*",text)]
    print(a)                      