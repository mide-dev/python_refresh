# python program to automatically name a beer brand by chosing from 2 words
# randomly from 3answers. the 3questions asked should be choosing randomly from 8 questions

import random

# create
def ask(question):
    if question == date:
        date = input('Enter company launch date: ')
        return date
    elif question == color:
        color = input('Enter favorite color: ')
        return color
    elif question == pet:
        pet = input('Enter favorite pet breed: ')
        return pet
    elif question == planet:
        planet = input('Enter a random planet name you like: ')
        return planet
    elif question == city:
        city = input('Enter favorite city: ')
        return city
    elif question == movie:
        movie = input('Enter best movie: ')
        return movie
    elif question == sport_team:
        sport_team = input('Enter favorite sport\'s team: ')
        return sport_team
    elif question == mother:
        mother = input('Enter mother\'s name: ')
        return mother
    else:
        return
       
    

choose = [date, color, pet, planet, city, movie, sport_team, mother]

choose_rand = random.choice(choose)

question = []

while len(question < 3):
    choose_rand
    if choose_rand not in question:
        question.append(choose_rand)
        
left = random.choice(question)
question.remove(left)
right = random.choice(question)



