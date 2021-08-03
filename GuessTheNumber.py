import random
randomInt=random.randrange(1,10)
chancecount=0
print("\n\nGUESS A NUMBER BETWEEN 1 TO 9")
print("\nYOU HAVE 5 CHANCES")
while chancecount < 5:
    guess=int(input("ENTER YOU GUESS HERE : "))
    chancecount=chancecount+1
    if guess < randomInt:
        print("\nTOO LOW!!! GUESS A NUMBER HIGHER THAN ",guess)

    if guess > randomInt:
        print("\nTOO HIGH!!! GUESS A NUMBER LOWER THAN ", guess)   

    if guess == randomInt:
        print("\nYOU WIN!!!")
        break

    if not chancecount < 5:
        print("\nYOU LOSE!!! THE NUMBER IS", randomInt)    