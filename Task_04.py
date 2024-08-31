import random
Number = random.randint(1,10)
while True:
    try:
        User_Guess = int(input("Enter a number between 1 and 10: "))
        if User_Guess < Number:
            print ("Your guess is too low")
        elif User_Guess > Number:
            print ("Your guess is too high")
        else:
            print ("You guess is correct")
            break
    except ValueError:
        print("Please enter a number between 1 and 10")



