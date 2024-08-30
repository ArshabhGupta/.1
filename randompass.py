import random
password = random.randint(0,9999)
print("You have to guess the password!")
def pick():
	guesses = 8
	while guesses > 0:
		guess = input()
		guess = int(guess)
		if guess != password:
			print("Incorrect password! Please try again!")
		if guess == password:
			break
		guesses = guesses - 1
		if guesses == 0:
			print("Too many tries please try again later!", password)
pick()