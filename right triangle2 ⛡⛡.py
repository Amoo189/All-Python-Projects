#⛮POWERED BY || SALEH AMOO
def r(c, f, s):
    if c ** 2 == f ** 2 + s ** 2:
        return 'it is a Right triangle'
    else:
        return 'it is not a Right triangle.'
c = int(input("Enter the Chord of Right triangle:"))
f = int(input("Enter the first Left over Line of Right triangle:"))
s = int(input("Enter the second Left over Line of Right triangle:"))
r = r(c, f, s)
print(r)