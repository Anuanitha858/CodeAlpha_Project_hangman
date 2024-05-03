import random

# List of words for the game
words = ["apple", "banana", "orange", "grape", "kiwi", "peach", "strawberry", "blueberry", "watermelon"]

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    print("Welcome to Hangman!")
    word = choose_word(words)
    guessed_letters = []
    attempts = 6

    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")
            if attempts == 0:
                print("Sorry, you ran out of attempts. The word was:", word)
                break
        else:
            print("Good guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

hangman()

