print("Welcome to the Oregon Trail")
print("You set off with your family west")

def challenge_1():
	#Challenge 1
	print("YOU HEAR A SCREAM")
	print("A bear attacks your little Timmy")
	print("You have a choice")
	print("a. grab your gun")
	print("b. run for your life")

	user_input = input()

	if user_input == "a":
		print("you shoot the bear and survive good job")
		return "alive"
	elif user_input == "b":
		print("little Timmy is eaten by the bear")
		return "dead"
	else:
		print("you selected neither option and were eaten by the bear good game")
		return "dead"

def challenge_2():
	#Challenge 2
	print("A mystic meets you on the road and says he's thinking of two numbers between 1 and 10. You must guess a number between his numbers or you will die ")
	print("guess a number from 1-10")
	user_input = int(input())
	if user_input > 5 and user_input < 7:
		print("wow you somehow survived")
		return "alive"
	else:
		print("you were wrong. the mystic magic puts a spell on you and you melt and die")
		return "dead"

def challenge_3():
	#Challenge 3
	print("You have to cross a land known for snakes")
	print("Pick a number between 10 and 15. If you pick the unlucky number you die")
	user_input = int(input())
	if user_input < 10 or user_input > 15:
		print("you couldn't follow the rules and died")
		return "dead"
	else:
		if user_input != 13:
			print("the snake does not attack you")
			return "alive"
		else:
			print("you knew that was an unlucky number but you picked it anyway and died")
			return "dead"

alive = "alive"
import random
challenge_history = []

history = ""

while alive == "alive":
	challenge_number = random.randint(1,3)
	challenge_history.append(challenge_number)
	if challenge_number == 1:
		alive = challenge_1()
		history = history + "1 "
	elif challenge_number == 2:
		history = history + "2 "
		alive = challenge_2()
	elif challenge_number == 3:
		history = history + "3 "
		alive = challenge_3()

print("you are now dead good game")

filename = "history.txt"
with open(filename, 'w') as f:
    f.write(history)
