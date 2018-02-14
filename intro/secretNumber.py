import random

print('hello, what is your name')
name = input()

print('i am thinking about a number between 1 and 20')
secretNumber = random.randint(1,20)

for guessTaken in range(1,7):
    print('take a guess')
    guess= int(input())
    if guess < secretNumber:
        print('too low!')
    elif guess > secretNumber:
        print('too high')
    else:
        break ## bo to jest to czego szukamy

if guess == secretNumber:
    print('brawo, that is it')
else:
    print('nie tym razem. Moja liczba to '+ str(secretNumber))
