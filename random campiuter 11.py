import random
a = random.randint(1, 100)
#print('Welcome to guess the number game!')
#print('Guess the number from 1 to 100')
print(a)
guess = input("The number is tru or falls?:")
while guess == 'f':
	a = random.randint(1, 100)
	c = []
	cc = []
	c.append(a)
	for item in c:
	    if item not in cc:
	        cc.append(item)
	print(cc)
	guess = input("The number is tru or falls?:")
	if guess == 't':
		print("◇☆☆GOOD JOB, I'M  WON!☆☆◇")