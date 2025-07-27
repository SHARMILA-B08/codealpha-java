import random

def hangman():
    words = ['apple', 'brain', 'crane', 'delta', 'eagle']
    word = random.choice(words)
    guessed = '_' * len(word)
    guessed = list(guessed)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman Game!")
    print("Guess the word. You have 6 incorrect attempts.")

    while attempts > 0 and ''.join(guessed) != word:
        print("\nWord: ", ' '.join(guessed))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Correct guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            print("Incorrect guess!")
            attempts -= 1

        guessed_letters.append(guess)

    if ''.join(guessed) == word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Out of attempts! The word was:", word)

hangman()
