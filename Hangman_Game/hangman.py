import random

words = ["python", "computer", "student", "program", "science"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("=== Hangman Game ===")

while wrong_guesses < max_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_guesses - wrong_guesses)

    # Check if all letters are guessed
    completed = True
    for letter in word:
        if letter not in guessed_letters:
            completed = False
            break

    if completed:
        print("\nCongratulations! You guessed the word:", word)
        break

if wrong_guesses == max_guesses:
    print("\nGame Over!")
    print("The word was:", word)