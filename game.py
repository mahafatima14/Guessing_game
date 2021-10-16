"""A number-guessing game."""
import random
print("Hi")
# Put your code here
print("Hello, Welcome to the Guessing Game!")
name = input("What is your name? ")
print("Hey,", name)

right_ans = random.randint(1,100)
tries = 0

while True:
    guess = int(input("Im thinking of a number between 1 and 100. Can you guess what it is?"))
    if guess < right_ans:
        print("Too low!, Try again.")
        tries += 1
    elif guess > right_ans:
        print("Too high! Try again.")
        tries += 1
    else:
        print(f"Good Job!{name} you guessed the answer in {tries} attempts")
        break

   