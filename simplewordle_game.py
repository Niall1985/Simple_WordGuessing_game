import sys
import random
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
             "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla"]
# add more words as per your wish

key1 = random.choice(words).upper().strip()
key = list(key1)
print("You have 5 tries to guess the word")
print(f"The word has {len(list(key1))} letters\n")

for i in range(0,5):
    guess = input("Enter you guess:").upper().strip()
    guess_main = list(guess)

    if key == guess_main:
        print("Word guessed successfuly")
        sys.exit()  

    elif len(key) != len(guess_main):
        print("Incorrect length")
        continue
   
    else:
        for i in range (len(key)):
            if key[i] != guess_main[i]:
                print(f"Oops! The letter at the {i+1} position is incorrect.")
        print("\n")
    
        continue
print(f"Sorry, your 5 tries are over, the correct word was {key1}")
    
    
    
