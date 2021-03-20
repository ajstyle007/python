n = 30
chance = 0
print("you have 7 chance to guess the number.")

while chance < 7 :

    guess = int(input("enter a number: "))
    chance = chance + 1

    if guess > 30 :
        print("number is less than your number.")
        print("you have", 7 - chance, "chance left.")
    elif guess < 30 :
        print("number is greater than your number.")
        print("you have", 7 - chance, "chance left.")
    elif guess == 30:
        print("correct ! yeahh this is the number. ")
        print("you take ",chance,"chance to guess the correct number.")
        break
if chance >= 7:
    print("game over")
    print("That number is 30.")
