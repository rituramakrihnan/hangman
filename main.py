# Initializing the values
guessed_letters = []
max_attempts = 5
incorrect_guesses = []

# Function to display the current state of the word
def display_word(user_word, guessed_letters):
    display = ""
    for letter in user_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main function to start the Hangman game
def play_hangman():
    # Get the user word from player 1 in the Hangman game
    user_word = input("Enter a word for the game: ").lower()
    if not user_word.isalpha():
        print("Please enter a valid word containing only alphabetic characters.")
        return

    attempts = 0
    game_over = False
    current_display = "_" * len(user_word)

    while not game_over:
        # Check if the player has guessed the entire word
        if current_display == user_word:
            game_over = True
            break

        # Ask the player to guess a letter or the full word
        guess = input("Guess a letter or the full word: ").lower()

        # Check if the guess is a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            else:
                guessed_letters.append(guess)
                if guess in user_word:
                    print("Good guess!")
                    current_display = display_word(user_word, guessed_letters)
                else:
                    print("Incorrect guess.")
                    incorrect_guesses.append(guess)
                    # Increment the number of incorrect attempts
                    attempts += 1
        elif guess == user_word:
            current_display = user_word
            game_over = True
        else:
            print("Please enter a valid single letter or the full word.")

        # Display the current state of the word
        print("Current word:", current_display)
        print("Attempts left:", max_attempts - attempts)
        # Display the incorrect guesses
        if incorrect_guesses:
            print("Incorrect guesses:", ", ".join(incorrect_guesses))

        # Check if the player has run out of attempts
        if attempts >= max_attempts:
            print("Sorry, you've run out of attempts. The word was:", user_word)
            game_over = True

    if user_word == current_display:
        print("Congratulations! You've guessed the word:", user_word)
    else:
        print("Game over!")

def main():
    print("Welcome to Hangman!")
    play_hangman()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
