import random
import string

WORDLIST_FILENAME = "words.txt"

# Loads text file and makes a list of words.
def load_words():
    print("Loading word list from file...")
    fhandle = open(WORDLIST_FILENAME, 'r')
    line = fhandle.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# Chooses random word from list of words.
def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

# Determines if word is guessed.
def is_word_guessed(secret_word, letters_guessed):
    win = True
    for letter in secret_word:
        if letter not in letters_guessed:
            win = False
    return win

# Returns word with underscores for unguessed letters.
def get_guessed_word(secret_word, letters_guessed):
    guessed_word = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            # Space for usability
            guessed_word.append('_ ')
    return ''.join(guessed_word)

# Returns unguessed letters.
def get_available_letters(letters_guessed):
    alphabet_list = list(string.ascii_lowercase)
    for letter in alphabet_list[:]:
        if letter in letters_guessed:
            alphabet_list.remove(letter)
    return ''.join(alphabet_list)  

# Matches secret word with all possible correct words in list.
def match_with_gaps(my_word, other_word):
    my_word_list = list(my_word)
    other_word_list = list(other_word)

    # Removes spaces after underscores from list
    for char in my_word_list[:]:
        if char == ' ':
            my_word_list.remove(char)
    
    match = True

    # Determines if length of secret word and possible words are the same
    if len(my_word_list) != len(other_word_list):
        match = False

    # Determines if characters in secret word and possible words are the same at each index
    else:
        for char_index in range(len(my_word_list)):
            if my_word_list[char_index] != '_':
                if my_word_list[char_index] != other_word_list[char_index]:
                    match = False
            else:
                if other_word_list[char_index] in my_word_list:
                    match = False
    return match
            
# Returns possible correct words
def show_possible_matches(my_word):
    matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matches.append(other_word)
    if len(matches) == 0:
        print('No matches found.')
    return ' '.join(matches)

def hangman_with_hints(secret_word):
    
    # Initial variables.
    current_guess = ...
    guesses_left = 6
    letters_guessed = []
    warnings = 3

    # Startup messages.
    print('Welcome to the Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warnings, 'warnings left.')
    print('-----------')
    
    # Game loop.
    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:
        
        # Messages to user.
        print('You have', guesses_left, 'guesses left.')
        print('Letters you have not guessed:', get_available_letters(letters_guessed))
        print('Enter ? for hint')
        current_guess = input('Please guess a letter:').lower()

        # User inputs '*' for hangman with hints.
        if current_guess == '?':
            print('Possible correct words are: ')
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            print('-----------')

        #User does not guess an ascii character.
        if current_guess not in string.ascii_letters and current_guess != '?':
            
            # User had warnings left.
            if warnings > 0:
                warnings -= 1
                print('Uh oh! That is not a valid letter. You have', warnings, 'warnings left.')
                print('-----------')
           
            # User does not have warnings left.
            else:
                guesses_left -= 1
                warnings = 0
                print('Uh oh! That is not a valid letter. You have no warnings left '
                      'so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
                print('-----------')
        
        # User guesses an already gussed character.
        elif current_guess in letters_guessed:
            
            # User had warnings left.
            if warnings > 0:
                warnings -= 1
                print('Uh oh! You already guessed that letter. You have', warnings, 'warnings left.')
                print('-----------')
            
            # User does not have warnings left.
            else:
                guesses_left -= 1
                warnings = 0
                print('Uh oh! You already guessed that letter. You have no warnings left '
                      'so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
                print('-----------')
        
        # Validate user guess.
        elif current_guess != '?':
            letters_guessed.append(current_guess)
            
            # The user guess is correct.
            if current_guess in secret_word:
                print('Great guess!: ', get_guessed_word(secret_word, letters_guessed))
                print('-----------')
            
            # The user guess is incorrect.
            else:
                print('Uh oh! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                guesses_left -= 1
                print('-----------')

    # Exit game loop.

    # The user ran out of guesses.
    if guesses_left == 0:
        print('Sorry, you ran out of guesses, the word was:', secret_word)
    
    #The user won.
    else:
        print('Congradulations, you won!')
        print('Your total score is:', guesses_left*len(set(secret_word)))

# sets secret word
if __name__ == "__main__":
    pass
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
