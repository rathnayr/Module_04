Inches_to_Centimeters = 2.54
while True:
    Inches=float(input("Enter a value to convert:"))

    if Inches<0:
        print("You have entered a negative values. Program is ended")
        break
    Centimeters=Inches*Inches_to_Centimeters
    print(f"Entered {Inches} equal to {Centimeters}")

