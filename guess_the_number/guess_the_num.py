# GUESS THE NUMBER GAME

# GAME STARTS
import keyboard
import random

# SAYS "WELCOME TO THE NUMBER GAME - 
# PLEASE ENTER YOUR NAME TO CONTINUE"
print("\n")
print("WELCOME TO THE NUMBER GAME🔢")
print("**************************")
print("\n")
player_name = input("PLEASE ENTER YOUR NAME TO CONTINUE: ")

# Hi Player, To WIN, you need to guess the secret number
print(f"Hi {player_name}, To WIN, you need to guess the \nsecret number between 1-20 correctly. \nYou have 8 tries.")

# Enter any key to Start
print("\n Press ENTER key to Continue")
# wait until player press enter
keyboard.wait('enter')

def verify_input():
    player_input = input("Enter Your Guess 🤐\n")
    
    while not player_input.isdigit():
        player_input = input("Enter Your Guess 🤐\n")
    return int(player_input)
    


# Secret number set
secret_number = random.randint(1,21)
print("\n Secret Number is picked")

# keep track of the no of times player guessed, burst at 8- "You Loose"
guess = 0

while guess < 8:
    # Player inputs their guess
    
    guess += 1
    number = verify_input()
    
    if number == secret_number:
        print('BULLS EYE🎯- YOU WIN!!!')
        print(f'Secret Number is {secret_number}')
        print(f'You guessed in {guess} tries')
        break
    
    if number < secret_number:
        print("Tow Low ⬇️")
        
    if number > secret_number:
        print("Tow High ⬆️")

if guess == 8:
    print("You Loose")

print("**************************")
print('\n')
    
    
