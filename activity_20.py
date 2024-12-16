import os
fruits = []
loop = True
while loop == True:
    ad_fruits = str(input("Enter a fruit you want to add (type 'none' if you are satisfied, type 'remove' if you want to delete an item): "))
    if ad_fruits == "none":
        os.system('cls')
        print(f"Your final fruits are: {fruits} ")
        break
    elif ad_fruits == "remove":
        rmv = str(input("Enter the fruit you want to remove: "))
        for item in fruits:
            if item == rmv:
                os.system('cls')
                fruits.remove(item)
                print(f"Your final fruits are: {fruits} ")
            else:
                print(f"Your final fruits are: {fruits} ")
                break
    else:
        os.system('cls')
        fruits.append(ad_fruits)
        print(f"Your fruits are: {fruits} ")
        continue  
print("---------------------------------------------------------------------------------------------------------------")
