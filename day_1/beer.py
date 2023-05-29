# python program to automatically name a beer brand by chosing from 2 words
# randomly from 3answers. the 3questions asked should be choosing randomly from 8 questions

import random

# create a function to ask the right question based on inputs
def ask(question):
    if question == 'date':
        result = input('Enter company launch date: ')
    elif question == 'color':
        result = input('Enter favorite color: ')
    elif question == 'pet':
        result = input('Enter favorite pet breed: ')
    elif question == 'planet':
        result = input('Enter a random planet name you like: ')
    elif question == 'city':
        result = input('Enter favorite city: ')
    elif question == 'movie':
        result = input('Enter best movie: ')
    elif question == 'sport_team':
        result = input('Enter favorite sport\'s team: ')
    elif question == 'mother':
        result = input('Enter mother\'s name: ')
    else:
        return
    
    return result  

    
# a list of questions
choose = ['date', 'color', 'pet', 'planet', 'city', 'movie', 'sport_team', 'mother']

# choose a random question
choose_rand = random.choice(choose)

# initalize the question array to accept 3 random questions
question = []

# populate the question array with 3 distinct questions
while len(question) < 4:
    choose_rand = random.choice(choose)
    if choose_rand not in question:
        question.append(choose_rand)
        
left = random.choice(question)
question.remove(left)

middle = random.choice(question)
question.remove(middle)

right = question[0]


answer1 = ask(left)
answer2 = ask(middle)
answer3 = ask(right)

brand_name = [answer1, answer2, answer3]

side_1 = random.choice(brand_name)
brand_name.remove(side_1)

side_2 = random.choice(brand_name)

print(f'Your beer brand name is:\n {side_1} {side_2}')


