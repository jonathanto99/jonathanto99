import random

def display_hangman(tries):
    """Display hangman stages based on remaining tries."""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |     
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |     
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |     
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |     
           |     
           |     
           -
        """
    ]
    return stages[tries]

def play_hangman():
    """Main hangman game loop."""
    word_list = ["python", "hangman", "programming", "developer", "challenge", "computer", "algorithm"]
    word = random.choice(word_list).upper()
    word_length = len(word)
    guessed_letters = set()
    correct_letters = set()
    tries = 6
    
    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters.")
    
    while tries > 0:
        # Display current state
        display_word = "".join([letter if letter in correct_letters else "_" for letter in word])
        print(display_hangman(tries))
        print(f"Word: {display_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")
        print(f"Tries remaining: {tries}\n")
        
        # Check win condition
        if display_word == word:
            print(f"Congratulations! You won! The word was: {word}")
            return
        
        # Get player guess
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            correct_letters.add(guess)
            print("Good guess!\n")
        else:
            tries -= 1
            print("Wrong guess!\n")
    
    # Game over
    print(display_hangman(tries))
    print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()