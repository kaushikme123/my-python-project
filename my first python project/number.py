import random

number = random.randrange(1,100)
guess = int (input("Guess the number"))

while guess != number:
    if guess < number:
        print ("You need to guess higher. Try again")
        guess = int (input("\n Guess a number between 1 and 100: "))
    else:
        print ("You need to guess lower. Try again") 
        guess = int (input("\n Guess a number between 1 and 100: ")) 
print("You guessed the number correctly!")                           
        