import random
a = random.randint(1, 100)
#print('Welcome to guess the number game!')
#print('Guess the number from 1 to 100')
print(a)
guess = input("The number is tru or falls?:")
while guess == 'n':
	a = random.randint(1, 100)
	c = []
	c.append(a)
	ss = set(c)
	print(ss)
	guess = input("The number is tru or falls?:")
	if guess == 'y':
		print("◇☆☆GOOD JOB, I'M  WON!☆☆◇")