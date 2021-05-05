import random
number=random.randrange(1,9)
print("NUMBER GUESSING GAME")
guess=int(input("Guess the number between 1 to 9"))
chances=0
while chances<5:
    chances=chances+1
    if guess<number:
        print("Too low, try again")
        guess=int(input("Guess the number between 1 to 9"))
    if guess>number:
        print("Two high, try again")
        guess=int(input("Guess the number between 1 to 9"))
    if guess==number:
        print("YOU WON!,Wow you must be a mind reader")
        break

if not chances<5:
    print("YOU LOSE. The number is",number)


