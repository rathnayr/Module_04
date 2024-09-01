Correct_Username = "python"
Correct_Password = "rules"

attempts=0
maximum_attempts=5

while attempts<maximum_attempts:
    Username=input("Enter your username: ")
    Password=input("Enter your password: ")
    if Username==Correct_Username and Password==Correct_Password:
        print("Welcome")
        break
    else:
        attempts+=1
        if attempts<maximum_attempts:
            print("Wrong username or password, Try again")
        continue
if attempts==maximum_attempts:
    print("Access Denied")
