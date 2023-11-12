# Swahili Version of the Hungman game

import random

swahili_words = ['Jambo' , 'Pamoja' , 'Tumaini']

word = random.choice(swahili_words).lower()

correct_guess = []
incorrect_guess = []
tries = 4
count = -1
while tries > 0:
    output = ''
    for letter in word:
        if letter in correct_guess:
            output += letter 
        else:
            output += '_ '
    if output == word:
        break
    print("Jaribu kunipa neno la jawabu: ", output)
    print("umebakisha majaribio ",tries)
    guess = input().lower()
    if guess in correct_guess or guess in incorrect_guess:
        print("Umeshatumia herufi hio" , guess)
    elif guess in word:
        print("Pongezi! Umepata herufi sahihi! ")
        correct_guess.append(guess)
    else:
        print("Pole, umeandika herufi ambayo haitakikani")
        count = count + 1
        tries = tries - 1
        incorrect_guess.append(guess)
if tries > 0:
    print("Umepata neno hilo, na umeshinda!")
else:
    print("Umefeli, Jaribu tena")


