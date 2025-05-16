from random import randint
from numguessr_logo import logo

# Global Constants
EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5

def play_game():
    print("\n" * 22)
    print(logo)

    def verify_guess(num, random_number, total_attempts):
        """Checks to see if guess is higher or lower than the random number, then returns the attempts left."""
        if num > random_number:
            print("Too high.")
            return total_attempts - 1
        elif num < random_number:
            print("Too low")
            return total_attempts - 1
        return None

    def set_difficulty(selected_difficulty):
        """Sets attempts according to the difficulty level."""
        if selected_difficulty == "easy":
            return EASY_MODE_ATTEMPTS
        elif selected_difficulty == "hard":
            return HARD_MODE_ATTEMPTS
        return None

    print("Welcome to NumGuessr.\nI am thinking of a number between 1 and 100.")
    # Choose a random number between 1 and 100
    random_num = randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = set_difficulty(difficulty)

    game_over = False
    while not game_over:
        # Just for grammar purposes
        if attempts == 1:
            print("You have 1 attempt remaining to guess the number.")
        else:
            print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = verify_guess(guess, random_num, attempts)
        if guess == random_num:
            game_over = True
            print(f"You got it! The number was {random_num}.")
        if attempts == 0:
            game_over = True
            print(f"You have run out of guesses. The number was {random_num}.")
        elif guess != random_num:
            print("Guess again.\n")

    replay = input("Do you want to play again? Type 'y' to play again or 'n' to exit game: ").lower()

    if replay == "y":
        play_game()
    elif replay == "n":
        print("Exited game.")

play_game()
