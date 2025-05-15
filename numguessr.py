from random import randint
from numguessr_logo import logo

# Global Constants
EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5

def play_game():
    # Choose a random number between 1 and 100
    random_num = randint(1, 100)

    print("\n" * 22)
    print(logo)
    def set_difficulty(selected_difficulty):
        """Sets the total attempts according to the difficulty level."""
        if selected_difficulty == "easy":
            return EASY_MODE_ATTEMPTS
        elif selected_difficulty == "hard":
            return HARD_MODE_ATTEMPTS
        return None

    def attempts_remaining(num):
        """Displays the remaining attempts."""
        print(f"You have {num} attempts remaining to guess the number.")

    # For grammar purposes
    def one_attempt_remaining():
        """Displays 1 attempt remaining."""
        print("You have 1 attempt remaining to guess the number.")

    print("Welcome to NumGuessr.\nI am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = set_difficulty(difficulty)
    attempts_remaining(attempts)
    
    game_over = False
    while not game_over:
        guess = int(input("Make a guess: "))
        if guess > random_num:
            attempts -= 1
            if attempts > 1:
                print("Too high.\nGuess again.\n")
                attempts_remaining(attempts)
            # Just for grammar purposes
            elif attempts == 1:
                print("Too high.\nGuess again\n")
                one_attempt_remaining()
        elif guess < random_num:
            attempts -= 1
            if attempts > 1:
                print("Too low.\nGuess again.\n")
                attempts_remaining(attempts)
            # Just for grammar purposes
            elif attempts == 1:
                print("Too low.\nGuess again.\n")
                one_attempt_remaining()
        elif guess == random_num:
            game_over = True
            print(f"You got it! The number was {random_num}.")
        if attempts == 0:
            game_over = True
            print(f"You have run out of guesses. The number was {random_num}.")

    replay = input("Do you want to play again? Type 'y' to play again or 'n' to exit game: ").lower()

    if replay == "y":
        play_game()
    elif replay == "n":
        print("Exited game.")

play_game()
