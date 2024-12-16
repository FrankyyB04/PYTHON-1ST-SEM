
given = 0 
IsRepeat = True
print("Enter the number 0 if you are satisfied with the numbers you input")
while IsRepeat == True:
    num = eval(input("Enter a number: "))
    given += num

    if num == 0:
        print(f"The sum of all number given is: {given}")
        IsRepeat = False
        break

