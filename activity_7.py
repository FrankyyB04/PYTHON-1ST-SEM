name = input("Enter your name: ")
isEnrolled = input("Are you enrolled in DLL (yes/no): ")
if isEnrolled.lower() == "yes":
    print(f"Hi {name}, welcome to DLL scholarship application")
    
    age = int(input("Enter your age: "))
    if age >= 18 and age <= 35 :
        print("Your age is qualified with the age requirement")

        grade = eval(input("Enter your GWA here: "))
        if grade >= 85 and age <= 99:
            print("Your grade is qualified in DLL scholarship application")
            is4ps = input("Are you a 4ps beneficiary?(yes/no): ")
            if is4ps.lower() == "yes":
                print("You are now a scholar ng bayan, goodluck!!")
            else:
                print("You must be a 4ps beneficiary, apply now")
        else:
            print("--> Your Grade is not qualified in DLL scholarship, better luck next time <--")
    else:
        print("--> Your age is not valid in DLL sholarship <--")
elif isEnrolled.lower() == "no":
    print("I'm sorry, you must be enrolled to ")

else:
    print("Invalid input")
        