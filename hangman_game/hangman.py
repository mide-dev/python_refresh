# game where user guess the hidden word.
# looks like this __p_y => happy
# open words txt and use it as dictionary
# clean it up and store it
# give user number of words to guess and increase
# difficulty in ranges as user suceed
# user also has 6 life to guess words in each stage

# START
# import the raw words txt file
with open('words.txt', 'r') as file:
    contents = file.read()
