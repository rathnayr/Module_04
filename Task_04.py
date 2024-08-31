import random
Number = random.randint(1,10)
while True:
    try:
        User_Guess = int(input("Enter a number between 1 and 10: "))

        if User_Guess <1 or User_Guess >10:
            print("Enter a number between 1 and 10")
            continue
        if User_Guess < Number:
            print ("Your guess is Too Low")
        elif User_Guess > Number:
            print ("Your guess is Too High")
        else:
            print ("You guess is Correct")
            print("Thanks for playing")
            break
    except ValueError:
        print("Please enter a number between 1 and 10")



