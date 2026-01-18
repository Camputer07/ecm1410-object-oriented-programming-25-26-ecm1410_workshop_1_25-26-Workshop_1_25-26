import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    #x = random.randint(poss_values)
    return poss_values[len(poss_values) // 2]

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val and user_input == "h":
        return True
    elif next_val < current_val and user_input == "l":
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    # Keeps track of if the letter is in the word
    letter_present = False
    # Loop through each letter in the hangman word
    for i in range(len(word)):
        if letter == word[i]:
            # Update the board at this location with 'letter'
            board[i] = letter
            # Update the boolean tracker variable
            letter_present = True
    
    # Check if the letter is present
    if letter_present is True:
        # Output success message
        print(f"Well done! '{letter}' is in the word")
        return True
    else:
        # Output failed message
        print(f"Sorry, '{letter}' is not in the word")
        return False
