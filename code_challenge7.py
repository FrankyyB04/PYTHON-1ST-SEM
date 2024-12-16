#Minus discount nga po pala sa taxed item dun po ako tumagal HAHAHHAHAHA
#16HRS ginawa :((

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