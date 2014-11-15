import random

random_number = random.randint(1, 10)
allowed_guesses = 5
tried_guesses = 0

while tried_guesses < allowed_guesses:
    try:
        picked_number = int(input("Guess a number between 1 and 10: "))
        tried_guesses += 1
    except:
        print("Error, '{}' isn't a number, please enter only numbers.")
        continue

    if picked_number < random_number:
        print("{} is smaller than the correct answer, please try again. You've tried {} time(s), and you have {} time(s) left.".format(picked_number, tried_guesses, allowed_guesses - tried_guesses))
        continue
    elif picked_number > random_number:
        print("{} is bigger than the correct answer, please try again. You've tried {} time(s), and you have {} time(s) left.".format(picked_number, tried_guesses, allowed_guesses - tried_guesses))
        continue
    else:
        print("Congratulations! {} is the correct answer. Tried {} time(s)".format(picked_number, tried_guesses))
        break
