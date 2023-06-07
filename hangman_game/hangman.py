# START
import random

# import the raw words txt file
with open("C:/Users/Ayomide/Desktop/Development/Python/Python_refresh/hangman_game/words.txt", "r") as file:
    lines = file.read().split('\n')

# store the words in a set
words_list = set()
for line in lines:
    # remove words that contains special char or number
    if line.isalpha() and len(line) > 2 and len(line) <= 12:
        # remove white space
        word = line.strip()
        
        #prevent empty lines
        if word:
            words_list.add(word)


def hangman():
    # Set default variables
    user_life = 6
    high_score = 0

    # Game welcome screen
    print("WELCOME TO HANGMAN GAME😇")
    print("Rules are as Follows.\nYou'll be given a word with missing letters.\nYour task is to guess the letters correctly\nin 6 tries or you loose")
    print("*******************************")
    print("\n")



def generate_secret_word(word_difficulty = range(3,5)):
    # function to select random word with specified length
    secret_word = next(word for word in words_list if len(word) in word_difficulty)

    # remove secret word from words_list 
    # to prevent generating same word in future
    words_list.discard(secret_word)
    
    return secret_word

secret_word = 'Good'




# a dict that holds every letter in secret word
# and count their number of occurence
secret_dict = {}
for char in secret_word:
    if char in secret_dict:
        secret_dict[char] += 1
    else:
        secret_dict[char] = 1


def hide_word_parts(secret_word):
    # convert secret word into a list to randomly
    # select parts to hide
    secret_list = list(secret_word)

    # determine how many letters to hide
    no_of_hidden_letters = round(len(secret_word)/2)

    # randomly select and hide the letters
    prev_index = None
    for i in range(no_of_hidden_letters):
        hidden_index = random.randrange(len(secret_list))
        
        # to prevent the code from choosing same index twice
        if hidden_index == prev_index:
            hidden_index = random.randrange(len(secret_list))
        else:
            prev_index = hidden_index
        
        secret_list[hidden_index] = "_"
    
    return secret_list




print(secret_list)
    



# choose a random word with specific length range
# delete the word from list
# randomly hide 50% of the selected word char
# if user guess right, reveal their guess



