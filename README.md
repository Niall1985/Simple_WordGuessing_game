Here's a README for the word guessing game script:

---

# Word Guessing Game

This is a simple word guessing game implemented in Python. The program selects a random word from a predefined list and allows the user to guess the word. The user has 5 attempts to guess the word, and after each attempt, the program provides feedback on the correctness of the guesses.

## How to Play

1. Run the script using Python:

   ```sh
   python word_guessing_game.py
   ```

2. You will be prompted to guess the word. Enter your guess and press enter.

3. After each guess, the program will provide feedback:
   - If the guessed letter is in the word and in the correct position, it will indicate that the letter is correct.
   - If the guessed letter is in the word but not in the correct position, it will indicate that the letter is in the word but in the wrong position.
   - If the guessed letter is not present in the word, it will indicate the letters that are not in the word.
   - If the guess is incorrect, the program will provide a message indicating the number of remaining attempts.

4. Continue guessing until you guess the word correctly or exhaust all your attempts.

5. After 5 attempts, the program will reveal the correct word.

## Customization

You can customize the list of words used in the game by modifying the `words` list in the script. Simply add or remove words as per your preference.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README further to suit your needs or add additional sections as necessary. Enjoy playing the word guessing game!
