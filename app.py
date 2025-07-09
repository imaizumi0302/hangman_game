import random


# This function lets the user choose a difficulty level and returns a random word accordingly
# , "frozen", "inception", "parasite"
def choose_difficulty():
    word_list_easy = ["titanic", "frozen", "inception", "parasite"]
    word_list_medium = ["black panther", "la la land", "jurassic park", "finding nemo"]
    word_list_difficult = ["pirates of the caribbean","the lord of the rings","everything everywhere all at once"]

    while True:
        difficulty_level = input("choose difficulty level (easy = 1, medium = 2, hard = 3):")

        # Return a random word based on selected difficulty
        if difficulty_level == "1":
            return random.choice(word_list_easy)
        elif difficulty_level == "2":
            return random.choice(word_list_medium)
        elif difficulty_level == "3":
            return random.choice(word_list_difficult)
        else:
            # Handle invalid input
            print("invalid difficulty level. please enter a number again.")
            print()


# This function initializes the current word list with underscores for letters and spaces preserved
def initialize_word(answer):
    current_word_list = []
    for i in answer:
        if i == " ":
            current_word_list.append(" ")  # Keep spaces visible
        else:
            current_word_list.append("_")  # Replace letters with underscores
    return current_word_list


# This function displays the current state of the game: word, guessed letters, and remaining attempts
def display_status(current_word_list, guessed_letters, incorrect_guesses_remaining):
    print()
    print(f"Current word: {' '.join(current_word_list)}")  # Show underscores or revealed letters
    print(f"Guessed letters: {guessed_letters}")  # List of guessed letters
    print(f"Incorrect guesses remaining: {incorrect_guesses_remaining}")  # Remaining mistakes allowed


# This function gets the player's letter guess and validates the input
def get_guess(guessed_letters):
    while True:
        your_guess = input("Guess a letter:")
        your_guess = your_guess.lower()

        # Check for non-alphabetical input
        if not your_guess.isalpha():
            print("Invalid input. Please enter a letter.")
            print()

        # Check for repeated guesses
        elif your_guess in guessed_letters:
            print("You already guessed that letter. Please try again.")
            print()

        else:
            return your_guess


# This function processes the guess and updates the game state accordingly
def process_guess(answer, your_guess, guessed_letters, current_word_list, incorrect_guesses_remaining):
    if your_guess.lower() in answer:
        print(f"Good job! '{your_guess}' is in the word.")
        guessed_letters.append(your_guess)  # Add guess to guessed letters

        # Reveal the correct letter in all matching positions
        for i, c in enumerate(answer):
            if c == your_guess:
                current_word_list[i] = your_guess.lower()
        print()
        return incorrect_guesses_remaining

    else:
        print(f"Sorry, '{your_guess}' is not in the word.")
        guessed_letters.append(your_guess)
        incorrect_guesses_remaining -= 1  # Reduce attempts for wrong guess
        print()
        return incorrect_guesses_remaining


# Main program starts here
print("Welcome to Hangman!")
print()

answer = choose_difficulty()  # Choose a word based on difficulty
current_word_list = initialize_word(answer)  # Initialize the display word with underscores
guessed_letters = []  # Store guessed letters
incorrect_guesses_remaining = 6  # Number of incorrect guesses allowed

# Main game loop
while True:
    display_status(current_word_list, guessed_letters, incorrect_guesses_remaining)  # Show game status

    your_guess = get_guess(guessed_letters)  # Get a new letter from the user

    incorrect_guesses_remaining = process_guess(
        answer, your_guess, guessed_letters, current_word_list, incorrect_guesses_remaining
    )  # Update game state based on guess

    # Check if the player has run out of attempts
    if incorrect_guesses_remaining == 0:
        print(f"Game over! The word was: {answer}")
        break

    # Check if the player has guessed the full word
    elif "_" not in current_word_list:
        print(f"Congratulations! You guessed the word: {answer}")
        break