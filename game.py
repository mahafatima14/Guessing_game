def guessing_game():
    """A number-guessing game."""
    
    print("Hello, Welcome to the guessing game")
    import random
    print("Hi")
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
guessing_game()

def play_again():
    """Ask the user if they wish to play again"""
    while True:
        play_choice = input("Do you want to play again?Y/N")
        play_choice = play_choice.upper()
        if play_choice == "Y":
            guessing_game()
        else:
            print("Thank you for playing!")
            break
play_again()