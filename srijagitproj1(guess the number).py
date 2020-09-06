import random
num=random.randrange(1,50)
guess=int(input("Guess a number between 1 and 50: "))
while guess!=num:
    if(guess<num):
        print("Guess higher")
        guess=int(input("Guess a number between "+ str(guess) +"and 50 :"))
    else:
        print("Guess Lower")
        guess=int(input("Guess a number between 1 and "+ str(guess) +":"))

print("You have guessed it right!!")
        
       
