import random 
number = random.randint(1,10)
for i in range(0,3):
	user= int(input("Guess the number:-"))
	if user == number:
		print("Hurray!")
		print("You have guessed the right number")
		break
if user!= number:
	print("Wrong guess")
