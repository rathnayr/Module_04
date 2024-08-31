Numbers_List = []

while True:
    number= input("Enter a number: ")
    if number == "":
        break
    try:
        number=float(number)
        Numbers_List.append(number)
    except ValueError:
        print("Incorrect Input, enter a number")
        continue
    if True:
        smallest = min(Numbers_List)
        largest = max(Numbers_List)

        print("The smallest number is", smallest)
        print("The largest number is", largest)
if not Numbers_List:
    print("No number was entered")