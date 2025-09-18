import random
import sys

# Hangman stages - ASCII art to show hangman progress
HANGMAN_PICS = ['''
  +---+
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

# Word lists by difficulty
EASY_WORDS = ['cat', 'dog', 'sun', 'book', 'tree', 'fish']
MEDIUM_WORDS = ['python', 'hangman', 'garden', 'planet', 'window']
HARD_WORDS = ['astronomy', 'difficult', 'pneumonia', 'xylophone', 'subtle']

def choose_word(difficulty):
    """Choose a random word based on difficulty."""
    if difficulty == 'easy':
        word = random.choice(EASY_WORDS)
    elif difficulty == 'medium':
        word = random.choice(MEDIUM_WORDS)
    else:
        word = random.choice(HARD_WORDS)
    return word.lower()

def get_difficulty():
    """Ask the user to select a difficulty level."""
    while True:
        print("Select difficulty: easy / medium / hard")
        choice = input("Your choice: ").lower()
        if choice in ['easy', 'medium', 'hard']:
            return choice
        else:
            print("Invalid choice. Please select easy, medium, or hard.")

def display_status(hangman_pics, wrong_guesses, guessed_letters, word_display):
    """Display the current game state."""
    print(hangman_pics[len(wrong_guesses)])
    print("\nWord: ", ' '.join(word_display))
    print("Guessed letters:", ' '.join(sorted(guessed_letters)))
    print(f"Wrong guesses ({len(wrong_guesses)}):", ' '.join(wrong_guesses))

def get_guess(guessed_letters):
    """Prompt the user for a guess and validate input."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter! Try again.")
        else:
            return guess

def play_round():
    difficulty = get_difficulty()
    word = choose_word(difficulty)
    word_display = ['_' for _ in word]
    guessed_letters = set()
    wrong_guesses = []

    max_wrong = len(HANGMAN_PICS) - 1  # Max wrong guesses allowed

    print(f"\nLet's start! Difficulty: {difficulty.capitalize()}")
    print(f"You have {max_wrong} wrong guesses before the hangman is complete.")

    while True:
        display_status(HANGMAN_PICS, wrong_guesses, guessed_letters, word_display)

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! The letter '{guess}' is in the word.")
            # Reveal the guessed letters in the display
            for idx, letter in enumerate(word):
                if letter == guess:
                    word_display[idx] = guess
            # Check if player won
            if '_' not in word_display:
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            wrong_guesses.append(guess)
            # Check if player lost
            if len(wrong_guesses) == max_wrong:
                display_status(HANGMAN_PICS, wrong_guesses, guessed_letters, word_display)
                print("\nGame Over! You ran out of guesses.")
                print(f"The word was: {word}")
                break

def main():
    print("Welcome to Hangman!")
    while True:
        play_round()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ('yes', 'y'):
            print("Thanks for playing! Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()
