import random
print('Number Guessing')
num=random.randint(1,9)
chances=0
print('Guess a number between 1 to 9: ')
while chances<5:
    guess=int(input('Enter your guess'))

    if guess==num:
        print('Contrats! You won')
        break
    elif guess<num:
        print('You guess was too low, guess a bigger number than',guess)
    else:
        print('Your guess was too high, guess a smaller number than',guess)
    chances=chances+1
if not chances<5:
    print('You Lose, the number was',num)









