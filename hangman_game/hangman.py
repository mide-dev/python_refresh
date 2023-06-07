# game where user guess the hidden word.
# looks like this __p_y => happy
# open words txt and use it as dictionary
# clean it up and store it
# give user number of words to guess and increase
# difficulty in ranges as user suceed
# user also has 6 life to guess words in each stage

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

no_of_hidden_letters = round(len(secret_word)/2)

secret_list = list(secret_word)
for i in range(no_of_hidden_letters):
    # hidden_letter = 
    
    print(random.choice(secret_list))
    



# choose a random word with specific length range
# delete the word from list
# randomly hide 50% of the selected word char
# if user guess right, reveal their guess



