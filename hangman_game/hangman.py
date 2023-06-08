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


# *******************************************************

# generate next word for player to guess
def generate_secret_word(player_level):
    word_difficulty = range(3,5)
    
    # word difficulty
    if player_level > 6 and player_level < 12:
        word_difficulty = range(3, 6)
        
    if player_level > 12 and player_level < 25:
        word_difficulty = range(3, 8)
    
    if player_level > 25 and player_level < 40:
        word_difficulty = range(4, 9)
        
    if player_level > 40 and player_level < 70:
        word_difficulty = range(4, 10)
        
    if player_level > 70:
        word_difficulty = range(5, 12)
    
    
    # function to select random word with specified length
    secret_word = next(word for word in words_list if len(word) in word_difficulty)

    # remove secret word from words_list 
    # to prevent generating same word in future
    words_list.discard(secret_word)
    
    return secret_word
          
    
# function to hide parts of the word
def hide_word_parts(secret_list):

    if len(secret_list) == 3:
        no_of_hidden_letters = 1
    else: 
        no_of_hidden_letters = round(len(secret_list)/2)

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
    return " ".join(secret_list)


# display word to the player
def display_next_word(word):
    print(f"Guess the following word: \n{word}")


# determine if guess is right or wrong
def player_guess(secret_word, secret_list, secret_dict, player_input):
    
    
    for char in secret_word:
        if char in secret_dict:
            secret_dict[char] += 1
        else:
            secret_dict[char] = 1
 
    # if letter already printed on screen, remove the 
    # from guess dictionary
    for letter in secret_list:
        if letter in secret_dict:
            secret_dict[letter] -= 1
      
    # verify player guess
    try:
        if secret_dict[player_input] == 0 : return False
        
        if secret_dict[player_input] > 0:
            for index, letter in enumerate(secret_list):
                if letter == '_' and player_input == secret_word[index]:
                    secret_list[index] = player_input
                    secret_dict[player_input] -= 1
                    return secret_list           
    except KeyError:
        return False

 

# collect player input
def player_input():
    player_input = '-1'
    while not player_input.isalpha():
        player_input = input("Enter Your Next Guess: ").lower()
    return player_input



# main game
def hangman():
    # Set default variables
    user_life = 6
    player_level = 1

    # Game welcome screen
    print("*******************************")
    print("WELCOME TO HANGMAN GAME😇")
    print("Rules are as Follows.\nYou'll be given a word with missing letters.\nYour task is to guess the letters correctly\nin 6 tries or you loose")
    print("*******************************")
    print("\n")
    print(f"Level {player_level}")
    
    # generate the next word
    secret_word = generate_secret_word(player_level).lower()
    
    # convert secret word into a list
    secret_list = list(secret_word)
    
    # a dict that holds every letter in generated 
    # secret word plus their number of occurence
    secret_dict = {}
    
    # hide some parts and store it
    displayed_word = hide_word_parts(secret_list)
    
    # display generated word with hidden parts
    display_next_word(displayed_word)
    
    player_inp = player_input()
    player_input_verify = player_guess(secret_word, secret_list ,secret_dict, player_inp)
    
    game_on = True
    
    while game_on:   
        if player_input_verify:
            if '_' not in player_input_verify:
                print("You Guessed the Word Correctly ✅✅✅🎉")
                print(f'{secret_word} 🎯')
                print("*********************************")
                player_level += 1
                user_life = 6
                print(f"Level {player_level} 😇")
                # generate new word for next level
                secret_word = generate_secret_word(player_level).lower()
                # convert secret word into a list
                secret_list = list(secret_word)
                # empty secret dict
                secret_dict = {}
                # hide some parts and store it
                displayed_word = hide_word_parts(secret_list)
                # display generated word with hidden parts
                display_next_word(displayed_word)
                # collect player input
                player_inp = player_input()
                # verify if input is correct
                player_input_verify = player_guess(secret_word, secret_list ,secret_dict, player_inp)  
            else:
                print(f"{''.join(player_input_verify)} ✅")
                player_inp = player_input()
                player_input_verify = player_guess(secret_word, secret_list ,secret_dict, player_inp)
                
        else:   
            user_life -= 1
            if user_life == 0:
                print("------------")
                print("You Loose ☹️")
                print(f'The word is: {secret_word}')
                game_on = False
            else:
                print("---------------")
                print("Wrong Guess ❌")
                print(f'Remaining Tries: {user_life}')
                player_inp = player_input()
                player_input_verify = player_guess(secret_word, secret_list ,secret_dict, player_inp)  
    

hangman()



