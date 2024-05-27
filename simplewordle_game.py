import sys
import random

# List of words to choose from, you may add more words as per your wish
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
         "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla"]

# Select a random word and prepare it
key1 = random.choice(words).upper().strip()
key = list(key1)

print("You have 5 tries to guess the word")
print(f"The word has {len(key)} letters\n")

# Allow the user 5 attempts to guess the word
for attempt in range(5):
    guess = input("Enter your guess: ").upper().strip()
    guess_main = list(guess)

    if key == guess_main:
        print("Word guessed successfully!")
        sys.exit()

    elif len(key) != len(guess_main):
        print("Incorrect length. Please try again.")
        continue

    else:
        correct_positions = []
        wrong_positions = []
        
        for i in range(len(key)):
            if key[i] == guess_main[i]:
                correct_positions.append(i)
            elif guess_main[i] in key:
                wrong_positions.append(i)
        
        for i in correct_positions:
            print(f"The letter '{guess_main[i]}' at position {i+1} is correct.")
        
        for i in wrong_positions:
            if i not in correct_positions:  # Ensuring it is not already marked correct
                print(f"The letter '{guess_main[i]}' at position {i+1} is in the word but in the wrong position.")
        
        not_present = [letter for letter in guess_main if letter not in key]
        if not_present:
            print("The following letter/letters are not present in the word:", ", ".join(not_present))
        
        print("\n")

print(f"Sorry, your 5 tries are over. The correct word was {key1}.")
