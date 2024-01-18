import random
import requests

def choose_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word")
        word = response.json()[0]
        return word.lower()
    except requests.RequestException as e:
        print(f"Error fetching word from API: {e}")
        # Use a predefined word in case of API failure
        return random.choice(["python", "hangman", "developer", "programming", "challenge", "game"])

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6  # You can adjust the number of allowed attempts

    while attempts > 0:
        current_display = display_word(secret_word, guessed_letters)
        print("\nWord:", current_display)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")
        else:
            print("Good guess!")

        if set(guessed_letters) == set(secret_word):
            print("\nCongratulations! You've guessed the word:", secret_word)
            break

    if attempts == 0:
        print("\nSorry, you've run out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
