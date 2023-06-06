# game where user guess the hidden word.
# looks like this __p_y => happy
# open words txt and use it as dictionary
# clean it up and store it
# give user number of words to guess and increase
# difficulty in ranges as user suceed
# user also has 6 life to guess words in each stage

# START
# import the raw words txt file
with open("C:/Users/Ayomide/Desktop/Development/Python/Python_refresh/hangman_game/words.txt", "r") as file:
    lines = file.read().split('\n')

words = set()
for line in lines:
    # remove words that contains special char or number
    if line.isalpha():
        # remove white space
        word = line.strip()
        
        #prevent empty lines
        if word:
            words.add(word)


print("WELCOME TO HANGMAN GAME😇")
print("Rules are as Follows\nYou'll be given a word with missing letters\nYour task is to guess the letters correctly")
print("*******************************")

