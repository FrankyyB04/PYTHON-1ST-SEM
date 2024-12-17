import os
def print_statements():
    os.system('cls')
    def printing():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> PRINTING <---")
        print("---> print() is commonly used to show the result of a program, debug code, or interact with the user <---")
        print("---------------------------------------------------------------------------------------------------------------")   
    def concatenation():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> CONCATENATION <---")
        print("---> Concatenating means joining two or more strings together <---")
        print("Here is the example:")
        print('print(" 5 + "SMILE" ") this will not work however')
        print('We will use print(5 , ""SMILE"") this will now work, we have to use comma rather than a addition sign.')
        print("The output of that will be: 5 SMILE")
        print("---------------------------------------------------------------------------------------------------------------")
    def string_formatting():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> STRING FORMATTING <---")
        print("String Formatting is the easiest and most readable method.")
        print('String Formatting is the use of "f" before the string and put variables in curly braces "{}" ')
        print("Here is an Example:")
        print("age = 20")
        print('print(f"Hello user! you are {age} yrs old")')
        print("The output will be: Hello user!, you are 20 yrs old")
        print("---------------------------------------------------------------------------------------------------------------")
    loop = True
    while loop == True:
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> PRINT STATEMENTS <---')
        print("1. PRINTING ")
        print("2. CONCATENATING ")
        print("3. STRING FORMATTING")
        print("4. EXIT")
        print("---------------------------------------------------------------------------------------------------------------")
        choice_1 = int(input("Enter a number you want to open: "))
        if choice_1 == 1:
            printing()
        elif choice_1 == 2:
            concatenation()
        elif choice_1 == 3:
            string_formatting()
        elif choice_1 == 4:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> THANK YOU FOR USING PRINT STATEMENTS <---")
            print("---------------------------------------------------------------------------------------------------------------")
            break
        else:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> INVALID INPUT <---")
            print("---------------------------------------------------------------------------------------------------------------")
            continue
def variables():
    os.system('cls')
    def number():
        os.system("cls")
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> NUMBER <---")
        print("You can store a value of number by doing this: age = 20")
        print('Now if you print "age"')
        print("print(age)")
        print("The output will be --> 20")
        print("---------------------------------------------------------------------------------------------------------------")
    def text():
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> TEXT <---")
        print('You can store a value of text by doing this: greet = "Happy birthday!"')
        print('Now if you print "greet"')
        print("print(greet)")
        print("The output will be --> Happy birthday!")
        print("---------------------------------------------------------------------------------------------------------------")
    def list():
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> LIST <---')
        print('You can store a value of list by doing this: shoes = ["nike", "addidas", "pumas"]')
        print('Now if you print "shoes"')
        print("print(shoes)")
        print("The output will be --> ['nike', 'addidas', 'puma']")
        print("---------------------------------------------------------------------------------------------------------------")  
    def calculation():
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> CALCULATION <---')
        print('You can store a value of list by doing this: length = 6 , width = 6')
        print('You can use the value of them by doing this for example:')
        print('print(length + width)')
        print("The output will be --> 12")
        print("You can also use different operations for that")
        print("---------------------------------------------------------------------------------------------------------------")
    loop = True
    while loop == True:
        print("---------------------------------------------------------------------------------------------------------------")
        print("\t\t---> VARIABLES <---")
        print("---> A variable is like a container that stores data <---")
        print("You give the container a name, and you can use it to hold different types of information")
        print("Such as: numbers, test, list, and calculation")
        print("---------------------------------------------------------------------------------------------------------------")
        print("1. NUMBER")
        print("2. TEXT")
        print("3. LIST")
        print("4. CALCULATION")
        print("5. EXIT")
        print("---------------------------------------------------------------------------------------------------------------")
        choice_v = int(input('Enter the number you want to open: '))
        if choice_v == 1:
            number()
        elif choice_v == 2:
            text()
        elif choice_v == 3:
            list()
        elif choice_v == 4:
            calculation()
        elif choice_v == 5:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> THANK YOU FOR USING VARIABLES <---")
            print("---------------------------------------------------------------------------------------------------------------")
            break
        else:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> INVALID INPUT <---")
            print("---------------------------------------------------------------------------------------------------------------")
            continue
def operators():
    os.system('cls')
    def arithmetic():
        os.system('cls')
        def add():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> ADDITION <---")
            print('Addition in Python is done using the "+" operator.')
            print("For example:")
            print("We will use variables to declare the value of a number")
            print("We will use eval() and input() fuctions for the user to add the numbers they want to input")
            num_1 = eval(input("Enter the first number you want to add: "))
            num_2 = eval(input("Enter the second number you want to add: "))
            print(f"The output will be: {num_1} '+' {num_2} = {num_1 + num_2}")
            print(f"In short we can get only the sum if we did this: print(num_1 + num_2)")
            print(f"The output will be only: {num_1 + num_2}")
            print("---------------------------------------------------------------------------------------------------------------")
        def sub():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> SUBTRACTION <---")
            print('Subtraction in Python is done using the "-" operator.')
            print("For example:")
            print("We will use variables to declare the value of a number")
            print("We will use eval() and input() fuctions for the user to add the numbers they want to input")
            num_1 = eval(input("Enter the first number you want to subtract: "))
            num_2 = eval(input("Enter the second number you want to subtract: "))
            print(f"The output will be: {num_1} '-' {num_2} = {num_1 - num_2}")
            print(f"In short we can get only the difference if we did this: print(num_1 - num_2)")
            print(f"The output will be only: {num_1 - num_2}")
            print("---------------------------------------------------------------------------------------------------------------")
        def mul():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> MULTIPLICATION <---")
            print('Multiplication in Python is done using the "*" operator.')
            print("For example:")
            print("We will use variables to declare the value of a number")
            print("We will use eval() and input() fuctions for the user to add the numbers they want to input")
            num_1 = eval(input("Enter the first number you want to multiply: "))
            num_2 = eval(input("Enter the second number you want to multiply: "))
            print(f"The output will be: {num_1} '*' {num_2} = {num_1 * num_2}")
            print(f"In short we can get only the product if we did this: print(num_1 * num_2)")
            print(f"The output will be only: {num_1 * num_2}")
            print("---------------------------------------------------------------------------------------------------------------")
        def div():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> DIVITION <---")
            print('Division in Python is done using the "/" operator.')
            print("For example:")
            print("We will use variables to declare the value of a number")
            print("We will use eval() and input() fuctions for the user to add the numbers they want to input")
            num_1 = eval(input("Enter the first number you want to divide: "))
            num_2 = eval(input("Enter the second number you want to divide: "))
            print(f"The output will be: {num_1} '/' {num_2} = {num_1 / num_2}")
            print(f"In short we can get only the quotient if we did this: print(num_1 / num_2)")
            print(f"The output will be only: {num_1 / num_2}")
            print("---------------------------------------------------------------------------------------------------------------")
        def floor():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> FLOOR DIVITION <---")
            print('Floor Division in Python is done using the "//" operator.')
            print("For example:")
            print("We will use variables to declare the value of a number")
            print("We will use eval() and input() fuctions for the user to add the numbers they want to input")
            num_1 = eval(input("Enter the first number you want to compute: "))
            num_2 = eval(input("Enter the second number you want to compute: "))
            print(f"The output will be: {num_1} '//' {num_2} = {num_1 // num_2}")
            print(f"In short we can get only the result if we did this: print(num_1 // num_2)")
            print(f"The output will be only: {num_1 // num_2}")
            print("---------------------------------------------------------------------------------------------------------------")
        def modu():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> MODULUS <---")
            print('Modulus in Python is done using the "%" operator.')
            print("For example:")
            print("We will use variables to declare the value of a number")
            print("We will use eval() and input() fuctions for the user to add the numbers they want to input")
            num_1 = eval(input("Enter the first number you want to compute: "))
            num_2 = eval(input("Enter the second number you want to compute: "))
            print(f"The output will be: {num_1} '%' {num_2} = {num_1 % num_2}")
            print(f"In short we can get only the remainder if we did this: print(num_1 % num_2)")
            print(f"The output will be only: {num_1 % num_2}")
            print("---------------------------------------------------------------------------------------------------------------")
        def expo():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> EXPONENTIATION <---")
            print('Exponentiation in Python is done using the "**" operator.')
            print("For example:")
            print("We will use variables to declare the value of a number")
            print("We will use eval() and input() fuctions for the user to add the numbers they want to input")
            num_1 = eval(input("Enter the first number you want to compute: "))
            num_2 = eval(input("Enter the second number you want to compute: "))
            print(f"The output will be: {num_1} '**' {num_2} = {num_1 ** num_2}")
            print(f"In short we can get only the yth power of x if we did this print(num_1 ** num_2)")
            print(f"The output will be only: {num_1 ** num_2}")
            print("---------------------------------------------------------------------------------------------------------------")     
        loop = True
        while loop == True:
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> ARITHMETIC OPERATORS <---")
            print("---------------------------------------------------------------------------------------------------------------")
            print("1. ADDITION")
            print("2. SUBTRACTION")
            print("3. MULTIPLICATION")
            print('4. DIVISION')
            print('5. FLOOR DIVISION')
            print('6. MODULUS')
            print('7. EXPONENTIATION')
            print('8. EXIT')
            print("---------------------------------------------------------------------------------------------------------------")
            choice_o = int(input("Enter the number you want to open: "))
            if choice_o == 1:
                add()
            elif choice_o == 2:
                sub()
            elif choice_o == 3:
                mul()
            elif choice_o == 4:
                div()
            elif choice_o == 5:
                floor()
            elif choice_o == 6:
                modu()
            elif choice_o == 7:
                expo()
            elif choice_o == 8:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print("\t\t---> THANK YOU FOR USING ARITHMETIC OPERATORS <---")
                print("---------------------------------------------------------------------------------------------------------------")
                break
            else:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print("\t\t---> INVALID INPUT <---")
                print("---------------------------------------------------------------------------------------------------------------")
                continue
    def relational_operators():
        os.system('cls')
        def equal_to():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> EQUAL TO "==" <---')
            print('The == operator checks if two values are equal. It returns True if the values are equal, and False otherwise.')
            print('For example:')
            print('a = 6\nb = 6')
            print('print(a == b) <--- The output will be: True')
            print('Another example:')
            print('x = 10\ny = 12')
            print('print(x == y) <--- The outpult will be: False')
            print("---------------------------------------------------------------------------------------------------------------")
        def not_equal_to():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> NOT EQUAL TO "!=" <---')
            print('The != operator checks if two values are not equal. It returns True if the values are not equal, and False otherwise.')
            print('For example:')
            print('a = 6\nb = 6')
            print('print(a != b) <--- The output will be: False')
            print('Another example:')
            print('x = 10\ny = 12')
            print('print(x != y) <--- The outpult will be: True')
            print("---------------------------------------------------------------------------------------------------------------")
        def greater_than():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> GREATER THAN ">" <---')
            print('The > operator checks if the value on the left is greater than the value on the right.') 
            print('It returns True if the left value is greater, and False otherwise.')
            print('For example:')
            print('a = 7\nb = 6')
            print('print(a > b) <--- The output will be: True')
            print('Another example:')
            print('x = 10\ny = 12')
            print('print(x > y) <--- The outpult will be: False')
            print("---------------------------------------------------------------------------------------------------------------")
        def less_than():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> LESS THAN "<" <---')
            print('The < operator checks if the value on the left is less than the value on the right') 
            print('It returns True if the left value is less, and False otherwise.')
            print('For example:')
            print('a = 5\nb = 7')
            print('print(a < b) <--- The output will be: True')
            print('Another example:')
            print('x = 10\ny = 7')
            print('print(x < y) <--- The outpult will be: False')
            print("---------------------------------------------------------------------------------------------------------------")
        def greater_equal():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> GREATER THAN OR EQUAL TO ">=" <---')
            print('The >= operator checks if the value on the left is greater than or equal to the value on the right.') 
            print('It returns True if the left value is greater than or equal, and False otherwise.')
            print('For example:')
            print('a = 7\nb = 6')
            print('print(a >= b) <--- The output will be: True')
            print('Another example:')
            print('x = 7\ny = 7')
            print('print(x >= y) <--- The outpult will be: True')
            print('Another example:')
            print('z = 2')
            print('print(z >= 5) <--- The output will be: False')
            print("---------------------------------------------------------------------------------------------------------------")
        def less_equal():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> LESS THAN OR EQUAL TO "<=" <---')
            print('The <= operator checks if the value on the left is less than or equal to the value on the right') 
            print('It returns True if the left value is less than or equal, and False otherwise.')
            print('For example:')
            print('a = 4\nb = 10')
            print('print(a <= b) <--- The output will be: True')
            print('Another example:')
            print('x = 7\ny = 7')
            print('print(x <= y) <--- The outpult will be: True')
            print('Another example:')
            print('z = 5')
            print('print(z <= 2) <--- The output will be: False')
            print("---------------------------------------------------------------------------------------------------------------")
        loop = True
        while loop == True:
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> RELATIONAL OPERATORS <---")
            print('Relational Operators are used to compare two values. The result will be True of False.')
            print('Relational Operators are often used to create test expressions that control program flow.')
            print('Commonly used in if/else function for the program to know which path it will show')
            print("---------------------------------------------------------------------------------------------------------------")
            print('1. EQUAL TO')
            print('2. NOT EQUAL TO')
            print('3. GREATER THAN')
            print('4. LESS THAN')
            print('5. GREATER THAN OR EQUAL TO')
            print('6. LESS THAN OR EQUAL TO')
            print('7. EXIT')
            print("---------------------------------------------------------------------------------------------------------------")
            choice_r = int(input('Enter the number you want to open: '))
            if choice_r == 1:
                equal_to()
            elif choice_r == 2:
                not_equal_to()
            elif choice_r == 3:
                greater_than()
            elif choice_r == 4:
                less_than()
            elif choice_r == 5:
                greater_equal()
            elif choice_r == 6:
                less_equal()
            elif choice_r == 7:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> THANK YOU FOR USING RELATIONAL OPERATORS <---')
                print("---------------------------------------------------------------------------------------------------------------")
                break
            else:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> INVALID INPUT <---')
                print("---------------------------------------------------------------------------------------------------------------")
                continue
    def logical_operators():
        os.system('cls')
        def logical_and():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> LOGICAL "AND" <---')
            print('The and operator returns True if both conditions are True. If either of the conditions is False, it returns False.')
            print('Example:')
            print('x = 5\ny = 10')
            print('print(x > 3 and y < 15) <--- The output will be: True (both conditions are True)')
            print('print(x > 3 and y > 15) <--- The output will be: False (second condition is False)')
            print("---------------------------------------------------------------------------------------------------------------")
        def logical_or():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> LOGICAL "OR" <---')
            print('The or operator returns True if at least one of the conditions is True.')
            print('If both conditions are False, it returns False.')
            print('Example:')
            print('x = 5\ny = 10')
            print('print(x > 3 or y < 15) <--- The output will be: True (first condition is True)')
            print('print(x < 3 or y > 15)  <--- The output will be: False (both conditions are False)')
            print("---------------------------------------------------------------------------------------------------------------")
        def logical_not():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> LOGICAL "NOT" <---')
            print('The not operator negates the result of a condition.')
            print("If the condition is True, not makes it False, and if the condition is False, it makes it True.")
            print('Example:')
            print('x = 5')
            print('print(not (x > 3)) <--- The output will be: False (x > 3 is True, so negating it gives False)')
            print('print(not (x < 3)) <--- The output will be: True (x < 3 is False, so negating it gives True)')
            print("---------------------------------------------------------------------------------------------------------------")
        loop = True
        while loop == True:
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> LOGICAL OPERATORS <---')
            print('Logical operators are used to combine conditional statements (expressions that evaluate to True or False).')
            print('These operators help in making more complex decisions in your programs.')
            print("---------------------------------------------------------------------------------------------------------------")
            print('1. LOGICAL "AND"')
            print('2. LOGICAL "OR"')
            print('3. LOGICAL "NOT"')
            print('4. EXIT')
            print("---------------------------------------------------------------------------------------------------------------")    
            choice_l = int(input('Enter the number you want to open: '))
            if choice_l == 1:
                logical_and()
            elif choice_l == 2:
                logical_or()
            elif choice_l == 3:
                logical_not()
            elif choice_l == 4:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> THANK YOU FOR USING LOGICAL OPERATORS <---')
                print("---------------------------------------------------------------------------------------------------------------")
                break
            else:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> INVALID INPUT <---')
                print("---------------------------------------------------------------------------------------------------------------")  
                continue         
    def assignment_operators():
        os.system('cls')
        def simple():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> SIMPLE ASSIGNMENT "=" <---')
            print('The = operator is used to assign a value to a variable.')
            print('Example:\nx = 10\ny = 5')
            print('print(x)  <--- The output will be: 10')
            print('print(y)  <--- The output will be: 5')
            print("---------------------------------------------------------------------------------------------------------------")
        def add_assign():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> ADDITION ASSIGNMENT "+=" <---')
            print('The += operator adds a value to the variable and assigns the result to that variable.')
            print('Example:')
            print('x = 10\nx += 5 <--- It is also equivalent to x = x + 5')
            print('print(x) <--- The output will be: 15')
            print("---------------------------------------------------------------------------------------------------------------")
        def sub_assign():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> SUBTRACTION ASSIGNMENT "-=" <---')
            print('The -= operator subtracts a value from the variable and assigns the result to that variable.')
            print('Example:')
            print('x = 10\nx -= 3  <--- It is also equivalent to x = x - 3')
            print('print(x) <--- The output will be: 7')
            print("---------------------------------------------------------------------------------------------------------------")
        def mul_assign():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> MULTIPLICATION ASSIGNMENT "*=" <---')
            print('The *= operator multiplies the variable by a value and assigns the result to that variable.')
            print('Example:')
            print('x = 5\nx *= 3  <--- It is also equivalent to x = x * 3')
            print('print(x) <--- The output will be: 15')
            print("---------------------------------------------------------------------------------------------------------------")
        def div_assign():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> DIVISION ASSIGNMENT "/=" <---')
            print('The /= operator divides the variable by a value and assigns the result to that variable. The result is always a float.')
            print('Example:')
            print('x = 10\nx /= 2 <--- It is also equivalent to x = x / 2')
            print('print(x) <--- The output will be: 5.0 (note that the result is a float when dividing)')
            print("---------------------------------------------------------------------------------------------------------------")
        def floor_assign():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> FLOOR DIVISION ASSIGNMENT "//=" <---')
            print('The //= operator divides the variable by a value and assigns the result to the variable.')
            print('But it performs floor division (rounds down to the nearest integer).')
            print('Example:')
            print('x = 10\nx //= 3  <--- It is also equivalent to x = x // 3')
            print('print(x) <--- The output will be: 3 (floor division)')
            print("---------------------------------------------------------------------------------------------------------------")
        def modulo_assign():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> MODULO ASSIGNMENT "%=" <---')
            print('The %= operator calculates the remainder of the division of the variable by a value and assigns the result to that variable.')
            print('Example:')
            print('x = 10\nx %= 3 <--- It is also equivalent to x = x % 3')
            print('print(x) <--- The output will be: 1 (remainder of 10 divided by 3)')
            print("---------------------------------------------------------------------------------------------------------------")
        def expo_assign():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> EXPONENTIATION ASSIGNMENT "**=" <---')
            print('The **= operator raises the variable to the power of a value and assigns the result to that variable.')
            print('Example:')
            print('x = 2\nx **= 3 <--- It is also equivalent to x = x ** 3')
            print('print(x) <--- The output will be: 8 (2 raised to the power of 3)')
            print("---------------------------------------------------------------------------------------------------------------")
        def over_example():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> OVERALL EXAMPLE OF ASSINMENT OPERATORS <---')
            print('x = 10')
            print('x += 5  <--- Now the value of x = 15')
            print('x -= 3  <--- Now the value of x = 12')
            print('x *= 2  <--- Now the value of x = 24')
            print('x /= 4  <--- Now the value of x = 6.0')
            print('x //= 2 <--- Now the value of x = 3')
            print('x %= 2  <--- Now the value of x = 1')
            print('x **= 3 <--- Now the value of x = 1')
            print("The final value of x is 1")
            print("---------------------------------------------------------------------------------------------------------------")
        loop = True
        while loop == True:
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> ASSIGNMENT OPERATORS <---')
            print('Assignment operators are used to assign values to variables.')
            print("---------------------------------------------------------------------------------------------------------------")
            print('1. SIMPLE ASSIGNMENT "="')
            print('2. ADDITION ASSIGNMENT "+="')
            print('3. SUBTRACTION ASSIGNMENT "-="')
            print('4. MULTIPLICATION ASSIGNMENT "*="')
            print('5. DIVISION ASSIGNMENT "/="')
            print('6. FLOOR DIVISION ASSIGNMENT "//="')
            print('7. MODULO ASSIGNMENT "%="')
            print('8. EXPONENTIATION ASSIGNMENT "**="')
            print('9. OVERALL ASSIGNMENT')
            print('10. EXIT')
            print("---------------------------------------------------------------------------------------------------------------")
            choice_a = int(input('Enter the number you want to open: '))
            if choice_a == 1:
                simple()
            elif choice_a == 2:
                add_assign()
            elif choice_a == 3:
                sub_assign()
            elif choice_a == 4:
                mul_assign()
            elif choice_a == 5:
                div_assign()
            elif choice_a == 6:
                floor_assign()
            elif choice_a == 7:
                modulo_assign()
            elif choice_a == 8:
                expo_assign()
            elif choice_a == 9:
                over_example()
            elif choice_a == 10:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print("\t\t---> THANK YOU FOR USING ASSIGNMENT OPERATORS <---")
                print("---------------------------------------------------------------------------------------------------------------")
                break
            else:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> INVALID INPUT <---')
                print("---------------------------------------------------------------------------------------------------------------")
                continue
    loop = True
    while loop == True:
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> OPERATORS <---')
        print('Operators are special symbols or keywords in Python that perform operations on values or variables.')
        print('They are the building blocks of programming logic.')
        print("---------------------------------------------------------------------------------------------------------------")
        print("1. ARITHMETIC OPERATORS")
        print("2. RELATIONAL OPERATORS")
        print("3. LOGICAL OPERATORS")
        print("4. ASSIGNMENT OPERATORS")
        print("5. EXIT")
        print("---------------------------------------------------------------------------------------------------------------")
        choice_operator = int(input('Enter the number you want to open: '))
        if choice_operator == 1:
            arithmetic()
        elif choice_operator == 2:
            relational_operators()
        elif choice_operator == 3:
            logical_operators()
        elif choice_operator == 4:
            assignment_operators()
        elif choice_operator == 5:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print("\t\t---> THANK YOU FOR USING OPERATORS <---")
            print("---------------------------------------------------------------------------------------------------------------")
            break
        else:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> INVALID INPUT <---')
            print("---------------------------------------------------------------------------------------------------------------")
            continue
def conditionals():
    os.system('cls')
    def if_condition():
        os.system('cls')
        def basic_if():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> BASIC IF STATEMENT <---')
            print('The if statement in Python is used to execute a block of code only if a given condition is true')
            print('Example:\nx = 10')
            print('if x > 5:')
            print('\tprint("x is greater than 5")')
            print('The output will be: x is greater than 5')
            print("---------------------------------------------------------------------------------------------------------------")
        def multi_if():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> MULTIPLE CONDITIONS USING LOGICAL OPERATORS <---')
            print('You can use logical operators like and, or, and not to combine conditions.')
            print('Example:\nx = 7')
            print('if x > 5 and x < 10:')
            print('\tprint("x is between 5 and 10")')
            print('The output will be: x is between 5 and 10 ')
            print("---------------------------------------------------------------------------------------------------------------")
        def boolean_if():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> If WITH BOOLEAN VALUES <---')
            print('Any value that evaluates to True or False can be used with an if condition.')
            print('Example:\nLet_Me_In = True')
            print('if Let_Me_In:')
            print('\tprint("Welcome, you are in!!")')
            print('The output will be: Welcome, you are in!!')
            print("---------------------------------------------------------------------------------------------------------------")
        loop = True
        while loop == True:
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t ---> IF CONDITIONS <---')
            print('The "if" statement in Python is used to execute a block of code only if a given condition is true.')
            print('If the condition evaluates to false, the code block is skipped.')
            print("---------------------------------------------------------------------------------------------------------------")
            print('1. BASIC IF STATEMENT')
            print('2. MULTIPLE CONDITIONS USING LOGICAL OPERATORS')
            print('3. If WITH BOOLEAN VALUES')
            print('4. EXIT')
            print("---------------------------------------------------------------------------------------------------------------")
            choice_if = int(input('Enter the number you want to open: '))
            if choice_if == 1:
                basic_if()
            elif choice_if == 2:
                multi_if()
            elif choice_if == 3:
                boolean_if()
            elif choice_if == 4:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> THANK YOU FOR USING IF CONDITIONS <---')
                print("---------------------------------------------------------------------------------------------------------------")
                break
            else:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> INVALID INPUT <---')
                continue
    def elif_condition():
        os.system('cls')
        def single_elif():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> SINGLE ELIF STATEMENT <---')
            print('Example:\nx = 10')
            print('if x < 5:\n\tprint("x is less than 5")')
            print('elif x == 10:\n\tprint("x is equal to 10")')
            print('else:\n\tprint("x is greater than 5 but not 10")')
            print('The output will be: x is equal to 10')
            print('*The elif will trigger because it is the one who qualified the value of x')
            print("---------------------------------------------------------------------------------------------------------------")
        def multi_elif():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> MULTIPLE ELIF STATEMENTS <---')
            print('Example:\nGWA = 85')
            print('if GWA >= 90:\n\tprint("Grade: A+")')
            print('elif GWA >= 80:\n\tprint("Grade: A")')
            print('elif marks >= 70:\n\tprint("Grade: B")')
            print('else:\n\tprint("Grade: C")')
            print('The output will be: Grade: A')
            print('"Grade: A" will trigger because the 80 qualified to the value of GWA which is 85')
            print('It says that if the value of GWA = 85 is greater than or equal to 80: the output will be True and will trigger the elif condition')
            print("---------------------------------------------------------------------------------------------------------------")
        def combine():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> COMBINING IF, ELSE, ELIF STATEMENTS <---')
            print('Example:\nnumber = -3')
            print('if number > 0:\n\tprint("Positive number")')
            print('elif number == 0:\n\tprint("Zero")')
            print('else:\n\tprint("Negative number")')
            print('The output will be: Negative number')
            print('The "else" will trigger because if and elif statements given are equals to false')
            print("---------------------------------------------------------------------------------------------------------------")
        def nested_elif():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> NESTED ELIF STATEMENTS <---')
            print('You can nest if-elif statements if needed, though too much nesting can make the code harder to read.')
            print('Example:\n\tage = 20\n\thas_ticket = True')
            print('if age >= 18:\n\tif has_ticket:\n\t\tprint("Allowed entry")')
            print('\telse:\n\t\tprint("No ticket, no entry")')
            print('elif age < 18:\n\tprint("Underage")')
            print('The output will be: Allowed entry')
            print('It will be the output because the if will qualify the statement and') 
            print('the nested if that is has_ticket will trigger because it is equals to True')
            print("---------------------------------------------------------------------------------------------------------------")
        loop = True
        while loop == True:
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> ELIF CONDITIONS <---')
            print('- The elif statement in Python stands for "else if."')  
            print('- It is used to test additional conditions after the initial if condition.') 
            print('- If the if condition is false, Python will evaluate the elif conditions in order.')   
            print('- Once a true condition is found, the corresponding block of code is executed, and the remaining conditions are ignored.')
            print("---------------------------------------------------------------------------------------------------------------")
            print('1. SINGLE ELIF STATEMENTS')
            print('2. MULTIPLE ELIF STATEMENTS')
            print('3. COMBINED IF,ELIF,ELSE STATEMENTS')
            print('4. NESTED ELIF STATEMENTS')
            print('5. EXIT')
            choice_e = int(input('Enter the number you want to open: '))
            if choice_e == 1:
                single_elif()
            elif choice_e == 2:
                multi_elif()
            elif choice_e == 3:
                combine()
            elif choice_e == 4:
                nested_elif()
            elif choice_e == 5:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> THANK YOU FOR USING ELIF CONDITIONS <---')
                print("---------------------------------------------------------------------------------------------------------------")
                break
            else:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> INVALID INPUT <---')
                print("---------------------------------------------------------------------------------------------------------------")
                continue       
    def else_condition():       
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> ELSE CONDITIONS <---')
        print('- "else" runs when all other conditions are false.')
        print('- It is optional and acts as a "default" case.')
        print('Example:\nx = 0')
        print('if x > 0:\n\tprint("Positive")')
        print('elif x < 0:\n\tprint("Negative")')
        print('else:\n\tprint("Zero")')
        print('The output will be: Zero <--- Because if and elif statements are both false that is why the else statement will trigger')
        print("---------------------------------------------------------------------------------------------------------------")
    loop = True
    while loop == True:
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> CONDITIONALS <---')
        print('- Conditionals allow you to execute specific blocks of code based on whether a condition is true or false.')
        print('- They use the if, elif, and else keywords.')
        print("---------------------------------------------------------------------------------------------------------------")
        print('1. IF CONDITIONS')
        print('2. ELIF CONDITIONS')
        print('3. ELSE CONDITIONS')
        print('4. EXIT')
        choice_cons = int(input('Enter the number you want to open: '))
        if choice_cons == 1:
            if_condition()
        elif choice_cons == 2:
            elif_condition()
        elif choice_cons == 3:
            else_condition()
        elif choice_cons == 4:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> THANK YOU FOR USING CONDITIONALS <---')
            print("---------------------------------------------------------------------------------------------------------------")
            break
        else:
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> INVALID INPUT <---')
            print("---------------------------------------------------------------------------------------------------------------")
            continue
def loops():
    os.system('cls')
    def for_loop():
        os.system('cls')
        def iterating_list():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> ITERATING OVER A LIST <---')
            print('Example:')
            print("fruits = ['apple', 'banana', 'cherry']")
            print('for fruit in fruits:\n\tprint(fruit)')
            print('The output will be:\napple\nbanana\ncherry')
            print("The for loop starts by taking the first element of the fruits list ('apple') and assigns it to the variable fruit.")
            print("It then moves to the second element ('banana'), and then the third ('cherry'), repeating the block of code each time.")
            print("---------------------------------------------------------------------------------------------------------------")
        def range_loops():
            os.system('cls')
            def incremental_range():
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> INCREMENTAL <---')
                print('Example:')
                print('for x in range(1,5):\n\tprint(x)')
                print('It will starts at 1, 1 is the starting point and the 5 will be the stopping point')
                print('It will stop at the 4 by default because it is programmed like that')
                print('The output will be:\n1\n2\n3\n4')
                print('the output will be on a new line one by one')
                print("---------------------------------------------------------------------------------------------------------------")
            def decremental_range():
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> DECREMENTAL <---')
                print('Decremental is the same as incremental but it count backwards')
                print('Example: ')
                print('for x in range(5, 0, -1):\n\tprint(x)')
                print('The 5 will be the starting point, the 0 will be the stopping point and the -1 is the step for the loop to count backwards')
                print('The output will be:\n5\n4\n3\n2\n1')
                print('The output will be on every new line one by one')
                print("---------------------------------------------------------------------------------------------------------------")
            loop = True
            while loop == True:
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> USING RANGE <---')
                print('The range() function in Python generates a sequence of numbers.')
                print('It is commonly used in loops to repeat an action for a set number of times or iterate through numbers in a specific pattern.')
                print("---------------------------------------------------------------------------------------------------------------")
                print('1. INCREMENTAL for loop')
                print('2. DECREMENTAL for loop')
                print('3. EXIT')
                print("---------------------------------------------------------------------------------------------------------------")
                choice_loop = int(input('Enter the number you want to open: '))
                if choice_loop == 1:
                    incremental_range()
                elif choice_loop == 2:
                    decremental_range()
                elif choice_loop == 3:
                    os.system('cls')
                    print("---------------------------------------------------------------------------------------------------------------")
                    print('\t\t---> THANK YOU FOR USING RANGE <---')
                    print("---------------------------------------------------------------------------------------------------------------")
                    break
                else:
                    os.system('cls')
                    print("---------------------------------------------------------------------------------------------------------------")
                    print('\t\t---> INVALID INPUT <---')
                    print("---------------------------------------------------------------------------------------------------------------")
                    continue
        def while_loops():    
            os.system('cls')
            def simple_while():
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> WHILE LOOP <---')
                print('Example:\nbilang = 0')
                print('while count < 5:  <--- Loop runs as long as bilang is less than 5\n\tprint(count)\n\tcount += 1  <--- Increment count by 1')
                print('- The while loop checks if count < 5')
                print('- If True, it prints the value of bilang and then increases count by 1 (count += 1).')
                print('- This continues until bilang becomes 5, at which point the condition count < 5 is False, and the loop stops.')
                print('The output will be:\n0\n1\n2\n3\n4')
                print("---------------------------------------------------------------------------------------------------------------")
            def break_continue():
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> WHILE LOOP WITH BREAK AND CONTINUE <---')
                print('break: Exits the loop completely, even if the condition is still True.')
                print('continue: Skips the current iteration and jumps to the next one.')
                print('Example:\nbilang = 0')
                print('while bilang < 5:\n\tbilang += 1\n\tif count == 3:')
                print('\t\tcontinue <--- Skip the print statement when count is 3')
                print('\tif count == 4:\n\t\tbreak <--- Exit the loop when count is 4')
                print('\tprint(count)')
                print('When count == 3, the continue skips printing.\nWhen count == 4, the break exits the loop.')
                print('The output will be:\n1\n2')
                print("---------------------------------------------------------------------------------------------------------------")
            loop = True
            while loop == True:
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> WHILE LOOP <---')
                print('- A while loop repeatedly executes a block of code as long as a condition is True. ')
                print('- Once the condition becomes False, the loop stops running.')
                print("---------------------------------------------------------------------------------------------------------------")
                print('1. SIMPLE WHILE LOOP')
                print('2. WHILE LOOP WITH BREAK AND CONTINUE')
                print('3. EXIT')
                print("---------------------------------------------------------------------------------------------------------------")
                choice_w = int(input('Enter the number you want to open: '))
                if choice_w == 1:
                    simple_while()
                elif choice_w == 2:
                    break_continue()
                elif choice_w == 3:
                    os.system('cls')
                    print("---------------------------------------------------------------------------------------------------------------")
                    print('\t\t---> THANK YOU FOR USING WHILE LOOP <---')
                    print("---------------------------------------------------------------------------------------------------------------")
                    break
                else:
                    os.system('cls')
                    print("---------------------------------------------------------------------------------------------------------------")
                    print('\t\t---> INVALID INPUT <---')
                    print("---------------------------------------------------------------------------------------------------------------")
                    continue
        loop = True
        while loop == True:
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> FOR LOOPS <---')
            print('The for loop is used for iterating over a sequence')
            print("---------------------------------------------------------------------------------------------------------------")
            print('1. ITERATING OVER A LIST')
            print('2. RANGE')
            print('3. WHILE LOOP')
            print('4. EXIT')
            print("---------------------------------------------------------------------------------------------------------------")
            choice_lp = int(input('Enter the number you want to open: '))
            if choice_lp == 1:
                iterating_list()
            elif choice_lp == 2:
                range_loops()
            elif choice_lp == 3:
                while_loops()
            elif choice_lp == 4:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> THANK YOU FOR USING FOR LOOPS <---')
                print("---------------------------------------------------------------------------------------------------------------")
                break
            elif choice_lp == 2:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> INVALID INPUT <---')
                print("---------------------------------------------------------------------------------------------------------------")
                continue
    def nested_loop():
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------------------")
        print('--> NESTED FOR LOOP SIMPLIED <---')
        print('Example:')
        print('for x in range(1,3):\n\tfor y in range(1,5):\n\t\tprint("*")')
        print('for x in range(1, 3): <---- will be the outer loop: x goes from 1 to 2')
        print('for y in range(1, 3):  <---- will be Inner loop: y goes from 1 to 2')
        print('print("*")  will prints an asterisk symbol on each iteration')
        print('Explanation:')
        print('The outer loop (for x in range(1, 3)) runs 2 times. It starts at x = 1 and goes until x = 2')
        print('For each iteration of the outer loop, the inner loop (for y in range(1, 2)) also runs 2 times.')
        print('It starts at y = 1 and goes until y = 2)')
        print('The print("*") inside the inner loop prints an askterisk (*) for each iteration of the inner loop.')
        print('The output will be:')
        for x in range(1,3):
            for y in range(1,3):
                print("*")
        print("---------------------------------------------------------------------------------------------------------------")
    loop = True
    while loop == True:
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> LOOPS <---')
        print('Loops are used to repeatedly execute a block of code as long as a condition is met or for a fixed number of iterations.')
        print("---------------------------------------------------------------------------------------------------------------")
        print('1. FOR LOOP')
        print('2. NESTED FOR LOOP')
        print('3. EXIT')
        print("---------------------------------------------------------------------------------------------------------------")
        choice_loop = int(input('Enter the number you want to open: '))
        if choice_loop == 1:
            for_loop()
        elif choice_loop == 2:
            nested_loop()
        elif choice_loop == 3:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> THANK YOU FOR USING LOOPS <---')
            print("---------------------------------------------------------------------------------------------------------------")
            break
        else:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> INVALID INPUT <---')
            print("---------------------------------------------------------------------------------------------------------------")
            continue
def lists():
    os.system('cls')
    def create_list():
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> CREATING A LIST <---')
        print('Example: ')
        print('my_list = [1, 2, 3, 4, 5]  <--- List of Numbers')
        print('fruits = ["apple", "banana", "cherry"] <----list of words')
        my_list = [1, 2, 3, 4, 5]
        fruits = ["apple", "banana", "cherry"]
        print('print(my_list)')
        print(f"The output will be:\n{my_list}")
        print('print(fruits)')
        print(f'The output will be:\n{fruits}')
        print("---------------------------------------------------------------------------------------------------------------")
    def what_list():
        os.system('cls')
        def add_list():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> ADD SOMETHING IN THE LIST <---')
            print('fruits = ["apple", "banana", "cherry"]')
            fruits = ["apple", "banana", "cherry"]
            print('fruits.append("orange")  will add "orange" to the end')
            fruits.append("orange")
            print('print(fruits)')
            print('The output will be:')
            print(fruits)
            print("---------------------------------------------------------------------------------------------------------------")
        def remove_list():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> REMOVE SOMETHING IN THE LIST <---')
            print('fruits = ["apple", "banana", "cherry"]')
            fruits = ["apple", "banana", "cherry"]
            print('fruits.remove("banana")  will remove "banana"')
            fruits.remove("banana")
            print('print(fruits)')
            print('The output will be:')
            print(fruits)
            print("---------------------------------------------------------------------------------------------------------------")
        def go_through():
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> GO THROUGH EVERYTHING IN THE LIST <---')
            print('fruits = ["apple", "banana", "cherry"]')
            fruits = ["apple", "banana", "cherry"]
            print('for fruit in fruits:\n\tprint(fruit)')
            print('The output will be:')
            for fruit in fruits:
                print(fruit)
            print("---------------------------------------------------------------------------------------------------------------")
        loop = True
        while loop == True:
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> WHAT CAN YOU DO WITH A LIST <---')
            print("---------------------------------------------------------------------------------------------------------------")
            print('1. ADD SOMETHING IN THE LIST')
            print('2. REMOVE SOMETHING IN THE LIST')
            print('3. GO THROUGH IN THE LIST')
            print('4. EXIT')
            print("---------------------------------------------------------------------------------------------------------------")
            list_choice = int(input('Enter the number you want to open: '))
            if list_choice == 1:
                add_list()
            elif list_choice == 2:
                remove_list()
            elif list_choice == 3:
                go_through()
            elif list_choice == 4:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> THANK YOU FOR USING WHAT CAN YOU DO WITH A LIST <---')
                print("---------------------------------------------------------------------------------------------------------------")
                break
            else:
                os.system('cls')
                print("---------------------------------------------------------------------------------------------------------------")
                print('\t\t---> INVALID INPUT <---')
                print("---------------------------------------------------------------------------------------------------------------")
                continue
    loop = True
    while loop == True:
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> LIST <---')
        print('A list is a built-in data structure that allows you to store an ordered, mutable collection of elements.')
        print("---------------------------------------------------------------------------------------------------------------")
        print("1. HOW CREATE A LIST")
        print('2. WHAT CAN YOU DO WITH A LIST')
        print('3. EXIT')
        print("---------------------------------------------------------------------------------------------------------------")
        list_choice1 = int(input('Enter the number you want to open: '))
        if list_choice1 == 1:
            create_list()
        elif list_choice1 == 2:
            what_list()
        elif list_choice1 == 3:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t ---> THANK YOU FOR USING LIST <---')
            print("---------------------------------------------------------------------------------------------------------------")
            break
        else:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t ---> INVALID INPUT <---')
            print("---------------------------------------------------------------------------------------------------------------")
            continue
def functions():
    os.system('cls')
    def creating_def():
        os.system('cls')
        print('\t\t---> CREATING A FUNCTIONS <---')
        print("---------------------------------------------------------------------------------------------------------------")
        print('In Python a function is defined using the "def" keyword')
        print('Example:')
        print('def say_hello():\n\tprint("Hello, world!")')
        print("---------------------------------------------------------------------------------------------------------------")
    def calling_def():
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> CALLING A FUNCTION <---')
        print('- To use a function, write its name followed by parentheses.')
        print('Example:')
        print('def say_hello():\n\tprint("Hello, world!")')
        print('say_hello() <--- USED TO CALL A FUNCTION')
        print('The output will be:\nHello, world!')
        print("---------------------------------------------------------------------------------------------------------------")
    def function_para():
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> FUNCTION WITH PARAMETERS <---')
        print('- Parameters are like "inputs" for your function. They make the function flexible.')
        print('Example:')
        print('def greet(name):\n\tprint(f"Hello, {name}!")')
        print('greet("GOKU") <--- USED TO CALL A FUNCTION')
        print('The output will be:\nHello, GOKU!')
        print("---------------------------------------------------------------------------------------------------------------")
    def return_values():
        os.system('cls')
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> RETURN VALUES <---')
        print('- Sometimes, a function gives something back (a result).')
        print('Example:')
        print('def add_numbers(a, b):\n\treturn a + b')
        print('result = add_numbers(3, 5)\nprint(result) <--- USED TO CALL A FUNCTION')
        print('The output will be: 8')
        print("---------------------------------------------------------------------------------------------------------------")
    loop = True
    while loop == True: 
        print("---------------------------------------------------------------------------------------------------------------")
        print('\t\t---> FUNCTIONS <---')
        print('A function is a block of code which only runs when it is called.')
        print('You can pass data, known as parameters, into a function.')
        print('A function can return data as a result.')
        print("---------------------------------------------------------------------------------------------------------------")
        print('1. CREATING A FUNCTIONS')
        print('2. CALLING A FUNCTION')
        print('3. FUNCTION WITH PARAMETERS')
        print('4. RETURN VALUES')
        print('5. EXIT')
        print("---------------------------------------------------------------------------------------------------------------")
        function_choice = int(input('Enter the number you want to open: '))
        if function_choice == 1:
            creating_def()
        elif function_choice == 2:
            calling_def()
        elif function_choice == 3:
            function_para()
        elif function_choice == 4:
            return_values()
        elif function_choice == 5:
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> THANK YOU FOR USING FUNCTIONS <---')
            print("---------------------------------------------------------------------------------------------------------------")
            break
        else: 
            os.system('cls')
            print("---------------------------------------------------------------------------------------------------------------")
            print('\t\t---> INVALID INPUT <---')
            print("---------------------------------------------------------------------------------------------------------------")
            continue
loop = True
while loop == True:
    print("\t\t***********************************************************************************************")
    print("\t\t\t\t---> WELCOME TO FRANCO BERIÑA'S FINAL PROJECT <---")
    print("\t\t---> THIS IS A PROGRAM THAT CONTAINS A BRIEF SUMMARY OF THE BASICS TOPICS OF PYTHON <---")
    print("\t\t\t---> THIS IS ALSO A SHORT RECALL ON WHAT TOPICS I'VE MASTERED A LITTLE <---")
    print("\t\t***********************************************************************************************")
    print('1. PRINT STATEMENTS')
    print('2. VARIABLES')
    print('3. OPERATORS')
    print('4. CONDITIONALS')
    print('5. LOOPS')
    print('6. LISTS')
    print('7. FUNCTIONS')
    print('8. EXIT')
    choice_04 = int(input('Enter the number you want to open:'))
    if choice_04 == 1:
        print_statements()
    elif choice_04 == 2:
        variables()
    elif choice_04 == 3:
        operators()
    elif choice_04 == 4:
        conditionals()
    elif choice_04 == 5:
        loops()
    elif choice_04 == 6:
        lists()
    elif choice_04 == 7:
        functions()
    elif choice_04 == 8:
        os.system('cls')
        print('\t\t\t---> THANK YOU FOR USING MY FINAL PROJECT <---')
        break
    else:
        os.system('cls')
        print('\t\t\t---> INVALID INPUT <---')
        continue