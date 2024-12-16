import os
def code_challenge_1():
    os.system('cls')
    print("*********************************************************************************")
    print("*THIS IS THE FIRST CODE CHALLENGE WE HAVE DONE*")
    print("*THIS CODE CHALLENGE ONLY CONTAINS ESCAPE SEQUENCE AND PRINT FUCTION*")
    print("*********************************************************************************")
    print("\t\t\t\t Hello, World!")
    print("\n\t\t\t\t\t*\n\t\t\t\t*\t*\t*\n\t\t\t*\t*\t*\t*\t*\n\t\t*\t*\t*\t*\t*\t*\t*\n\t\t\t*\t*\t*\t*\t*\n\t\t\t\t*\t*\t*\n\t\t\t\t\t*\n")
    print("*********************************************************************************")
def code_challenge_2():
    os.system('cls')
    print("*********************************************************************************")
    print("*THIS CHALLENGE CONTAINS A CONCATENATION BETWEEN STR AND ESCAPE SEQUENCE \n\t TO FORM A  DIAMOND AND A STRING TO PUT THE NAME INSIDE THE DIAMOND*")
    print("*THIS TIME WE USED INPUT FUNCTION*")
    print("*TRY TO ENTER YOUR NAME*")
    print("*********************************************************************************")
    name = input("What's your name? ")
    print("\n\t\t\t\t\t*\n\t\t\t\t*\t*\t*\n\t\t\t*\t*\t*\t*\t*\n\t\t*\t*\t*" + "   Hi! " + name + "\t*\t*\t*\n\t\t\t*\t*\t*\t*\t*\n\t\t\t\t*\t*\t*\n\t\t\t\t\t*\n")
    print("*********************************************************************************")
def code_challenge_3():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("*THIS TIME WE USED CONCATINATION TO STR AND INT*")
    print("*BASIC OPERATIONS WAS USED IN THIS PROGRAM*")
    print("*TRY TO ENTER A NUMBER*")
    print("---------------------------------------------------------------------------------------------------------------")
    num1 = eval(input("Please enter a number: \n"))
    num2 = eval(input("Please enter another number: \n"))
    print("The sum of",num1,"and",num2,"is",num1+num2)
    print("The difference of",num1,"and",num2,"is",num1-num2)
    print("The product of",num1,"and",num2, "is",num1*num2)
    print("The quotient of",num1,"and",num2,"is",num1/num2)
    print(num1,"exponent by",num2,"is",num1**num2)
    print("The remainder of",num1,"and",num2,"is",num1%num2)
    print("The floor division of",num1,"and",num2,"is",num1//num2)
    print("---------------------------------------------------------------------------------------------------------------")
def code_challenge_4():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("IN THIS CODE CHALLENGE, WE MADE A DENOMINATION")
    print("THE DENOMINATION CONSISTS OF DECLARING A VALUE AND CHANGING THE VALUE")
    print("MODULUS AND FLOOR DIVISION ARE THE PRIMARY OPERATORS THAT ARE USED IN THIS PROGRAM*\n *TRY TO ENTER A NUMBER YOU WANT*")
    print("---------------------------------------------------------------------------------------------------------------")
    print("Hello, welcome to Denomination")
    cash = eval(input("Enter Amount here: "))
    th = cash//1000
    th_c = cash%1000
    fh = th_c//500
    fh_c = th_c%500
    two_h = fh_c//200
    two_h_c = fh_c%200
    one_h = two_h_c//100
    one_h_c = two_h_c%100
    fif = one_h_c//50
    fif_c = one_h_c%50
    twe = fif_c//20
    twe_c = fif_c%20
    ten = twe_c//10
    ten_c = twe_c%10
    five = ten_c//5
    five_c = ten_c%5
    one = five_c//1
    one_c = five_c%1
    print(th,"- 1000")
    print(fh,"- 500")
    print(two_h,"- 200")
    print(one_h,"- 100")
    print(fif,"- 50")
    print(twe,"- 20")
    print(ten,"- 10")
    print(five,"- 5")
    print(one,"- 1")
def code_challenge_5():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("*This program calculates the final grade of a student based on their grades in various components*")
    print("*This time, we used a eval function which is choosing between int and float*")
    print("*This is also the first time we used if-else statement which will display whether the student passed or failed*")
    print("---------------------------------------------------------------------------------------------------------------")
    num1 = eval(input("Enter your grade in prelim here: "))
    num2 = eval(input("Enter your grade in midterm here: "))
    num3 = eval(input("Enter your semi-final grade here: "))
    num4 = eval(input("Enter your grade in final here: "))
    num5 = eval(input("Enter your grade in Quiz here: "))
    num6 = eval(input("Enter your grade in project here: "))
    fg = (num1 * .15) + (num2 * .15) + (num3 * .15) + (num4 * .15) + (num5 * .25) + (num6 * .15)
    print("---------------------------------------------------------------------------------------------------------------")
    if fg >= 75 :
        print(f"Congratulations! You passed the course and your final grade is {fg}")
    else :
        print(f"Sorry, you failed and your final grade is {fg}")
    print("---------------------------------------------------------------------------------------------------------------")
def code_challenge_6():
    os.system('cls')
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age <= 8 and age >=1 :
        print(f"Hello {name}, you are considered as a toddler")
    elif age >= 9 and age  <= 14 :
        print(f"Hello {name}, you are considered as a pre-teen") 
    elif age >= 15 and age  <= 18 :
        print(f"Hello {name}, you are considered as a teenager") 
    elif age >= 19 and age  <= 27 :
        print(f"Hello {name}, you are considered as a early adulthood") 
    elif age >= 28 and age  <= 44 :
        print(f"Hello {name}, you are considered as a middle age") 
    elif age >= 45 and age  <= 59 :
        print(f"Hello {name}, you are considered as a past adulthood") 
    elif age >= 60  and age <= 120 :
        print(f"Hello {name}, you are considered as a senior") 
    else:
        print("Invalid age")
def code_challenge_7():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("*This code collects user data, calculates tax and discounts, and checks payment \nsufficiency, providing feedback based on the user's input*")
    print("---------------------------------------------------------------------------------------------------------------")
    name = input("Enter your fullname: ")
    grocery = input("Did you purchase grocery today? (yes/no): ")
    if grocery.lower() == "yes" :
        age = int(input(f"Enter your age: "))
        if age >= 1 and age <= 59:
            purchase = input("Enter the Item you will purchase: ")    
            itemp = eval(input("Enter the Item price: "))
            if itemp > 1 :
                tax = itemp * .123 + itemp
                if itemp >= 4000: 
                    print(f"Here is the taxed price of your item: {round(tax,2)}")
                    print("Since your item exceeds the value of (Php 4000.00), a discount of 3.8% will be applied to your item enjoyy!!")
                    discount4k = tax - (tax * .038)
                    print(f"Here is the discounted price of your taxed item: {round(discount4k,2)}php")
                    payment = eval(input("Please enter your payment here: ")) 
                    if payment > discount4k:
                        print(f"Thank you {name}, here is your change: {round(payment - discount4k,2)}php ")
                    elif payment < discount4k:
                        print("Insufficient Cash Please Restart the page") 
                elif itemp <= 3999 and itemp >= 1:
                    print(f"Here is the taxed price of your item: {round(tax,2)}")
                    payment = eval(input("Please enter your payment here: ")) 
                    if payment > tax :
                        print(f"Thank you {name}, here is your change: {round(payment - tax,2)}php")
                    elif payment < tax :
                        print("Insufficient Cash Please Restart the page")
                else : 
                    print("Invalid Item price")
            elif itemp <= 0 :
                print("Invalid Item Price")
        elif age >= 60 and age <= 150:
            purchase = input("Enter the Item you will purchase: ")    
            itemp = eval(input("Enter the Item price: "))
            if itemp > 1 :
                tax = itemp * .123 + itemp
                print(f"Here is the taxed price of your item: {round(tax,2)}php")
                print("According to your AGE, a discount of 12.8% will be applied to your taxed item, enjoyy!!")
                discountSC = tax - (tax * .123)  
                print(f"Here is the discounted price of your taxed item: {round(discountSC,2)}")
                payment = eval(input("Enter your payment here: "))
                if payment > discountSC :
                    print(f"Thank you {name}, here is your change: {round(payment - discountSC,2)}php")
                elif payment < discountSC :
                    print("Insufficient Cash Please restart the page")  
            elif itemp <= 0 :
                print("Invalid Item Price")    
        else :
            print("Invalid Age")
    else :
        print(f"Thank you {name} for using our system")
    print("---------------------------------------------------------------------------------------------------------------")
def code_challenge_8():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("*The code collects 10 numbers from the user and calculates:\nThe sum of all entered numbers.\nThe sum of the even numbers.")
    print("*The sum of the odd numbers. It then displays the results for all three sums.*")
    print("*This is also the first time we used a Loop function*")
    print("---------------------------------------------------------------------------------------------------------------")
    sum = 0 
    even = 0
    odd = 0 
    for x in range(1,11):
        num = eval(input(f"Enter any number{x}: "))
        sum += num
        if num % 2 == 0:
            even += num
        else:
            odd += num
    print(f"The sum of all numbers are: {sum}")
    print(f"The sum of all even numbers are: {even}")
    print(f"The sum of all odd numbers are: {odd}")
    print("---------------------------------------------------------------------------------------------------------------")
def code_challenge_9():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("*This code prints a right-aligned pattern of stars using for loop function")
    print('*The number of spaces decreases and the number of stars increases as the rows progress')
    print("*The outer loop controls the rows, while the inner loops manage the spaces and stars for each row.")
    print("---------------------------------------------------------------------------------------------------------------")
    for x in range(1,11):
        for y in range(1,x+1):
            print(" ",end=" ")
        for z in range(11,x,-1):
            print("*",end=" ")
        print()
def code_challenge_10():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This code generates a pattern of stars (*) in the shape of a diamond.")
    print("The pattern is divided into two parts: the upper part (a downward triangle) and the lower part (an upward triangle).")
    print("The first part creates decreasing rows of stars with spaces on the left")
    print("and the second part creates increasing rows of stars with spaces on the left. The overall shape looks like a diamond.")
    print("The first part prints the upper triangle, and the second part prints the lower triangle to complete the diamond shape.")
    print("---------------------------------------------------------------------------------------------------------------")
    for j in range(6,0,-1):
        for k in range(1,j+1):
            print(" ",end=" ")
        for l in range(6,j,-1):
            print("*",end=" ")
        for l in range(6,j,-1):
            print("*",end=" ")
        print()
    for x in range(1,6):
        for y in range(1,x+1):
            print(" ",end=" ")
        for z in range(6,x,-1):
            print("*",end=" ")
        for z in range(6,x,-1):
            print("*",end=" ")
        print("")
    print("---------------------------------------------------------------------------------------------------------------")
def code_challenge_11():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This time, Perfect diamon is made using incremental and decremental loop")
    print("---------------------------------------------------------------------------------------------------------------")
    for j in range(7,0,-1):
        for k in range(1,j+1):
            print(" ",end=" ")
        for l in range(6,j,-1):
            print("*",end=" ")
        for m in range(7,j,-1):
            print("*",end=" ")
        print()
    for x in range(1,6):
        for y in range(0,x+1):
            print(" ",end=" ")
        for z in range(5,x,-1):
            print("*",end=" ")
        for z in range(6,x,-1):
            print("*",end=" ")
        print()
    print("---------------------------------------------------------------------------------------------------------------")
def code_challenge_12():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("Using Incremental and decremental loop, we can make a arrow like using asterisk")
    print("---------------------------------------------------------------------------------------------------------------")
    for j in range(7,0,-1):
        for k in range(1,j+1):
            print(" ",end=" ")
        for l in range(6,j,-1):
            print("*",end=" ")
        for m in range(6,j,-1):
            print("*",end=" ")
        print()
    for x in range(1,6):
        for y in range(1,3):
            print("    ",end=" ")
        for z in range(1,3):
            print("*",end=" ")
        print()
    print("---------------------------------------------------------------------------------------------------------------")
def code_challenge_13(): 
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This program continuously asks the user to input numbers and keeps a running sum (given).")
    print("If the user enters 0, it exits the loop and displays the total sum of all entered numbers.")
    print("This program is a combination of assignment operator and while loop to sum all of the entered numbers")
    print("---------------------------------------------------------------------------------------------------------------")
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
    print("---------------------------------------------------------------------------------------------------------------")
def code_challenge_14():
    import os
    class BankSimulation:
        def __init__(self):
            self.cash = 0

        def create_account(self):
            first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            mid = input("Enter your middle initial: ")
            print(f"Account created successfully for {first} {mid} {last}!")
            print("Filipino denomination: 1000php, 500php, 200php, 100php, 50php, 20php, 10php, 5php, 1php")
            self.cash = float(input("Enter the amount you want to deposit: "))
            self.print_denomination()
        def print_denomination(self):
            th = self.cash // 1000
            th_c = self.cash % 1000
            fh = th_c // 500
            fh_c = th_c % 500
            two_h = fh_c // 200
            two_h_c = fh_c % 200
            one_h = two_h_c // 100
            one_h_c = two_h_c % 100
            fif = one_h_c // 50
            fif_c = one_h_c % 50
            twe = fif_c // 20
            twe_c = fif_c % 20
            ten = twe_c // 10
            ten_c = twe_c % 10
            five = ten_c // 5
            five_c = ten_c % 5
            one = five_c // 1
            one_c = five_c % 1
            print(f"{th} - 1000")
            print(f"{fh} - 500")
            print(f"{two_h} - 200")
            print(f"{one_h} - 100")
            print(f"{fif} - 50")
            print(f"{twe} - 20")
            print(f"{ten} - 10")
            print(f"{five} - 5")
            print(f"{one} - 1")
        def add_balance(self):
            addbalance = float(input("Enter the amount you want to deposit: "))
            self.cash += addbalance
        def withdraw(self):
            cash2 = float(input("Enter the amount you want to withdraw: "))
            if cash2 <= self.cash:
                self.cash -= cash2
                print("Thank you for using our system")
            else:
                print("Insufficient balance")
        def check_balance(self):
            print(f"Here's your remaining balance: {self.cash}")
        def menu(self):
            repeat = True
            while repeat:
                print("PLEASE SELECT FROM THE OPTIONS BELOW")
                print("1 -- Withdraw")
                print("2 -- Check Balance")
                print("3 -- Denomination Breakdown")
                print("4 -- Add balance")
                print("5 -- Exit")
                choice = input("Which program would you like to run (1,2,3,4,5) --> ")
                if choice == "1":
                    os.system("cls" if os.name == "nt" else "clear")
                    self.withdraw()
                elif choice == "2":
                    os.system("cls" if os.name == "nt" else "clear")
                    self.check_balance()
                elif choice == "3":
                    os.system("cls" if os.name == "nt" else "clear")
                    self.print_denomination()
                elif choice == "4":
                    os.system("cls" if os.name == "nt" else "clear")
                    self.add_balance()
                elif choice == "5":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Thank you for using my program")
                    repeat = False
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Invalid Choice")
    if __name__ == "__main__":
        print("---------------------------------------------------------------------------------------------------------------")
        print("This program is the last code challenge we did and I think it was the longest and hardest for now")
        print("This program contains all the basic functions that our professor taught to us")
        print("This includes the denomination, collection of information, if and else statements, operations, and while loop")
        print("---------------------------------------------------------------------------------------------------------------")
        bank = BankSimulation()
        acc = input("Do you want to create a new account (yes/no)? ")
        if acc.lower() == "yes":
            bank.create_account()
        else:
            print("Thank you for using the system")
        bank.menu()
def activity_1():  
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This is the first program we have done")
    print("It is used for checking if the syntax is working")
    print("---------------------------------------------------------------------------------------------------------------")
    print("Hello World!")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_2():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This code takes input from the user, performs basic string operations and arithmetic, and displays the results.")
    print("We used a len() function to know how many characters that the name contains")
    print("---------------------------------------------------------------------------------------------------------------")
    name = input("Please enter your name: ")
    age = input("Enter your age number: ")
    email = input("Enter your email: ")
    print("Hi! " + name + " welcome to coding!! :) \n" + "Your age is " + age + " right? \n" + "Your email address is: " + email)
    print("Your name consist of" , len(name) , "characters")
    num1 = eval(input("Please input a number: "))
    num2 = eval(input("Please input a number: "))
    print(num1 , "+" , num2 , "=" , num1 + num2) 
    print("---------------------------------------------------------------------------------------------------------------")
def activity_3():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("this is the first time we used string formatting") 
    print("this is a biodata program")
    print("we concatenated 3 inputs to form a singular print")
    print("---------------------------------------------------------------------------------------------------------------")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    print(f"Hi {name}, from {address} and {age} yrs  old")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_4():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("We made our own formula for convering a fahrenheit to celcius and celcius to fahrenheit")
    print("---------------------------------------------------------------------------------------------------------------")
    f = eval(input("Enter the Fahrenheit you want to convert: "))
    c = (f-32)* 5 / 9
    print(f"{f} degree fahrenheit converted to celsius is {round(c,2)}")
    cel = eval(input("Enter the Celcius: "))
    fah = (c*9/5) + 32
    print(f"{cel} degree celcius converted to fahrenheit is {round(fah)}")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_5():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("activity 5 only shows assignment operators which are +=, -=, *=, /=")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_6():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("activity 6 shows decision structures/conditional statements which contains if else statements")
    print("The password is 'pogiako123'")
    print("---------------------------------------------------------------------------------------------------------------")
    password = "pogiako123"
    mypassword = input("Enter password: ")
    if password == mypassword:
        print("Welcome to conditional statements")
    elif mypassword == "pogisila123":
        print("Granted ka parin!!") 
    elif mypassword == "edipogitayo":
        print("May access ka parin!")
    else:
        print("Akses denayd")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_7():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This activity consist of many if and else statements which will checks if a user")
    print("meets the criteria for a DLL scholarship by verifying their enrollment status, age, grade, and 4Ps beneficiary status")
    print("---------------------------------------------------------------------------------------------------------------")
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
    print("---------------------------------------------------------------------------------------------------------------")
def activity_8():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This activity contains a loop that will start at 1 and ends to 11")
    print("The ouput will be the sum of all the numbers, sum of all even numbers, and sum of all the odd numbers")
    print("---------------------------------------------------------------------------------------------------------------")
    sum = 0
    odd = 0 
    even = 0
    for x in range(1,11):
        num = eval(input(f"Input# {x}: "))
        sum += num 
        if num % 2 == 0:
            even += num
        else:
            odd += num
    print(f"The sum of all numbers are: {sum}")
    print(f"The sum of all even numbers are: {even}")
    print(f"The sum of all odd numbers are: {odd}")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_9():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This activity will compute the factorial of the number you will enter")
    print("---------------------------------------------------------------------------------------------------------------")
    num = eval(input("Enter any number: "))
    factorial = 1 
    for x in range(num,0,-1):
        factorial *= x
    print(f"The factorial of {num} is {factorial}")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_10():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This activity will show a list of a number and asterisk using for loop function")
    print("---------------------------------------------------------------------------------------------------------------")
    for x in range(1,11):
        print(x,end=" ")
        for y in range(1,11):
            print("*",end=" ")
        print()
    print("---------------------------------------------------------------------------------------------------------------")
def activity_11():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("*This code prints a right-aligned pattern of stars using for loop function")
    print('*The number of spaces decreases and the number of stars increases as the rows progress')
    print("*The outer loop controls the rows, while the inner loops manage the spaces and stars for each row.")
    print("---------------------------------------------------------------------------------------------------------------")
    for x in range(1,11):
        for y in range(1,x+1):
            print(" ",end=" ")
        for z in range(11,x,-1):
            print("*",end=" ")
        print()
    print("---------------------------------------------------------------------------------------------------------------")
def activity_12():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This time, Perfect diamon is made using incremental and decremental loop")
    print("---------------------------------------------------------------------------------------------------------------")
    for x in range(7,0,-1):
        for y in range(1,x+1):
            print(" ",end=" ")
        for z in range(6,x,-1):
            print("*",end=" ")
        for q in range(7,x,-1):
            print("*",end=" ")
        print()
    for a in range(1,6):
        for b in range(0,a + 1):
            print(" ",end=" ")
        for c in range(5,a,-1): 
            print("*",end=" ")
        for d in range(6,a,-1):
            print("*",end=" ")
        print()
def activity_13():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This program will show the multiplication table of what number you are going input")
    print("---------------------------------------------------------------------------------------------------------------")
    no = int(input("Enter a number of column: "))
    for x in range (1,no):
        for y in range(1, no+1):
            print(f" |{x}x{y} = {x*y}|", end="")
    print()
    print("---------------------------------------------------------------------------------------------------------------")
def activity_14():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This activity contains a combination of while loop, for loop, and if and else statement to create a multiple triangles")
    print("and asking the user if they want to add more triangles")
    print("---------------------------------------------------------------------------------------------------------------")
    repeat = True
    nt = 0
    while repeat == True:
        var = input("Do you wish to add more triangles? (yes/no): ")
        if var.lower() == "no":
                os.system('cls')
                print("LOOP HAS BEEN STOPPED")
                repeat = False
                break
        elif var.lower() == "yes":
            os.system('cls')
            nt += 1
            for x in range(1,7):
                for z in range(1,nt+1):
                    for y in range(1, x+1):
                            print("*", end=" ")
                    for a in range(7, x, -1):
                            print(" ",end=" ")
                    print(end=" ")
                print()
            continue
        else:
            print("Invalid Input")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_15():
    print("---------------------------------------------------------------------------------------------------------------")
    print("This activity is about trigger switch which we will use if statement to break the while loop")
    print("---------------------------------------------------------------------------------------------------------------")
    isRepeat = True
    while isRepeat == True:
        name = input("Enter a name:  ")
        print(f"Hi {name}")
        #stopping point
        if name.lower() == "stop":
            print("Loop Terminated")
            break
    print("---------------------------------------------------------------------------------------------------------------")
def activity_16():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This activity contains infinite loop that will only stop when you enter (0)")
    print("The sum of all the number you input will be the result when you enter the (0)")
    print("---------------------------------------------------------------------------------------------------------------")
    tuloy = True
    sum = 0
    while tuloy == True:
        num = eval(input("Enter any number --->  "))
        if num == 0:
            print("LOOP STOPPED")
            print(f"The sum of all the numbers given is {sum}")
            break
        else:
            sum += num 
            continue
    print("---------------------------------------------------------------------------------------------------------------")
def activity_17():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("This program contains a define function which the programmer creates their own reusable function")
    print("This activity contains the combination of while loop, for loop, and factorial")
    print("The user can choose what they want to use")
    print("---------------------------------------------------------------------------------------------------------------")
    def greet_Someone():
        print("Hi , hoped your having a delightful Tuesday afternoon.")
    def greet_Person(name):
        print(f"Hi {name}, hoped your having a delightful Tuesday afternoon.")
    def right_Triangle():
        for x in range(1, 6):
            for y in range(1, x+1):
                print("*", end=" ")
            for z in range(6, x, -1):
                print(" ",end= " ")
            print()
    def get_info(name, age):
        print(f"Hi {name}, with age {age} yrs old.")
    def factorial(number):
        #factorial of 4 - 4 x 3 x 2 x 1 
        fact = 1 
        for x in range(number, 0, -1):
            fact *= x
        print(f"The factorial of {number} is {fact}")
    tuloy = True
    while tuloy:
        print("-------------------------------")
        print("WELCOME TO MY COMPILATION PROGRAM")
        print("PLEASE SELECT FROM THE OPTIONS BELOW")
        print("1 -- RIGHT TRIANGLE")
        print("2 -- FACTORIAL")
        print("3 -- GREET SOMEONE")
        print("4 -- EXIT")
        choice = eval(input("Which program would you like to run (1,2,3,4) -- > "))
        if choice == 1:
            print("THIS IS A PROGRAM THAT WILL SHOW YOU A RIGHT TRIANGLE MADE FROM PYTHON")
            right_Triangle()
            continue
        elif choice == 2:
            print("THIS IS A PROGRAM THAT CALCULATES FACTORIAL")
            number = eval(input("enter a number "))
            factorial(number)
            continue
        elif choice == 3:
            greet_Someone()
            continue
        elif choice == 4:
            print("Program Terminated")
            break
        else:
            print("INVALID CHOICE")
            continue
    print("---------------------------------------------------------------------------------------------------------------")
def activity_18():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("THIS FUNCTION IS FOR CALCULATING FACTORIAL, JUST PUT THE NUMBER INSIDE THE PARENTHESIS")
    print("This only shows how the return function works in the define function")
    print("Thank you")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_19():
    os.system('cls')
    print("---------------------------------------------------------------------------------------------------------------")
    print("activity 19 is all about importing a function from different file, thank you")
    print("---------------------------------------------------------------------------------------------------------------")
def activity_20():
    os.system
    print("---------------------------------------------------------------------------------------------------------------")
    print("This Final activity is all about lists")
    print("You can add or remove from the list")
    print("---------------------------------------------------------------------------------------------------------------")
    fruits = []
    loop = True
    while loop:
        ad_fruits = input("Enter a fruit you want to add (type 'none' if you are satisfied, type 'remove' if you want to delete an item): ").lower()  
        if ad_fruits == "none":
            os.system('cls')
            print(f"Your final fruits are: {fruits}")
            break
        elif ad_fruits == "remove":
            rmv = input("Enter the fruit you want to remove: ")
            if rmv in fruits:
                os.system('cls')
                fruits.remove(rmv)
                print(f"'{rmv}' has been removed. Your updated list of fruits: {fruits}")
            else:
                os.system('cls')
                print(f"'{rmv}' is not in the list. Your current list of fruits: {fruits}")
        else:
            os.system('cls')
            fruits.append(ad_fruits)
            print(f"Your fruits are: {fruits}")
loop = True
while loop == True:
    print("\t\t------WELCOME TO FRANCO BERIÑA'S FINAL PROJECT------")
    print("THESE ARE THE COMPILATIONS OF OUR ACTIVIES AND CODE CHALLANGES WHICH YOU CAN LOOK AT AND USE")       
    print("1. Code Challenge")
    print("2. Activity")
    print("3. Exit")
    choice = int(input('Enter the number you want to open: '))
    if choice == 1:
        os.system('cls')
        print(" 1. Code Challenge 1")
        print(" 2. Code Challenge 2")
        print(" 3. Code Challenge 3")
        print(" 4. Code Challenge 4")
        print(" 5. Code Challenge 5")
        print(" 6. Code Challenge 6")
        print(" 7. Code Challenge 7")
        print(" 8. Code Challenge 8")
        print(" 9. Code Challenge 9")
        print("10. Code Challenge 10")
        print("11. Code Challenge 11")
        print("12. Code Challenge 12")
        print("13. Code Challenge 13")
        print("14. Code Challenge 14")
        cc_choice = int(input("Enter the number of Code Challenge you want to open: "))
        if cc_choice == 1:
            code_challenge_1()
        elif cc_choice == 2:
            code_challenge_2()
        elif cc_choice == 3:
            code_challenge_3()
        elif cc_choice == 4:
            code_challenge_4()
        elif cc_choice == 5:
            code_challenge_5()
        elif cc_choice == 6:
            code_challenge_6()
        elif cc_choice == 7:
            code_challenge_7()
        elif cc_choice == 8:
            code_challenge_8()
        elif cc_choice == 9:
            code_challenge_9()
        elif cc_choice == 10:
            code_challenge_10()
        elif cc_choice == 11:
            code_challenge_11()
        elif cc_choice == 12:
            code_challenge_12()
        elif cc_choice == 13:
            code_challenge_13()
        elif cc_choice == 14:
            code_challenge_14()
        else:
            print("\t\t------ INVALID INPUT ------")
            break

    elif choice == 2:
        os.system('cls')
        print(" 1. Activity 1")
        print(" 2. Activity 2")
        print(" 3. Activity 3")
        print(" 4. Activity 4")
        print(" 5. Activity 5")
        print(" 6. Activity 6")
        print(" 7. Activity 7")
        print(" 8. Activity 8")
        print(" 9. Activity 9")
        print("10. Activity 10")
        print("11. Activity 11")
        print("12. Activity 12")
        print("13. Activity 13")
        print("14. Activity 14")
        print("15. Activity 15")
        print("16. Activity 16")
        print("17. Activity 17")
        print("18. Activity 18")
        print("19. Activity 19")
        print("20. Activity 20")
        act_choice = int(input("Enter the number of Activity you want to open: "))
        if act_choice == 1:
            activity_1()
        elif act_choice == 2:
            activity_2()
        elif act_choice == 3:
            activity_3()
        elif act_choice == 4:
            activity_4()
        elif act_choice == 5:
            activity_5()
        elif act_choice == 6:
            activity_6()
        elif act_choice == 7:
            activity_7()
        elif act_choice == 8:
            activity_8()
        elif act_choice == 9:
            activity_9()
        elif act_choice == 10:
            activity_10()
        elif act_choice == 11:
            activity_11()
        elif act_choice == 12:
            activity_12()
        elif act_choice == 13:
            activity_13()
        elif act_choice == 14:
            activity_14()
        elif act_choice == 15:
            activity_15()
        elif act_choice == 16:
            activity_16()
        elif act_choice == 17:
            activity_17()
        elif act_choice == 18:
            activity_18()
        elif act_choice == 19:
            activity_19()
        elif act_choice == 20:
            activity_20()
        else:
            print("\t\t------ INVALID INPUT ------")
            break
    else:
        print("\t\t------ INVALID INPUT ------")
        continue